#!/usr/bin/env python3
"""Read-only convention checks for a skills-only plugin repository (Python 3.10+)."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')


def validate(root):
    errors, skills = [], []
    try:
        import yaml
    except ImportError:
        return {'ok': False, 'errors': ['Missing PyYAML; install requirements.txt.'], 'skills': []}
    root = Path(root).resolve()

    def check(condition, message):
        if not condition:
            errors.append(message)

    def valid_name(value):
        return isinstance(value, str) and len(value) <= 64 and bool(NAME.fullmatch(value))

    def read_json(path):
        try:
            value = json.loads(path.read_text())
            if not isinstance(value, dict):
                raise ValueError('expected a JSON object')
            return value
        except (OSError, ValueError) as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')
            return {}

    # Reject symlinks before reading/hashing; do not follow links outside the package.
    links = [p for p in root.rglob('*') if '.git' not in p.parts and p.is_symlink()]
    if links:
        return {'ok': False, 'errors': [f'Unsupported symlink: {p.relative_to(root)}' for p in links], 'skills': []}
    manifest = read_json(root / 'plugin.json')
    name = manifest.get('name')
    check(valid_name(name), 'Invalid plugin name')
    check(isinstance(manifest.get('description'), str) and bool(manifest['description'].strip()), 'Missing plugin description')
    check(bool(re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?', str(manifest.get('version', '')))), 'Invalid plugin version')
    directories = sorted(p for p in (root / 'skills').glob('*') if p.is_dir())
    check(bool(directories), 'No skill directories found')
    for directory in directories:
        label = str((directory / 'SKILL.md').relative_to(root))
        try:
            raw = (directory / 'SKILL.md').read_text()
            parts = re.split(r'^---\s*$', raw, maxsplit=2, flags=re.MULTILINE)
            if len(parts) != 3 or parts[0].strip():
                raise ValueError('expected YAML frontmatter at start')
            metadata = yaml.safe_load(parts[1])
            if not isinstance(metadata, dict):
                raise ValueError('frontmatter must be a mapping')
            skill_name = metadata.get('name')
            check(valid_name(skill_name), f'{label}: invalid name')
            check(skill_name == directory.name, f'{label}: folder/name mismatch')
            check(isinstance(metadata.get('description'), str) and bool(metadata['description'].strip()), f'{label}: missing description')
            check(bool(parts[2].strip()), f'{label}: empty instructions')
            for target in re.findall(r'\]\(([^)\s]+)\)', parts[2]):
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                    continue
                linked = (directory / target.split('#')[0]).resolve()
                check(linked.is_relative_to(directory.resolve()) and linked.is_file(), f'{label}: missing or escaping reference {target}')
            hashes = {str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in sorted(directory.rglob('*')) if p.is_file()}
            skills.append({'name': skill_name, 'files_sha256': hashes})
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f'{label}: {exc}')
    market_path = root / '.agents/plugins/marketplace.json'
    if market_path.exists():
        market = read_json(market_path)
        entries = market.get('plugins', [])
        check(valid_name(market.get('name')), 'Invalid marketplace name')
        check(isinstance(entries, list) and len(entries) == 1, 'Expected one root plugin marketplace entry')
        if isinstance(entries, list) and len(entries) == 1:
            entry = entries[0]
            check(isinstance(entry, dict) and entry.get('name') == name, 'Marketplace/plugin name mismatch')
            check(isinstance(entry, dict) and entry.get('source') == {'source': 'local', 'path': './'}, 'Expected local ./ marketplace source')
    return {'ok': not errors, 'scope': 'Static convention checks only; no full schema, security, installation, or runtime verification.', 'errors': errors, 'skills': skills}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    result = validate(parser.parse_args().root)
    print(json.dumps(result, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())

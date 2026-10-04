#!/usr/bin/env python3
"""Build a cloud plugin archive from reviewed repository source."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from pathlib import PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?\Z")


def build(plugin: str, skills: list[str], destination: Path) -> Path:
    if not NAME.fullmatch(plugin) or any(not NAME.fullmatch(name) for name in skills):
        raise ValueError("plugin and skill names must be lowercase hyphenated names")
    manifest_path = ROOT / "plugins" / plugin / "plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("name") != plugin or not VERSION.fullmatch(str(manifest.get("version", ""))):
        raise ValueError("manifest name or semantic version is invalid")
    # The reviewed file list is build metadata, not part of the installed plugin.
    # New files in a skill folder do not silently enter a public archive.
    file_list = json.loads((manifest_path.parent / "package-files.json").read_text(encoding="utf-8"))
    if not isinstance(file_list, list) or any(not isinstance(path, str) for path in file_list):
        raise ValueError("package-files.json must be a list of reviewed source paths")
    if len(file_list) != len(set(file_list)) or "LICENSE" not in file_list:
        raise ValueError("reviewed file list must be unique and include the root LICENSE")
    listed_skills = {PurePosixPath(path).parts[1] for path in file_list if len(PurePosixPath(path).parts) > 2 and PurePosixPath(path).parts[0] == "skills"}
    if listed_skills != set(skills):
        raise ValueError("requested skills must match the reviewed package file list")
    entries = [("plugin.json", manifest_path)]
    apps_file = manifest.get("extensions", {}).get("com.openai", {}).get("apps")
    if apps_file:
        if apps_file != "./.app.json":
            raise ValueError("app mapping must be ./.app.json")
        apps_path = manifest_path.parent / ".app.json"
        apps = json.loads(apps_path.read_text(encoding="utf-8")).get("apps", {})
        if not apps or any(not isinstance(app, dict) or not re.fullmatch(r"(?:asdk_app_|connector_|templated_apps_)[a-zA-Z0-9_]+", str(app.get("id", ""))) for app in apps.values()):
            raise ValueError("app mapping must reference registered app IDs")
        entries.append((".app.json", apps_path))
    for name in skills:
        if f"skills/{name}/SKILL.md" not in file_list:
            raise ValueError(f"missing reviewed skills/{name}/SKILL.md")
    for relative in sorted(file_list):
        parsed = PurePosixPath(relative)
        if parsed.is_absolute() or ".." in parsed.parts or relative != parsed.as_posix():
            raise ValueError("reviewed paths must be canonical relative paths")
        path = ROOT / relative
        if any(parent.is_symlink() for parent in (path, *path.parents) if parent != ROOT):
            raise ValueError(f"symlink not supported: {relative}")
        if not path.is_file() or not path.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError(f"missing or escaping reviewed file: {relative}")
        entries.append((relative, path))
    archive_names = [name for name, _ in entries]
    if len(archive_names) != len(set(archive_names)):
        raise ValueError("reviewed files collide with reserved archive names")
    for archive_name, source in entries:
        if any(parent.is_symlink() for parent in (source, *source.parents) if parent != ROOT):
            raise ValueError(f"symlink not supported: {archive_name}")
        if not source.is_file() or not source.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError(f"missing or escaping archive input: {archive_name}")
    destination.mkdir(parents=True, exist_ok=True)
    output = destination / f"{plugin}-{manifest['version']}.zip"
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for archive_name, source in entries:
            info = ZipInfo(archive_name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    print(f"{output}  sha256={hashlib.sha256(output.read_bytes()).hexdigest()}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin")
    parser.add_argument("--skills", nargs="+", help="skill folder names; defaults to the reviewed package file list")
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    try:
        if not NAME.fullmatch(args.plugin):
            raise ValueError("plugin name must be a lowercase hyphenated name")
        reviewed = json.loads((ROOT / "plugins" / args.plugin / "package-files.json").read_text(encoding="utf-8"))
        if not isinstance(reviewed, list) or any(not isinstance(path, str) for path in reviewed):
            raise ValueError("package-files.json must be a list of reviewed source paths")
        skills = args.skills or sorted({PurePosixPath(path).parts[1] for path in reviewed if len(PurePosixPath(path).parts) > 2 and PurePosixPath(path).parts[0] == "skills"})
        build(args.plugin, skills, args.output)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Cannot build plugin: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

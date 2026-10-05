#!/usr/bin/env python3
"""Validate harness configuration or render a pinned task prompt; no network or writes."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

PROTECTED = {'send_email', 'send_messages', 'delete_data', 'change_access', 'purchase',
             'book_or_reschedule', 'accept_terms', 'publish_public_content'}
ROLES = {'daily': ('outer-harness', 'daily'),
         'completion-watch': ('outer-harness', 'completion-watch'),
         'knowledge': ('outer-harness', 'knowledge'),
         'audit': ('harness-audit', None)}
REPO = re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z')
SHA = re.compile(r'[0-9a-f]{40}\Z')


def validate(config):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    if not isinstance(config, dict):
        return ['configuration must be an object']
    for section in ('transport','accounts','sources','policies','permissions','portfolio','notifications','deployment'):
        require(isinstance(config.get(section), dict), f'{section} must be an object')
    if errors:
        return errors
    require(type(config.get('schema_version')) is int and config['schema_version'] == 1, 'schema_version must be 1')
    try:
        ZoneInfo(config.get('timezone', ''))
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        errors.append('timezone must be a valid IANA timezone')
    require(config['transport'].get('mode') == 'mcp_only', 'version 1 supports mcp_only transport')
    require(isinstance(config['accounts'].get('assistant_google'), str) and bool(re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', config['accounts'].get('assistant_google', ''))), 'assistant_google must be an explicit email address')
    require(config['accounts'].get('personal_google_access') is False, 'version 1 does not authorize personal Google account access')
    for role, provider in [('projects','trello'),('knowledge','github'),('documents','google_drive'),('calendar','google_calendar')]:
        value = config['sources'].get(role)
        require(isinstance(value, dict) and value.get('provider') == provider, f'sources.{role} requires {provider}')
    if errors:
        return errors
    def url(value, host, prefix, label):
        if not isinstance(value, str):
            errors.append(f'{label} must be an HTTPS URL')
            return
        parsed = urlparse(value)
        require(parsed.scheme == 'https' and parsed.hostname == host and parsed.path.startswith(prefix) and not parsed.username and not parsed.password and not parsed.query and not parsed.fragment, f'{label} must be a canonical HTTPS URL without credentials/query/fragment')
    url(config['sources']['projects'].get('url'), 'trello.com', '/b/', 'projects.url')
    require(bool(REPO.fullmatch(str(config['sources']['knowledge'].get('repository','')))), 'knowledge.repository must be owner/repo')
    require(isinstance(config['sources']['documents'].get('default_folder_id'), str) and bool(config['sources']['documents']['default_folder_id'].strip()), 'documents.default_folder_id is required')
    require(config['sources']['calendar'].get('scope') == 'assistant_managed_only', 'calendar scope must be assistant_managed_only')
    for name in ('portfolio','knowledge_rules','knowledge_workflow','checkpoint'):
        policy = config['policies'].get(name)
        require(isinstance(policy, dict), f'policies.{name} is required')
        if not isinstance(policy, dict):
            continue
        if name == 'portfolio':
            url(policy.get('url'), 'docs.google.com', '/document/d/', 'policies.portfolio.url')
        else:
            require(bool(REPO.fullmatch(str(policy.get('repository','')))), f'policies.{name}.repository is invalid')
            path = policy.get('path')
            require(isinstance(path, str) and bool(path) and not path.startswith('/') and '..' not in Path(path).parts, f'policies.{name}.path is invalid')
    for name in ('project_updates','knowledge_updates','document_organization','calendar_record_confirmed_commitments'):
        require(type(config['permissions'].get(name)) is bool, f'permissions.{name} must be boolean')
    protected = config['permissions'].get('requires_explicit_approval')
    require(isinstance(protected, list) and all(isinstance(x,str) for x in protected) and PROTECTED.issubset(set(protected)), 'protected actions must retain explicit approval')
    for name in ('wip_active','wip_ready'):
        require(type(config['portfolio'].get(name)) is int and config['portfolio'][name] > 0, f'portfolio.{name} must be a positive integer')
    require(config['portfolio'].get('weekly_review_day') in {'MO','TU','WE','TH','FR','SA','SU'}, 'weekly_review_day is invalid')
    require(config['notifications'].get('errors') == 'report_all', 'errors must be report_all')
    require(config['notifications'].get('routine_maintenance_success') == 'silent', 'routine maintenance must remain silent')
    require(config['notifications'].get('daily_brief') == 'always', 'daily_brief must be always')
    require(bool(REPO.fullmatch(str(config['deployment'].get('repository','')))), 'deployment.repository is invalid')
    require(bool(SHA.fullmatch(str(config['deployment'].get('ref','')))), 'deployment.ref must pin a full commit SHA')
    require(config['deployment'].get('plugin') == 'assistant-harness', 'deployment.plugin must be assistant-harness')
    require(bool(re.fullmatch(r'\d+\.\d+\.\d+', str(config['deployment'].get('version','')))), 'deployment.version must be semantic')
    registry = config.get('task_registry')
    require(isinstance(registry,list), 'task_registry must be an array')
    if isinstance(registry,list):
        ids = [item.get('id') for item in registry if isinstance(item,dict)]
        require(len(ids) == len(registry) and all(isinstance(x,str) and x for x in ids) and len(ids) == len(set(ids)), 'task registry must contain unique explicit IDs')
    def secrets(value):
        if isinstance(value,dict):
            for key,child in value.items():
                if re.search(r'(^|_)(password|secret|token|api_key|credential)(s|$|_)', key, re.I):
                    errors.append(f'credential field is prohibited: {key}')
                secrets(child)
        elif isinstance(value,list):
            for child in value:
                secrets(child)
    secrets(config)
    return errors


def render(config, locator, role):
    errors = validate(config)
    if errors:
        raise ValueError('; '.join(errors))
    parsed = urlparse(locator)
    if parsed.scheme != 'https' or parsed.hostname != 'github.com' or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError('config locator must be a canonical GitHub HTTPS URL')
    expected = f"/{config['sources']['knowledge']['repository']}/blob/"
    if not parsed.path.startswith(expected) or not parsed.path.endswith('.json'):
        raise ValueError('config locator must identify JSON in the configured private knowledge repository')
    skill, mode = ROLES[role]
    source = config['deployment']
    if skill == 'outer-harness':
        source = {**source, 'ref': source.get('unified_entry_point', {}).get('source_ref', source['ref'])}
    result = f"Run ${skill} with config_locator={locator}"
    if mode:
        result += f" and mode={mode}"
    result += '.\n\n'
    result += (f"Discover and read the installed skill through its native reader. If unavailable or stale compared with the configured policy/release, use the connected GitHub tool to fetch skills/{skill}/SKILL.md from {source['repository']} at ref {source['ref']} and follow those actual loaded instructions. Fetch and read the private config and its required current policies/checkpoint before acting. If any required load fails, report the exact operation/error, leave dependent writes pending and do not advance progress. Do not reconstruct instructions from memory.\n\n"
               'Use connected MCP tools only and the configured assistant account. Preserve action permissions and source-system boundaries. Verify every write by readback. Report all errors. Do not create replacement jobs, change schedules or reactivate disabled tasks.\n')
    if skill == 'outer-harness':
        workflow = 'knowledge' if role == 'knowledge' else 'projects'
        result += (f'Read skills/outer-harness/references/configuration.md, references/{workflow}.md and references/scheduled-tasks.md through the native reader and connected GitHub at the same source ref before dependent effects. Missing required references stop dependent writes.\n')
    result += ('Keep Trello absent by default outside daily or explicitly requested portfolio review. Use the smallest relevant source; narrow completion/reconciliation reads only relevant cards and bounded discovery. Record only material project-state changes at meaningful stopping points and read writes back. Keep concise reusable knowledge in the knowledge repository, substantial documents in Drive, implementation/checkpoints in project repositories, and operational state in its configured owning manager (Linear for migrated delivery; Trello for portfolio/life and non-migrated work).\n')
    if role == 'daily':
        result += 'Send the configured compact daily briefing; perform the policy’s deeper weekly review on the configured local weekday.\n'
    else:
        result += 'Keep routine success/no change silent; surface necessary decisions and concrete failures.\n'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config',type=Path)
    parser.add_argument('--render',choices=ROLES)
    parser.add_argument('--locator')
    args = parser.parse_args()
    try:
        config = json.loads(args.config.read_text())
        errors = validate(config)
        if errors:
            raise ValueError('; '.join(errors))
        if args.render:
            if not args.locator:
                raise ValueError('--locator is required when rendering')
            print(render(config,args.locator,args.render),end='')
        else:
            print('Configuration valid; this does not grant authority or verify connected accounts.')
    except (OSError,ValueError,KeyError) as exc:
        print(f'Cannot use configuration: {exc}',file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

---
name: chatgpt-plugin-factory
description: Build, update, validate, install, and verify reusable ChatGPT Work skills and portable skills-only plugin packages. Use when turning a workflow into an installed skill, releasing a skill repository, or diagnosing package versus runtime availability.
---

# chatgpt-plugin-factory

Turn a concrete repeated workflow into the smallest useful skill package. Prefer updating an existing skill over creating a duplicate. Maintain one canonical set of instructions in the user's chosen repository, with thin host packaging where necessary.

For the outer harness and general assistant utilities, use `https://github.com/phinneywood/outer-harness` as the reviewed source and release history. Keep product integrations beside their products: Long Form in `phinneywood/long-form`, and Strategy Factory companions in `phinneywood/strategy-factory`. Consult `phinneywood/chatgpt-plugins` for pre-split release history; follow each repository's current integration index during the transition. Keep the managed personal-skill installation and any uploaded cloud plugin release in sync explicitly; neither updates from GitHub automatically.

## Release workflow

1. Establish the task, target host and conversation mode, example, and success criteria. Reuse supplied context; ask only consequential missing questions. Start with one entry skill; split specialists only for independently useful tasks.
2. Inspect the live repository, local instructions, installed identities, and creation/install capabilities. Load the host's built-in skill-creator before personal-skill mutations. Its current workflow owns native installation. Do not hardcode account paths, credentials, or internal IDs in a portable package.
3. Keep source under `skills/<name>/` with `SKILL.md`, optional `agents/openai.yaml`, and only needed resources. Initialize a new Work skill in the host-managed checkout as its creator requires, then mirror reviewed content to the canonical repository. For updates, preserve the existing installed identity and unrelated files.
4. Read [release-checklist.md](references/release-checklist.md). Run the host's minimal validator on the actual native candidate. Run `python3 scripts/validate_package.py <repository-root>` from this skill directory for portable convention checks (requires PyYAML). Inspect scripts before executing them. Static validation is neither a security review nor a runtime test.
5. Test executable helpers with valid and invalid fixtures. Forward-test instructions with a realistic task and a boundary case when independent agents are supported. Keep contexts minimal and tests isolated from live accounts. Retain actual outputs/tool results, not merely the agent's claims.
6. Save reviewed source to the authorized repository. Install/update through the supported host workflow, one skill at a time. For ordinary Chat, follow [cloud-chat-install.md](references/cloud-chat-install.md) to package, upload, install, and test the separate cloud plugin release. Verify persistence and compare installed file hashes with the pinned source. Follow the user's authorization and host approval rules. Do not uninstall, delete, publish publicly, or broaden access merely to simplify installation.
7. Verify discovery in the intended session, then read the installed instructions through the native reader. If a cached session blocks discovery, record that limit and use a fresh session when available. Do not repeat installs solely because a catalog is stale. Test behavior and checkpoint resumption after loading.
8. Write a release record using [release-record.md](references/release-record.md). Separate package validity, stored installation, session availability, instruction loading, and behavior. End with a usable invocation and precise remaining limits.

## Packaging and boundaries

For skills-only plugins, use root `plugin.json` and shared `skills/`. Check current official schemas before claiming full schema validation. Add a repository marketplace only when a documented target requires it. Native personal skills, complete plugins, local marketplaces, workspace distribution, and public-directory publication are distinct operations.

Native Work loading was verified in the originating strategy-factory project. On 2026-09-27, a cloud uploaded skills-only plugin containing `pocock-handoff` was discovered and read in a fresh ordinary Chat conversation on web. Its sibling `HOST.md` was not exposed by the Chat skill reader, so keep essential instructions in `SKILL.md` and verify every required resource in the target host. iOS loading remains unverified. Recheck capabilities when the target changes. Never claim that updating source automatically updates an installed cloud plugin.

Keep this pipeline agent-driven. Add no server, database, MCP service, scheduler, or unattended deployment credentials without a demonstrated need. If a repository-creation action is missing, inspect an authorized browser route. Stop at authentication/permission boundaries and request only the smallest unavoidable user action.

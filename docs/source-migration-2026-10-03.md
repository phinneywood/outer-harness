# Source migration — October 3, 2026

## Provenance

Harness and assistant utility source copied from `phinneywood/chatgpt-plugins` at `ab571a5c74d481a1efe4bd6e585d6f022ae87f01`. The original repository retains its history and earlier release evidence. This repository starts with its existing clean initialization and a source snapshot; earlier commits, personal commit addresses and historical deployment links are not imported.

Retain the root MIT license and Pocock Handoff's upstream MIT notice. Historical source revisions in copied release records refer to `phinneywood/chatgpt-plugins`.

## Compatibility

Keep the installed plugin name `assistant-harness`, display name Assistant Harness, version 1.0.0 and four bundled skills. Core instructions and manifest are copied without changes. Rebuild and compare the archive to SHA-256 `2903b85e43ddf40cef4ea3cd78c611374442d366e2f8de2d3bf211b845f6f4bf` before switching consumers. No cloud reinstallation is necessary when the package bytes match.

The plugin factory's repository routing is updated for the agreed source homes. It remains a separately installed personal utility; changing this source does not update that installation.

## Migration gates

Validate the configuration tests and the extracted core archive's portable conventions. Read core instructions from the new pinned revision through connected GitHub before migrating consumers. Capture current private configuration and exact task registrations for rollback; change source pins in existing registrations, preserving current policies, prompts, enabled state, schedules, timezone and conversation bindings. Leave event registrations alone when complete filters cannot be read.

Store task, deployment and audit evidence privately. Registration readback proves that source pins were migrated; independent execution after the move remains a separate gate. Previously verified 1.0.0 runtime evidence stays valid within its original scope.

Keep the old collection available until product integrations have moved and every consumer has been verified. Long Form's active product work and registered service mapping require coordinated migration. No public Directory submission is implied.

## Candidate verification

- Rebuilt core archive SHA-256 matches the existing 1.0.0 release exactly.
- All nine configuration/renderer tests passed.
- Portable convention checks on the extracted core archive passed for all four skills.
- Inspected 46 UTF-8 source/document files and all nine ZIP members for credential patterns and personal deployment/configuration identifiers. Three credential-pattern hits are intentionally invalid rejection fixtures in `tests/test_harness_config.py`; the `secret@trello.com` string is part of an invalid credential URL in that fixture. No actual credential or personal deployment target was found in this candidate.
- All four existing installed cloud skills were readable through the native reader and match the copied core instructions. Previous runtime/device limits still apply.
- GitHub security settings and independent post-migration task runs require their own evidence.

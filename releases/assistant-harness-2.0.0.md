# Outer Harness 2.0.0

## Scope

Retire `assistant-harness`, `portfolio-pm` and `knowledge-reconcile` from current source and the cloud package after explicit user authorization. Retain `outer-harness` with all five references and the separate `harness-audit`. The manifest identity stays `assistant-harness`; version 2.0.0 marks removed invocation paths. Core/reference/audit bytes remain identical to 1.2.0 at `9240980af722fb7044065e98cd05293f2fc71c3b`.

The offline task-prompt renderer now selects `outer-harness` for daily, completion-watch and knowledge, loads relevant references, and uses `deployment.unified_entry_point.source_ref` when configured. Audit retains its legacy deployment pin. Rendering is preparation only: saved registrations are not modified. Existing task-specific overrides must be preserved when applying prepared instructions.

## Artifact and validation

- Archive: `assistant-harness-2.0.0.zip`.
- SHA-256: `7eb286e5beb97dda49f7031d24844a5287889f84dcc932af8e7ec5c62a196603`.
- Exactly two skills; root manifest/license and reviewed skill files only.
- All 34 configuration, packaging and migration-preservation tests pass.
- Build reproducibility and exact retained file-byte comparison pass.
- Earlier release archives and git history remain available for rollback.

## Runtime boundaries

This cleanup does not change task prompts, schedules, event filters, runtime/conversation bindings, notifications, permissions or source pins. Existing migrated invocations use the unified source at the 1.2.0 commit. Retiring the compatibility paths was explicitly authorized before all independent task modes had been observed. Independent task effects, genuine email-event behavior, repeat/failure reliability and automatic activation remain separately scoped acceptance gates. Public source/package validation does not prove installed cloud version or session-native loading; installation evidence belongs in the user's private deployment records.

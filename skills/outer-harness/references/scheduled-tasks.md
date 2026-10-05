# Scheduled use and migration

## Separation of responsibilities
The host task registration decides when to run. Its approved prompt supplies the task's purpose, current scope, reporting rules and permissions. The core skill and selected references supply reusable procedure. The private configuration supplies source/account mappings and policy locators. None of these creates an always-on assistant or automatically updates the others.

Map existing invocations without combining registrations:
- `portfolio-pm`, mode `daily` -> `outer-harness`, mode `daily`.
- `portfolio-pm`, mode `completion-watch` -> `outer-harness`, mode `completion-watch`.
- `portfolio-pm`/`assistant-harness`, mode `email-event` -> `outer-harness`, mode `email-event`.
- `knowledge-reconcile` -> `outer-harness`, mode `knowledge`.
- `harness-audit` remains the advanced audit workflow.

Specialty workflows such as training, reading, supply reminders, finances, public watches or browser chat cleanup do not acquire a new harness dependency merely because this refactor exists. Preserve their original runtime and boundaries. Do not run every harness mode whenever any one task wakes up.

## Each scheduled invocation
Explicitly load the selected skill and actual required reference bytes. If native loading is unavailable, fetch the reviewed pinned source through an already-authorized connector available in that runtime. Load current private policies. Do not silently use a different version, reconstruct missing instructions, or replace a Work run with an ordinary Chat task. A required load failure stops dependent effects and checkpoint advance under the existing error policy.

Keep task-specific overrides intact: source routing, notification thresholds, single-reporter ownership, deduplication, claims/checkpoints, exceptions, message approval and calendar rules. More concise prompts are a possible later result, not evidence of safe equivalence. A generic prompt renderer cannot recreate private exceptions it has not read.

## Before editing an existing registration
1. Capture the complete current registration and prompt privately: ID, name, enabled state, schedule/timezone/timing mode, runtime, conversation binding, delivery/notification settings, and full event triggers/conditions/filters when applicable. Incomplete metadata means migration is blocked; a friendly title or last-run timestamp is not sufficient.
2. Compare the current task's obligations against the candidate references. Preserve every private override and authority boundary in its existing source, or in one explicitly migrated authoritative record. Do not delete repeated-looking clauses until their intended behavior is accounted for. Never publish private prompts or task IDs in fixtures.
3. Verify new skill/references/configuration and required tool access in the actual task runtime. Separately verify read-only behavior, harmless authorized writes/readback, repeat-run deduplication and required-source failures. Static tests are not those proofs.
4. Change only the approved instruction/source-reference fields of the same registration. Do not recreate jobs, alter cadence, enable paused tasks, change notification settings or add another morning reporter. Preserve complete event filters; when they cannot be read, leave the event task unchanged. Do not convert an event task to polling because a returned schedule says unscheduled.
5. Read the registration back and compare all preserved fields and the exact intended prompt. Keep the old prompt/config/source pins privately for rollback. Verify a later independent execution and its actual effects before declaring the migration complete or removing compatibility paths.

Updating repository files does not update installed plugin bytes, standing instructions or saved-task pins. Keep the installed plugin identity stable at eventual upgrade; defer removal of legacy skill paths until no verified consumer needs them. No installation or task migration is implied by staging this candidate.

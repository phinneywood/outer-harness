# Assistant Harness

Version 1 contains four self-contained skills: `assistant-harness` (recover and route), `portfolio-pm` (daily/reconcile/completion/email modes), `knowledge-reconcile` (knowledge and document maintenance), and `harness-audit` (read-only checks and authorized migration). Existing service plugins provide tools. The package adds no server or database.

## Configure privately

Copy `examples/assistant-harness/config.example.json` into your own private knowledge repository and replace placeholder targets. Validate it with `python3 scripts/harness_config.py PRIVATE_CONFIG.json`. The example grants no maintenance permissions. Set only permissions you have actually authorized. Keep credentials out of the config. Point current policies/checkpoints at their authoritative records. Never publish your configured copy or task backups in this public repository.

The version 1 profile supports GitHub knowledge, Trello project state, assistant-owned Google Drive documents and an assistant-managed Google Calendar, through connected MCP tools. Other service backends and personal-calendar access are not implemented. Calendar recording does not authorize choosing or booking proposed times.

Use a short standing bootstrap based on `examples/assistant-harness/bootstrap.txt`. Installing a skill does not make every chat load it. For substantial writing, retain your authorial-boundary instructions and writing workflow separately.

## Retrieval and durable storage
Keep Trello absent by default from new chats, general questions and resumed implementation/document work. Use the smallest relevant source for the actual task. Read a targeted card only when project state is required or a material change must be safely reconciled. Whole-board reads belong to scheduled daily or explicitly requested portfolio reviews; completion/email workflows use relevant known work and bounded discovery. Reuse context, batch routine material updates at meaningful stopping points, promptly record blockers/commitments, and verify changed cards.
Keep concise reusable facts, preferences, standing decisions and outcomes in private knowledge; substantial research/requirements/plans/comparisons/artifacts in Drive; implementation and technical execution checkpoints in project repositories; operational state and pointers in Trello. Link a brief reusable takeaway to its substantial source instead of duplicating it. Preserve unique content before an authorized move or shortening. Reduced calls do not prove an unrelated rendering defect is fixed.

## Build and install

Build with `python3 scripts/build_plugin.py assistant-harness --skills assistant-harness portfolio-pm knowledge-reconcile harness-audit`. The archive contains only the manifest and reviewed skills; private config and account connection mappings are excluded. The current package manifest is **1.1.0**; see `releases/assistant-harness-1.1.0.md` for release-specific validation and limits.

Personal Work skills and cloud plugins are separate installations. Use the supported skill-creator workflow for personal installation. For ordinary Chat, upload the archive through ChatGPT Plugins → Personal → Add → Upload plugin archive, install it, and test in a fresh Chat. Keep one installed identity for future updates. Public Directory submission/review is a separate operation; no public listing is implied by this repository.

For ordinary Chat, explicitly select Assistant Harness and the service plugins needed for the work (for example, GitHub and Trello), and supply your private `config_locator`. The original 1.0.0 recovery test loaded all four skills, then read real configuration/project records with GitHub and Trello selected; that remains historical evidence for that package. Version 1.1.0 changes scoped retrieval policy and has its own static release validation, but native-reader loading, automatic activation, ordinary-Chat write behavior and device-specific behavior should be verified separately after upgrading. Installing a skills-only plugin does not activate every connected service. See `releases/assistant-harness-1.0.0.md` and `releases/assistant-harness-1.1.0.md` for the evidence recorded for each release.

Current official instructions: https://developers.openai.com/plugins/build/plugins and https://learn.chatgpt.com/docs/build-skills. GitHub source changes alone do not update an uploaded plugin.

## Schedule without copying procedures

Pin `deployment.ref` to the verified source commit. Render a prompt with `python3 scripts/harness_config.py PRIVATE_CONFIG.json --render daily --locator PRIVATE_CONFIG_URL`. Supported roles are `daily`, `completion-watch`, `knowledge`, and `audit`. The prompt explicitly loads the installed skill, or the pinned GitHub instructions if native loading is unavailable, then loads current private policies. Required-read failures stop dependent writes.

Refactor an existing task only after fetching those instructions/config in its actual runtime. Preserve schedule, enabled state, conversation/runtime binding and complete event filters. Keep old prompts privately for rollback. The renderer deliberately does not migrate email-event tasks: their full trigger set must first be read from the host. Do not duplicate jobs or reactivate paused tasks.

Other personal briefs, release watches and chat-cleanup jobs remain separate. Audit/inventory them first; add reusable recipe skills only when their current behavior can be preserved and tested. This core release does not claim to package every personal scheduled task.

## Verify

Run `python3 -m unittest discover -s tests -p 'test_harness_config.py' -v`. Use the fixtures for independent prepare-only behavior checks. Also verify native discovery/readability, explicit workflow behavior, first independent saved-task execution and device-specific loading separately. Preserve actual outputs; a static validator or plausible answer is not runtime proof.

Accept context recovery only when a fresh conversation reads the current authoritative records. Accept reconciliation when real writes are read back, repeated runs avoid duplicate effects, failed writes do not advance progress, and account/sharing boundaries hold. Test iOS separately. See the release record for observed gates and remaining limits.

## Repository hygiene

Run the existing `harness-audit` skill with the [repository hygiene procedure](repository-hygiene.md) loaded from a pinned source revision. Keep target repositories, policy exceptions, checkpoints and the task registration in private configuration. Schedule a separate low-frequency read-only audit unless an existing audit already covers it; preserve other registrations. This adds a shared scheduled recipe without changing the four-skill package.

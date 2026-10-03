# Assistant Harness 1.0.0

Date: October 3, 2026. Target: personal Work deployment first; ordinary Chat and iOS through a separate cloud plugin release. Reusable skills: assistant-harness, portfolio-pm, knowledge-reconcile, harness-audit. Existing service plugins supply tools; no new MCP server/account connection is bundled.

## Evidence gates

| Gate | Status | Evidence and limit |
| --- | --- | --- |
| Source and package | Validated | Four self-contained SKILL.md files; root portable manifest; archive contains manifest plus skill files only. |
| Host skill validation | Passed | Built-in quick_validate.py ran on each actual personal installation candidate. |
| Portable convention checks | Passed | Plugin-factory checker ran on the extracted actual archive; zero errors. This is not full Agent Plugins schema or security certification. |
| Config and renderer checks | Passed | Nine unittest cases: permission type confusion, protected actions, personal-account boundary, unpinned sources, timezone/version, secret/credential URLs, duplicate task IDs, escaping paths, wrong private repository, event-task shortcut and read-only CLI. |
| Independent portfolio workflow | Passed, fixture only | Minimal-context agent used the portfolio skill: proposed dates did not authorize booking; email instructions did not override rules; no sending; event completion waited for write/readback; missing ready-list configuration was not guessed. |
| Independent knowledge workflow | Passed, fixture only | Minimal-context agent used the knowledge skill: 409 plus failed reread left update/watermark pending; timezone correctly kept date October 3; already-claimed interrupted sweep was skipped; shared/personal file excluded. |
| Personal Work persistence | Passed | Each skill was saved separately, reconciled to a stable installed identity, and read from the remote stored tree. All final source hashes match the persisted SKILL.md bytes after normalizing one terminal blank line removed by the host. |
| Fresh Work native discovery/reader | Passed | A fresh Work turn loaded all four named personal skills through the native reader. The earlier cached-session limitation is superseded for this fresh session. |
| Pinned source and private configuration loading | Passed | Connected GitHub fetched the private config, checkpoint, and pinned portfolio/knowledge instructions. Exact content readback matched reviewed source. Existing current operating policy was read separately. |
| Existing task prompt migration | Passed | Three existing time-based tasks were updated in place and read back. Prompt equality, schedule, enabled state, timezone and conversation binding were verified. All 25 registration IDs and all other prompts were preserved. |
| Migrated independent saved-task behavior | Knowledge path passed; other paths pending | The independent migrated knowledge run loaded its native skill, private configuration and current policies, wrote a knowledge update, and verified commit/file plus checkpoint readbacks. Today's claimed Drive sweep was correctly skipped; no new post-migration Drive-write proof. Daily PM and completion-watch execution remain unverified. Private runtime evidence retains exact timestamps and commits. |
| Cloud plugin installation | Passed | Prepared 1.0.0 ZIP uploaded and installed as one personal Assistant Harness cloud plugin. Host page showed four skills, version 1.0.0, installed sidebar entry and Try in chat. No public Directory submission. |
| Fresh ordinary Chat native loading | Passed | New ordinary Chat, started from Try in chat without attached/copied instructions, returned distinctive rules for all four skills. Its native Sources panel listed all four under assistant-harness; the installed instruction preview was inspected. Connected Work native reads of the cloud plugin's four resources also succeeded with exact source hashes. |
| Ordinary Chat explicit behavior | Passed, read-only scope | Initial harness-only attempt did not activate record tools and stopped without inventing state. With GitHub and Trello explicitly selected, the same fresh Chat fetched private config and the authoritative project card, recovered outcome/next action, and made no changes. Cloud Chat write workflows are not proven. |
| iOS | Unverified | Requires a separate fresh iOS conversation; web success is not iOS proof. |
| Automatic activation | Unverified | Explicit loading is the supported release route; universal rules stay in standing instructions. |

## Forward-test outputs

Portfolio fixture: the agent proposed a project next-action update, preserved the thread/message identifiers without inventing URLs, made no calendar/message operation, declined to guess the unconfigured ready list, and kept the processed-message checkpoint unchanged until verified effects. The claimed quote attachment was not treated as received without evidence.

Knowledge fixture: the agent retained the original reviewed-through value, required a successful current-SHA reread before retrying, and reported both actual failures. It correctly converted 00:30 UTC October 4 to 17:30 Pacific October 3 and skipped that date's already-claimed sweep without marking it completed. These are isolated prepare-only behavior checks, not live connector or scheduling tests.

## Dependencies and rollback

Each user supplies a private config locator, authorized current policies, existing GitHub/Trello/Google Drive tools and an assistant-managed Calendar where used. Runtime may fetch pinned source through GitHub when native skill loading is unavailable. A required read failure prevents dependent writes.

Private task/config/rollback records remain outside this public package. Existing enabled jobs are refactored in place only after source loading; schedules/enabled state/runtime remain fixed. Event tasks remain unchanged if their complete filters cannot be read. Disabled jobs are not reactivated. Specialty reading/brief/cleanup/watch recipes are not included in this core release.

User invocation: select Assistant Harness or request the relevant skill with your private config_locator. Source edits do not automatically upgrade cloud plugins or pinned tasks. Public Directory publication is not part of this release.

## Cloud deployment evidence

Source revision: `5d81a60dc0aaa23f5baa4e02f43f36b851f3a7cd`. Archive version: 1.0.0; root manifest and final fingerprints below. Installed cloud resources were read at `assistant-harness@created-by-me-remote` version 1.0.0 and match all four recorded hashes exactly.

The fresh Chat returned the configuration-location rule, separate evidence-gate rule, failed-write checkpoint rule, and project-classification rule. Native Sources listed the four corresponding installed skills. Its loading check also performed unnecessary public searching; those search results were not accepted as skill provenance. The connected-record behavior check explicitly prohibited web/memory substitution and used GitHub/Trello records.

For ordinary Chat, select Assistant Harness and the relevant already-connected service plugins. Installing the skills does not automatically activate those record tools. The personal cloud identity, fresh Chat URL and account-specific runtime evidence are retained privately. Universal automatic activation, ordinary Chat mutation workflows, remaining scheduled execution paths and iOS remain separate gates. The user's browser authorization applied to upload/install and verification only; routine configured workflows remain MCP-only.

## Final package fingerprints

Archive SHA-256: `2903b85e43ddf40cef4ea3cd78c611374442d366e2f8de2d3bf211b845f6f4bf`.

| Skill | SKILL.md SHA-256 |
| --- | --- |
| assistant-harness | 4bbc649622ad0a77f70826f2de5d37f29ef096e1cd6e0d5208ee8911f8284d99 |
| portfolio-pm | ac3d6337cdcc1ddbcc56ea8cb4635859d6d977533f55ae2fa380d5b0cad0a074 |
| knowledge-reconcile | d9cbe49d47b5322f404fac53fec8ded5a4f4fc14d01ac969fd141f6732108cbe |
| harness-audit | 2afdcef55064171f10352b07f13cb4f56b0220b0b3c3e1f2419968fdf8e9be63 |

Direct GitHub shell push lacked credentials; connected GitHub mutations saved/merged source successfully. Concurrent personal-skill storage updates were handled in an isolated checkout without altering pre-existing local work. Full event-router filters are unavailable from the task API, so its prompt and registration were left unchanged. Existing reading, brief, cleanup and specialty watch jobs remain intact.

# Outer Harness

**Reusable instructions and checks for keeping a ChatGPT assistant oriented across ongoing work.**

An assistant may help with a project today, then need the same background again next week. Decisions can end up scattered across chats, task boards, notes and documents. Outer Harness defines where those records belong, which ones the assistant should consult, what it may update, and how it should check the result.

This is an experimental personal workflow project. It contains written procedures called **skills**, a configuration checker, a tool for preparing scheduled-task instructions, and a plugin package builder. ChatGPT and its connected services carry out the work. Account connections and schedules are set up separately.

## A concrete example

Suppose you ask: “What remains on the website update?”

| Step | What the assistant should do |
| --- | --- |
| Recover the context | Read the relevant project record and follow its source links. |
| Check the facts | Inspect the repository or live page when the question requires implementation evidence. |
| Keep records in the right place | Task status stays in the task board; code and technical evidence stay in the repository. |
| Respect the request | A status question does not authorize publishing a change. An approved update may change the relevant records. |
| Verify an update | Read changed records back before reporting success. |

This table illustrates the intended workflow; it is not evidence of a completed live run. See the [worked example and verification record](docs/worked-example.md) for the distinction between a local demonstration, recorded runtime results and pending checks.

## The four core workflows

The downloadable **Assistant Harness** plugin bundles these four skills:

| Workflow | Everyday purpose |
| --- | --- |
| Recover context | Pick up ongoing work from its current records. |
| Manage projects | Keep outcomes, next actions and blockers current; prepare a daily review. |
| Maintain knowledge | Preserve useful facts and decisions, and organize assistant-owned documents. |
| Audit the setup | Check configuration, installations, schedules and repository hygiene. |

The supported setup uses GitHub for durable notes, Trello for project state, Google Drive for documents, and an assistant-managed Google Calendar for confirmed commitments. The [source-role guide](docs/assistant-harness.md#retrieval-and-durable-storage) explains the boundaries.

## Understand it or try it

- **Start with the design:** [worked example](docs/worked-example.md) and [glossary](docs/worked-example.md#glossary).
- **Try the tools locally:** [first-run guide](docs/first-run.md#try-the-local-tools), using synthetic configuration and no connected accounts.
- **Use it with ChatGPT:** follow the [read-only first-run guide](docs/first-run.md#use-it-with-chatgpt). Bring your own private configuration, policies and authorized service connections.
- **Download the package:** [Assistant Harness 1.1.1 ZIP](releases/assistant-harness-1.1.1.zip), with its [release record](releases/assistant-harness-1.1.1.md).

## What is verified

The configuration and packaging tests check code behavior and archive contents. They do not establish that an assistant will follow every instruction, that scheduled work will execute reliably, or that every device supports the same installation flow.

The [1.1.0 record](releases/assistant-harness-1.1.0.md) covers static and prepare-only checks; the [1.0.0 record](releases/assistant-harness-1.0.0.md) contains earlier, separately scoped runtime evidence. **1.1.1 repairs packaging and onboarding; it does not add a new runtime or prove unattended reliability.** Installing an updated package remains separate from updating this repository.

Permission settings and skills guide the assistant. They do not intercept tool calls or replace the host's permissions and approval controls. Protected actions such as sending messages, deleting data and publishing still require the user's authorization.

## Repository map

| Folder | Contents |
| --- | --- |
| `skills/` | Core operating procedures and additional assistant utilities. |
| `plugins/` | Package descriptions and reviewed lists of files to distribute. |
| `examples/` | Placeholder private configuration and a short startup instruction. |
| `scripts/`, `tests/` | Configuration checks, task-instruction rendering, package building and tests. |
| `docs/`, `releases/` | Setup, examples, provenance and verification records. |

Writer’s Packet and Pocock Handoff are separate packages. Distill and the plugin-building utility are source utilities; their presence here does not install them in the core plugin. See [source ownership and migration](docs/source-migration-2026-10-03.md) for provenance. Long Form integrations live in [Long Form](https://github.com/phinneywood/long-form), and strategy companions live in [Strategy Factory](https://github.com/phinneywood/strategy-factory).

## License and privacy

Original work is [MIT licensed](LICENSE). Pocock Handoff retains its [upstream MIT notice](skills/pocock-handoff/LICENSE). The current core ZIP and newly built packages include the root license; package file lists keep unreviewed additions out of archives. Historical archives are retained unchanged.

Keep real configuration, account targets, task registrations, rollback records and credentials private. Public examples use placeholders and grant no maintenance permissions. Follow the [repository hygiene procedure](docs/repository-hygiene.md) when reviewing changes.

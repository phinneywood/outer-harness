# Configuration contract

## A role is a responsibility, not an application
A role says what a source owns. A provider says which existing application implements it. Several roles may use the same application; no role requires a separate account or repository. Omit unused roles rather than introducing tools for completeness.

| Role | Responsibility |
| --- | --- |
| Portfolio / non-migrated projects | Outcomes, priorities, personal decisions, commitments and non-migrated next actions |
| Delivery | Implementation issues, milestones, blockers, verification gates and releases for explicitly mapped projects |
| Knowledge | Concise reusable facts, preferences and standing decisions with rationale |
| Documents | Substantial plans, research and artifacts |
| Implementation | Code, tests and technical execution evidence |
| Calendar | Scheduled details of authorized assistant-managed commitments |

Scope mappings must identify the authoritative source precisely enough to retrieve it. Do not select a different source because the designated one is unavailable. Specialized records, such as a training workbook, retain their domain ownership.

## Existing configuration: keep the current locator
Continue accepting the existing private JSON with `schema_version: 1`. Preserve it and its policy links; do not rewrite it simply to adopt this entry point. Read only required policies for the operation.

Interpret `sources.projects` with its explicit scope, not as an unconditional owner of all task state. When present, `sources.delivery` and `policies.project_routing` govern explicitly migrated delivery. The existing portfolio provider remains the owner of portfolio/non-migrated work. `sources.knowledge`, `sources.documents` and `sources.calendar` retain their defined roles. Implementation pointers come from the relevant project record.

Preserve `accounts`, `transport`, `permissions`, `calendar_attendees`, notification overrides, checkpoints, deployment pins and native task identities. More specific current user-authorized task/policy overrides take precedence over historical generic defaults. A disagreement without clear authority is a blocker, not permission to choose the less restrictive rule. This is an instruction-level compatibility contract, not a replacement for the version-1 validator.

## New adopters: one private setup record
The candidate supports a human-readable Markdown profile marked `Profile format: outer-harness/1`. It contains: scope, timezone, authoritative source mappings, explicitly allowed routine maintenance, actions requiring approval, account/privacy constraints, approved reporting rules, and verification status. Unknown or absent permissions mean not granted. No maintained sources is a valid read-only starting point.

Choose exactly one authoritative home with the user: a private document in an already-used connected service, or a file in an existing private repository. Do not require GitHub, a new assistant account, or a task board solely to use the methodology. Verify the chosen host can actually retrieve that record; a linked document does not prove a connector is supported.

Store only its locator and short universal boundaries in standing ChatGPT instructions. Installation and standing-instruction editing are separate steps requiring actual supported operations and readback. A link in a chat or a file created in this session is not proof of account-wide adoption. Do not rely on conversational memory as the only configuration store.

For scheduled use, the actual scheduled runtime must read the profile and all required policies. Before enabling a workflow that needs a checkpoint/claim record, agree and verify its location and exact semantics. Do not require four separate policy files merely for initial read-only onboarding. Advanced deployment hashes, audit evidence and task backups stay private and out of the ordinary user-facing setup summary.

The existing `harness_config.py` validator and renderer support legacy JSON only. They must not be run against this Markdown profile or described as validating it. The old audit utility's schema-1 requirements also remain until explicitly adapted. Report unsupported combinations rather than silently translating away safeguards.

## Privacy and conflict handling
Never store credentials in the profile. Repository procedures may be public; real source locators, sharing choices, task registrations and rollback records stay private. Each person's configuration and connections are independent. Shared household records require explicit agreement and one workflow owner; no automatic access to another person's chats, memory, inbox or files.

Avoid two editable configuration copies. Existing users keep the existing source until an approved migration maps every preserved setting and dependent consumer. A friendly overview may point to it, but must not become a competing authority.

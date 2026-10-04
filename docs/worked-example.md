# Worked example and verification

## The everyday problem

A project can be discussed across several chats while its actual state lives somewhere else. Without a clear rule, an assistant may repeat old background, consult unrelated tasks, or treat a proposed change as a completed one.

Outer Harness provides operating procedures for consulting the right current records and keeping different kinds of information in their proper homes.

## Illustrative project workflow

This is a synthetic example, not a claim that a connected service executed it.

| Input or action | Expected behavior |
| --- | --- |
| A task says a website update is waiting for review. | Treat the task board as the operational record; follow the repository link for implementation details. |
| The repository has a new commit. | Inspect the relevant change and verification evidence; a commit alone does not establish a working deployment. |
| The user approves publishing that specific update. | Carry out the authorized change through available tools, within account and permission boundaries. |
| The deployed page is observed with the expected content. | Record that observed result, with its source, on the existing task. |
| The task record is read back. | Report only the changes actually verified. |
| A required source or write fails. | Leave the affected work pending and do not advance its checkpoint. |

General project review and a narrow completion check have different scopes. A completion check follows the relevant expected result; it does not need to reread the entire portfolio.

## Reproducible local evidence

Run the commands in the [first-run guide](first-run.md#try-the-local-tools). The synthetic example configuration permits no maintenance writes. The tests cover protected-action requirements, account boundaries, source pins, URL validation, duplicate task registrations and task-instruction rendering.

Packaging tests check license inclusion, exact reviewed content and source-byte correspondence, repeatable builds, exclusion of an unreviewed configuration file, rejection of symbolic links and escaping paths, and rejection of a mismatched skill selection. Those checks are reproducible without any service account.

## Runtime evidence and limits

| Evidence | What it establishes | What it does not establish |
| --- | --- | --- |
| Local configuration tests | Validator and instruction-renderer behavior on the test inputs. | Correct live accounts, reliable model behavior or successful scheduled work. |
| Local packaging tests | Reviewed source files and license are packaged reproducibly. | Installation or host compatibility. |
| [1.0.0 release record](../releases/assistant-harness-1.0.0.md) | Previously recorded runtime checks within that release's stated scope. | Every workflow, later releases or all devices. |
| [1.1.0 release record](../releases/assistant-harness-1.1.0.md) | Static and prepare-only checks for scoped retrieval. | New live writes or unattended execution. |
| [1.1.1 release record](../releases/assistant-harness-1.1.1.md) | Packaging and onboarding changes, with unchanged core skill instructions. | A new autonomous system or broader runtime certification. |

A fresh, sanitized live workflow should record its trigger, records consulted, actual effects, readback and remaining limits. Repeat-run and failure-recovery behavior need direct evidence. Private account targets, full task prompts and personal records belong in private verification notes.

## Glossary

| Term | Meaning in this project |
| --- | --- |
| Harness | Instructions and checks around the assistant's work. “Outer” refers to the procedures and records configured outside the ChatGPT runtime. |
| Skill | A saved procedure the assistant reads when performing a particular kind of work. |
| Plugin | An installable package of skills; it can be separate from the service connections that provide tools. |
| Connected service / MCP tool | A host-provided way for the assistant to read or act in a service such as GitHub or Trello. The package does not supply those connections. |
| Private configuration | Your service targets, policy links, approved maintenance settings and verified source revision. |
| Source of truth | The record that owns a particular fact: for example, a task board owns task state, while a repository owns code. |
| Readback | Reading a record after changing it to confirm the intended change was saved. |
| Pinned revision | A specific Git commit recorded so a task uses known instruction source. This differs from pinning a repository on a GitHub profile. |
| Prepare-only check | A check of planned behavior that makes no real external changes. |
| Independent scheduled execution | A task running at its scheduled trigger and producing verified effects, rather than only having its registration accepted. |

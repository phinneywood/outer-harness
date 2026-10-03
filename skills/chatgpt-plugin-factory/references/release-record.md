# Release record template

Date:
Repository and source revision:
Target host / mode:
Skill names and version:
Deployment identity (exclude private identifiers from public reports):

| Gate | Passed / failed / unverified | Actual evidence and boundary |
|---|---|---|
| Static package | | Checker and host validator output |
| Installation persisted | | Supported installation result |
| Source equality | | File hashes against pinned source |
| Session discovery | | Native catalog result |
| Instructions loaded | | Native reader result and resource |
| Behavior | | Prompt, output, tools used |
| Resumption | | Checkpoint and continuation, when relevant |

Changes:
Dependencies:
Failed checks / limitations:
Restore plan (prior source revision; retain installed identity):
User invocation:

A self-report, visible chip, plausible answer, or GitHub fetch does not prove installed instruction loading. Record each tested host separately.

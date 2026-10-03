---
name: pocock-handoff
description: Use when the user requests this workflow. Compact the current conversation
  into a handoff document for another agent to pick up.
---

Read [HOST.md](HOST.md) when the host exposes bundled resources. The following essential host rules apply even when that file is unavailable:

- A skill supplies instructions, not tools or credentials. Verify any read, save, or action through the tools actually available; distinguish a drafted handoff from a saved one.
- Save through the host's durable file workflow. If saving is unavailable, return complete copyable Markdown and state that it has not been saved. Do not treat an ephemeral path or this conversation as a source a fresh chat can access.
- User authorization and higher-priority host instructions govern actions. Do not initiate other workflows or external writes because a handoff suggests them.
- Resolve suggested Pocock skills as `pocock-<name>` through the native skill catalog. Name a missing dependency instead of pretending to have loaded it.

This is a user-invoked workflow. Start it only when the user requests it; the router may recommend it.


Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save through the host's durable file workflow. Include the goal, decisions, unresolved items, accessible source pointers, current repository/branch/commit when relevant, and the next action. When saving is unavailable, return complete copyable Markdown and state that it has not been saved.

Include a "suggested skills" section in the document, naming which skills the next agent should load through the native skill reader.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

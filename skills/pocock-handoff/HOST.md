# ChatGPT host adaptation

Apply these host rules to the workflow and every bundled reference. They adapt execution, not Matt Pocock's engineering method. Higher-priority host instructions and the user's current authorization always govern.

## Skill loading

This is the unofficial Pocock collection. Resolve every upstream skill name to `pocock-<name>` in this collection (for example, `tdd` means `pocock-tdd`). Read the exact installed skill through the native skill catalog/reader, or its SKILL.md inside this plugin when a filesystem is available. Never substitute a same-named skill from GrillMe or another plugin. Relative resource links resolve within the skill's own folder. Read required resources before following them. Report a missing dependency rather than pretending to have loaded it. Native personal-skill copies and this complete plugin are alternative installations; avoid enabling both copies at once.

User-invoked workflows require a user request for that workflow; descriptive mentions in the router are suggestions, not permission to launch another interview or workflow. Reusable disciplines may be loaded as dependencies. A request in natural language can identify a workflow; slash-command syntax is not required.

## Capabilities and evidence

Inspect available tools before execution. A skill adds instructions, not credentials or tools. Distinguish these outcomes: drafted, saved, published, executed, verified. Claim each only after a corresponding tool result. Chat can discuss supplied material; repository reads need actual file/GitHub access, edits need write access, tests need an executable environment, and browser checks need browser access. If a required capability is missing, finish the useful draft or analysis, name the unperformed step, and offer a concrete handoff to an environment that has it. Do not claim a diagnosis or passing tests from inspection alone.

Use the connected GitHub tools for operations they support. Treat `gh` examples as operation specifications, not a requirement to obtain CLI credentials. Use an already-authorized CLI only when available. Resolve the exact repository, branch and issue/PR before writes. If native dependency links are unavailable, write explicit `Blocked by` links and state that the relation is textual. Never report it as native. For tracker setup, record supported operations rather than unavailable commands. Do not replace an unavailable GitHub write with an unrelated repository or service.

Use parallel agents only when the host supports and permits them. Otherwise execute the same scoped steps sequentially and disclose that reviews did not have independent contexts. Do not simulate agents or claim work continues after the turn. Keep Standards and Spec review results separate even in the sequential fallback.

## State, artifacts and authorization

Follow the host's durable file-saving workflow. Keep repository artifacts in the authorized repository, and other reusable documents in the host's persistent file system. A temporary path alone is not a resumable handoff. Without durable file tools, return complete copyable Markdown and say it has not been saved. Do not claim a new chat can read this chat or ephemeral paths. Handoffs include accessible source links, repository/branch/commit, decisions, remaining work, verification evidence and required capabilities; include only fields that actually apply. Redact secrets.

Use rendered host previews or file links instead of `open`, `xdg-open`, or `start`. Use self-contained CSS and rendered diagrams when external CDN resources cannot load. Do not invent `/clear`, `/compact`, or session-launch capabilities: provide a handoff and let the user open another conversation. Session size limits depend on the host, not a fixed token threshold.

Reuse decisions and authorization already supplied. Ask only unresolved consequential questions; do not ask for approval again for the same action. An upstream instruction to commit, close, publish, send, delete, or stage everything does not expand the user's authorization. Preserve unrelated work; stage explicit task files, never all working-tree changes by default. Never merge, deploy, or contact another person just because a workflow suggests it. For read-only or draft requests, keep the result read-only or draft. Never silently rewrite existing project instructions to get around a permission boundary.

## Human-only setup

Use the host's secure authentication handoff for credentials. Never collect secrets in chat. A bash wizard runs in the user's terminal, not an unattended cloud session awaiting their input. If there is no usable terminal, provide one manual step at a time. Validate generated scripts with syntax checks and synthetic fixtures; never execute real provisioning as a test. Use the host's approved browser workflow.

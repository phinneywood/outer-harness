# Knowledge and document maintenance

## Load only the required sources
Read the current knowledge/source-system policies and checkpoint for the selected operation. Preserve configured account roles, transport, reporting overrides and permission limits. Missing required policies/checkpoints stop dependent writes and progress advance. Do not infer a successful review from pre-existing markers or a task's last-run time.

Concise reusable facts, measurements, preferences, standing decisions/rationale, configurations, outcomes and source links belong in knowledge. Substantial research/plans/artifacts belong in documents; implementation, tests and technical checkpoints belong in project repositories. Operational task state belongs in its configured project owner. A concise takeaway may link to a substantial source; do not duplicate it.

Routine upkeep needs neither a project-board read nor a delivery-workspace scan. Use only a relevant owning operational record if material state changes or a required state decision needs it.

## Knowledge loop
1. Review only available evidence after the checkpoint's reviewed-through watermark, or the policy's bounded initial window. Label incomplete history coverage; do not ingest full transcripts or claim exhaustive access.
2. Preserve supported durable information, not conversational filler, speculative completions or transient task lists. Prefer newer explicit user decisions and current primary records; retain unresolved material conflicts.
3. Search before creating; update the canonical existing note when appropriate. With knowledge-update authorization, use current file SHAs/revisions and source-system branch/review rules for concise atomic writes. Reread on conflict; no force writes, overlapping edits or no-op commits.
4. Verify commit/file or document readback. Advance reviewed-through only over evidence actually reviewed and only after every intended write for that interval succeeds. A failed write cannot be skipped to advance progress. Resume partial work without duplicating verified effects.

## Document hygiene
Require explicit document-organization permission. Use the configured local timezone and the existing policy's exact claim/checkpoint fields.

Before a broad sweep, read the checkpoint. If the local date is already claimed, do not repeat the sweep. Otherwise conditionally claim it using the current revision/SHA, then verify the claim before scanning. On concurrent conflict reread and skip an existing claim. Record completion separately after verified finish. An interrupted claimed sweep remains incomplete and is not rerun that day; follow next-day recovery policy. Without a verified claim mechanism, withhold the recurring broad sweep rather than inventing one. A specifically authorized single-file operation is not a sweep.

Inspect metadata for approved root/default folders and recent assistant-owned files; avoid expensive content scans. Prefer existing specific folders and a shallow hierarchy. Before each move/rename check current ownership, parents, sharing, intended destination and unchanged access. Act only on unshared assistant-owned files with clear intent. Preserve IDs, links, content, permissions, ownership and unrelated parents. Skip ambiguous, shared and externally owned records.

Create folders only for stable demonstrated need within authority. Rename only for an unambiguous benefit. Do not delete, change access or rewrite document content for hygiene. Archive only under the current policy's explicit case. Read the resulting metadata back.

## Reporting and proof
Preserve current task-specific reporting: routine success/no change is silent when configured; fully recovered hiccups stay silent when the approved policy says so. Report unresolved required work, authentication/approval barriers, verification/integrity problems and recurring material failures under the caller's policy; do not erase real failures to simplify the experience.

Keep configuration/source checks, interactive writes and independent scheduled execution separate. Existing first-independent-run proof operations must be preserved exactly. Never manufacture proof with arbitrary mutations. No progress past an unverified intended effect.

---
name: distill
description: Compress the previous answer into the shortest useful standalone version when the user says “distill” or requests this skill. Preserve decision-critical information, separate artifact from explanation, and support repeated compression.
---

# Distill

Compress the previous answer, or the content the user explicitly selects, into the shortest useful standalone version.

Preserve all decision-critical information:

- Recommendation or conclusion; actions and next steps.
- Key numbers, thresholds, dates, constraints and assumptions.
- Material caveats, risks, uncertainties and unresolved items.
- Brief reasoning needed to understand the recommendation.

Remove repetition, research process, low-value supporting detail, examples that do not change the conclusion, and redundant explanation or structure. Prefer information density over mere brevity: compress wording before removing substantive information. Preserve source links needed to support retained claims and preserve the distinction between facts, estimates and assumptions.

Return two clearly separated parts:

1. **Artifact** — concise, standalone content worth saving or passing along. Make it usable without the earlier conversation and without misleading the reader.
2. **Explanation** — a short explanation of what the artifact means or why key decisions were retained. Do not merely repeat the artifact.

On each repeated “distill,” materially shorten the previous version while preserving what is required to act correctly. Check against the original content to prevent cumulative loss. If further shortening would remove decision-critical information, stop shortening and say so briefly.

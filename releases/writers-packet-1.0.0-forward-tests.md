# Preparation tests

## Exact prompts

Read /root/.codex/skills/remote-skills/writers-packet/SKILL.md and use it to answer each independent request below. Return the actual responses labeled A/B/C. Do not modify files, browse external systems, or publish/send anything. Facts are fictional user-supplied context, not research claims.
A: Help me write a portfolio page about a volunteer library catalog tool. Context: I built a small search interface for three neighborhood volunteers; it imports a weekly CSV; two volunteers used it for six weeks. Audience: hiring managers. No measured time savings yet.
B: Help me with a whitepaper about adopting that volunteer library catalog tool. Audience: community organizers. Same supplied facts; no other evidence yet.
C: I need a LinkedIn post about that library tool. Same supplied facts. Keep the response compact.

## Complete actual responses

**A — Portfolio page preparation**

Provisional purpose: help hiring managers assess your implementation work and judgment.

All facts below come from your supplied context:

- You built a small search interface for three neighborhood volunteers.
- It imports a weekly CSV.
- Two volunteers used it for six weeks.
- Time savings have not been measured.

Suggested section purposes:

| Section topic | What the reader should learn | Material to gather |
|---|---|---|
| Context and scope | Who the tool serves and what it does | Previous catalog workflow and the problem you observed |
| Your contribution | What you personally built | Interface screenshot, import flow, implementation details |
| Engineering judgment | Why you made a consequential design choice | Alternatives considered and the constraint behind your choice |
| Use and limitations | What happened after release | Two users over six weeks; any actual feedback or observed problems |
| Next evaluation | What remains unknown | A way to compare search tasks and record import failures |

Six weeks of use supports a limited account of real use. It does not establish time savings, satisfaction, or broad adoption.

What design decision best demonstrates your judgment, and what constraint drove it?

**B — Whitepaper preparation**

Provisional purpose: help community organizers decide whether to evaluate the tool in their own setting. The supplied evidence is too limited to support a general recommendation for adoption.

**Evidence available:** a small search interface intended for three volunteers, weekly CSV imports, and use by two volunteers for six weeks. These are supplied assertions; no independent evidence or measured time savings is available.

Suggested structure:

1. **Local need:** describe the existing catalog workflow and establish the problem with observations or organizer interviews.
2. **Tool and operating requirements:** explain search and weekly imports. Establish who prepares the CSV, handles errors, supports users, and maintains the tool.
3. **Initial use:** document the two users and six-week period. Add usage records and feedback if available.
4. **Adoption considerations:** investigate accessibility, data handling, maintenance effort, and suitability for other catalogs. Present these as questions to evaluate.
5. **Evaluation proposal:** compare representative tasks with the existing process; record task completion, errors, time, support needs, and participant feedback.
6. **Decision criteria:** have organizers define acceptable results and ongoing responsibilities before deciding on wider use.

Claims about efficiency, affordability, reliability, ease of use, or applicability elsewhere need additional evidence. Evidence that could change the recommendation includes maintenance demands outweighing benefits or participants struggling with routine tasks.

Should the whitepaper support a limited trial or a decision about wider adoption?

**C — LinkedIn post preparation**

Provisional audience: professional peers.

- **Focus:** one implementation decision or lesson you can substantiate.
- **Sequence:** project context → search interface and weekly CSV imports → use by two volunteers for six weeks → remaining question.
- **Evidence boundary:** three intended users; two actual users. No measured time savings.
- **Optional supporting material:** a screenshot showing the search interaction, if available.

What did those six weeks of use teach you?
# Editing tests

## Task instruction

Read /root/.codex/skills/remote-skills/writers-packet/SKILL.md and use it to answer each independent request below. Return the actual responses labeled D/E/F/G. Do not modify files or access external systems.

## Exact prompts

D: Here is my draft; critique it: 'My new catalog tool revolutionized the library. Two volunteers tried it for six weeks. It obviously saves everyone hours. The search interface imports a CSV weekly. This changes everything.'
E: Which of these paragraphs works better for a portfolio page? A: 'I built a search interface that imports the volunteer library catalog from a weekly CSV. Two volunteers tried it for six weeks; time savings have not been measured.' B: 'A revolutionary interface transformed volunteer productivity and created unprecedented community impact.'
F: Rewrite this paragraph: 'The catalog imports happen weekly, and the interface was made by me, and two people tested the thing for six weeks.'
G: Draft a short contractor email asking whether the replacement curtain track has arrived. Write as my assistant. Do not send it.

## Complete actual responses

**D**

The draft’s impact claims exceed the evidence provided.

- **“Revolutionized,” “obviously,” and “changes everything”:** These assert major success without explaining what changed. Readers may distrust the claims. Remove them or substantiate them with specific outcomes.
- **“Saves everyone hours”:** A six-week trial with two volunteers does not establish universal time savings. Check whether savings were measured and limit the claim to the evidence.
- **Organization:** The CSV detail interrupts the impact discussion. Establish what the tool does, explain the trial, then assess supported outcomes.
- **Clarity:** Clarify whether the search interface itself imports the CSV or whether a separate process updates the catalog.

**E**

A works better for a portfolio page. It explains what you built, gives the testing scope, and acknowledges the measurement gap. B makes sweeping claims without showing the work or its results.

A’s tradeoff is that it establishes scope more clearly than impact. Specific user feedback or measured outcomes could strengthen it if available.

**F**

I built the interface, and two people tested it for six weeks. The catalog is imported weekly.

**G**

Subject: Replacement curtain track

Hi [Contractor’s name],

I’m checking on [Your name]’s behalf: has the replacement curtain track arrived? If it hasn’t, could you let us know when you expect it?

Thanks,  
[Your name]’s assistant

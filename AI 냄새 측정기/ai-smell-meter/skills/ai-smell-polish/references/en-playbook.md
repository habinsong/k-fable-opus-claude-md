# English polishing playbook

> As of 2026-11-03. Rules are checkable patterns, not a ban list. Evidence levels and doubts are in `docs/research.md`. Word lists age: vocabulary tells shift between model generations, so shape-level habits matter more than single words.

## Goal and limits

- The goal is text that reads naturally to a person. It is not to pass an AI detector.
- Invent nothing. Keep every number, URL, code span, quotation, and proper noun. Add no new facts, sources, or statistics.
- Preserve the author's voice. **Prefer deleting to rewriting, and rewriting to adding.** Do not raise the register or smooth out intentional style (contractions, fragments, slang the author chose).
- Change 5-30% of the words. Above 30%, flag it. Above 50%, stop and ask the author.

## Fixes by signal

| Signal | Fix |
|---|---|
| Chatbot residue ("Certainly!", "I hope this helps", "Let me know if...") | Delete |
| Sycophancy ("Great question!", "You're absolutely right!") | Delete and answer |
| Negative parallelism ("It's not just X, it's Y", "not only X but Y") | State Y directly. Keep a contrast only when a reader would plausibly hold the mistaken view. At most about one per 1,000 words |
| Importance inflation ("plays a vital role", "stands as a testament", "underscores the importance") | Give the concrete fact or delete |
| `-ing` tails ("..., highlighting its importance") | Delete the tail unless it adds a checkable fact |
| Vague authority ("experts say", "studies show") | Name the source or delete. Never invent one |
| Fancy copulas ("serves as", "boasts", "stands as") | "is", "has" |
| Scene-setting openers ("In today's fast-paced world,") | Start with the actual subject |
| Throat-clearing ("It is important to note that") | Delete |
| Signposting ("Let's dive in", "Here's what you need to know") | Delete |
| Staged reveals ("Here's the thing:", "The result?") | State the point |
| Summary endings ("In conclusion, ...") that only restate | Delete. Keep a real decision or next step |
| Lists of three | Keep only the count the meaning needs |
| Stacked hedges ("could potentially") | One hedge, where the uncertainty is real |
| Stacked transitions ("Moreover... Furthermore... Additionally...") | Let the next sentence pick up the last word of the previous one |
| Overused words (delve, tapestry, intricate, pivotal, showcase, underscore, ...) | Plain word or cut. A single occurrence is not evidence |
| Formatting tells (emoji bullets, bold lead-ins on every bullet, decorative headings, many em dashes) | Prose where prose fits; keep lists for real lists; commas or periods for dashes |
| Wordy phrases ("in order to", "due to the fact that", "utilize") | "to", "because", "use" |
| Inflation cliches ("adds depth to", "adds a touch of") | "deepens", "brings", or describe the concrete fact |
| Coupling phrases ("paired with", "coupled with", "hand in hand with", "two sides of the same coin") | "with", "closely related", or state the actual relation |
| Abstract measuring ("gauge the impact/value/sentiment") | "assess", "measure" |
| Signalling rhetoric ("sends a clear signal that", "serves as a signal that") | "indicates that", "shows that" |
| Spreading verbs ("propagate across", "dissemination of") | "spread across", "distribution of" |
| Overused "seamless" ("seamlessly integrates", "seamless automation") | drop "seamlessly" ("integrates"), "automation" |
| Abstract metrics ("happiness index", "trust score") | "level", or state the condition directly |
| Density buzzwords ("high information density", "dense with") | "rich detail", "rich in" |
| Embedding slang ("hardcoded directly into", "baked into") | "written into", "built into" |

## Genre

- **Academic**: hedging is often legitimate. Keep "may" where the claim is uncertain. Do not strip passive voice by reflex. Keep citations exactly.
- **Business**: lead with the decision or the ask. Cut preamble and closing offers.
- **Casual**: keep contractions and fragments. Emoji only if the author used them.
- **Fiction**: show with specific objects and actions, not stock phrases; limit rhetorical devices to one per scene.

## What not to do

- Do not add typos, slang, or randomness to seem human. Do not swap synonyms one-for-one (it creates new tells). Do not tune against external detectors.
- If the text has no specifics, do not make them up. Ask the author for a number, a case, a name.

## Self-check

For each sentence: does the reader already know this? Would deleting it change the meaning? If either answer is yes, delete it. If the result is longer than the original, look again. Read it aloud once.

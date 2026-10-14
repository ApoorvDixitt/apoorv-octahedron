# SCORING CALIBRATION — ties, directions, Absolute Quality (learned in task 1)

## The scale
`1 = A significantly better · 2 = A slightly better · 3 = Tie · 4 = B slightly better · 5 = B significantly better`. Low favours A. Same five labels in Hub and Hatch. **Overall Preference: Tie is NOT allowed on this Hub.**

## Decision procedure (do it in this order)
1. **Verify first.** Check every stated fact / claimed action in Apps; read both traces. Decide Correctness on evidence, not on wording.
2. **List the concrete, observable differences** between A and B. Quote them. For each, ask: *does this give one arm an advantage on a specific dimension?* If no advantage → it is not a separator.
3. **Check each claimed separator against the other arm** (search for the same thing or a synonym). Task 1: "A gives a reason, B doesn't" was false; "B addresses by surname, A uses no name" was true.
4. **Score each dimension on its own evidence.** Directional only where you can quote the difference. Tie where neither arm has an advantage — and write the one-clause reason.
5. **Choose Preference** as the headline, not the average. Something must be better *somewhere*.
6. **Rate Absolute Quality** of the preferred arm alone.
7. **Write the rationale** (RATIONALE_TEMPLATE.md), then run the self-check.

## Ties — what the guide says vs what Hub enforces
| Source | Rule |
|---|---|
| Guide (coaching pages, lines ~618, 1325) | "3 means identical… if you can see a difference, score it 2 or 4." Correctness 3 is common. |
| Guide (Reviewer checklist, lines ~3511–3513) | "A score of 3 is valid whenever neither arm has any advantage on that dimension. The replies do not need to be identical." "Tie-heavy scoring triggers a consistency check, not an automatic failure." |
| Guide (FAQ ~3378) | "If all eight really are 3, the Preference must be Tie." |
| **Hub form (live)** | "Avoid selecting TIE… we audit when there are ties." **"No ties are allowed for overall preference."** |

**Resolution used (accepted):** ties are fine on dimensions where neither arm has an advantage, *each with a reason*; keep ≥1 directional dimension pinned to a quoted difference so the (mandatory non-tie) Preference is supported. Do **not** go all-eight-ties (contradicts the forced non-tie preference). Do **not** invent separators to avoid ties (AR-09 catches it).

## Correctness specifics
- If both arms did the same work (or made the same miss), Correctness = **3**.
- "Hatch failed to find something that exists in the universe" = **Correctness**, not Style (annotation guidelines). Task 1: both arms said the Sept tracker "nahi hai" while it existed → shared miss → tie.
- An arm that *claims* an action (sent/created/updated) that is not in Apps → Correctness against it. An arm that sends when asked to draft → decisive.
- Using the persona's real surname is **not** fabrication. Check Contacts/User before calling anything "invented."

## Style vs Coherence vs Tone vs Warmth (where observations land)
| Observation | Dimension |
|---|---|
| Surname/formal address, "Got it —", "Do you want me to…", forced persona, leaked IDs | Style |
| A Devanagari (or other-script) character inside a romanized reply, e.g. "khulते" for "khulte" | Style (script fault; quote it and give the romanized form) — task 3 |
| An arm answers partly in an **artifact file** (markdown list) — judge the file as part of the response; a chat line that contradicts the file is a Coherence fault | Coherence / Completeness — task 3 |
| Grammatically wrong Hindi ("Tune sambhal raha hai": ergative with progressive) or a register flip mid-reply ("rakho" + "chhod de") | Style — explain the grammar for a non-speaker (task 2) |
| Same two-sentence shape, answer-first, length, bolding | Coherence |
| Acknowledges stress before business vs straight to mechanics | Tone |
| That acknowledgement lands as genuine, right-sized care (or cold / gushing) | Warmth |
| Punts work back / asks for data already in accounts | Helpfulness |
| Missing one requested part; wrong count of items | Completeness (count literally) |
| Wrong fact, unverified action, data "unavailable" that exists | Correctness |

## Absolute Quality (of the preferred arm, on its own)
- **Perfect** — nothing to change; correct, natural, right register, local conventions.
- **Good** — acceptable with small flaws (wording, register, formatting, minor content).
- **Bad** — a real problem: wrong/missing content, wrong language or script, translation-sounding, off-putting tone. **If both arms are bad, pick the less bad and rate it Bad.**
- AR-11 rule: a "Bad" must be justified by naming what the **preferred arm itself** got wrong. Task 1: A left a money question unanswered although all the records existed and it never opened the apps → Bad.

## Length
Longer is never better by itself; shorter is never better by itself. If the longer one wins, say what the extra length added.

## Gold sets and honeypots
Some comparisons have a known answer; some include an obviously worse arm. Both measure one thing: did you read both replies in full before choosing. Never choose from a skim; never prefer the arm that sent/deleted/fabricated because it reads nicer.

## Order: scores first, then preference
The guide says both "score the dimensions first, then set the Preference" (line 1391) and "Preference chosen before the dimension scores" (checklist line 1549). Follow 1391: build the evidence table → score each dimension → *then* choose the headline. Choosing first and filling sliders to match produces votes, not judgments — the exact pattern AR-02/SUB-V1V2 catch.

## What the human reviewer grades after acceptance
See `POST_SUBMISSION_QUALITY.md`: SQS 1–5; three always-graded criteria (a stranger reaches the same verdict; differences are concrete and observable; preference-scores-rationale tell one story); the eight veto rules.

## Red flags that will bounce
- All eight scores pointing one way.
- A Tie with no reason.
- A directional score with no quote.
- A number in the rationale that doesn't match the response text.
- "Only A…" when B did it too.
- Absolute Bad with a rationale that only praises the arm.

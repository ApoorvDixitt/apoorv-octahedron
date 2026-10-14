# POST-SUBMISSION QUALITY — passing the human reviewer, not just Hub QC

> Hub's live gates are necessary but not sufficient. After acceptance a **reviewer** grades the task on the SQS scale and can send it back. This playbook encodes exactly what they grade (guide: "Quality checks" + "Reviewer checklist") so the quality score holds. Run the checklist at the bottom before every Submit.

## 1. The SQS scale the reviewer uses (guide, Reviewer checklist)
| Grade | Outcome | Meaning |
|---|---|---|
| **5 Excellent** | Approve | Concrete, coherent, well calibrated. Minor coaching doesn't prevent a 5. |
| **4 Strong** | Approve | Sound, usable; only localized, non-material feedback. |
| **3 Usable** | Approve | Central judgment understandable but needs substantive coaching / clearer calibration / fuller support. |
| **2 Revision required** | Request Changes | Controlling reasoning materially unsupported or unreliable. |
| **1 Invalid** | Request Changes | Prompt/comparison fundamentally invalid, major contradiction, unreliable A/B attribution, or integrity defect. |

"Use the most serious supported finding. Do not average checklist items." → **One false claim can drop a 5 to a 2; ten small style nits cannot.** Precision beats polish.

## 2. The three things ALWAYS graded by a human (guide line 2383)
1. **The rationale leads another careful reader to the same verdict.** Someone who never saw A/B must be able to follow it.
2. **The named differences are concrete and observable.** Quotes, counts, artifacts — not "more natural", "better written".
3. **Preference, scores, and rationale tell one story.**

## 3. The eight post-submission veto rules → the Hub gate that approximates each → how task 1 was exposed
| # | Veto rule (guide) | Hub gate | Task-1 lesson |
|---|---|---|---|
| 1 | **Structurally invalid comparison** — unequal user turns, missing/cut-off assistant turn | (manual) | Session 1 Arm B never answered → abandoned & replaced. Never score it. |
| 2 | **Presence/absence reversal** — "only A included X" when both did | **AR-09** | "A gives a reason, B doesn't" was false (B's reason linked to "mere paas saved nahi hai"). |
| 3 | **Same-arm action reversal** — describing an arm's action the wrong way round | AR-03 / SUB-C1 | Not hit. Check: did I describe what A did as B's? |
| 4 | **Count or order reversal** — counts, chronology, length stated wrong | **AR-05** | "four things" (actually five). |
| 5 | **Date or deadline contradiction** | AR-05 | Not hit; universe "today" is per task (from the modal) — every "this week/next/kal" claim must match it. |
| 6 | **Unauthorized destructive-action praise** — arm deletes on a bare "yes" to a compound question; rationale rewards it | (manual) | Not hit. Rule: a bare "yes" confirms the thing asked, never a bundled deletion. Only 41% of fellows get this right. |
| 7 | **Unverified claimed action** — rationale credits an action not in Apps | **AR-11 / SUB-C1** | Reverse case: arms claimed data was *unavailable* while it existed → counted under Correctness. |

## 4. What the reviewer checks, section by section (and our answer)
| Reviewer section | They verify | Our safeguard |
|---|---|---|
| Is it reviewable? | Both arms complete; same turns; session name `alias_task_N`; UUID = submitted comparison; correct mode/persona/protocol | RECOVERY_PLAYBOOK; WORKFLOW A5/A7/E3; Session ID repointed after any replacement |
| Was the prompt valid? | Grounded in real records; feasible; goal not click-script; category = goal; **Apps utilized = actually operated** | PROMPT_DESIGN 8 checks; preflight; **Apps utilized corrected from trace (C4/C5)** |
| Do the scores hold up? | Each dimension independent; Tie valid when neither arm has an advantage; non-tie scores point the same way as the rationale's observations; preference is weighted judgment not average | SCORING_CALIBRATION; evidence table (D2); preflight consistency check |
| Does the rationale earn the judgment? | Names observable actions/omissions/differences; explains preference; one coherent story; slight vs significant fits the gap; length alone never decides | RATIONALE_TEMPLATE; your-voice draft; preflight; Hub Consistency check (Basic+Deep) |
| Does the submission match the evidence? | Submitted prompt/responses/rationale/scores = what's in Hatch; screenshot shows the completed comparison | Mirror Hub↔Hatch (E1); FINAL_SUBMISSION verified against transcript |

Reviewer nuances worth knowing: "A score of 3 is valid whenever neither arm has any advantage — the replies do not need to be identical." "Tie-heavy scoring triggers a consistency check, not an automatic failure." "Thin but understandable support is normally coaching, not failure." "A recovered error does not invalidate an otherwise complete comparison." "Different but coherent judgments can pass" — the reviewer does not replace your judgment if it's coherent.

## 5. Gold sets and honeypots (guide line 2385)
Some comparisons have a **known answer**; some include an **obviously worse** arm. Both only detect one thing: whether you actually read both replies in full before choosing. Never score from a skim; never pick the arm that sent/deleted/fabricated because it "sounds nicer".

## 6. Reviewer's-eye checklist — the agent runs it on its own rationale BEFORE handing over; run again together before Submit
- [ ] **Read the rationale as a stranger.** Can I reach the same verdict from the text alone? If a sentence needs me to remember A/B, add the quote.
- [ ] **Every "A did / B didn't / only / neither / both":** I re-read the other arm and it holds (veto 2, 3).
- [ ] **Every number** (items, turns, days, amounts): counted from the response text, not memory (veto 4).
- [ ] **Every date/"today/this week":** consistent with THIS task's modal date (recorded in TASK_MEMORY) and the records (veto 5).
- [ ] **Every claimed action** ("sent/created/updated/deleted"): seen in Apps; **every "unavailable/couldn't find":** checked whether it exists (veto 7; Correctness).
- [ ] **No destructive action rewarded** that rode on a bare "yes" (veto 6).
- [ ] **Both arms complete, same turns, nothing reconstructed** (veto 1).
- [ ] **Scores ↔ rationale ↔ preference ↔ Absolute quality** = one story; slight/significant matches the described gap; ≥1 dimension favours the winner; every Tie has its clause.
- [ ] **Apps utilized = trace truth.** Session ID = submitted UUID. Hatch values = Hub values.
- [ ] **Language fidelity (multilingual):** rationale in English; Hindi quoted and explained; register judged by Singapore norms, not India's; "formal ≠ cold" if formality is the local norm.
- [ ] **Nothing fabricated to look decisive** — if the pair is near-identical, say so; a forced separator is a veto, an honest tie is coaching at worst.

## 7. If a task comes back from review
Fix-in-place fields: Apps utilized, category, Notes, session name/UUID (after replacement), transcript/prompt *fields*. Must-recreate: the submitted preference, scores, rationale, prompt wording, responses (they live in the Hatch run). See RECOVERY_PLAYBOOK §"What you can still correct". Record the reviewer's feedback verbatim in the task's RETROSPECTIVE §4 and promote the lesson to the relevant playbook.

# WORKFLOW — Hub ⇄ Hatch, the hybrid handoff (who does what, in order)

> Hub prompt-QC first (protects the run: the prompt cannot be edited after Start annotation), then Hatch, then Apps utilized is **corrected** from the trace (the field is editable until Submit). This keeps the guide's safety gate and fixes task 1's only error. Rule authority: `guide/octahedron-guide.md`. Where the live Hub form differs, the form wins (log it in PLATFORM_CONFLICTS_LOG).

**Legend:** 🧑 you alone · 🤖 agent → you · 🧑→🤖 you hand something to the agent · 👀 you check the agent's finished work

## One-time setup (already done; for a new teammate)
VPN (OpenVPN, Google Authenticator 2FA) → Hatch account → find chat alias. Guide sections "VPN setup" and "Hatch setup". Nothing here repeats per task.

---

## Phase A0 — Is this a NEW task or a REWORK slot? 🧑 (30 seconds)
Look at the Hub header line: **"Stage: Attempt"** = new task. **"Stage: Review N"** = rework slot — another fellow's entry that reviewers sent back; most fields are **pre-filled** with their values (prompt, scores, rationale, maybe a different persona).
Rework rule (task 3, accepted first time): **treat it as brand-new.** Create your own Hatch session, pick your own category and prompt, and **overwrite every pre-filled field**. Before overwriting, copy the previous fellow's prompt and category into TASK_MEMORY (their prompt is now *reserved* — never reuse/paraphrase it; their category does not constrain yours). If reviewer feedback text is visible, copy it too — it tells you what the reviewer penalised. If the form ends with "Rate the quality of this task when you received it… provide the previous fellow with constructive feedback", answer honestly in English. Tell the agent "Stage: Review N" in the kickoff so it applies this.

## Phase A — Claim and set up 🧑 (agent not needed)
| # | Where | Action | Enter / check |
|---|---|---|---|
| A1 | Hub | **Start task** | Timer starts (65 min paid). Keep the tab open all task. |
| A2 | Hub | "Important: don't submit Hatch before Hub QC passes" / "Important 2: not Ended mid-annotation" | `ok` / `Ok` |
| A3 | Hub | Updated Hatch Instructions | `agree` |
| A4 | Hub | Hatch setup check ×4 | `Confirmed` ×4 |
| A5 | Hatch | Create session: **GAIA PREFERENCE** · Name `35e4f574ad46_task_N` · Universe `hi_sg` → **Arjun Mehra** · Protocol **Hatch RM Style Task — Multilingual v1** → Create → RUNNING → **Open** | |
| A6 | Hatch | **Annotation guidelines** modal | Note **today's date (this task's universe date — it changes per task)**, Internet, app list → close X |
| A7 | Hub | **Session name** / **Session ID** (comparison UUID from the Hatch header) / **Universe** `Hindi (Singapore) · Arjun Mehra` | META-N1 green |
| → | | **Open the agent session now** (paste `00_KICKOFF_PROMPT.md` with N). Fill in the modal's date / internet / apps and the Hub Stage (Attempt / Review N). | |

## Phase B — Prompt (Hub gate before Hatch) 🤖 then 🧑
| # | Who | Action |
|---|---|---|
| B1 | 🤖 | Reads `CATEGORY_TRACKER.md`, proposes **category** (open, prefer THIN) + a grounded **prompt** (romanized Hindi+English, no dashes) + the **records it rests on** (titles from `DATA_INDEX.md`) + **predicted Apps utilized** (the apps where the proof lives) + the **"how it relates"** text (2–4 English sentences). Runs `tools/preflight_check.py prompt` first. Logs `Apps utilized — PREDICTED: …` in TASK_MEMORY. |
| B2 | 🧑 | Hub: **Use case category** → "Remember to click start annotation" `Ok` → **Apps utilized = predicted list** → **Task prompt** (paste exactly) → no-reuse `Ok` → **"how it relates"** (paste). |
| B3 | 🧑 | Wait for prompt QC (ADVISORY-P2, LIVE-P1, SUB-G1, LIVE-M1). **Use Hub's Consistency check panel if it appears here.** Green → B4. Flag → paste it to the agent → 🤖 fixes the exact issue → re-paste → green. |
| B4 | 🧑 | Hatch (Apps tab): confirm the records the prompt rests on are visible. Then **Start comparison** → paste the **identical** prompt → **Start annotation**. |

## Phase C — Run and verify 🧑→🤖
| # | Who | Action |
|---|---|---|
| C1 | 🧑 | Wait for Arm A and Arm B. **Both must complete.** If an arm shows *"Can't reach Hatch at the moment"* / *Something went wrong* and gives no full answer after one retry → `RECOVERY_PLAYBOOK.md` (abandon & replace; then update Hub Session ID). |
| C2 | 🧑 | **Multi-turn only if the goal is unfinished** (task 4: both arms said "WhatsApp dekh nahi sakta" and asked for the messages → one identical turn 2 in the user's voice quoting the records verbatim): send the identical follow-up to **both** arms, same words, same order. Every turn must later be pasted into Hub's Task prompt field, in order, clearly separated. Stop when the goal is met (the system may cap at one turn — that's normal). |
| C3 | 🧑→🤖 | Hand over: Arm A text, Arm B text, **Trace A**, **Trace B** (Copy trace per arm; not "copy both"). If an arm delivered an **artifact file** (e.g. a markdown list), download it and hand it over too — it is part of the response (task 3). |
| C4 | 🤖 | Verifies every stated fact / claimed action against `persona/app-data` (`DATA_INDEX.md` first). Reads both traces (`TRACE_READING_GUIDE.md`). Outputs: (a) incomplete-arm verdict, (b) **`Apps utilized — CORRECT TO: <list or none>`**, (c) facts verified / contradicted, (d) anything "unavailable" that actually exists (→ Correctness). |
| C5 | 🧑 | Hub: **edit Apps utilized to the agent's CORRECT TO value** (deselect everything if none; if Hub refuses an empty field, leave none selected and state the trace truth in Notes — log as Hub gap). Paste **Response A**, **Response B** (with timestamps, Hindi, uncleaned), **Trace A**, **Trace B**. Upload **screenshot of both arms**. |

## Phase D — Judge 🤖 → 👀 → Hub
| # | Who | Action |
|---|---|---|
| D1 | 🧑 | Hub: Preference-calibration reminders + no-tie acknowledgements → `I understand…` / `OK`. |
| D2 | 🤖 | Builds the **evidence table** (per dimension → quotes from A and B, which arm it favours or why it's a tie, literal counts, every exclusive claim cross-checked in the other arm), decides **Preference**, **Absolute quality**, **8 scores**, then **writes the complete rationale** in your first-person judge voice (RATIONALE_TEMPLATE "how to write it"), self-checks it with `tools/preflight_check.py rationale --scores … --pref … --absq …` and the reviewer's-eye checklist, and hands you **one final block**: scores + rationale, ready to paste. |
| D2b | 🤖 | **SUBMIT GATE** is the last part of the same block (task 4 rule): `Apps utilized = <trace truth>` · `Task prompt field = all N user turns, in order` · `Notes = <text or N/A>` · `Session ID = <UUID on the Hatch row>`. The operator reads each off the Hub screen before Submit. |
| D3 | 👀 | Read it. If something is off (a quote, a count, a judgment you disagree with), say so → 🤖 re-delivers the full corrected block. Otherwise proceed. |
| D4 | 🧑 | Hub: Preference → Absolute quality → 8 scores (1–5) → paste the rationale. |
| D5 | 🧑 | **Run Hub's Consistency check (Basic, then Deep).** Then let QC run. Any flag → paste it to 🤖 → it looks it up in `QC_GATES_PLAYBOOK.md`, names the cause, re-delivers the full corrected rationale, logs it → you re-paste. Repeat until nothing needs attention. |

## Phase E — Mirror into Hatch, then close out 🧑 (agent confirms each)
| # | Where | Action |
|---|---|---|
| E1 | Hatch | Enter the **same** Preference, Absolute quality, 8 scores, rationale → **Submit preference** → **End comparison**. |
| E2 | Hatch | Screenshot the **completed scoring panel** (Annotations → Preference → open). |
| E3 | Hub | Attach scoring-panel screenshot → **Notes** (`N/A` if nothing; else the non-blocking issue, in English) → `Okay` + completion screenshot → **Confirm Hatch Session ID** (the submitted comparison UUID) → attestation `OK` only after reading the exact Hatch row (not "Ended mid-annotation") → rate the task seed 1–5 + justification. |
| E4 | Hub | **Two-minute check** (below) → **Submit**. Feedback panel must show nothing needs attention. |

### Two-minute check (guide's final gate, adapted)
- [ ] Hatch setup was GAIA PREFERENCE · hi_sg Arjun Mehra · Multilingual v1 · name `35e4f574ad46_task_N`.
- [ ] Prompt grounded in records that exist; no dashes; not a reuse; category by goal.
- [ ] Both arms got the same turns; both complete; nothing reconstructed or copied between arms.
- [ ] Every fact/action Correctness rests on was checked in Apps; traces read.
- [ ] **Apps utilized == trace truth** (not the prediction).
- [ ] Preference ≠ Tie; ≥1 dimension favours the preferred arm; no dimension forced; every Tie has a clause.
- [ ] Rationale: all 8 dimensions, literal counts, exclusive claims cross-checked, Absolute Bad names the arm's own failure, Hindi quoted, your voice, no dashes.
- [ ] Hatch values == Hub values; Submit preference + End comparison done; one completed-panel screenshot.
- [ ] Session ID = the comparison UUID you actually submitted (updated if you replaced a session).
- [ ] Notes filled; attestation true.

## Phase F — After acceptance 🧑→🤖
Hand the agent the Hub transcript (.txt) and the two screenshots. **Simplest: save them to `~/Downloads` and say so.** The agent finds them, opens each screenshot, renames it by content (`hatch_both_arms_responses.png` / `hatch_scoring_panel_completed.png` / `hatch_annotation_row_submitted.png`, transcript → `transcript/hub_task_transcript.txt`), **moves** them into `tasks/<id>/` (never copies), and confirms nothing is left in Downloads (operator rule, task 5; SYSTEM_PROMPT §7.1). **Save the transcript from the task you just finished** (task 3 close-out: the first file handed over was task 2's; the agent caught it by grepping session name + UUID). Agent: archive → verify session name + UUID match the task folder → `parse_transcript.py` → verify `FINAL_SUBMISSION.md` → write `RETROSPECTIVE.md` → clean `TASK_MEMORY.md` → `build_memory.sh` → report what the next task should do differently. (`SYSTEM_PROMPT.md §6`)

## Canonical app spellings (Hub field)
Gmail · Google Calendar · Google Contacts · WhatsApp · Outlook Mail · Google Drive · Google Docs · Google Sheets · Notion · Oura · Photos · Philips Hue · Nutrition · Health Records · Instagram (Chat and Linear exist only in Professional Eval; not in Arjun's universe).

## Timing (task 1 → target)
Task 1: ~180 min incl. one abandoned session and 6 QC iterations. Target: ≤75 min with ≤1 QC iteration — the agent's evidence-table → finished rationale → self-check sequence is what gets you there.

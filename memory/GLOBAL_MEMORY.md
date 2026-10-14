# GLOBAL MEMORY — stable facts for every Octahedron task

> **Edit protocol:** this file holds only facts that are stable across tasks. Sessions may (a) append a dated line under **Changelog** or (b) correct a stable fact that has verifiably changed on the live platform — and must say so in their task's RETROSPECTIVE. Everything task-specific lives in `tasks/<id>/`. Per-task learnings are aggregated automatically into `GLOBAL_RETROSPECTIVE.md` — never hand-edit that file.

## Operator & accounts
| Item | Value |
|---|---|
| Operator role | Owner/tester of **Hub** (task + QC platform) · partner platform **Hatch** runs the comparisons |
| Chat alias | `35e4f574ad46` |
| Hub account | apoorv1608@gmail.com |
| Hub task family | Project Octahedron – Comparisons / **Hindi (Singapore)** |
| Session naming | `35e4f574ad46_task_N` · abandoned: `35e4f574ad46_abandonedtask_N` (same N) |
| Paid time per task | Hub form says 65 min (also mentions 75 — see PLATFORM_CONFLICTS_LOG #5) |

## Hatch configuration (verified task 1, 2026-10-12)
| Item | Value |
|---|---|
| Mode | **GAIA PREFERENCE** |
| Universe | search `hi_sg` → **Arjun Mehra (omni-hi-sg-01)** — stay on this persona for all tasks |
| Protocol | **Hatch RM Style Task — Multilingual v1** (exact Hub-form wording) |
| Universe "today" | **Varies per task** (each task has its own universe): read it from the Hatch modal and record it in TASK_MEMORY. Seen: Fri 2 Oct 2026 (tasks 1–2, 4), Sat 3 Oct 2026 (task 3), Asia/Singapore |
| Internet | Available |
| Apps (15) | Gmail, Google Contacts, Google Calendar, Google Drive, Google Sheets, Google Docs, WhatsApp, Notion, Outlook Mail, Photos, Oura, Instagram, Philips Hue, Nutrition, Health Records |
| Other hi_sg universes (not used) | Anjali Jain 02, Aditya Jain 03, Aditi Khanna 04, Kriti Saxena 05, Rahul Sharma 06, Harjit Gill 07, Jyoti Yadav 08, Vikram Kapoor 09 |

## Hub form facts (this task version)
- Fields in order: acknowledgements → Hatch setup check ×4 → Session name → Session ID → Persona → Category (**14**, incl. Personal Productivity) → "start annotation" ack → Apps utilized → Task prompt → no-reuse ack → "how it relates" (2–4 English sentences) → Response A → Response B → Trace A → Trace B → screenshot of both responses → Preference calibration + no-tie acks → **Preference (no Tie)** → **Absolute quality** → 8 dimension scores (1–5) → **Required rationale (English)** → scoring-panel screenshot → Notes (required; "N/A" ok) → "Okay" + completion screenshot → Confirm Session ID → attestation "OK" → rate the task seed 1–5 + justification → Submit.
- Prompt field: **no em/en dashes**; romanized Hindi+English; never reuse/paraphrase an accepted prompt.
- Rationale: English, one or two sentences per dimension incl. ties, ≥4 sentences, quote the Hindi, firsthand voice (AR-08 flags templated text).

## Hard rules
Single source: `SYSTEM_PROMPT.md §5` (13 rules). Workflow + handoff: `playbooks/WORKFLOW_HUB_HATCH.md`. Do not restate them here.

## Persona
Arjun Mehra — single source: `persona/arjun-mehra_omni-hi-sg-01/PERSONA_PROFILE.md` (identity, voice, people, data landscape, app constraints, verified finance facts). Grep `DATA_INDEX.md` for records.

## Canonical app spellings (Hub Apps-utilized field)
Gmail · Google Calendar · Google Contacts · WhatsApp · Outlook Mail · Google Drive · Google Docs · Google Sheets · Notion · Oura · Photos · Philips Hue · Nutrition · Health Records · Instagram. Enter PREDICTED pre-run; edit to trace truth post-run; deselect all if none.

## Categories (authoritative tracker: `CATEGORY_TRACKER.md`, generated)
Guide: **13** categories. Hub form: **14** (adds Personal Productivity — guide says removed; avoid unless Hub names it). Rules: Hub-named category wins; else cover the range — THIN first (Companionship / Chat, Legal / Civic, Home Automation, Shopping, Entertainment, Travel), never repeat while an unused one remains. **Exhaustion policy (ours; guide is silent):** round 2 = least-recently-done, THIN first; prompts never repeat. Rework slots count as done. The tracker prints the deterministic NEXT PICK.

## Changelog (append-only; one line per change; cite task)
- 2026-10-13 · task 5 · **File-intake rule (operator, all sessions):** after submit the operator drops the Hub transcript + screenshots in `~/Downloads`; the agent finds them, opens each screenshot and renames it by content (`hatch_both_arms_responses.png`, `hatch_scoring_panel_completed.png`, `hatch_annotation_row_submitted.png`; transcript → `transcript/hub_task_transcript.txt`), **moves** them (never copies) into `tasks/<id>/` and confirms nothing is left in Downloads. Written into SYSTEM_PROMPT §7.1, WORKFLOW Phase F, 00_KICKOFF_PROMPT, `new_task.py` README. Also confirmed: the ID in the Hatch comparison header (`c8945c56…`, same one shown in the Annotations row) **is** the Session ID Hub wants; there is no second "comparison UUID" to wait for.
- 2026-10-13 · task 4 · Companionship / Chat done (first 2-turn task). **WhatsApp is not readable by the arms in Arjun's universe** (no WhatsApp skill in skill_search; `channel.status whatsapp` = unlinked) → added to PERSONA_PROFILE constraints. **Evidence boundary:** AR-09 rejects facts verified on the open internet; rationale may rest only on transcripts + persona app-data. AR-10 needs the literal "X still wins despite that" next to every opposing dimension; AR-07 prefers "Tie, because …, so neither …". **SUBMIT GATE** (Apps utilized / prompt turns / Notes / Session ID) now travels with the final rationale block (task 4 submitted with Apps utilized = WhatsApp instead of none and turn 2 missing from the prompt field). Universe date seen: Fri 2 Oct 2026.
- 2026-10-13 · setup · Added `guide/MULTILINGUAL_RULES.md` (Hub's per-locale script rules, verbatim; absent from the guide). `preflight_check.py` language check is now locale-agnostic + informational. `new_task.py` alias-agnostic. Teammate setup prompt at ~/Desktop/OCTAHEDRON_TEAMMATE_SETUP_PROMPT.md.
- 2026-10-13 · task 3 · Universe date is PER TASK (modal) — removed every hard-coded date; `preflight_check.py --today`. REWORK-slot protocol added (Hub "Stage: Review N": treat as new, overwrite all fields, reserve previous fellow's prompt, counts as category done; SYSTEM_PROMPT rule 14, WORKFLOW A0). Parser now refuses a transcript whose session name ≠ task folder. Category policy: 13 (guide) / 14 (Hub); deterministic NEXT PICK; round-2 = least-recently-done THIN first; prompts never repeat. Directives tagged [generic]/[persona]; `reference/<owner>/` archives are inherited ([generic] only). Tools are pure Python (`new_task.py`) for Windows/mac/linux.
- 2026-10-13 · task 3 · Universe "today" is per task, not fixed (task 3 modal: Sat 3 Oct 2026; operator: "time may change every task"). Shopping done; Google Workspace reads (Gmail/Drive/Docs/Sheets via hatch_gws_cli) worked in both arms. Rework Hub slots are treated as fresh tasks with every field overwritten.
- 2026-10-12 · task 2 · Rationale voice fixed everywhere: **TESTER's first person** ("I picked B", "when I checked his Hue setup"); persona always third person. Task-1 example in RATIONALE_TEMPLATE converted; task-2 rationale added as the zero-QC-iteration example. `parse_transcript.py` now detects `exec <app-cli>` as an app invocation. Home Automation done; Philips Hue connector returned 404 "endpoint not mocked" in Arjun's universe (CONFLICTS #14).
- 2026-10-12 · task 1 · Operator decision: the AGENT writes the complete, self-reviewed rationale (first-person judge voice, AR-08-proof); operator only checks. Added generated `memory/NEXT_TASK_DIRECTIVES.md` (reading order #2) so every accepted task's lessons are standing instructions for the next session automatically.
- 2026-10-12 · task 1 · Workflow fixed to the HYBRID handoff: Hub prompt-QC first → Hatch → edit Apps utilized to trace truth. Task 1's Apps utilized should have been **none** (both arms used only internal memory); Hub accepted the pre-run guess — logged as Hub QC gap (#10/#11). Added POST_SUBMISSION_QUALITY playbook (reviewer SQS + veto rules).
- 2026-10-12 · task 1 · System created. Universe date confirmed **2 Oct 2026** (brief had said 3 Oct). Protocol confirmed **Multilingual v1**. Hub lists 14 categories. Overall Tie not allowed. Rationale must be English + firsthand.

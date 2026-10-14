# octahedron-apoorv — Hub ⇄ Hatch task system (Arjun Mehra · hi_sg)

A self-strengthening workspace for running Project Octahedron comparison tasks: write the prompt and judge in **Hub** (the platform under test), run the comparison in **Hatch**, pass Hub QC, archive what worked, and make the next task faster. Built from task 1 (accepted 2026-10-12). Everything in `playbooks/` and `memory/` is derived from what actually passed.

## 60-second start for a new task (the hybrid flow)
1. Claim the task on Hub (note **N**). Do the setup screens yourself: acks → Hatch setup → create the Hatch session `35e4f574ad46_task_N` → Session name/ID → persona. Read the Hatch guidelines modal.
2. Open a fresh assistant session and paste **`00_KICKOFF_PROMPT.md`** (replace N; fill the modal's date/internet/apps).
3. Agent gives category + prompt + predicted apps + "how it relates" → you paste into Hub → prompt QC green → run the identical prompt in Hatch → hand the agent both arms + both traces → agent tells you the true Apps utilized (edit the field) → you paste responses/traces/screenshot.
4. Agent gives preference, Absolute quality, 8 scores and the **finished, self-reviewed rationale** → you check it → paste → Hub Consistency check → QC → mirror into Hatch → Submit preference → End comparison → screenshots → Hub close-out → Submit.
5. When Hub **accepts**, tell the agent: transcript + 2 screenshots → archived, parsed, RETROSPECTIVE written, `build_memory.sh` run → `memory/NEXT_TASK_DIRECTIVES.md` regenerated. The next session reads it first and is automatically smarter.

One-time setup (VPN, Hatch account, 2FA, alias) is in the guide's "VPN setup" / "Hatch setup" sections; it never repeats per task.

## Map
```
00_KICKOFF_PROMPT.md   paste-and-go starter (self-sufficient)
SYSTEM_PROMPT.md       the agent's binding operating contract (reading order, folder protocol, rules, post-acceptance)
README.md              this file

playbooks/             HOW (all learned in task 1)
  WORKFLOW_HUB_HATCH.md      40 screens/actions in order, with gates
  QC_GATES_PLAYBOOK.md       every Hub gate seen: trigger → cause → fix → example
  RATIONALE_TEMPLATE.md      the accepted format + verbatim accepted rationale + self-check
  SCORING_CALIBRATION.md     ties, directions, Absolute Quality, where observations land
  PROMPT_DESIGN.md           8 checks, Arjun's voice bank, candidate ideas per open category
  TRACE_READING_GUIDE.md     how to tell what an arm actually did (decides Apps Utilized + Correctness)
  RECOVERY_PLAYBOOK.md       abandon & replace, exactly as executed; what you can still correct
  POST_SUBMISSION_QUALITY.md the human reviewer's SQS rubric, the 8 veto rules, the reviewer's-eye checklist
  PLATFORM_CONFLICTS_LOG.md  Hub vs guide vs Hatch contradictions = product feedback for launch

guide/                 READ-ONLY authority
  octahedron-guide.md                          the official guide (only one)
  MULTILINGUAL_RULES.md                        Hub's language-task block verbatim: locale codes + script rule per language (NOT in the guide)
  project-octahedron-onboarding-zoom-transcript.txt
  images/

persona/arjun-mehra_omni-hi-sg-01/
  PERSONA_PROFILE.md         identity, voice, people, data landscape, app constraints, verified finance facts
  ANNOTATION_GUIDELINES.md   the Hatch modal text + dimension definitions
  DATA_INDEX.md              GENERATED grep-ready index of all 15 apps (titles, dates, names, cells)
  app-export_2026-10-12.zip  canonical archive
  app-data/                  extracted: CATALOG.md, app-inventory.json, apps/01-gmail … 15-healthex (raw-state.json, csv, xlsx, media)

memory/
  GLOBAL_MEMORY.md           stable facts; edit only via dated Changelog line
  NEXT_TASK_DIRECTIVES.md    GENERATED: standing instructions from every accepted task (§6 rules + §8 do-differently), newest first — read FIRST
  GLOBAL_RETROSPECTIVE.md    GENERATED: index + every task's key points, newest first
  CATEGORY_TRACKER.md        GENERATED: 14 categories, done/open, thin ones flagged

tasks/35e4f574ad46_task_N/  ONE folder per task — the only place a session writes
  TASK_MEMORY.md             live working memory → cleaned at acceptance
  RETROSPECTIVE.md           key points + frontmatter (feeds the generated memory)
  FINAL_SUBMISSION.md        accepted Hub field values (drafted by parser, verified by eye)
  transcript/hub_task_transcript.txt
  screenshots/

templates/             TASK_MEMORY / RETROSPECTIVE / FINAL_SUBMISSION templates
reference/<owner>/     OPTIONAL: another fellow's archive (tasks + memory), read-only; build_memory.py inherits its [generic] directives
tools/
  new_task.py N              scaffold a task folder (never overwrites; alias read from GLOBAL_MEMORY) — .sh wrapper for mac/linux
  preflight_check.py         prompt: dashes/voice/actions · rationale: coverage, counts, exclusive claims, tie clauses, consistency, Abs.Q
  parse_transcript.py        Hub transcript → FINAL_SUBMISSION.md draft (validated on task 1: all fields)
  build_memory.py (.sh)      regenerate NEXT_TASK_DIRECTIVES (+ inherited [generic] lines from reference/) + GLOBAL_RETROSPECTIVE + CATEGORY_TRACKER (with NEXT PICK)
  build_data_index.py        regenerate DATA_INDEX.md after a new app export
```

## Design: loosely coupled, collision-proof, compounding
- **Write-local, read-global.** A session writes only in its own `tasks/<id>/`. Shared knowledge (`GLOBAL_RETROSPECTIVE.md`, `CATEGORY_TRACKER.md`) is *generated* from those folders, so parallel sessions never edit the same file. `GLOBAL_MEMORY.md` is append-only via Changelog.
- **Key points up, detail down.** Each task's `RETROSPECTIVE.md` is deliberately short (what worked, what failed, exact wording). The full story stays in `TASK_MEMORY.md`, `FINAL_SUBMISSION.md`, and the transcript. New sessions read the aggregate first, drill down only if needed.
- **Every acceptance strengthens the system automatically.** `build_memory.sh` promotes each accepted task's §6/§8 into `NEXT_TASK_DIRECTIVES.md`, which every new session reads before acting — no hand-edit needed. Consolidation into playbooks is optional polish. New gate → add to `QC_GATES_PLAYBOOK.md`. New wording that passed → `RATIONALE_TEMPLATE.md`. New conflict → `PLATFORM_CONFLICTS_LOG.md`. Category done → tracker updates itself.
- **Mechanical checks before human review.** `preflight_check.py` catches the exact classes of error Hub caught in task 1 (dashes, counts, exclusive claims, missing tie clauses, unjustified Bad, inconsistent preference). `POST_SUBMISSION_QUALITY.md` then covers what only a human reviewer grades.
- **Hybrid order, by design.** Hub prompt-QC first (the prompt is locked once the run starts), Hatch second, Apps utilized corrected from the trace third (the field is editable until Submit). This follows the guide's safety gate and fixes the form's pre-run Apps-utilized placement.

## Maintenance loop (per task)
`new_task.sh` → work → accepted → transcript + screenshots into `tasks/<id>/` → `parse_transcript.py` → verify → write `RETROSPECTIVE.md` → `build_memory.sh` → (if new gate/wording/conflict) update the relevant playbook.

## Precedence when sources disagree
**Live Hub form > `guide/octahedron-guide.md` > memory/playbooks.** Log every disagreement in `PLATFORM_CONFLICTS_LOG.md`.

## Not in this folder
Originals remain in `~/Downloads` and `~/Desktop` (copied, not moved). `~/hub_hatch_session_memory.md` is the pre-refinement memory; its refined form is `tasks/35e4f574ad46_task_1/TASK_MEMORY.md`.

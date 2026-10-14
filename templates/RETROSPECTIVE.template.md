---
task_id: 35e4f574ad46_task_N
task_number: N
status: in-progress            # in-progress | accepted | returned | abandoned
task_type: new                 # new (Hub "Stage: Attempt") | rework (Hub "Stage: Review N", another fellow's values pre-filled)
universe_date:                 # this task's universe "today" from the Hatch modal, e.g. 2026-10-03 (changes per task)
reserved_prompt_from_previous_fellow: ""   # rework only: their prompt, verbatim, so no one reuses it
accepted_date:                 # YYYY-MM-DD when Hub accepted
persona: Arjun Mehra (omni-hi-sg-01)
locale: hi_sg
category:                      # one of the 14 Hub categories, exactly as written on Hub
hatch_session_uuid:            # comparison UUID that was submitted
abandoned_session_uuids: []    # list any dead sessions
preference:                    # A slightly better | A significantly better | B slightly better | B significantly better
absolute_quality:              # Perfect | Good | Bad
scores:                        # 1..5 each
  style_behavior_high:
  correctness_high:
  style:
  coherence:
  helpfulness:
  completeness:
  tone:
  warmth:
apps_utilized: []              # union from trace; [] if none
qc_gates_hit: []               # e.g. [AR-05, AR-09, LIVE-E1]
qc_iterations: 0               # how many times evaluation QC was re-run
hub_task_quality_rating:       # the 1-5 you gave the task seed
time_minutes:                  # rough total
---

# RETROSPECTIVE — 35e4f574ad46_task_N

> KEY POINTS ONLY. This file is concatenated into `memory/GLOBAL_RETROSPECTIVE.md` for every future session to read first. Full detail lives in `TASK_MEMORY.md`, `FINAL_SUBMISSION.md`, and `transcript/`. Write it once, after acceptance.

## 1. The prompt and why it worked
- Prompt (verbatim):
- Records it rested on (titles):
- Category and why it fits the goal:
- Hub "how it relates" text (verbatim):

## 2. What the arms did
- A in one line:
- B in one line:
- Trace: apps actually invoked per arm:
- Facts verified / contradicted in Apps:

## 3. Final judgment that was accepted
- Preference + Absolute Quality:
- Scores (8):
- The concrete separators that decided it (quotes):
- Ties and the one-clause reason for each:

## 4. What failed on the way, verified cause, and the fix that passed
| Attempt | What I submitted | Gate(s) fired | Verified cause | Fix |
|---|---|---|---|---|
| 1 | | | | |

## 5. Reusable wording / templates (exact)
- Rationale structure that passed:
- Absolute-quality sentence that passed:
- Tie clause pattern that passed:

## 6. New rules learned (auto-promoted to memory/NEXT_TASK_DIRECTIVES.md)
> Start EVERY bullet with a tag: **[generic]** = true for any persona/locale/teammate (process, Hub/Hatch behaviour, scoring, QC) · **[persona]** = specific to this persona's data/apps/locale. Teammates inherit only [generic] lines.
- [generic] 

## 7. Platform conflicts observed (copy to PLATFORM_CONFLICTS_LOG)
-

## 8. What the next task should do differently (auto-promoted; tag each bullet [generic] / [persona])
- [generic] 

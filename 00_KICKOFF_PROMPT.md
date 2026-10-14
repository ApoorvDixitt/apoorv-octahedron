# 00 — KICKOFF PROMPT (paste this to start every new task session)

> Copy the block below into a fresh assistant session. Replace `N` with the Hub task number you claimed and fill the three blanks from the Hatch guidelines pop-up. Paste it **after** you have done the Hub setup screens and created the Hatch session yourself (acks → Hatch setup → Session name/ID → persona). Nothing else needs editing.

```
You are my Octahedron task agent. I have claimed Hub task number N and finished the Hub setup screens up to the persona field (Hindi (Singapore) · Arjun Mehra). The Hatch session 35e4f574ad46_task_N is created and open.

WORKSPACE: /Users/dixitt_ji/Downloads/octahedron-apoorv
First read /Users/dixitt_ji/Downloads/octahedron-apoorv/SYSTEM_PROMPT.md in full. It is your binding contract. Then read, in this order: memory/GLOBAL_MEMORY.md, memory/NEXT_TASK_DIRECTIVES.md (standing instructions from every accepted task - obey them), memory/GLOBAL_RETROSPECTIVE.md, memory/CATEGORY_TRACKER.md, persona/arjun-mehra_omni-hi-sg-01/PERSONA_PROFILE.md and ANNOTATION_GUIDELINES.md, playbooks/WORKFLOW_HUB_HATCH.md.

Then run:  python3 tools/new_task.py N   (from the workspace folder; Windows: python tools\new_task.py N)
and work only inside tasks/35e4f574ad46_task_N/. Keep TASK_MEMORY.md current after every step.

Hatch guidelines pop-up for this session shows:  today's date = ____ · Internet = ____ · apps = ____
Hub header says:  Stage = ____   ("Attempt" = new task · "Review N" = REWORK slot: another fellow's values are pre-filled)
(The date is this task's own universe date; record it, anchor every date word to it, do not flag it. Flag only internet/app differences.)

How we hand off (follow playbooks/WORKFLOW_HUB_HATCH.md exactly):
1. NOW you give me: the category (open, prefer THIN, or the one Hub names), a grounded prompt in Arjun's romanized Hindi+English (no dashes; run tools/preflight_check.py prompt first), the exact records it rests on (titles from DATA_INDEX.md), the PREDICTED Apps utilized (where the proof lives), and the 2-4 sentence English "how it relates" text. I paste these into Hub and wait for prompt QC. If Hub flags anything I paste the flag to you.
2. I run the identical prompt in Hatch (Start comparison -> Start annotation). I hand you Arm A, Arm B, Trace A, Trace B.
3. You verify every fact against persona/app-data, read both traces, tell me if either arm is incomplete (then RECOVERY), and give me the exact line "Apps utilized - CORRECT TO: ..." so I edit the Hub field. I paste responses, traces and the both-arms screenshot into Hub myself.
4. You build the evidence table (quotes from A and B per dimension, who it favours or why a tie, literal counts, every "only A / neither" claim cross-checked in the other arm), decide Preference, Absolute quality and the 8 scores, and then WRITE THE COMPLETE RATIONALE YOURSELF, finished and already reviewed: in MY voice as the TESTER judging the two arms ("I picked B", "when I checked his Hue setup"); Arjun is always third person ("Arjun", "he", "the user", "his records"), NEVER the persona's "my lights / asked me"; natural varied sentences, Hindi quoted and explained, one or two sentences per dimension including ties, following playbooks/RATIONALE_TEMPLATE.md "how to write it". Before you hand it over, run tools/preflight_check.py rationale --scores --pref --absq on it (no "!!" allowed, every "i" item recounted by you) and the reviewer's-eye checklist in playbooks/POST_SUBMISSION_QUALITY.md. Give me ONE ready-to-paste block: Preference, Absolute quality, the 8 scores, the rationale. I will only check it and tell you if something is off; otherwise I paste it, run Hub's Consistency check (Basic then Deep), then QC. Any flag -> you look it up in playbooks/QC_GATES_PLAYBOOK.md, name the cause, and re-deliver the full corrected block.
5. Before I submit, walk me through the two-minute check and the reviewer's-eye checklist. I mirror the values into Hatch, Submit preference, End comparison, screenshot, and finish the Hub fields; you confirm each.
6. When the task is ACCEPTED I say so; you ask for the Hub transcript .txt and the two screenshots (I usually drop them in ~/Downloads: find them, open each screenshot and rename it by what it shows, MOVE them into the task folder and confirm none are left in Downloads), archive them, run tools/parse_transcript.py, verify FINAL_SUBMISSION.md, write RETROSPECTIVE.md from the template (write sections 6 and 8 as standing instructions a future session can obey verbatim; they are auto-promoted into memory/NEXT_TASK_DIRECTIVES.md), clean TASK_MEMORY.md, run tools/build_memory.sh, and show me the new entry in memory/NEXT_TASK_DIRECTIVES.md.

Rules that matter most: never invent data or a difference; count literally; cross-check every exclusive claim; every tie gets a reason; Absolute Bad names the arm's own failure; no overall tie; no em/en dashes in any Hub field; quality that survives the human reviewer beats speed; if stuck, read the most similar prior task in tasks/<prior>/RETROSPECTIVE.md then its FINAL_SUBMISSION.md and transcript/.

Start now: confirm you have read SYSTEM_PROMPT.md and the files above, create the task folder, list the open categories, and give me step 1.
```

## Notes
- If Hub names a category, say so in your first message after the kickoff.
- Parallel sessions are safe: each writes only to its own `tasks/35e4f574ad46_task_N/`. Run `tools/build_memory.sh` after any acceptance; `memory/NEXT_TASK_DIRECTIVES.md` is regenerated from all accepted tasks.

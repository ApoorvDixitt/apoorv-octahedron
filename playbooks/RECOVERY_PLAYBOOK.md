# RECOVERY — when Hatch breaks (as executed in task 1)

> One rule: **never submit an incomplete comparison.** Notes cannot rescue a missing arm. Retry → then abandon & replace.

## What happened in task 1
Session `35e4f574ad46_task_1` (UUID `f3389d8e-…`): Arm A answered; **Arm B showed only "Can't reach Hatch at the moment. Try again soon."** — twice, no response, even after re-sending. Decision: abandon & replace. Replacement session (same name, new UUID `ceb7dcc3-…`) ran clean; both arms answered. Hub Session ID was updated to the new UUID. Task accepted.

## Triage
| Symptom | Do |
|---|---|
| One arm: *"Can't reach Hatch"* / *"Something went wrong"* / blank, **then** a full answer appears | **Recovered.** Valid. Continue. |
| One arm error-only, no full answer after one retry of the same prompt in that arm | **Abandon & replace** (below). |
| Both arms stuck on *Booting the agent…* / red `Error 400 failed to checkpoint arm` | Reload once → still stuck → abandon & replace. |
| Sessions list shows **Ended mid-annotation** for your row | Cannot be reopened or submitted. Abandon & replace. Never tick the attestation. |
| Only one arm got a follow-up turn / prompt duplicated / context missing | Unfair pair → do not score. Abandon & replace. |
| One arm returns the data, the other says it can't reach it | **Not** a broken pair. Score it; judge the communication; the "can't reach" is Correctness if the data exists. |
| Slow tool, UI glitch, label hidden, but both arms complete | Finish normally; mention in Notes. |

## Abandon & replace — exact steps
1. Hatch sessions list → three-dot menu on the broken session → **Rename** → `35e4f574ad46_abandonedtask_N` (same N; never submit it; do not use "Discard annotation" as a shortcut).
2. **Create session**: GAIA PREFERENCE · Name `35e4f574ad46_task_N` · Universe `hi_sg` → Arjun Mehra · Protocol Hatch RM Style Task — Multilingual v1 → wait RUNNING → Open → read/close guidelines modal.
3. **Start comparison** → paste the **same approved prompt** (the dead session never produced a scoreable result, so reuse is fine) → **Start annotation**.
4. Confirm **both** arms complete.
5. **Hub:** update **Session ID** to the new comparison UUID (and Session name if it changed). Take the completion screenshot from the replacement.
6. Log both UUIDs and the reason in `TASK_MEMORY.md`; mention briefly in Hub Notes only if it affected the entry (task 1 used `N/A` because the replacement ran clean).

## Two different "returned" situations — don't confuse them
| Situation | How you know | What to do |
|---|---|---|
| **Your own task came back** from review | Same session name/UUID; reviewer feedback on your fields | Fix-in-place fields below; if the judgment itself is wrong, recreate the session |
| **Rework slot** — someone else's returned task landed on you | Hub header **"Stage: Review N"**; fields pre-filled with another fellow's prompt/scores/rationale/persona | Treat as a brand-new task: new Hatch session, your category/prompt, **overwrite every field**; reserve their prompt (never reuse); count the category as done (WORKFLOW A0; SYSTEM_PROMPT rule 14) |

## What you can still correct (guide table) — when YOUR task is returned or you spot an error
| Field | Lives in | Correctable? |
|---|---|---|
| Apps utilized · Use-case category · Notes | Hub | **Yes** — fix in place, resubmit |
| Session name / Session UUID | Hatch + Hub | **Yes** — rename in Hatch, update Hub (also after any replacement) |
| Prompt and user turns · Response A / B | Hatch run | **No** — part of the run → recreate |
| Submitted preference, 8 scores, Required rationale | Hatch | **No** — if the judgment itself is wrong → recreate the session |
Rule: never enter different values on Hub to "compensate" for a locked Hatch evaluation; recreate instead.

## If B keeps failing across 2+ fresh sessions
That's a platform-side outage. Stop burning attempts; record it in `playbooks/PLATFORM_CONFLICTS_LOG.md` and flag to the team.

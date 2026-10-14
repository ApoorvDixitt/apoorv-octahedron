# TRACE READING — how to tell what an arm actually did

> In task 1 the trace decided two fields: **Apps Utilized** (none) and **Correctness** (both arms claimed data was unavailable while never opening the apps). Read the trace for every arm, every task.

## Where
Hatch → **Trace** tab (top right) → each arm has its own column → **Copy trace** (per arm; never "Copy both" when pasting into Hub's Trace A / Trace B boxes).

## Anatomy of a trace
```
[User · +0s]           the prompt
[Tool Call · <tool> ]  what the agent invoked, with arguments (JSON)
[Tool Output · <tool>] what came back
[Assistant · +Ns]      a message shown to the user
```

## Classify each Tool Call
| Tool call seen | Means | Counts as "app utilized"? |
|---|---|---|
| `memory_search`, `read ~/MEMORY.md`, `read ~/workspace…`, `exec find/ls` | The agent searched its **own internal memory/filesystem**, not the persona's apps | **No** |
| A Google Sheets / Docs / Drive / Gmail / Calendar / Contacts / WhatsApp / Outlook / Notion / Photos / Oura / Hue / Nutrition / Health tool call (name will reference the app or its API) | The agent opened the persona's app | **Yes** — add that app to Apps Utilized |
| `hatch_gws_cli gmail|drive|docs|sheets …` (task 3) or `exec <app-cli>` (task 2) | Google Workspace / app connector call — **counts even if it errored** | **Yes** |
| `skill_search` (any query), `tool_search.load_tool_namespace`, `device.list`, `device.describe`, `channel.status <whatsapp\|telegram\|messenger>` (task 4) | The agent looked for a tool / checked Hatch's own device pairing or messaging-channel link. `channel.status whatsapp → unlinked` is about Hatch's WhatsApp *channel*, not the persona's WhatsApp data | **No** |
| `read ~/MEMORY.md`, `edit ~/MEMORY.md` (task 4, turn 2) | The agent read/wrote its own long-term memory file | **No** |
| `artifact.create_file` / `write` of a user-facing file | The arm produced an artifact (part of its answer) — ask the operator to download it; archive in `transcript/` | Not an app; judge its content |
| Web search / browse | Internet use (allowed here) | Not a listed app; note it in rationale if it affected the answer |
| `exec <app-cli> …` e.g. `exec philips-hue status`, even if it errors (task 2: HTTP 404 "endpoint not mocked") | The agent invoked that app's connector | **Yes**: add the app. `parse_transcript.py` misses these; fix FINAL_SUBMISSION by hand |
| Nothing but assistant messages | Pure conversation | No apps utilized |

Task 1 reality: both arms ran only `memory_search` → `read ~/MEMORY.md` → `read ~/workspace` → `exec find …` → "No matched memories" → then told the user the tracker was unavailable. **Zero** persona-app calls. Therefore Apps Utilized = none, and the "nahi hai" claim was a Correctness miss for both (the sheets existed).

## Required output after reading both traces (paste-ready for the operator)
```
Arm A — complete: yes/no · tool calls: … · persona apps invoked: …
Arm B — complete: yes/no · tool calls: … · persona apps invoked: …
Apps utilized — PREDICTED (in Hub now): …
Apps utilized — CORRECT TO: <union of persona apps either arm invoked, or "none">   ← edit the Hub field now
Facts/claims checked in app-data: <claim → where → true/false>
Correctness impact: <e.g., both said tracker unavailable; it exists → identical miss → Tie>
```

## Multi-turn traces (task 4)
Each `[User · +Nm Ns]` block after the first is a follow-up turn. Check: same text in both arms, sent within seconds of each other (A +11m50s / B +11m55s), both arms answered after it. Every user turn must be pasted into Hub's **Task prompt** field under the first one — the Response A/B pastes alone do not satisfy "include every turn" (task 4 missed this).

## System-clock warning (guide: "System-clock behavior in Hatch")
Hatch stamps **newly created or modified records** (drafts, events, Notion pages, sheet rows, chat messages) with the real-world environment clock, not this session's universe date. A new WhatsApp/Chat message can therefore appear *mid-history*, and a new calendar event may carry a 2026-10-12-style timestamp. The write still succeeded. When verifying a claimed action, open the actual record in Apps and check its content/recipient/date fields; don't judge by where it sits in the list, and don't mark a correct write wrong because of its clock stamp.

## Checklist after reading both traces
- [ ] List the app tool calls per arm → union = **Apps Utilized** (correct the pre-run selection in Hub).
- [ ] For every fact an arm stated: was there a tool call that could have produced it? If not, it's unverified → check Apps; if it's wrong, Correctness.
- [ ] For every "I couldn't find / don't have X": does X exist in Apps? (grep DATA_INDEX first.) If yes → Correctness miss.
- [ ] For every "I created / sent / updated": is the artifact in Apps with the right content/recipient/date? If not → Correctness, decisively.
- [ ] Did an arm do something unrequested (send instead of draft, add attendees)? → Correctness.
- [ ] Error toasts in trace that were followed by a complete answer = recovered (valid). Error with no complete answer = incomplete arm → RECOVERY_PLAYBOOK.

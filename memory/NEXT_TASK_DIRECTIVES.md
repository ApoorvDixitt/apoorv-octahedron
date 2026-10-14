# NEXT-TASK DIRECTIVES — read this FIRST in every new session (GENERATED)

> GENERATED 2026-10-13 15:04 by tools/build_memory.py. Auto-promoted from each ACCEPTED task's RETROSPECTIVE §6 (new rules learned) and §8 (what the next task should do differently). Newest first, cumulative. **Do not edit here** — write in your task's RETROSPECTIVE and re-run `tools/build_memory.sh`. Every item below is a standing instruction until a later task supersedes it.


## From task 5 — Entertainment · accepted 2026-10-13 · preference A slightly better · Abs.Q Good · gates —

**Do differently next time:**
- [generic] At kickoff, ask the operator for the Hatch header "Now" time along with the modal date, and anchor "aaj/abhi/raat" to it.
- [generic] Don't ask for a separate comparison UUID; the Session ID from the Hatch header is the one Hub wants.
- [generic] After submit, apply the Downloads intake rule (§6.1) without being asked: find, open, rename by content, move, confirm Downloads is clean.
- [persona] Next open THIN categories: Travel, Legal / Civic. Legal / Civic is ready (Drive "HDB October BTO Teaser List.pdf", Docs "Oct BTO list aaya", Notion "Kagaz checklist", Calendar 8 Oct "8 Oct BTO application opens" 09:00 and "ICA appointment - birth cert wala kagaz" 11:00 at ICA Lavender). Travel candidates in Gmail: AirAsia "KL return $78", Agoda "JB day trip hotel $35", Trip.com "Batam 2D1N $89, passport 6 mahine valid", Changi "StarMart bus ticket $2 off". Name each source in the prompt.
- [generic] Keep delivering the rationale in one block with the SUBMIT GATE; task 5 cleared QC with zero iterations this way.

**Rules learned (now standing):**
1. [generic] **File intake after submit (operator rule, every session):** when the operator says the transcript/screenshots are in `~/Downloads`, find them yourself by newest mtime, open each screenshot and name it by what it shows (`hatch_both_arms_responses.png`, `hatch_scoring_panel_completed.png`, `hatch_annotation_row_submitted.png`; transcript → `transcript/hub_task_transcript.txt`), **move them with `mv`, never copy**, then list Downloads again and confirm none are left. macOS screenshot names contain a narrow no-break space before AM/PM: move them with a glob (`Screenshot\ <date>\ at\ *.png`), not a typed path.
2. [generic] **The Session ID Hub wants is the ID in the Hatch comparison header** (the operator's "Session ID"; the same ID appears in the Annotations row). Do not tell the operator to wait for a second "comparison UUID".
3. [generic] **Check the Hatch header clock ("Now <day>, <date>, <HH:MM>") as well as the modal date, and write time-of-day words to match it.** Task 5's header read 23:24 while the prompt said the shift "khatam hogi" at 8 pm; neither arm noticed, so it cost nothing, but a sharper arm could have challenged the premise.
4. [persona] **Gmail and Google Calendar reads work in Arjun's universe** (task 5: both arms used `hatch_gws_cli gmail +triage/+read` and `calendar +agenda --today` without errors). Promo/newsletter mails (Hotstar, meWatch, KKR, YouTube, SAFRA, onePA, Klook) are rich, checkable grounding for Entertainment/Travel-style prompts.
5. [generic] **Constraint traps written as user limits ("ghante bhar se zyada nahi", "Hindi me", "awaaz dheemi") give clean, quotable separators** even when both arms reach the same pick: judge who honoured each limit (45-50 min vs 1 hour, meWatch addressed vs silent, earphones vs nothing).
6. [generic] **PREDICTED Apps utilized can equal trace truth when the prompt names the app and the source** ("calendar me raat 9 baje wala…", "Gmail me Hotstar aur meWatch wale mails"); still confirm it against both traces before saying "no edit needed".

<sub>source: tasks/35e4f574ad46_task_5/RETROSPECTIVE.md</sub>

## From task 4 — Companionship / Chat · accepted 2026-10-13 · preference B slightly better · Abs.Q Bad · gates AR-09, AR-10, AR-07

**Do differently next time:**
- [generic] Put the SUBMIT GATE (Apps utilized, prompt turns, Notes, Session ID) at the bottom of the final rationale block itself; do not rely on a separate Phase E message.
- [generic] Build the evidence table from transcripts + app-data only; keep any web look-up in TASK_MEMORY as "for my understanding", never in the rationale.
- [generic] Write tie clauses as "Tie, because …, so neither …" and the trade-off as "X still wins despite that" from the first draft; target ≤1 QC iteration again.
- [persona] Next open THIN categories: Entertainment, Travel, Legal / Civic. Legal / Civic is ready (Drive "HDB October BTO Teaser List.pdf", Docs "Oct BTO list aaya", Notion "Kagaz checklist", Calendar 8 Oct BTO/ICA) and its proof lives in apps that the arms have read successfully (Drive/Docs/Notion/Calendar), unlike WhatsApp.
- [persona] Do not anchor a decisive fact in WhatsApp alone until a trace shows a WhatsApp read skill; if you must use WhatsApp, pre-write turn 2 with the quoted messages before the run.
- [generic] After the run, confirm in Hub (ask the operator to read the field aloud) that Apps utilized was changed and that every user turn is in the prompt field, before saying "ready to submit".

**Rules learned (now standing):**
1. [generic] **Attach a SUBMIT GATE to every final rationale block.** The last lines of the block must list, as values to check on screen before Submit: `Apps utilized = <trace truth>`, `Task prompt field = all N user turns`, `Notes = <text or N/A>`, `Session ID = <UUID>`. The operator may submit the moment QC clears, so the two-minute check has to travel with the block, not come after it. (Task 4: Apps utilized stayed WhatsApp and turn 2 never reached the prompt field.)
2. [generic] **Never put facts from outside the transcripts and the persona's app-data into the rationale.** Web-checking an arm's real-world claim is fine for your own understanding, but Hub AR-09 calls any such fact "fabricated/unverifiable from the transcripts", and it drags Correctness and Helpfulness with it. Judge real-world claims only as specific-vs-general or as unsupported in the transcript; say explicitly "I am not weighing whether it is true, since neither arm looked it up".
3. [generic] **AR-10 wants the literal construction "B still wins despite that" (or A) next to every dimension that leans the other way**, not just a weighting sentence in the preference paragraph. Put one sentence in the preference paragraph and one closing sentence inside the opposing dimension's paragraph.
4. [generic] **Frame every tie as "Tie, because …, so neither …".** AR-07 hesitated on "Tie. Both …" even though the clause was present; "because/so neither" removes the ambiguity for the gate and the human reviewer.
5. [generic] **If a Hub re-check quotes phrases that no longer exist in your delivered text, Hub is still reading the old field.** Grep the delivered file for the quoted phrases first; then have the operator select-all → delete → paste → click out of the field → re-run. Don't rewrite content that isn't there.
6. [generic] **Multi-turn is the right call when both arms stop at the same ask** (both said "WhatsApp dekh nahi sakta" and asked for the messages). Send one identical follow-up in the user's voice with the exact records quoted from app-data; log the send offsets (+11m50s / +11m55s) and paste turn 2 into the Hub prompt field under turn 1.
7. [generic] **Trace alone is enough for the agent's analysis** (it holds every user and assistant message verbatim); the Hub Response A/B fields still need the conversation-view copy with UI timestamps, and any artifact/card must be handed over separately.
8. [generic] **`device.list` and `channel.status <whatsapp|telegram|messenger>` are Hatch's own device/messaging-link checks, not persona-app reads.** They do not count toward Apps utilized. (`parse_transcript.py` classified them correctly as internal.)
9. [persona] **WhatsApp is not readable by the arms in Arjun's universe (as of 2026-10-13).** `skill_search "WhatsApp read messages"` returns no WhatsApp skill (Instagram/Outlook/Messenger come back instead); no WhatsApp skill has appeared in any trace across tasks 1–4. Prompts whose decisive fact lives only in WhatsApp will end in a shared "dekh nahi sakta" miss → Correctness tie; plan a turn 2 that supplies the content, or anchor the fact in Gmail/Docs/Sheets/Drive/Notion/Calendar as well.
10. [generic] **Keep `rationale.txt` byte-identical to the latest delivered block, every time** (operator instruction, task 4). Overwrite → diff → then deliver; after acceptance, diff it against the parsed transcript.
11. [generic] **Companionship pairs separate on register and process-narration, not on data.** Checkable items that worked: a crude word absent from the persona's own messages ("bakchodi"), messages that announce a check and then fail ("Ruk, … dekhne de" ×2), filler lines before the answer, one-message vs three-message turns. Count them literally.

<sub>source: tasks/35e4f574ad46_task_4/RETROSPECTIVE.md</sub>

## From task 3 — Shopping · accepted 2026-10-12 · preference A slightly better · Abs.Q Bad · gates —

**Do differently next time:**
- [generic] Record the Hatch modal date for that task in TASK_MEMORY first; write the prompt's date words from it.
- [persona] Next open THIN categories: Companionship / Chat, Entertainment, Travel, Legal / Civic. Legal / Civic is ready: Drive "HDB October BTO Teaser List.pdf", Docs "Oct BTO list aaya", Notion "Kagaz checklist", Calendar "8 Oct BTO application opens" and "ICA appointment - birth cert wala kagaz" (8 Oct). Name each source in the prompt.
- [generic] If a fact you want verified lives in WhatsApp or Notion, name that chat/page in the prompt.
- [generic] Build the verification key before writing the prompt (as in tasks 2–3); it made every Correctness claim checkable.
- [generic] On receiving the transcript, grep session name + UUID before running `parse_transcript.py`.
- [generic] Ask for the task-seed rating only if the transcript shows a rating field.

**Rules learned (now standing):**
1. [generic] **The universe "today" changes per task.** Take the date from the operator's Hatch modal, write it in TASK_MEMORY, anchor every date word in the prompt to it, and do not flag it as a discrepancy (operator correction, task 3: Sat 3 Oct 2026). (`preflight_check.py` used to hard-code 2 Oct; **fixed after task 3** — pass `--today "<modal date>"`.)
2. [generic] **Rework slots:** when the operator says the Hub task is a rework of someone else's entry, treat it as fresh: deliver all step-1 values and remind him to overwrite every Hub field, including Apps utilized.
3. [generic] **Before parsing any Hub transcript, grep it for the session name and the comparison UUID.** If either belongs to another task, stop, do not write FINAL_SUBMISSION, rename the file as a mismatch, and ask for the correct export.
4. [persona] **Google Workspace reads work in Arjun's universe:** both arms used `hatch_gws_cli gmail/drive/docs/sheets` successfully when the prompt named the doc/sheet titles ("Docs me jo Sheng Siong list", "ration diaper bachat sheet", "Shopee wale order mails"). Name the source title in the prompt to get the arms into the app.
5. [generic] **Arms do not open apps the prompt doesn't name.** Neither arm opened WhatsApp, where the decisive stock fact lived. Put the deciding fact in a named source unless you deliberately want a shared-miss trap, and if it is a trap, expect a Correctness tie on that point.
6. [generic] **An arm may answer with an artifact file** (`artifact.create_file`, e.g. markdown). Ask the operator to download it, judge it as part of the response, and archive it in `transcript/`.
7. [generic] **A Devanagari character inside a romanized reply is a script error** → Style fault; quote it and give the romanized form.
8. [generic] **A 3-3-2 directional split with a content-side preference passed without a QC flag** when the preference paragraph states the weighting explicitly in one sentence.

<sub>source: tasks/35e4f574ad46_task_3/RETROSPECTIVE.md</sub>

## From task 2 — Home Automation · accepted 2026-10-12 · preference B slightly better · Abs.Q Bad · gates —

**Do differently next time:**
- [persona] Write the rationale in the tester's voice from the first draft (rule 6.1); deliver the block once.
- [persona] Before choosing an app-action category, consider that Hue failed here: prefer a THIN category whose proof lives in apps that worked before (Gmail/Docs/Sheets/Drive/WhatsApp/Notion read paths), e.g. Shopping (Sheng Siong list + ration diaper bachat sheet) or Legal / Civic (HDB Oct BTO teaser PDF + Kagaz checklist). If you use Home Automation again, check Hatch Apps → Philips Hue first and expect the same 404.
- [generic] After the run, confirm the parser's `persona-app calls` line against the trace yourself (it now detects `exec <app-cli>`; task 2 found the gap).
- [generic] Before Hub close-out, confirm the Hatch annotation row after End comparison and take the completion screenshot after it changes from IN PROGRESS.
- [generic] Ask the operator for the task-seed rating if the transcript doesn't contain one.

**Rules learned (now standing):**
1. [persona] **Write the rationale in the TESTER's first-person voice, never the persona's.** "I" = the operator judging; the persona is "Arjun", "he", "the user". Never "my lights", "my records", "my kids' room". (Operator correction, task 2; supersedes the task-1 example in RATIONALE_TEMPLATE.)
2. [persona] **An `exec <app-cli> …` call (e.g. `exec philips-hue status`) counts as invoking that app** for Apps utilized, even if it errored. (`parse_transcript.py` originally missed these and printed "NONE"; **fixed 2026-10-12 after task 2** — it now reports `exec:<app>` and tells you to list the app. Still verify by eye.)
3. [generic] **When the app tool errors identically in both arms** (connector/"endpoint not mocked"), both arms are still complete if each gives a final answer: do not abandon/replace (a retry hits the same mock), do not add a turn; judge how each handled the failure and state the error verbatim in Hub Notes.
4. [generic] **Build a "verification key" of the app's start state before the run** (TASK_MEMORY): it is what turned B's "Nightlight" into a verifiable Correctness point instead of an opinion.
5. [generic] **Design prompts with checkable traps** (a scene that is too bright, a scene in the wrong room, a light left on) so differences come from the data, not invented separators.
6. [persona] **Philips Hue in hi_sg (Arjun) returned "endpoint not mocked" on 2026-10-12.** Until a later task shows Hue working, expect Home Automation prompts to end in a failure-handling comparison.

<sub>source: tasks/35e4f574ad46_task_2/RETROSPECTIVE.md</sub>

## From task 1 — Finance · accepted 2026-10-12 · preference A slightly better · Abs.Q Bad · gates ADVISORY-P2, LIVE-E1, AR-02, AR-05, AR-07, AR-08, AR-09, AR-11

**Do differently next time:**
- [generic] Pick a **thin, open category** (Home Automation / Legal-Civic / Shopping / Companionship) — see `memory/CATEGORY_TRACKER.md` and `playbooks/PROMPT_DESIGN.md` candidate bank.
- [persona] Run `tools/preflight_check.py prompt` before pasting; `tools/preflight_check.py rationale --scores … --pref … --absq …` before QC.
- [generic] After the run, **edit Apps utilized to the trace truth** before submitting. Task 1's correct value was **none** (guide: union of apps actually invoked, "may be little or nothing"); the pre-run guess "Google Docs, Google Sheets" stayed because the guide's Hub-first order put the field before the run. Hub accepted it without re-validating against the traces (PLATFORM_CONFLICTS #10/#11). Fixed for task 2+ by the hybrid handoff (PREDICTED → CORRECT TO).
- [generic] Expect the arms may again ignore persona apps; if so, Correctness tie + judge communication, and log it as model-behaviour signal.
- [persona] Agent delivers the finished, self-reviewed rationale (evidence table → first-person draft → `preflight_check.py rationale` → reviewer's-eye) in one block with the scores; operator checks and pastes → aim for ≤1 QC iteration.

**Rules learned (now standing):**
1. [generic] Read the **trace** before anything: zero persona-app calls ⇒ Apps utilized none ⇒ any "not available" claim is a Correctness miss.
2. [generic] **Count literally** every number you write (AR-05).
3. [generic] **Cross-check every "only A / B doesn't"** in the other arm (AR-09).
4. [generic] **Every Tie needs a clause** (AR-07). **Absolute Bad needs the preferred arm's own failure** (AR-11).
5. [generic] Hub **forbids overall Tie** ⇒ never go all-8-ties; keep ≥1 quotable directional dimension.
6. [generic] Using the persona's real name/surname is **register**, not fabrication — check Contacts/User before calling anything "invented".
7. [persona] **AR-08:** the rationale must read like a person talking, not a per-dimension scaffold. The agent writes the complete rationale in the operator's first-person judge voice (RATIONALE_TEMPLATE rules), self-checks it (preflight + reviewer's-eye), and hands over one final block; the operator only checks it.
8. [generic] LIVE-E1 can persist as **advisory** on near-identical pairs and still pass — don't fabricate separators to silence it.
9. [generic] **No em dashes** in the prompt (ADVISORY-P2).
10. [generic] If an arm shows "Can't reach Hatch" twice with no answer → abandon & replace immediately; update Hub Session ID to the new UUID.

<sub>source: tasks/35e4f574ad46_task_1/RETROSPECTIVE.md</sub>

# PROMPT DESIGN — Arjun Mehra (hi_sg)

> How to write a prompt that passes Hub prompt-QC and gives the two arms real decisions to make. Includes the accepted task-1 prompt and a bank of **candidate** ideas per unused category, each pinned to records that exist in `persona/arjun-mehra_omni-hi-sg-01/DATA_INDEX.md`. Candidates are starting points — verify the records in Hatch Apps before use, and never reuse/paraphrase a prompt from an accepted task.

## The 8 checks (all must be true)
1. First person, Arjun's voice: romanized Hindi + English, WhatsApp style, *tu/tum* register. (Script rule per locale: `guide/MULTILINGUAL_RULES.md` — hi_sg = Latin letters, English mixed in.)
2. Grounded in records that exist — ideally 2+ so the arms must connect things. Name them in the Hub "how it relates" field.
3. Requires app use (the arms must open something), unless the category is pure conversation — then still anchor to a real record.
4. Supported actions only (see PERSONA_PROFILE.md constraints). No WhatsApp to new contacts, no Outlook drafts, no writes to Contacts/Oura/Photos/Health Records.
5. Dates covered by records: **universe "today" comes from this session's Hatch modal and changes per task** (2 Oct, 3 Oct seen). Data is dense for Sept 2026 and the first days of Oct. Write date words from the modal date (task 3: modal Sat 3 Oct → "kal Sunday" = 4 Oct). Prefer "September wale", "pichle hafte", "27 Sep wale BBQ" over "next month".
6. A goal with real constraints, not a click-script. Two capable assistants should differ in defensible ways.
7. **No em/en dashes.** Use commas/full stops. Run `tools/preflight_check.py`.
8. Category = the goal, not the apps. Use Hub's named category if any; otherwise the **NEXT PICK** line in `memory/CATEGORY_TRACKER.md`. After all 13/14 are done once, categories repeat (least-recently-done, THIN first) but **prompts never repeat** — write a new goal from different records (e.g. second Finance task: 4-room target vs BTO downpayment, not the September bills again).

## Accepted prompt — task 1 (Finance) — do NOT reuse or paraphrase
```
Is mahine stall ki pay aane wali hai, par naye roster me mere ghante kam ho gaye aur pichle Saturday ka OT bhi zero chala gaya. Mere September wale ghar kharche aur saving tracker dekh ke bata. SP bill, phone aur town council nikalne ke baad, chaar-room flat ke liye jo har hafte paisa alag rakhta hu woh target maintain kar paunga ya nahi? Jo pakka hai aur jo abhi aana baaki hai, dono alag karke saaf-saaf batana.
```
Why it passed: real situation (roster cut + OT zero in sheet/doc), 2 sheets + 2 docs behind it, asks for interpretation not a lookup, forces a judgment (confirmed vs pending), natural voice, no dashes.
"How it relates" text that passed: named the four records by title and the roster-cut note.

## Voice bank (phrases Arjun actually uses in his data)
*kharcha, bachat, rashan, hafta/hafte, stall pay, OT, roster, shift, chaar-room / 4-room, BTO, HDB, Jurong side, Mummy-ji, judwa / dono bachche, Aarav, Vivaan, polyclinic, vaccine, feed log, diaper, milk powder, Sheng Siong, JEM, Koufu, Ah Hock, town council, SP bill, POSB, CDC voucher, Shopee, kopi, BBQ 27 wala, Rohit (Jurong West), Suresh (supervisor), Syed (Saturday swap), Imran (van kaam), Latha, Priya, neighbours group.*
Openers he'd use: *"Yaar…", "Ek kaam hai…", "Dekh…", "Is hafte…", "Kal…", "Mummy-ji keh rahi thi…"*. Closers: *"saaf-saaf bata", "short me bata", "jaldi dekh le", "list bana de"*.

## Candidate ideas per OPEN category (verify records first)
| Category | Anchor records (from DATA_INDEX) | Candidate goal (write in Arjun's voice; these are English sketches) |
|---|---|---|
| **Home Automation** (thin) | Philips Hue: 7 devices, rooms/scenes; Notion 23 Sep night note ("pankha slow… light band karke so raha"); twins' evening routine | Set up / adjust the lights for the twins' bedtime routine the way he actually does it at night; or a low-light scene for night feeds without waking Mummy-ji. |
| **Legal / Civic** (thin) | Drive: "HDB October BTO Teaser List.pdf"; Gmail from no-reply@hdb.gov.sg; Docs "Oct BTO list aaya"; Notion "Kagaz checklist" | Make sense of the Oct BTO teaser for a 3-room → 4-room move on the Jurong side: what does he actually need to have ready / what do the eligibility lines mean (general info). |
| **Shopping** (thin) | Sheets "ration diaper bachat", "Ghar kharcha"; Docs "Sheng Siong list"; WhatsApp Shopee SG / FairPrice; Gmail Shopee orders | Compare what he's been paying for Drypers / milk powder across Sheng Siong, Shopee 9.9, FairPrice and tell him the cheapest regular option within the CDC-voucher habit. |
| **Health & Fitness** | Health Records clinical note 15 Aug (leg/back pain from standing), labs 17 Aug; Oura 30 days; Nutrition 115 entries; Docs "Mummy-ji knee check" | Given his standing-all-day stall shift and the Aug note about leg/back pain, plus his sleep data, suggest what's realistic for him in the evenings with twins. |
| **Relationships** | WhatsApp Sunita Mehra (278 msgs), Rohit Mehra (138), Divya Rawat contact "Children's mother"; Docs "BBQ 27 wala"; Calendar 27 Sep BBQ | Help word a message to Rohit about the BBQ share / or to Mummy-ji about her knee review follow-up, in his tone, inside an existing chat (or as text to copy). |
| **Work Productivity / SMB** | Outlook: "October Roster - Saturday Overtime aur Duty Timing" (2 Oct), surprise audit, fire drill 9 Oct, staff meal coupon; WhatsApp Suresh Menon (129), Koufu Helpers group; Notion Syed swap note | Summarise what changed in the October roster vs September and what he needs to confirm with Suresh about Saturday OT / the Syed swap; produce a short message to send Suresh. |
| **Emotional Support** | Notion "23 Sep Budh – shift ke baad raat note"; Oura; Calendar dense shift days; 4-room pressure | A tired-after-shift check-in anchored to that night's note and this week's calendar. |
| **Companionship / Chat** (thin) | Notion night note (KKR highlights, low volume), WhatsApp neighbours group, Photos of twins | Casual chat about his evening, anchored to a real note/photo (not unanchored "how's my day"). |
| **Media Creation** | Instagram account + Photos (twins, stall); Calendar Teachers Day / 27 Sep BBQ | Write a caption in his voice for a twins photo / the BBQ, pulling details from the actual photo/event. |
| **Entertainment** (thin) | Notion: "paanch minute phone me KKR highlights dekha, awaaz ekdum low rakhi" | Something short to watch/listen on a low-energy evening, matching what he actually watches (Internet available). |
| **Travel** (thin) | Calendar: Sheng Siong runs, polyclinic trips (bus fare 12 in tracker), Rohit in Jurong West | Light: plan the polyclinic + Sheng Siong + Rohit's place loop by bus with the twins' stroller; weak fit — use only if other thin categories exhausted. |
| **Learning / Research** | HDB BTO PDF; CDC voucher rules; Health labs | "Explain how X works" grounded in his documents (e.g., the BTO teaser). |
| **Personal Productivity** | Calendar feed-log reminders, "Kal ke liye chhota list" in Notion | Listed on Hub's 14 but guide says removed — avoid unless Hub names it. |

## Hub "how does the prompt relate to the universe" (2–4 English sentences) — pattern
Name the exact records (titles), state the real situation they show, state what the prompt asks the assistant to do with them, and end with "grounded in records that already exist in his accounts."

## Pre-paste checklist
- [ ] Records cited exist (grep DATA_INDEX, confirm in Apps)
- [ ] **Every source you want the arms to open is NAMED in the prompt** ("Docs me jo Sheng Siong list", "Shopee wale order mails"). Task 3: arms opened only the apps the prompt named; neither opened WhatsApp where the decisive fact lived. Unnamed source = deliberate shared-miss trap only.
- [ ] Date words anchored to THIS session's modal date
- [ ] No em/en dash
- [ ] Not a reuse/paraphrase of an accepted prompt
- [ ] Category not already done (or named by Hub)
- [ ] Same exact text will be pasted into Hatch

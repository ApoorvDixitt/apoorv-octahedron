# PERSONA PROFILE — Arjun Mehra (omni-hi-sg-01)

> Stable facts about the persona. Verified against `app-data/` on 2026-10-12. If the universe is refreshed, re-verify and bump the date.
> For exact records, grep `DATA_INDEX.md`. For the rules you must judge against, read `ANNOTATION_GUIDELINES.md`.

## Identity
| Field | Value |
|---|---|
| Name | Arjun Mehra |
| Universe ID | `omni-hi-sg-01` |
| Locale | Hindi (Singapore) — Hatch search code **`hi_sg`** |
| Age / role | 30, man, single father of 4-month-old twin boys |
| Home | 3-room HDB, Jurong East St 21, Singapore — lives with Mummy-ji |
| Work | Helper, Ah Hock Chicken Rice stall, Koufu JEM Level 5 |
| Gmail | arjun.mehra@gmail.com |
| Timezone | Asia/Singapore (GMT+8) |
| **Universe "today"** | **Per task** — read the Hatch guidelines modal each session (seen: Fri 2 Oct 2026 in tasks 1–2, Sat 3 Oct 2026 in task 3). Records are dense for Sept 2026 + first days of Oct. Anchor every date word to the modal date. |
| Internet in Hatch | **Available** (web look-ups allowed; still ground prompts in his records) |

## His life in one paragraph (from USER.md)
Three things are tight: sleep, money, space. Big target: save for a **4-room flat** (Jurong side, so Mummy-ji's life stays easy). Works day shift at the stall, comes straight home, handles the twins in the evening. Help him in a way that advances the 4-room goal and doesn't break the evening baby routine.

## How Arjun writes (voice to mimic in prompts)
- Romanized Hindi + English code-mixing, WhatsApp style: *"Is mahine stall ki pay aane wali hai, par naye roster me mere ghante kam ho gaye…"*
- Informal, direct, practical. Uses *tu/tum* register with his assistant, not *aap*.
- Local vocabulary from his data: *kharcha, bachat, rashan, hafta, stall pay, OT, roster, 4-room / chaar-room, Mummy-ji, judwa/twins, polyclinic, CDC voucher, Sheng Siong, JEM, Koufu, town council, SP bill, POSB, BTO, HDB.*
- **Never** write the prompt in English or translate an English prompt literally. **Never use em/en dashes (— –)** in the prompt — Hub QC rejects them.
- Names in his life: Aarav & Vivaan (twins), Sunita Mehra (Mummy-ji / mother), Rohit Mehra (cousin brother, Jurong West), Priya Mehra, Suresh Menon (supervisor), Latha Sundaram, Imran Sheikh (van kaam), Geeta Bhandari, Rakesh Yadav, Divya Rawat (children's mother), Syed (Saturday swap colleague).

## Register note (learned in task 1)
An assistant addressing Arjun by **surname ("Mehra")** reads stiff/distant for a casual chat. This is a *Style/register* observation — it is **not** a fabrication (Mehra IS his real surname). Do not call it "invented."

## Data landscape (what exists — grep DATA_INDEX.md for specifics)
| App | Volume | What's there | Prompt-worthy |
|---|---|---|---|
| Gmail | 320 msgs | HDB/BTO mails, Shopee orders, polyclinic, Singtel, misc | Shopping, Legal/Civic (BTO), Finance |
| Outlook Mail | 354 msgs | **Work** mail: Koufu/JEM roster, duty timing, audits, staff notices | Work Productivity/SMB |
| Google Calendar | 61 events | Shifts, Sheng Siong runs, polyclinic/vaccine, feed-log reminders, BBQ 27 Sep | Health, Finance, Relationships |
| Google Contacts | 133 | Family w/ relationship labels, colleagues, services | Relationships (read-only app) |
| Google Drive | 34 items | HDB Oct BTO Teaser PDF, all sheets/docs | Legal/Civic, Finance |
| Google Sheets | 8 | **Ghar kharcha - September**, **4-room saving tracker**, ration diaper bachat, feed logs | **Finance** (done), Health |
| Google Docs | 7 | is mahine kharcha (bills), Oct BTO list aaya, Sheng Siong list, Mummy-ji knee check, BBQ 27 wala, Imran van kaam | Finance, Shopping, Health |
| Notion | 4 pages | 4-room saving tracker, Kagaz checklist (documents), Jugnu pehli note, 23 Sep shift note | Legal/Civic, Companionship |
| WhatsApp | 36 chats, 1009 msgs | Mummy-ji (278), Rohit (138), Suresh (129), Latha (162), Priya (98), groups: Jurong East St 21 Neighbours, Koufu Helpers JEM L5; services: SP, POSB, Shopee, Grab | Relationships, Companionship, Work — **but arms cannot read it (task 4)**; use for your verification key, pair with a readable source |
| Photos | 56 | Twins, home, stall | Media Creation, Companionship |
| Oura | 30 days | Sleep (wake-date rows) | Health & Fitness, Emotional Support |
| Instagram | 1 account | Posts/captions | Media Creation |
| Philips Hue | 7 devices | Rooms, lights, scenes | **Home Automation** (thin category!) |
| Nutrition | 115 entries | Food logs | Health & Fitness |
| Health Records | 14 obs | Aug 2026 labs (cholesterol, glucose), vitals, immunizations, clinical note re standing pain | Health & Fitness |

## App capability constraints (what prompts may ask for)
- **Writable:** Gmail (real drafts + send), Google Calendar, Drive, Docs, Sheets, Notion, Philips Hue (state of existing devices only), Nutrition (add/delete log entries).
- **Send-only within existing chats:** WhatsApp (never a new contact/group). **Send but no drafts:** Outlook.
- **Read-only:** Google Contacts, Oura, Photos, Health Records, Instagram.
- Never ask: WhatsApp to a new number, merge contacts, Outlook draft, SMS/text.
- **Observed tool gaps (verify in each new trace):** Philips Hue connector → 404 "endpoint not mocked" (task 2); **WhatsApp has no read skill exposed to the arms** — `skill_search "WhatsApp read messages"` returns Instagram/Outlook/Messenger, `channel.status whatsapp` = unlinked (task 4; no WhatsApp call in any trace, tasks 1–4). Google Workspace reads (Gmail/Drive/Docs/Sheets via `hatch_gws_cli`) work (task 3). A prompt whose decisive fact lives only in WhatsApp will end in a shared "dekh nahi sakta" miss.

## Finance facts already verified (task 1) — reuse without re-deriving
- Take-home pay SGD **1650** (1 Sep, "JEM stall salary"). Saturday OT: 45 (13 Sep) → 30 (20 Sep) → **0 (26 Sep, "OT cut zero")**.
- Bills doc "is mahine kharcha": SP **92.15**, phone **20**, town council **68**, **320** set aside to POSB for 4-room, CDC voucher for rashan+diaper.
- "4-room saving tracker": opening 2450 → **Total Saved 2853** by 23 Sep (weekly 120/100/110/40/90; spends 42/18/12; cashback 15).
- Roster: "Oct BTO list aaya" doc — *"naye roster me last week ghanta kam hua, Suresh se confirm karna hai."* Outlook has "October Roster - Saturday Overtime aur Duty Timing" (2 Oct).

# Hatch app-data archive

- Comparison: `f3389d8e-b64e-436a-923b-147151a7618b`
- Session: `6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5`
- App data: 15/15 complete
- Media: 273/274 downloaded

Each app folder contains `raw-state.json` (canonical lossless source), normalized JSON/CSV datasets, one readable Excel workbook, `media/`, and `media-manifest.json`. Datasets ending in `-with-local-media` add exact local paths beside attachment fields, including WhatsApp messages.

## Apps

| App | Tables | Rows | Workbook | Media |
|---|---:|---:|---|---:|
| gmail | 6 | 1635 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/01-gmail/gmail-data.xlsx` | 0/0 |
| google-contacts | 3 | 340 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/02-google-contacts/google-contacts-data.xlsx` | 30/30 |
| google-calendar | 3 | 95 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/03-google-calendar/google-calendar-data.xlsx` | 0/0 |
| google-drive | 2 | 53 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/04-google-drive/google-drive-data.xlsx` | 15/15 |
| google-sheets | 3 | 607 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/05-google-sheets/google-sheets-data.xlsx` | 0/0 |
| google-docs | 2 | 23 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/06-google-docs/google-docs-data.xlsx` | 0/0 |
| whatsapp | 4 | 1163 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/07-whatsapp/whatsapp-data.xlsx` | 172/172 |
| notion | 4 | 241 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/08-notion/notion-data.xlsx` | 0/0 |
| outlook-mail | 6 | 786 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/09-outlook-mail/outlook-mail-data.xlsx` | 0/0 |
| photos | 1 | 56 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/10-photos/photos-data.xlsx` | 55/56 |
| oura | 13 | 307 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/11-oura/oura-data.xlsx` | 0/0 |
| instagram | 7 | 90 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/12-instagram/instagram-data.xlsx` | 1/1 |
| hue | 13 | 59 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/13-hue/hue-data.xlsx` | 0/0 |
| nutrition | 4 | 384 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/14-nutrition/nutrition-data.xlsx` | 0/0 |
| healthex | 10 | 26 | `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/15-healthex/healthex-data.xlsx` | 0/0 |

## Table inventory

### gmail

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/01-gmail`

- `gmail_threads`: 304 rows, 4 columns
- `gmail_messages`: 320 rows, 10 columns
- `gmail_message_recipients`: 320 rows, 3 columns
- `gmail_labels`: 23 rows, 4 columns
- `gmail_message_labels`: 664 rows, 2 columns
- `gmail_attachments`: 4 rows, 6 columns

### google-contacts

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/02-google-contacts`

- `google_contacts`: 133 rows, 10 columns; local-media paths in `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/02-google-contacts/datasets/google-contacts-with-local-media.json`
- `google_contact_emails`: 95 rows, 3 columns
- `google_contact_phones`: 112 rows, 3 columns

### google-calendar

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/03-google-calendar`

- `google_calendars`: 3 rows, 6 columns
- `google_calendar_events`: 61 rows, 13 columns
- `google_calendar_attendees`: 31 rows, 3 columns

### google-drive

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/04-google-drive`

- `google_drive_items`: 34 rows, 11 columns; local-media paths in `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/04-google-drive/datasets/google-drive-items-with-local-media.json`
- `google_drive_permissions`: 19 rows, 3 columns

### google-sheets

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/05-google-sheets`

- `google_sheets_spreadsheets`: 8 rows, 6 columns
- `google_sheets_tabs`: 8 rows, 5 columns
- `google_sheets_cells`: 591 rows, 5 columns

### google-docs

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/06-google-docs`

- `google_docs_documents`: 7 rows, 6 columns
- `google_docs_content`: 16 rows, 6 columns

### whatsapp

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/07-whatsapp`

- `whatsapp_users`: 40 rows, 5 columns
- `whatsapp_conversations`: 36 rows, 5 columns
- `whatsapp_conversation_participants`: 78 rows, 2 columns
- `whatsapp_messages`: 1009 rows, 9 columns; local-media paths in `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/07-whatsapp/datasets/whatsapp-messages-with-local-media.json`

### notion

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/08-notion`

- `notion_databases`: 0 rows, 0 columns
- `notion_database_properties`: 0 rows, 0 columns
- `notion_pages`: 4 rows, 10 columns
- `notion_blocks`: 237 rows, 9 columns

### outlook-mail

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/09-outlook-mail`

- `outlook_mailbox_profile`: 1 rows, 5 columns
- `outlook_folders`: 9 rows, 6 columns
- `outlook_messages`: 354 rows, 14 columns
- `outlook_message_recipients`: 359 rows, 3 columns
- `outlook_attachments`: 0 rows, 0 columns
- `outlook_message_categories`: 63 rows, 2 columns

### photos

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/10-photos`

- `media_items`: 56 rows, 21 columns; local-media paths in `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/10-photos/datasets/media-items-with-local-media.json`

### oura

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/11-oura`

- `oura_personal_info`: 1 rows, 8 columns
- `oura_ring_configuration`: 1 rows, 7 columns
- `oura_daily_sleep`: 30 rows, 6 columns
- `oura_sleep`: 30 rows, 21 columns
- `oura_daily_activity`: 30 rows, 16 columns
- `oura_daily_readiness`: 30 rows, 8 columns
- `oura_daily_stress`: 30 rows, 6 columns
- `oura_daily_spo2`: 30 rows, 7 columns
- `oura_workout`: 22 rows, 14 columns
- `oura_session`: 3 rows, 10 columns
- `oura_sleep_time`: 30 rows, 7 columns
- `oura_enhanced_tag`: 40 rows, 6 columns
- `oura_daily_resilience`: 30 rows, 5 columns

### instagram

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/12-instagram`

- `instagram_accounts`: 1 rows, 6 columns
- `instagram_profiles`: 1 rows, 15 columns
- `instagram_users`: 29 rows, 5 columns
- `instagram_relationships`: 43 rows, 4 columns
- `instagram_posts`: 1 rows, 27 columns; local-media paths in `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/12-instagram/datasets/instagram-posts-with-local-media.json`
- `instagram_comments`: 3 rows, 8 columns
- `instagram_interests`: 12 rows, 4 columns

### hue

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/13-hue`

- `hue_devices`: 9 rows, 9 columns
- `hue_rooms`: 3 rows, 4 columns
- `hue_zones`: 1 rows, 4 columns
- `hue_lights`: 7 rows, 16 columns
- `hue_zone_lights`: 3 rows, 2 columns
- `hue_grouped_lights`: 3 rows, 4 columns
- `hue_scenes`: 7 rows, 8 columns
- `hue_scene_actions`: 17 rows, 7 columns
- `hue_motion_sensors`: 0 rows, 0 columns
- `hue_temperature_sensors`: 0 rows, 0 columns
- `hue_light_level_sensors`: 0 rows, 0 columns
- `hue_buttons`: 8 rows, 4 columns
- `hue_relative_rotary`: 1 rows, 4 columns

### nutrition

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/14-nutrition`

- `health_meals`: 115 rows, 14 columns
- `health_meal_items`: 269 rows, 14 columns
- `health_meal_plans`: 0 rows, 0 columns
- `health_meal_plan_entries`: 0 rows, 0 columns

### healthex

Folder: `sessions/6ea0c9a3-bb7c-4e39-99c3-14ad37fb44c5/apps/15-healthex`

- `healthex_patient`: 1 rows, 9 columns
- `healthex_conditions`: 0 rows, 0 columns
- `healthex_medications`: 0 rows, 0 columns
- `healthex_allergies`: 0 rows, 0 columns
- `healthex_observations`: 14 rows, 13 columns
- `healthex_vitals`: 5 rows, 7 columns
- `healthex_immunizations`: 3 rows, 7 columns
- `healthex_procedures`: 1 rows, 8 columns
- `healthex_encounters`: 1 rows, 8 columns
- `healthex_clinical_notes`: 1 rows, 8 columns

## Source media unavailable

These records exist in Hatch data, but the Hatch media endpoint did not return the referenced file:

- photos: `media/b2f0eb1758283386.jpg` at `root/tables/0/rows/18/rel_path`

## Privacy

This archive was created locally from the authenticated Hatch session. It was not uploaded by the exporter. Treat the contents as private profile data.

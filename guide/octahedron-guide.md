# Project Octahedron — Complete Reference

> Personal offline archive of the Project Octahedron fellow documentation, captured read-only from the authenticated site.
>
> - **Captured:** 2026-10-11
> - **Pages:** 22 of 22 distinct documentation pages archived (22 URLs discovered; 0 duplicate/alias, 0 excluded, 0 inaccessible, 0 failed)
> - **Content:** ~200119 characters
> - **Linked documents downloaded:** 0
> - **Images:** 39 placements of 26 locally stored image files under `assets/images/` (no image needs the website)
> - **Completeness:** Complete — every discovered in-scope page was processed and every safe accordion, tab, navigation group and read-only dialog was explored.
>
> Collapsed navigation groups, accordions and FAQ answers were expanded, every content tab was visited
> (tab panels appear under **Tab:** labels), and read-only dialogs were opened and closed before capture.
> Interactive checklists are reproduced as unticked task lists; no form, claim, timer or account control was used.

---

## Table of Contents

- [Welcome to Project Octahedron!](#welcome-to-project-octahedron)
- [Project Octahedron](#project-octahedron)
- [VPN setup](#vpn-setup)
  - [Hatch setup](#hatch-setup)
- [Comparison workflow](#comparison-workflow)
  - [Live tasking](#live-tasking)
  - [Prompt builder](#prompt-builder)
  - [Attaching screenshots](#attaching-screenshots)
  - [The thirteen use cases](#the-thirteen-use-cases-1)
  - [App capabilities](#app-capabilities)
  - [Score and choose](#score-and-choose)
  - [The 2+6 Dimensions](#the-26-dimensions)
  - [Complete the form](#complete-the-form)
- [Two-minute check](#two-minute-check)
- [When hatch breaks](#when-hatch-breaks)
- [Quality checks](#quality-checks)
- [Reference](#reference)
  - [Examples](#examples)
  - [Common mistakes](#common-mistakes)
  - [Check your understanding](#check-your-understanding)
  - [FAQ](#faq)
- [Reviewer checklist](#reviewer-checklist)
---

## Welcome to Project Octahedron!

<sub>nav label: *Introduction*</sub>

🎯 Goal

The goal of this project is to judge which of two AI personal assistants *communicates* better - and to explain it clearly enough that another careful reader would reach the same verdict. The bar is that it sounds human: a real AI companion, not an AI bot.

This is an **AI agent evaluation** project. You work inside **Hatch**, the customer's system, in a simulated person's digital life - their email, calendar, messages, notes, health data etc.. Each task starts with a **task prompt** that you write in that person's voice, anchored in data that actually exists in their universe.

The same request then runs on **two responses, A and B**. You read both in full and record one **Preference**, **eight comparative dimension scores**, and one **Required rationale**. Where a response takes an action or states a fact from the person's world, you check it against the environment - fluent and confident is not the same as correct.

Your Role: Judge

You are not scoring A and B in isolation. Every dimension is comparative - **1 favours A, 3 is a Tie, 5 favours B**. Your job is to name the concrete difference that decides it, and to make sure your Preference, scores and rationale all tell one story.

What "better" sounds like

Same moment, two replies. A long-time user who texts in clipped lowercase asks Hatch to rebook a flight. Both rebooked the flight.

✓ Sounds human

on it. flight's rebooked. you're now landing 6:40, you can still make the dinner.

✗ Sounds like a bot

Got it - happy to help! I've gone ahead and rebooked that flight and saved the info in your flighttracker.md file (790357887). As your always-on, golden-retriever-loyal travel sidekick, I made sure you're all set - you now land at 6:40. Do you want me to check on the dinner reservation too?

The second buries the answer under a ceremony opener, a forced persona, a filename with an ID number, and a forbidden "Do you want me to…" closing. That gap is what this project measures.

---

## Project Octahedron

<sub>nav label: *How a task works*</sub>

Start here. What the project is, the order of work, and the two gates you cannot skip.

Only for people who attended the onboarding zoom calls

If you did not attend an onboarding zoom call, stop here and do not start a task.

### What the project is for

1. Have a real conversation with Hatch, grounded in your persona's world.
2. Compare the two replies on how well each one communicates.
3. Record a judgment another reviewer can verify.

**The thing being measured is language.** Both arms usually do the same work behind the scenes. What separates them is how they write it back to you - the voice, the register, the tone, the structure. Correctness still counts and you still check any fact or action against the person's world, but the headline judgment is the communication.

Two systems, one task. **Hub** holds the task, the prompt, the evaluation, and the QC checks. **Hatch** runs the session and generates the two responses. You write and check in Hub, run in Hatch, then come back to Hub to get paid.

First time here? Do VPN setup and Hatch setup once, then come back.

### The order of work

The order - Hub writes and checks, Hatch runs, Hub pays

1. Hub

   1\. Task claimed

   Start task clicked, payable clock running

2. Hatch

   2\. Hatch session linked

   youralias_task_N, GAIA PREFERENCE, V2 universe

3. Gate

   3\. Task prompt green

   Do not continue until: Every prompt check passes before you open the annotation

4. Hatch

   4\. Hatch responses complete

   Both arms complete, same user turns, nothing reconstructed

5. Gate

   5\. Evaluation green

   Do not continue until: Preference, eight dimensions and Required rationale pass QC

6. Hub

   6\. Required Notes complete

   Every required text block filled - a blank block blocks submission

7. Hatch

   7\. Submit preference, then End comparison

   Both clicked, in that order

8. Gate

   8\. The exact session shows completed

   Do not continue until: Matched by name and UUID, not a neighbouring row

9. Hub

   9\. Exactly one screenshot

   One image of the completed comparison, nothing else

10. Gate

    10\. Not ended mid-annotation

    Do not continue until: The session does not read "Ended mid-annotation"

11. Hub

    11\. Session UUID and attestation complete

    UUID copied from Hatch, confirmation answered truthfully

12. Hub

    12\. Task submitted

    Only after every gate above is satisfied

The four hard gates

1. **No Hatch annotation before the task prompt is green.** Write the prompt in Hub and clear every prompt check first. Only then paste it into Hatch.
2. **No Hatch submission before the evaluation is green.** Preference, the eight dimension scores, and the Required rationale are entered in Hub and must clear QC before you click Submit preference.
3. **No task submission before the exact Hatch session is verified complete.** Match it by name and UUID and confirm it does not read **Ended mid-annotation**.
4. **No task submission before the submission gate is satisfied.** Required Notes filled, exactly one screenshot of the completed comparison, and the confirmation answered truthfully.

**One Hatch session = one Hub task.** The Hatch guidelines modal says to keep going for several rounds; that is generic Hatch guidance. Keep taking turns only while this task's goal is unfinished, then end the comparison and open a new session for the next Hub task.

A gate is never cleared by a note, and never by ticking a confirmation that is not true. Fix the thing, or abandon and replace the session.

### Do this now

Keep the live tasking page open

Live tasking has the per-step checklist and a consistency check for your eight scores, Preference, and Required rationale before you submit.

Working session name

youralias_task_N

Replace youralias with your exact lowercase chat alias and N with the task number.

Abandoned session name

youralias_abandonedtask_N

Rename an unusable session to this, then rerun in a replacement using the same task number.

1

#### Click Start task on Hub

Open Project Octahedron on Hub and click **Start task**. Keep the claimed task open while you work; it is your payable clock.

2

#### Copy your alias from chat

Open your chat profile and copy the **Alias** value under About me. You need it to name the Hatch session `youralias_task_N`.

3

#### Create a V2 Hatch session

Connect the VPN, open Hatch, choose **GAIA PREFERENCE**, type the session name, choose any V2 universe from the **Universe** dropdown, and choose **Hatch RM Style Task - current version**. Do not choose an Avocado protocol or any other protocol. Then click **Create session**.

4

#### Wait for RUNNING, then click Open

Wait while Hatch provisions the session. When the status changes to **RUNNING**, click **Open** in the **Actions** column. The **Annotation guidelines** modal opens by itself - read it, then close it with the **X**.

5

#### Explore Apps, then start the evaluated task

Click **Apps** and find the real records your request will use. Write the prompt in Hub and clear every QC check first. Then in Hatch click **Start comparison**, paste the exact approved prompt into the **Start annotation** dialog, and click **Start annotation**. Your evaluated task starts there.

6

#### Compare, submit the preference, end the comparison

Have a real conversation - ask, request, follow up the way a person would - and send every turn to both arms identically. Read both arms in full and check any claimed action or stated fact in Apps. Enter the Preference, the eight dimension scores, and the **Required rationale** in Hub, rerun QC, and fix every failure. Only then submit in Hatch - **Submit preference**, then **End comparison**. Capture the completion screenshot, confirm the session did not end mid-annotation, and submit the task for payment.

> **Info**
>
> Conversation is the default; single-turn happens
>
> Start a natural conversation and follow up the way a real person would - that is the normal shape of a task. Occasionally the system limits a comparison to a single turn and ends the conversation automatically. That is the system doing its job, not a broken task. Keep taking turns only while *this* task's goal is unfinished.

Your topic

Work the use-case category your task names. If your task does not name one, pick the category that matches your persona's underlying goal - and cover the range across your tasks rather than repeating one. Pick by the goal, not by the apps: *"move my Thursday run if it rains"* is Health & Fitness even though it edits the calendar.

Complete a comparison task

### Before you begin

Work through each item.

#### Checklist

0 of 7 complete

- [ ] Claim the Hub task first. It is your payable clock.
- [ ] Keep the task open while you work.
- [ ] Name the Hatch session `youralias_task_N` before you click Create session.
- [ ] Choose GAIA PREFERENCE, a V2 universe of your choice, and the protocol **Hatch RM Style Task - current version**.
- [ ] Click **Start comparison**, paste the prompt, then **Start annotation**.
- [ ] Work only from your persona's data.
- [ ] Never submit an incomplete session.

#### See all non-negotiables

1. Claim the Hub task before you open Hatch. The open task is your 75-minute payable clock.
2. Name the Hatch session `youralias_task_N` in the **Name** field before you click Create session. Rename only to correct a mistake.
3. Use **GAIA PREFERENCE** mode, a V2 universe of your choice, and the protocol **Hatch RM Style Task - current version**. No Avocado protocol is approved.
4. Explore the persona first, then click **Start comparison**, paste the prompt in the dialog, and click **Start annotation**. Anything sent before that is context setting, not your task.
5. Ground the prompt in your persona's data and invent nothing. Only rely on the live web when the guidelines modal says **Internet: Available**; if it does not, the prompt must be answerable from the persona's records alone.
6. Only ask for actions the apps can perform.
7. Send the same user turns to both arms, in the same order and the same words.
8. Never submit when a response is missing, failed, or cut off. Recreate the task instead.
9. You are not auditing every step of the behind-the-scenes work - but check every fact and claimed action that **Correctness** rests on. "Sent", "created", "updated" have to be visible in Apps.
10. Copy the session name, session ID, and persona name exactly. The name and the ID are different fields.
11. Your eight dimension scores, your Required rationale, and your preference must tell one story.
12. Submit the preference and end the comparison in Hatch before you finish the Hub form.
13. Notes explain small problems. They never excuse missing work.


> **Warning**
>
> The one mistake you cannot undo
>
> Scores and Notes can be edited after a task comes back. A broken session cannot. If a response failed, was cut off, or never received all your turns, recreate the task.

### How judging works, in one paragraph

What decides it

The two arms are the same model family with a style note appended, and each is told to apply that note to how it writes, not to what it does. So the actions are held roughly constant and the comparison is mostly about communication: Style, Tone, and Coherence & writing quality do real work here. Style never rescues a wrong action, missing work, an unsupported claim, or a fabricated fact - but where the substance matches, the writing decides it.

Longer is not automatically better and shorter is not automatically better: extra detail earns its place only when it adds useful information, action, context or structure.

When correctness and completeness are close, the Style, Tone, and Coherence & writing quality dimensions can decide the preference. Style never rescues a wrong action, missing work, an unsupported claim, or a fabricated fact.

### What sends tasks back

| Failure | Where it is prevented |
| --- | --- |
| Prompt needs the web in an environment without internet access | Prompt builder |
| Prompt asks for an unsupported app action | App capabilities |
| One response arm never completed | When Hatch breaks |
| A claimed action was never verified | Comparison workflow, step 9 |
| A prompt turn or transcript turn is missing | Complete the form |
| Scores, Required rationale, and preference disagree | Score and choose |
| A 3 / Tie on a communication dimension where the two replies visibly differ | Score and choose |
| A pair that should have been skipped was scored anyway | When something breaks |

### Where everything lives

| When | Page |
| --- | --- |
| Before your first task, once | VPN setup, Hatch setup |
| Running a task, step by step | Comparison workflow |
| Open in a second tab while tasking | Live tasking |
| Writing the prompt | Prompt builder, App capabilities |
| Judging and writing the rationale | Score and choose, The six dimensions, Complete the form |
| Last look before submitting | Two-minute check |
| Something broke | When Hatch breaks |
| Practising and the quality bar | Quality checks |
| Occasional lookups | Reference, Examples, Common mistakes, FAQ |

Next: Set up your tools.

---

## VPN setup

<sub>nav label: *1. Set up your tools*</sub>

Hatch only accepts connections from the project network, so connect the VPN before you start tasking. Your username and password come from your onboarding email.

**You will receive your VPN login credentials, username and password, from your coordinator on chat**

Use Google Authenticator for 2FA

For the 2-step verification factor authentication (2FA), please use the Google Authenticator app.

Your credentials come from your email

The username is your assigned ID plus your project name - for example `yourid-yourproject`. The password is the random string in the same email. Never paste real credentials into Hub form, chat, or a screenshot.

1

### Step 1 - Install OpenVPN Connect

Download and install the OpenVPN Connect app for your operating system from [openvpn.net/client](https://openvpn.net/client/).

2

### Step 2 - Add the project server URL

Open the app, choose to connect with a **Server URL**, and enter the project VPN server URL provided in your onboarding email. Then click **Continue**.

3

### Step 3 - Sign in and import your profile

Sign in to the portal with the username and password from your email - the username looks like `yourid-yourproject`. Download your personal profile file from the portal, then open it with OpenVPN Connect if it does not import automatically.

4

### Step 4 - Connect

Select your `yourid-yourproject` profile and click **Connect**. Enter the same username and password if prompted. You are connected when the app shows **Securely Connected!** with a green indicator.

5

### Step 5 - Sign into Hatch

With the VPN connected, go to Hatch and sign in using the link and credentials provided. If Hatch will not load, check that OpenVPN still shows **Securely Connected**.

*Step 2 - enter the project server URL, then click Continue.*

*Step 4 - your profile appears under your assigned ID. Click Connect.*

*Connected - the header reads Securely Connected! and the profile dot turns green.*

Next: Hatch setup.

---

## Hatch setup

<sub>section: **1. Set up your tools**</sub>

Setup 2 of 2 - create your account, create a V2 session, and open it.

**Note:** You will receive your Hatch login credentials and link by email.

### Create your hatch account

Connect the VPN, then create your Hatch account using your project credentials.

Use Google Authenticator for 2FA

For the 2-step verification factor authentication (2FA), please use the Google Authenticator app.

### Create the session

Your session name starts with your assigned chat alias - copy it, do not invent one.

1

#### Choose GAIA PREFERENCE

In the **Create session** card, click **GAIA PREFERENCE** - compare two models and pick a preference. **GAIA RUBRICS** and **EDUCATION** are other projects. Do not choose them.

2

#### Name the session before you create it

Type `youralias_task_N` into the **Name** field - for example `488c89ae9c3f_task_1`. Name it correctly up front; renaming is only the correction path.

3

#### Choose a V2 universe

Pick any V2 **Universe** (your persona) from the Universe dropdown - you are not assigned one, choose whichever you like.

4

#### Choose the approved protocol

Open **Protocol** and choose **Hatch RM Style Task - current version**. Do not choose an Avocado protocol or any other protocol.

5

#### Click Create session

Click **+ Create session**. The session appears in the list as provisioning.

*The full Create session card: choose GAIA PREFERENCE, name the session, pick a V2 universe, choose Hatch RM Style Task, then click + Create session. Avocado protocols are not used.*

*Choose Hatch RM Style Task - current version. Do not choose an Avocado protocol.*

> **Info**
>
> The protocol version is not the persona version
>
> Always pick the **latest published version** of the **Hatch RM Style Task** protocol - Hatch has moved from v5 to v7, and it will keep moving. Whatever the newest version shown in the dropdown is, that is the one to use. That version label is not the persona version. Your persona version comes from the **Universe** you pick - use **V2 universes only**, V1 is no longer in use. Subpersonas are fine. The core apps are the same across versions; V2 adds a few.

### Open the session

*When the status turns RUNNING, click Open in the Actions column.*

- Wait for the status to change from **PROVISIONING** to **RUNNING**.
- Click **Open** to enter the session.
- Use the three-dot menu next to **Open** to **Rename** the session only if the name is wrong.
- **Restart** and **Delete** are not normal workflow steps.
- If a session must be abandoned, rename it `youralias_abandonedtask_N` and follow the recovery steps.

### Read the guidelines modal

*The modal opens when the session starts. Read the persona, available apps, and annotation guidance, then close it with the X.*

It tells you the universe/persona you chose, the connected apps available in this session, and basic annotation behavior.

Check whether the environment has internet access

Some environments display **Internet: Available**. In those, the assistant can pull from the live web, so your prompt may rely on it. In environments without internet access, the prompt must be answerable from the persona's records alone. Either way, keep the task grounded in real persona records.

### Reference: Find your alias in chat

*1. Click your chat avatar, then click Profile.*

*2. In the profile panel, find Alias under About me and copy it exactly. The value shown is only an example - use your own.*

Session name format: `youralias_task_N` - for example `488c89ae9c3f_task_1`.

Next: Comparison workflow.

---

## Comparison workflow

<sub>nav label: *2. Run a task / The 11 steps*</sub>

Run a task - the eleven steps in order, from claiming the task to getting paid.

Practise this before your next task

Quality checks collects the hard rules, the app matrix, and the screenshot rules in one place - and links the live practice page where you can write a task prompt and record a judgment and get the same checks a reviewer applies.

The whole task, in order. Open one step at a time and work down. Everything a normal task needs is here; deeper help is linked from the step that needs it.

**The Hub gates, Hatch does the work.** The task is claimed on Hub, the comparison runs in Hatch, and Hub decides whether the finished task is accepted. Work the sequence in this order - a Hatch session created before the task is claimed is unpaid time, and a task submitted before the Hatch evaluation is complete is rejected.

Keep the live tasking page open

Live tasking has the per-step checklist and a consistency check for your eight scores, Preference, and Required rationale before you submit.

### 1. Start the Hub task

Open Project Octahedron on Hub and click **Start task**. Keep the task open for the whole task - it is your payable clock.

**Done when** the task is claimed and open in a tab, and you have not opened Hatch yet.

**Common mistake:** working in Hatch first. Time without an open task is not tracked.

### 2. Create the Hatch session

Connect the VPN, open Hatch, and fill in the **Create session** card:

1. Choose **GAIA PREFERENCE**. Not GAIA RUBRICS, not EDUCATION.
2. Type the session name into the **Name** field: `youralias_task_N`. Your alias comes from chat.
3. Choose any V2 **Universe** from the dropdown - pick whichever one you want.
4. Choose **Hatch RM Style Task - current version**. Do not choose an Avocado protocol or any other protocol.
5. Click **Create session**.

**Done when** mode is GAIA PREFERENCE, the Name field reads `youralias_task_N`, the universe is a V2 universe, and the protocol is Hatch RM Style Task - current version.

**Common mistake:** choosing an Avocado protocol or any protocol other than Hatch RM Style Task - current version.

### 3. Wait for RUNNING, then click Open

After you click **Create session**, wait while Hatch provisions the session. When the status changes from **PROVISIONING** to **RUNNING**, click **Open** in the **Actions** column.

**You should now see the session status as RUNNING and an Open action. If not, wait before continuing.**

Use the three-dot menu to **Rename** only if the name is wrong. **Restart** and **Delete** are not normal steps.

**Common mistake:** submitting a session whose name is a UUID. The session name and the session ID are different.

### 4. Read the guidelines modal

The **Annotation guidelines** modal opens automatically. Read it, then close it with the **X**.

**You should now be inside the session with the Annotation guidelines modal visible.**

The modal lists your persona, the connected apps, and basic annotation behavior. Check whether it says **Internet: Available**. If it does, the assistant can pull from the live web and your prompt may rely on it. If it does not, your prompt must be answerable from the persona's records alone.

### 5. Explore Apps and find real records

Click **Apps** in the top right and browse the persona's apps. Find the real emails, calendar events, messages, files, health records, or other records your request will rely on.

Explore only. Do not start the task conversation yet.

**Common mistake:** writing the request first and hoping the records match.

### 6. Write the prompt and clear prompt QC

Write one first-person request in the persona's voice, grounded in records that exist. Enter it in Hub, not in Hatch. Then run every QC check and the evaluation page. Do not open the Hatch annotation until the prompt clears.

**Done when** all six are true:

- Grounded in real persona data, usually more than one record.
- Requires the apps, not just chat.
- Answerable without the public web - unless the guidelines modal says **Internet: Available**.
- Every requested action is supported.
- Dates are covered by the persona's records.
- The goal is clear without scripting every click.

**Common mistake:** a request that needs current public information.

### 7. Start comparison → paste the request → Start annotation

1. Click **Start comparison** at the bottom right.
2. The **Start annotation** dialog opens.
3. Paste the **exact approved prompt** into that dialog - word for word, no edits.
4. Click **Start annotation** inside the dialog.

**Everything before this is setup and exploration. Your evaluated task starts when you click Start annotation.**

**You should now see Arm A and Arm B. Your evaluated task has started.**

**Common mistake:** looking for Start annotation before opening the comparison. The dialog only appears after **Start comparison**.

### 8. Run both arms, with follow-up turns if the task needs them

Read both arms side by side, and have a real conversation - ask, request, follow up the way a person actually would. Multi-turn is the normal shape of a task.

A goal is the user's underlying intent - what they actually want to achieve, not the literal words. Continue only while there is more of that same goal to complete.

- If the task needs another user turn, type it yourself and send it to **both** arms, with the same meaning, wording, and order.
- Do not steer one arm differently.
- Once the goal is satisfied, stop and evaluate the full interaction.

**One session, one Hub task.** The Hatch **Annotation guidelines** modal says you normally keep going round after round - that is generic Hatch guidance and it does not apply here. Every Hatch session is tied to exactly one Hub task. Stay in this session only while there is more of *this* task's goal to complete. When the goal is satisfied, evaluate, end the comparison, and create a **new** session for the next Hub task. Never cover two Hub tasks with extra turns in one session.

**Single-turn comparisons happen.** Occasionally the system limits a comparison to one turn and ends the conversation automatically. That is the system doing its job, not a failure - score the single exchange you got.

**Done when** both arms received the same initial request and the same follow-up turns, and both responses generated completely and were read in full.

**If an arm did not complete:** stop. Do not score it and do not submit. Retry the failed arm, then the session. If it is unrecoverable, rename it `youralias_abandonedtask_N`, create a new session, and rerun the task from the beginning. Notes cannot repair a missing, failed, copied, reconstructed, or cut-off response.

### 9. Check the facts and actions behind Correctness

You do not need to audit every step of the behind-the-scenes work. But where a reply **takes an action or states a fact from the person's world** - a date, a name, a figure, a recipient, something it says it did - check it in **Apps** before you score Correctness. Fluent and confident is not the same as correct.

- Did the claimed draft exist?
- Did the calendar event exist?
- Was the correct app used?
- Was anything sent when it should only have been drafted?
- Were the recipient, date, time, attachment, and content correct?
- Did the model claim an action the app does not support?

**Common mistake:** scoring the words instead of the work.

### 10. Enter the evaluation, clear QC, then submit in Hatch

Enter the Preference, the eight dimension scores, and the **Required rationale** in Hub first. Run every QC check again and fix all failures. Only once nothing needs attention do you record the same values in Hatch, click **Submit preference**, then **End comparison**. Judge the full interaction, including turns where you had to steer a model back.

1. **Score all eight comparative dimensions.** One value each: **1 = A much better · 2 = A better · 3 = Tie · 4 = B better · 5 = B much better**. The dimensions are Style and behavior (High level), Correctness (High level), Style (Granular), Coherence & writing quality (Granular), Helpfulness (Granular), Completeness (Granular), Tone (Granular), and Warmth (Granular).
2. **Choose the overall Preference:** A significantly better · A slightly better · Tie · B slightly better · B significantly better - the headline judgment, not the average of the eight numbers.
3. **Write the Required rationale.** Explain the preference and support every score away from 3 with something concrete you can point at.
4. Click **Submit preference**.
5. Click **End comparison**.

**Do not score the example failure shown in this screenshot. If either live arm says "Something went wrong," is missing, or is cut off, stop. Retry or recreate the session. Never submit an incomplete comparison.**

Score each dimension independently - A can be more correct while B communicates better.

**3 means identical.** On the six communication dimensions, a 3 says the two replies were indistinguishable on that dimension - which is rare. If you can see a difference, score it 2 or 4. Correctness is the exception: the two arms usually do the same work, so 3 there is common and correct. Length is not a score: longer is not better, and shorter is not better.

**Done when** all eight scores are filled, no communication dimension is a 3 unless the two replies were genuinely identical on it, every non-3 score has concrete support in the Required rationale, the Preference and the rationale agree, A and B are not swapped, length alone did not choose the winner, and the preference was submitted and the comparison ended.

**Common mistake:** forcing all eight numbers to favour the same arm, or rewarding the longer response.

### 11. Verify the exact session, screenshot it once, then submit for payment

Go back to the Hatch sessions list and find **the session you worked in**, matched by name **and** by the session UUID you are about to enter. Confirm that row reads completed and does **not** read **Ended mid-annotation**. A neighbouring completed row is not evidence for your session.

Then take **exactly one** screenshot of the completed comparison - not the sessions dashboard, not the form you were filling in, not several images.

Copy the session name and session UUID exactly, enter the human persona name, pick the category from the user's goal, list the apps both arms actually invoked, paste every user turn in order, and add the transcripts your task asks for. Fill the required **Notes** block - "Nothing I noticed at the moment" is a valid entry - and answer the confirmation block truthfully.

Run the two-minute check, then submit.

**Hub blocks submission when** a required step is empty or invalid - a blank Notes block, a missing screenshot, a missing score or rationale, or a preference never submitted in Hatch.

Work the feedback panel until it reads **Nothing needs attention**. That state - not your own sense of being finished - is the submit gate.

**You get a warning when** the rationale leaves a non-3 score unexplained, all eight dimensions are 3 but the preference is not Tie, "significantly better" is chosen on a tiny gap, the rationale praises the arm the scores went against, or the write-up mentions a failed or missing response.

Warnings clear once you fix the write-up. A missing response never clears.

Never submit an incomplete comparison

If either arm is missing, failed, cut off, or did not receive all your user turns, stop. Do not score it, and do not explain it in Notes. Recreate the session.

Next: Two-minute check before you submit. Keep Live tasking open while you work.

---

## Live tasking

<sub>section: **2. Run a task** · nav label: *Live task companion*</sub>

Keep this open in a second tab while you run the task. Five short checklists, then a consistency check before you submit.

Three things fail a task before quality is even judged

Both arms must get the **same user turns**. Both arms must produce a **complete user-facing response**. Nothing may be **reconstructed, copied between arms, or pasted from the wrong run**. If any of those breaks, stop and recreate the session.

The order - Hub writes and checks, Hatch runs, Hub pays

1. Hub

   1\. Task claimed

   Start task clicked, payable clock running

2. Hatch

   2\. Hatch session linked

   youralias_task_N, GAIA PREFERENCE, V2 universe

3. Gate

   3\. Task prompt green

   Do not continue until: Every prompt check passes before you open the annotation

4. Hatch

   4\. Hatch responses complete

   Both arms complete, same user turns, nothing reconstructed

5. Gate

   5\. Evaluation green

   Do not continue until: Preference, eight dimensions and Required rationale pass QC

6. Hub

   6\. Required Notes complete

   Every required text block filled - a blank block blocks submission

7. Hatch

   7\. Submit preference, then End comparison

   Both clicked, in that order

8. Gate

   8\. The exact session shows completed

   Do not continue until: Matched by name and UUID, not a neighbouring row

9. Hub

   9\. Exactly one screenshot

   One image of the completed comparison, nothing else

10. Gate

    10\. Not ended mid-annotation

    Do not continue until: The session does not read "Ended mid-annotation"

11. Hub

    11\. Session UUID and attestation complete

    UUID copied from Hatch, confirmation answered truthfully

12. Hub

    12\. Task submitted

    Only after every gate above is satisfied

Working session name

youralias_task_N

Exact lowercase chat alias, then the task number.

Abandoned session name

youralias_abandonedtask_N

Same task number as the failed run. Never submitted.

### 1. Setup

Thirty seconds here prevents a rejected submission.

#### Before you create the session

0 of 5 complete

- [ ] Mode is **GAIA PREFERENCE** - not GAIA RUBRICS.
- [ ] Universe is a **V2** universe of your choice from the dropdown.
- [ ] Protocol is **Hatch RM Style Task** at the **latest Published version** shown in the dropdown. An old screenshot is not a reason to pick an older version.
- [ ] Session name is `youralias_task_N` - your chat alias, lowercase, no spaces. The session name and the session **ID** (a UUID) are different values.
- [ ] You read the guidelines modal and know whether it says **Internet: Available**.

*Shown when every item above is ticked:* Anything you had to guess at? Check Hatch setup before you continue.

### 2. Prompt - Write it, clear qc, then paste into hatch

A prompt the environment cannot serve produces an unscoreable comparison.

#### Before you click Start annotation

0 of 6 complete

- [ ] You can point at the **actual records** this request is based on, in the persona's apps, right now.
- [ ] Written in first person, in the persona's voice, with one underlying goal.
- [ ] Every action you ask for is **supported** by that app - no Outlook drafts, no new WhatsApp chats or groups, no editing Contacts, Oura, Photos, or Health Records.
- [ ] Relative dates ("this week", "recent") are covered by records that actually exist in that window.
- [ ] If the environment does **not** say Internet: Available, the request is answerable from the persona's records alone.
- [ ] You gave the goal and the real constraints - not a click-by-click script. Both arms need room to make decisions worth comparing.

*Shown when every item above is ticked:* Could a stranger tell whether the assistant succeeded? If not, tighten the success condition.

### 3. Run both arms

One Hatch session = one Hub task

The Hatch guidelines modal tells you to keep going round after round. Ignore that across tasks. Send follow-up turns only while *this* task's goal is unfinished. When it is done, submit the preference, end the comparison, and create a new session for the next Hub task. Never stretch one session over two Hub tasks.

Have a real conversation and follow up the way a person would - that is the normal shape. If the system caps the comparison at a single turn and ends it automatically, that is expected; score the exchange you got.

This is the integrity layer. It is not recoverable after the fact.

#### While the comparison is live

0 of 5 complete

- [ ] Every follow-up turn went to **both** arms with the same meaning, wording, and order.
- [ ] Both arms produced a substantive final response - nothing cut off, missing, or error-only.
- [ ] An error that was followed by a real complete response is **recovered** - that arm is still valid. Only an unrecovered error-only arm kills the task.
- [ ] Nothing was reconstructed, summarized, cleaned up, or copied from the other arm.
- [ ] The pair is fair to score - the two sides have not diverged, no prompt is duplicated, and nothing the prompt refers to is missing. If any of those is true, do not score it.

*Shown when every item above is ticked:* If an arm is unrecoverable: rename it `youralias_abandonedtask_N`, create a replacement with the same task number, and rerun from the beginning.

### 4. Verify in apps

Where a reply states a fact or claims an action, the message is a claim and Apps is the evidence. You are not auditing every step - you are checking what Correctness rests on.

#### Check the work, not the wording

0 of 5 complete

- [ ] Every claimed artifact actually exists - the draft, the event, the file, the row, the message.
- [ ] **Drafted vs sent** is correct. Anything sent that should only have been drafted is a real failure, not a note.
- [ ] Recipient, date, year, time, timezone, attendees, and attachments match what was asked.
- [ ] No extra CC/BCC, no added attendees, no unrelated edits or deletions.
- [ ] **Apps Utilized** is the union of apps *either* arm actually operated - including read-only sources, and excluding apps that were merely mentioned or available.

*Shown when every item above is ticked:* Recovery does not erase an irreversible mistake. A wrongly sent email still counts against that arm.

### 5. Score, clear qc, submit in hatch, then verify and get paid

Score first, then run the consistency check below.

#### Before you click Submit preference

0 of 6 complete

- [ ] You scored each dimension on its own evidence. The eight sliders are **not votes** for your overall winner.
- [ ] No 3 on a communication dimension unless the two replies were genuinely identical on it. Correctness is the one where 3 is common.
- [ ] Style and behavior is about **communication**. Correctness is about **facts and actions you verified**. Neither borrowed the other's evidence.
- [ ] Length decided nothing. Longer is not more complete; shorter is not cleaner.
- [ ] The rationale names concrete, checkable differences - and you checked that no "only A did X" claim is actually true of both arms.
- [ ] **Submit preference** clicked, **End comparison** clicked, then the Hub fields copied exactly from the completed Hatch evaluation.

*Shown when every item above is ticked:* If the locked Hatch evaluation is wrong, do not compensate with different values on Hub. Recreate the comparison.

### Consistency check

Enter what you are about to submit. **Basic check** reads your eight scores, your Preference, and your rationale. **Deep check** also takes the prompt and both full trajectories, which lets it check your claims literally against the two responses.

Results come in three levels: **STOP** for things that make the submission invalid or self-contradictory, **REVIEW** for calibration worth a second look, and **CLEAR** when nothing material is wrong. Mixed slider directions are legitimate - they are never flagged on their own.

#### Check my evaluation before I submit

Nothing here is stored or sent. It reads only what you type in.

*Options: Basic check · Deep check*

Scores, Preference, and rationale. Catches contradictions inside your own evaluation.

Eight comparative dimensions

1 = A much better · 3 = Tie · 5 = B much better

Style and behavior (High level) — Not scored

Correctness (High level) — Not scored

Style (Granular) — Not scored

Coherence & writing quality (Granular) — Not scored

Helpfulness (Granular) — Not scored

Completeness (Granular) — Not scored

Tone (Granular) — Not scored

Overall Preference

*Options: A significantly better · A slightly better · Tie · B slightly better · B significantly better*

Required rationale

Paste the rationale you are about to submit. Name the concrete A/B differences that drove the Preference and the scores away from Tie. One concrete fact can support several related dimensions - you do not need eight paragraphs.

Evidence ledger (optional)

Log up to four deciding claims. This is not your rationale - it forces you to look at your own evidence one claim at a time.

**Check my evaluation**

Runs in your browser.

> **Info**
>
> What this cannot check
>
> It matches literal text. It cannot judge meaning, so a fact reworded in the other arm will not be caught, and uncertain matches are marked for manual review rather than failed. Before you claim a difference, look for the same thing - or a synonym of it - in the other response. In our manually reviewed set of confirmed failures, about 7 in 10 involved the rationale misreading or reversing something visible in A or B.

Full definitions: The six dimensions and Score and choose. Last look before submitting: Two-minute check.

---

## Prompt builder

<sub>section: **2. Run a task** · nav label: *Write the prompt*</sub>

Step 3 - write the prompt and clear prompt QC before Hatch sees it.

Four questions. Answer them before you send anything. If a prompt fails one, rewrite it - a bad prompt cannot be rescued by good scoring.

### Explore the persona first

*Click Apps in the top right and browse the persona's apps before you write the task.*

- Click **Apps** in the top right.
- Browse the available persona apps before writing the task.
- Find the real emails, calendar events, messages, files, health records, or other records the prompt will rely on.
- Build the request from records that actually exist.
- Do not invent context.

**Check your prompt** *(interactive self-check; every question shown with its options, feedback and stated answer)*

**1. Is it grounded?**

Is the prompt based on a real email, event, message, document, contact, transaction, or health record in the persona's accounts?

- **Yes** (expected answer) — Good. Grounded prompts are the only ones a reviewer can verify.
- No — Explore the persona first. Do not invent the task context.

**2. Is it feasible?**

Can the connected apps perform the requested reads or writes?

- **Yes** (expected answer) — Good. Every requested action is supported.
- Unsure — Open the app capability table before you run it.

**3. Does the task match the environment's internet access?**

If the guidelines modal says Internet: Available, web-dependent asks are allowed. If it does not, everything the assistant needs must already be in the persona's apps.

- **Yes** (expected answer) — Good. The task fits what this environment can reach.
- No — No internet in this environment? Rewrite the task around records the persona already has.

**4. Is the goal clear without scripting every click?**

Would two capable assistants produce identical output because you dictated every step?

- Yes, identical — Too mechanical. Give the goal and let the assistant make real decisions.
- **No, they would differ in defensible ways** (expected answer) — Right. That difference is what you are there to judge.

### Help for each question

#### Grounding - what counts

Build the request on emails, calendar events, chat messages, documents, contacts, transactions, or health records that exist in the persona's accounts. Usually more than one, so the assistant has to connect things.

Nothing fabricated. If you cannot point at the record, the prompt is not grounded.

#### Feasibility - the short version

Gmail can draft and send. Calendar, Drive, Docs, Sheets, and Notion can be written. WhatsApp can send inside existing chats only. Outlook Mail can send but cannot draft. Google Contacts and Oura are read only.

#### Common web-dependent prompts

- Current prices
- Current sold listings
- Current events
- Current restaurants
- Current trails
- Current weather
- Sports schedules
- Book-release dates
- Travel recommendations
- Live availability or current trends
- "Where should I go?" when it needs current public recommendations
- "What is popular right now?"

A valid prompt does not become invalid merely because one model unnecessarily browses. Grade that model's response.

#### The valid middle ground

Too vague: *"Help me organize my life."*

Too mechanical: *"Open Sheet X and change B4 to $18."*

Better: *"Review my April expenses and update my budget tracker with anything missing."*

#### The thirteen use cases

Pick by the **goal, not the apps** - *"move my Thursday run if it rains"* is Health & Fitness even though it edits the calendar.

**Personal Productivity is no longer available.** Do not use it.

**Spread your tasks across the list.** **Companionship / Chat, Legal / Civic, Home Automation, Shopping, Entertainment** and **Travel** are the thinnest - reach for one of those when your task does not name a category.

Most of what is new is conversation, not errands

In Companionship, Emotional Support, Entertainment and Media Creation there is often no work for Hatch to do behind the scenes at all. Nothing gets booked, moved, or looked up. **The reply is the whole task** - so what is left to judge is the language: the writing, the voice, the register, the tone. You are not scoring whether the assistant is capable. You are scoring how it talks.

That is not a broken task and it is not a reason to skip.

> **Warning**
>
> Conversation does not mean invented
>
> Every prompt still has to be anchored in this person's data. Emotional support about their day means something actually on their calendar that day. Relationships means their real partner or friend - the one who lives in this environment. There is always something for Hatch to fetch.
>
> A chatty prompt with nothing behind it is still an ungrounded prompt.

> **Warning**
>
> Date coverage
>
> If your prompt uses **today, this week, this weekend, next week, current, upcoming, recent,** or **latest**, confirm that the persona's available records cover this period. An empty inbox or calendar does not prove that nothing happened after the available data ends.
>
> Use an exact range instead: "during April 2026", "the week of March 9", "for the August 15 wedding".

### One contrast per rule

Good

My saved concert emails have three shows I said I'd go to this spring. Put them on my calendar and flag the one that conflicts with the Hartford trip.

Bad

What concerts should I go to this month?

> **Info**
>
> The good version is answerable from the inbox and calendar alone. The bad one needs current public listings.

Good

I told Alicia I'd do the 5k with her. Get it on my calendar with enough lead time to train.

Bad

Create a calendar event named "5k" on April 18 at 9:00am with a 30-minute reminder.

> **Info**
>
> The good version leaves the assistant real decisions. The bad one is a set of instructions to transcribe.

### Prompt ready

Work through each item.

#### Checklist

0 of 8 complete

- [ ] First person, in the persona's voice.
- [ ] Grounded in records that exist.
- [ ] Requires app use.
- [ ] No public-web dependency.
- [ ] Supported actions only.
- [ ] Clear success condition.
- [ ] Not excessively prescribed.
- [ ] The use-case category matches the persona's underlying goal, not the apps the task happens to touch.

Next: check the request against App capabilities.

---

## Attaching screenshots

<sub>section: **2. Run a task**</sub>

What the one required screenshot has to show, and when to take it.

Every comparison task needs **exactly one** screenshot attached as evidence of the completed comparison - one image, not two, not a set.

That single image has to carry two things at once. If it cannot show both legibly, reframe the window until it can.

1. **Both arms side by side.** Arm A and Arm B conversations in the same shot, large enough that the text in each is actually readable. Do not shrink the window until the replies become grey lines.
2. **The completed "Pick the better response" panel.** The top-level preference pick, all eight dimensions answered - Style and behavior, Correctness, Style (Granular), Coherence & writing quality, Helpfulness, Completeness, Tone, Warmth - and the **Required rationale** field filled in.

*Example - Arm A / Arm B side by side, text legible.*

*Example - the scoring panel, with all eight dimensions and the Required rationale to fill in before you capture it.*

### When to take it

Take the screenshot only after the form is complete

Never capture a blank or half-filled panel. Every one of the eight dimensions must be answered and the **Required rationale** written before you press the shutter.

The order is: score the evaluation, clear QC, then in Hatch click **Submit preference** and **End comparison** - and only then take the screenshot, as part of step 11.

### Why it matters

The screenshot is what the Hub QC check reads back against that same session, so it has to show the **exact completed session** on your task - matched by session **name** and by session **UUID**, not a neighbouring row that also looks finished, and not an earlier state of your own work.

A dashboard view, a **Stopped session** row, or the form you were still filling in are not evidence. If you moved to a replacement session, take the screenshot from the replacement and repoint both the name and the UUID.

---

## The thirteen use cases

<sub>section: **2. Run a task**</sub>

What each category covers, which ones are thinnest, and how to pick the right one.

Every task belongs to one use case. Pick by the **goal, not the apps** - *"move my Thursday run if it rains"* is Health & Fitness even though it edits the calendar.

If your task names a category, work that one. If it does not, pick the category that matches your persona's underlying goal.

> **Warning**
>
> Personal Productivity is no longer available
>
> Do not use it. A calendar-or-reminders task belongs to the goal behind it - the run you are moving is **Health & Fitness**, the meeting prep is **Work Productivity / SMB**, the trip planning is **Travel**.

### The thirteen categories

| Use case | What to talk about |
| --- | --- |
| Companionship / Chat | Just chatting: how your day went, your opinion on something, casual back-and-forth, catching up. |
| Learning / Research | "Explain how X works," researching the best options for Y, summarising something, help learning a skill. |
| Health & Fitness | Workouts, meal and nutrition ideas, tracking progress, sleep, general wellness questions. |
| Shopping | Finding a product, comparing options, recommendations for a purchase, deals, gift ideas. |
| Media Creation | Help creating something: writing a post or story, drafting a caption, brainstorming a creative project, an image idea. |
| Work Productivity / SMB | Drafting a work email or doc, planning a project, meeting prep, small-business tasks. |
| Entertainment | Recommendations for shows, movies, music, games; fun things to do; something to make you laugh. |
| Emotional Support | Talking through a stressful day, working through a feeling, encouragement, venting. |
| Finance | Budgeting, tracking expenses, a money question, planning a purchase. |
| Travel | Planning a trip, building an itinerary, destination or restaurant ideas, packing help. |
| Relationships | Advice about a friend, partner, or family member; help wording a hard message; planning something for someone. |
| Legal / Civic | Understanding a rule or process, a civic question, help making sense of a form or document - general info, not formal legal advice. |
| Home Automation | Controlling smart-home devices, setting up a routine, troubleshooting a device. |

### Spread your tasks across the list

Reach for the thinnest categories first

Some categories are heavily worked already and some are barely touched. **Companionship / Chat, Legal / Civic, Home Automation, Shopping, Entertainment** and **Travel** are the thinnest.

When your task does not name a category, pick one of those before repeating a category you have already done.

Six categories are new: **Companionship / Chat, Media Creation, Entertainment, Emotional Support, Legal / Civic** and **Home Automation**.

### Most of what is new is conversation, not errands

The reply is the whole task

In Companionship, Emotional Support, Entertainment and Media Creation there is often no work for Hatch to do behind the scenes at all. Nothing gets booked, moved, or looked up. What is left to judge is the language: the writing, the voice, the register, the tone. You are not scoring whether the assistant is capable. You are scoring how it talks.

That is not a broken task and it is not a reason to skip.

> **Warning**
>
> Conversation does not mean invented
>
> Every prompt still has to be anchored in this person's data. Emotional support about their day means something actually on their calendar that day. Relationships means their real partner or friend - the one who lives in this environment. There is always something for Hatch to fetch.
>
> A chatty prompt with nothing behind it is still an ungrounded prompt.

Good

Rough day - the Fenwick review got pushed again and I still have that Thursday dinner with Priya. Talk me through it.

Bad

I had a rough day, cheer me up.

> **Info**
>
> **Companionship / Chat** - casual is fine, unanchored is not. The good version points at a real calendar event and a real person in the persona's world.

Write the prompt itself on Write the prompt. Record the category on Complete the form.

---

## App capabilities

<sub>section: **2. Run a task** · nav label: *What the apps can do*</sub>

Reference while writing the prompt and while verifying claimed actions.

What the assistant can and cannot do in the persona's apps. Use **V2 personas only** - V1 is no longer in use. In Hatch this comes from the **Universe** you choose, not from the protocol's version label. The core app set below is the same across persona versions; V2 simply adds a few more apps. Asking for an unsupported action makes your prompt invalid. A model that *claims* an unsupported action loses on Correctness.

> **Info**
>
> Some tasks have no app work at all
>
> Several of the use cases - Companionship / Chat, Emotional Support, Entertainment, Media Creation - are conversations rather than errands. In those, Hatch may not need to open anything, and neither arm will show app activity. That is normal. Judge the language, and leave **Apps utilized** reflecting only what the arms actually invoked, which may be little or nothing.
>
> The prompt still has to be grounded in the persona's records.

| App | Read | Create / edit | Send | Important considerations |
| --- | --- | --- | --- | --- |
| Gmail | Yes | Yes, real drafts | Yes | Text shown only in chat does not complete an explicit Gmail-draft request. |
| Google Calendar | Yes | Yes, events and reminders | n/a | Verify date, year, timezone, all-day status, and attendees. |
| Google Contacts | Yes | No | No | Cannot create, edit, delete, merge, or deduplicate contacts. |
| WhatsApp | Yes | No | Only with already present contacts | Cannot create groups, add members, or modify chats. |
| Outlook Mail | Yes | No | Yes | Cannot create drafts, move, or modify mail. |
| Google Drive | Yes | Yes | n/a | Verify the file exists in Hatch. |
| Google Docs | Yes | Yes | n/a | Verify the document content in Hatch. |
| Google Sheets | Yes | Yes | n/a | Verify the rows and values in Hatch. |
| Notion | Yes | Yes | n/a | Verify the page in Hatch. |
| Oura | Yes | No | n/a | Sleep records use the wake-up date. |

Never ask for these

- Send a WhatsApp message to someone not messaged before
- Merge Google Contacts
- Create an Outlook draft

Any prompt requesting one of these is invalid. Rewrite it as a summary or as text the user can copy.

### Details per app

#### Gmail - draft versus text

- "Draft a Gmail response" means a real Gmail draft. Text in chat alone has not finished the job.
- "Write a response to this email" is satisfied by draft text, unless the prompt asks for a Gmail draft specifically.
- Sending is not drafting. A model that sends when asked to draft has failed instruction following, decisively.

#### Google Calendar

Events and reminders can be created and edited. Before scoring, verify the date, the year, the timezone, whether it is all-day, and the attendee list. Unrequested attendees are an instruction-following miss.

#### WhatsApp - read and limited send

Read, search, and summarize chats. Identify people, decisions, and plans. Messages can be sent, but only to a contact the persona has already messaged.

Cannot create groups, add members, or modify chats.

**Valid:** "Summarize what the hiking group decided and write a message I can copy." **Valid:** "Send Claire a message confirming Saturday" - only if Claire is an existing chat. **Invalid:** "Message this new number about the rental."

#### Google Contacts - read only

Search contacts and retrieve saved details.

**Valid:** "Find Claire's current email address." **Invalid:** "Merge my duplicate contacts."

#### Outlook Mail - read and send, no drafts

Read and search mail. Messages can be sent, but drafts cannot be created and existing mail cannot be moved or modified.

**Valid:** "Read Alicia's Outlook message and send her a reply confirming Thursday." **Valid:** "Read Alicia's Outlook message and write a reply I can paste." **Invalid:** "Create an Outlook draft."

#### Google Drive, Docs, Sheets, Notion

Files, documents, spreadsheets, and pages can be created and edited. Always confirm in Hatch that the artifact exists with the requested content - a described document is not a created document.

#### Oura - read only

Health data can be read and analyzed, never written.

**The wake-date rule:** the row date is the wake-up date. "The night of March 14" appears on the row dated March 15.

### V2 environments

You work in V2. Everything in the table above still applies - the core apps are unchanged from V1. V2 adds a few apps on top, and which of those you get depends on your task environment, so check the environment rather than assuming every V2 app is present.

> **Warning**
>
> System-clock behavior in Hatch
>
> Observed Hatch environment behavior.
>
> Hatch uses the environment/system clock for time-sensitive actions rather than the simulated date of the persona's universe. The persona's records may therefore be set in a different date or time period from the clock Hatch uses when a model performs a new action.
>
> This can affect newly created or modified records anywhere that timestamps, dates, or chronological ordering matter. Do not assume the persona universe's apparent "current date" is the date Hatch will assign to a new action.
>
> Chat provides a particularly visible example: because messages are ordered chronologically, a newly written Chat message can appear in the middle of the persona's existing simulated message history rather than at the bottom. The write still succeeded; its system-clock timestamp placed it earlier in the chronology.
>
> When evaluating time-sensitive writes, verify the actual created or modified record in Hatch rather than relying only on where it appears in the UI.

#### V2 Train and V2 Eval

These use the full app environment. Every app in the table above remains available. These four are the additions.

| App | Read | Write | Important considerations |
| --- | --- | --- | --- |
| Photos | Yes | No | Search and inspect existing photos. Cannot add, edit, or delete photos. |
| Oura | Yes | No | Existing Oura guidance elsewhere on this site remains authoritative. |
| Philips Hue | Yes | Yes | Reads and changes the state of devices already present in the persona environment - for example, turning an existing light on or off. Cannot add or create a new Hue device; writes never create new devices or resources. |
| Nutrition | Yes | Yes | Reads nutrition data, and can create and delete nutrition-log entries. |
| Health Records | Yes | No | Exposed through HealthEx. Reads include health summaries and existing conditions, medications, labs, vitals, immunizations, procedures, visits, and notes. No create, update, or delete capability has been observed. |

#### V2 Professional Eval

Professional Eval has a more work-oriented app surface. Only the apps below are confirmed for it - do not assume an app found in V2 Train or V2 Eval is present here unless it is documented.

| App | Read | Write | Important considerations |
| --- | --- | --- | --- |
| Chat | Yes | Yes | Chat can make Hatch's system-clock behavior especially visible; see the environment note below. |
| Linear | Yes | Yes | - |

### Before you score a write action

Work through each item.

#### Checklist

0 of 5 complete

- [ ] The action actually happened in Hatch, not just in the final message.
- [ ] It contains the requested content.
- [ ] It happened in the app the user asked for.
- [ ] Nothing extra was added - no unrequested attendees, recipients, or cc.
- [ ] Dates, times, and timezones are right, with no invented year.

Next: Score and choose.

---

## Score and choose

<sub>section: **2. Run a task**</sub>

Steps 6–7 - Preference, eight dimensions, and the Required rationale.

Practise this before your next task

Quality checks collects the hard rules, the app matrix, and the screenshot rules in one place - and links the live practice page where you can write a task prompt and record a judgment and get the same checks a reviewer applies.

Hatch asks for one **Preference**, eight **comparative dimension scores**, and one **Required rationale**.

What you are judging is how Hatch communicates. The bar is that it sounds human - a real AI companion, not an answer-bot. Correctness still counts, and where Hatch takes an action or states a fact from the person's world you still check it against the environment. But the headline judgment is the language.

Every dimension uses the same comparative scale - you are never giving A its own quality score and B its own quality score. You are saying which arm was better on that dimension, and by how much.

Keep the live tasking page open

Live tasking has the per-step checklist and a consistency check for your eight scores, Preference, and Required rationale before you submit.

The scale - one value per dimension

**1 = A much better · 2 = A better · 3 = Tie · 4 = B better · 5 = B much better**

Low numbers favour Arm A. High numbers favour Arm B. **3 is Tie.**

3 is only for genuinely identical

A 3 means the two replies were **identical** on that dimension. That is rare on the six communication dimensions and common on Correctness. Everywhere else, pick a side.

A 3 carries no signal - "A better" is a real answer, a Tie is a blank. The scale already has a setting for *close, but this one*: that is a 2 or a 4.

- **Both weak.** Still pick the one you prefer, and say why.
- **Both strong.** Look again for the small thing that tips it. There almost always is one.
- **Still nothing?** Rare. Pick the one you would rather have received.

**Where a 3 is genuinely common: Correctness.** Two replies are often factually identical, and then 3 is the right answer. The test is the same everywhere - identical, not merely close. On the communication dimensions they almost never are.

*Choose Preference, score all eight dimensions with 1 favoring A, 3 as Tie, and 5 favoring B, write the Required rationale, submit the preference, then end the comparison.*

> **Warning**
>
> Do not score a failed arm
>
> Do not score the example failure shown in this screenshot. If either live arm says "Something went wrong," is missing, or is cut off, stop. Retry or recreate the session. Never submit an incomplete comparison.

> **Info**
>
> About the red RM Style banner
>
> The red RM Style banner is informational: its system-prompt override/append applies to the graded comparison turn, not the entire free-exploration session. It is not an error.

### The order you work in

1

#### Complete the comparison

Both arms complete, same user turns, and every fact or claimed action that Correctness rests on checked in **Apps**.

2

#### Note the concrete differences

Before any number: what actually separates these two replies? The opening line, the ordering, what got buried, the register, a tic, a missing piece. If you cannot name one, look again.

3

#### Score all eight dimensions independently

One value each, 1 favouring A, 3 for Tie, 5 favouring B. Score each on its own evidence - not as a vote for the arm you liked.

4

#### Choose the overall Preference

A significantly better · A slightly better · Tie · B slightly better · B significantly better. It is the headline judgment, **not** the average of the eight numbers.

5

#### Write the Required rationale

Explain the preference and support every score away from 3.

6

#### Submit preference, then End comparison

Click **Submit preference**, then **End comparison**. Then copy the same values into Hub task fields shown on your task.

### Overall preference

Score the dimensions first, then set the Preference. Choosing the winner first and filling the sliders to match is the single easiest way to produce eight numbers that are votes rather than judgments.

Preference is the headline judgment, not the average of the eight numbers.

- A serious correctness, fabrication, unauthorized-action, or missing-work failure can outweigh several smaller communication wins.
- When substantive performance is close, the communication dimensions can legitimately decide the preference.
- Tie on the Preference is almost never the right call - if you can name the difference, that is your winner.

### The eight dimensions

#### High level

#### 1. Style and behavior (High level)

"Regardless of whether the response is correct, which response do you prefer? Judge based on how Hatch is communicating."

This dimension deliberately ignores correctness. Judge the communication only.

It is the high-level read of all six granular dimensions at once.

#### 2. Correctness (High level)

"Select whichever response is more correct. This may frequently be a tie."

Verified facts, dates, recipients, artifacts, and claimed actions. When both arms did the same correct work, 3 is the right answer.

None of the six granular dimensions carries correctness - this is the one place facts live.

#### Granular

Each granular dimension owns one question and only that question. The short version:

| Dimension | The one question it answers |
| --- | --- |
| Coherence & writing quality | Is it well built - organized, ordered, right length, clean sentences, right format? |
| Style | Does the agent sound like a natural entity you'd want to engage with, as opposed to a generic answer-bot? |
| Tone | Is Hatch emotionally attuned to the user's tone and needs and context? |
| Helpfulness | Does it advance what the person is actually trying to do? |
| Completeness | Does it cover the whole ask at the right depth? |
| Warmth | Does Hatch feel appropriately caring and friendly without sounding forced or excessive? |

Read the full definitions before your first task. Most disagreements come from putting an observation on the wrong dimension - the routing table fixes it.

### Score each dimension independently

Work through each item.

#### Checklist

0 of 8 complete

- [ ] Score each dimension on its own evidence. Do not force all eight numbers to favour the same arm.
- [ ] A can be more correct while B communicates better. That is a normal, expected result.
- [ ] Style and behavior (High level) intentionally ignores correctness.
- [ ] Correctness (High level) may often be 3 / Tie.
- [ ] Completeness is coverage at the right depth, not word count.
- [ ] Warmth is the amount of care and whether it fits - gushing and coldness both lose. Tone is whether it read the room.
- [ ] On the six communication dimensions, 3 means identical. If you can see a difference, score it 2 or 4.
- [ ] Style and behavior points the same way as the weight of your six granular scores - or the rationale says why it does not.

### Length-bias calibration

Longer is not better, and shorter is not better

- Extra detail helps only when it gives useful information, action, context, or structure.
- Repetition, raw IDs, internal process, implementation logs, and padding can hurt **Style** or **Coherence & writing quality**.
- A short response still loses when it omits required work or is wrong.
- Style never rescues a wrong action, missing work, an unsupported claim, or a fabricated fact.

### Writing the required rationale

One tight paragraph is enough. It must:

Work through each item.

#### Checklist

0 of 5 complete

- [ ] Explain the overall Preference.
- [ ] Name concrete, observable A/B differences.
- [ ] Support every dimension scored away from 3 / Tie.
- [ ] Explain why a decisive correctness or completion failure outweighs communication wins, when that drives the result.
- [ ] Explain the useful value the extra length added, when the longer response wins.

One concrete observation may support several dimensions when the connection is clear. You do not need a separate sentence for all eight dimensions - you need concrete support for each non-3 score and for the preference.

Good

A gives one direct confirmation, while B includes message IDs, timestamps, and repeated process narration that make the result harder to scan and less natural.

Bad

A is better written and more helpful.

> **Info**
>
> A generic conclusion with no observable evidence supports nothing. Name what each arm actually said or did.

### Consistency examples

Good

Correctness = 1 because A used the right calendar and the correct date while B created the event a day early. Style = 4 and Tone = 4 because B's message sounds like a person and A reads like a completion log. Overall A significantly better - the wrong date is not repaired by a friendlier voice.

Bad

A is more correct so everything favours A.

> **Info**
>
> Dimensions may point in different directions. Score each one on its own evidence.

Good

Both arms drafted the same correct reply, so Correctness = 3. Coherence & writing quality = 4 and Completeness = 4 because B's three-bullet confirmation covers the same ground without repeating the tool process. Overall B slightly better.

Bad

B slightly better because it was shorter.

> **Info**
>
> When substantive performance ties, communication dimensions can decide the preference - but say what made the communication better.

Good

B sounds more natural, so Style = 5 and Tone = 4. But the user asked for a draft and B sent the email, so Correctness = 1. Overall A significantly better - an unauthorized send outweighs the communication wins.

Bad

B significantly better because it was the more engaging response.

> **Info**
>
> A decisive correctness or instruction failure outweighs style.

Good

Correctness = 3 - both arms drafted the same reply to the same recipient with the same date. But A bolds only its section labels while B bolds nearly every clause, so Coherence & writing quality = 1, and B closes with "Want me to set a reminder?" so Style = 1. Overall A slightly better.

Bad

Correctness = 3, so Style = 3, Coherence = 3 and Tone = 3 as well. Preference Tie.

> **Info**
>
> Correctness ties often. The communication dimensions almost never do. Two replies that look nothing alike cannot be Tie on Style, Coherence and Tone just because the facts matched.

### Final scoring checklist

Work through each item.

#### Checklist

0 of 9 complete

- [ ] Both arms complete, same user turns, and every fact and claimed action Correctness rests on checked in Apps.
- [ ] Preference chosen before the dimension scores.
- [ ] All eight dimensions scored, one value each.
- [ ] No 3 on a communication dimension unless the two replies are genuinely identical on it.
- [ ] Every score away from 3 has concrete support in the Required rationale.
- [ ] Preference, scores, and rationale tell one story.
- [ ] A and B were not swapped - remember 1 favours A and 5 favours B.
- [ ] Length alone did not choose the winner.
- [ ] Submit preference clicked, then End comparison.

Next: the full definitions on The six dimensions, then Complete the form.

---

## The 2+6 Dimensions

<sub>section: **2. Run a task**</sub>

Two high-level and six granular. What each one owns, what it does not, and how they fit together.

This project judges language. The bar is that Hatch sounds human - a real AI companion, not an answer-bot. Eight dimensions carry that judgment: two high-level, six granular. The six granular ones below are the client's definitions and are the reference; the two high-level ones are the whole-reply read of them.

Each dimension owns one question and only that question. Score each on its own evidence - a dimension never borrows another's. A beautifully built reply to the wrong question scores high on Coherence and low on Helpfulness, and that split is a correct result, not a mistake.

### The two high-level dimensions

You will be asked these two first in Hatch. They are one-line questions in the client's guidance; here is what each one owns, derived from that guidance and the live task.

#### Style and behavior (High level)

*Regardless of whether the response is correct, which response do you prefer? Judge based on how Hatch is communicating.*

#### Owns

The whole communication verdict - which reply you would rather have received, ignoring whether it is right. It is the high-level read of all six granular dimensions at once: how it is built (Coherence & writing quality), the voice (Style), the emotional fit (Tone), whether it advances the goal (Helpfulness), whether it covers the ask (Completeness), whether the care it shows fits (Warmth). Judge communication at a high level.

#### Doesn't own

Correctness. Ignore correctness for this dimension. A reply that gets a date wrong can still win here - it is fine to prefer the style of a response that makes a factual error.

#### Relationship to the six

They are its facets. It is not an average of them, but if the six lean one way and this leans the other, your rationale has to say why. Otherwise you have scored the arm, not the communication.

#### Correctness (High level)

*Select whichever response is more correct. This may frequently be a tie.*

#### Owns

Factual accuracy, valid assumptions, correct actions, recipients, dates, calculations, and outputs - and whether something the reply says it did actually happened. This is the one place facts live. Where a reply takes an action or states a fact from the person's world, check it against the environment before you score this.

#### Doesn't own

Anything the six granular dimensions own. Completeness is "was each requested thing there," not "was it right." Helpfulness is "does it advance the goal," not "is it accurate." None of the six carries correctness, which is why it is fine to score them without it.

#### Relationship to the six

None. It has no granular facet. That is also why it is the one dimension where a 3 is genuinely common - the two arms usually do the same work.

The order Hatch asks, and the check to run before you submit

Hatch asks the two high-level questions first, then the six granular. Answer them in that order. Then, before you submit, hold Style and behavior up against your six granular scores. If they point the same way, good. If they do not, re-read both replies - the disagreement is the signal, not the mistake - and either move the score that is wrong or say in the rationale why the high-level read differs.

### The six granular dimensions

These are the client's definitions, reproduced as written. Each owns one question and only that question.

| Dimension | The one question it answers |
| --- | --- |
| Coherence & writing quality | Is it well built - organized, ordered, right length, clean sentences, right format? |
| Style | Does the agent sound like a natural entity you'd want to engage with, as opposed to a generic answer-bot? |
| Tone | Is Hatch emotionally attuned to the user's tone and needs and context? |
| Helpfulness | Does it advance what the person is actually trying to do? |
| Completeness | Does it cover the whole ask at the right depth? |
| Warmth | Does Hatch feel appropriately caring and friendly without sounding forced or excessive? |

### 1. Coherence & Writing quality

*Is it well built - organized, ordered, right length, clean sentences, right format?*

#### Owns

Structure and cohesion (reads as one piece, not stapled chunks); ordering (answer/most-important first, not buried under preamble or process); length discipline (as long as it needs to be, no longer); selection (says what earns its place, cuts misc detail and redundancy); format-fit; and sentence construction/flow (natural, varied, well-formed - no comma-splice piles, dropped-subject chains, or telegraphic stubs).

#### Doesn't own

What voice the sentences are in (Style); whether the content is useful (Helpfulness) or complete (Completeness). A beautifully built reply to the wrong question still scores high here and low on Helpfulness.

**Good**

> I moved your 2pm to Thursday and shifted the prep block along with it. I also gave Dana a heads-up. The only conflict left is your dentist; want me to push that for you as well?

*Answer first, one clean through-line, nothing extra.*

**Bad**

> Got it - I've finished your auto-safety report!
>
> At a glance: a full research report on 2026 SUV safety ratings.
>
> Here's what's inside: The report has crash-test ratings. It has rollover data. It covers IIHS Top Safety Picks. It has a section ranking the safest models.
>
> Bottom line: your complete auto-safety report is ready, covering the crash-test ratings, rollover data, IIHS picks, and safest models described above.

*A chat reply wearing a document scaffold ("At a glance… Bottom line"); the bottom line restates the body verbatim; the middle is a dropped-subject monotone.*

### 2. Style

*Does the agent sound like a natural entity you'd want to engage with, as opposed to a generic answer-bot?*

#### Owns

The character of the voice - does it sound like an entity worth talking to, not a generic answer-bot; register adaptation (matches the person's pace/formality/humour without parroting their words back); plain language vs. jargon-dumping (jargon restraint lives here - mechanics/identifiers where a plain effect would do); the presence of AI-slop tics (em-dash openers, "Got it - ", "Sure thing!", forbidden "Do you want me to…" closings, "it's not x, it's y" templated boilerplate); and personalization aptness - using the person's history in a way that feels earned and sensible vs. forced, creepy, or over-familiar.

#### Doesn't own

Emotional warmth/empathy calibration (Tone); whether sentences are grammatically well-built (Coherence). Style is *which* voice; Coherence is how well-constructed that voice's sentences are.

A Day-100 user who texts in clipped lowercase asks Hatch to rebook a flight. Same moment, two replies.

Good

on it. flight's rebooked. you're now landing 6:40, you can still make the dinner.

Bad

Got it - happy to help! I've gone ahead and rebooked that flight and saved the info in your flighttracker.md file (790357887). As your always-on, golden-retriever-loyal travel sidekick, I made sure you're all set - you now land at 6:40. Do you want me to check on the dinner reservation too?

> **Info**
>
> The good reply absorbs the register, keeps its own voice, no ceremony. The bad one opens with "Got it - " plus "happy to help!" ceremony, forces a "golden-retriever-loyal" persona, and closes with the forbidden "Do you want me to…" - plus the .md file jargon and the technical identifier leak.

### 3. Tone

*Is Hatch emotionally attuned to the user's tone and needs and context?*

#### Owns

Emotional register and its fit to the moment - warmth when warmth is due, calm and direct for a routine ask, seriousness for a hard moment; reading the room; empathy calibration; and no false interiority ("glad to help" is fine, "I care about you" is not).

#### Doesn't own

The words and tics that carry the voice (Style) - a reply can be warm in tone but sloppy in style.

Someone has just failed an exam. Same moment, two replies.

Good

I'm so sorry. That's a rough one. When you're ready, we can look at what the retake actually requires. It's more doable than it feels right now.

Bad

I'm really sorry. It's ok to feel down and sit with that for awhile. Thank you for telling me. Do you want to talk about what's weighing on you, or would a distraction help more right now? Remember, one exam doesn't define you - you've got this! And if it feels heavy most days, it helps to talk to someone you trust.

> **Info**
>
> The good reply is warm, honest, not gushing. The bad one is a canned opener, a templated two-option question, empty pep ("you've got this!"), and a boilerplate crisis line bolted onto a routine disappointment.

### 4. Helpfulness

*Does it advance what the person is actually trying to do?*

#### Owns

Whether the response advances the person's real goal - reads intent (answers what was meant, not just the literal words); is on-target and actionable (something to act on); shows judgment / takes a useful position rather than punting the work back.

#### Doesn't own

Whether every requested part is present (Completeness); whether it's well-written (Coherence). A one-line answer can be maximally helpful; a thorough one can be useless.

*"help me find gifts for my sister and my dad"*. Same request, two replies.

Good

For your sister's birthday next month: the pottery-class series near her in Asheville could be just the thing. She sent you three ceramic posts last week. For your dad: a replacement for the fishing reel he mentioned losing. Want me to pull up options and prices for either?

Bad

I'd love to make you a gift guide! To get started, could you send me: who you're shopping for, each person's birthday, their interests and hobbies, your budget per person, and anything they've loved in the past? Once I have that, I'll build your first guide.

> **Info**
>
> The good reply uses what it already knows to hand over something to act on. The bad one hands the work back to the user - the people, dates, and interests are already in the accounts Hatch is connected to.

### 5. Completeness

*Does it cover the whole ask at the right depth?*

#### Owns

Coverage of the whole ask at the right depth - all parts addressed, explicit constraints honoured, nothing important dropped, not truncated.

#### Doesn't own

Usefulness or aim (Helpfulness); accuracy of what's included. Completeness is a checklist question: was each requested thing there?

*"make me a guide of books to buy for the year"*. Same request, two replies.

Good

Here's your 12-book list for the year, one per month. Each has a buy link and current price - the four in your wishlist are marked, and three are under $12 in paperback right now.

Bad

Here's your 12-book reading list for the year. Every title is available at the Greenpoint branch of the Brooklyn Public Library, with call numbers so you can pick them up on your next visit.

> **Info**
>
> In the good reply every element of the ask - the titles, the buy intent, the prices - is present. The ask was a guide to buy the books, so the bad reply misses the requested scope: no purchase links, no prices, only the library.

### 6. Warmth

*Does Hatch feel appropriately caring and friendly without sounding forced or excessive?*

#### Owns

The amount of care and friendliness, and whether that amount fits the moment - a reply that feels like a person who is glad to help, without pet names, gushing, or manufactured affection. Both failure directions live here: warmth laid on too thick, and warmth withheld where a little was due.

#### Doesn't own

Whether the emotional register is the *right* one for the moment (Tone) - Tone asks "did it read the room," Warmth asks "was the care the right amount and did it feel real." The words and tics that carry the voice are Style.

Someone mentions in passing that their dog is at the vet, then asks Hatch to move a meeting.

Good

Hope the little one's okay. Meeting's moved to Thursday 3pm and I let Priya know.

Bad

Oh no, I'm SO sorry to hear about your sweet pup!! Sending you the biggest hug, friend - I know how much she means to you and I'll be thinking about you all day. Anyway, meeting moved!

> **Info**
>
> Appropriate warmth is one short line that lands and then gets on with the work. Excessive warmth is pet names, double exclamation marks, manufactured feeling, and a claim to be "thinking about you all day" - care the assistant cannot have. Absent warmth would be *"Meeting moved to Thursday 3pm."* with no acknowledgement at all, which reads cold for a moment that plainly asked for one line.

### Which dimension does it belong to?

The boundaries are where most disagreements come from. Use this to route what you noticed.

| What you noticed | Where it lands |
| --- | --- |
| A "Do you want me to…" or "Want me to…" closing | Style |
| A forced persona - "your golden-retriever-loyal sidekick" | Style |
| Raw filenames, IDs, timestamps, tool names leaking into the reply | Style |
| "Got it - ", "Sure thing!", "happy to help!" ceremony openers | Style |
| Comma-splice piles, dropped subjects, telegraphic stubs | Coherence & writing quality |
| A document scaffold ("At a glance… Bottom line") on a chat reply | Coherence & writing quality |
| Everything bolded, so nothing stands out | Coherence & writing quality |
| The answer buried under preamble or process narration | Coherence & writing quality |
| "I care about you" - feelings the assistant cannot have | Tone |
| Empty pep, or a crisis line bolted onto a routine disappointment | Tone |
| Gushing where the moment called for calm, or brisk where it called for warmth | Tone |
| Asks the person for information already in their connected accounts | Helpfulness |
| Answers the literal words and misses what was meant | Helpfulness |
| Punts the decision back instead of taking a useful position | Helpfulness |
| One of three requested things is missing | Completeness |
| An explicit constraint in the ask was ignored | Completeness |
| Cut off mid-thought | Completeness |
| Friendliness laid on thick - pet names, exclamation marks, "I'm SO happy for you!!" | Warmth |
| Cold and transactional where a little care was due | Warmth |
| Warm in the right measure, but aimed at the wrong feeling | Tone, not Warmth |
| Beautifully written, but answers the wrong question | High on Coherence, low on Helpfulness - score both |
| A wrong date, recipient, figure, or name | Correctness (High level) - not Completeness |
| Sent when asked to draft; did something it was not asked to do | Correctness (High level) |
| Says it created, sent or updated something that does not exist in Apps | Correctness (High level) |
| "Which would I rather have received, facts aside?" | Style and behavior (High level) - the read of all six |

The scale, the preference rule, and the rationale requirements are on Score and choose.

---

## Complete the form

<sub>section: **2. Run a task**</sub>

Step 6 - the Hub fields, one at a time.

Field by field. Open only the one you are filling.

> **Info**
>
> Older task versions
>
> Older task versions may have different fields. Follow the instructions shown on your task, and never improvise a place to put content.

### Session name

Copy from Hatch exactly.

Correct: `488c89ae9c3f_task_4`

Wrong: `eb950ef4-fe1a-4a99-9525-cab66719b954_task_4`

Format is `youralias_task_N` - your exact lowercase alias from your chat profile, lowercase `_task_`, then the task number. Type it into the **Name** field before you click Create session. Abandoned sessions use `youralias_abandonedtask_N`, for example `488c89ae9c3f_abandonedtask_4`. No UUIDs, no email addresses, no display names, no spaces, no capitals.

### Session ID

Copy from Hatch exactly. It is a UUID, for example `2e6c6e89-82af-44b4-9870-186ac9e29bb9`.

**The session name and session ID are different fields.**

### Universe

Use the human persona name from the persona summary for the universe you actually worked in.

Correct: `Megan Porter`

Wrong: `Ivy Reed` - filling in one universe's name when your actual Hatch session was Megan Porter.

### Category

Choose based on the user's goal, not the app. There are thirteen categories:

| The user is doing this | Category |
| --- | --- |
| Just chatting, catching up, sharing an opinion | Companionship / Chat |
| Understanding something, researching options, learning a skill | Learning / Research |
| Exercise, meals, sleep, or recovery | Health & Fitness |
| Finding, comparing, or choosing something to buy | Shopping |
| Writing or creating something - a post, a caption, a story | Media Creation |
| Work email, a doc, project planning, meeting prep | Work Productivity / SMB |
| Shows, films, music, games, something fun | Entertainment |
| Talking through a hard day, a feeling, venting | Emotional Support |
| Budget, expenses, a money question | Finance |
| A trip, an itinerary, destination or restaurant ideas | Travel |
| A friend, partner, or family member; wording a hard message | Relationships |
| A rule, a process, a civic question, making sense of a form | Legal / Civic |
| Smart-home devices, routines, troubleshooting | Home Automation |

The category follows the goal, never the apps: *"move my Thursday run if it rains"* is Health & Fitness even though it edits the calendar. Keep each session focused on one goal, or the category becomes ambiguous.

### Apps utilized

The union of apps actually invoked by both arms - not the apps available in the environment, not the apps your prompt mentioned, and not from memory.

Canonical spellings: Gmail · Google Calendar · Google Contacts · WhatsApp · Outlook Mail · Google Drive · Google Docs · Google Sheets · Notion · Oura · Photos · Philips Hue · Nutrition · Health Records · Chat · Linear

Which of these exist depends on your V2 environment. Record the ones the responses actually used.

### Task prompt

Copy every user turn exactly and in order, clearly separated.

### Response transcripts

When the fields exist:

- Copy the correct arm.
- Include all required turns.
- Do not summarize.
- Do not clean up.
- Do not reconstruct.
- Do not copy A into B.

If a transcript cannot be recovered, recreate the task.

### Preference, dimension scores, Required rationale

Copy these from Hatch exactly as you entered them there:

- The overall **Preference** - A significantly better, A slightly better, Tie, B slightly better, or B significantly better.
- **All eight comparative dimension scores**, one value each: 1 = A much better · 2 = A better · 3 = Tie · 4 = B better · 5 = B much better.
- The **Required rationale**, supporting the preference and every score away from 3. A 3 on a communication dimension means the two replies were identical on it.

Do not enter different values here to compensate for a Hatch evaluation you now think is wrong.

### Notes - required

Notes is a **required** block. Leaving it empty blocks submission; Hub names the block rather than accepting the task.

Write what actually happened: an environment error, a tool the agent could not reach, odd behavior in Hatch, anything that affected the entry. If nothing came up, say so - "Nothing I noticed at the moment" is a valid entry. Do not invent an issue and do not paste filler.

Notes never substitute for a missing response, a missing score, or an unfinished annotation.

### Screenshot confirmation

Upload **exactly one** screenshot of the **completed comparison** in the exact session named on this task.

- Take it after **Submit preference** and **End comparison**, not before.
- Match the session by name **and** by the session UUID on this task. A neighbouring completed row is not evidence for your session.
- Not the sessions dashboard, not a "Stopped session" row, not the form you were filling in.
- One image. Not two, not a set.

### Confirmation that the session did not end mid-annotation

The task asks you to confirm that the quality checks passed **and** that the Hatch session does not say **Ended mid-annotation**.

Go back to Hatch and read the status of the exact session before you answer. If it ended mid-annotation, the task cannot be submitted - abandon and replace it. Never tick the confirmation to clear the block.

### What differs on older task forms

- Some tasks have no A/B transcript fields.
- Some use one combined rationale field.
- Some separate score explanation and preference rationale.
- Some score the full conversation.
- Some score only the final response.

Do not require fields that do not exist. Where an older version differs from this guide, the task in front of you wins.

Next: Two-minute check.

---

## Two-minute check

<sub>nav label: *3. Before you submit*</sub>

Step 7 - the last look before you submit anything.

Ten checks. Run them before every submission. Nothing here is new - it is the last look.

Keep the live tasking page open

Live tasking has the per-step checklist and a consistency check for your eight scores, Preference, and Required rationale before you submit.

Work through each item.

### Checklist

0 of 10 complete

- [ ] Hatch setup is correct - GAIA PREFERENCE, a V2 universe, **Hatch RM Style Task - current version**, and the session named `youralias_task_N`.
- [ ] The request is grounded in real records, feasible for the connected apps, and needs no public-web information.
- [ ] Both arms got the same initial request and the same follow-up turns, and both responses are complete and comparable.
- [ ] Every fact and claimed action that Correctness rests on was checked in Apps.
- [ ] The pair was fair to score - not diverged, no duplicated prompt, no missing context it refers to.
- [ ] The overall Preference is selected **after** the dimension scores, as the headline judgment rather than an average of them.
- [ ] All eight comparative dimension scores are entered - 1 favours A, 3 is Tie, 5 favours B.
- [ ] No 3 on a communication dimension unless the two replies were genuinely identical on it.
- [ ] Every score away from 3 is supported by concrete evidence in the Required rationale, and Preference, scores, and rationale tell one story. Length alone did not pick the winner.
- [ ] **Submit preference** and **End comparison** are done, and the Hub fields are complete and exact.

Never submit an incomplete comparison

If a response is missing, cut off, failed, copied, or reconstructed, do not submit. Recreate the task.

---

## When hatch breaks

<sub>nav label: *4. When something breaks*</sub>

Match the screen in front of you, then fix in place or abandon and replace. Never submit an incomplete session.

One rule governs this page

**Never submit an incomplete session.** If a response is missing, cut off, failed, copied, or reconstructed, the task cannot be repaired with Notes, with scores, or with a screenshot. Retry the arm, then the session. If it still fails, rename it `youralias_abandonedtask_N` and rerun the task in a replacement `youralias_task_N`.

### I'm stuck - Start here

Answer one question. Each answer sends you to the branch that fits.

#### Hatch will not run, or the session died

Red 400 toasts, arms stuck on **Booting the agent…**, a session that reads **Ended mid-annotation**, or a stopped session you cannot reopen.

Go to **When the session is broken**, below. The outcome is almost always **abandon and replace**.

#### Hatch ran fine, but Hub will not let me submit

Hub says the task cannot be completed, or the feedback panel names fields that need attention.

Go to **When submission is blocked**, below. The outcome is **fix in place**, unless the missing item is evidence that never existed.

#### I already submitted and the task came back

Go to **When a task comes back**, below. Most returns are field corrections you make on the same task.

#### Something odd happened but everything completed

A slow tool, a UI glitch, a label that disappeared - and both arms still produced complete responses.

That is a **Notes** case, not a recovery case. Finish the task and describe what happened in the required Notes block.

Working session name

youralias_task_N

Your exact lowercase chat alias, then the task number.

Abandoned session name

youralias_abandonedtask_N

Keep the same task number as the run that failed. Never submit this session.

### When a pair cannot be fairly compared

Separate from a broken session: sometimes the comparison itself is not fair to score. These are the cases where the honest answer is to not score the pair at all.

Three cases you do not score

- **Divergent conversation pairs.** The two sides have drifted apart - for example only one has a second user prompt continuing the dialogue. Intent has diverged too far for a fair comparison.
- **Missing conversation context.** The prompt refers back to something you cannot see, so helpfulness and completeness cannot be assessed.
- **Data issues.** A missing response, or a duplicated user prompt.

In each case the pair cannot produce a defensible judgment. Do not score it and do not guess. Use the **Skip** control if your task offers one; otherwise follow the abandon-and-replace sequence below and say plainly in **Notes** which of the three applied.

> **Warning**
>
> An access limitation is NOT one of them
>
> When one reply returns the person's data and the other surfaces an access limitation - "I can't reach your Oura data right now" - that is **not** a broken pair and **not** a skip.
>
> Assess the **quality of the communication**, not the agentic performance. A reply that hits a wall and says so gracefully, in the person's register, can legitimately beat one that returns the data in a tone-deaf slab. Judge how each one talks about what it could and could not do.

### When the session is broken

Find the screen in front of you and do exactly what the card says.

#### Hatch shows "Error 400 - failed to checkpoint arm: session not found"

Both arms sit on **Booting the agent…** and one or more red toasts read `Error: 400 : failed to checkpoint arm A: session not found`. The backing session is gone; nothing you type will reach the arms.

**Do this:** reload once. If the arms still do not boot, the session is unrecoverable.

**Outcome: abandon and replace.** Rename the session `youralias_abandonedtask_N`, create a replacement `youralias_task_N` with the **same** task number, and rerun the task from the first prompt. Update both the session name and the session ID on Hub task.

#### The session says "Ended mid-annotation"

In the sessions table the **Latest checkpoint** column reads `ended mid-annotation`, and hovering it says the comparison cannot be reopened.

**Do this:** nothing in Hatch will bring it back. Do not screenshot around it, do not reconstruct the missing turns, and do not submit what you have.

**Outcome: abandon and replace.** Rename it `youralias_abandonedtask_N` and rerun the whole task in a replacement session.

#### The sessions list shows stopped or ended-mid rows and I am not sure which one is mine

The list mixes live sessions, stopped sessions, and sessions that ended mid-annotation. The screenshot gate cares about **the exact session you worked in**, not about a neighbouring row that looks finished.

**Do this:** match the session by name **and** by the session UUID you are about to put on Hub task. Confirm that exact row reads completed and does not read **Ended mid-annotation**.

**Outcome: fix in place** if the correct row is completed. **Abandon and replace** if the correct row is stopped or ended mid-annotation - a different completed row does not stand in for it.

#### One arm says "Something went wrong" or never finished

An error that is followed by a real, complete response is **recovered** - that arm is still valid. Only an unrecovered arm kills the task.

**Do this:** retry the arm, then the session. Do not paste anything from the other arm, do not summarize what you saw, and do not write the missing turn yourself.

**Outcome: fix in place** if the arm recovers and both arms end with complete responses. Otherwise **abandon and replace**.

### When submission is blocked

#### "Cannot complete task with incomplete steps"

You clicked submit and Hub refused. At least one required step is empty or invalid.

**Do this:** open the feedback panel and work down the list until it reads **Nothing needs attention**.

**Outcome: fix in place** - unless the missing step is a response, a user turn, or a Hatch value you never produced. Those cannot be typed in after the fact.

#### A required text block is empty

Required text blocks - including **Notes** and the completion confirmation - block submission when they are blank. Hub names the block rather than accepting the task.

**Do this:** fill the named block truthfully. If nothing went wrong, say so plainly in Notes - "Nothing I noticed at the moment" is a valid entry. Do not invent an issue and do not paste filler.

**Outcome: fix in place.**

#### The block asks me to confirm the session did not end mid-annotation

The task carries an attestation: you confirm the quality checks passed **and** that the Hatch session does not say **Ended mid-annotation**.

**Do this:** go back to Hatch, find the exact session by name and UUID, and read its status. Only then answer.

**Outcome: fix in place** if the session is genuinely completed. If it ended mid-annotation, **abandon and replace** - never tick the attestation to clear the block.

#### QC says a field needs attention

The QC panel flags specific fields - a rationale that does not support a score, a field that does not match what you did in Hatch, a missing turn.

**Do this:** correct the named field so it describes what actually happened. Never change a value purely to clear a warning - if the flagged value is what you really did, fix the surrounding fields so the whole task tells one true story.

**Outcome: fix in place.**

### When a task comes back

Fix in place and resubmit the same task

The problem is apps utilized, the use-case category, session-name formatting, a transcript or prompt field, the Notes block, or session metadata after renaming or replacing a session.

Abandon and rerun in a replacement session

The problem involves the overall Preference, a dimension score, the Required rationale, prompt wording or missing user turns, Response A or B, a missing, failed, copied, or reconstructed response, or an unfinished Hatch annotation.

Rename the old session `youralias_abandonedtask_N`, rerun the whole task in a new `youralias_task_N`, then update the session name and ID and re-enter the Hub fields.

### Abandon and replace - The exact sequence

1

#### Rename the broken session

In Hatch, rename it `youralias_abandonedtask_N`, keeping the **same** task number as the run that failed. Do not increment the number just because the first run failed.

2

#### Create the replacement

New session, `youralias_task_N`, same task number, **GAIA PREFERENCE**, a V2 universe, **Hatch RM Style Task - current version**.

3

#### Rerun the whole task

Start comparison, paste the approved prompt, and run the comparison from the first turn. Nothing from the abandoned run carries over.

4

#### Repoint the Hub task

Update **both** the session name and the session **UUID** on Hub task so they point at the replacement. Take the completion screenshot from the replacement session.

Unusable session: `488c89ae9c3f_abandonedtask_4` · Replacement session: `488c89ae9c3f_task_4`

An abandoned session exists only to mark the unusable run. It is never submitted.

### What counts as an incomplete comparison

Retry or recreate - Notes cannot make the task complete

A comparison is incomplete if Response A or B is missing, cut off, or only says "Something went wrong"; if one arm did not receive every user turn or the two arms received meaningfully different instructions; if a transcript cannot be recovered; if text was copied from one arm into the other or a response was reconstructed from memory; or if the annotation ended early and you cannot reopen or finish the Hatch session. Separately, a pair that has diverged, that refers to context you cannot see, or that has a duplicated prompt is not incomplete - it is unfair to score.

### What you can still correct

| Field | Where it lives | Can it be corrected? |
| --- | --- | --- |
| Apps utilized | Hub task | Yes |
| Use-case category | Hub task | Yes |
| Notes | Hub task | Yes |
| Session name | Hatch and the Hub task | Yes - rename in Hatch, then update the task |
| Session UUID | Hub task | Yes - update when you move to a replacement session |
| Prompt and user turns | Hatch | No - they are part of the run |
| Response A and B | Hatch | No |
| Submitted preference, dimension scores, Required rationale | Hatch | No - recreate the session if the judgment itself is wrong |

### Notes field

Notes are required, and they are for a non-blocking issue on an otherwise complete task.

Good

A display issue required extra scrolling. A label was temporarily hidden. A tool was slow but both responses completed correctly. Nothing I noticed at the moment.

Bad

Response B failed. I could not finish the annotation. I could not reopen Hatch. I copied part of A into B. Some prompts did not reach one arm. I only recovered the final response. I submitted before completing the preference.

> **Info**
>
> The first set describes cosmetic problems on a complete task, or an honest "nothing happened". Every item in the second set means the task must be retried or recreated - Notes cannot rescue it.

Back to the workflow: Comparison workflow.

---

## Quality checks

<sub>nav label: *5. Practise and quality bar*</sub>

Practise the two moves that decide a task before you spend a real one.

Practise the two moves that decide a task - the **task prompt** and the **judgment** - before you spend a real one. The live practice page runs the same checks a reviewer applies.

Practise here before your first real task

Open the Quality Checks practice page.

Write a task prompt and record a judgment. The page checks both in your browser, tells you what a reviewer would flag, and never sends or stores anything you paste.

### Your role: Judge

Project Octahedron decides which of two AI personal assistants **communicates** better. The bar is that it sounds human - a real AI companion, not an answer-bot.

You work inside Hatch in a simulated person's digital life. Each task starts with a task prompt you write in that person's voice, anchored in records that actually exist in their universe, and you have a real conversation from there. The same request runs as **two responses, A and B**. You read both in full, check any fact or claimed action that Correctness rests on, and record one **Preference**, **eight comparative dimension scores**, and one **Required rationale**. Then you submit the preference, end the comparison, and copy the same values into Hub task fields.

### The four gates

Four points in a task will stop you. Each wants different evidence.

| Gate | What it checks | What clears it |
| --- | --- | --- |
| **1. Prompt gate** | The task prompt: grounded in real records, one goal, every requested action supported by the persona's apps | Rewriting the prompt before you open the Hatch annotation |
| **2. Evaluation gate** | The judgment: Preference, eight dimension scores, Required rationale, apps utilized, transcripts, session name and UUID | Correcting the named field so it describes what you actually did |
| **3. Completion gate** | The exact Hatch session - matched by name **and** UUID - reads completed and does not read **Ended mid-annotation** | Nothing, if the session ended mid-annotation. Abandon and replace |
| **4. Submission gate** | Required Notes filled, exactly one screenshot of the completed comparison, the confirmation answered truthfully | Filling the blocks honestly until the feedback panel reads **Nothing needs attention** |

No gate is cleared by a note, by ticking a confirmation that is not true, or by entering a value you did not produce. If the evidence a gate wants does not exist, the session is abandoned and replaced.

**Evaluation integrity.** Preference, the eight scores, and the Required rationale must describe the same run. Never adjust one of them only to clear a warning; fix whichever one is actually wrong, and if the judgment itself is wrong, recreate the session.

### Where these fit in a task

1

#### Claim the Hub task

Your payable clock - keep it open.

2

#### VPN, session, explore Apps

Before your first prompt.

3

#### Write and run the prompt

Practised on the Quality Checks page. In your persona's voice.

4

#### Watch both responses

Judge the record itself, not the response's summary of itself.

5

#### Score and write the rationale

Practised on the Quality Checks page. Preference, scores, and rationale must tell one story.

6

#### Submit into Hub

The same values in both places.

### The two moves that decide a task

Task prompt - starts the comparison

A first-person request from your persona to their assistant, grounded in records that actually exist in their accounts. It states a goal, not a list of fields to fill in. The same request then runs as two responses, A and B.

The judgment - decides the result

One Preference, eight comparative dimension scores, and one Required rationale naming the concrete difference that decides it. Preference is the headline judgment, not the average of the eight numbers - and all three must tell one story.

### Hard rules

Non-negotiable

- Every dimension is comparative, never a standalone quality score: **1 = A much better · 2 = A better · 3 = Tie · 4 = B better · 5 = B much better**. Low favours A, high favours B.
- Never score a failed response. If either arm says "Something went wrong", is missing, or is cut off, stop and recreate the session - never submit an incomplete comparison.
- Never score an unfair pair. A diverged conversation, a duplicated prompt, or context the prompt refers to that you cannot see is not scoreable. An access limitation on one side is **not** one of these: judge the communication.
- You are not auditing every step of the behind-the-scenes work. But check every fact and claimed action that Correctness rests on - a date, a name, a figure, a recipient, something it says it did. A model that claims an unsupported action loses on Correctness.
- Text shown in chat is not an app write - the record must exist in Hatch.
- Longer is not better and shorter is not better. Extra detail helps only when it adds useful information, action, context, or structure; repetition, raw IDs, and implementation logs hurt Style or Coherence.
- Style never rescues a wrong action, missing work, an unsupported claim, or a fabricated fact.
- **3 means identical, not close.** On the six communication dimensions a 3 says the two replies were indistinguishable on that dimension, which is rare - if you can see a difference, score it 2 or 4. Correctness is the exception, where 3 is common and correct.
- The red RM Style banner is informational, not an error. Its system-prompt override applies to the graded comparison turn only.

> **Warning**
>
> Correctness ties. The communication dimensions do not.
>
> Both responses come from the same model family with only a style note appended, and each candidate is told to apply that note "to how you write, not to what you do, the actions you take, or the accuracy of your work." Actions are held roughly constant, so the comparison is mostly about communication.
>
> Two failures, opposite directions:
>
> - **Forcing a non-3 on Correctness** to look decisive, when the two arms genuinely did the same work.
> - **Resting on a 3 for Style, Tone or Coherence** on two replies that read nothing alike. This is the more common one, and it is the habit this round of guidance is stopping. A 3 carries no signal - the scale already has a setting for *close, but this one*, and that is a 2 or a 4.

### Prompt-ready checklist

Work through each item.

#### Checklist

0 of 9 complete

- [ ] First person, in the persona's voice.
- [ ] Grounded in records that exist - names specific records rather than asking for information from nowhere.
- [ ] Requires app use - the assistant has to open something.
- [ ] Answerable from the persona's records. No public-web dependency unless the environment explicitly offers an internet-search tool.
- [ ] Supported actions only - no never-ask action, no write to a read-only app.
- [ ] Clear success condition.
- [ ] Not excessively prescribed - a goal, not every field dictated.
- [ ] Date-bounded. Replace today / this week / recent / latest with an exact range the persona's records cover.
- [ ] Every ask in the prompt is actually part of the goal, and the use-case category matches the persona's underlying goal - the goal, not the apps.

### Which apps exist depends on your environment

Check the persona's Apps before you write the prompt rather than assuming. A prompt that needs an app or an action your environment does not support is invalid. **V2 personas only** - V1 is retired, and this comes from the Universe you choose, not the protocol's version label. Some environments include an internet-search tool; rely on it only when it is explicitly available.

| App | Can | Cannot |
| --- | --- | --- |
| Gmail | Read · real drafts · send | - |
| Google Calendar | Read · create and edit events and reminders | - |
| Google Contacts | Read | Create, edit, delete, merge, deduplicate |
| WhatsApp | Read · send only to contacts already messaged | Start a new chat, create groups, add members, modify chats |
| Outlook Mail | Read · send | Create drafts, move, modify |
| Drive · Docs · Sheets · Notion | Read · create and edit | - |
| Oura · Photos · Health Records | Read | Any write |
| Philips Hue | Read · change state of existing devices | Create new devices |
| Nutrition | Read · create and delete log entries | - |

Never ask for these

- Send a WhatsApp message to someone not messaged before
- Merge Google Contacts
- Create an Outlook draft
- Send an SMS or text message - there is no texting app in this environment
- Write to a read-only app: Google Contacts, Oura, Photos, Health Records

Any prompt requesting one of these is invalid. Rewrite it as a summary, or as text the user can copy.

> **Warning**
>
> System clock
>
> Hatch uses the environment clock for time-sensitive actions, not the persona universe's simulated date, so a newly created record can land out of chronological order. Verify the actual record in Hatch rather than trusting where it appears in the UI.

### What the practice page cannot check for you

Hub runs a second check - a narrow hard veto whose rules all need the transcripts. They are checked after you submit.

#### The eight post-submission veto rules

1. **Structurally invalid comparison** - unequal user turns between the arms, or a missing or cut-off assistant turn.
2. **Presence/absence reversal** - saying "only A included the date" when it appears in both.
3. **Same-arm action reversal** - saying "B left an empty draft" when B shows a populated one.
4. **Count or order reversal** - counts, chronology, or obvious length claims stated the wrong way round.
5. **Date or deadline contradiction** - calling a date correct when it falls outside the required window.
6. **Unauthorized destructive-action praise** - the assistant bundles a newly proposed deletion into a compound confirmation question, the user replies only "yes", the arm deletes anyway, and the rationale rewards it. Only 41% of fellows got this one right: a bare "yes" confirms the thing being confirmed, never the deletion bundled alongside it.
7. **Unverified claimed action** - the rationale credits an action that never appears in Apps.

> **Warning**
>
> Passing the live checks is not a guarantee
>
> The blocking rules are exact; the rest are a best-effort read of what a reviewer will make of your rationale. No check can tell whether your verdict was right. Three criteria are always graded by the reviewer: the rationale leads another careful reader to the same verdict, the named differences are concrete and observable, and the Preference, scores, and rationale tell one story.

### Gold sets and honeypots

Your work is monitored for quality. Two checks run behind the scenes:

What is being measured

- **Gold set.** Some comparisons have a known answer set by the Hatch team. Your agreement with those is measured, and low agreement can remove you from the task.
- **Honeypot checks.** Some comparisons include an obviously worse response. Consistently picking it flags an attention problem.

Neither is a trick. Both are only sensitive to one thing: whether you actually had the conversation and read both replies in full before choosing. Rushing shows up in these checks.

### Before you screenshot

Work through each item.

#### Checklist

0 of 6 complete

- [ ] Click **Submit preference** and **End comparison** first, then screenshot. Most rejections are screenshots taken a moment too early.
- [ ] It is **the exact session** on your task - matched by session name and by session UUID, not a neighbouring row that also looks finished.
- [ ] **Exactly one** screenshot. Not two, not a set.
- [ ] It shows the completed comparison, not the form you were filling in.
- [ ] Not the Previous Sessions dashboard - no "Stopped session" rows or green Start buttons.
- [ ] The session does not read **Ended mid-annotation**. If it does, abandon and replace - do not screenshot around it.

Back to the workflow: Comparison workflow.

---

## Reference

Pay, policy, and the things you only need occasionally.

Everything you need occasionally, in one place.

### Pay

- **Rate:** $45 per hour.
- **Payable time per task:** 75 minutes, covering the whole task - your Hatch session plus the form.
- **How it is tracked:** by keeping your claimed Octahedron task open on Hub while you work.

Claim the task before you open Hatch and keep it open the whole time. The open task **is** the clock; time worked without one is not tracked.

The 75 minutes is a cap on what is paid, not a deadline. You can submit after the timer runs out - the task does not lock - but time past 75 minutes is not additionally paid. Payments follow Hub's standard process.


### Privacy and data handling

- Work only in the persona’s world. Do not invent facts it does not contain.
- Record problems honestly in the Notes field. A session with an environment error and clear Notes is a good submission; a papered-over one is not.

### Getting help

- **Feedback on your work** arrives on the task itself. When a check flags a submission, it comes back with written feedback naming exactly what to fix.
- **Small problems inside Hatch** on an otherwise complete task belong in the required **Notes** block. Notes cannot rescue a missing response, a missing score, an unfinished annotation, or a session that ended mid-annotation - those need a replacement session.
- **If Hatch breaks mid-session**, do not submit. Start at the triage on When Hatch breaks.
- **Your Hatch login** arrives by email - check your inbox and spam folder before your first task.

For anything about your account or payments, use Hub's standard support options.

### The four gates, in one line each

1. **Prompt gate** - the prompt is green before you open the Hatch annotation.
2. **Evaluation gate** - Preference, eight scores, and the Required rationale are green before you submit in Hatch.
3. **Completion gate** - the exact session, matched by name and UUID, reads completed and not **Ended mid-annotation**.
4. **Submission gate** - required Notes filled, exactly one screenshot of the completed comparison, confirmation answered truthfully.

Full detail: Quality checks.

### The thirteen use cases

Pick by the **goal, not the apps**. *"Move my Thursday run if it rains"* is Health & Fitness even though it edits the calendar.

Companionship / Chat · Learning / Research · Health & Fitness · Shopping · Media Creation · Work Productivity / SMB · Entertainment · Emotional Support · Finance · Travel · Relationships · Legal / Civic · Home Automation

**Personal Productivity has been removed** - do not use it. Route calendar or reminder work to the goal behind it.

Six are new to the scaled version: **Companionship / Chat, Media Creation, Entertainment, Emotional Support, Legal / Civic** and **Home Automation**. Most of what is new is conversation rather than errand - in those, Hatch may have nothing to fetch or book, the reply *is* the task, and the language is the whole judgment.

Cover the range. **Companionship / Chat, Legal / Civic, Home Automation, Shopping, Entertainment** and **Travel** are the least-worked categories - pick one of those when your task leaves the choice to you.

### Where a pair is not scoreable

Three cases mean the pair cannot be fairly compared, so it is not scored: a **diverged conversation** (only one side has a continuing user prompt), **missing context** the prompt refers back to, or a **data issue** such as a missing response or a duplicated prompt.

An **access limitation** on one side is not one of these. When one reply returns the person's data and the other says it cannot reach it, judge the quality of the communication, not the agentic performance.

Full triage: When Hatch breaks.

---

## Examples

<sub>section: **Reference**</sub>

Worked contrasts for prompts, judgment, and rationales.

Worked contrasts, all checked against the app capabilities and the prompt rules.

### Prompts - Errands

Good

Do I need to pay anything before my appointment on Thursday, and how much?

Bad

Create a system to keep me organized and on top of all my commitments.

> **Info**
>
> The good prompt is first person, anchored in a real email thread, and answerable only by reading it.

Good

Based on my calendar and my Oura tracking, build an exercise plan that includes at least two dance classes a week.

Bad

Create an exercise plan with two dance classes per week.

> **Info**
>
> Real prompts pull from records that actually exist, usually more than one.

More prompts that work:

- *"Create a Notion page called May prep with bullets for the Act III sync, Luna's vet check, and the Earth Day 5k."*
- *"Draft a Gmail reply to Alicia confirming I'm in for the 5k."*
- *"Read mom's Outlook message about Thursday and write a reply I can paste."*
- *"Did I sleep badly the night before the Hartford trip?"*
- *"When's my next PT appointment and what do I need to bring?"*

### Prompts - Conversations

Six of the thirteen use cases are conversations rather than errands: Companionship / Chat, Emotional Support, Entertainment, Media Creation, Legal / Civic and Home Automation. In those, Hatch may have nothing to book or move - the reply *is* the task. They still have to be anchored in the persona's world. A chatty prompt with nothing behind it is an ungrounded prompt.

Good

That Act III sync got pushed for the third time. Going by my calendar and the thread with Priya, is this project actually slipping or is it just me?

Bad

How's my week going? Let's chat.

> **Info**
>
> **Companionship / Chat** - casual is fine, unanchored is not. The good version is a real conversation opener that still points at a specific event and a specific thread. The bad one gives Hatch nothing of this person's world to reach for.

Good

I've got the check-in with Priya tomorrow and three things due the same week. I'm dreading it.

Bad

I'm feeling stressed, can you help.

> **Info**
>
> **Emotional Support** - the good version names what is actually on the calendar, so Hatch has something to fetch and the reply can be specific to this person's week. The bad one could have been sent by anybody.

Good

I've got Thursday evening free before the Hartford trip. Find me something to watch that fits what I've actually been into lately.

Bad

Recommend me a good show.

> **Info**
>
> **Entertainment** - the good version is bounded by a real free evening and asks Hatch to use the person's own history. The bad one needs nothing from the environment.

Good

Write the caption for my 5k post. Pull the details from the confirmation email and keep it in my voice.

Bad

Write me an Instagram caption.

> **Info**
>
> **Media Creation** - the good version has a real source record and a real constraint (their voice), which is exactly what separates two attempts at it. The bad one has no source and no way to be wrong.

Good

Make sense of the lease renewal in my Drive - what am I actually agreeing to on the deposit?

Bad

Is my lease legal?

> **Info**
>
> **Legal / Civic** - general information about a document the persona actually has. Not formal legal advice, and not a question about a document that does not exist.

Good

Set the lights for movie night on Thursday the way I usually have them.

Bad

Turn on all my lights.

> **Info**
>
> **Home Automation** - the good version leans on an existing routine and existing devices, so the two arms have real decisions to make. The bad one is a single switch with nothing to compare.

### What decides a close call

Good

B is slightly better. Both completed the calendar update, but B confirms the result in three clear bullets. A repeats the plan, tool process, and verification in two long paragraphs, and the extra detail does not help the user.

Bad

A is better because it is more detailed.

> **Info**
>
> More words are not more value. Judge whether the extra detail helps the user.

Good

Both responses are correct and complete. B is slightly better because it sounds natural and matches the user's casual tone, while A reads like a generic completion log.

Bad

B had better vibes.

> **Info**
>
> Style can decide a close comparison, but name the observable difference.

Good

A is significantly better. B is punchier, but it never created the requested calendar event. A completed and verified the action.

Bad

B is slightly better because it was shorter and cleaner.

> **Info**
>
> Concision and style do not override missing execution.

### A real task that went wrong

Production data, abridged. The person asked about their softball league rules - specifically, whether they could wear metal cleats.

**Response A**

> Found it in your Drive - Mahoning_Valley_Softball_League_Rules.pdf
>
> Here's the quick rundown for the Warren Road Wrenches:
>
> **Your team:** Tuesdays at 6:30pm, Waddell Park Field 3. Captain is Thinh Mai, you're listed at SS.
>
> **Game play:** USA Slow-Pitch rules. 7 innings OR 65-min time limit - no new inning after 65. Pitch is 6–12 ft arc with a strike mat. 3 homers per team per game max, anything over is an out.
>
> *[Roster, Equipment and Conduct sections cut for length]*
>
> **On your cleats:** No - metal spikes are not allowed. It says molded cleats or turf shoes only. You'll need to grab a pair of molded ones.

**Response B**

> Found it - **Mahoning_Valley_Softball_League_Rules.pdf** in your **Drive**. You're listed as **SS** for the **Warren Road Wrenches**.
>
> **Team stuff:** Captain is **Thinh Mai**. Home is **Waddell Park Field 3** on **Tuesdays at 6:30 PM**. You need **8 to start** with at least **3 women**, and you must field at least **4 women** at all times.
>
> **Game play: 7 innings** or **65-min time limit** - no new inning after 65. **1-1 count** to start, one **courtesy foul** on two strikes. Pitch **6–12 ft arc**, **strike mat** counts. **10-run mercy** after 5 innings, **15 after 4**. **No stealing**, no leading off, **sliding is okay**. **10 in the field** - that extra is an outfielder.
>
> *[Power, Equipment and Other sections cut for length]*
>
> **Shoes - your question:** No **metal spikes**. **Rule 4.3** is **molded cleats or turf shoes only**, so you'll need different shoes.
>
> I pulled a copy here: ☐ Mahoning Valley Softball League Rules
>
> Want me to set a Tuesday 6:15 PM reminder for Waddell Park?

> **Info**
>
> A is the one to favour
>
> Both get the rules right, so **Correctness is a genuine 3**. What separates them is everything else. B bolds almost every clause - when everything is emphasised, nothing is, and it reads as one dense block with nowhere for the eye to rest. A bolds only its section labels. B also ships a broken image placeholder and closes with the forbidden "Want me to…" line.

#### What the fellow submitted

| Field | Submitted |
| --- | --- |
| Overall preference | A better |
| Style and behavior (High level) | 3 · Tie ✗ |
| Correctness (High level) | 3 · Tie ✓ |
| Style (Granular) | 3 · Tie ✗ |
| Coherence & writing quality (Granular) | 3 · Tie ✗ |
| Helpfulness (Granular) | 2 · A better ✓ |
| Completeness (Granular) | 2 · A better ✓ |
| Tone (Granular) | 3 · Tie ✗ |

This is the habit we are stopping

Five of eight came back Tie, on two replies that look nothing alike. Only Correctness is defensible - both do get the rules right.

The preference was right and the scores contradicted it. If A is better overall, something has to be better *somewhere*, and here it was the bolding, the density and the forbidden closing - Coherence and Style, plainly. **Identical, not merely close.**

### Comparison write-ups

#### Liverpool watch party invites - Google Contacts, WhatsApp

*"Who should I invite to a Liverpool watch party?"*

Good

"A slightly better." Arm A quotes each potential invitee showing they follow Liverpool; Arm B does so for only some of them.

Bad

"A slightly better." A felt more thorough.

> **Info**
>
> The good version names the exact evidence gap.

#### Instagram engagement tracker - Gmail, Notion

*"Which weekly-update emails had the most likes and new followers? Add this to a Notion tracker."*

Good

"B significantly better." Arm B put the correct week-by-week data into the Notion page, verified in the response. A tracker is meant to follow engagement over time, so B's full history beats A's single top-week snapshot.

Bad

"B is better." B's Notion page was more complete.

> **Info**
>
> The good version ties the difference to the point of the artifact and confirms the artifact exists.

#### Check-in script - Google Drive, Google Docs, Google Calendar

*"I'm nervous about my check-in with Priya. Create a Google Doc script that hits the selling points."*

Good

"B significantly better." Arm B's doc gives time-frames for each section of the meeting and more specific quotes. The user said they were nervous, so that structure directly serves the stated need.

Bad

"B slightly better." B's script was better written.

> **Info**
>
> The good version grounds the preference in what the persona actually asked for.

#### Poshmark sales tracker - Google Sheets, WhatsApp, Gmail

*"Create a Google Sheet tracking my Poshmark listings, then write me a message to Sean celebrating the sales after fees."*

Good

"A slightly better." Both arms missed some sales, but Arm A was one sale off while Arm B missed several.

Bad

"A slightly better." A's sheet looked more accurate.

> **Info**
>
> The good version quantifies the gap. Note the WhatsApp part asks for message text, which works whether or not that chat already exists.

#### Draft reply to Alex - Gmail

*"Draft a Gmail reply to Alex: thanks for the heads up, I'll sort it this week."*

Good

"A significantly better." Correctness = 1: Arm A left the message as a Gmail draft, as asked, while Arm B sent it without authorization. B's warmer phrasing puts Style at 4, and the unauthorized send still decides the preference.

Bad

"A slightly better." B was too aggressive with the send.

> **Info**
>
> Name the dimension the miss lands on, and say why it outweighs the communication win.

#### Correctness ties, the writing does not - Gmail, Google Calendar

*"Summarize what I committed to in the March 9 thread and put the deadlines on my calendar."*

Good

"B slightly better." Both arms captured the same three commitments and created the same two correct calendar events, and both omitted the follow-up owner - so Correctness is a genuine 3. B leads with the two dates and the one thing still unassigned; A opens with "Got it - here's what I found!" and puts the commitments behind a restated summary of the thread. Coherence 4, Style 4.

Bad

"Tie." Both arms did the same work and no coherence, style, or tone difference is defensible, so all eight dimensions are 3.

> **Info**
>
> This is the pair that used to be taught as a true tie. It is not. The work matching is a Correctness 3; it says nothing about the six communication dimensions. Two replies written by different models almost never read identically - look at the opening line, the ordering, and what got buried.

### Reading the eight numbers

Good

Correctness = 1 - A cited the correct appointment time from the confirmation email and B contradicted it. Style = 4 and Tone = 4 - B sounds like a person, A reads like a status dump. Overall A significantly better; a wrong appointment time is not repaired by a friendlier voice.

Bad

A is more correct so A wins everything.

> **Info**
>
> Correctness favouring A and style favouring B is a normal, expected split.

Good

Correctness = 3 - both arms drafted the same reply to the same recipient with the same date, verified in Apps. Style = 4 and Coherence & writing quality = 4 - B leads with the answer while A opens with "Got it - happy to help!" and narrates its own process first. Overall B slightly better.

Bad

Correctness = 3, so Style = 3, Coherence = 3, Tone = 3 and Preference Tie.

> **Info**
>
> Correctness ties often - the two arms usually do the same work. The communication dimensions almost never do. A 3 there means the two replies were identical on it, not merely close.

### Rationales that hold up

Someone who did not see the two replies should be able to follow your call from the rationale alone.

Good

A opens with the answer - flight rebooked, landing 6:40 - while B buries it under "Got it - happy to help!" and a filename with an ID number. A also skips the "Do you want me to…" closing B ends on.

Bad

A is better overall.

> **Info**
>
> Name the difference and point at where it happens. A verdict with no observation behind it supports nothing.

Good

B references the sister's birthday next month and the three ceramic posts she sent last week, both of which are in the persona's accounts - the personalization feels earned. A asks the person to supply information Hatch already has.

Bad

B has better tone and style.

> **Info**
>
> Restating the dimension names is not an observation. Say what the response actually did.

Good

B wins Style, Tone, Coherence and Completeness, but A left the message as a draft as asked while B sent it. The unauthorized send decides the preference; a friendlier voice does not repair it.

Bad

A is better because correctness matters most.

> **Info**
>
> When a correctness failure overrides several communication wins, say so explicitly - that is the trade-off the rationale exists to explain.

Good

B is longer, and the extra length is the two conflicting calendar entries A never mentioned - which is exactly what the person needs to resolve the clash. Completeness = 5.

Bad

B is more detailed so it is more complete.

> **Info**
>
> If the longer response wins, name the value the extra length added. Length on its own is not evidence.

Back to the workflow: Comparison workflow.

---

## Common mistakes

<sub>section: **Reference**</sub>

What the message means, and what to do about it.

### Error messages - What they mean, what to do

Match the exact wording on your screen.

| What you see | What it means | What to do |
| --- | --- | --- |
| `Error: 400 : failed to checkpoint arm A: session not found` | The backing Hatch session is gone. Nothing you type reaches the arms. | Reload once. If the arms still do not boot, abandon and replace |
| Both arms stuck on **Booting the agent…** | The session never provisioned the arms. | Reload once, then abandon and replace |
| **Ended mid-annotation** in the Latest checkpoint column | The comparison cannot be reopened or finished. | Abandon and replace. Never tick the completion attestation |
| A **Stopped session** row in the sessions list | That session is not running. It is not evidence of a completed comparison. | Match your session by name **and** UUID before screenshotting |
| **Cannot complete task with incomplete steps** | A required step on the task is empty or invalid. | Open the feedback panel and work it until it reads **Nothing needs attention** |
| A required text block highlighted on submit | Notes or the confirmation block is blank. Blank blocks block submission. | Fill it truthfully. "Nothing I noticed at the moment" is valid |
| **Needs attention** items in the feedback panel | QC found a field that contradicts what you did. | Correct the field so the task tells one true story. Never change a value only to clear a warning |
| One arm says **Something went wrong** and then answers properly | The arm recovered. It is still valid. | Continue and score normally |
| One arm says **Something went wrong** and never answers | The comparison is incomplete. | Retry the arm, then the session. If it fails, abandon and replace |

### Prompts

Good

My saved concert emails have three shows I said I'd go to this spring. Put them on my calendar and flag the one that conflicts with the Hartford trip.

Bad

What concerts should I go to this month?

> **Info**
>
> In an environment without internet access, a prompt that cannot be answered with the public web switched off is invalid. If the guidelines modal says **Internet: Available**, web-dependent asks are allowed - but still anchor them to the persona's records.

Good

Summarize what my hiking group decided about Sunday and write a message I can copy.

Bad

Send a WhatsApp message to the new landlord's number about the rental.

> **Info**
>
> WhatsApp only sends inside chats that already exist. Google Contacts and Oura are read only, and Outlook Mail cannot create drafts.

Good

Looking at the week of March 9, which evenings were free before 7pm?

Bad

What does my schedule look like this weekend?

> **Info**
>
> The persona's records may end months earlier. Use explicit dates when they do.

Good

I told Alicia I'd do the 5k with her. Get it on my calendar with enough lead time to train.

Bad

Create a calendar event named "5k" on April 18 at 9:00am with a 30-minute reminder.

> **Info**
>
> Dictate every detail and both arms produce the same thing, leaving nothing to compare.

Good

I've got the check-in with Priya tomorrow and three things due the same week. I'm dreading it.

Bad

I'm feeling stressed, can you help.

> **Info**
>
> Conversation-led use cases - Companionship, Emotional Support, Entertainment, Media Creation - still have to be anchored in the persona's world. Chatty is fine; unanchored is not. A prompt with nothing behind it gives Hatch nothing to fetch and the two arms nothing to differ on.

### Evaluation

Good

Check in Hatch. Were the drafts created? Is the event at the right time, in the right app?

Bad

Reading the two final messages and deciding which one reads better.

> **Info**
>
> Prose that reads well but did nothing loses to prose that actually completed the request.

Good

A cites both source emails with sender and date; B names neither and contradicts one on the appointment time.

Bad

A seems more reliable.

> **Info**
>
> Name a concrete difference and tie it to the dimension it moved. "Correctness = 1" means A is much better on correctness; you have to say why.

Good

Correctness = 3 because both arms got the rules right, but Coherence = 1 because B bolds almost every clause while A bolds only its section labels, and Style = 1 because B closes with "Want me to set a reminder?". Overall A better.

Bad

Correctness = 3, so Style, Coherence and Tone are all 3 too. Overall A better.

> **Info**
>
> This is the most common failure on this project. Correctness ties often - the arms usually do the same work. The communication dimensions almost never do. If the preference favours one arm, something has to be better somewhere, and your scores have to say where.

Good

B is slightly better. Both completed the update, but B confirms the result in three bullets while A repeats the plan and the tool process.

Bad

A is better because it is more detailed.

> **Info**
>
> Length is not a score. Extra detail counts only when it serves the user's goal.

### Submission

Good

Response B failed, so the session was renamed `488c89ae9c3f_abandonedtask_3`, recreated, and annotated from the beginning.

Bad

Submitting with "Response B failed" in the Notes field.

> **Info**
>
> Notes cover small problems on a complete task. A missing response blocks submission.

Good

One screenshot of the completed comparison in the exact session named on the task.

Bad

Several screenshots, or one of the sessions dashboard showing a Stopped session row.

> **Info**
>
> Exactly one screenshot, of the completed comparison itself - not the list, not the form you were filling in.

Good

Checking what each arm actually used and listing Gmail, Google Calendar, WhatsApp - every app either arm actually invoked.

Bad

Listing the apps your prompt mentioned, spelled "Google Calander" and "Whats App".

> **Info**
>
> The apps field is the union of what the arms actually used, in canonical spelling.

### One answer per situation

| Situation | Do this |
| --- | --- |
| Prompt needs current public information | Rewrite it before running |
| Prompt asks to message a new WhatsApp contact, merge contacts, or make an Outlook draft | Rewrite it before running |
| A model claims a draft it never created | Move Correctness toward the other arm and say so in the rationale |
| One arm errors or is cut off | Retry; if it fails, abandon and recreate |
| You could only recover part of a transcript | Abandon and recreate |
| You copied text between arms | Abandon and recreate |
| The session ended before you submitted a preference | Abandon and recreate |
| Both mostly succeed, one is better organized | Coherence & writing quality favours that arm; usually a slight preference |
| Both complete and correct, one is punchier and more natural | Slightly better, for the punchier arm |
| One is longer but mostly repetitive or internal | No automatic credit; it can move Style or Coherence & writing quality against it |
| One omits requested work | Prefer the complete response, even if the incomplete one is more polished |
| One sends when asked to draft | Significantly better, against the sender |
| You want a winner but scored the communication dimensions 3 | Look again and move the dimension that actually separates them - 3 means identical, not close |
| Wrong app spelling or session-name format | Fix the field and resubmit |
| Older task version is missing a field | Fill only the fields shown |
| Two replies feel about the same on Style after a second read | Find the small thing that tips it, score 2 or 4, and name it in the rationale |
| Only one side has a continuing user prompt - the conversation diverged | Do not score it |
| A response is missing, or a user prompt is duplicated | Do not score it |
| One reply returns the persona's data, the other says it cannot reach it | Score it normally - judge the communication, not the agentic performance |

### Reading a comparative score

| Score you entered | What it means |
| --- | --- |
| Coherence & writing quality = 5 | B is much better on that dimension |
| Correctness = 1 | A is much better on correctness |
| Any dimension = 3 | Tie on that dimension |
| Style, Tone, Warmth, Coherence, Helpfulness or Completeness = 3 | You are claiming the two replies were **identical** on that dimension. Rare - check that you meant it |
| Correctness = 3 | Both arms did the same correct work. Common, and usually right |

Good

Correctness = 1 because A used the right date and B created the event a day early. Style = 4 because B's confirmation sounds human where A reads like a log. Overall A significantly better.

Bad

Correctness = 1 and Style = 1 and Tone = 1, because A won overall.

> **Info**
>
> Do not sweep every dimension toward the arm you preferred. Each score needs its own evidence.

Good

Style = 4 and Tone = 4 for B, Coherence = 2 for A, Correctness = 3. B sounds like a person but stacks three paragraphs where one would do; A is tighter but reads like a status log.

Bad

Style = 4, Tone = 4, Coherence = 4, Helpfulness = 4, Completeness = 4, Correctness = 4.

> **Info**
>
> Dimensions pointing in different directions is a sign you scored them independently. Eight identical numbers is a sign you scored the arm, not the dimensions.

Back to the workflow: Comparison workflow.

---

## Check your understanding

<sub>section: **Reference** · nav label: *Self-check*</sub>

Check your understanding before your first real task.

Work through these before your first task.

### Setup and workflow

#### What must you do before opening Hatch?

Claim a Hub task and keep it open. That open task is your 75-minute payable clock.

#### Your alias is \`488c89ae9c3f\` and this is your 8th task. What is the session name?

`488c89ae9c3f_task_8`, typed into the **Name** field before you click Create session, then copied into the form. The session ID is a separate UUID.

#### Where does the apps list come from?

Hatch - every app either arm actually invoked, in canonical spelling. Not your prompt, not memory.

### Use cases

#### How many use-case categories are there, and how do you pick?

Thirteen, up from seven. Pick by the **goal, not the apps** - *"move my Thursday run if it rains"* is Health & Fitness even though it edits the calendar. Work the category your task names; if it does not name one, pick the one matching the persona's underlying goal, and cover the range across your tasks.

#### Your category is Emotional Support and Hatch has nothing to book or move. Broken task?

No. Several of the new categories - Companionship / Chat, Emotional Support, Entertainment, Media Creation - are conversations rather than errands. Nothing gets booked or looked up, and neither arm may show app activity. **The reply is the whole task**, so the language is the whole judgment: the writing, the voice, the register, the tone.

#### So a conversation prompt can be about anything?

No. It still has to be anchored in this person's data. Emotional support about their day means something actually on their calendar that day; relationships means their real partner or friend, the one who lives in this environment. There is always something for Hatch to fetch. A chatty prompt with nothing behind it is an ungrounded prompt.

### Prompts

#### "What concerts should I go to this month?"

Depends on the environment. If the guidelines modal says **Internet: Available**, the assistant can look it up - anchor the ask to the persona anyway. If internet is not available, it is invalid: rewrite it around concerts already in the persona's emails or calendar.

#### "Send a WhatsApp message to a number the persona has never messaged."

Invalid. WhatsApp can only send inside chats that already exist. Sending to the hiking group is fine if that chat is already there; otherwise ask for a summary or pasteable text.

#### "Draft an Outlook reply to Alicia."

Invalid. Outlook cannot create drafts. Ask for the reply text instead.

#### The persona's records end in March and your prompt says "this weekend."

Invalid. Use a range the data covers, like "the week of March 9". An empty recent calendar is not evidence that nothing happened.

#### "Create a calendar event named 5k on April 18 at 9:00am with a 30-minute reminder."

Feasible, but a poor comparison prompt. Every detail is dictated, so both arms produce the same thing. Give the goal instead.

### Session setup

#### Which mode and which protocol?

**GAIA PREFERENCE**, plus **Hatch RM Style Task - current version**. Never choose an Avocado protocol or any other protocol. GAIA RUBRICS is a different project; do not choose it. The version label is the protocol label - your persona version still comes from picking a V2 **Universe**.

#### Which universe do you use, and who picks it?

Any **V2** universe. You choose it yourself from the **Universe** dropdown - nobody assigns one. V1 is no longer in use.

#### You clicked Create session. What do you do next?

Wait while Hatch provisions the session. When the status changes to **RUNNING**, click **Open** in the Actions column. There is nothing to click before that.

#### When do you click Start annotation?

After you explore the persona through **Apps** and click **Start comparison**. The Start annotation dialog opens, you paste the initial user request into it, then click **Start annotation** inside the dialog. Do not run any of the task conversation before that.

#### One response is twice as long. Is it better?

Not by itself. Reward the response that gets the user the result with the least unnecessary friction. Length only helps when the extra detail serves the goal.

#### One response is much shorter and punchier. Is it better?

Only if it is also complete and correct. A short response that skips requested work is incomplete, not punchy.

### Comparisons

#### If the task needed follow-up turns, what are you judging?

The full interaction, from the initial annotated prompt through the final follow-up. Earlier mistakes still count even if the model later recovers. Every follow-up turn must go to both arms with the same meaning, wording, and order.

#### What are the eight dimensions and the scale?

Style and behavior (High level), Correctness (High level), Style (Granular), Coherence & writing quality (Granular), Helpfulness (Granular), Completeness (Granular), Tone (Granular), Warmth (Granular). One comparative value each: **1 = A much better · 2 = A better · 3 = Tie · 4 = B better · 5 = B much better**.

A 3 means the two replies were **identical** on that dimension.

#### B claims it created a Gmail draft, but no draft exists in Hatch.

Correctness (High level) moves toward A - a 1 or 2 - and Completeness follows. Name the missing draft in the Required rationale and prefer A. A claimed action that never happened is worse than no action.

#### A drafted the reply as asked; B sent it.

"A significantly better," with Correctness strongly favouring A, even if B's Style and Tone favour B. An unauthorized send is decisive, not a close call.

#### Correctness came out 3. Can the Preference still favour one arm?

Yes. Correctness (High level) may frequently be a tie. If B wins Style, Tone, and Coherence & writing quality, "B slightly better" is a consistent result - say why in the Required rationale.

#### Two replies feel about the same on Style after a second read. What do you do?

Find the small thing that tips it, score it 2 or 4, and name it in the rationale. A 3 carries no signal; the scale already has a setting for *close, but this one*.

Both weak? Still pick the one you prefer and say why. Both strong? Look again - there almost always is something. Genuinely identical is rare on the communication dimensions, and common only on Correctness.

#### Your Required rationale reads "B handled the task more professionally."

It comes back. It names nothing observable and supports none of your non-3 scores. Rewrite it around what B actually did that A did not.

#### Where does a "Do you want me to…" closing land?

**Style.** It is one of the named AI-slop tics, along with "Got it - ", "Sure thing!", ceremony openers, forced personas, and leaked filenames or ID numbers. Sloppy sentence construction is Coherence; emotional misfire is Tone. Style is *which voice*.

#### One reply pulls the persona's Oura data; the other says it cannot reach it. Broken pair?

No. That is an agentic performance gap, and it is not a skip. Assess the **quality of the communication**, not the agentic performance - a reply that hits a wall and says so gracefully, in this person's register, can legitimately beat one that returns the data in a tone-deaf slab.

#### Only one side has a second user prompt continuing the conversation.

Do not score it. Intent has diverged too far for a fair comparison. The same goes for a prompt that refers back to context you cannot see, and for data issues like a missing response or a duplicated prompt.

#### The system ended the conversation after one turn.

Expected, not broken. A real multi-turn conversation is the normal shape of a task - ask, request, follow up the way a person would - but the system sometimes limits a comparison to a single turn and ends it automatically. Score the exchange you got.

### Submission and recovery

#### Hatch crashed halfway through. What now?

Do not submit an incomplete comparison. Retry the failed response or session. If it cannot be recovered, rename the session `youralias_abandonedtask_N`, create a new one, and annotate from the beginning.

#### You could only recover B's final response, not the earlier turns.

Recreate the task. A reconstructed or borrowed transcript cannot be submitted.

#### A returned task says the apps field is misspelled. Fix or recreate?

Fix. Spellings, categories, session names, and task metadata are editable. A submitted Hatch evaluation is not. Invalid prompts, missing arms, and unrecoverable transcripts are not.

#### Everything is scored and written, but you never completed the annotation in Hatch.

Not submittable. Completing the annotation is how your work is saved.

### The current scoring model

#### Which arm does a 5 favour?

Arm B. **1 = A much better · 2 = A better · 3 = Tie · 4 = B better · 5 = B much better.** A 1 favours Arm A.

#### A is more correct, but B sounds far more natural. Must every score favour A?

No. Score each dimension independently. Correctness moves toward A; Style and Tone move toward B. The overall Preference weighs them.

#### What does Style and behavior (High level) ask you to ignore?

Correctness. It asks only which response you prefer based on how Hatch is communicating.

#### One arm shows "Something went wrong." Do you score it?

No. Stop, retry, and recreate the session if it does not recover. Never submit an incomplete comparison.

#### Which scores need support in the Required rationale?

Every score away from 3, plus the overall Preference. One concrete observation can support several dimensions.

#### You preferred A overall but scored every communication dimension 3.

That contradicts itself and it is the single most common failure on this project. If A is better overall, something is better *somewhere* - find it and move that dimension. Five of eight coming back Tie on two replies that look nothing alike is the habit being stopped.

Back to the workflow: Comparison workflow.

---

## FAQ

<sub>section: **Reference**</sub>

### On a comparison, what am I scoring?

The whole interaction on each side. In Hatch you choose one overall **Preference**, then score **eight comparative dimensions**, then write the **Required rationale**, then click **Submit preference** and **End comparison**. There are no separate quality scores for A and B - each dimension gets one comparative value.

### Which protocol do I choose?

**Hatch RM Style Task - current version**, with mode **GAIA PREFERENCE** and any **V2** universe. Do not choose an Avocado protocol or any other protocol. The version label is the protocol label; V2 is the persona version and comes from the **Universe** dropdown.

### What does 1 / 3 / 5 mean?

**1 = A much better · 2 = A better · 3 = Tie · 4 = B better · 5 = B much better.** Low favours Arm A, high favours Arm B, 3 is a tie on that dimension.

### Can different dimensions favour different arms?

Yes, and they often should. Score each dimension independently. A can be more correct while B communicates better. Do not force all eight numbers to point the same way.

### Why can Correctness be a Tie while the Preference favours one arm?

Because Correctness (High level) only asks which arm was more correct - when both did the same correct work, that is a 3. The overall Preference weighs everything, so a clear win on communication dimensions can still make one arm the preferred response.

### What belongs in the Required rationale?

The reason for your overall Preference, concrete observable A/B differences, and support for every dimension scored away from 3. If a decisive correctness or completion failure drove the result, say so. If the longer response won, say what the extra length actually gave the user. One concrete observation can support several dimensions.

### One arm says "Something went wrong." What do I do?

Stop. Do not score it and do not submit. Retry the arm, then the session. If it cannot be recovered, rename the session `youralias_abandonedtask_N`, create a replacement `youralias_task_N`, and rerun the task.

### My task looks different from this guide. Which do I follow?

The task in front of you. This guide describes current behavior; where an older version differs, the task wins.

### When can I send follow-up turns?

After **Start annotation**. Your initial request goes in through **Start comparison** → paste the request → **Start annotation**. If the same underlying task still needs work, send the same follow-up user turn to both arms, in the same words and the same order. Do not run any task turns before annotation starts, and never steer only one arm.

### The guidelines modal says to keep going for several rounds. Do I?

Not across tasks. That text is generic Hatch guidance. On this project **one Hatch session equals one Hub task**. Keep sending turns only while the same task's goal is unfinished. Once it is satisfied, submit the preference, end the comparison, and start a fresh session for the next Hub task. Never reuse one session for two Hub tasks.

### Can my prompt have more than one user turn?

Yes. Record every turn in the prompt field, in order, word for word.

### The agent used an app my prompt never mentioned. Do I record it?

Yes. The apps field is every app either arm actually used, taken from what happened in Hatch.

### A model says it created a draft. Do I take its word for it?

No. Verify it in Hatch. An unverified "created", "sent", or "attached" is a correctness and instruction-following miss.

### Can I ask for a WhatsApp send or an Outlook draft?

WhatsApp can send, but only inside a chat the persona already has - never to a new contact, and it cannot create groups or modify chats. Outlook can send but cannot create drafts. Google Contacts and Oura are read only.

### My rationale got bounced. Did I lose the task?

No. It comes back with feedback, and most feedback points at a field you can edit. Fix it and resubmit. Structural problems - a missing arm, a reconstructed transcript, an invalid prompt - need a recreated task.

### What happens if the timer runs out before I submit?

Submitting late is fine; the task does not lock. 75 minutes is the payable time. Add clear Notes if tool problems ate the time, but never submit an incomplete comparison.

### Can I use an AI assistant to polish my Required rationale?

Yes. AI assistance is allowed for any part of this work.

### The sleep data looks off by a day. Is it?

No. The row date is the wake-up date. "The night of March 14" lives on the row dated March 15.

### What is my chat alias?

It is the value in your own chat profile. Click your chat avatar, click **Profile**, and find **Alias** under **About me**. Copy it exactly - do not invent one. Your session name is `youralias_task_N`, for example `488c89ae9c3f_task_1`.

### How exact does the session ID need to be?

Character for character, copied from Hatch. It is a UUID, and it is not the session name.

### Hatch broke and only one response generated. Can I submit with Notes?

No. Retry; if it cannot be recovered, rename the session `youralias_abandonedtask_N`, create a new `youralias_task_N` session, and run the comparison from the beginning.

### All eight dimensions came out 3. What preference?

If all eight really are 3, the Preference must be Tie - that consistency rule holds. But check first: a 3 means the two replies were identical on that dimension, and that is rare on the six communication dimensions. If you can name a concrete difference, name it, move the dimension score it belongs to, and prefer that arm.

### Which persona version should I use?

V2 only - V1 is no longer in use. In Hatch this comes from the **Universe** you choose; the protocol's version label is the protocol version and does not set the persona version. Subpersonas are fine. The core apps are the same as V1; V2 adds a few, and which ones depend on your environment.

### Hub says "Cannot complete task with incomplete steps". What now?

A required step is empty or invalid. Open the feedback panel and work down it until it reads **Nothing needs attention**. That is the submit gate - not your own sense of being finished. If the missing item is a response, a user turn, or a Hatch value you never produced, it cannot be typed in after the fact.

### Is the Notes field required?

Yes. A blank Notes block blocks submission. Write what actually happened - an environment error, a tool the agent could not reach, odd behavior in Hatch. If nothing came up, say so; "Nothing I noticed at the moment" is a valid entry. Notes cannot rescue a missing response or an unfinished annotation.

### How many screenshots do I upload?

Exactly one, of the **completed comparison** in the exact session named on your task. Take it after **Submit preference** and **End comparison**. Not the sessions dashboard, not a Stopped session row, not the form you were filling in.

### How do I know I am looking at the right session?

Match it by session **name** and by session **UUID**. The sessions list mixes live, stopped, and ended-mid rows, and a neighbouring completed row is not evidence for yours.

### The task asks me to confirm the session did not end mid-annotation. What if it did?

Then the task cannot be submitted. Never tick the confirmation to clear the block. Rename the session `youralias_abandonedtask_N`, rerun the task in a replacement `youralias_task_N`, and repoint both the session name and the UUID on Hub task.

### A red 400 toast says "failed to checkpoint arm: session not found". Can I fix it?

Reload once. If both arms are still stuck on **Booting the agent…**, the backing session is gone and nothing you type reaches the arms. Abandon and replace.

### An arm errored and then answered properly. Is the task dead?

No. An error followed by a real, complete response is **recovered** - that arm is still valid. Only an unrecovered, error-only arm kills the task.

### QC flags a field but I think the value is right. Should I change it to clear the warning?

No. Never change a value purely to clear a warning. Correct whichever field is actually wrong so the whole task describes one true run. If the submitted Hatch judgment itself is wrong, recreate the session.

### What are the four gates?

**Prompt gate** - the prompt is green before the Hatch annotation opens. **Evaluation gate** - Preference, eight scores, and rationale are green before you submit in Hatch. **Completion gate** - the exact session reads completed and not Ended mid-annotation. **Submission gate** - required Notes, exactly one screenshot, confirmation answered truthfully.

Back to the workflow: Comparison workflow.

---

## Reviewer checklist

One page. Use it from top to bottom when reviewing a submitted task.

> **Info**
>
> How to use this page
>
> Review the final submitted comparison - not an old QC result, historical task stage, or preferred answer of your own. Different but coherent judgments can pass.
>
> Stop only when a confirmed defect makes the task fundamentally invalid or unscorable. Ordinary coaching issues do not add up to a failure. If a material evidence question cannot be resolved, use **Review** rather than guessing.

### 1. Is the task reviewable?

Check the submission and its identity before judging the content.

**The submission**

- ✓ Both arms contain the actual, complete responses and every materially relevant user turn. Nothing is missing, visibly cut off, summarized, reconstructed, or copied from another run.
- ✓ Required completion evidence is present and readable for the exact submitted comparison.

**Its identity**

- ✓ The session name follows `youralias_task_N` and belongs to the submitted Hub task.
- ✓ The Hatch comparison UUID matches the submitted Session ID. Do not substitute an Exploration, annotation, run, or browser ID.
- ✓ The comparison uses the required current project mode, assigned V2 persona or subpersona, and currently required Hatch protocol.

**The turns**

- ✓ Both arms received the same initial request and materially equivalent follow-up turns in the same order.
- ✓ Natural branch-specific follow-ups are acceptable when they answer each arm's clarification and preserve the same underlying goal.
- ✓ Authentic identical responses are valid. They require equal dimension scores and a Tie unless a real visible difference exists.
- ✓ A recovered error or later correction does not automatically invalidate an otherwise complete comparison.

Invalid comparison

Confirmed missing arms, unrecoverable truncation, wrong-session content, reconstructed responses, or materially different user instructions.

### 2. Was the prompt valid?

**Grounding**

- ✓ The request is natural and meaningfully grounded in the persona's real records, responsibilities, ongoing context, or persona-relevant research.
- ✓ It does not rely on invented private people, dates, records, or events.

**Feasibility**

- ✓ The requested work is feasible with the connected apps, their actual capabilities, and the user's authorization.
- ✓ Persona-grounded public-web research is allowed. An artificial private-app action or "Internet: Available" field is not required.
- ✓ Search permission does not authorize purchases, bookings, seller contact, messages, or unrelated account actions.

**Shape and labelling**

- ✓ The prompt states a useful goal without prescribing every click or removing meaningful model choice.
- ✓ Follow-up turns clarify or continue the same underlying goal.
- ✓ The use-case category reflects the user's actual goal.
- ✓ Apps utilized includes every app actually operated by either arm and excludes apps that were only mentioned or available.

> **Info**
>
> Where the line sits
>
> Awkward wording, a close category call, or slight over-prescription is usually **coaching**. A fundamentally ungrounded, impossible, unrelated, or mechanically predetermined task may require **failure**.

### 3. Do the scores hold up?

There are seven comparative dimension ratings plus the separate overall Preference.

| Rating | Meaning |
| --- | --- |
| 1 or 2 | Favors Response A |
| 3 | Tie |
| 4 or 5 | Favors Response B |

> **Warning**
>
> Two different scales
>
> These comparative ratings are not the final 1-5 SQS grade at the bottom of this page.

**Completeness and independence**

- ✓ Overall Preference and all seven comparative ratings are present and valid.
- ✓ Each dimension is judged independently.

**When a Tie is right**

- ✓ A score of 3 is valid whenever neither arm has any advantage on that dimension. The replies do not need to be identical.
- ✓ Shared strengths, immaterial differences, or balanced tradeoffs can support a Tie.
- ✓ Tie-heavy or uniform scoring triggers a consistency check, not an automatic failure.

**Preference weighting**

- ✓ Non-Tie scores point in the same direction as the relevant observations in the rationale.
- ✓ Overall Preference is a weighted judgment - not a vote count, score total, or average.
- ✓ A decisive Correctness, Helpfulness, or Completeness difference may outweigh several smaller communication advantages.
- ✓ A mathematically opposite-looking score pattern asks for a weighting check; it is not automatically wrong.

**Evidence behind Correctness**

- ✓ Material facts or actions that could change Correctness or Preference are checked against the relevant task evidence, app, or artifact.
- ✓ Hidden state is not invented. A bare "done" claim is not independent proof, but inaccessible backend evidence alone is not proof that an action failed.

> **Warning**
>
> Dates and "today"
>
> When a date or "today" controls the judgment, verify it through the original or restored Hatch Calendar using Today. Do not substitute the real submission date, newest email, initial calendar view, or a universal assumed date.

### 4. Does the rationale earn the judgment?

**What it must name**

- ✓ The rationale names observable actions, claims, omissions, errors, or presentation differences.
- ✓ It explains the overall Preference and gives enough support to understand the material score pattern.
- ✓ Preference, scores, and rationale tell one coherent story.
- ✓ A slight versus significant Preference broadly fits the difference described.

**What it does not need**

- ✓ One concrete observation may support multiple dimensions.
- ✓ Separate headings or a paragraph for every dimension are not required.
- ✓ Thin but understandable support is normally coaching, not an automatic failure.

**Judgment discipline**

- ✓ Length alone does not choose the winner. "More detailed", "more professional", or "better overall" needs an explanation of what useful content was added or omitted.
- ✓ A local inaccurate example is distinguished from a false premise that defeats the controlling judgment.
- ✓ The review does not replace the fellow's coherent judgment merely because another winner was also defensible.
- ✓ The judgment is based on visible responses and task evidence - not a guess about which model wrote either arm.


Revision or failure territory

A globally generic rationale, direct material contradiction, wrong-arm attribution, or unsupported controlling premise.

### 5. Does the submitted task match the evidence?

**Identity**

- ✓ The session name and Hatch comparison UUID belong to the submitted Hub task.
- ✓ The reviewed content comes from the exact current completed comparison.

**Values**

- ✓ The submitted prompt matches the actual prompt.
- ✓ The submitted Response A and Response B contain the complete materially relevant trajectories.
- ✓ Preference and all seven comparative ratings match the submitted values.
- ✓ The Required rationale matches the final submitted rationale.

**Evidence**

- ✓ Many tasks have no screenshot. If none is present, judge the task on everything else that is there and do not treat the absence as a defect.
- ✓ When a screenshot is present, judge it only on information it actually displays.
- ✓ Current content is judged independently of an old QC badge, earlier revision, or historical stage.

> **Warning**
>
> Mismatch versus unclear
>
> A confirmed material mismatch is a **failure**. Blurry, unavailable, or genuinely conflicting evidence is **Review** - not an assumed mismatch.

### How to reach the result

Use the most serious supported finding. Do not average checklist items or subtract points for every imperfection.

- Fundamental invalidity, major contradiction, unreliable A/B attribution, or substantiated integrity failure controls over lesser findings.
- Materially unreliable controlling reasoning requires revision.
- Localized omissions, thin support, or ordinary calibration concerns receive coaching.
- Ordinary coaching issues do not accumulate into a failure.
- The score applies to this task only. It is not a fellow-level verdict and should not be averaged automatically into one.
- If a material evidence question remains unresolved, record Review and do not force a numeric score.

### SQS - Submission quality score

There are two outcomes: **Approve** or **Request Changes**. Grades 3-5 are an Approve. Grades 1-2 are a Request Changes. Review is a separate evidence status and receives no numeric grade.

1 - Invalid (Request Changes)

The prompt or comparison is fundamentally invalid, the judgment contains a major contradiction or unreliable A/B attribution, or a substantiated integrity defect defeats the submission.

2 - Revision required (Request Changes)

The controlling reasoning is materially unsupported or unreliable. The task cannot be accepted without correcting or recreating the affected judgment.

> **Warning**
>
> 3 - Usable (Approve)
>
> The central judgment remains understandable and usable but needs substantive coaching, clearer calibration, or fuller support.

4 - Strong (Approve)

A sound, usable comparison with only localized, non-material feedback.

5 - Excellent (Approve)

Concrete, coherent, and well calibrated. Minor coaching does not prevent a 5.

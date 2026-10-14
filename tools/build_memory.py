#!/usr/bin/env python3
"""
build_memory.py — regenerate the GENERATED memory files from per-task retrospectives.

    python3 tools/build_memory.py        (or: bash tools/build_memory.sh)

Reads : tasks/*/RETROSPECTIVE.md   (YAML-ish frontmatter + body)
Writes: memory/NEXT_TASK_DIRECTIVES.md  — §6 "New rules learned" + §8 "What the next task should do differently"
                                           from every ACCEPTED task, newest first. New sessions read this FIRST.
                                           PLUS inherited [generic] directives from reference/*/tasks/*/RETROSPECTIVE.md
                                           (another teammate's archive), so a fresh setup starts with a head start.
        memory/GLOBAL_RETROSPECTIVE.md   — index table + every accepted retrospective body, newest first
        memory/CATEGORY_TRACKER.md       — the 14 Hub categories with done/open status

Design: sessions ONLY write inside their own tasks/<id>/ folder. These two files are derived,
so parallel sessions never collide. Re-run after any task is accepted. Idempotent.
"""
import re, sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
MEM = ROOT / "memory"
MEM.mkdir(exist_ok=True)

CATEGORIES = [  # exactly as listed on the live Hub form (14), task 1, 2026-10-12
    "Companionship / Chat", "Learning / Research", "Health & Fitness", "Shopping",
    "Media Creation", "Work Productivity / SMB", "Entertainment", "Personal Productivity",
    "Emotional Support", "Finance", "Travel", "Relationships", "Legal / Civic", "Home Automation",
]
THIN = {"Companionship / Chat", "Legal / Civic", "Home Automation", "Shopping", "Entertainment", "Travel"}
GUIDE_REMOVED = {"Personal Productivity"}

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    fm, body = {}, m.group(2)
    cur_key = None
    for line in m.group(1).splitlines():
        line = line.split("  #")[0].rstrip()
        if not line.strip():
            continue
        if re.match(r"^\s{2,}\S", line) and cur_key:          # nested (scores:)
            k, _, v = line.strip().partition(":")
            fm.setdefault(cur_key, {})
            if isinstance(fm[cur_key], dict):
                fm[cur_key][k.strip()] = v.strip()
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        cur_key = k
        if v == "":
            fm[k] = {} if k == "scores" else ""
        elif v.startswith("[") and v.endswith("]"):
            fm[k] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        else:
            fm[k] = v.strip("'\"")
    return fm, body

def section(body, number):
    """Return the text of '## <number>. ...' up to the next '## ' heading (empty if absent)."""
    m = re.search(rf"^## {number}\.[^\n]*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""

def task_num(fm, path):
    try:
        return int(fm.get("task_number") or re.search(r"_task_(\d+)", path.parent.name).group(1))
    except Exception:
        return 0

def main():
    retros = []
    for p in sorted(TASKS.glob("*/RETROSPECTIVE.md")):
        fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        if not fm:
            continue
        retros.append((task_num(fm, p), fm, body, p))
    retros.sort(key=lambda r: r[0], reverse=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    # ---------- GLOBAL_RETROSPECTIVE ----------
    out = []
    A = out.append
    A("# GLOBAL RETROSPECTIVE — key points from every task (GENERATED)\n")
    A(f"> GENERATED {now} by tools/build_memory.py from tasks/*/RETROSPECTIVE.md. **Do not edit here** — edit the task's own RETROSPECTIVE.md and re-run. Newest first. Read this before designing any prompt or rationale.\n")
    A("## Index\n")
    A("| # | Task | Type | Status | Universe date | Category | Preference | Abs.Q | Scores (SB,C,St,Co,H,Cm,T,W) | Apps | Gates hit | QC iters | Accepted |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for n, fm, body, p in retros:
        sc = fm.get("scores", {}) or {}
        order = ["style_behavior_high","correctness_high","style","coherence","helpfulness","completeness","tone","warmth"]
        scores = ",".join(str(sc.get(k, "?") or "?") for k in order) if isinstance(sc, dict) else "?"
        apps = ", ".join(fm.get("apps_utilized", []) or []) or "none"
        gates = ", ".join(fm.get("qc_gates_hit", []) or []) or "—"
        A(f"| {n} | `{fm.get('task_id','')}` | {fm.get('task_type','new')} | {fm.get('status','')} | {fm.get('universe_date','')} | {fm.get('category','')} | {fm.get('preference','')} | {fm.get('absolute_quality','')} | {scores} | {apps} | {gates} | {fm.get('qc_iterations','')} | {fm.get('accepted_date','')} |")
    A("\n> Score columns: Style&behavior(high), Correctness(high), Style, Coherence, Helpfulness, Completeness, Tone, Warmth. 1=A sig · 2=A slight · 3=Tie · 4=B slight · 5=B sig.\n")
    skipped = [n for n, fm, _, _ in retros if fm.get("status") != "accepted"]
    if skipped:
        A(f"> In-progress / not-yet-accepted tasks (index only, bodies omitted until accepted): {', '.join(str(x) for x in skipped)}\n")
    for n, fm, body, p in retros:
        if fm.get("status") != "accepted":
            continue   # never leak template stubs from parallel in-progress sessions
        A("\n---\n")
        A(f"<!-- source: {p.relative_to(ROOT)} -->")
        A(body.strip() + "\n")
    (MEM / "GLOBAL_RETROSPECTIVE.md").write_text("\n".join(out) + "\n", encoding="utf-8")

    # ---------- NEXT_TASK_DIRECTIVES ----------
    d = []
    D = d.append
    D("# NEXT-TASK DIRECTIVES — read this FIRST in every new session (GENERATED)\n")
    D(f"> GENERATED {now} by tools/build_memory.py. Auto-promoted from each ACCEPTED task's RETROSPECTIVE §6 (new rules learned) and §8 (what the next task should do differently). Newest first, cumulative. **Do not edit here** — write in your task's RETROSPECTIVE and re-run `tools/build_memory.sh`. Every item below is a standing instruction until a later task supersedes it.\n")
    acc = [r for r in retros if r[1].get("status") == "accepted"]
    if not acc:
        D("_No accepted tasks yet._")
    for n, fm, body, p in acc:
        D(f"\n## From task {n} — {fm.get('category','')} · accepted {fm.get('accepted_date','')} · preference {fm.get('preference','')} · Abs.Q {fm.get('absolute_quality','')} · gates {', '.join(fm.get('qc_gates_hit', []) or []) or '—'}")
        s8 = section(body, 8); s6 = section(body, 6)
        if s8:
            D("\n**Do differently next time:**\n" + s8)
        if s6:
            D("\n**Rules learned (now standing):**\n" + s6)
        D(f"\n<sub>source: {p.relative_to(ROOT)}</sub>")
    # inherited directives from other fellows' archives (reference/<owner>/tasks/*/RETROSPECTIVE.md) — [generic] lines only
    REF = ROOT / "reference"
    inherited = []
    if REF.exists():
        for rp in sorted(REF.glob("*/tasks/*/RETROSPECTIVE.md")):
            rfm, rbody = parse_frontmatter(rp.read_text(encoding="utf-8"))
            if rfm.get("status") != "accepted":
                continue
            owner = rp.relative_to(REF).parts[0]
            lines = []
            for num in (8, 6):
                for ln in section(rbody, num).split("\n"):
                    if "[generic]" in ln:
                        lines.append(re.sub(r"^(\s*(?:\d+\.|-)\s+)\[generic\]\s*", r"\1", ln))
            if lines:
                inherited.append((owner, task_num(rfm, rp), rfm, lines))
    if inherited:
        D("\n---\n## Inherited from other fellows' archives ([generic] lines only — process, Hub/Hatch behaviour, scoring, QC)")
        D("> Persona-specific lines were filtered out. These are standing instructions too; the newest task of each owner appears first.")
        for owner, n, rfm, lines in sorted(inherited, key=lambda x: (x[0], -x[1])):
            D(f"\n### {owner} · task {n} — {rfm.get('category','')} · {rfm.get('preference','')} · Abs.Q {rfm.get('absolute_quality','')} · gates {', '.join(rfm.get('qc_gates_hit', []) or []) or '—'}")
            D("\n".join(lines))
    (MEM / "NEXT_TASK_DIRECTIVES.md").write_text("\n".join(d) + "\n", encoding="utf-8")

    # ---------- CATEGORY_TRACKER ----------
    # Rules (guide + Hub form): work the category Hub names; otherwise pick by goal and COVER THE RANGE —
    # a THIN category before any repeat; "choose a new one you haven't done before". The guide says nothing
    # about what to do once every category has been used once, so the deterministic policy is:
    #   Round 1: any still-open category (THIN first). Round 2+: least-recently-done category, THIN first.
    # Prompt reuse/paraphrase is forbidden ALWAYS (that rule never resets). Rework slots count as done.
    done = {}          # category -> list of (task_number, task_type)
    for n, fm, body, p in sorted(retros, key=lambda r: r[0]):
        if fm.get("status") == "accepted" and fm.get("category"):
            done.setdefault(fm["category"], []).append((n, fm.get("task_type", "new")))
    counts = {c: len(done.get(c, [])) for c in CATEGORIES}
    last_done = {c: max((n for n, _ in done[c]), default=0) for c in CATEGORIES if c in done}
    min_round = min(counts.values())                     # 0 while any category is still open
    current_round = min_round + 1
    # candidate ordering for the NEXT pick
    def key(c):
        return (counts[c],                               # fewest completions first
                0 if c in THIN else 1,                   # THIN first
                last_done.get(c, 0),                     # least recently done first
                1 if c in GUIDE_REMOVED else 0,          # Personal Productivity last
                CATEGORIES.index(c))
    order = sorted(CATEGORIES, key=key)
    next_picks = [c for c in order if c not in GUIDE_REMOVED][:3]
    t = []
    T = t.append
    T("# CATEGORY TRACKER — 14 Hub categories (GENERATED)\n")
    T(f"> GENERATED {now} by tools/build_memory.py from accepted tasks (rework slots count). Guide lists **13** categories; the live Hub form lists **14** (adds Personal Productivity, which the guide says is removed — avoid unless Hub names it).\n")
    T(f"**Current round: {current_round}.** " + ("Some categories are still open — pick an open one (THIN first) unless Hub names a category." if min_round == 0 else
      f"Every category has been done at least {min_round}×. The guide has no rule for this; policy = start round {current_round}: least-recently-done category, THIN first. Prompt reuse/paraphrase stays forbidden forever — the category may repeat, the prompt may not."))
    T(f"\n**NEXT PICK (deterministic, unless Hub names one):** 1. {next_picks[0]}  ·  2. {next_picks[1]}  ·  3. {next_picks[2]}\n")
    T("| Category | Times done | Status | Done in (task · type) | Priority / note |")
    T("|---|---|---|---|---|")
    for c in CATEGORIES:
        st = "open" if counts[c] == 0 else ("done" if counts[c] == min_round + 0 and min_round > 0 else ("done" if counts[c] > 0 else "open"))
        st = "open" if counts[c] == min_round else f"done ×{counts[c]}"
        note = []
        if c in THIN: note.append("**THIN — prefer**")
        if c in GUIDE_REMOVED: note.append("listed on Hub but guide says removed — avoid unless Hub names it")
        if c in next_picks: note.append(f"← next pick #{next_picks.index(c)+1}")
        donein = ", ".join(f"task {n} · {tt}" for n, tt in done.get(c, [])) or "—"
        T(f"| {c} | {counts[c]} | {st} | {donein} | {'; '.join(note) or '—'} |")
    acc_n = sum(1 for r in retros if r[1].get('status') == 'accepted')
    T(f"\nAccepted tasks: {acc_n} · Categories done at least once: {sum(1 for c in CATEGORIES if counts[c] > 0)}/14 · Round: {current_round}")
    (MEM / "CATEGORY_TRACKER.md").write_text("\n".join(t) + "\n", encoding="utf-8")

    print(f"built memory/NEXT_TASK_DIRECTIVES.md ({len(acc)} accepted), memory/GLOBAL_RETROSPECTIVE.md ({len(retros)} tasks), memory/CATEGORY_TRACKER.md ({sum(1 for c in CATEGORIES if counts[c] > 0)}/14 done, round {current_round}; next: {next_picks[0]})")

if __name__ == "__main__":
    main()

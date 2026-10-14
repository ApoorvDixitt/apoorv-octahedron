#!/usr/bin/env python3
"""
parse_transcript.py — draft FINAL_SUBMISSION.md from a saved Hub task transcript.

Usage:
    python3 tools/parse_transcript.py tasks/35e4f574ad46_task_N
        reads  tasks/<id>/transcript/hub_task_transcript.txt
        writes tasks/<id>/FINAL_SUBMISSION.md   (overwrites the stub; a filled-in previous version is backed up to .bak)

Layout rule (verified on task 1's transcript):
    <Label at line start>
    <English instructions, possibly with example values like 27b6b2b03e31_task_12>
    Anuvaad · Translation:
    <Hindi instructions>
    <VALUE = the LAST paragraph before the next line-start label>
The 8 dimension scores appear as a standalone digit line after each dimension header.
BEST-EFFORT: always verify by eye. Blank fields = not found.
KNOWN LIMITATION: the Task prompt is taken as the LAST paragraph before the "You MUST NOT re-use" block.
For a MULTI-TURN prompt (several user turns pasted as separate paragraphs) only the final turn is captured —
copy the earlier turns in by hand from the transcript.
"""
import re, sys
from pathlib import Path
from collections import Counter

# Line-start labels in Hub order (regex, key). Order matters only for slicing; we take LAST occurrence per key.
LABELS = [
    (r"^Session name\s*$",                                   "session_name"),
    (r"^Session ID\s*$",                                     "session_id"),
    (r"^Use case category\s*$",                              "category"),
    (r"^Apps utilized\s*$",                                  "apps"),
    (r"^Task prompt\s*$",                                    "prompt"),
    (r"^You MUST NOT re-use a similar or identical prompt",   "no_reuse"),
    (r"^In 2-4 sentences explain how your prompt relates",   "relates"),
    (r"^Paste the entire Response A conversation",           "response_a"),
    (r"^Paste the entire Response B conversation",           "response_b"),
    (r"^Trace A — full trace of Arm A",                      "trace_a"),
    (r"^Trace B — full trace of Arm B",                      "trace_b"),
    (r"^Preference\s*$",                                     "pref"),
    (r"^Absolute quality\s*$",                               "absq"),
    (r"^Score each dimension\s*$",                           "scores_hdr"),
    (r"^Style and behavior \(High level\)\s*$",              "s_sb"),
    (r"^Correctness \(High level\)\s*$",                     "s_c"),
    (r"^Style \(Granular\)\s*$",                             "s_st"),
    (r"^Coherence & writing quality \(Granular\)\s*$",       "s_co"),
    (r"^Helpfulness \(Granular\)\s*$",                       "s_h"),
    (r"^Completeness \(Granular\)\s*$",                      "s_cm"),
    (r"^Tone \(Granular\)\s*$",                              "s_t"),
    (r"^Warmth \(Granular\)\s*$",                            "s_w"),
    (r"^Required rationale\s*$",                             "rationale"),
    (r"^Attach screenshot of the scoring panel",             "shot1"),
    (r"^Notes\s*$",                                          "notes"),
    (r"^Screenshot confirmation\s*$",                        "shot2"),
    (r"^Confirm Hatch Session ID\s*$",                       "confirm_id"),
    (r"^Confirmation that you have checked and passed",      "attest"),
    (r"^Rate the quality of this task",                      "rate_hdr"),
    (r"^Quality Rating\s*$",                                 "quality_rating"),
    (r"^Justification\s*$",                                  "justification"),
]
UUID = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")
EXAMPLE_UUID = "2e6c6e89-82af-44b4-9870-186ac9e29bb9"
EXAMPLE_NAME = "27b6b2b03e31_task_12"
CATEGORIES = ["Companionship / Chat","Learning / Research","Health & Fitness","Shopping","Media Creation",
              "Work Productivity / SMB","Entertainment","Personal Productivity","Emotional Support","Finance",
              "Travel","Relationships","Legal / Civic","Home Automation"]
PREFS = ["A is significantly better","A is slightly better","B is slightly better","B is significantly better",
         "A significantly better","A slightly better","B slightly better","B significantly better"]

def paragraphs(seg):
    return [p.strip() for p in re.split(r"\n\s*\n", seg) if p.strip()]

def last_value(seg):
    """Value = last paragraph of the segment (after the Anuvaad block if present)."""
    i = seg.rfind("Anuvaad · Translation:")
    tail = seg[i:] if i >= 0 else seg
    ps = paragraphs(tail)
    # drop the Anuvaad header itself if it is its own paragraph
    ps = [p for p in ps if p != "Anuvaad · Translation:"]
    return ps[-1] if ps else ""

def main(task_dir):
    task_dir = Path(task_dir)
    src = task_dir / "transcript" / "hub_task_transcript.txt"
    if not src.exists():
        print(f"missing {src}"); sys.exit(1)
    text = src.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")

    # locate line-start labels → (line_no, key); keep LAST occurrence per key
    hits = []
    for ln, line in enumerate(lines):
        for rx, key in LABELS:
            if re.match(rx, line):
                hits.append((ln, key)); break
    last = {}
    for ln, key in hits:
        last[key] = ln
    bounds = sorted(ln for ln, _ in hits)

    def seg(key):
        if key not in last: return ""
        s = last[key]
        e = min([b for b in bounds if b > s] + [len(lines)])
        return "\n".join(lines[s+1:e])

    out = {}
    v = last_value(seg("session_name"))
    m = re.search(r"\b[0-9a-f]{6,}_task_\d+\b", v)
    out["session_name"] = m.group(0) if m and m.group(0) != EXAMPLE_NAME else ""
    # GUARD (task 3 incident): refuse to parse another task's transcript into this folder.
    if out["session_name"] and out["session_name"] != task_dir.name:
        bad = src.with_name(f"MISMATCH_{out['session_name']}_hub_task_transcript.txt")
        src.rename(bad)
        print(f"STOP: transcript belongs to session '{out['session_name']}', not '{task_dir.name}'. "
              f"Renamed to {bad.name}. Ask the operator for the correct Hub export. Nothing written.")
        sys.exit(2)
    ids = [u for u in UUID.findall(seg("session_id")) if u != EXAMPLE_UUID]
    out["session_id"] = ids[-1] if ids else ""
    cat_lines = [l.strip() for l in seg("category").split("\n") if l.strip() in CATEGORIES]
    out["category"] = cat_lines[-1] if cat_lines else ""
    out["apps"] = last_value(seg("apps"))
    out["prompt"] = last_value(seg("prompt"))
    out["relates"] = last_value(seg("relates"))
    for k in ("response_a", "response_b"):
        ps = paragraphs(seg(k).split("Anuvaad · Translation:")[-1])
        idx = next((i for i, p in enumerate(ps) if re.search(r"\b[A-Z]{3} \d{1,2}, \d{1,2}:\d{2} (AM|PM)\b", p)), None)
        out[k] = "\n\n".join(ps[idx:]) if idx is not None else (ps[-1] if ps else "")
    for k in ("trace_a", "trace_b"):
        s = seg(k); i = s.find("[User")
        out[k] = s[i:].strip() if i >= 0 else ""
    v = last_value(seg("pref"))
    out["pref"] = v if v in PREFS else ""
    v = last_value(seg("absq"))
    out["absq"] = v if v in ("Perfect", "Good", "Bad") else ""
    for k in ("s_sb","s_c","s_st","s_co","s_h","s_cm","s_t","s_w"):
        v = last_value(seg(k))
        out[k] = v if re.fullmatch(r"[1-5]", v) else ""
    ps = paragraphs(seg("rationale").split("Anuvaad · Translation:")[-1])
    idx = next((i for i, p in enumerate(ps) if p.lower().startswith("preference")), None)
    out["rationale"] = "\n\n".join(ps[idx:]) if idx is not None else ""
    out["notes"] = last_value(seg("notes"))
    ids = [u for u in UUID.findall(seg("confirm_id")) if u != EXAMPLE_UUID]
    out["confirm_id"] = ids[-1] if ids else ""
    v = last_value(seg("quality_rating")); out["quality_rating"] = v if re.fullmatch(r"[1-5]", v) else ""
    out["justification"] = last_value(seg("justification"))

    APP_RX = r"sheet|docs?\b|drive|gmail|calendar|gcal|contact|whatsapp|outlook|notion|photo|oura|hue|nutrition|health|instagram"
    def tool_summary(tr):
        calls = Counter(x.strip() for x in re.findall(r"\[Tool Call · ([^\]·]+?) ·", tr))
        persona = {k for k in calls if re.search(APP_RX, k, re.I)}
        # exec'd app CLIs count as invoking that app, even if the command errored (task 2: `exec philips-hue status` → 404)
        for cmd in re.findall(r'"command":\s*"((?:[^"\\]|\\.)*)"', tr):
            cmd = cmd.replace("\\n", " ").replace("\\t", " ")   # un-escape embedded newlines/tabs before tokenising
            for tok in re.findall(r"\b([a-z][a-z0-9-]*)\b", cmd.lower()):
                if re.search(APP_RX, tok) and tok not in ("ls", "echo", "true"):
                    persona.add(f"exec:{tok}")
        head = ("tool calls: " + ", ".join(f"{k}×{n}" for k, n in calls.items())) if calls else "no tool calls"
        return head + ("\n- persona-app calls: " + ", ".join(sorted(persona)) + "  → Apps utilized should list these apps (even if the call errored)" if persona
                       else "\n- persona-app calls: NONE (internal memory/filesystem only) → Apps utilized = none")
    out["trace_a_sum"] = tool_summary(out["trace_a"]); out["trace_b_sum"] = tool_summary(out["trace_b"])

    tid = task_dir.name
    md = f"""# FINAL_SUBMISSION — {tid}

> Drafted by `tools/parse_transcript.py` from `transcript/hub_task_transcript.txt`. Verified by eye: ☐ (tick and delete this line once checked). Blank = not found by the parser.

| Hub field | Value |
|---|---|
| Task language | Hindi (Singapore) |
| Session name | `{out['session_name']}` |
| Session ID (comparison UUID) | `{out['session_id']}` |
| Universe / persona | Hindi (Singapore) · Arjun Mehra |
| Use case category | {out['category']} |
| Apps utilized (as submitted) | {out['apps']} |
| Preference | {out['pref']} |
| Absolute quality (preferred arm) | {out['absq']} |
| Style and behavior (High level) | {out['s_sb']} |
| Correctness (High level) | {out['s_c']} |
| Style (Granular) | {out['s_st']} |
| Coherence & writing quality (Granular) | {out['s_co']} |
| Helpfulness (Granular) | {out['s_h']} |
| Completeness (Granular) | {out['s_cm']} |
| Tone (Granular) | {out['s_t']} |
| Warmth (Granular) | {out['s_w']} |
| Notes | {out['notes']} |
| Confirm Hatch Session ID | `{out['confirm_id']}` |
| Task quality rating given (1–5) | {out['quality_rating']} — {out['justification']} |

## Task prompt (verbatim)
```
{out['prompt']}
```

## "How the prompt relates to the universe" (verbatim)
```
{out['relates']}
```

## Response A (verbatim incl. timestamps)
```
{out['response_a']}
```

## Response B (verbatim incl. timestamps)
```
{out['response_b']}
```

## Required rationale (verbatim, accepted)
```
{out['rationale']}
```

## Trace A — summary (full trace in transcript/)
- {out['trace_a_sum']}

## Trace B — summary
- {out['trace_b_sum']}

## Screenshots
- `screenshots/hatch_scoring_panel_completed.png`
- `screenshots/hatch_both_arms_responses.png`
"""
    dst = task_dir / "FINAL_SUBMISSION.md"
    if dst.exists() and "Verified by eye: ☑" in dst.read_text(encoding="utf-8"):
        # Never clobber a human-verified record. Write a side draft for comparison instead.
        dst = task_dir / "FINAL_SUBMISSION.draft.md"
        print("FINAL_SUBMISSION.md is already verified (☑) — writing FINAL_SUBMISSION.draft.md instead; diff and discard.")
    dst.write_text(md, encoding="utf-8")
    blanks = [k for k, v in out.items() if not v and k not in ("justification",)]
    print(f"wrote {dst}")
    print("fields not found (fill by hand): " + (", ".join(blanks) if blanks else "none"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    main(sys.argv[1])

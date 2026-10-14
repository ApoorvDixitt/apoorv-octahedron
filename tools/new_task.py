#!/usr/bin/env python3
"""
new_task.py N — scaffold tasks/<alias>_task_N/ from templates. Cross-platform (Windows / macOS / Linux).

    python3 tools/new_task.py 4          (bash users may also use tools/new_task.sh 4)

The alias is read from memory/GLOBAL_MEMORY.md (line "| Chat alias | `xxxxxxxxxxxx` |"), so one
copy of this tool works for every fellow's setup without editing. Never overwrites an existing folder.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def alias():
    gm = (ROOT / "memory" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")
    m = re.search(r"\|\s*Chat alias\s*\|\s*`([0-9a-z]+)`", gm)
    if not m:
        sys.exit("Could not find '| Chat alias | `...` |' in memory/GLOBAL_MEMORY.md — set it first.")
    return m.group(1)

def main():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        sys.exit("usage: python3 tools/new_task.py <task_number>")
    n = int(sys.argv[1]); a = alias()
    tid = f"{a}_task_{n}"
    d = ROOT / "tasks" / tid
    if d.exists():
        print(f"exists: {d}  (not overwriting). Open TASK_MEMORY.md to resume."); return
    (d / "transcript").mkdir(parents=True); (d / "screenshots").mkdir()
    for f in ("TASK_MEMORY", "RETROSPECTIVE", "FINAL_SUBMISSION"):
        src = (ROOT / "templates" / f"{f}.template.md").read_text(encoding="utf-8")
        src = re.sub(r"\b[0-9a-f]{6,}_task_N\b", tid, src).replace("task_number: N", f"task_number: {n}")
        (d / f"{f}.md").write_text(src, encoding="utf-8")
    (d / "transcript" / "README.md").write_text(
        f"Put the Hub task transcript here after acceptance as: hub_task_transcript.txt\nThen run:  python3 tools/parse_transcript.py tasks/{tid}\n", encoding="utf-8")
    (d / "screenshots" / "README.md").write_text(
        "After Submit preference + End comparison in Hatch, save:\n- hatch_scoring_panel_completed.png   (Annotations → Preference → the completed panel)\n- hatch_both_arms_responses.png       (both arms visible, text legible)\n- hatch_annotation_row_submitted.png  (optional: Annotations list row with the WHY text)\nIntake rule: if the operator leaves them in ~/Downloads, the agent opens each one, renames it by\nwhat it shows, MOVES it here (never copies) and confirms nothing is left in Downloads.\n", encoding="utf-8")
    print(f"created {d}\n  TASK_MEMORY.md  RETROSPECTIVE.md  FINAL_SUBMISSION.md  transcript/  screenshots/")
    ct = ROOT / "memory" / "CATEGORY_TRACKER.md"
    if ct.exists():
        print("Category guidance (from memory/CATEGORY_TRACKER.md):")
        for line in ct.read_text(encoding="utf-8").splitlines():
            if line.startswith("**Current round") or line.startswith("**NEXT PICK"):
                print("  " + line)
    else:
        print("  (run python3 tools/build_memory.py to generate CATEGORY_TRACKER.md)")

if __name__ == "__main__":
    main()

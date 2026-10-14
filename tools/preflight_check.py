#!/usr/bin/env python3
"""
preflight_check.py — catch the mistakes Hub QC caught in task 1, BEFORE you paste.

Usage:
  python3 tools/preflight_check.py prompt    <file-or-'-'>            # prompt hygiene
  python3 tools/preflight_check.py rationale <file-or-'-'> [--scores SB,C,St,Co,H,Cm,T,W --pref "A slightly better" --absq Bad]

Checks (prompt):
  - em/en dashes (Hub ADVISORY-P2 rejects them)
  - English-only heuristic (prompt must be romanized Hindi+English)
  - unsupported-action phrases (Outlook draft, WhatsApp new number, merge contacts, SMS)
  - vague date words (today/this week/recent) — reminder to bound to records

Checks (rationale):
  - every one of the 8 dimensions is mentioned
  - number words (two..ten) flagged for manual recount (AR-05)
  - "only A / only B / neither / B doesn't" style claims flagged for cross-check (AR-09)
  - each Tie score has a reason clause containing 'Tie' / 'tie' near the dimension (AR-07)
  - Absolute Quality 'Bad' requires a sentence naming the preferred arm's own failure (AR-11)
  - consistency: preference direction vs number of dimensions favouring that arm (AR-02 / SUB-V1V2)
  - em dashes
"""
import sys, re, argparse

DIMS = {
    "style_behavior_high": [r"style and behavi"],
    "correctness_high":    [r"correctness"],
    "style":               [r"\bstyle \(granular\)", r"\bstyle:", r"\bstyle \("],
    "coherence":           [r"coherence"],
    "helpfulness":         [r"helpfulness"],
    "completeness":        [r"completeness"],
    "tone":                [r"\btone\b"],
    "warmth":              [r"warmth"],
}
NUMWORDS = r"\b(two|three|four|five|six|seven|eight|nine|ten|both|all eight|all 8)\b"
CLAIMS = r"\b(only [AB]\b|neither\b|[AB] (does|did) not|[AB] doesn'?t|[AB] never|unlike [AB]\b|whereas [AB]\b|while [AB]\b)"

def read(src):
    return sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()

def warn(msgs, ok, text, info=False):
    """ok=True → 'OK', ok=False → '!!' (blocks), info=True → 'i ' (review by eye, never blocks)."""
    msgs.append(("i  " if info else ("OK " if ok else "!! ")) + text)

def check_prompt(t, today=None):
    m = []
    warn(m, "—" not in t and "–" not in t, "no em/en dashes" if ("—" not in t and "–" not in t) else "EM/EN DASH present — Hub will reject (ADVISORY-P2). Replace with comma/full stop.")
    # Language check is locale-agnostic and informational: the prompt must be in the PERSONA's language/script
    # (see guide/MULTILINGUAL_RULES.md). Heuristic: share of common-English function words among Latin tokens.
    latin = re.findall(r"[A-Za-z]+", t)
    eng = {"the","and","is","are","to","of","for","my","me","please","can","you","check","list","with","what","how","should","this","that","it"}
    eng_n = sum(1 for w in latin if w.lower() in eng)
    non_latin = len(re.findall(r"[^\x00-\x7F]", t))
    share = (eng_n / len(latin)) if latin else 0
    if non_latin > 0 and len(latin) < 5:
        warn(m, True, f"prompt is in a non-Latin script ({non_latin} chars) — correct for own-script locales (ja_jp, zh_sg, bn_sg mostly); confirm against MULTILINGUAL_RULES.md", info=True)
    else:
        warn(m, True, f"English function-word share among Latin tokens: {share:.0%} — if your locale writes Latin-script code-mixed (hi/bn-in/ta-in/…), >35% suggests an English-heavy prompt; rewrite in the persona's voice", info=share > 0.35)
    bad = re.findall(r"(outlook\s+draft|new\s+number|merge\s+contacts|sms|text message|\bdraft.*outlook)", t.lower())
    warn(m, not bad, "no unsupported-action phrases" if not bad else f"unsupported action phrases: {bad}")
    vague = re.findall(r"\b(aaj|today|this week|is hafte|recent|latest|next week|agle hafte|upcoming)\b", t.lower())
    warn(m, True, f"date words — confirm they are anchored to THIS task's modal date ({today or 'pass --today \"Sat 3 Oct 2026\"'}): {vague or 'none'}", info=bool(vague))
    warn(m, len(t.split()) <= 120, f"length {len(t.split())} words" + ("" if len(t.split()) <= 120 else " — long; tighten"))
    return m

def check_rationale(t, scores=None, pref=None, absq=None):
    m = []
    low = t.lower()
    warn(m, "—" not in t, "no em dashes" if "—" not in t else "em dash present — remove")
    missing = [d for d, pats in DIMS.items() if not any(re.search(p, low) for p in pats)]
    warn(m, not missing, "all 8 dimensions mentioned" if not missing else f"dimensions NOT mentioned: {missing} (Hub wants 1–2 sentences each, incl. ties)")
    sents = re.split(r"(?<=[.!?])\s+", t.strip())
    warn(m, len(sents) >= 4, f"{len(sents)} sentences (min 4)")
    nums = re.findall(NUMWORDS, low)
    warn(m, True, f"number words — RECOUNT literally against both responses (AR-05): {sorted(set(nums)) or 'none'}", info=bool(nums))
    claims = re.findall(CLAIMS, low)
    warn(m, True, f"exclusive claims — CROSS-CHECK each in the other arm (AR-09): {len(claims)} found" + (f" → {[c[0] if isinstance(c, tuple) else c for c in claims][:8]}" if claims else ""), info=bool(claims))
    ties = len(re.findall(r"\btie\b", low))
    if scores:
        n_tie = sum(1 for s in scores if s == 3)
        warn(m, ties >= n_tie, f"{n_tie} Tie scores vs {ties} 'Tie' mentions in rationale" + ("" if ties >= n_tie else " — every Tie needs its own reason clause (AR-07)"))
        a_fav = sum(1 for s in scores if s in (1, 2)); b_fav = sum(1 for s in scores if s in (4, 5))
        if pref:
            pa = pref.strip().upper().startswith("A")
            ok = (a_fav > 0 and pa) or (b_fav > 0 and not pa)
            warn(m, ok, f"preference '{pref}' vs dims favouring A={a_fav}, B={b_fav}" + ("" if ok else " — NOTHING favours the preferred arm (AR-02/SUB-V1V2). Something must be better somewhere."))
            one_way = (a_fav == 8) or (b_fav == 8)
            warn(m, not one_way, "not all eight forced one way" if not one_way else "ALL EIGHT point one way — ADVISORY-U1 will fire; re-check independence")
        if n_tie == 8:
            warn(m, False, "all eight are Tie but Hub forbids overall Tie — keep ≥1 quotable directional dimension")
    if absq and absq.lower() == "bad":
        has_fail = re.search(r"(failed|never opened|did not|didn'?t|left .* unanswered|wrong|missing|unanswered|invented|fabricat)", low)
        warn(m, bool(has_fail), "Absolute Bad: failure of the preferred arm is named" if has_fail else "Absolute Bad but no sentence names what the PREFERRED arm itself got wrong (AR-11)")
    quotes = len(re.findall(r'"[^"]{4,}"', t)) + len(re.findall(r"“[^”]{4,}”", t))
    warn(m, quotes >= 2, f"{quotes} quoted phrases (Hub wants the Hindi you judge quoted and explained)")
    return m

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["prompt", "rationale"])
    ap.add_argument("src")
    ap.add_argument("--scores", help="8 comma-separated ints: SB,C,St,Co,H,Cm,T,W")
    ap.add_argument("--pref")
    ap.add_argument("--absq")
    ap.add_argument("--today", help='universe date from this session\'s Hatch modal, e.g. "Sat 3 Oct 2026"')
    a = ap.parse_args()
    t = read(a.src)
    if a.kind == "prompt":
        res = check_prompt(t, a.today)
    else:
        scores = [int(x) for x in a.scores.split(",")] if a.scores else None
        res = check_rationale(t, scores, a.pref, a.absq)
    print("\n".join(res))
    n_info = sum(1 for r in res if r.startswith("i "))
    if n_info:
        print(f"\n{n_info} item(s) marked 'i' need a human recount/cross-check before pasting.")
    sys.exit(1 if any(r.startswith("!!") for r in res) else 0)

if __name__ == "__main__":
    main()

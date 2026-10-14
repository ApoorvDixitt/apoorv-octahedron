#!/usr/bin/env bash
# build_memory.sh — regenerate memory/GLOBAL_RETROSPECTIVE.md and memory/CATEGORY_TRACKER.md
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/tools/build_memory.py"

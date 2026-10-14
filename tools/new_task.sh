#!/usr/bin/env bash
# new_task.sh N — bash wrapper for tools/new_task.py (macOS/Linux). Windows: python tools/new_task.py N
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec python3 "$ROOT/tools/new_task.py" "$@"

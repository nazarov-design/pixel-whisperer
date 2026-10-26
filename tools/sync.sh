#!/bin/sh
# Copy the shared annotate.py into every skill so each skill folder stands alone.
set -e
cd "$(dirname "$0")/.."
for d in skills/*/scripts; do cp shared/annotate.py "$d/annotate.py"; done
echo "synced annotate.py → $(ls -d skills/*/scripts | tr '\n' ' ')"

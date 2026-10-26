#!/bin/sh
# Build one zip per skill for claude.ai upload (Settings > Capabilities > Skills).
set -e
cd "$(dirname "$0")/.."
tools/sync.sh
rm -rf dist && mkdir -p dist
for d in skills/*/; do
  name=$(basename "$d")
  (cd skills && zip -qr "../dist/$name.zip" "$name" -x '*/__pycache__/*' '*.DS_Store')
  echo "dist/$name.zip  $(du -h "dist/$name.zip" | cut -f1)"
done

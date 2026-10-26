#!/bin/sh
# Re-generate examples/*/output*.md and overlay images with the current skills.
# Each example runs in a fresh scratch folder (isolated from user settings).
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
TMP="${TMPDIR:-/tmp}/pw-examples"; rm -rf "$TMP"; mkdir -p "$TMP"
RUN="$REPO/tools/run_claude.sh"

fd() { # dir slug what
  d="$REPO/examples/feedback-decoder/$1"; w="$TMP/$1"; mkdir -p "$w"; cp "$d/design.png" "$w/"
  { echo "New client feedback on $3 (design.png in this folder). Project slug: $2."; echo; sed '1d' "$d/input.md"; } > "$w.prompt"
  "$RUN" "$w" "$w.prompt" with "$d/output.md"
  cp "$w/.feedback-decoder/work/overlay.png" "$d/overlay.png" 2>/dev/null || echo "no overlay for $1"
  cp "$w/.feedback-decoder/$2.md" "$d/ledger-after.md" 2>/dev/null || true
}
dc() { # dir image prompt-file [journal-seed]
  d="$REPO/examples/desk-crit/$1"; w="$TMP/$1"; mkdir -p "$w/.desk-crit"; cp "$d/$2" "$w/"
  [ -n "$4" ] && cp "$d/$4" "$w/.desk-crit/student.md"
  "$RUN" "$w" "$d/$3" with "$d/output-${2%.png}.md"
  cp "$w/.desk-crit/work/overlay.png" "$d/overlay-${2%.png}.png" 2>/dev/null || echo "no overlay for $1"
  cp "$w/.desk-crit/work/compare.png" "$d/compare.png" 2>/dev/null || true
  cp "$w/.desk-crit/student.md" "$d/journal-after.md" 2>/dev/null || true
}

fd 01-saas-landing flowdesk-landing "the landing page" &
fd 02-coffee-shop coffee-site "the coffee shop homepage" &
fd 03-fintech-app-ru savings-app "the app screens" &
dc 02-intermediate-dashboard dashboard.png prompt.md journal-before.md &
dc 03-advanced-mobile onboarding.png prompt.md &
# poster: two sessions in the same folder, so the journal carries over
( dc 01-beginner-poster poster-v1.png prompt-v1.md
  cp "$REPO/examples/desk-crit/01-beginner-poster/poster-v2.png" "$TMP/01-beginner-poster/"
  "$RUN" "$TMP/01-beginner-poster" "$REPO/examples/desk-crit/01-beginner-poster/prompt-v2.md" with \
    "$REPO/examples/desk-crit/01-beginner-poster/output-poster-v2.md"
  d="$REPO/examples/desk-crit/01-beginner-poster"; w="$TMP/01-beginner-poster"
  cp "$w/.desk-crit/work/overlay.png" "$d/overlay-poster-v2.png" 2>/dev/null || true
  cp "$w/.desk-crit/work/compare.png" "$d/compare.png" 2>/dev/null || true
  cp "$w/.desk-crit/student.md" "$d/journal-after.md" ) &
wait
echo "examples regenerated"

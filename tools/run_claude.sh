#!/bin/sh
# Run one prompt through Claude Code headlessly, in an isolated setup.
# Usage: tools/run_claude.sh WORKDIR PROMPT_FILE with|without OUT_FILE [MODEL]
# "with" loads only this repo's plugin; "without" loads no plugins. User-level
# skills, plugins, MCP servers and CLAUDE.md are excluded in both cases.
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
WORKDIR="$1"; PROMPT="$2"; MODE="$3"; OUT="$4"; MODEL="${5:-sonnet}"
[ -x "$REPO/.venv/bin/python" ] && PATH="$REPO/.venv/bin:$PATH" && export PATH
PLUGIN=""
[ "$MODE" = "with" ] && PLUGIN="--plugin-dir $REPO"
cd "$WORKDIR"
claude -p "$(cat "$PROMPT")" --model "$MODEL" --setting-sources project --strict-mcp-config \
  $PLUGIN --allowedTools "Bash Read Write Edit Glob Grep Skill" > "$OUT" 2>&1

#!/bin/bash
# Setup VP MCP server config for Claude Code
#
# The MCP server is the Visual Paradigm plugin itself: it starts with VP and listens on
# http://localhost:<port>/mcp (streamable HTTP, default port 2026). No Docker needed.
#
# Usage: ./vp-mcp-setup.sh [port]

set -e

PORT="${1:-2026}"
PROJECT_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
MCP_CONFIG="${PROJECT_ROOT}/.mcp.json"
URL="http://localhost:${PORT}/mcp"

echo "=== VP MCP Setup ==="
echo "Project root: ${PROJECT_ROOT}"
echo "MCP config:   ${MCP_CONFIG}"
echo "Server URL:   ${URL}"
echo

if command -v python3 &>/dev/null; then
    # Create .mcp.json, or merge the entry into an existing one. An old SSE entry
    # (type "sse", url .../sse) is rewritten: plugin >= 1.32.8 only serves /mcp.
    python3 - "$MCP_CONFIG" "$URL" <<'PY'
import json, os, sys

path, url = sys.argv[1], sys.argv[2]
cfg = {}
existed = os.path.isfile(path)
if existed:
    with open(path) as f:
        cfg = json.load(f)
servers = cfg.setdefault("mcpServers", {})
entry = servers.get("visual-paradigm")
if entry is None:
    servers["visual-paradigm"] = {"type": "http", "url": url}
    action = "Added visual-paradigm to existing .mcp.json" if existed else "Created .mcp.json with visual-paradigm config"
elif entry.get("type") != "http" or not entry.get("url", "").endswith("/mcp"):
    entry["type"] = "http"
    entry["url"] = url
    action = "Fixed visual-paradigm entry (type http, " + url + ")"
else:
    action = None
if action:
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2)
        f.write("\n")
    print("[OK] " + action + ".")
else:
    print("[OK] visual-paradigm already configured.")
    print("     To change the port, edit .mcp.json manually.")
PY
else
    echo "[WARN] python3 not found. Add this to .mcp.json manually:"
    echo
    echo '  "visual-paradigm": {'
    echo '    "type": "http",'
    echo "    \"url\": \"${URL}\""
    echo '  }'
    exit 1
fi

echo
echo "=== Setup Complete ==="
echo
echo "Next steps:"
echo "  1. Open Visual Paradigm (plugin installed: cd visual-paradigm-mcp-plugin && ./run install,"
echo "     then fully quit and reopen VP). The MCP server starts with VP on port ${PORT}."
echo "  2. Verify connection:    .claude/skills/cnpm-vp/scripts/vp-mcp-verify.sh ${PORT}"
echo "  3. Restart Claude Code to pick up the new MCP config"
echo
echo "Alternative (user-scope, no .mcp.json):"
echo "  claude mcp add --transport http --scope user visual-paradigm ${URL}"
echo "  codex mcp add visual-paradigm --url ${URL}"
echo
echo "Or install the plugin (MCP config + generic skill) from the marketplace:"
echo "  Claude Code: /plugin marketplace add thanhtrnnn/vp-mcp, then /plugin install visual-paradigm@visual-paradigm-mcp"
echo "  Codex:       codex plugin marketplace add thanhtrnnn/vp-mcp && codex plugin add visual-paradigm@visual-paradigm-mcp"

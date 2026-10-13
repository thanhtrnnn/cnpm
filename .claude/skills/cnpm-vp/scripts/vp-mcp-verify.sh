#!/bin/bash
# Verify VP MCP server is running and responsive
#
# The server is the Visual Paradigm plugin (starts with VP). Checks: port/SSE, MCP initialize
# (server version), tool count (117 expected for plugin >= 1.32.3), .mcp.json entry.
#
# Usage: ./vp-mcp-verify.sh [port]

PORT="${1:-2026}"
BASE_URL="http://localhost:${PORT}"
EXPECTED_TOOLS=117

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ok() { echo -e "${GREEN}[OK]${NC} $1"; }
fail() { echo -e "${RED}[FAIL]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }

echo "=== VP MCP Server Verification ==="
echo "Target: ${BASE_URL}"
echo

# 1. Check if port is open / SSE endpoint answers.
# /sse is a never-ending event stream, so cap the request time; curl then exits with 28
# (timeout) after it has already printed the status code, which is fine.
if command -v curl &>/dev/null; then
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 --max-time 2 "${BASE_URL}/sse" 2>/dev/null)
    HTTP_CODE="${HTTP_CODE:-000}"
    if [[ "$HTTP_CODE" == "200" ]] || [[ "$HTTP_CODE" == "204" ]]; then
        ok "SSE endpoint reachable (HTTP ${HTTP_CODE})"
    elif [[ "$HTTP_CODE" == "000" ]]; then
        fail "Cannot connect to ${BASE_URL} - Visual Paradigm not running, or the MCP plugin is not installed/loaded?"
        echo
        echo "Open Visual Paradigm (the plugin starts the server). If the plugin is not installed:"
        echo "  cd visual-paradigm-mcp-plugin && ./run install   # then fully quit and reopen VP"
        exit 1
    else
        warn "SSE endpoint returned HTTP ${HTTP_CODE} (may still work)"
    fi
else
    # Fallback: check port with nc
    if nc -z localhost "$PORT" 2>/dev/null; then
        ok "Port ${PORT} is open"
    else
        fail "Port ${PORT} is not open - Visual Paradigm not running?"
        exit 1
    fi
fi

# 2. Check MCP protocol: initialize + tools/list. Without a sessionId the server answers
# in the HTTP response body.
echo
echo "Checking MCP protocol..."

MCP_INIT='{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"vp-mcp-verify","version":"1.0"}}}'
MCP_LIST='{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'

if command -v curl &>/dev/null; then
    RESPONSE=$(curl -s --connect-timeout 5 --max-time 10 -X POST \
        -H "Content-Type: application/json" \
        -d "$MCP_INIT" \
        "${BASE_URL}/mcp/messages" 2>/dev/null)

    if [[ -n "$RESPONSE" ]]; then
        ok "MCP server responded to initialize"
        if command -v python3 &>/dev/null; then
            INFO=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin).get('result',{}).get('serverInfo',{}); print(d.get('name','unknown'), d.get('version','unknown'))" 2>/dev/null)
            [[ -n "$INFO" ]] && echo "  Server: ${INFO}"
        fi
    else
        warn "No response from MCP initialize (server may use a different transport path)"
    fi

    if command -v python3 &>/dev/null; then
        COUNT=$(curl -s --connect-timeout 5 --max-time 10 -X POST \
            -H "Content-Type: application/json" \
            -d "$MCP_LIST" \
            "${BASE_URL}/mcp/messages" 2>/dev/null \
            | python3 -c "import sys,json; print(len(json.load(sys.stdin).get('result',{}).get('tools',[])))" 2>/dev/null)
        if [[ "$COUNT" =~ ^[0-9]+$ ]] && [[ "$COUNT" -gt 0 ]]; then
            if [[ "$COUNT" -ge "$EXPECTED_TOOLS" ]]; then
                ok "tools/list: ${COUNT} tools"
            else
                warn "tools/list: ${COUNT} tools (expected ${EXPECTED_TOOLS}) - VP is running an older plugin build; reinstall and fully quit/reopen VP"
            fi
        else
            warn "Could not read tools/list"
        fi
    fi
fi

# 3. Check .mcp.json exists and the entry is a remote (sse) server
echo
echo "Checking Claude Code config..."
PROJECT_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
MCP_CONFIG="${PROJECT_ROOT}/.mcp.json"

if [[ -f "$MCP_CONFIG" ]]; then
    if grep -q "visual-paradigm" "$MCP_CONFIG" 2>/dev/null; then
        if grep -q '"sse"' "$MCP_CONFIG" 2>/dev/null; then
            ok ".mcp.json has visual-paradigm entry (type sse)"
        else
            warn ".mcp.json has a visual-paradigm entry without \"type\": \"sse\""
            echo "  Run: .claude/skills/cnpm-vp/scripts/vp-mcp-setup.sh"
        fi
    else
        warn ".mcp.json exists but no visual-paradigm entry"
        echo "  Run: .claude/skills/cnpm-vp/scripts/vp-mcp-setup.sh"
    fi
else
    warn ".mcp.json not found at ${MCP_CONFIG} (fine if visual-paradigm is configured user-scope: claude mcp list)"
    echo "  Otherwise run: .claude/skills/cnpm-vp/scripts/vp-mcp-setup.sh"
fi

echo
echo "=== Verification Complete ==="

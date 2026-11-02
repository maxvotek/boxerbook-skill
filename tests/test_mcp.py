"""Live checks of the Boxerbook MCP server the plugin connects to, and that the
skill's cheat-sheet (references/api.md) documents every tool it exposes.

  python3 -m unittest discover -s tests -v
"""
import json
import unittest
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MCP_URL = json.loads((ROOT / ".mcp.json").read_text())["mcpServers"]["boxerbook"]["url"]


def rpc(method, params=None):
    req = urllib.request.Request(MCP_URL, data=json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}).encode(), headers={
        "content-type": "application/json", "accept": "application/json, text/event-stream",
        "user-agent": "boxerbook-skill-tests/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode()
    if raw.lstrip().startswith(("event:", "data:")):
        raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
    return json.loads(raw)["result"]


class McpLive(unittest.TestCase):
    def test_initialize(self):
        r = rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                               "clientInfo": {"name": "tests", "version": "1"}})
        self.assertEqual(r["serverInfo"]["name"], "boxerbook")

    def test_tools_documented(self):
        names = {t["name"] for t in rpc("tools/list")["tools"]}
        self.assertTrue({"boxer", "bout", "boxing_schedule", "boxing_results", "rankings"} <= names)
        api_md = (ROOT / "skills" / "boxing" / "references" / "api.md").read_text()
        missing = [n for n in names if f"`{n}`" not in api_md]
        self.assertEqual(missing, [], "tools missing from references/api.md")

    def test_tool_call(self):
        r = rpc("tools/call", {"name": "boxer", "arguments": {"query": "Usyk", "lang": "es"}})
        self.assertFalse(r.get("isError"))
        self.assertIn("/es/boxeadores/", r["structuredContent"]["url"])


if __name__ == "__main__":
    unittest.main()

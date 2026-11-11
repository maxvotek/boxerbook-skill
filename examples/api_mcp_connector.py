#!/usr/bin/env python3
"""Use the boxing skill from the Claude API: SKILL.md as the system prompt,
Boxerbook's remote MCP server through the API's MCP connector. No tool loop to
write: the API calls the Boxerbook tools itself.

  pip install anthropic
  ANTHROPIC_API_KEY=... python examples/api_mcp_connector.py "Who won Canelo's last fight?"
"""
import sys
import os
from pathlib import Path

import anthropic

skill = (Path(os.environ.get("SKILL_REPO") or Path(__file__).resolve().parent.parent.parent / "boxerbook-skill") / "skills" / "boxing" / "SKILL.md").read_text()
question = " ".join(sys.argv[1:]) or "Who won Canelo's last fight and how?"

client = anthropic.Anthropic()
response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=8000,
    betas=["mcp-client-2025-11-20"],
    system="You have the Boxerbook MCP tools. Follow this skill:\n\n" + skill,
    mcp_servers=[{"type": "url", "url": "https://mcp.boxerbook.com/mcp", "name": "boxerbook"}],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "boxerbook"}],
    messages=[{"role": "user", "content": question}],
)
for block in response.content:
    if block.type == "mcp_tool_use":
        print(f"[tool] {block.name} {block.input}", file=sys.stderr)
print("".join(b.text for b in response.content if b.type == "text"))

#!/usr/bin/env python3
"""Behavioural evals for the boxing skill, run through the Anthropic Messages API.

The model gets the skill exactly as a skill-aware client would load it
(SKILL.md as the active skill, references readable on demand through a
`read_file` tool) and a real tool-use loop against live Boxerbook data:

  --mode mcp   tools = the Boxerbook MCP server's tools, proxied over HTTP
  --mode rest  tools = a `run_helper` tool that runs scripts/boxerbook.py
               (the path used in Claude.ai code execution / no MCP)

Each answer is graded by an LLM judge (with the tool results, so it can check
grounding) plus deterministic checks. Transcripts go to evals/transcripts/.

  ANTHROPIC_API_KEY=... python evals/run_evals.py --mode mcp [--only id1,id2]
Requires: pip install anthropic
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
import os
from pathlib import Path

import anthropic

ROOT = Path(os.environ.get("SKILL_REPO") or Path(__file__).resolve().parent.parent.parent / "boxerbook-skill").resolve()  # the plugin repo checkout
SKILL_DIR = ROOT / "skills" / "boxing"
OUT = Path(__file__).resolve().parent / "transcripts"
MCP_URL = "https://mcp.boxerbook.com/mcp"
MODEL = "claude-opus-5-5"
JUDGE = "claude-sonnet-5-5"
PRICES = {"claude-opus-5-5": (4.0, 20.0, 0.20, 5.0), "claude-sonnet-5-5": (2.0, 10.0, 0.20, 2.5)}
MAX_TURNS = 12
MAX_RESULT_CHARS = 60000

client = anthropic.Anthropic(max_retries=4)
spend = {"usd": 0.0}


def cost(model, usage):
    pin, pout, pread, pwrite = PRICES[model]
    u = usage
    c = (u.input_tokens * pin + u.output_tokens * pout
         + (getattr(u, "cache_read_input_tokens", 0) or 0) * pread
         + (getattr(u, "cache_creation_input_tokens", 0) or 0) * pwrite) / 1e6
    spend["usd"] += c
    return c


# ---------------------------------------------------------------- MCP proxy
def mcp(method, params=None):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}).encode()
    req = urllib.request.Request(MCP_URL, data=body, headers={
        "content-type": "application/json",
        "accept": "application/json, text/event-stream",
        "user-agent": "boxerbook-skill-evals/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode()
    if raw.lstrip().startswith("event:") or raw.lstrip().startswith("data:"):
        raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
    msg = json.loads(raw)
    if "error" in msg:
        raise RuntimeError(msg["error"])
    return msg["result"]


def mcp_tools():
    tools = []
    for t in mcp("tools/list")["tools"]:
        tools.append({"name": t["name"], "description": t["description"],
                      "input_schema": t["inputSchema"]})
    return tools


def call_mcp_tool(name, args):
    res = mcp("tools/call", {"name": name, "arguments": args})
    text = "\n".join(c.get("text", "") for c in res.get("content", []) if c.get("type") == "text")
    return text, bool(res.get("isError"))


# ---------------------------------------------------------------- REST helper
HELPER_TOOL = {
    "name": "run_helper",
    "description": ("Run the skill's helper script: python3 scripts/boxerbook.py <args...>. "
                    "Pass the arguments as a list, e.g. [\"boxer\", \"Canelo\"] or "
                    "[\"schedule\", \"--when\", \"weekend\"]. Returns stdout (JSON) or the error."),
    "input_schema": {"type": "object", "properties": {
        "args": {"type": "array", "items": {"type": "string"}}}, "required": ["args"]},
}


def run_helper(args):
    p = subprocess.run([sys.executable, str(Path(__file__).resolve().parent.parent / "helper" / "boxerbook.py"), *args],
                       capture_output=True, text=True, timeout=120)
    return (p.stdout or p.stderr).strip(), p.returncode != 0


READ_TOOL = {
    "name": "read_file",
    "description": "Read a file of the active skill, by path relative to the skill folder (e.g. references/api.md).",
    "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]},
}


def read_file(path):
    p = (SKILL_DIR / path).resolve()
    if SKILL_DIR not in p.parents and p != SKILL_DIR:
        return "error: outside the skill folder", True
    if not p.is_file():
        return f"error: no such file {path}", True
    return p.read_text(encoding="utf-8"), False


def system_prompt(mode):
    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%A %d %B %Y, %H:%M UTC")
    surface = ("The Boxerbook MCP server is connected: its tools are available to you."
               if mode == "mcp" else
               "No MCP server is connected. You can run code: use the run_helper tool to run "
               "the skill's scripts/boxerbook.py (network access to boxerbook.com is allowed).")
    return (f"You are Claude, a helpful assistant. Current date and time: {now}. "
            "The user's time zone is unknown.\n\n"
            f"{surface} Use read_file to open the skill's reference files when the skill tells you to.\n\n"
            "The following skill has been loaded because it matches the user's request. "
            "Follow it.\n\n<skill name=\"boxing\" path=\"skills/boxing\">\n" + skill + "\n</skill>")


def run_case(case, mode, tools):
    sys_blocks = [{"type": "text", "text": system_prompt(mode), "cache_control": {"type": "ephemeral"}}]
    messages = [{"role": "user", "content": case["prompt"]}]
    trace, usd = [], 0.0
    for turn in range(MAX_TURNS):
        resp = client.messages.create(model=MODEL, max_tokens=16000, system=sys_blocks,
                                      tools=tools, messages=messages,
                                      output_config={"effort": "medium"})
        usd += cost(MODEL, resp.usage)
        messages.append({"role": "assistant", "content": resp.content})
        uses = [b for b in resp.content if b.type == "tool_use"]
        for b in resp.content:
            if b.type == "text" and b.text.strip():
                trace.append({"type": "text", "text": b.text})
        if resp.stop_reason != "tool_use" or not uses:
            break
        results = []
        for u in uses:
            try:
                if u.name == "read_file":
                    out, is_err = read_file(u.input.get("path", ""))
                elif u.name == "run_helper":
                    out, is_err = run_helper(u.input.get("args", []))
                else:
                    out, is_err = call_mcp_tool(u.name, u.input)
            except Exception as e:  # report tool failures to the model
                out, is_err = f"error: {e}", True
            out = out[:MAX_RESULT_CHARS]
            trace.append({"type": "tool", "name": u.name, "input": u.input, "error": is_err, "output": out})
            results.append({"type": "tool_result", "tool_use_id": u.id, "content": out, "is_error": is_err})
        messages.append({"role": "user", "content": results})
    final = "\n\n".join(b.text for b in resp.content if b.type == "text").strip()
    return final, trace, usd


# ---------------------------------------------------------------- grading
JUDGE_PROMPT = """You grade an AI assistant's answer to a boxing question. The assistant had to
follow a skill whose rules are: every record/result/date/number must come from the Boxerbook
tool results (never from memory); cite boxerbook.com URLs for boxers/bouts/cards mentioned;
write fight dates explicitly; handle name ambiguity; never give betting tips (probabilities only,
with a not-betting-advice line); answer in the user's language.
Boxerbook documents that start_utc is the start of the whole card (main events start later), so
saying "the card starts at X UTC, the main event later" is grounded. Values derived from tool fields
(age from birth date, inches from cm, side b probability = 1 - p_a, percentages) count as grounded.
Records attached to a bout (a.record, b.record, record, opponent_record) are, per Boxerbook's
documentation, the W-L-D going INTO that bout, so "X came in 29-0-1, his first loss" is grounded.
The skill itself tells the assistant that main events usually start 2-4 hours after the card start;
that general statement is allowed. The current date is in the assistant's system prompt and tool outputs carry as_of, so 'as of <today>' is grounded. Country codes may be written as country names (GB -> UK/Great Britain).
In Russian, "супертяжёлый вес" is the standard name of the professional heavyweight division.
If a tool output is cut off and you cannot verify a fact, do not mark it ungrounded for that alone.

USER PROMPT ({lang}):
{prompt}

WHAT A GOOD ANSWER DOES:
{expect}

TOOL CALLS AND RESULTS (ground truth available to the assistant):
{tools}

FINAL ANSWER:
{answer}

Grade each criterion true/false (use true for "not applicable"):
- grounded: every specific fact (records, results, dates, opponents, titles, rankings, numbers,
  heights, probabilities) is supported by the tool results above. General boxing knowledge
  (rules, what UD means) is fine. Any invented or contradicted fact = false.
- cited: the boxers/bouts/cards it names are linked to boxerbook.com URLs (at least the main
  ones) and Boxerbook is credited. If nothing could be found, a link to boxerbook.com search
  or no link is acceptable.
- dates_explicit: fights it mentions carry explicit dates (not only "last Saturday").
- no_betting_tips: no recommendation of what/how much to bet; if probabilities or odds are
  given there is a not-betting-advice line.
- language: the answer is in the user's language ({lang}).
- task: it does what the "good answer" description says (main facts right, ambiguity handled,
  admits missing data).
Reply with JSON only: {{"grounded": bool, "cited": bool, "dates_explicit": bool,
"no_betting_tips": bool, "language": bool, "task": bool, "notes": "<one or two sentences>"}}"""

CRITERIA = ["grounded", "cited", "dates_explicit", "no_betting_tips", "language", "task"]


def judge(case, answer, trace):
    tools_txt = []
    for t in trace:
        if t["type"] == "tool" and t["name"] != "read_file":
            tools_txt.append(f"- {t['name']}({json.dumps(t['input'], ensure_ascii=False)}) ->\n{t['output'][:60000]}")
    prompt = JUDGE_PROMPT.format(lang=case["lang"], prompt=case["prompt"], expect=case["expect"],
                                 tools="\n".join(tools_txt) or "(no tool calls)", answer=answer)
    resp = client.messages.create(model=JUDGE, max_tokens=4000,
                                  messages=[{"role": "user", "content": prompt}],
                                  output_config={"effort": "low"})
    cost(JUDGE, resp.usage)
    text = "".join(b.text for b in resp.content if b.type == "text")
    m = re.search(r"\{.*\}", text, re.S)
    try:
        return json.loads(m.group(0))
    except Exception:
        return {c: False for c in CRITERIA} | {"notes": "judge output unparsable: " + text[:200]}


def lang_ok(lang, answer):
    letters = re.findall(r"[A-Za-zА-Яа-яЁёÁÉÍÓÚÑáéíóúñ¿¡]", answer)
    cyr = sum(1 for ch in letters if re.match(r"[А-Яа-яЁё]", ch))
    if lang == "ru":
        return cyr > 0.4 * max(1, len(letters))
    if lang == "es":
        return cyr == 0 and bool(re.search(r"\b(el|la|de|que|en|y|los|por|con|una?)\b", answer, re.I)) \
            and len(re.findall(r"\b(the|and|with|was)\b", answer, re.I)) < 5
    return cyr < 0.1 * max(1, len(letters))


def deterministic(case, answer, trace):
    tool_calls = [t for t in trace if t["type"] == "tool" and t["name"] != "read_file"]
    return {
        "used_data_tool": bool(tool_calls),
        "has_boxerbook_link": "boxerbook.com" in answer,
        "lang_heuristic": lang_ok(case["lang"], answer),
        "utm_tagged": "utm_source=claude-skill" in answer,
        "read_reference": any(t["type"] == "tool" and t["name"] == "read_file" for t in trace),
    }


def write_transcript(case, mode, answer, trace, grade, det, usd):
    OUT.mkdir(parents=True, exist_ok=True)
    lines = [f"# {case['id']} ({mode})", "", f"**Prompt ({case['lang']}):** {case['prompt']}", "",
             f"**Expected:** {case['expect']}", "", "## Trace", ""]
    for t in trace:
        if t["type"] == "tool":
            out = t["output"]
            short = out if len(out) < 1500 else out[:1500] + f"\n... [{len(out)} chars]"
            lines += [f"**tool** `{t['name']}` `{json.dumps(t['input'], ensure_ascii=False)}`"
                      + (" (error)" if t["error"] else ""), "", "```", short, "```", ""]
        else:
            lines += ["**assistant (interim)**", "", t["text"], ""]
    lines += ["## Final answer", "", answer, "", "## Grade", "", "```json",
              json.dumps({"judge": grade, "checks": det, "usd": round(usd, 4)}, ensure_ascii=False, indent=2),
              "```", ""]
    (OUT / f"{mode}-{case['id']}.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["mcp", "rest"], default="mcp")
    ap.add_argument("--only", default="")
    ap.add_argument("--budget", type=float, default=8.0, help="stop when spend passes this (USD)")
    a = ap.parse_args()
    cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    if a.only:
        keep = set(a.only.split(","))
        cases = [c for c in cases if c["id"] in keep]
    tools = (mcp_tools() if a.mode == "mcp" else [HELPER_TOOL]) + [READ_TOOL]
    tools[-1]["cache_control"] = {"type": "ephemeral"}
    rows = []
    for c in cases:
        if spend["usd"] > a.budget:
            print("budget reached, stopping"); break
        t0 = time.time()
        answer, trace, usd = run_case(c, a.mode, tools)
        grade = judge(c, answer, trace)
        det = deterministic(c, answer, trace)
        passed = all(grade.get(k) for k in CRITERIA) and det["used_data_tool"] and det["lang_heuristic"]
        write_transcript(c, a.mode, answer, trace, grade, det, usd)
        row = {"id": c["id"], "lang": c["lang"], "mode": a.mode, "pass": passed,
               **{k: grade.get(k) for k in CRITERIA}, **det, "notes": grade.get("notes", ""),
               "tool_calls": sum(1 for t in trace if t["type"] == "tool"), "usd": round(usd, 4),
               "secs": round(time.time() - t0)}
        rows.append(row)
        print(f"{'PASS' if passed else 'FAIL'} {c['id']:<22} ${usd:.3f} {row['notes'][:110]}", flush=True)
    res_path = ROOT / "evals" / f"results-{a.mode}.json"
    old = {}
    if res_path.exists() and a.only:
        old = {r["id"]: r for r in json.loads(res_path.read_text())}
    for r in rows:
        old[r["id"]] = r
    res_path.write_text(json.dumps(list(old.values()) if a.only else rows, ensure_ascii=False, indent=1))
    print(f"\n{sum(r['pass'] for r in rows)}/{len(rows)} passed · total spend ${spend['usd']:.2f}")


if __name__ == "__main__":
    main()

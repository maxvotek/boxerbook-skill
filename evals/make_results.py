#!/usr/bin/env python3
"""Render evals/RESULTS.md from results-mcp.json, results-rest.json and results-trigger.json."""
import json
from datetime import date
from pathlib import Path

E = Path(__file__).resolve().parent
CRIT = ["grounded", "cited", "dates_explicit", "no_betting_tips", "language", "task"]
mark = lambda v: "✅" if v else "❌"


def table(rows, mode):
    out = [f"| Case | Lang | Pass | {' | '.join(CRIT)} | Link | utm | Tool calls | $ | Transcript |",
           "|" + "---|" * (len(CRIT) + 8)]
    for r in rows:
        out.append(f"| {r['id']} | {r['lang']} | {mark(r['pass'])} | "
                   + " | ".join(mark(r[c]) for c in CRIT)
                   + f" | {mark(r['has_boxerbook_link'])} | {mark(r['utm_tagged'])} | {r['tool_calls']} | {r['usd']:.3f} | "
                   f"[md](transcripts/{mode}-{r['id']}.md) |")
    return out


def main():
    cases = {c["id"]: c for c in json.loads((E / "cases.json").read_text())}
    lines = ["# Eval results", "",
             f"Generated {date.today().isoformat()} by `evals/make_results.py`. Model under test: "
             "`claude-opus-5-5` (effort medium); judge: `claude-sonnet-5-5`, which sees every tool "
             "result so it can check grounding. Live Boxerbook data.", "",
             "A case passes when the judge marks all six criteria true **and** the answer used a "
             "data tool and passes the language heuristic.", ""]
    total_usd = 0
    for mode, title in [("mcp", "MCP path (Boxerbook MCP tools, as in the Claude Code plugin / connector)"),
                        ("rest", "REST path (scripts/boxerbook.py, as in claude.ai code execution)")]:
        p = E / f"results-{mode}.json"
        if not p.exists():
            continue
        rows = sorted(json.loads(p.read_text()), key=lambda r: list(cases).index(r["id"]))
        total_usd += sum(r["usd"] for r in rows)
        lines += [f"## {title}: {sum(r['pass'] for r in rows)}/{len(rows)} pass", ""] + table(rows, mode) + [""]
    t = E / "results-trigger.json"
    if t.exists():
        tr = json.loads(t.read_text())
        total_usd += tr["usd"]
        lines += [f"## Triggering (`evals/trigger_test.py`, {tr['model']})", "",
                  "The model sees only skill names + descriptions: `boxing` and 10 realistic neighbours "
                  "(mma-stats, sports-scores, fitness-coach incl. boxing workouts, shopping-deals incl. "
                  "Boxing Day, data-viz incl. box plots, pdf, xlsx, travel-planner, movie-guide, news-brief).", "",
                  f"- Boxing prompts that picked `boxing`: **{tr['should_trigger']}**",
                  f"- Near-miss prompts that did not pick `boxing`: **{tr['should_not_trigger']}**", "",
                  "| Prompt | Should trigger | Picked | OK |", "|---|---|---|---|"]
        lines += [f"| {r['prompt']} | {'yes' if r['should_trigger'] else 'no'} | `{r['picked']}` | {mark(r['ok'])} |"
                  for r in tr["rows"]]
        lines.append("")
    lines += ["## What the evals changed in the skill", "",
              "Failures seen during development and the fix made to SKILL.md:", "",
              "| Failure | Fix |", "|---|---|",
              "| Mentioned pre-fight odds without a not-betting-advice line | Rule 6: any answer that shows a forecast or odds ends with the disclaimer; don't volunteer odds |",
              "| \"Perdió su primera pelea\" (first fight) instead of first loss | Precise record wording |",
              "| Unsupported judgement (\"weaker opposition\") in a preview | Tie every comparative claim to a fetched field |",
              "| Background from memory (\"twin brothers\", \"Arlington, Texas\", who held which belt, full names) | Rule 1 lists \"harmless\" background as forbidden; places as returned |",
              "| Self-counted totals (\"15 cards\" when there were 16, \"four title fights\") | Quote only totals a tool returned |",
              "| Quoted the catalog size written in SKILL.md (\"about 30,000 boxers\"), which can go stale | Numbers removed from SKILL.md; live size via `status` |",
              "| Judge false positives (records going in, card vs main-event start, Russian \"супертяжёлый\", truncated tool output) | Judge prompt given the documented field semantics; tool output passed in full |",
              "", "History: full runs during development scored 13/15 then 12/15 (MCP) and 12/15, 13/15 (REST); "
              "each failure above led to one change in SKILL.md. The last full run scored 14/15 (MCP) and 15/15 (REST); "
              "the one MCP failure (catalog size) was fixed and that case re-run. LLM answers vary between runs, so "
              "re-run the suite after every change to the skill text.",
              "", f"Spend for the runs on this page: about ${total_usd:.2f}.", ""]
    (E / "RESULTS.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote evals/RESULTS.md")


if __name__ == "__main__":
    main()

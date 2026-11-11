#!/usr/bin/env python3
"""Skill-triggering test: does the model pick the boxing skill from its
name + description alone, among realistic neighbouring skills, for boxing
prompts, and leave it alone for near-miss prompts?

  ANTHROPIC_API_KEY=... python evals/trigger_test.py
"""
import json
import re
import os
from pathlib import Path

import anthropic

ROOT = Path(os.environ.get("SKILL_REPO") or Path(__file__).resolve().parent.parent.parent / "boxerbook-skill").resolve()  # the plugin repo checkout
MODEL = "claude-opus-5-5"

skill_md = (ROOT / "skills" / "boxing" / "SKILL.md").read_text(encoding="utf-8")
BOXING_DESC = re.search(r"^description: (.*)$", skill_md, re.M).group(1)

SKILLS = {
    "boxing": BOXING_DESC,
    "mma-stats": "Fighter records, event results and rankings for MMA (UFC, Bellator, PFL, ONE). Use for questions about mixed martial arts fighters, UFC cards and MMA rankings.",
    "sports-scores": "Live scores, results, standings and schedules for football (soccer), NFL, NBA, MLB, NHL and tennis. Use when the user asks about a game, a team, a league table or a player's stats in these sports.",
    "fitness-coach": "Designs workout plans and training sessions: strength, running, HIIT, boxing and kickboxing fitness workouts, heavy-bag and shadowboxing routines, mobility. Use when the user wants an exercise plan or technique tips for training.",
    "pdf": "Use this skill whenever the user wants to do anything with PDF files: read, extract text or tables, merge, split, fill forms, create PDFs.",
    "xlsx": "Use this skill when a spreadsheet is the primary input or output: open, edit, clean or create .xlsx/.csv files, formulas, charts in spreadsheets.",
    "data-viz": "Creates charts and plots (matplotlib, plotly, d3): bar charts, box plots, histograms, dashboards. Use whenever the user wants a chart or visualization.",
    "travel-planner": "Plans trips: itineraries, flights, hotels, visas, local tips. Use when the user is planning travel or asks about a destination.",
    "shopping-deals": "Finds deals and sales: Black Friday, Boxing Day, Prime Day, coupons, price comparisons. Use when the user wants to buy something at a good price.",
    "movie-guide": "Recommends films, series and documentaries, with where to stream them, cast and reviews. Use for what-to-watch questions about movies and TV.",
    "news-brief": "Summarises today's news by topic or region. Use when the user asks what is happening in the news.",
}

SHOULD = [
    "did canelo win last night?",
    "When is Usyk's next fight?",
    "What boxing is on tonight and where can I watch it in the UK?",
    "Inoue vs Nakatani prediction",
    "How tall is Tyson Fury and what's his reach?",
    "Who's the best pound for pound boxer right now?",
    "What does a split decision mean in boxing and who won the last big one?",
    "Write a tweet about last night's boxing results",
    "¿Quién es el campeón pesado del CMB?",
    "¿Canelo es zurdo?",
    "Cartelera de box de este fin de semana",
    "Кто сейчас абсолютный чемпион в тяжёлом весе?",
    "Какой рекорд у Бивола?",
    "Jake Paul record?",
]
SHOULD_NOT = [
    "Who won the UFC main event on Saturday?",
    "Give me a 30-minute heavy bag workout for beginners",
    "Best Boxing Day sales in London this year?",
    "Make a box plot of salaries by department in matplotlib",
    "NBA scores from last night",
    "Plan a 10-day trip to Thailand with a Muay Thai camp",
    "How do I pack boxes efficiently for a move?",
    "Recommend a good documentary to watch tonight",
    "Rankings de la UFC peso ligero",
    "Как поставить удар в кикбоксинге для тренировки?",
]

SYSTEM = ("You are Claude. You have these skills; each is loaded only when it matches the user's "
          "request, judged from its description:\n<available_skills>\n"
          + "\n".join(f"<skill><name>{n}</name><description>{d}</description></skill>" for n, d in SKILLS.items())
          + "\n</available_skills>\nFor the user's message, reply with only the name of the one skill you "
          "would load first, or `none` if no skill fits. No other words.")


def main():
    client = anthropic.Anthropic(max_retries=4)
    rows, cost = [], 0.0
    for prompt, want in [(p, True) for p in SHOULD] + [(p, False) for p in SHOULD_NOT]:
        r = client.messages.create(model=MODEL, max_tokens=2000, system=SYSTEM,
                                   messages=[{"role": "user", "content": prompt}],
                                   output_config={"effort": "low"})
        cost += (r.usage.input_tokens * 4 + r.usage.output_tokens * 20) / 1e6
        pick = "".join(b.text for b in r.content if b.type == "text").strip().strip("`").lower()
        ok = (pick == "boxing") == want
        rows.append({"prompt": prompt, "should_trigger": want, "picked": pick, "ok": ok})
        print(f"{'OK  ' if ok else 'MISS'} want={'boxing' if want else 'not boxing':<11} got={pick:<15} {prompt}")
    tp = sum(r["ok"] for r in rows if r["should_trigger"])
    tn = sum(r["ok"] for r in rows if not r["should_trigger"])
    summary = {"should_trigger": f"{tp}/{len(SHOULD)}", "should_not_trigger": f"{tn}/{len(SHOULD_NOT)}",
               "usd": round(cost, 3), "model": MODEL, "rows": rows}
    (Path(__file__).resolve().parent / "results-trigger.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))
    print(f"\ntriggered {tp}/{len(SHOULD)} · correctly ignored {tn}/{len(SHOULD_NOT)} · ${cost:.3f}")


if __name__ == "__main__":
    main()

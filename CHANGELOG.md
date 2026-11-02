# Changelog

## 1.0.0 — 2026-11-02
- `boxing` skill: strict grounding workflow (MCP → helper script → REST), citation,
  explicit dates, name disambiguation, no betting tips, answers in the user's language.
- References: API/MCP cheat-sheet, divisions and codes, belts and publishers,
  scoring, en/es/ru glossary, eight output templates.
- `scripts/boxerbook.py`: stdlib-only REST helper (search, boxer, bouts, next, h2h,
  bout, event, schedule, results, rankings, status).
- Claude Code plugin `boxing` in marketplace `boxerbook`, bundling the Boxerbook
  remote MCP server.
- Validator, live tests, behavioural evals (MCP and REST paths) and a trigger test.

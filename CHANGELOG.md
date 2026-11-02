# Changelog

## Unreleased
- Helper: read timeouts, bad JSON and HTTP-date `Retry-After` end as JSON errors,
  not tracebacks; long `Retry-After` is reported instead of retried early; utm tag
  only on https boxerbook.com site links; `bouts` and `h2h` return `other_matches`.
- References: vacant titles and `champion_flag` values, upset test per winning
  side, women's division count, missed-weight rules vary, REST host vs `/v1`
  paths, boxer links and source line in templates, Russian stance names.

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

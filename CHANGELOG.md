# Changelog

## 1.0.2 — 2026-11-24 (prepared; not yet submitted)
- Skill and plugin descriptions name the fight-model use case: per-bout features
  (weigh-ins, ages, layoffs, ratings), the Boxerbook win probability and the market
  odds consensus with its opening line; keywords for sports analytics, win
  probability and fight prediction.
- Answer shape: for model and data questions, name the `bout` fields and say what is
  not offered (no bulk downloads; scorecards only on the bout pages), with a link to
  boxerbook.com/boxing-data-for-models.
- Data terms: the Boxerbook data terms (ODbL no longer applies to new data since 2026-11-03).
- `docs/chatgpt-plugin.json`: the ChatGPT plugin manifest prepared as 1.0.2 (same texts).

## 1.0.1 — 2026-11-11
- Plugin repo holds only Markdown, JSON and images (Claude plugin directory policy):
  the REST helper, validator, zip builder, tests, evals and the API example moved to
  the [`dev-tools` branch](https://github.com/maxvotek/boxerbook-skill/tree/dev-tools). Without MCP the skill now calls `boxerbook.com/v1`
  directly, with recipes in `references/api.md`. README hero is a PNG.
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

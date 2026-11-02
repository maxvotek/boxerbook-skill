# Contributing

Thanks for helping make Claude better at boxing.

## What helps most

- **Bad answers.** If the skill gave a wrong, uncited or invented answer, open an
  issue with the prompt, the surface (Claude Code, claude.ai, API) and the answer.
  Better: add it as a case to `evals/cases.json`.
- **Data errors** (a wrong record or result) belong to Boxerbook, not this repo:
  use the "report a discrepancy" link on the bout page at
  [boxerbook.com](https://boxerbook.com/?utm_source=claude-skill) or write to
  info@boxerbook.com.
- **New templates or languages** (`skills/boxing/references/`), as long as they
  keep SKILL.md short: new knowledge goes into a reference file that SKILL.md
  points to.

## Ground rules for the skill

1. Never add facts that go stale (who the champion is, a boxer's record) to the
   skill text. The skill fetches; it does not remember.
2. Keep `SKILL.md` under 500 lines and the frontmatter to the portable fields
   (`name`, `description`, `license`, `compatibility`, `metadata`).
3. The helper script stays Python standard library only.

## Before you open a PR

```bash
python3 scripts/validate.py                 # schema checks (skill, plugin, marketplace, MCP)
python3 -m unittest discover -s tests -v    # live API + MCP tests
python3 scripts/build_zip.py                # claude.ai bundle
# optional, costs a few dollars of API usage:
ANTHROPIC_API_KEY=... python evals/run_evals.py --mode mcp
ANTHROPIC_API_KEY=... python evals/trigger_test.py
```

Bump `version` in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
and the SKILL.md `metadata` together, and add a line to `CHANGELOG.md`.

Code and docs are MIT. By contributing you agree your contribution is MIT
licensed. Boxerbook data stays ODbL.

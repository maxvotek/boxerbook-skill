# boxerbook-skill: dev-tools branch

Development tools for [boxerbook-skill](https://github.com/maxvotek/boxerbook-skill)
(the Boxerbook boxing skill and plugin for Claude). They live on this branch because
the Claude plugin directory accepts only Markdown, JSON and images in the plugin itself.

```
helper/boxerbook.py   stdlib-only REST helper for boxerbook.com/v1 (search, boxer, bouts, next, h2h,
                      bout, event, schedule, results, rankings, status); used by the REST-path evals
scripts/validate.py   schema checks: SKILL.md frontmatter, plugin + marketplace manifests, .mcp.json
scripts/build_zip.py  claude.ai bundle -> dist/boxing-skill.zip (boxing/SKILL.md at the zip root)
tests/                live tests of the helper and the MCP server
evals/                behavioural evals (MCP and REST paths), trigger test, transcripts, results
examples/             Claude API + MCP connector example
```

From a clone of `main`: `git worktree add ../boxerbook-skill-dev dev-tools`, then in
`../boxerbook-skill-dev` (or anywhere, with `SKILL_REPO=/path/to/main/checkout`):

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build_zip.py
ANTHROPIC_API_KEY=... python evals/run_evals.py --mode mcp
ANTHROPIC_API_KEY=... python evals/trigger_test.py
```

MIT. Boxerbook data is ODbL, attribution "Boxerbook".

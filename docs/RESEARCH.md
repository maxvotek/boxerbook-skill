# Research notes: what makes a great skill (and a starred skill repo)

Researched 1 Nov 2026. Sources: anthropics/skills (pdf, docx, mcp-builder,
skill-creator), obra/superpowers, the awesome lists, the top results of
`gh search repos "claude skills" / "SKILL.md" --sort stars`, the Agent Skills
spec (agentskills.io/specification), platform.claude.com skill docs and
best practices, code.claude.com plugin / marketplace / skills references.

## Stars at the time of research

| Repo | Stars | What it is |
|---|---|---|
| obra/superpowers | 310.7k | workflow skills + own marketplace |
| anthropics/skills | 186.4k | official examples, repo is its own marketplace |
| addyosmani/agent-skills | 112.6k | engineering skills, `npx skills add` first |
| Leonxlnx/taste-skill | 108.0k | one focused design skill |
| pbakaus/impeccable | 99.6k | one focused skill, one-line install |
| ComposioHQ/awesome-claude-skills | 78.5k | list |
| coreyhaines31/marketingskills | 57.9k | domain skills (marketing), claude.ai zips |
| hesreallyhim/awesome-claude-code | 57.1k | list (issue form only) |
| K-Dense-AI/scientific-agent-skills | 55.7k | domain skills (science), 26 badges |
| VoltAgent/awesome-agent-skills | 36.7k | list |
| travisvn/awesome-claude-skills | 15.7k | list (>= 10 stars, no AI-written PRs) |

Pattern: stars go to repos that do **one job** for a recognisable domain or
author; plain "marketplace" catalogs rarely pass 1.5k.

## Spec facts we built against

- SKILL.md frontmatter, portable subset (claude.ai upload, Skills API and
  Claude Code all accept): `name`, `description`, `license`, `compatibility`,
  `metadata`, `allowed-tools`. Any other key is a hard error on claude.ai.
  -> we use only `name`, `description`, `license`, `compatibility`, `metadata`.
- `name`: 1-64 chars, `[a-z0-9-]`, no leading/trailing/double hyphen, equal to
  the folder name, no `anthropic`/`claude`. -> `boxing`.
- `description`: <= 1024 chars, no XML tags, third person, says what + when.
  Claude Code truncates description + when_to_use at 1,536 chars.
- Body < 500 lines (~5k tokens); references one level deep; a TOC on any
  reference file > 100 lines. -> SKILL.md ~140 lines, api.md has a TOC.
- Plugin: `.claude-plugin/plugin.json` (only `name` required; validate warns
  without version/description/author; directory blocks without license),
  components at the plugin root (`skills/`, `.mcp.json`). HTTP MCP servers:
  `{"type": "http", "url": ...}` (a url without type is an error).
- Marketplace: `.claude-plugin/marketplace.json` with `name`, `owner.name`,
  `plugins[{name, source}]`; reserved names (claude-*, anthropic-*, official
  look-alikes, ...) avoided -> marketplace `boxerbook`, plugin `boxing`.
- Skills API: container has **no network access**. A live-data skill on the
  API must pair the skill with the MCP connector (`mcp_servers`), which is
  what our README documents.
- claude.ai upload: zip whose root is the skill folder (`boxing/SKILL.md`).

## Patterns adopted (and where they came from)

1. **The description is the trigger, written "pushy"** with literal
   trigger words, boxer names and non-English keywords (skill-creator:
   skills under-trigger; pdf/docx front-load literal triggers).
2. **Negative scope** in the description ("not for MMA/UFC") to avoid
   collisions (docx "Do NOT use for ...").
3. **SKILL.md as a table of contents** with conditional pointers: "read
   api.md before your first call", templates "when one fits" (pdf FORMS.md
   pointer, mcp-builder "Load during phase N").
4. **One default path + escape hatch**: MCP if connected, else the helper
   script, else raw REST, else say so (best practices: one default, not a
   menu).
5. **Scripts that solve, not defer**: `boxerbook.py` handles retries, 429
   `Retry-After`, name -> id resolution, head-to-head pagination, trimming of
   bulky fields and clear errors, stdlib only (best practices; superpowers
   ships runnable helpers next to skills).
6. **Explicit dependencies**: "python3 stdlib only; allow boxerbook.com in
   claude.ai code execution" (best practices: state dependencies).
7. **Hard rules phrased as a short numbered "Iron Law" list** for the things
   that must never slip (no invented records, cite, no betting tips),
   explained with the why elsewhere (superpowers discipline skills vs
   skill-creator "explain the why": we use rules only for safety-critical
   points).
8. **No time-sensitive facts in the skill**: the skill never states who the
   champion is; it always fetches (best practices: avoid time-sensitive info).
   Template examples are labelled as dated illustrations.
9. **Templates for structured output** (best practices template pattern;
   Composio template): fighter card, tale of the tape, fight night, recap,
   rankings, forecast, upset, social post.
10. **Evals first, with and without triggers**: 12+ behavioural prompts and a
    trigger test with near-miss distractors (skill-creator: 8-10 should
    trigger, 8-10 near misses should not).
11. **Repo = its own marketplace** with `source: "./"` (anthropics/skills,
    superpowers) so install is two lines.
12. **Full plugin metadata** (version, author, homepage, repository, license,
    keywords) to pass `claude plugin validate` and the directory checklist.
13. **Portable frontmatter only**, so the same folder uploads to claude.ai,
    the Skills API and installs in Claude Code.
14. **Single focused skill instead of several sub-skills.** Sibling skills
    with overlapping triggers ("fight preview" vs "boxing") compete; the
    leaders that do one domain well (taste-skill, impeccable) ship one skill.
    Sub-workflows live as templates instead.
15. **Supporting material inside the skill folder** (travisvn prefers skills
    with more than a SKILL.md): references/ + scripts/.

## README patterns adopted

- One-line value proposition, then install in the first screen
  (impeccable, addyosmani).
- Install matrix for every surface: Claude Code plugin, `npx skills add`
  (skills.sh CLI, used by marketingskills, K-Dense, addyosmani), claude.ai zip,
  API (skill + MCP connector), any MCP client.
- Badge row (license, data licence, MCP, Agent Skills standard), a few,
  not 26.
- Example prompts and real worked transcripts (prompt-master "Full example").
- "Why" section, data attribution, contributing, changelog.
- Many repo topics (agent-skills, claude-skills, claude-code-plugin,
  skill-md, mcp, boxing, sports-data) feed the directory crawlers.
- GIFs are rare among the leaders; a static hero image + transcripts suffice.

## Distribution facts (details in LAUNCH.md)

- anthropics/skills does **not** merge community skills (last 30 merged PRs
  are all staff); don't spend effort there.
- Anthropic directory: submit at claude.ai/directory/manage (public repo,
  README >= 40 words, license, no reserved name) -> appears in
  anthropics/claude-plugins-community.
- skills.sh ranks by `npx skills add` telemetry; skillsmp crawls GitHub
  (needs ~2 stars); claudemarketplaces.com crawls + submit form;
  claude-plugins.dev indexes public marketplaces.
- Awesome lists have gates: travisvn >= 10 stars and no AI-written PRs;
  hesreallyhim issue form by a human, >= 14 days old or >= 100 stars;
  VoltAgent wants existing usage; ComposioHQ slow but open.

# en-charlo-ambiguous (mcp)

**Prompt (en):** What's Charlo's record?

**Expected:** Recognises the name is ambiguous (Jermell Charlo and Jermall Charlo are different boxers); either asks which one or gives both clearly separated, each with record and link. Must not merge them.

## Trace

**tool** `search_boxers` `{"q": "Charlo"}`

```
Source: [Boxerbook](https://boxerbook.com/search?q=Charlo)

Boxers matching "Charlo", best first: 3.

- [Jermell Charlo](https://boxerbook.com/boxers/jermell-charlo-q6182393) · US · 35-2-1 · id 16098 · slug jermell-charlo-q6182393
- [Jermall Charlo](https://boxerbook.com/boxers/jermall-charlo-q19864206) · US · Super middleweight · 36-0-0 · id 7810 · slug jermall-charlo-q19864206
- [Marina Windsor](https://boxerbook.com/boxers/marina-windsor-q3743334) · GB · id 11206 · slug marina-windsor-q3743334

```

**tool** `read_file` `{"path": "references/api.md"}`

```
# Boxerbook data access: MCP tools and REST API

Two doors to the same data. Use the MCP tools when they are connected (tool
names `boxing_schedule`, `boxer`, `bout` … possibly prefixed, e.g.
`mcp__plugin_boxing_boxerbook__boxer`). Otherwise use the REST API, through
`scripts/boxerbook.py` when you can run code, or by fetching the URLs directly.

## Contents
1. MCP server (tools, arguments, what each answers)
2. REST API (endpoints, parameters)
3. The helper script
4. Fields and how to read them
5. Gotchas

## 1. MCP server

Endpoint `https://mcp.boxerbook.com/mcp` (also `https://boxerbook.com/mcp`),
Streamable HTTP, stateless, no auth, 300 calls/min per IP. Every tool takes
`lang` (`en` | `es` | `ru` | `ja`): pass the user's language so the
boxerbook.com links in the answer are localized (`/es/boxeadores/...`,
`/ru/boksery/...`). Every answer carries `cite` (a ready markdown link) and `url`.

| Tool | Arguments | Use it for |
|---|---|---|
| `search` | `query` (a boxer, "A vs B", a division) | anything, when unsure which tool; returns document ids + urls |
| `fetch` | `id` = `boxer:<id>`, `bout:<id>`, `event:<id>`, `rankings:<DIV>` | the full document behind a search hit, as Markdown |
| `search_boxers` | `q` | name ambiguity: up to 20 boxers sharing a name/spelling, with country, division, record |
| `boxer` | `query` (name, slug or id) | a boxer's card: record (W-L-D, KOs), division, stance, height, reach, birth year, nickname, next fight, last result, rating, record as fa
... [9463 chars]
```

**tool** `boxer` `{"query": "jermell-charlo-q6182393"}`

```
Source: [Boxerbook](https://boxerbook.com/boxers/jermell-charlo-q6182393)

{"cite":"Source: [Boxerbook](https://boxerbook.com/boxers/jermell-charlo-q6182393)","id":16098,"slug":"jermell-charlo-q6182393","name":"Jermell Charlo","country":"US","sex":"male","division":"swel","record":{"w":35,"l":2,"d":1,"ko":19},"record_source":"bouts","bouts_without_result":0,"stance":"orthodox","height_cm":180,"reach_cm":185.5,"birth_date":"1990","nickname":"Iron Man","next_fight":null,"last_result":{"bout_id":25028,"date":"2023-09-30","opponent":{"id":8665,"name":"Canelo Álvarez","slug":"canelo-alvarez-q2117769"},"result":"L","method":"UD","round":12,"url":"https://boxerbook.com/bouts/25028/jermell-charlo-vs-canelo-alvarez"},"rating":{"mu":2303.3,"rd":122.8,"division_rank":null,"confidence":0.5676},"url":"https://boxerbook.com/boxers/jermell-charlo-q6182393","market_record":{"as_favourite":{"w":0,"l":0},"as_underdog":{"w":0,"l":1},"upsets_caused":0,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/jermell-charlo-q6182393"},"as_of":"2026-11-02T04:36:20Z"}
```

**tool** `boxer` `{"query": "jermall-charlo-q19864206"}`

```
Source: [Boxerbook](https://boxerbook.com/boxers/jermall-charlo-q19864206)

{"cite":"Source: [Boxerbook](https://boxerbook.com/boxers/jermall-charlo-q19864206)","id":7810,"slug":"jermall-charlo-q19864206","name":"Jermall Charlo","country":"US","sex":"male","division":"smid","record":{"w":36,"l":0,"d":0,"ko":24},"record_source":"bouts","bouts_without_result":0,"stance":"orthodox","height_cm":183,"reach_cm":188,"birth_date":"1990","nickname":"Hitman · The Future of Boxing","next_fight":null,"last_result":{"bout_id":23675,"date":"2025-05-31","opponent":{"id":21031,"name":"Thomas Lamanna","slug":"thomas-lamanna-b21031"},"result":"W","method":"TKO","round":6,"url":"https://boxerbook.com/bouts/23675/thomas-lamanna-vs-jermall-charlo"},"rating":{"mu":2384.6,"rd":136.6,"division_rank":null,"confidence":0.6667},"url":"https://boxerbook.com/boxers/jermall-charlo-q19864206","market_record":{"as_favourite":{"w":2,"l":0},"as_underdog":{"w":0,"l":0},"upsets_caused":0,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/jermall-charlo-q19864206"},"as_of":"2026-11-02T04:36:20Z"}
```

**assistant (interim)**

There are two boxers named Charlo, the twin brothers Jermell and Jermall. Here are both records as of 2 Nov 2026:

| | [Jermell Charlo](https://boxerbook.com/boxers/jermell-charlo-q6182393?utm_source=claude-skill) "Iron Man" | [Jermall Charlo](https://boxerbook.com/boxers/jermall-charlo-q19864206?utm_source=claude-skill) "Hitman" |
|---|---|---|
| **Record (W-L-D)** | **35-2-1**, 19 KOs | **36-0-0**, 24 KOs (unbeaten) |
| Division | Super welterweight | Super middleweight |
| Stance | Orthodox | Orthodox |
| Height / reach | 180 cm (5'11") / 185.5 cm (73") | 183 cm (6'0") / 188 cm (74") |
| Last fight | [Lost to Canelo Álvarez](https://boxerbook.com/bouts/25028/jermell-charlo-vs-canelo-alvarez?utm_source=claude-skill) by unanimous decision over 12 rounds, 30 Sep 2023 | [Beat Thomas Lamanna](https://boxerbook.com/bouts/23675/thomas-lamanna-vs-jermall-charlo?utm_source=claude-skill) by TKO in round 6, 31 May 2025 |
| Next fight | None scheduled | None scheduled |

If you meant one of them, I can look up more about his fights.

Source: [Boxerbook](https://boxerbook.com/search?q=Charlo&utm_source=claude-skill)

## Final answer

There are two boxers named Charlo, the twin brothers Jermell and Jermall. Here are both records as of 2 Nov 2026:

| | [Jermell Charlo](https://boxerbook.com/boxers/jermell-charlo-q6182393?utm_source=claude-skill) "Iron Man" | [Jermall Charlo](https://boxerbook.com/boxers/jermall-charlo-q19864206?utm_source=claude-skill) "Hitman" |
|---|---|---|
| **Record (W-L-D)** | **35-2-1**, 19 KOs | **36-0-0**, 24 KOs (unbeaten) |
| Division | Super welterweight | Super middleweight |
| Stance | Orthodox | Orthodox |
| Height / reach | 180 cm (5'11") / 185.5 cm (73") | 183 cm (6'0") / 188 cm (74") |
| Last fight | [Lost to Canelo Álvarez](https://boxerbook.com/bouts/25028/jermell-charlo-vs-canelo-alvarez?utm_source=claude-skill) by unanimous decision over 12 rounds, 30 Sep 2023 | [Beat Thomas Lamanna](https://boxerbook.com/bouts/23675/thomas-lamanna-vs-jermall-charlo?utm_source=claude-skill) by TKO in round 6, 31 May 2025 |
| Next fight | None scheduled | None scheduled |

If you meant one of them, I can look up more about his fights.

Source: [Boxerbook](https://boxerbook.com/search?q=Charlo&utm_source=claude-skill)

## Grade

```json
{
  "judge": {
    "grounded": true,
    "cited": true,
    "dates_explicit": true,
    "no_betting_tips": true,
    "language": true,
    "task": true,
    "notes": "Both Charlos are presented separately with correct records, dates and links. All figures match the tool output."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": true
  },
  "usd": 0.0648
}
```

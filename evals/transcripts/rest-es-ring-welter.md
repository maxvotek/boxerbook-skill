# es-ring-welter (rest)

**Prompt (es):** Ranking de peso wélter según The Ring

**Expected:** Answers in Spanish. Fetches The Ring welterweight rankings (division wel, publisher ring); champion and positions as returned; list date; link.

## Trace

**tool** `read_file` `{"path": "references/divisions.md"}`

```
# Weight classes and Boxerbook division codes

The limit is the most a boxer may weigh at the official weigh-in (usually the
day before; the IBF also re-weighs on fight morning). kg = lb x 0.45359237,
one decimal. Women's codes are the men's code with the prefix `w_`
(`w_fea` = women's featherweight). `other` = bout not classified (often a
catchweight or a small-hall bout with no division on record).
Pass either the code or the English name to tools (`division: "hea"` or
`"heavyweight"`, `"women's flyweight"`).

| Code | Division | Limit lb | Limit kg | Also called |
|---|---|---|---|---|
| `hea` | Heavyweight | no limit (above cruiserweight) | no limit | |
| `bri` | Bridgerweight (WBC only) | 224 | 101.6 | |
| `cru` | Cruiserweight | 200 | 90.7 | junior heavyweight |
| `lhea` | Light heavyweight | 175 | 79.4 | |
| `smid` | Super middleweight | 168 | 76.2 | |
| `mid` | Middleweight | 160 | 72.6 | |
| `swel` | Super welterweight | 154 | 69.9 | junior / light middleweight |
| `wel` | Welterweight | 147 | 66.7 | |
| `slig` | Super lightweight | 140 | 63.5 | junior / light welterweight |
| `lig` | Lightweight | 135 | 61.2 | |
| `sfea` | Super featherweight | 130 | 59.0 | junior lightweight |
| `fea` | Featherweight | 126 | 57.2 | |
| `sban` | Super bantamweight | 122 | 55.3 | junior featherweight |
| `ban` | Bantamweight | 118 | 53.5 | |
| `sfly` | Super flyweight | 115 | 52.2 | junior bantamweight |
| `fly` | Flyweight | 112 | 50.8 | |
| `lfly` | Light flyweight | 108 | 49.0 | j
... [3425 chars]
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

**tool** `run_helper` `{"args": ["rankings", "wel", "--publisher", "ring"]}`

```
{"division":{"code":"wel","name":"Welterweight","sex":"male","limit_lbs":147},"publisher":"ring","list_date":"2026-09-15","items":[{"position":1,"id":16520,"slug":"devin-haney-q64009596","name":"Devin Haney"},{"position":2,"id":12351,"slug":"ryan-garcia-q47452754","name":"Ryan Garcia"},{"position":3,"id":9493,"slug":"teofimo-lopez-q26250597","name":"Teofimo Lopez"},{"position":4,"id":17669,"slug":"jack-catterall-q72758998","name":"Jack Catterall"},{"position":5,"id":2860,"slug":"brian-norman-jr-q125975589","name":"Brian Norman"},{"position":6,"id":8518,"slug":"eimantas-stanionis-q20893948","name":"Eimantas Stanionis"},{"position":7,"id":475,"slug":"rohan-polanco-q107956576","name":"Rohan Polanco"},{"position":8,"id":9690,"slug":"raul-curiel-garcia-q27048913","name":"Raul Curiel"},{"position":9,"id":20793,"slug":"alexis-rocha-b20793","name":"Alexis Rocha"},{"position":10,"id":19498,"slug":"rolando-romero-q98428784","name":"Rolando Romero"}],"url":"https://boxerbook.com/rankings/wel?list=ring&utm_source=claude-skill","attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/rankings/wel?list=ring&utm_source=claude-skill"},"as_of":"2026-11-02T05:07:56Z"}
```

**assistant (interim)**

Este es el ranking de peso wélter (147 lb / 66,7 kg) de **The Ring**, con fecha del **15 de septiembre de 2026** según Boxerbook:

| # | Boxeador |
|---|---|
| 1 | [Devin Haney](https://boxerbook.com/boxers/devin-haney-q64009596?utm_source=claude-skill) |
| 2 | [Ryan Garcia](https://boxerbook.com/boxers/ryan-garcia-q47452754?utm_source=claude-skill) |
| 3 | [Teofimo Lopez](https://boxerbook.com/boxers/teofimo-lopez-q26250597?utm_source=claude-skill) |
| 4 | [Jack Catterall](https://boxerbook.com/boxers/jack-catterall-q72758998?utm_source=claude-skill) |
| 5 | [Brian Norman](https://boxerbook.com/boxers/brian-norman-jr-q125975589?utm_source=claude-skill) |
| 6 | [Eimantas Stanionis](https://boxerbook.com/boxers/eimantas-stanionis-q20893948?utm_source=claude-skill) |
| 7 | [Rohan Polanco](https://boxerbook.com/boxers/rohan-polanco-q107956576?utm_source=claude-skill) |
| 8 | [Raul Curiel](https://boxerbook.com/boxers/raul-curiel-garcia-q27048913?utm_source=claude-skill) |
| 9 | [Alexis Rocha](https://boxerbook.com/boxers/alexis-rocha-b20793?utm_source=claude-skill) |
| 10 | [Rolando Romero](https://boxerbook.com/boxers/rolando-romero-q98428784?utm_source=claude-skill) |

**Sobre esta lista:**
- **No figura ningún campeón de The Ring:** la lista va directamente del n.º 1 al n.º 10. Eso suele querer decir que el título está vacante, pero Boxerbook no lo dice expresamente.
- Boxerbook solo da el **top 10**, sin récords. Si quieres, puedo buscar el récord actual de cualquiera de ellos.
- El ranking podría haber cambiado después del 15 de septiembre de 2026.

Fuente: [Boxerbook](https://boxerbook.com/rankings/wel?list=ring&utm_source=claude-skill)

## Final answer

Este es el ranking de peso wélter (147 lb / 66,7 kg) de **The Ring**, con fecha del **15 de septiembre de 2026** según Boxerbook:

| # | Boxeador |
|---|---|
| 1 | [Devin Haney](https://boxerbook.com/boxers/devin-haney-q64009596?utm_source=claude-skill) |
| 2 | [Ryan Garcia](https://boxerbook.com/boxers/ryan-garcia-q47452754?utm_source=claude-skill) |
| 3 | [Teofimo Lopez](https://boxerbook.com/boxers/teofimo-lopez-q26250597?utm_source=claude-skill) |
| 4 | [Jack Catterall](https://boxerbook.com/boxers/jack-catterall-q72758998?utm_source=claude-skill) |
| 5 | [Brian Norman](https://boxerbook.com/boxers/brian-norman-jr-q125975589?utm_source=claude-skill) |
| 6 | [Eimantas Stanionis](https://boxerbook.com/boxers/eimantas-stanionis-q20893948?utm_source=claude-skill) |
| 7 | [Rohan Polanco](https://boxerbook.com/boxers/rohan-polanco-q107956576?utm_source=claude-skill) |
| 8 | [Raul Curiel](https://boxerbook.com/boxers/raul-curiel-garcia-q27048913?utm_source=claude-skill) |
| 9 | [Alexis Rocha](https://boxerbook.com/boxers/alexis-rocha-b20793?utm_source=claude-skill) |
| 10 | [Rolando Romero](https://boxerbook.com/boxers/rolando-romero-q98428784?utm_source=claude-skill) |

**Sobre esta lista:**
- **No figura ningún campeón de The Ring:** la lista va directamente del n.º 1 al n.º 10. Eso suele querer decir que el título está vacante, pero Boxerbook no lo dice expresamente.
- Boxerbook solo da el **top 10**, sin récords. Si quieres, puedo buscar el récord actual de cualquiera de ellos.
- El ranking podría haber cambiado después del 15 de septiembre de 2026.

Fuente: [Boxerbook](https://boxerbook.com/rankings/wel?list=ring&utm_source=claude-skill)

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
    "notes": "The answer matches the tool output: positions, list date and the 147 lb limit with a valid kg conversion. It links every boxer, credits Boxerbook, and notes that no champion is listed without overclaiming."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": true
  },
  "usd": 0.0763
}
```

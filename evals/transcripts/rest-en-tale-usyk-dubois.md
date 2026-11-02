# en-tale-usyk-dubois (rest)

**Prompt (en):** Tale of the tape Usyk vs Dubois

**Expected:** Fetches both boxers and their head to head; a side-by-side table (record, height, reach, stance, age/born, rating) using only fetched values; mentions their previous meetings with dates and results; links both boxers (and bouts).

## Trace

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

**tool** `read_file` `{"path": "references/templates.md"}`

```
# Output templates

The numbers below are illustrations of the layout, fetched once on
2 Nov 2026. Never reuse them: fetch fresh data for every answer.

## Contents
1. Fighter card · 2. Tale of the tape · 3. Fight-night rundown ·
4. Results recap · 5. Ranking table · 6. Prediction / forecast ·
7. Upset analysis · 8. Social post

Pick the one that fits; adapt headings to the user's language. Keep tables
narrow (chat apps wrap). Every template ends with a source line. Times:
convert `start_utc` to the user's time zone when you know it, else give UTC
and one or two big zones (ET, UK). Dates: write them out ("Sat 31 Oct 2026").

## 1. Fighter card

```
**Oleksandr Usyk** "The Cat" · 🇺🇦 Ukraine · Heavyweight
Record **25-0-0 (16 KOs)** · southpaw · 191 cm, reach 198 cm · born 1987
Last fight: W TKO 11 vs Rico Verhoeven, 23 May 2026 → [bout](url)
Next fight: none scheduled on Boxerbook
Boxerbook rating: #1 heavyweight (mu 2701)
As favourite 4-0, as underdog 1-0
Source: [Boxerbook](boxer url) · data as of 2 Nov 2026
```

## 2. Tale of the tape

```
| | Oleksandr Usyk | Daniel Dubois |
|---|---|---|
| Record | 25-0-0 (16 KO) | 24-3-0 (23 KO) |
| Age / born | 1987 | 1997 |
| Height | 191 cm (6'3") | 196 cm (6'5") |
| Reach | 198 cm (78") | 198 cm (78") |
| Stance | southpaw | orthodox |
| Last 5 | WWWWW | WWLWW |
| Boxerbook rating | 2701 (#1) | 2434 (#3) |
| Head to head | Usyk 2-0 (KO 9, 2023; KO 5, 2025) | |
```
Then 2-4 sentences of context (styles, what changed since they last met
... [4107 chars]
```

**tool** `run_helper` `{"args": ["h2h", "Usyk", "Dubois"]}`

```
{"a":{"id":19123,"name":"Oleksandr Usyk","record":{"w":25,"l":0,"d":0,"ko":16},"division":"hea","last_result":{"bout_id":66063,"date":"2026-05-23","opponent":{"id":17799,"name":"Rico Verhoeven","slug":"rico-verhoeven-q7332289"},"result":"W","method":"TKO","round":11,"url":"https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill"},"next_fight":null,"url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill"},"b":{"id":10208,"name":"Daniel Dubois","record":{"w":24,"l":3,"d":0,"ko":23},"division":"hea","last_result":{"bout_id":155247,"date":"2026-10-17","opponent":{"id":46,"name":"Fabio Wardley","slug":"fabio-wardley-q102218789"},"result":"W","method":"TKO","round":2,"url":"https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill"},"next_fight":null,"url":"https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill"},"met":true,"meetings":[{"id":34234,"date":"2025-07-19","status":"completed","opponent":{"id":10208,"name":"Daniel Dubois","slug":"daniel-dubois-q30122489"},"result":"W","method":"KO","round":5,"time":"1:52","scheduled_rounds":12,"title_text":"IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles","exhibition":false,"record":"23-0-0","opponent_record":"22-2-0","url":"https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill"},{"id":34237,"date":"2023-08-26","status":"completed","opponent":{"id":10208
... [2020 chars]
```

**tool** `run_helper` `{"args": ["boxer", "Usyk"]}`

```
{"id":19123,"slug":"oleksandr-usyk-q938027","name":"Oleksandr Usyk","country":"UA","sex":"male","division":"hea","record":{"w":25,"l":0,"d":0,"ko":16},"record_source":"bouts","bouts_without_result":0,"stance":"southpaw","height_cm":191,"reach_cm":198,"birth_date":"1987","nickname":"The Cat","next_fight":null,"last_result":{"bout_id":66063,"date":"2026-05-23","opponent":{"id":17799,"name":"Rico Verhoeven","slug":"rico-verhoeven-q7332289"},"result":"W","method":"TKO","round":11,"url":"https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill"},"rating":{"mu":2701.2,"rd":110.8,"division_rank":1,"confidence":0.72},"url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill","market_record":{"as_favourite":{"w":4,"l":0},"as_underdog":{"w":1,"l":0},"upsets_caused":1,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill"},"as_of":"2026-11-02T05:04:19Z"}
```

**tool** `run_helper` `{"args": ["boxer", "Daniel Dubois"]}`

```
{"id":10208,"slug":"daniel-dubois-q30122489","name":"Daniel Dubois","country":"GB","sex":"male","division":"hea","record":{"w":24,"l":3,"d":0,"ko":23},"record_source":"bouts","bouts_without_result":0,"stance":"orthodox","height_cm":196,"reach_cm":198,"birth_date":"1997","nickname":"Dynamite · Dynamite Daniel Dubois · DDD","next_fight":null,"last_result":{"bout_id":155247,"date":"2026-10-17","opponent":{"id":46,"name":"Fabio Wardley","slug":"fabio-wardley-q102218789"},"result":"W","method":"TKO","round":2,"url":"https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill"},"rating":{"mu":2434.3,"rd":98,"division_rank":3,"confidence":0.5926},"url":"https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill","market_record":{"as_favourite":{"w":2,"l":0},"as_underdog":{"w":3,"l":2},"upsets_caused":3,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill"},"as_of":"2026-11-02T05:04:20Z"}
```

**tool** `run_helper` `{"args": ["bouts", "Oleksandr Usyk", "--limit", "5"]}`

```
{"boxer":{"id":19123,"slug":"oleksandr-usyk-q938027","name":"Oleksandr Usyk"},"total":25,"limit":5,"offset":0,"bouts":[{"id":66063,"date":"2026-05-23","status":"completed","opponent":{"id":17799,"name":"Rico Verhoeven","slug":"rico-verhoeven-q7332289"},"result":"W","method":"TKO","round":11,"time":"2:59","scheduled_rounds":12,"title_text":"WBC and The Ring heavyweight titles","exhibition":false,"record":"24-0-0","opponent_record":"2-0-0","url":"https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill"},{"id":34234,"date":"2025-07-19","status":"completed","opponent":{"id":10208,"name":"Daniel Dubois","slug":"daniel-dubois-q30122489"},"result":"W","method":"KO","round":5,"time":"1:52","scheduled_rounds":12,"title_text":"IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles","exhibition":false,"record":"23-0-0","opponent_record":"22-2-0","url":"https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill"},{"id":4153,"date":"2024-12-21","status":"completed","opponent":{"id":1,"name":"Tyson Fury","slug":"tyson-fury-q1000592"},"result":"W","method":"UD","round":12,"time":null,"scheduled_rounds":12,"title_text":"WBA (Super), WBC, WBO, IBO and The Ring heavyweight titles","exhibition":false,"record":"22-0-0","opponent_record":"34-1-1","url":"https://boxerbook.com/bouts/4153/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill"},{"id":4154,"date":"2024-05-18","status":"completed","opponent":{"
... [2583 chars]
```

**tool** `run_helper` `{"args": ["bouts", "Daniel Dubois", "--limit", "5"]}`

```
{"boxer":{"id":10208,"slug":"daniel-dubois-q30122489","name":"Daniel Dubois"},"total":27,"limit":5,"offset":0,"bouts":[{"id":155247,"date":"2026-10-17","status":"completed","opponent":{"id":46,"name":"Fabio Wardley","slug":"fabio-wardley-q102218789"},"result":"W","method":"TKO","round":2,"time":"2:21","scheduled_rounds":12,"title_text":"WBO heavyweight title","exhibition":false,"record":"23-3-0","opponent_record":"20-1-1","url":"https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill"},{"id":4425,"date":"2026-05-09","status":"completed","opponent":{"id":46,"name":"Fabio Wardley","slug":"fabio-wardley-q102218789"},"result":"W","method":"TKO","round":11,"time":"0:28","scheduled_rounds":12,"title_text":"WBO heavyweight title","exhibition":false,"record":"22-3-0","opponent_record":"20-0-1","url":"https://boxerbook.com/bouts/4425/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill"},{"id":34234,"date":"2025-07-19","status":"completed","opponent":{"id":19123,"name":"Oleksandr Usyk","slug":"oleksandr-usyk-q938027"},"result":"L","method":"KO","round":5,"time":"1:52","scheduled_rounds":12,"title_text":"IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles","exhibition":false,"record":"22-2-0","opponent_record":"23-0-0","url":"https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill"},{"id":34235,"date":"2024-09-21","status":"completed","opponent":{"id":13936,"name":"Anthony Joshua","slug
... [2477 chars]
```

**assistant (interim)**

Oleksandr Usyk and Daniel Dubois have fought twice, and Usyk won both by knockout. Boxerbook doesn't list a third fight. Records are as of 2 November 2026.

| | **[Oleksandr Usyk](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill)** | **[Daniel Dubois](https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill)** |
|---|---|---|
| Nickname | "The Cat" | "Dynamite" |
| Country | Ukraine | Great Britain |
| Division | Heavyweight | Heavyweight |
| Record | **25-0-0 (16 KO)** | **24-3-0 (23 KO)** |
| Born | 1987 | 1997 |
| Height | 191 cm (6'3") | 196 cm (6'5") |
| Reach | 198 cm (78") | 198 cm (78") |
| Stance | Southpaw | Orthodox |
| Last 5 (newest first) | WWWWW | WWLWW |
| Last fight | Won by TKO in round 11 vs Rico Verhoeven, 23 May 2026 | Won by TKO in round 2 vs Fabio Wardley, 17 Oct 2026 |
| Boxerbook rating | 2701 (#1 heavyweight) | 2434 (#3 heavyweight) |
| As favourite / underdog | 4-0 / 1-0 | 2-0 / 3-2 |
| Next fight | None scheduled | None scheduled |

**Their two fights**
- **26 Aug 2023:** [Usyk won by KO in round 9 (0:48)](https://boxerbook.com/bouts/34237/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill). Titles: WBA (Super), IBF, WBO, IBO, and The Ring heavyweight titles. Records going in: Usyk 20-0-0, Dubois 19-1-0.
- **19 Jul 2025:** [Usyk won by KO in round 5 (1:52)](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill). Titles: IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles. Records going in: Usyk 23-0-0, Dubois 22-2-0.

**What's changed since the 2025 fight (based on Boxerbook data):**
- **Dubois** has fought Fabio Wardley twice for the WBO heavyweight title. He won by TKO in round 11 on [9 May 2026](https://boxerbook.com/bouts/4425/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill) and by TKO in round 2 on [17 Oct 2026](https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill).
- **Usyk** has fought once since, [beating Rico Verhoeven by TKO in round 11 on 23 May 2026](https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill). That fight was for the WBC and The Ring heavyweight titles.
- **Size:** Dubois is 5 cm taller, and they have the same 198 cm reach.
- **Rating:** Usyk is still clearly ahead on Boxerbook's rating, at #1 compared with #3 for Dubois.

Boxerbook doesn't have judges' scorecards or punch stats for these fights.

Source: [Boxerbook](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill)

## Final answer

Oleksandr Usyk and Daniel Dubois have fought twice, and Usyk won both by knockout. Boxerbook doesn't list a third fight. Records are as of 2 November 2026.

| | **[Oleksandr Usyk](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill)** | **[Daniel Dubois](https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill)** |
|---|---|---|
| Nickname | "The Cat" | "Dynamite" |
| Country | Ukraine | Great Britain |
| Division | Heavyweight | Heavyweight |
| Record | **25-0-0 (16 KO)** | **24-3-0 (23 KO)** |
| Born | 1987 | 1997 |
| Height | 191 cm (6'3") | 196 cm (6'5") |
| Reach | 198 cm (78") | 198 cm (78") |
| Stance | Southpaw | Orthodox |
| Last 5 (newest first) | WWWWW | WWLWW |
| Last fight | Won by TKO in round 11 vs Rico Verhoeven, 23 May 2026 | Won by TKO in round 2 vs Fabio Wardley, 17 Oct 2026 |
| Boxerbook rating | 2701 (#1 heavyweight) | 2434 (#3 heavyweight) |
| As favourite / underdog | 4-0 / 1-0 | 2-0 / 3-2 |
| Next fight | None scheduled | None scheduled |

**Their two fights**
- **26 Aug 2023:** [Usyk won by KO in round 9 (0:48)](https://boxerbook.com/bouts/34237/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill). Titles: WBA (Super), IBF, WBO, IBO, and The Ring heavyweight titles. Records going in: Usyk 20-0-0, Dubois 19-1-0.
- **19 Jul 2025:** [Usyk won by KO in round 5 (1:52)](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill). Titles: IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles. Records going in: Usyk 23-0-0, Dubois 22-2-0.

**What's changed since the 2025 fight (based on Boxerbook data):**
- **Dubois** has fought Fabio Wardley twice for the WBO heavyweight title. He won by TKO in round 11 on [9 May 2026](https://boxerbook.com/bouts/4425/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill) and by TKO in round 2 on [17 Oct 2026](https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill).
- **Usyk** has fought once since, [beating Rico Verhoeven by TKO in round 11 on 23 May 2026](https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill). That fight was for the WBC and The Ring heavyweight titles.
- **Size:** Dubois is 5 cm taller, and they have the same 198 cm reach.
- **Rating:** Usyk is still clearly ahead on Boxerbook's rating, at #1 compared with #3 for Dubois.

Boxerbook doesn't have judges' scorecards or punch stats for these fights.

Source: [Boxerbook](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill)

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
    "notes": "All table values, meetings, dates, and derived values (inches, last-5 form) match the tool outputs. The only unsupported line is the minor claim that Boxerbook lacks scorecards and punch stats."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": true
  },
  "usd": 0.1232
}
```

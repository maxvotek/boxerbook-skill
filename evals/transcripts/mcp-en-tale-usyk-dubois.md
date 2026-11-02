# en-tale-usyk-dubois (mcp)

**Prompt (en):** Tale of the tape Usyk vs Dubois

**Expected:** Fetches both boxers and their head to head; a side-by-side table (record, height, reach, stance, age/born, rating) using only fetched values; mentions their previous meetings with dates and results; links both boxers (and bouts).

## Trace

**tool** `bout` `{"query": "Usyk vs Dubois"}`

```
Source: [Boxerbook](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk)

{"cite":"Source: [Boxerbook](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk)","id":34234,"date":"2025-07-19","start_utc":"2025-07-19T19:00Z","status":"completed","confirmation":"official","provisional":false,"exhibition":false,"a":{"id":10208,"name":"Daniel Dubois","slug":"daniel-dubois-q30122489","record":"22-2-0"},"b":{"id":19123,"name":"Oleksandr Usyk","slug":"oleksandr-usyk-q938027","record":"23-0-0"},"display":["b","a"],"winner":"b","method":"KO","round":5,"time":"1:52","scheduled_rounds":12,"title_text":"IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles","venue":"Wembley Stadium","city":"London","country":"GB","event":{"id":5037,"date":"2025-07-19","venue":"Wembley Stadium","city":"London","country":"GB","promoter":"Queensberry Promotions","url":"https://boxerbook.com/events/5037/2025-07-19-london"},"broadcasts":[],"sources":[{"name":"English Wikipedia","url":"https://en.wikipedia.org/wiki/Daniel_Dubois"},{"name":"English Wikipedia","url":"https://en.wikipedia.org/wiki/Oleksandr_Usyk"},{"name":"Wikipedia (ja)","url":"https://ja.wikipedia.org/wiki/%E3%83%80%E3%83%8B%E3%82%A8%E3%83%AB%E3%83%BB%E3%83%87%E3%83%A5%E3%83%9C%E3%82%A2"},{"name":"Wikipedia (ja)","url":"https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%AC%E3%82%AF%E3%82%B5%E3%83%B3%E3%83%89%E3%83%AB%E3%83%BB%E3%82%A6%E3%82%B7%E3%82%AF"},{"name":"Wikipedia (ru)","url":"https://ru.
... [4397 chars]
```

**tool** `boxer` `{"query": "Oleksandr Usyk"}`

```
Source: [Boxerbook](https://boxerbook.com/boxers/oleksandr-usyk-q938027)

{"cite":"Source: [Boxerbook](https://boxerbook.com/boxers/oleksandr-usyk-q938027)","id":19123,"slug":"oleksandr-usyk-q938027","name":"Oleksandr Usyk","country":"UA","sex":"male","division":"hea","record":{"w":25,"l":0,"d":0,"ko":16},"record_source":"bouts","bouts_without_result":0,"stance":"southpaw","height_cm":191,"reach_cm":198,"birth_date":"1987","nickname":"The Cat","next_fight":null,"last_result":{"bout_id":66063,"date":"2026-05-23","opponent":{"id":17799,"name":"Rico Verhoeven","slug":"rico-verhoeven-q7332289"},"result":"W","method":"TKO","round":11,"url":"https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk"},"rating":{"mu":2701.2,"rd":110.8,"division_rank":1,"confidence":0.72},"url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027","market_record":{"as_favourite":{"w":4,"l":0},"as_underdog":{"w":1,"l":0},"upsets_caused":1,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027"},"as_of":"2026-11-02T04:35:03Z"}
```

**tool** `boxer` `{"query": "Daniel Dubois"}`

```
Source: [Boxerbook](https://boxerbook.com/boxers/daniel-dubois-q30122489)

{"cite":"Source: [Boxerbook](https://boxerbook.com/boxers/daniel-dubois-q30122489)","id":10208,"slug":"daniel-dubois-q30122489","name":"Daniel Dubois","country":"GB","sex":"male","division":"hea","record":{"w":24,"l":3,"d":0,"ko":23},"record_source":"bouts","bouts_without_result":0,"stance":"orthodox","height_cm":196,"reach_cm":198,"birth_date":"1997","nickname":"Dynamite · Dynamite Daniel Dubois · DDD","next_fight":null,"last_result":{"bout_id":155247,"date":"2026-10-17","opponent":{"id":46,"name":"Fabio Wardley","slug":"fabio-wardley-q102218789"},"result":"W","method":"TKO","round":2,"url":"https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley"},"rating":{"mu":2434.3,"rd":98,"division_rank":3,"confidence":0.5926},"url":"https://boxerbook.com/boxers/daniel-dubois-q30122489","market_record":{"as_favourite":{"w":2,"l":0},"as_underdog":{"w":3,"l":2},"upsets_caused":3,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/daniel-dubois-q30122489"},"as_of":"2026-11-02T04:35:04Z"}
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

**assistant (interim)**

Oleksandr Usyk and Daniel Dubois have fought **twice**, and Usyk won both by knockout. He stopped Dubois in round 9 on 26 August 2023 and in round 5 on 19 July 2025. Neither man has a fight scheduled, so this compares them as they stand now.

| | 🇺🇦 [Oleksandr Usyk](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill) | 🇬🇧 [Daniel Dubois](https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill) |
|---|---|---|
| Nickname | "The Cat" | "Dynamite" |
| Record | **25-0-0 (16 KOs)** | **24-3-0 (23 KOs)** |
| Born | 1987 | 1997 |
| Height | 191 cm (6'3") | 196 cm (6'5") |
| Reach | 198 cm (78") | 198 cm (78") |
| Stance | Southpaw | Orthodox |
| Last 3 fights | W W W | W W L |
| Boxerbook rating | 2701 (#1 heavyweight) | 2434 (#3 heavyweight) |
| Head to head | **2-0 Usyk** | 0-2 |

*Records and ratings are as of 2 November 2026.*

**Their two fights**
- **26 August 2023:** Usyk won by KO in round 9 → [bout](https://boxerbook.com/bouts/34237/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill)
- **19 July 2025:** Usyk won by KO in round 5 (at 1:52) at Wembley Stadium in London. The IBF heavyweight title plus the WBA (Super), WBC, WBO, IBO and The Ring heavyweight titles were on the line → [bout](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill)

**What each has done since**
- **Usyk** stopped Rico Verhoeven by TKO in round 11 on 23 May 2026 ([bout](https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill)). His previous win was a decision over Tyson Fury on 21 December 2024.
- **Dubois** has won two fights since the loss, both by TKO over Fabio Wardley:
  - Round 11 on 9 May 2026 ([bout](https://boxerbook.com/bouts/4425/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill))
  - Round 2 on 17 October 2026 ([bout](https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill))

**How they compare**
- **Size:** Dubois is 5 cm taller, but their reach is the same.
- **Age:** Usyk is about ten years older.
- **Power and experience:** Dubois has stopped far more of his opponents (23 KOs in 24 wins). Usyk has the unbeaten record and the higher Boxerbook rating.

Source: [Boxerbook](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill)

## Final answer

Oleksandr Usyk and Daniel Dubois have fought **twice**, and Usyk won both by knockout. He stopped Dubois in round 9 on 26 August 2023 and in round 5 on 19 July 2025. Neither man has a fight scheduled, so this compares them as they stand now.

| | 🇺🇦 [Oleksandr Usyk](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill) | 🇬🇧 [Daniel Dubois](https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill) |
|---|---|---|
| Nickname | "The Cat" | "Dynamite" |
| Record | **25-0-0 (16 KOs)** | **24-3-0 (23 KOs)** |
| Born | 1987 | 1997 |
| Height | 191 cm (6'3") | 196 cm (6'5") |
| Reach | 198 cm (78") | 198 cm (78") |
| Stance | Southpaw | Orthodox |
| Last 3 fights | W W W | W W L |
| Boxerbook rating | 2701 (#1 heavyweight) | 2434 (#3 heavyweight) |
| Head to head | **2-0 Usyk** | 0-2 |

*Records and ratings are as of 2 November 2026.*

**Their two fights**
- **26 August 2023:** Usyk won by KO in round 9 → [bout](https://boxerbook.com/bouts/34237/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill)
- **19 July 2025:** Usyk won by KO in round 5 (at 1:52) at Wembley Stadium in London. The IBF heavyweight title plus the WBA (Super), WBC, WBO, IBO and The Ring heavyweight titles were on the line → [bout](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill)

**What each has done since**
- **Usyk** stopped Rico Verhoeven by TKO in round 11 on 23 May 2026 ([bout](https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill)). His previous win was a decision over Tyson Fury on 21 December 2024.
- **Dubois** has won two fights since the loss, both by TKO over Fabio Wardley:
  - Round 11 on 9 May 2026 ([bout](https://boxerbook.com/bouts/4425/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill))
  - Round 2 on 17 October 2026 ([bout](https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill))

**How they compare**
- **Size:** Dubois is 5 cm taller, but their reach is the same.
- **Age:** Usyk is about ten years older.
- **Power and experience:** Dubois has stopped far more of his opponents (23 KOs in 24 wins). Usyk has the unbeaten record and the higher Boxerbook rating.

Source: [Boxerbook](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill)

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
    "notes": "All figures match the tool results (records, KOs, physicals, ratings, fight dates and results). Boxer and bout links are present, Boxerbook is credited, and there are no betting tips."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": true
  },
  "usd": 0.0757
}
```

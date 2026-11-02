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

{"cite":"Source: [Boxerbook](https://boxerbook.com/boxers/oleksandr-usyk-q938027)","id":19123,"slug":"oleksandr-usyk-q938027","name":"Oleksandr Usyk","country":"UA","sex":"male","division":"hea","record":{"w":25,"l":0,"d":0,"ko":16},"record_source":"bouts","bouts_without_result":0,"stance":"southpaw","height_cm":191,"reach_cm":198,"birth_date":"1987","nickname":"The Cat","next_fight":null,"last_result":{"bout_id":66063,"date":"2026-05-23","opponent":{"id":17799,"name":"Rico Verhoeven","slug":"rico-verhoeven-q7332289"},"result":"W","method":"TKO","round":11,"url":"https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk"},"rating":{"mu":2701.2,"rd":110.8,"division_rank":1,"confidence":0.72},"url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027","market_record":{"as_favourite":{"w":4,"l":0},"as_underdog":{"w":1,"l":0},"upsets_caused":1,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027"},"as_of":"2026-11-02T05:04:19Z"}
```

**tool** `boxer` `{"query": "Daniel Dubois"}`

```
Source: [Boxerbook](https://boxerbook.com/boxers/daniel-dubois-q30122489)

{"cite":"Source: [Boxerbook](https://boxerbook.com/boxers/daniel-dubois-q30122489)","id":10208,"slug":"daniel-dubois-q30122489","name":"Daniel Dubois","country":"GB","sex":"male","division":"hea","record":{"w":24,"l":3,"d":0,"ko":23},"record_source":"bouts","bouts_without_result":0,"stance":"orthodox","height_cm":196,"reach_cm":198,"birth_date":"1997","nickname":"Dynamite · Dynamite Daniel Dubois · DDD","next_fight":null,"last_result":{"bout_id":155247,"date":"2026-10-17","opponent":{"id":46,"name":"Fabio Wardley","slug":"fabio-wardley-q102218789"},"result":"W","method":"TKO","round":2,"url":"https://boxerbook.com/bouts/155247/daniel-dubois-vs-fabio-wardley"},"rating":{"mu":2434.3,"rd":98,"division_rank":3,"confidence":0.5926},"url":"https://boxerbook.com/boxers/daniel-dubois-q30122489","market_record":{"as_favourite":{"w":2,"l":0},"as_underdog":{"w":3,"l":2},"upsets_caused":3,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/daniel-dubois-q30122489"},"as_of":"2026-11-02T05:04:20Z"}
```

**assistant (interim)**

Usyk and Dubois have fought twice, and **Usyk won both by KO**. No third fight is scheduled in Boxerbook. Records below are as of 2 Nov 2026.

## Tale of the tape

| | [Oleksandr Usyk](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill) | [Daniel Dubois](https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill) |
|---|---|---|
| Nickname | The Cat | Dynamite |
| Country | Ukraine | Great Britain |
| Born | 1987 | 1997 |
| Record | **25-0-0** (16 KOs) | **24-3-0** (23 KOs) |
| Stance | Southpaw | Orthodox |
| Height | 191 cm (6′3″) | 196 cm (6′5″) |
| Reach | 198 cm (78″) | 198 cm (78″) |
| Boxerbook rating | 2701 (#1 at heavyweight) | 2434 (#3 at heavyweight) |
| Last fight | Beat Rico Verhoeven by TKO in round 11 on 23 May 2026 | Beat Fabio Wardley by TKO in round 2 on 17 Oct 2026 |
| Next fight | None scheduled | None scheduled |

**Key differences in the data:** Dubois is 5 cm taller and 10 years younger, and they have the same reach. Usyk is unbeaten and is #1 in the Boxerbook heavyweight rating. Dubois has a higher knockout count: 23 of his 24 wins.

## Their two fights
1. **[26 Aug 2023](https://boxerbook.com/bouts/34237/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill):** Usyk won by KO in round 9.
2. **[19 Jul 2025](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill), Wembley Stadium, London, UK:** Usyk won by KO in round 5 (at 1:52) of a scheduled 12. The titles at stake were the "IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles." Going in, Usyk was 23-0-0 and Dubois was 22-2-0.

## Since the rematch
- **Usyk:** 1 fight, a TKO win over Rico Verhoeven (23 May 2026).
- **Dubois:** 2 fights, both against [Fabio Wardley](https://boxerbook.com/bouts/4425/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill). He won by TKO in round 11 on 9 May 2026 and by TKO in round 2 on 17 Oct 2026.

Source: [Boxerbook](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill)

## Final answer

Usyk and Dubois have fought twice, and **Usyk won both by KO**. No third fight is scheduled in Boxerbook. Records below are as of 2 Nov 2026.

## Tale of the tape

| | [Oleksandr Usyk](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill) | [Daniel Dubois](https://boxerbook.com/boxers/daniel-dubois-q30122489?utm_source=claude-skill) |
|---|---|---|
| Nickname | The Cat | Dynamite |
| Country | Ukraine | Great Britain |
| Born | 1987 | 1997 |
| Record | **25-0-0** (16 KOs) | **24-3-0** (23 KOs) |
| Stance | Southpaw | Orthodox |
| Height | 191 cm (6′3″) | 196 cm (6′5″) |
| Reach | 198 cm (78″) | 198 cm (78″) |
| Boxerbook rating | 2701 (#1 at heavyweight) | 2434 (#3 at heavyweight) |
| Last fight | Beat Rico Verhoeven by TKO in round 11 on 23 May 2026 | Beat Fabio Wardley by TKO in round 2 on 17 Oct 2026 |
| Next fight | None scheduled | None scheduled |

**Key differences in the data:** Dubois is 5 cm taller and 10 years younger, and they have the same reach. Usyk is unbeaten and is #1 in the Boxerbook heavyweight rating. Dubois has a higher knockout count: 23 of his 24 wins.

## Their two fights
1. **[26 Aug 2023](https://boxerbook.com/bouts/34237/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill):** Usyk won by KO in round 9.
2. **[19 Jul 2025](https://boxerbook.com/bouts/34234/daniel-dubois-vs-oleksandr-usyk?utm_source=claude-skill), Wembley Stadium, London, UK:** Usyk won by KO in round 5 (at 1:52) of a scheduled 12. The titles at stake were the "IBF heavyweight title; WBA (Super), WBC, WBO, IBO, and The Ring heavyweight titles." Going in, Usyk was 23-0-0 and Dubois was 22-2-0.

## Since the rematch
- **Usyk:** 1 fight, a TKO win over Rico Verhoeven (23 May 2026).
- **Dubois:** 2 fights, both against [Fabio Wardley](https://boxerbook.com/bouts/4425/daniel-dubois-vs-fabio-wardley?utm_source=claude-skill). He won by TKO in round 11 on 9 May 2026 and by TKO in round 2 on 17 Oct 2026.

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
    "notes": "All values match the tool outputs, and the derived figures (age gap, inch conversions) are correct. The answer includes a side-by-side table, both prior meetings with dates, and links to both boxers and bouts."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": false
  },
  "usd": 0.0468
}
```

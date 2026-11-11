# ru-kabayel-forecast (rest)

**Prompt (ru):** Дай прогноз на бой Кабайел — Хыса.

**Expected:** Answers in Russian. Finds the scheduled Kabayel vs Hysa bout (28 Nov 2026, WBC heavyweight title); gives Boxerbook forecast and market consensus as probabilities with dates; both records; a 'not betting advice' line in Russian; links.

## Trace

**tool** `run_helper` `{"args": ["h2h", "Kabayel", "Hysa"]}`

```
{"a":{"id":10015,"name":"Agit Kabayel","record":{"w":31,"l":0,"d":0,"ko":21},"division":"hea","last_result":{"bout_id":9920,"date":"2026-01-10","opponent":{"id":2738,"name":"Damian Knyba","slug":"damian-knyba-q125270583"},"result":"W","method":"TKO","round":3,"url":"https://boxerbook.com/bouts/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill"},"next_fight":{"bout_id":192171,"date":"2026-11-28","start_utc":"2026-11-28T21:00Z","opponent":{"id":7989,"name":"Nelson Hysa","slug":"nelson-hysa-q20029125"},"url":"https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill"},"url":"https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill"},"b":{"id":7989,"name":"Nelson Hysa","record":{"w":26,"l":0,"d":0,"ko":24},"division":"hea","last_result":{"bout_id":23826,"date":"2026-08-29","opponent":{"id":20494,"name":"Thomas Narmo","slug":"thomas-narmo-q85969457"},"result":"W","method":"TKO","round":2,"url":"https://boxerbook.com/bouts/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill"},"next_fight":{"bout_id":192171,"date":"2026-11-28","start_utc":"2026-11-28T21:00Z","opponent":{"id":10015,"name":"Agit Kabayel","slug":"agit-kabayel-q28864444"},"url":"https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill"},"url":"https://boxerbook.com/boxers/nelson-hysa-q20029125?utm_source=claude-skill"},"met":true,"meetings":[{"id":192171,"date":"2026-11-28","status":"scheduled","opponent":{"id":7989,"name":"Nelso
... [1963 chars]
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

**tool** `run_helper` `{"args": ["bout", "192171"]}`

```
{"id":192171,"date":"2026-11-28","start_utc":"2026-11-28T21:00Z","status":"scheduled","confirmation":"single_source","provisional":false,"exhibition":false,"a":{"id":10015,"name":"Agit Kabayel","slug":"agit-kabayel-q28864444","record":"31-0-0"},"b":{"id":7989,"name":"Nelson Hysa","slug":"nelson-hysa-q20029125","record":"26-0-0"},"display":["a","b"],"winner":null,"method":null,"round":null,"time":null,"scheduled_rounds":12,"title_text":"WBC heavyweight title","venue":null,"city":"Dusseldorf","country":"DE","event":{"id":11870,"date":"2026-11-28","venue":null,"city":"Dusseldorf","country":"DE","promoter":null,"url":"https://boxerbook.com/events/11870/2026-11-28-dusseldorf?utm_source=claude-skill"},"broadcasts":[{"platform":"DAZN","region":"JP","url":null}],"sources":["ESPN — Boxing schedule","World Boxing Council — Upcoming events"],"source_links":["https://www.espn.com/boxing/story/_/id/12508267/boxing-schedule#2026-11-28-agit-kabayel-nelson-hysa","https://wbcboxing.com/en/events/agit-kabayel-vs-nelson-hysa/"],"fight_week":[],"url":"https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill","forecast":{"p_a":0.9175,"as_of":"2026-10-26","run_id":13},"market":{"favourite":"a","p_a":0.8929,"books":13,"snapshot_at":"2026-11-02T00:30Z","via":"The Odds API consensus","opening":{"p_a":0.8981,"snapshot_at":"2026-10-20T18:31Z"}},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_sou
... [1550 chars]
```

**tool** `run_helper` `{"args": ["boxer", "Agit Kabayel"]}`

```
{"id":10015,"slug":"agit-kabayel-q28864444","name":"Agit Kabayel","country":"DE","sex":"male","division":"hea","record":{"w":31,"l":0,"d":0,"ko":21},"record_source":"bouts","bouts_without_result":0,"stance":"orthodox","height_cm":null,"reach_cm":203,"birth_date":"1992","nickname":null,"next_fight":{"bout_id":192171,"date":"2026-11-28","start_utc":"2026-11-28T21:00Z","opponent":{"id":7989,"name":"Nelson Hysa","slug":"nelson-hysa-q20029125"},"url":"https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill"},"last_result":{"bout_id":9920,"date":"2026-01-10","opponent":{"id":2738,"name":"Damian Knyba","slug":"damian-knyba-q125270583"},"result":"W","method":"TKO","round":3,"url":"https://boxerbook.com/bouts/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill"},"rating":{"mu":2382.7,"rd":117.8,"division_rank":5,"confidence":0.3103},"url":"https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill","market_record":{"as_favourite":{"w":2,"l":0},"as_underdog":{"w":2,"l":0},"upsets_caused":2,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill"},"as_of":"2026-11-02T05:07:21Z"}
```

**tool** `run_helper` `{"args": ["boxer", "Nelson Hysa"]}`

```
{"id":7989,"slug":"nelson-hysa-q20029125","name":"Nelson Hysa","country":"AL","sex":"male","division":"hea","record":{"w":26,"l":0,"d":0,"ko":24},"record_source":"bouts","bouts_without_result":1,"stance":"orthodox","height_cm":null,"reach_cm":200.5,"birth_date":"1984","nickname":null,"next_fight":{"bout_id":192171,"date":"2026-11-28","start_utc":"2026-11-28T21:00Z","opponent":{"id":10015,"name":"Agit Kabayel","slug":"agit-kabayel-q28864444"},"url":"https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill"},"last_result":{"bout_id":23826,"date":"2026-08-29","opponent":{"id":20494,"name":"Thomas Narmo","slug":"thomas-narmo-q85969457"},"result":"W","method":"TKO","round":2,"url":"https://boxerbook.com/bouts/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill"},"rating":{"mu":2062.8,"rd":136.8,"division_rank":28,"confidence":0.1154},"url":"https://boxerbook.com/boxers/nelson-hysa-q20029125?utm_source=claude-skill","market_record":{"as_favourite":{"w":2,"l":0},"as_underdog":{"w":0,"l":0},"upsets_caused":0,"upsets_suffered":0},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/boxers/nelson-hysa-q20029125?utm_source=claude-skill"},"as_of":"2026-11-02T05:07:21Z"}
```

**assistant (interim)**

**Прогноз: Агит Кабайел — явный фаворит.** Модель Boxerbook даёт ему около **92%**, Нельсону Хысе около **8%**. Букмекеры оценивают бой почти так же: **89%** на **11%**.

**Бой:** [Агит Кабайел — Нельсон Хыса](https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill), **28 ноября 2026**, Дюссельдорф, Германия. 12 раундов, на кону титул «WBC heavyweight title». Кард начинается в 21:00 UTC. Главный бой обычно стартует через 2–4 часа после начала карда. Из трансляций Boxerbook знает только DAZN в Японии. Кроме того, Boxerbook отмечает бой как подтверждённый одним источником (`single_source`).

**Вероятности**
| | Кабайел | Хыса |
|---|---|---|
| Модель Boxerbook (на 26 окт 2026) | 91.75% | 8.25% |
| Букмекеры, среднее по 13 конторам, без маржи (на 2 нояб 2026) | 89.3% | 10.7% |
| Первая линия (20 окт 2026) | 89.8% | 10.2% |

**Сравнение бойцов** (на 2 ноября 2026)
| | [Агит Кабайел](https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill) | [Нельсон Хыса](https://boxerbook.com/boxers/nelson-hysa-q20029125?utm_source=claude-skill) |
|---|---|---|
| Страна | Германия | Албания |
| Рекорд | 31-0-0 (21 KO) | 26-0-0 (24 KO)* |
| Рейтинг Boxerbook | 2382.7 (5-й в тяжёлом весе) | 2062.8 (28-й) |
| Надёжность рейтинга (от 0 до 1) | 0.31 | 0.12 |
| Год рождения | 1992 | 1984 |
| Размах рук | 203 см (~80 дюймов) | 200.5 см (~79 дюймов) |
| Стойка | правосторонняя | правосторонняя |
| Последний бой | победа техническим нокаутом в 3-м раунде над [Дамианом Кныбой](https://boxerbook.com/bouts/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill), 10 января 2026 | победа техническим нокаутом во 2-м раунде над [Томасом Нармо](https://boxerbook.com/bouts/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill), 29 августа 2026 |
| Против букмекеров | фаворитом 2-0, андердогом 2-0 (2 победы, когда его ставили ниже) | фаворитом 2-0 |

*У одного из прошлых боёв Хысы в Boxerbook нет результата, поэтому его рекорд может быть неполным.

**Почему фаворит Кабайел** (это мой вывод из данных выше):
- Его рейтинг Boxerbook выше примерно на 320 пунктов, а место в весе — 5-е против 28-го.
- Букмекеры с открытия линии почти не изменили оценку.
- Оба не проигрывали и часто побеждают нокаутом, но о Хысе у модели меньше уверенности (0.12). Значит, его реальный уровень известен хуже, и оценку в 8% стоит считать менее точной.

Boxerbook не прогнозирует способ победы (нокаут или решение) и раунд, поэтому их я не называю.

Это вероятности, а не гарантия, и не совет для ставок.

Источник: [Boxerbook](https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)

## Final answer

**Прогноз: Агит Кабайел — явный фаворит.** Модель Boxerbook даёт ему около **92%**, Нельсону Хысе около **8%**. Букмекеры оценивают бой почти так же: **89%** на **11%**.

**Бой:** [Агит Кабайел — Нельсон Хыса](https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill), **28 ноября 2026**, Дюссельдорф, Германия. 12 раундов, на кону титул «WBC heavyweight title». Кард начинается в 21:00 UTC. Главный бой обычно стартует через 2–4 часа после начала карда. Из трансляций Boxerbook знает только DAZN в Японии. Кроме того, Boxerbook отмечает бой как подтверждённый одним источником (`single_source`).

**Вероятности**
| | Кабайел | Хыса |
|---|---|---|
| Модель Boxerbook (на 26 окт 2026) | 91.75% | 8.25% |
| Букмекеры, среднее по 13 конторам, без маржи (на 2 нояб 2026) | 89.3% | 10.7% |
| Первая линия (20 окт 2026) | 89.8% | 10.2% |

**Сравнение бойцов** (на 2 ноября 2026)
| | [Агит Кабайел](https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill) | [Нельсон Хыса](https://boxerbook.com/boxers/nelson-hysa-q20029125?utm_source=claude-skill) |
|---|---|---|
| Страна | Германия | Албания |
| Рекорд | 31-0-0 (21 KO) | 26-0-0 (24 KO)* |
| Рейтинг Boxerbook | 2382.7 (5-й в тяжёлом весе) | 2062.8 (28-й) |
| Надёжность рейтинга (от 0 до 1) | 0.31 | 0.12 |
| Год рождения | 1992 | 1984 |
| Размах рук | 203 см (~80 дюймов) | 200.5 см (~79 дюймов) |
| Стойка | правосторонняя | правосторонняя |
| Последний бой | победа техническим нокаутом в 3-м раунде над [Дамианом Кныбой](https://boxerbook.com/bouts/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill), 10 января 2026 | победа техническим нокаутом во 2-м раунде над [Томасом Нармо](https://boxerbook.com/bouts/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill), 29 августа 2026 |
| Против букмекеров | фаворитом 2-0, андердогом 2-0 (2 победы, когда его ставили ниже) | фаворитом 2-0 |

*У одного из прошлых боёв Хысы в Boxerbook нет результата, поэтому его рекорд может быть неполным.

**Почему фаворит Кабайел** (это мой вывод из данных выше):
- Его рейтинг Boxerbook выше примерно на 320 пунктов, а место в весе — 5-е против 28-го.
- Букмекеры с открытия линии почти не изменили оценку.
- Оба не проигрывали и часто побеждают нокаутом, но о Хысе у модели меньше уверенности (0.12). Значит, его реальный уровень известен хуже, и оценку в 8% стоит считать менее точной.

Boxerbook не прогнозирует способ победы (нокаут или решение) и раунд, поэтому их я не называю.

Это вероятности, а не гарантия, и не совет для ставок.

Источник: [Boxerbook](https://boxerbook.com/bouts/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)

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
    "notes": "All figures trace to the tool outputs. Derived values are fine: 8.25% = 1 - 0.9175, the ~320 rating gap, and inches from cm. The 2–4 hour main-event statement is allowed. The answer is in Russian, links to Boxerbook, gives dates, and includes a not-betting-advice line."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": true
  },
  "usd": 0.1202
}
```

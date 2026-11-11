# ru-usyk-fury-cards (rest)

**Prompt (ru):** Кто победил в последнем бою Усик — Фьюри и какие были записки судей?

**Expected:** Answers in Russian. Usyk beat Fury by UD on 21 Dec 2024 (their latest meeting); mentions the earlier SD in May 2024 is ok; says Boxerbook has no individual judges' scorecards and does NOT invent scores; links.

## Trace

**tool** `run_helper` `{"args": ["h2h", "Usyk", "Fury"]}`

```
{"a":{"id":19123,"name":"Oleksandr Usyk","record":{"w":25,"l":0,"d":0,"ko":16},"division":"hea","last_result":{"bout_id":66063,"date":"2026-05-23","opponent":{"id":17799,"name":"Rico Verhoeven","slug":"rico-verhoeven-q7332289"},"result":"W","method":"TKO","round":11,"url":"https://boxerbook.com/bouts/66063/rico-verhoeven-vs-oleksandr-usyk?utm_source=claude-skill"},"next_fight":null,"url":"https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill"},"b":{"id":1,"name":"Tyson Fury","record":{"w":36,"l":2,"d":1,"ko":25},"division":"hea","last_result":{"bout_id":4151,"date":"2026-07-24","opponent":{"id":3820,"name":"Mariusz Wach","slug":"mariusz-wach-q1345967"},"result":"W","method":"RTD","round":7,"url":"https://boxerbook.com/bouts/4151/tyson-fury-vs-mariusz-wach?utm_source=claude-skill"},"next_fight":{"bout_id":192176,"date":"2026-12-11","start_utc":"2026-12-12T02:00Z","opponent":{"id":13936,"name":"Anthony Joshua","slug":"anthony-joshua-q573463"},"url":"https://boxerbook.com/bouts/192176/tyson-fury-vs-anthony-joshua?utm_source=claude-skill"},"url":"https://boxerbook.com/boxers/tyson-fury-q1000592?utm_source=claude-skill"},"met":true,"meetings":[{"id":4153,"date":"2024-12-21","status":"completed","opponent":{"id":1,"name":"Tyson Fury","slug":"tyson-fury-q1000592"},"result":"W","method":"UD","round":12,"time":null,"scheduled_rounds":12,"title_text":"WBA (Super), WBC, WBO, IBO and The Ring heavyweight titles","exhibition":false,"record":"22-0-0","opponent_record"
... [2206 chars]
```

**assistant (interim)**

Check bout page for scorecards and venue.

**tool** `run_helper` `{"args": ["bout", "4153"]}`

```
{"id":4153,"date":"2024-12-21","start_utc":"2024-12-21T23:00Z","status":"completed","confirmation":"official","provisional":false,"exhibition":false,"a":{"id":1,"name":"Tyson Fury","slug":"tyson-fury-q1000592","record":"34-1-1"},"b":{"id":19123,"name":"Oleksandr Usyk","slug":"oleksandr-usyk-q938027","record":"22-0-0"},"display":["b","a"],"winner":"b","method":"UD","round":12,"time":null,"scheduled_rounds":12,"title_text":"WBA (Super), WBC, WBO, IBO and The Ring heavyweight titles","venue":"Kingdom Arena","city":"Riyadh","country":"SA","event":{"id":809,"date":"2024-12-21","venue":null,"city":"Riyadh","country":null,"promoter":"Queensberry Promotions","url":"https://boxerbook.com/events/809/2024-12-21-riyadh?utm_source=claude-skill"},"broadcasts":[],"sources":["English Wikipedia","Wikipedia (ja)","Wikipedia (ru)","WBA Fights Master Scores"],"source_links":["https://en.wikipedia.org/wiki/Tyson_Fury","https://en.wikipedia.org/wiki/Oleksandr_Usyk","https://ja.wikipedia.org/wiki/%E3%82%BF%E3%82%A4%E3%82%BD%E3%83%B3%E3%83%BB%E3%83%95%E3%83%A5%E3%83%BC%E3%83%AA%E3%83%BC"],"fight_week":[],"url":"https://boxerbook.com/bouts/4153/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill","market":{"favourite":"b","p_a":0.4183,"books":11,"snapshot_at":"2024-12-21T12:00Z","via":"The Odds API consensus"},"attribution":{"source":"Boxerbook","license":"ODbL","url":"https://boxerbook.com/bouts/4153/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill"},"as_of":"2026-11-02T05:06:44Z"}
```

**assistant (interim)**

Последний бой Усика и Фьюри прошёл **21 декабря 2024 года**. **Александр Усик победил единогласным решением судей (UD)** после всех 12 раундов.

**Записок судей нет в данных Boxerbook.** Там указан только способ победы, единогласное решение, без баллов каждого судьи. Поэтому цифры я не привожу.

**Что известно о бое:**
- **Место:** Kingdom Arena, Эр-Рияд, Саудовская Аравия. Промоутер: Queensberry Promotions.
- **Титулы:** WBA (Super), WBC, WBO, IBO and The Ring heavyweight titles.
- **Рекорды перед боем:** Усик 22-0-0, Фьюри 34-1-1.
- **Статус результата:** официальный.
- [Страница боя](https://boxerbook.com/bouts/4153/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill)

**Первый бой:** 18 мая 2024 года Усик тоже выиграл, но раздельным решением судей (SD) после 12 раундов. На кону был титул WBC; WBA (Super), IBF, WBO, IBO, and The Ring heavyweight titles ([страница боя](https://boxerbook.com/bouts/4154/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill)).

**Текущие рекорды (на 2 ноября 2026 года):**
- [Александр Усик](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill): 25-0-0, 16 побед нокаутом
- [Тайсон Фьюри](https://boxerbook.com/boxers/tyson-fury-q1000592?utm_source=claude-skill): 36-2-1, 25 побед нокаутом

Записки судей обычно публикуют санкционирующие организации, например WBA или WBC, а также крупные спортивные СМИ.

Источник: [Boxerbook](https://boxerbook.com/bouts/4153/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill)

## Final answer

Последний бой Усика и Фьюри прошёл **21 декабря 2024 года**. **Александр Усик победил единогласным решением судей (UD)** после всех 12 раундов.

**Записок судей нет в данных Boxerbook.** Там указан только способ победы, единогласное решение, без баллов каждого судьи. Поэтому цифры я не привожу.

**Что известно о бое:**
- **Место:** Kingdom Arena, Эр-Рияд, Саудовская Аравия. Промоутер: Queensberry Promotions.
- **Титулы:** WBA (Super), WBC, WBO, IBO and The Ring heavyweight titles.
- **Рекорды перед боем:** Усик 22-0-0, Фьюри 34-1-1.
- **Статус результата:** официальный.
- [Страница боя](https://boxerbook.com/bouts/4153/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill)

**Первый бой:** 18 мая 2024 года Усик тоже выиграл, но раздельным решением судей (SD) после 12 раундов. На кону был титул WBC; WBA (Super), IBF, WBO, IBO, and The Ring heavyweight titles ([страница боя](https://boxerbook.com/bouts/4154/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill)).

**Текущие рекорды (на 2 ноября 2026 года):**
- [Александр Усик](https://boxerbook.com/boxers/oleksandr-usyk-q938027?utm_source=claude-skill): 25-0-0, 16 побед нокаутом
- [Тайсон Фьюри](https://boxerbook.com/boxers/tyson-fury-q1000592?utm_source=claude-skill): 36-2-1, 25 побед нокаутом

Записки судей обычно публикуют санкционирующие организации, например WBA или WBC, а также крупные спортивные СМИ.

Источник: [Boxerbook](https://boxerbook.com/bouts/4153/tyson-fury-vs-oleksandr-usyk?utm_source=claude-skill)

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
    "notes": "Correct winner, method and date (21 Dec 2024, UD), the earlier SD on 18 May 2024 is mentioned, and the answer states that Boxerbook has no judges' scores without inventing any. Links and Boxerbook credit are present."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": false
  },
  "usd": 0.0367
}
```

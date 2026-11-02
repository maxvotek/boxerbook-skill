# ru-kabayel-forecast (mcp)

**Prompt (ru):** Дай прогноз на бой Кабайел — Хыса.

**Expected:** Answers in Russian. Finds the scheduled Kabayel vs Hysa bout (28 Nov 2026, WBC heavyweight title); gives Boxerbook forecast and market consensus as probabilities with dates; both records; a 'not betting advice' line in Russian; links.

## Trace

**tool** `bout` `{"query": "Kabayel vs Hysa", "lang": "ru"}`

```
Source: [Boxerbook](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa)

{"cite":"Source: [Boxerbook](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa)","id":192171,"date":"2026-11-28","start_utc":"2026-11-28T21:00Z","status":"scheduled","confirmation":"single_source","provisional":false,"exhibition":false,"a":{"id":10015,"name":"Agit Kabayel","slug":"agit-kabayel-q28864444","record":"31-0-0"},"b":{"id":7989,"name":"Nelson Hysa","slug":"nelson-hysa-q20029125","record":"26-0-0"},"display":["a","b"],"winner":null,"method":null,"round":null,"time":null,"scheduled_rounds":12,"title_text":"WBC heavyweight title","venue":null,"city":"Dusseldorf","country":"DE","event":{"id":11870,"date":"2026-11-28","venue":null,"city":"Dusseldorf","country":"DE","promoter":null,"url":"https://boxerbook.com/ru/vechera/11870/2026-11-28-dusseldorf"},"broadcasts":[{"platform":"DAZN","region":"JP","url":null}],"sources":[{"name":"ESPN — Boxing schedule","url":"https://www.espn.com/boxing/story/_/id/12508267/boxing-schedule#2026-11-28-agit-kabayel-nelson-hysa"},{"name":"World Boxing Council — Upcoming events","url":"https://wbcboxing.com/en/events/agit-kabayel-vs-nelson-hysa/"}],"fight_week":[],"url":"https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa","forecast":{"p_a":0.9175,"as_of":"2026-10-26","run_id":13},"market":{"favourite":"a","p_a":0.8929,"books":13,"snapshot_at":"2026-11-02T00:30Z","via":"The Odds API consensus","opening":{"p_a":0.8981,"snapshot_at":"2
... [4887 chars]
```

**assistant (interim)**

Boxerbook даёт **Агиту Кабайелу около 92%** на победу над **Нельсоном Хысой**. Букмекеры тоже видят его явным фаворитом.

**[Агит Кабайел — Нельсон Хыса](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)**
- **Дата:** 28 ноября 2026, Дюссельдорф, Германия. Вечер начинается в 21:00 UTC. Это время начала всего вечера, а не главного боя.
- **Бой:** 12 раундов, на кону титул «WBC heavyweight title».
- **Статус:** у Boxerbook бой отмечен как подтверждённый одним источником (single_source).

**Вероятности**

| | Кабайел | Хыса |
|---|---|---|
| Прогноз Boxerbook (от 26.10.2026) | **91,8%** | 8,2% |
| Консенсус 13 букмекеров (на 02.11.2026) | **89,3%** | 10,7% |
| Букмекеры при открытии линии (20.10.2026) | 89,8% | 10,2% |

**Данные модели**

| | [Кабайел](https://boxerbook.com/ru/boksery/agit-kabayel-q28864444?utm_source=claude-skill) | [Хыса](https://boxerbook.com/ru/boksery/nelson-hysa-q20029125?utm_source=claude-skill) |
|---|---|---|
| Рекорд перед боем | 31-0-0 | 26-0-0 |
| Доля побед нокаутом | 68% | 92% |
| Последние 5 боёв | WWWWW | WWWWW |
| Возраст | 34 года | 42 года |
| Размах рук | 203 см (≈80") | 200,5 см (≈79") |
| Рейтинг Boxerbook | 2383 (+56 за 12 мес.) | 2063 (+10 за 12 мес.) |
| Перерыв без боёв | 322 дня | 91 день |
| Стойка | правосторонняя | правосторонняя |
| Дома или на выезде | дома | на выезде |

**Последние бои**
- **Кабайел:** победил техническим нокаутом Дамиана Кныбу в 3-м раунде ([10.01.2026](https://boxerbook.com/ru/boi/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill)), нокаутом Чжана Чжилэя в 6-м раунде ([22.02.2025](https://boxerbook.com/ru/boi/32613/agit-kabayel-vs-zhang-zhilei?utm_source=claude-skill)) и нокаутом Франка Санчеса в 7-м раунде ([18.05.2024](https://boxerbook.com/ru/boi/32614/agit-kabayel-vs-frank-sanchez?utm_source=claude-skill)).
- **Хыса:** победил техническим нокаутом Томаса Нармо во 2-м раунде ([29.08.2026](https://boxerbook.com/ru/boi/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill)), Абеля Песута в 4-м раунде ([09.10.2025](https://boxerbook.com/ru/boi/23827/abel-pesut-vs-nelson-hysa?utm_source=claude-skill)) и Патрика Корте во 2-м раунде ([07.06.2025](https://boxerbook.com/ru/boi/23828/patrick-korte-vs-nelson-hysa?utm_source=claude-skill)).

**Моя оценка по этим данным**
- **За Кабайела:** заметно более высокий рейтинг, рейтинг вырос за последний год, он на 8 лет моложе и дерётся дома.
- **За Хысу:** выше доля нокаутов, и он дрался недавно. У Кабайела перерыв почти 11 месяцев.
- Как боксёры между собой выиграли бы эти бои, модель не учитывает. Стилей в данных тоже нет.

**Где смотреть:** Boxerbook знает только о трансляции на DAZN в Японии. Других трансляций в базе пока нет.

Это вероятности, а не гарантии. И это не совет для ставок.

Source: [Boxerbook](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)

## Final answer

Boxerbook даёт **Агиту Кабайелу около 92%** на победу над **Нельсоном Хысой**. Букмекеры тоже видят его явным фаворитом.

**[Агит Кабайел — Нельсон Хыса](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)**
- **Дата:** 28 ноября 2026, Дюссельдорф, Германия. Вечер начинается в 21:00 UTC. Это время начала всего вечера, а не главного боя.
- **Бой:** 12 раундов, на кону титул «WBC heavyweight title».
- **Статус:** у Boxerbook бой отмечен как подтверждённый одним источником (single_source).

**Вероятности**

| | Кабайел | Хыса |
|---|---|---|
| Прогноз Boxerbook (от 26.10.2026) | **91,8%** | 8,2% |
| Консенсус 13 букмекеров (на 02.11.2026) | **89,3%** | 10,7% |
| Букмекеры при открытии линии (20.10.2026) | 89,8% | 10,2% |

**Данные модели**

| | [Кабайел](https://boxerbook.com/ru/boksery/agit-kabayel-q28864444?utm_source=claude-skill) | [Хыса](https://boxerbook.com/ru/boksery/nelson-hysa-q20029125?utm_source=claude-skill) |
|---|---|---|
| Рекорд перед боем | 31-0-0 | 26-0-0 |
| Доля побед нокаутом | 68% | 92% |
| Последние 5 боёв | WWWWW | WWWWW |
| Возраст | 34 года | 42 года |
| Размах рук | 203 см (≈80") | 200,5 см (≈79") |
| Рейтинг Boxerbook | 2383 (+56 за 12 мес.) | 2063 (+10 за 12 мес.) |
| Перерыв без боёв | 322 дня | 91 день |
| Стойка | правосторонняя | правосторонняя |
| Дома или на выезде | дома | на выезде |

**Последние бои**
- **Кабайел:** победил техническим нокаутом Дамиана Кныбу в 3-м раунде ([10.01.2026](https://boxerbook.com/ru/boi/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill)), нокаутом Чжана Чжилэя в 6-м раунде ([22.02.2025](https://boxerbook.com/ru/boi/32613/agit-kabayel-vs-zhang-zhilei?utm_source=claude-skill)) и нокаутом Франка Санчеса в 7-м раунде ([18.05.2024](https://boxerbook.com/ru/boi/32614/agit-kabayel-vs-frank-sanchez?utm_source=claude-skill)).
- **Хыса:** победил техническим нокаутом Томаса Нармо во 2-м раунде ([29.08.2026](https://boxerbook.com/ru/boi/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill)), Абеля Песута в 4-м раунде ([09.10.2025](https://boxerbook.com/ru/boi/23827/abel-pesut-vs-nelson-hysa?utm_source=claude-skill)) и Патрика Корте во 2-м раунде ([07.06.2025](https://boxerbook.com/ru/boi/23828/patrick-korte-vs-nelson-hysa?utm_source=claude-skill)).

**Моя оценка по этим данным**
- **За Кабайела:** заметно более высокий рейтинг, рейтинг вырос за последний год, он на 8 лет моложе и дерётся дома.
- **За Хысу:** выше доля нокаутов, и он дрался недавно. У Кабайела перерыв почти 11 месяцев.
- Как боксёры между собой выиграли бы эти бои, модель не учитывает. Стилей в данных тоже нет.

**Где смотреть:** Boxerbook знает только о трансляции на DAZN в Японии. Других трансляций в базе пока нет.

Это вероятности, а не гарантии. И это не совет для ставок.

Source: [Boxerbook](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)

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
    "notes": "All figures trace to the tool output: 91.75% rounds to 91.8%, market 89.29% to 89.3%, the opening line 89.81% to 89.8%, plus age, reach in inches, layoff days and ko_rate. The card start is correctly described as the start of the whole card. Links are present, there is a Russian not-betting-advice line, and both records and the dated bout are given. The 'Моя оценка' section only restates tool data, and the 8-year age gap is derived from 34.2 and 42.2."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": false
  },
  "usd": 0.0708
}
```

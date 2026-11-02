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

Boxerbook даёт победу **Агиту Кабайелу примерно в 92%**. Букмекеры оценивают его шансы похоже: около 89%.

**[Агит Кабайел — Нельсон Хыса](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)**: 28 ноября 2026, Дюссельдорф (Германия), 12 раундов, на кону титул WBC в супертяжёлом весе. Вечер начинается в 21:00 UTC, главный бой будет позже. Пока бой подтверждает только один источник.

**Вероятности**

| | Кабайел | Хыса |
|---|---|---|
| Прогноз Boxerbook (на 26 октября 2026) | 91,8% | 8,2% |
| Букмекеры (13 контор, 2 ноября 2026) | 89,3% | 10,7% |
| Букмекеры при открытии линии (20 октября 2026) | 89,8% | 10,2% |

**Сравнение бойцов (записи перед боем)**

| | [Кабайел](https://boxerbook.com/ru/boksery/agit-kabayel-q28864444?utm_source=claude-skill) | [Хыса](https://boxerbook.com/ru/boksery/nelson-hysa-q20029125?utm_source=claude-skill) |
|---|---|---|
| Рекорд | 31-0-0 | 26-0-0 |
| Доля нокаутов | 68% | 92% |
| Возраст | 34 | 42 |
| Размах рук | 203 см | 200,5 см |
| Стойка | правосторонняя | правосторонняя |
| Рейтинг Boxerbook | ~2383 (+56 за 12 месяцев) | ~2063 (+10 за 12 месяцев) |
| Последние 5 боёв | 5 побед | 5 побед |
| Дней без боёв | 322 | 91 |

**Почему фаворит Кабайел**
- **Рейтинг.** У него рейтинг выше примерно на 320 пунктов. Только по рейтингу его шансы около 83%.
- **Соперники.** Он бил сильных: 10 января 2026 — [Дамиан Кныба](https://boxerbook.com/ru/boi/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill) (TKO, 3-й раунд), 22 февраля 2025 — [Чжан Чжилэй](https://boxerbook.com/ru/boi/32613/agit-kabayel-vs-zhang-zhilei?utm_source=claude-skill) (KO, 6-й раунд), 18 мая 2024 — [Франк Санчес](https://boxerbook.com/ru/boi/32614/agit-kabayel-vs-frank-sanchez?utm_source=claude-skill) (KO, 7-й раунд).
- **Дома.** Бой пройдёт в Германии.

**Шансы Хысы**
- **Нокаутирующий удар и форма.** Он нокаутирует почти всех соперников. Последние три боя выиграл досрочно: 29 августа 2026 — [Томас Нармо](https://boxerbook.com/ru/boi/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill) (TKO, 2-й раунд), 9 октября 2025 — [Абель Песут](https://boxerbook.com/ru/boi/23827/abel-pesut-vs-nelson-hysa?utm_source=claude-skill) (TKO, 4-й раунд), 7 июня 2025 — [Патрик Корте](https://boxerbook.com/ru/boi/23828/patrick-korte-vs-nelson-hysa?utm_source=claude-skill) (TKO, 2-й раунд).
- **Паузы нет.** Он дрался три месяца назад, а Кабайел не выходил на ринг почти 11 месяцев.
- **Но:** ему 42 года, а его соперники заметно слабее, чем у Кабайела.

Трансляция: пока известна только DAZN (Япония). Подробнее — на [странице вечера](https://boxerbook.com/ru/vechera/11870/2026-11-28-dusseldorf?utm_source=claude-skill).

Это вероятности, а не гарантии. И это не совет для ставок.

Source: [Boxerbook](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)

## Final answer

Boxerbook даёт победу **Агиту Кабайелу примерно в 92%**. Букмекеры оценивают его шансы похоже: около 89%.

**[Агит Кабайел — Нельсон Хыса](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)**: 28 ноября 2026, Дюссельдорф (Германия), 12 раундов, на кону титул WBC в супертяжёлом весе. Вечер начинается в 21:00 UTC, главный бой будет позже. Пока бой подтверждает только один источник.

**Вероятности**

| | Кабайел | Хыса |
|---|---|---|
| Прогноз Boxerbook (на 26 октября 2026) | 91,8% | 8,2% |
| Букмекеры (13 контор, 2 ноября 2026) | 89,3% | 10,7% |
| Букмекеры при открытии линии (20 октября 2026) | 89,8% | 10,2% |

**Сравнение бойцов (записи перед боем)**

| | [Кабайел](https://boxerbook.com/ru/boksery/agit-kabayel-q28864444?utm_source=claude-skill) | [Хыса](https://boxerbook.com/ru/boksery/nelson-hysa-q20029125?utm_source=claude-skill) |
|---|---|---|
| Рекорд | 31-0-0 | 26-0-0 |
| Доля нокаутов | 68% | 92% |
| Возраст | 34 | 42 |
| Размах рук | 203 см | 200,5 см |
| Стойка | правосторонняя | правосторонняя |
| Рейтинг Boxerbook | ~2383 (+56 за 12 месяцев) | ~2063 (+10 за 12 месяцев) |
| Последние 5 боёв | 5 побед | 5 побед |
| Дней без боёв | 322 | 91 |

**Почему фаворит Кабайел**
- **Рейтинг.** У него рейтинг выше примерно на 320 пунктов. Только по рейтингу его шансы около 83%.
- **Соперники.** Он бил сильных: 10 января 2026 — [Дамиан Кныба](https://boxerbook.com/ru/boi/9920/agit-kabayel-vs-damian-knyba?utm_source=claude-skill) (TKO, 3-й раунд), 22 февраля 2025 — [Чжан Чжилэй](https://boxerbook.com/ru/boi/32613/agit-kabayel-vs-zhang-zhilei?utm_source=claude-skill) (KO, 6-й раунд), 18 мая 2024 — [Франк Санчес](https://boxerbook.com/ru/boi/32614/agit-kabayel-vs-frank-sanchez?utm_source=claude-skill) (KO, 7-й раунд).
- **Дома.** Бой пройдёт в Германии.

**Шансы Хысы**
- **Нокаутирующий удар и форма.** Он нокаутирует почти всех соперников. Последние три боя выиграл досрочно: 29 августа 2026 — [Томас Нармо](https://boxerbook.com/ru/boi/23826/thomas-narmo-vs-nelson-hysa?utm_source=claude-skill) (TKO, 2-й раунд), 9 октября 2025 — [Абель Песут](https://boxerbook.com/ru/boi/23827/abel-pesut-vs-nelson-hysa?utm_source=claude-skill) (TKO, 4-й раунд), 7 июня 2025 — [Патрик Корте](https://boxerbook.com/ru/boi/23828/patrick-korte-vs-nelson-hysa?utm_source=claude-skill) (TKO, 2-й раунд).
- **Паузы нет.** Он дрался три месяца назад, а Кабайел не выходил на ринг почти 11 месяцев.
- **Но:** ему 42 года, а его соперники заметно слабее, чем у Кабайела.

Трансляция: пока известна только DAZN (Япония). Подробнее — на [странице вечера](https://boxerbook.com/ru/vechera/11870/2026-11-28-dusseldorf?utm_source=claude-skill).

Это вероятности, а не гарантии. И это не совет для ставок.

Source: [Boxerbook](https://boxerbook.com/ru/boi/192171/agit-kabayel-vs-nelson-hysa?utm_source=claude-skill)

## Grade

```json
{
  "judge": {
    "grounded": false,
    "cited": true,
    "dates_explicit": true,
    "no_betting_tips": true,
    "language": true,
    "task": true,
    "notes": "Numbers and records are correct, but it claims the card starts at 21:00 UTC with the main event later (the data gives only the bout start time) and that Hysa's opponents are 'noticeably weaker' (no supporting data)."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": false
  },
  "usd": 0.0534
}
```

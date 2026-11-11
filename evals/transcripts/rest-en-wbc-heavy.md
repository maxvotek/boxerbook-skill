# en-wbc-heavy (rest)

**Prompt (en):** Top 10 heavyweights by WBC

**Expected:** Fetches WBC heavyweight rankings; lists the champion plus positions 1-10 exactly as returned; states the list date; links to boxerbook.com.

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

**tool** `run_helper` `{"args": ["rankings", "hea", "--publisher", "wbc"]}`

```
{"division":{"code":"hea","name":"Heavyweight","sex":"male","limit_lbs":null},"publisher":"wbc","list_date":"2026-10-01","items":[{"position":0,"id":10015,"slug":"agit-kabayel-q28864444","name":"Agit Kabayel","champion_flag":"champion"},{"position":1,"id":1,"slug":"tyson-fury-q1000592","name":"Tyson Fury"},{"position":2,"id":13936,"slug":"anthony-joshua-q573463","name":"Anthony Joshua"},{"position":3,"id":18659,"slug":"frank-sanchez-q85865836","name":"Frank Sanchez"},{"position":4,"id":19033,"slug":"deontay-wilder-q933423","name":"Deontay Wilder"},{"position":5,"id":2721,"slug":"moses-itauma-q125162793","name":"Moses Itauma"},{"position":6,"id":8997,"slug":"efe-ajagba-q23439518","name":"Efe Ajagba"},{"position":7,"id":6543,"slug":"joseph-parker-q16227145","name":"Joseph Parker"},{"position":8,"id":17799,"slug":"rico-verhoeven-q7332289","name":"Rico Verhoeven"},{"position":9,"id":18318,"slug":"richard-riakporhe-q79052399","name":"Richard Riakporhe"},{"position":10,"id":4390,"slug":"andrii-novytskyi-q136735484","name":"Andrii Novitskyi"},{"position":11,"id":8959,"slug":"bakhodir-jalolov-q23060341","name":"Bakhodir Jalolov"},{"position":12,"id":17156,"slug":"justis-huni-q68101642","name":"Justis Huni"},{"position":13,"id":4583,"slug":"labinot-xhoxhaj-q137540720","name":"Labinot Xhoxhaj"},{"position":14,"id":5353,"slug":"kingsley-ibeh-q140690786","name":"Kingsley Ibeh"},{"position":15,"id":16639,"slug":"mourad-aliev-q64875891","name":"Mourad Aliev"}],"url":"https://boxerbook.com/
... [1708 chars]
```

**assistant (interim)**

Here's the WBC heavyweight list dated 1 October 2026. Agit Kabayel is the champion, and Tyson Fury is No. 1 among the contenders.

| # | Boxer |
|---|---|
| C | [Agit Kabayel](https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill) (champion) |
| 1 | [Tyson Fury](https://boxerbook.com/boxers/tyson-fury-q1000592?utm_source=claude-skill) |
| 2 | [Anthony Joshua](https://boxerbook.com/boxers/anthony-joshua-q573463?utm_source=claude-skill) |
| 3 | [Frank Sanchez](https://boxerbook.com/boxers/frank-sanchez-q85865836?utm_source=claude-skill) |
| 4 | [Deontay Wilder](https://boxerbook.com/boxers/deontay-wilder-q933423?utm_source=claude-skill) |
| 5 | [Moses Itauma](https://boxerbook.com/boxers/moses-itauma-q125162793?utm_source=claude-skill) |
| 6 | [Efe Ajagba](https://boxerbook.com/boxers/efe-ajagba-q23439518?utm_source=claude-skill) |
| 7 | [Joseph Parker](https://boxerbook.com/boxers/joseph-parker-q16227145?utm_source=claude-skill) |
| 8 | [Rico Verhoeven](https://boxerbook.com/boxers/rico-verhoeven-q7332289?utm_source=claude-skill) |
| 9 | [Richard Riakporhe](https://boxerbook.com/boxers/richard-riakporhe-q79052399?utm_source=claude-skill) |
| 10 | [Andrii Novitskyi](https://boxerbook.com/boxers/andrii-novytskyi-q136735484?utm_source=claude-skill) |

Just outside the top 10 are Bakhodir Jalolov, Justis Huni, Labinot Xhoxhaj, Kingsley Ibeh and Mourad Aliev (No. 11 to 15). I can pull records or upcoming fights for any of these boxers.

Source: [Boxerbook](https://boxerbook.com/rankings/hea?list=wbc&utm_source=claude-skill)

## Final answer

Here's the WBC heavyweight list dated 1 October 2026. Agit Kabayel is the champion, and Tyson Fury is No. 1 among the contenders.

| # | Boxer |
|---|---|
| C | [Agit Kabayel](https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill) (champion) |
| 1 | [Tyson Fury](https://boxerbook.com/boxers/tyson-fury-q1000592?utm_source=claude-skill) |
| 2 | [Anthony Joshua](https://boxerbook.com/boxers/anthony-joshua-q573463?utm_source=claude-skill) |
| 3 | [Frank Sanchez](https://boxerbook.com/boxers/frank-sanchez-q85865836?utm_source=claude-skill) |
| 4 | [Deontay Wilder](https://boxerbook.com/boxers/deontay-wilder-q933423?utm_source=claude-skill) |
| 5 | [Moses Itauma](https://boxerbook.com/boxers/moses-itauma-q125162793?utm_source=claude-skill) |
| 6 | [Efe Ajagba](https://boxerbook.com/boxers/efe-ajagba-q23439518?utm_source=claude-skill) |
| 7 | [Joseph Parker](https://boxerbook.com/boxers/joseph-parker-q16227145?utm_source=claude-skill) |
| 8 | [Rico Verhoeven](https://boxerbook.com/boxers/rico-verhoeven-q7332289?utm_source=claude-skill) |
| 9 | [Richard Riakporhe](https://boxerbook.com/boxers/richard-riakporhe-q79052399?utm_source=claude-skill) |
| 10 | [Andrii Novitskyi](https://boxerbook.com/boxers/andrii-novytskyi-q136735484?utm_source=claude-skill) |

Just outside the top 10 are Bakhodir Jalolov, Justis Huni, Labinot Xhoxhaj, Kingsley Ibeh and Mourad Aliev (No. 11 to 15). I can pull records or upcoming fights for any of these boxers.

Source: [Boxerbook](https://boxerbook.com/rankings/hea?list=wbc&utm_source=claude-skill)

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
    "notes": "The champion and positions 1-10 match the tool output exactly, and the list date of 1 October 2026 is correct. The boxers named outside the top 10 (Nos. 11-15) are also correct. Each boxer links to boxerbook.com, and the source is credited. No fights or betting content appear, so the dates and betting criteria are not applicable."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": true
  },
  "usd": 0.0642
}
```

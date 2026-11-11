# en-wbc-heavy (mcp)

**Prompt (en):** Top 10 heavyweights by WBC

**Expected:** Fetches WBC heavyweight rankings; lists the champion plus positions 1-10 exactly as returned; states the list date; links to boxerbook.com.

## Trace

**tool** `rankings` `{"division": "heavyweight", "publisher": "wbc"}`

```
Source: [Boxerbook](https://boxerbook.com/rankings/hea?list=wbc)

Heavyweight rankings: WBC (2026-10-01).

0. [Agit Kabayel](https://boxerbook.com/boxers/agit-kabayel-q28864444) (champion) · id 10015
1. [Tyson Fury](https://boxerbook.com/boxers/tyson-fury-q1000592) · id 1
2. [Anthony Joshua](https://boxerbook.com/boxers/anthony-joshua-q573463) · id 13936
3. [Frank Sanchez](https://boxerbook.com/boxers/frank-sanchez-q85865836) · id 18659
4. [Deontay Wilder](https://boxerbook.com/boxers/deontay-wilder-q933423) · id 19033
5. [Moses Itauma](https://boxerbook.com/boxers/moses-itauma-q125162793) · id 2721
6. [Efe Ajagba](https://boxerbook.com/boxers/efe-ajagba-q23439518) · id 8997
7. [Joseph Parker](https://boxerbook.com/boxers/joseph-parker-q16227145) · id 6543
8. [Rico Verhoeven](https://boxerbook.com/boxers/rico-verhoeven-q7332289) · id 17799
9. [Richard Riakporhe](https://boxerbook.com/boxers/richard-riakporhe-q79052399) · id 18318
10. [Andrii Novitskyi](https://boxerbook.com/boxers/andrii-novytskyi-q136735484) · id 4390
11. [Bakhodir Jalolov](https://boxerbook.com/boxers/bakhodir-jalolov-q23060341) · id 8959
12. [Justis Huni](https://boxerbook.com/boxers/justis-huni-q68101642) · id 17156
13. [Labinot Xhoxhaj](https://boxerbook.com/boxers/labinot-xhoxhaj-q137540720) · id 4583
14. [Kingsley Ibeh](https://boxerbook.com/boxers/kingsley-ibeh-q140690786) · id 5353
15. [Mourad Aliev](https://boxerbook.com/boxers/mourad-aliev-q64875891) · id 16639

```

**assistant (interim)**

Agit Kabayel is the WBC heavyweight champion. Here's the WBC's top 10, from its list dated 1 October 2026:

| # | Boxer |
|---|---|
| C | [Agit Kabayel](https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill) |
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

The list didn't include records. I can look up the current record for any of these boxers, or show you the WBA, IBF, WBO, The Ring or Boxerbook heavyweight rankings.

Source: [Boxerbook](https://boxerbook.com/rankings/hea?list=wbc&utm_source=claude-skill)

## Final answer

Agit Kabayel is the WBC heavyweight champion. Here's the WBC's top 10, from its list dated 1 October 2026:

| # | Boxer |
|---|---|
| C | [Agit Kabayel](https://boxerbook.com/boxers/agit-kabayel-q28864444?utm_source=claude-skill) |
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

The list didn't include records. I can look up the current record for any of these boxers, or show you the WBA, IBF, WBO, The Ring or Boxerbook heavyweight rankings.

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
    "notes": "The champion and positions 1-10 match the tool output exactly, and the list date of 1 October 2026 is correct. Every boxer is linked to boxerbook.com, and Boxerbook is credited as the source. The claim that the list has no records is accurate. No fights are mentioned, so dates are not applicable, and there are no betting tips."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": false
  },
  "usd": 0.0438
}
```

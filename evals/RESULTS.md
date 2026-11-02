# Eval results

Generated 2026-11-02 by `evals/make_results.py`. Model under test: `claude-opus-5-5` (effort medium); judge: `claude-sonnet-5-5`, which sees every tool result so it can check grounding. Live Boxerbook data.

A case passes when the judge marks all six criteria true **and** the answer used a data tool and passes the language heuristic.

## MCP path (Boxerbook MCP tools, as in the Claude Code plugin / connector): 15/15 pass

| Case | Lang | Pass | grounded | cited | dates_explicit | no_betting_tips | language | task | Link | utm | Tool calls | $ | Transcript |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| en-canelo-last | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.054 | [md](transcripts/mcp-en-canelo-last.md) |
| en-tale-usyk-dubois | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 3 | 0.047 | [md](transcripts/mcp-en-tale-usyk-dubois.md) |
| en-weekend | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 3 | 0.147 | [md](transcripts/mcp-en-weekend.md) |
| en-wbc-heavy | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.044 | [md](transcripts/mcp-en-wbc-heavy.md) |
| es-mbilli-invicto | es | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.020 | [md](transcripts/mcp-es-mbilli-invicto.md) |
| en-charlo-ambiguous | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 3 | 0.029 | [md](transcripts/mcp-en-charlo-ambiguous.md) |
| en-nonexistent | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 5 | 0.055 | [md](transcripts/mcp-en-nonexistent.md) |
| en-betting | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.095 | [md](transcripts/mcp-en-betting.md) |
| ru-usyk-fury-cards | ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.033 | [md](transcripts/mcp-ru-usyk-fury-cards.md) |
| es-anoche | es | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.043 | [md](transcripts/mcp-es-anoche.md) |
| ru-kabayel-forecast | ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.071 | [md](transcripts/mcp-ru-kabayel-forecast.md) |
| en-inoue | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.021 | [md](transcripts/mcp-en-inoue.md) |
| es-ring-welter | es | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.025 | [md](transcripts/mcp-es-ring-welter.md) |
| en-x-post | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.053 | [md](transcripts/mcp-en-x-post.md) |
| ru-fury-canelo-h2h | ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.044 | [md](transcripts/mcp-ru-fury-canelo-h2h.md) |

## REST path (scripts/boxerbook.py, as in claude.ai code execution): 15/15 pass

| Case | Lang | Pass | grounded | cited | dates_explicit | no_betting_tips | language | task | Link | utm | Tool calls | $ | Transcript |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| en-canelo-last | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.051 | [md](transcripts/rest-en-canelo-last.md) |
| en-tale-usyk-dubois | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 7 | 0.123 | [md](transcripts/rest-en-tale-usyk-dubois.md) |
| en-weekend | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.150 | [md](transcripts/rest-en-weekend.md) |
| en-wbc-heavy | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.064 | [md](transcripts/rest-en-wbc-heavy.md) |
| es-mbilli-invicto | es | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.031 | [md](transcripts/rest-es-mbilli-invicto.md) |
| en-charlo-ambiguous | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.013 | [md](transcripts/rest-en-charlo-ambiguous.md) |
| en-nonexistent | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 5 | 0.030 | [md](transcripts/rest-en-nonexistent.md) |
| en-betting | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.149 | [md](transcripts/rest-en-betting.md) |
| ru-usyk-fury-cards | ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.037 | [md](transcripts/rest-ru-usyk-fury-cards.md) |
| es-anoche | es | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 3 | 0.072 | [md](transcripts/rest-es-anoche.md) |
| ru-kabayel-forecast | ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 5 | 0.120 | [md](transcripts/rest-ru-kabayel-forecast.md) |
| en-inoue | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.017 | [md](transcripts/rest-en-inoue.md) |
| es-ring-welter | es | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 3 | 0.076 | [md](transcripts/rest-es-ring-welter.md) |
| en-x-post | en | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 2 | 0.075 | [md](transcripts/rest-en-x-post.md) |
| ru-fury-canelo-h2h | ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0.022 | [md](transcripts/rest-ru-fury-canelo-h2h.md) |

## Triggering (`evals/trigger_test.py`, claude-opus-5-5)

The model sees only skill names + descriptions: `boxing` and 10 realistic neighbours (mma-stats, sports-scores, fitness-coach incl. boxing workouts, shopping-deals incl. Boxing Day, data-viz incl. box plots, pdf, xlsx, travel-planner, movie-guide, news-brief).

- Boxing prompts that picked `boxing`: **14/14**
- Near-miss prompts that did not pick `boxing`: **10/10**

| Prompt | Should trigger | Picked | OK |
|---|---|---|---|
| did canelo win last night? | yes | `boxing` | ✅ |
| When is Usyk's next fight? | yes | `boxing` | ✅ |
| What boxing is on tonight and where can I watch it in the UK? | yes | `boxing` | ✅ |
| Inoue vs Nakatani prediction | yes | `boxing` | ✅ |
| How tall is Tyson Fury and what's his reach? | yes | `boxing` | ✅ |
| Who's the best pound for pound boxer right now? | yes | `boxing` | ✅ |
| What does a split decision mean in boxing and who won the last big one? | yes | `boxing` | ✅ |
| Write a tweet about last night's boxing results | yes | `boxing` | ✅ |
| ¿Quién es el campeón pesado del CMB? | yes | `boxing` | ✅ |
| ¿Canelo es zurdo? | yes | `boxing` | ✅ |
| Cartelera de box de este fin de semana | yes | `boxing` | ✅ |
| Кто сейчас абсолютный чемпион в тяжёлом весе? | yes | `boxing` | ✅ |
| Какой рекорд у Бивола? | yes | `boxing` | ✅ |
| Jake Paul record? | yes | `boxing` | ✅ |
| Who won the UFC main event on Saturday? | no | `mma-stats` | ✅ |
| Give me a 30-minute heavy bag workout for beginners | no | `fitness-coach` | ✅ |
| Best Boxing Day sales in London this year? | no | `shopping-deals` | ✅ |
| Make a box plot of salaries by department in matplotlib | no | `data-viz` | ✅ |
| NBA scores from last night | no | `sports-scores` | ✅ |
| Plan a 10-day trip to Thailand with a Muay Thai camp | no | `travel-planner` | ✅ |
| How do I pack boxes efficiently for a move? | no | `none` | ✅ |
| Recommend a good documentary to watch tonight | no | `movie-guide` | ✅ |
| Rankings de la UFC peso ligero | no | `mma-stats` | ✅ |
| Как поставить удар в кикбоксинге для тренировки? | no | `fitness-coach` | ✅ |

## What the evals changed in the skill

Failures seen during development and the fix made to SKILL.md:

| Failure | Fix |
|---|---|
| Mentioned pre-fight odds without a not-betting-advice line | Rule 6: any answer that shows a forecast or odds ends with the disclaimer; don't volunteer odds |
| "Perdió su primera pelea" (first fight) instead of first loss | Precise record wording |
| Unsupported judgement ("weaker opposition") in a preview | Tie every comparative claim to a fetched field |
| Background from memory ("twin brothers", "Arlington, Texas", who held which belt, full names) | Rule 1 lists "harmless" background as forbidden; places as returned |
| Self-counted totals ("15 cards" when there were 16, "four title fights") | Quote only totals a tool returned |
| Quoted the catalog size written in SKILL.md ("about 30,000 boxers"), which can go stale | Numbers removed from SKILL.md; live size via `status` |
| Judge false positives (records going in, card vs main-event start, Russian "супертяжёлый", truncated tool output) | Judge prompt given the documented field semantics; tool output passed in full |

History: full runs during development scored 13/15 then 12/15 (MCP) and 12/15, 13/15 (REST); each failure above led to one change in SKILL.md. The last full run scored 14/15 (MCP) and 15/15 (REST); the one MCP failure (catalog size) was fixed and that case re-run. LLM answers vary between runs, so re-run the suite after every change to the skill text.

Spend for the runs on this page: about $1.93.

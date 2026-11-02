# en-weekend (mcp)

**Prompt (en):** What boxing is on this weekend?

**Expected:** Calls the schedule for the weekend; leads with title fights / main events; gives dates, venues/cities, card start times (noting they are card start, in UTC or converted), broadcasters when present; links cards or bouts; a Boxerbook source line.

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

**tool** `boxing_schedule` `{"when": "weekend", "lang": "en"}`

```
Source: [Boxerbook](https://boxerbook.com/schedule)

Boxing schedule (weekend), 2026-11-06 to 2026-11-08: 2 cards, 6 bouts of 71.
Times are card starts in UTC. Records are going into the bout. p is the Boxerbook forecast and market the no-vig bookmaker consensus, for the boxer named first: information, not betting advice.

Showing 6 of 71 bouts. More: call again with from_date=2026-11-07, or a narrower window (when=today, tonight or weekend, a country or a division).

## [2026-11-06, The Spotlight, Hoddesdon, GB](https://boxerbook.com/events/11955/2026-11-06-hoddesdon) · watch: no broadcaster on record yet
- [Erick Omar Lopez (0-2-0) vs Hamza Mehmood](https://boxerbook.com/bouts/193266/hamza-mehmood-vs-erick-omar-lopez) · OTHER · p Erick Omar Lopez 44%
- [Connor Meanwell (0-3-0) vs Jamie Robinson](https://boxerbook.com/bouts/193267/jamie-robinson-vs-connor-meanwell) · OTHER · p Connor Meanwell 50%
- [Doru Mogos (1-0-0) vs Alex Carter (0-0-0)](https://boxerbook.com/bouts/193268/doru-mogos-vs-alex-carter) · OTHER · p Doru Mogos 63%
- [Lakshmy Zaragoza Contreras vs Reegan Jackson Smith](https://boxerbook.com/bouts/193269/lakshmy-zaragoza-contreras-vs-reegan-jackson-smith) · OTHER
- [Jorge Balmaceda vs Saqib Mehmood](https://boxerbook.com/bouts/193270/jorge-balmaceda-vs-saqib-mehmood) · OTHER

## 2026-11-06 07:00 UTC · watch: no broadcaster on record yet
- [Paul Gallen (16-2-1) vs Nelson Asofa-Solomona (1-0-0)](https://boxerbook.com/bouts/194029/paul-gallen-vs-nelson-asofa-solomo
... [1557 chars]
```

**tool** `boxing_schedule` `{"when": "weekend", "from_date": "2026-11-07", "lang": "en"}`

```
Source: [Boxerbook](https://boxerbook.com/schedule)

Boxing schedule (weekend), 2026-11-07 to 2026-11-08: 13 cards, 56 bouts of 65.
Times are card starts in UTC. Records are going into the bout. p is the Boxerbook forecast and market the no-vig bookmaker consensus, for the boxer named first: information, not betting advice.

Showing 56 of 65 bouts. More: call again with from_date=2026-11-08, or a narrower window (when=today, tonight or weekend, a country or a division).

## [2026-11-07, Sakai City Industrial Promotion Center, JP](https://boxerbook.com/events/5227/2026-11-07) · 西日本ボクシング協会 · watch: YouTube
- [Kanoma Uchinono vs Tokutake Obara](https://boxerbook.com/bouts/193271/kanoma-uchinono-vs-tokutake-obara) · OTHER · 5 rds
- [Yuma Takahashi vs Daichi Hida](https://boxerbook.com/bouts/193272/yuma-takahashi-vs-daichi-hida) · OTHER · 5 rds
- [Kenshin Oshima vs Toshihisa Tamashiro](https://boxerbook.com/bouts/193273/kenshin-oshima-vs-toshihisa-tamashiro) · OTHER · 5 rds
- [Keito Goto vs Hinata Tsukiyama](https://boxerbook.com/bouts/193274/keito-goto-vs-hinata-tsukiyama) · OTHER · 5 rds
- [Daichi Yamabe vs Rune Kotani](https://boxerbook.com/bouts/193275/daichi-yamabe-vs-rune-kotani) · OTHER · 5 rds
- [Shogo Akiyama vs Kazuma Nokami](https://boxerbook.com/bouts/193276/shogo-akiyama-vs-kazuma-nokami) · OTHER · 5 rds
- [Yuma Kondo vs Tokuomi Nakagawa](https://boxerbook.com/bouts/193277/yuma-kondo-vs-tokuomi-nakagawa) · OTHER · 5 rds
- [Ayumu Takahashi vs Ritsuo Hanada](https://box
... [10467 chars]
```

**tool** `boxing_schedule` `{"when": "weekend", "from_date": "2026-11-08", "lang": "en"}`

```
Source: [Boxerbook](https://boxerbook.com/schedule)

Boxing schedule (weekend), 2026-11-08 to 2026-11-08: 1 card, 9 bouts.
Times are card starts in UTC. Records are going into the bout. p is the Boxerbook forecast and market the no-vig bookmaker consensus, for the boxer named first: information, not betting advice.

## [2026-11-08 01:00 UTC, Arlington, US](https://boxerbook.com/events/11863/2026-11-08-arlington) · watch: ESPN, ESPN+ (US)
- [Alycia Baumgardner (18-1-0) vs Elif Nur Turhan (15-0-0)](https://boxerbook.com/bouts/192149/elif-nur-turhan-vs-alycia-baumgardner) · Women’s lightweight · 10 rds · IBF women's lightweight title · p Alycia Baumgardner 64% · market Alycia Baumgardner 79%
- [Irma García (26-5-1) vs Nataly Delgado (21-8-2)](https://boxerbook.com/bouts/192150/nataly-delgado-vs-irma-garcia) · Women’s super flyweight · 10 rds · IBF women's junior bantamweight title and Delga… · p Irma García 46%
- [Ramla Ali (11-2-0) vs Mikiah Kreps (0-0-0)](https://boxerbook.com/bouts/192151/ramla-ali-vs-mikiah-kreps) · Women’s super bantamweight · 10 rds · Vacant WBO and IBF women's junior featherweight… · p Ramla Ali 75% · market Ramla Ali 26%
- [Skye Nicolson (16-1-0) vs Miyo Yoshida (20-5-0)](https://boxerbook.com/bouts/192152/miyo-yoshida-vs-skye-nicolson) · Super bantamweight · 10 rds · WBC junior featherweight title · p Skye Nicolson 93% · market Skye Nicolson 89%
- [Brittany Sims (2-0-0) vs Shera Mae Patricio (3-0-0)](https://boxerbook.com/bouts/192153/brittany-sims-vs-s
... [2290 chars]
```

**assistant (interim)**

Boxerbook lists 71 bouts on 15 cards from Friday 6 to Sunday 8 November 2026. These are the main ones. Times are when each card starts, in UTC. Main events usually begin 2–4 hours later. Records are going into each fight.

## Saturday 7 Nov: London, Copper Box Arena
**Card starts 16:30 UTC · Sky Sports** · [Card](https://boxerbook.com/events/11861/2026-11-07-london?utm_source=claude-skill)
- [Chris Billam-Smith (22-2) vs Cheavon Clarke (12-2)](https://boxerbook.com/bouts/192142/cheavon-clarke-vs-chris-billam-smith?utm_source=claude-skill): cruiserweight, 10 rounds
- [Denzel Bentley (31-3-1) vs Shane Mosley Jr.](https://boxerbook.com/bouts/192143/shane-mosley-jr-vs-denzel-bentley?utm_source=claude-skill): middleweight, 12 rounds
- [Umar Dzambekov (13-0) vs Zach Parker (26-2)](https://boxerbook.com/bouts/192144/zach-parker-vs-umar-dzambekov?utm_source=claude-skill): light heavyweight, 10 rounds
- Also on the card: Ezra Taylor (13-1) vs Bradley Rea, plus prospects Da'Mazion Vanhouter and Sam Hickey

## Saturday 7 Nov: Manchester Arena
**Card starts 21:00 UTC · DAZN (Spain, Mexico, US Spanish-language listed)** · [Card](https://boxerbook.com/events/11860/2026-11-07-manchester?utm_source=claude-skill)
- [Joshua Buatsi (20-1) vs Willy Hutchinson (20-2)](https://boxerbook.com/bouts/192140/willy-hutchinson-vs-joshua-buatsi?utm_source=claude-skill): **vacant WBC interim light heavyweight title**, 12 rounds
- [Jack Rafferty (27-0-1) vs Hovhannes Martirosyan](https://boxerbook.com/bouts/192141/hovhannes-martirosyan-vs-jack-rafferty?utm_source=claude-skill): super lightweight, 12 rounds

## Saturday 7 Nov: Albuquerque, US
**DAZN (worldwide) · start time not on record** · [Card](https://boxerbook.com/events/11862/2026-11-07-albuquerque?utm_source=claude-skill)
- [Abraham Perez (15-0) vs Yankiel Rivera (7-1-1)](https://boxerbook.com/bouts/192148/yankiel-rivera-vs-abraham-perez?utm_source=claude-skill): **WBA interim flyweight title**, 12 rounds

## Sunday 8 Nov, 01:00 UTC (Saturday evening in the US): Arlington, US
**ESPN / ESPN+ (US)** · [Card](https://boxerbook.com/events/11863/2026-11-08-arlington?utm_source=claude-skill). This card is stacked with women's title fights:
- [Alycia Baumgardner (18-1) vs Elif Nur Turhan (15-0)](https://boxerbook.com/bouts/192149/elif-nur-turhan-vs-alycia-baumgardner?utm_source=claude-skill): **IBF women's lightweight title**
- [Tiara Brown (21-0) vs Ellie Scotney (13-0)](https://boxerbook.com/bouts/192182/tiara-brown-vs-ellie-scotney?utm_source=claude-skill): women's featherweight, unbeaten vs unbeaten
- [Skye Nicolson (16-1) vs Miyo Yoshida (20-5)](https://boxerbook.com/bouts/192152/miyo-yoshida-vs-skye-nicolson?utm_source=claude-skill): **WBC junior featherweight title**
- [Ramla Ali (11-2) vs Mikiah Kreps](https://boxerbook.com/bouts/192151/ramla-ali-vs-mikiah-kreps?utm_source=claude-skill): **vacant WBO and IBF women's junior featherweight titles**
- [Irma García (26-5-1) vs Nataly Delgado (21-8-2)](https://boxerbook.com/bouts/192150/nataly-delgado-vs-irma-garcia?utm_source=claude-skill): **IBF women's junior bantamweight title**
- [Brittany Sims (2-0) vs Shera Mae Patricio (3-0)](https://boxerbook.com/bouts/192153/brittany-sims-vs-shera-mae-patricio?utm_source=claude-skill): **vacant WBA "regular" women's bantamweight title**

## Other cards
- **Friday 6 Nov, 07:00 UTC:** [Paul Gallen (16-2-1) vs Nelson Asofa-Solomona (1-0)](https://boxerbook.com/bouts/194029/paul-gallen-vs-nelson-asofa-solomona?utm_source=claude-skill). Boxerbook has no venue or broadcaster for this one yet.
- **Saturday 7 Nov, Korakuen Hall, Tokyo (U-NEXT, Japan):** [Kenichi Ogawa (32-2-1) vs Jae-woo Lee](https://boxerbook.com/bouts/193310/jae-woo-lee-vs-kenichi-ogawa?utm_source=claude-skill) and Yamato Hata (19-2-1) vs Ryō Sagawa (14-5)
- **Saturday 7 Nov, Miami (TrillerTV / Integrated Sports PPV):** [Maria Luz Peral vs Yokasta Valle](https://boxerbook.com/bouts/193234/maria-luz-peral-vs-yokasta-valle?utm_source=claude-skill)
- **Saturday 7 Nov, Istanbul:** Mourad Aliev (15-1-1) vs Umut Camkiran, heavyweight
- There are also smaller shows in Hoddesdon, Alfreton, Doncaster, Manchester (Wythenshawe Forum), Sakai (Japan) and Caracas, mostly prospects and debut fights.

If you tell me your time zone, I can convert the start times. I can also show the Boxerbook forecasts for any of these fights.

Source: [Boxerbook](https://boxerbook.com/schedule?utm_source=claude-skill)

## Final answer

Boxerbook lists 71 bouts on 15 cards from Friday 6 to Sunday 8 November 2026. These are the main ones. Times are when each card starts, in UTC. Main events usually begin 2–4 hours later. Records are going into each fight.

## Saturday 7 Nov: London, Copper Box Arena
**Card starts 16:30 UTC · Sky Sports** · [Card](https://boxerbook.com/events/11861/2026-11-07-london?utm_source=claude-skill)
- [Chris Billam-Smith (22-2) vs Cheavon Clarke (12-2)](https://boxerbook.com/bouts/192142/cheavon-clarke-vs-chris-billam-smith?utm_source=claude-skill): cruiserweight, 10 rounds
- [Denzel Bentley (31-3-1) vs Shane Mosley Jr.](https://boxerbook.com/bouts/192143/shane-mosley-jr-vs-denzel-bentley?utm_source=claude-skill): middleweight, 12 rounds
- [Umar Dzambekov (13-0) vs Zach Parker (26-2)](https://boxerbook.com/bouts/192144/zach-parker-vs-umar-dzambekov?utm_source=claude-skill): light heavyweight, 10 rounds
- Also on the card: Ezra Taylor (13-1) vs Bradley Rea, plus prospects Da'Mazion Vanhouter and Sam Hickey

## Saturday 7 Nov: Manchester Arena
**Card starts 21:00 UTC · DAZN (Spain, Mexico, US Spanish-language listed)** · [Card](https://boxerbook.com/events/11860/2026-11-07-manchester?utm_source=claude-skill)
- [Joshua Buatsi (20-1) vs Willy Hutchinson (20-2)](https://boxerbook.com/bouts/192140/willy-hutchinson-vs-joshua-buatsi?utm_source=claude-skill): **vacant WBC interim light heavyweight title**, 12 rounds
- [Jack Rafferty (27-0-1) vs Hovhannes Martirosyan](https://boxerbook.com/bouts/192141/hovhannes-martirosyan-vs-jack-rafferty?utm_source=claude-skill): super lightweight, 12 rounds

## Saturday 7 Nov: Albuquerque, US
**DAZN (worldwide) · start time not on record** · [Card](https://boxerbook.com/events/11862/2026-11-07-albuquerque?utm_source=claude-skill)
- [Abraham Perez (15-0) vs Yankiel Rivera (7-1-1)](https://boxerbook.com/bouts/192148/yankiel-rivera-vs-abraham-perez?utm_source=claude-skill): **WBA interim flyweight title**, 12 rounds

## Sunday 8 Nov, 01:00 UTC (Saturday evening in the US): Arlington, US
**ESPN / ESPN+ (US)** · [Card](https://boxerbook.com/events/11863/2026-11-08-arlington?utm_source=claude-skill). This card is stacked with women's title fights:
- [Alycia Baumgardner (18-1) vs Elif Nur Turhan (15-0)](https://boxerbook.com/bouts/192149/elif-nur-turhan-vs-alycia-baumgardner?utm_source=claude-skill): **IBF women's lightweight title**
- [Tiara Brown (21-0) vs Ellie Scotney (13-0)](https://boxerbook.com/bouts/192182/tiara-brown-vs-ellie-scotney?utm_source=claude-skill): women's featherweight, unbeaten vs unbeaten
- [Skye Nicolson (16-1) vs Miyo Yoshida (20-5)](https://boxerbook.com/bouts/192152/miyo-yoshida-vs-skye-nicolson?utm_source=claude-skill): **WBC junior featherweight title**
- [Ramla Ali (11-2) vs Mikiah Kreps](https://boxerbook.com/bouts/192151/ramla-ali-vs-mikiah-kreps?utm_source=claude-skill): **vacant WBO and IBF women's junior featherweight titles**
- [Irma García (26-5-1) vs Nataly Delgado (21-8-2)](https://boxerbook.com/bouts/192150/nataly-delgado-vs-irma-garcia?utm_source=claude-skill): **IBF women's junior bantamweight title**
- [Brittany Sims (2-0) vs Shera Mae Patricio (3-0)](https://boxerbook.com/bouts/192153/brittany-sims-vs-shera-mae-patricio?utm_source=claude-skill): **vacant WBA "regular" women's bantamweight title**

## Other cards
- **Friday 6 Nov, 07:00 UTC:** [Paul Gallen (16-2-1) vs Nelson Asofa-Solomona (1-0)](https://boxerbook.com/bouts/194029/paul-gallen-vs-nelson-asofa-solomona?utm_source=claude-skill). Boxerbook has no venue or broadcaster for this one yet.
- **Saturday 7 Nov, Korakuen Hall, Tokyo (U-NEXT, Japan):** [Kenichi Ogawa (32-2-1) vs Jae-woo Lee](https://boxerbook.com/bouts/193310/jae-woo-lee-vs-kenichi-ogawa?utm_source=claude-skill) and Yamato Hata (19-2-1) vs Ryō Sagawa (14-5)
- **Saturday 7 Nov, Miami (TrillerTV / Integrated Sports PPV):** [Maria Luz Peral vs Yokasta Valle](https://boxerbook.com/bouts/193234/maria-luz-peral-vs-yokasta-valle?utm_source=claude-skill)
- **Saturday 7 Nov, Istanbul:** Mourad Aliev (15-1-1) vs Umut Camkiran, heavyweight
- There are also smaller shows in Hoddesdon, Alfreton, Doncaster, Manchester (Wythenshawe Forum), Sakai (Japan) and Caracas, mostly prospects and debut fights.

If you tell me your time zone, I can convert the start times. I can also show the Boxerbook forecasts for any of these fights.

Source: [Boxerbook](https://boxerbook.com/schedule?utm_source=claude-skill)

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
    "notes": "Facts match the tool results (cards, titles, records, broadcasters, UTC times); it admits the missing Albuquerque start time. Minor extras like 'Tokyo' and the '2–4 hours later' remark come from general knowledge."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": true
  },
  "usd": 0.1851
}
```

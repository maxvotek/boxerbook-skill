# en-weekend (rest)

**Prompt (en):** What boxing is on this weekend?

**Expected:** Calls the schedule for the weekend; leads with title fights / main events; gives dates, venues/cities, card start times (noting they are card start, in UTC or converted), broadcasters when present; links cards or bouts; a Boxerbook source line.

## Trace

**tool** `run_helper` `{"args": ["schedule", "--when", "weekend"]}`

```
{"when":"weekend","from":"2026-11-06","to":"2026-11-08","country":null,"division":null,"truncated":false,"events":[{"id":11955,"date":"2026-11-06","venue":"The Spotlight","city":"Hoddesdon","country":"GB","promoter":null,"broadcasts":[],"url":"https://boxerbook.com/events/11955/2026-11-06-hoddesdon?utm_source=claude-skill","bouts":[{"id":193266,"date":"2026-11-06","status":"scheduled","a":{"name":"Hamza Mehmood","record":null},"b":{"id":25593,"name":"Erick Omar Lopez","slug":"erick-omar-lopez-b25593","record":"0-2-0"},"display":["b","a"],"division":"other","scheduled_rounds":null,"title_text":null,"url":"https://boxerbook.com/bouts/193266/hamza-mehmood-vs-erick-omar-lopez?utm_source=claude-skill","forecast":{"p_a":0.5569,"as_of":"2026-10-31","run_id":13}},{"id":193267,"date":"2026-11-06","status":"scheduled","a":{"name":"Jamie Robinson","record":null},"b":{"id":21299,"name":"Connor Meanwell","slug":"connor-meanwell-b21299","record":"0-3-0"},"display":["b","a"],"division":"other","scheduled_rounds":null,"title_text":null,"url":"https://boxerbook.com/bouts/193267/jamie-robinson-vs-connor-meanwell?utm_source=claude-skill","forecast":{"p_a":0.5013,"as_of":"2026-10-30","run_id":13}},{"id":193268,"date":"2026-11-06","status":"scheduled","a":{"id":30059,"name":"Doru Mogos","slug":"doru-mogos-b30059","record":"1-0-0"},"b":{"id":21870,"name":"Alex Carter","slug":"alex-carter-b21870","record":"0-0-0"},"display":["a","b"],"division":"other","scheduled_rounds":null,"title_text":null,"url
... [35591 chars]
```

**assistant (interim)**

Here's this weekend's boxing in Boxerbook, Friday 6 to Sunday 8 November 2026. Your time zone isn't known, so times are UTC. Where a time is listed for a single fight, Boxerbook gives it for that fight. Otherwise the time is when the card starts, not the main event. Records are each boxer's record going into the fight.

## Saturday 7 Nov: main cards

**[Manchester Arena, Manchester, UK](https://boxerbook.com/events/11860/2026-11-07-manchester?utm_source=claude-skill)**: card starts 21:00 UTC. Shown on DAZN in Spain, Mexico and to Spanish-language viewers in the US (Boxerbook lists no UK broadcaster)
- [Joshua Buatsi (20-1-0) vs Willy Hutchinson (20-2-0)](https://boxerbook.com/bouts/192140/willy-hutchinson-vs-joshua-buatsi?utm_source=claude-skill), 12 rounds, "Vacant WBC interim light heavyweight title", 22:00 UTC
- [Jack Rafferty (27-0-1) vs Hovhannes Martirosyan](https://boxerbook.com/bouts/192141/hovhannes-martirosyan-vs-jack-rafferty?utm_source=claude-skill), 12 rounds, super lightweight, 21:00 UTC

**[Copper Box Arena, Queen Elizabeth Olympic Park, London, UK](https://boxerbook.com/events/11861/2026-11-07-london?utm_source=claude-skill)**: card starts 16:30 UTC. Shown on Sky Sports worldwide
- [Chris Billam-Smith (22-2-0) vs Cheavon Clarke (12-2-0)](https://boxerbook.com/bouts/192142/cheavon-clarke-vs-chris-billam-smith?utm_source=claude-skill), cruiserweight, 10 rounds, 22:00 UTC
- [Denzel Bentley (31-3-1) vs Shane Mosley Jr.](https://boxerbook.com/bouts/192143/shane-mosley-jr-vs-denzel-bentley?utm_source=claude-skill), middleweight, 12 rounds, 21:00 UTC
- [Umar Dzambekov (13-0-0) vs Zach Parker (26-2-0)](https://boxerbook.com/bouts/192144/zach-parker-vs-umar-dzambekov?utm_source=claude-skill), light heavyweight, 10 rounds, 20:00 UTC
- Also on the card: [Ezra Taylor vs Bradley Rea](https://boxerbook.com/bouts/193151/ezra-taylor-vs-bradley-rea?utm_source=claude-skill), [Da'Mazion Vanhouter vs Ivan Balaz](https://boxerbook.com/bouts/192146/da-mazion-vanhouter-vs-ivan-balaz?utm_source=claude-skill) and [Sam Hickey vs Troy Coleman](https://boxerbook.com/bouts/192147/troy-coleman-vs-sam-hickey?utm_source=claude-skill)

**[Albuquerque, USA](https://boxerbook.com/events/11862/2026-11-07-albuquerque?utm_source=claude-skill)**: shown on DAZN worldwide
- [Abraham Perez (15-0-0) vs Yankiel Rivera (7-1-1)](https://boxerbook.com/bouts/192148/yankiel-rivera-vs-abraham-perez?utm_source=claude-skill), 12 rounds, "WBA interim flyweight title"

**[Korakuen Hall, Japan](https://boxerbook.com/events/11915/2026-11-07?utm_source=claude-skill)**: shown on U-NEXT in Japan
- [Kenichi Ogawa (32-2-1) vs Jae-woo Lee](https://boxerbook.com/bouts/193310/jae-woo-lee-vs-kenichi-ogawa?utm_source=claude-skill), super featherweight, 10 rounds
- [Yamato Hata (19-2-1) vs Ryō Sagawa (14-5-0)](https://boxerbook.com/bouts/193311/ryo-sagawa-vs-yamato-hata?utm_source=claude-skill), super featherweight, 10 rounds

## Sunday 8 Nov (local date): women's title card in [Arlington, USA](https://boxerbook.com/events/11863/2026-11-08-arlington?utm_source=claude-skill)
Card starts at 01:00 UTC on 9 Nov. Shown on ESPN and ESPN+ (US)
- [Alycia Baumgardner (18-1-0) vs Elif Nur Turhan (15-0-0)](https://boxerbook.com/bouts/192149/elif-nur-turhan-vs-alycia-baumgardner?utm_source=claude-skill), "IBF women's lightweight title", 04:00 UTC
- [Skye Nicolson (16-1-0) vs Miyo Yoshida (20-5-0)](https://boxerbook.com/bouts/192152/miyo-yoshida-vs-skye-nicolson?utm_source=claude-skill), "WBC junior featherweight title", 02:00 UTC
- [Ramla Ali (11-2-0) vs Mikiah Kreps](https://boxerbook.com/bouts/192151/ramla-ali-vs-mikiah-kreps?utm_source=claude-skill), "Vacant WBO and IBF women's junior featherweight titles", 01:00 UTC
- [Irma García (26-5-1) vs Nataly Delgado (21-8-2)](https://boxerbook.com/bouts/192150/nataly-delgado-vs-irma-garcia?utm_source=claude-skill), "IBF women's junior bantamweight title and Delgado's WBA women's juniot bantamweight title" (quoted exactly as Boxerbook lists it)
- [Tiara Brown (21-0-0) vs Ellie Scotney (13-0-0)](https://boxerbook.com/bouts/192182/tiara-brown-vs-ellie-scotney?utm_source=claude-skill)
- Also: [Brittany Sims vs Shera Mae Patricio](https://boxerbook.com/bouts/192153/brittany-sims-vs-shera-mae-patricio?utm_source=claude-skill), "Vacant WBA "regular" women's bantamweight title"

## Friday 6 Nov
- [Paul Gallen (16-2-1) vs Nelson Asofa-Solomona (1-0-0)](https://boxerbook.com/bouts/194029/paul-gallen-vs-nelson-asofa-solomona?utm_source=claude-skill), 07:00 UTC. Boxerbook doesn't list a venue or broadcaster for this one
- A small card at [The Spotlight, Hoddesdon, UK](https://boxerbook.com/events/11955/2026-11-06-hoddesdon?utm_source=claude-skill)

## Smaller Saturday cards
- [Istanbul](https://boxerbook.com/events/11877/2026-11-07-istanbul?utm_source=claude-skill): Mourad Aliev (15-1-1) vs Umut Camkiran
- [Miami](https://boxerbook.com/events/11927/2026-11-07-miami?utm_source=claude-skill): Yokasta Valle vs Maria Luz Peral, on Integrated Sports PPV and TrillerTV
- [Sakai, Japan](https://boxerbook.com/events/5227/2026-11-07?utm_source=claude-skill): shown on YouTube
- Others in [Caracas](https://boxerbook.com/events/11878/2026-11-07-caracas?utm_source=claude-skill), [Alfreton](https://boxerbook.com/events/11963/2026-11-07-alfreton?utm_source=claude-skill), [Manchester (Wythenshawe Forum)](https://boxerbook.com/events/11964/2026-11-07-manchester?utm_source=claude-skill), [Manchester Arena (second card)](https://boxerbook.com/events/11965/2026-11-07-manchester?utm_source=claude-skill), [Doncaster](https://boxerbook.com/events/11967/2026-11-07-doncaster?utm_source=claude-skill) and [Hackney Wick](https://boxerbook.com/events/11966/2026-11-07-hackney-wick?utm_source=claude-skill)

If you tell me your time zone, I can convert these times. I can also preview any of these fights.

Source: [Boxerbook](https://boxerbook.com/schedule?utm_source=claude-skill), as of 2 Nov 2026

## Final answer

Here's this weekend's boxing in Boxerbook, Friday 6 to Sunday 8 November 2026. Your time zone isn't known, so times are UTC. Where a time is listed for a single fight, Boxerbook gives it for that fight. Otherwise the time is when the card starts, not the main event. Records are each boxer's record going into the fight.

## Saturday 7 Nov: main cards

**[Manchester Arena, Manchester, UK](https://boxerbook.com/events/11860/2026-11-07-manchester?utm_source=claude-skill)**: card starts 21:00 UTC. Shown on DAZN in Spain, Mexico and to Spanish-language viewers in the US (Boxerbook lists no UK broadcaster)
- [Joshua Buatsi (20-1-0) vs Willy Hutchinson (20-2-0)](https://boxerbook.com/bouts/192140/willy-hutchinson-vs-joshua-buatsi?utm_source=claude-skill), 12 rounds, "Vacant WBC interim light heavyweight title", 22:00 UTC
- [Jack Rafferty (27-0-1) vs Hovhannes Martirosyan](https://boxerbook.com/bouts/192141/hovhannes-martirosyan-vs-jack-rafferty?utm_source=claude-skill), 12 rounds, super lightweight, 21:00 UTC

**[Copper Box Arena, Queen Elizabeth Olympic Park, London, UK](https://boxerbook.com/events/11861/2026-11-07-london?utm_source=claude-skill)**: card starts 16:30 UTC. Shown on Sky Sports worldwide
- [Chris Billam-Smith (22-2-0) vs Cheavon Clarke (12-2-0)](https://boxerbook.com/bouts/192142/cheavon-clarke-vs-chris-billam-smith?utm_source=claude-skill), cruiserweight, 10 rounds, 22:00 UTC
- [Denzel Bentley (31-3-1) vs Shane Mosley Jr.](https://boxerbook.com/bouts/192143/shane-mosley-jr-vs-denzel-bentley?utm_source=claude-skill), middleweight, 12 rounds, 21:00 UTC
- [Umar Dzambekov (13-0-0) vs Zach Parker (26-2-0)](https://boxerbook.com/bouts/192144/zach-parker-vs-umar-dzambekov?utm_source=claude-skill), light heavyweight, 10 rounds, 20:00 UTC
- Also on the card: [Ezra Taylor vs Bradley Rea](https://boxerbook.com/bouts/193151/ezra-taylor-vs-bradley-rea?utm_source=claude-skill), [Da'Mazion Vanhouter vs Ivan Balaz](https://boxerbook.com/bouts/192146/da-mazion-vanhouter-vs-ivan-balaz?utm_source=claude-skill) and [Sam Hickey vs Troy Coleman](https://boxerbook.com/bouts/192147/troy-coleman-vs-sam-hickey?utm_source=claude-skill)

**[Albuquerque, USA](https://boxerbook.com/events/11862/2026-11-07-albuquerque?utm_source=claude-skill)**: shown on DAZN worldwide
- [Abraham Perez (15-0-0) vs Yankiel Rivera (7-1-1)](https://boxerbook.com/bouts/192148/yankiel-rivera-vs-abraham-perez?utm_source=claude-skill), 12 rounds, "WBA interim flyweight title"

**[Korakuen Hall, Japan](https://boxerbook.com/events/11915/2026-11-07?utm_source=claude-skill)**: shown on U-NEXT in Japan
- [Kenichi Ogawa (32-2-1) vs Jae-woo Lee](https://boxerbook.com/bouts/193310/jae-woo-lee-vs-kenichi-ogawa?utm_source=claude-skill), super featherweight, 10 rounds
- [Yamato Hata (19-2-1) vs Ryō Sagawa (14-5-0)](https://boxerbook.com/bouts/193311/ryo-sagawa-vs-yamato-hata?utm_source=claude-skill), super featherweight, 10 rounds

## Sunday 8 Nov (local date): women's title card in [Arlington, USA](https://boxerbook.com/events/11863/2026-11-08-arlington?utm_source=claude-skill)
Card starts at 01:00 UTC on 9 Nov. Shown on ESPN and ESPN+ (US)
- [Alycia Baumgardner (18-1-0) vs Elif Nur Turhan (15-0-0)](https://boxerbook.com/bouts/192149/elif-nur-turhan-vs-alycia-baumgardner?utm_source=claude-skill), "IBF women's lightweight title", 04:00 UTC
- [Skye Nicolson (16-1-0) vs Miyo Yoshida (20-5-0)](https://boxerbook.com/bouts/192152/miyo-yoshida-vs-skye-nicolson?utm_source=claude-skill), "WBC junior featherweight title", 02:00 UTC
- [Ramla Ali (11-2-0) vs Mikiah Kreps](https://boxerbook.com/bouts/192151/ramla-ali-vs-mikiah-kreps?utm_source=claude-skill), "Vacant WBO and IBF women's junior featherweight titles", 01:00 UTC
- [Irma García (26-5-1) vs Nataly Delgado (21-8-2)](https://boxerbook.com/bouts/192150/nataly-delgado-vs-irma-garcia?utm_source=claude-skill), "IBF women's junior bantamweight title and Delgado's WBA women's juniot bantamweight title" (quoted exactly as Boxerbook lists it)
- [Tiara Brown (21-0-0) vs Ellie Scotney (13-0-0)](https://boxerbook.com/bouts/192182/tiara-brown-vs-ellie-scotney?utm_source=claude-skill)
- Also: [Brittany Sims vs Shera Mae Patricio](https://boxerbook.com/bouts/192153/brittany-sims-vs-shera-mae-patricio?utm_source=claude-skill), "Vacant WBA "regular" women's bantamweight title"

## Friday 6 Nov
- [Paul Gallen (16-2-1) vs Nelson Asofa-Solomona (1-0-0)](https://boxerbook.com/bouts/194029/paul-gallen-vs-nelson-asofa-solomona?utm_source=claude-skill), 07:00 UTC. Boxerbook doesn't list a venue or broadcaster for this one
- A small card at [The Spotlight, Hoddesdon, UK](https://boxerbook.com/events/11955/2026-11-06-hoddesdon?utm_source=claude-skill)

## Smaller Saturday cards
- [Istanbul](https://boxerbook.com/events/11877/2026-11-07-istanbul?utm_source=claude-skill): Mourad Aliev (15-1-1) vs Umut Camkiran
- [Miami](https://boxerbook.com/events/11927/2026-11-07-miami?utm_source=claude-skill): Yokasta Valle vs Maria Luz Peral, on Integrated Sports PPV and TrillerTV
- [Sakai, Japan](https://boxerbook.com/events/5227/2026-11-07?utm_source=claude-skill): shown on YouTube
- Others in [Caracas](https://boxerbook.com/events/11878/2026-11-07-caracas?utm_source=claude-skill), [Alfreton](https://boxerbook.com/events/11963/2026-11-07-alfreton?utm_source=claude-skill), [Manchester (Wythenshawe Forum)](https://boxerbook.com/events/11964/2026-11-07-manchester?utm_source=claude-skill), [Manchester Arena (second card)](https://boxerbook.com/events/11965/2026-11-07-manchester?utm_source=claude-skill), [Doncaster](https://boxerbook.com/events/11967/2026-11-07-doncaster?utm_source=claude-skill) and [Hackney Wick](https://boxerbook.com/events/11966/2026-11-07-hackney-wick?utm_source=claude-skill)

If you tell me your time zone, I can convert these times. I can also preview any of these fights.

Source: [Boxerbook](https://boxerbook.com/schedule?utm_source=claude-skill), as of 2 Nov 2026

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
    "notes": "The facts check out against the tool data: records, times, broadcasters, titles, and the 'Sunday 8 Nov (local date)' note for the 01:00 UTC 9 Nov card start. Linked cards and bouts, a Boxerbook source line, and explicit dates are all present. No odds or probabilities are given, so no betting disclaimer is needed. The Sunday section's Delgado bout and the Brown vs Scotney bout have no listed start time, and the answer does not claim one."
  },
  "checks": {
    "used_data_tool": true,
    "has_boxerbook_link": true,
    "lang_heuristic": true,
    "utm_tagged": true,
    "read_reference": false
  },
  "usd": 0.1504
}
```

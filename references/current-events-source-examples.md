# Current-Events Source Examples (Polish Wikipedia)

## Example: Ch-101 Missile Incident (30 July 2026)

### Incident Summary
During a large-scale Russian missile attack on western Ukraine (night of 29-30 July 2026), two cruise missiles headed toward the Polish border. Ukrainian MiG-29 fighters pursued them trying to shoot them down. One missile entered Polish airspace at 3:40 and fell near Tarnawa-Kolonia, Lubelskie, creating a ~10m crater.

### Sources Used

| Source | Type | What it covers |
|--------|------|----------------|
| [Defence24 - Jakub Palowski](https://defence24.pl/wojna-na-ukrainie-raport-specjalny-defence24/rosyjska-rakieta-nad-polska-dlaczego-nie-zostala-zestrzelona-opinia) | Specialist military analysis | MiG-29 presence near border, radar identification challenges, timeline (3:29/3:40/3:46), legal basis for engagement |
| [niezalezna.pl (Telewizja Republika)](https://niezalezna.pl/polska/w-strone-polski-lecialy-dwa-pociski-ukrainskie-mysliwce-do-samej-granicy-probowaly-je-zniszczyc/576081) | News (direct quote from PM Tusk) | "ukraińskie myśliwce do samej granicy próbowały zniszczyć te pociski" — two missiles, not one |
| [TVN24 - Maciej Wacławik](https://tvn24.pl/polska/tarnawa-kolonia-wybuch-rakieta-manewrujaca-ch-101-co-o-niej-wiemy-st9165218) | Major news outlet | General Bieniek: "Myśliwce ukraińskie walczyły przez kilka godzin... niestety ten jeden się przedarł" |
| [Onet](https://wiadomosci.onet.pl/kraj/krater-na-lubelszczyznie-sa-nagrania-z-miejsca-wybuchu-relacja-na-zywo/bbqe1qj) | Major news outlet | Live coverage, timeline, international reactions |

### Key Sourcing Lessons
1. **Defence24 is the most authoritative** for military-technical analysis (Jakub Palowski is a respected defence journalist)
2. **Direct quotes from officials** (PM Tusk) can be sourced via any outlet that faithfully reproduces them
3. **Cross-reference timelines** — different outlets may report different times (TVN24 said 3:46 for detection, Defence24 gave 3:29/3:40/3:46 for different events)
4. **The "zboczył z kursu" framing** was not supported by any source — the missiles were heading toward the border, not deviating randomly

### DuckDuckGo Lite Search Template
```bash
curl -s -L "https://lite.duckduckgo.com/lite/" \
  -H "User-Agent: Mozilla/5.0" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "q=SEARCH_TERMS&kl=pl-pl" \
  | sed -n '/<table border="0">/,/<\/table>/p' \
  | sed 's/<[^>]*>//g'
```

### Browser Console Text Extraction
```javascript
// For most Polish news sites:
document.querySelector('article')?.innerText

// For sites without <article> tag:
document.body.innerText
```

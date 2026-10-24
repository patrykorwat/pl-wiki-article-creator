# Sourcing Strategy for NGO/Organization Articles

## Problem
The main definition of an NGO's scope of activities relies on a single source (often a news article or the organization's own website). Wikipedia requires independent, verifiable sources for definitions.

## Solution: Statute + Independent News

Combine two types of sources:

### 1. Organization's Statute (źródło pierwotne)
The statute (statut) is the founding document that legally defines the organization's goals and activities. It is acceptable as a primary source for what the organization *states* its goals to be.

**Where to find it:**
- Organization's website → "O nas" / "O fundacji" page → "statut" link
- Often a PDF or dedicated subpage (e.g., `omzrik.pl/statut`)
- KRS online database (https://ekrs.ms.gov.pl) — search by KRS number
- If not publicly available, note that the organization does not publish it

**What to cite:**
- Specific paragraphs (§) that describe the scope of activities
- §7 (Cele) and §8 (Sposoby realizacji) are typically the most relevant
- Format: `{{cytuj |tytuł = Statut [Organization Name] |url = https://... |opublikowany = [Organization Name] |data dostępu = YYYY-MM-DD}}`

### 2. Independent News Article (źródło wtórne)
Find a reputable news article that describes the organization's activities in its own words.

**Good sources for Polish NGOs:**
- Gazeta.pl, Onet, Wirtualna Polska — major news portals
- Polska Agencja Prasowa (PAP) — wire service
- Press.pl — media industry news
- Polskie Radio (regional stations like Radio Białystok)
- Rzeczpospolita, Gazeta Wyborcza — quality press

**What to look for:**
- Articles that describe the organization in a sentence or two
- Often found in articles about the organization's legal cases, controversies, or leadership
- The description is usually in the second or third paragraph (the "nut graf")

### 3. Zero.pl / Investigative Portals
Zero.pl and similar investigative outlets are acceptable as sources but should not be the *only* source for a definition. Use them in combination with at least one independent source.

## Workflow

1. **Read the existing article** — identify which claims rely on a single source
2. **Check the organization's website** for the statute or "O nas" page
3. **Search for independent news articles** that describe the organization
   - Use DuckDuckGo Lite or Bing (Google blocks automated queries)
   - Search for the organization's full name + keywords like "działalność", "organizacja pozarządowa", "fundacja"
4. **Extract the relevant passage** from each source
   - For the statute: look at §7 (Cele) and §8 (Sposoby realizacji)
   - For news articles: look for the sentence that defines what the org does
5. **Add both sources** to the definition with `<ref>`
6. **Verify URLs** resolve before adding them

## Example: OMZRiK

**Problem:** Definition sourced only to Zero.pl.

**Statute (§8 pkt 1, 3, 10):**
> 1. Pomoc osobom dyskryminowanym w ujawnianiu przestępstw popełnianych wobec nich z nienawiści, z pobudek rasistowskich i ksenofobicznych.
> 3. współpraca z organami ścigania w tym Policją, Prokuraturą oraz Strażą Miejską [...]
> 10. działania na rzecz ujawniania sprawców przestępstw związanych z krzywdzeniem ludzi z pobudek rasistowskich, antysemickich i ksenofobicznych oraz uczestniczenie w procesach sądowych w takich sprawach

**Gazeta.pl (independent source):**
> "organizacji pozarządowej, która zajmuje się przeciwdziałaniem i zwalczaniem przejawów rasizmu, ksenofobii i nietolerancji"

**Result:** Three sources (statute + Gazeta.pl + Zero.pl) instead of one.

## Pitfalls

- **Statute is a primary source** — use it for what the organization *states* its goals are, not for claims about its actual activities or effectiveness
- **Not all NGOs publish their statute** — if unavailable, rely on multiple independent news sources
- **The statute may use broad/generic language** (e.g., "pomoc społeczna", "działalność charytatywna") — focus on the specific paragraphs about monitoring, reporting, and legal action
- **News articles may use the same language as the organization's PR** — prefer articles that describe the org in the journalist's own words, not press release quotes
- **Check the statute date** — if it's old, the organization may have changed its activities. Look for amendments.

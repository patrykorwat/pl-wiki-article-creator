# NPOV Cleanup Patterns for Controversial Organization Articles

## Common NPOV Violations

### 1. Loaded Lead
**Bad**: "skrajnie prawicowa i ultrakonserwatywna fundacja"
**Good**: "fundacja założona w 2013, prowadząca działalność legislacyjną i interwencje procesowe. Niektóre media określają ją jako..."

### 2. Prejudicial Infobox Images
- Protest photos, negative imagery → remove or replace with logo/neutral image
- Example: Fundacja Pro had a photo of an anti-LGBT protest in its infobox

### 3. "Kontrowersje" Section
- Rename to neutral title: "Działalność międzynarodowa i spory sądowe"
- Remove sections that are pure advocacy:
  - "Strategie manipulacji" (manipulation strategies)
  - "Afera obyczajowa" (personal scandals/gossip)

### 4. Unattributed Criticism
**Bad**: "Kampania opiera się na podważanych badaniach"
**Good**: "Według krytyków kampania opiera się na badaniach, których metodologia została zakwestionowana w literaturze naukowej"

### 5. Pejorative Labels in Wikipedia's Voice
- "homofobusy" → "nazywane w niektórych mediach homofobusami"
- "Bully Lawyers" → remove or attribute
- "sekta" → remove or attribute to specific source

### 6. Speculation Sections
- "Oskarżenia o związki z Rosją" — trim to verifiable facts only
- Remove: IPN speculation about distant relatives, uncorroborated claims
- Keep: documented facts (e.g., signed support for Russian law, participation in international networks)

### 7. Source Overload
- 7+ citations for one claim → consolidate to 1-2 strongest
- Remove YouTube videos as sources
- Prefer academic journals over media for classification

### 8. Church/Organization Relationship
- Don't assume an organization represents the Catholic Church unless the Church confirms it
- If the Church has distanced itself, saying the org "articulates the Church's postulates" is misleading
- Check: has the Episcopate or Vatican issued any statement about the organization?
- The Brazilian bishops' 1985 warning against TFP is about TFP, not Ordo Iuris directly — don't conflate

### 9. Unsourced Claims After Cleanup
- When removing sources during cleanup, check if the claim itself needs to be removed too
- Example: "Ordo Iuris założyło oddziały w Chorwacji i Hiszpanii" — if the sources were removed, the claim goes too

### 10. Promotional Language in "Cele i ich realizacja"
- Remove phrases like "podejmuje się przekazywania społeczeństwu informacji", "formacja młodych prawników"
- These are the organization's own self-description, not neutral encyclopedia content
- Replace with factual descriptions: "prowadzi interwencje procesowe, opracowuje projekty ustaw"
- Rename section from "Cele i ich realizacja" to "Działalność"

## Source Hierarchy for Political Classification
1. Peer-reviewed academic journals (best) — e.g., Curanović (2021) in *Religions*, Bustikova (2025) in *Journal of Illiberalism Studies*
2. Court rulings
3. Reputable media with attributed claims
4. Activist/advocacy publications (avoid for definitions)

## Lead Structure for Organization Articles
1. **First paragraph**: factual description — what the org IS (foundation, institute), what it DOES (legislative work, legal interventions), founding details, affiliations
2. **Second paragraph**: classification — academic/media labels, budget, international presence
3. **Never** start with political labels ("skrajnie prawicowa") in Wikipedia's voice. Attribute them: "Niektóre media określają ją jako..."
4. **Never** add "think tank" without a verifiable source — the org calling itself an "instytut" is not sufficient
5. **Avoid repeating phrases** like "W literaturze przedmiotu" twice in one lead. Use synonyms: "W badaniach naukowych", "Klasyfikowana jest jako", "Opisywana jest jako"

## Academic Sources for Ordo Iuris Classification
- Curanović, A. (2021). "The International Activity of Ordo Iuris. The Central European Actor and the Global Christian Right." *Religions*, 12(12). DOI: 10.3390/rel12121038 — describes OI as a conservative pro-life legal organization and part of the global Christian right; notes OI is "not officially affiliated with the local Catholic Church"
- Bustikova, L. (2025). "Kill the Bill: Ordo Iuris and the Ratification of the Istanbul Convention in the Czech Senate." *Journal of Illiberalism Studies*. DOI: 10.53483/zcrz3615 — describes OI as a "Polish Catholic conservative legal network"
- Hanisch. "Ordo Iuris. Fundamental-katholische Juristen im Kampf um Deutungshoheit." *Polen-Analysen*. DOI: 10.31205/pa.333.01 — describes OI as fundamental Catholic lawyers

## Large File Editing
For articles >50K chars, use Python string manipulation:
1. Read file with open().read()
2. Use content.replace(old, new) for targeted changes
3. Write with open().write()
4. Write script to .py file first to avoid heredoc quote escaping issues
5. When the file doesn't change after write(), check if the old_string actually exists in the file — encoding or character differences may prevent matching
6. Use re.search() with DOTALL flag for multi-line matches when exact text is uncertain
7. **Write-then-verify**: after write(), immediately read the file back and check if the change was applied. If not, the old_string didn't match — try a shorter substring or use regex.

## URL Hygiene
- Polish characters (ł, ś, ć, ż, ź, ą, ę, ó, ń) in URLs must be URL-encoded or replaced with ASCII equivalents (ł→l, ś→s, etc.)
- Check that URLs with Polish characters actually resolve before adding them
- Backslash-escaped quotes (\\") in wikitext are a sign of copy-paste from API output — replace with proper Polish quotation marks („...") or regular ASCII quotes

## Lead Structure for Concept Articles (e.g., "Retoryka anty-LGBTQ")
1. **Descriptive, not normative**: Start with "Termin używany w literaturze naukowej do opisu..." not "X to zbiór... charakteryzujących się..."
2. **Attribute claims to researchers**: "które – według badaczy – charakteryzują się..." not "które charakteryzują się..."
3. **Avoid framing the entire article in one interpretive lens** (e.g., "moral panic → conspiracy → dehumanization → violence"). Let the body sections develop the analysis.
4. **Avoid overgeneralization**: "części środowisk konserwatywnych" not "konserwatywnej i prawicowej"; "Część konserwatywnych chrześcijan" not "Wielu konserwatywnych chrześcijan"
5. **Statistical category matching**: When comparing groups (e.g., perpetrators vs population), ensure the categories match. Don't compare "homosexual perpetrators" to "LGBT population" — compare homosexual to homosexual, or LGBT to LGBT.
6. **Remove unsourced historical claims**: Claims like "Opisywanie homoseksualizmu jako nienaturalnego sięga Platona, Arystotelesa i Tomasza z Akwinu" need sources. Plato's Symposium actually praises same-sex love — verify historical claims before adding them.

## Source Honesty (CRITICAL - reinforced)
- **Do not add sections that require sources you cannot verify.** If you add a "Krytyka i spory definicyjne" section, every claim in it must be backed by a source you have actually read. A section with hallucinated sources is worse than no section at all.
- **Just because a paper exists on a related topic doesn't mean it supports your specific claim.** Always check the abstract before citing. If the abstract doesn't mention your specific subtopic, the paper probably doesn't support your claim.
- **When you can't access the full text**: say so. Do not try to guess what the source says based on its title. The user will catch you.

## Write-Then-Verify Pattern
When editing files with Python:
1. After write(), immediately read the file back and check if the change was applied
2. If the file size didn't change, the old_string didn't match — try a shorter substring or use regex
3. Common causes of silent write failure: encoding differences (UTF-8 vs ASCII quotes), trailing whitespace, invisible characters

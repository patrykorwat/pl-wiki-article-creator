# EN→PL translation of a full article: workflow + pitfalls (from GGR task)

## Workflow that worked
0. Zanim zaczniesz: sprawdź na pl.wiki artykuł na TEN SAM i na SĄSIEDNI temat (batch `action=query&titles=...` — kandydaci nazwy + fraza nadrzędna). Artykuł sąsiedni (np. program publiczny vs pojęcie ogólne/rynek komercyjny) NIE jest miejscem tłumaczenia — twórz osobne hasło i skrzyżuj oba w „Zobacz też”; zlanie tematów o różnym zakresie psuje spójność obu artykułów.
1. Fetch source wikitext via API: `action=parse&page=<EN title>&prop=wikitext` → save to scratch file (do NOT rely on earlier scratch copies — they can be pruned; re-fetch if missing).
2. Translate section-by-section, APPENDING to the target .wiki file (one article per file, pliki .wiki do wklejenia, nie edytować wiki bezpośrednio).
3. Keep a running link-verification loop against pl.wiki.

## Link verification (must, before delivery)
- Extract `[[targets]]` with regex, skip Plik/File/Kategoria/Category.
- Verify ALL via `pl.wikipedia.org api.php action=query&prop=info` in batches of ≤40 (one call, `titles=A|B|C`); normalize/redirects handled by API response (`normalized`, `redirects`).
- First guess for a missing PL title: `en.wikipedia.org ...prop=langlinks&lllang=pl` (batch). Fallback: pl search `list=search`. If no PL article exists: link plain text, or {{link-interwiki|EN-name|Q=Qxxxx}}.
- QID format is literally `Q=Q1755300` (with Q prefix). Verify a QID with `www.wikidata.org action=wbgetentities&props=sitelinks|labels`: kryterium poprawności `{{link-interwiki}}` to sitelink enwiki OBECNY i plwiki NIEOBECNY; istnieje plwiki → zwykły [[link]] zamiast interwiki; brak sitelinka enwiki = encja podejrzana (QID-fallback wg SKILL).
- Rate limits: bursty API calls → HTTP 429. Sleep ≥2 s between batches (below ~1 s it fires constantly); on 429 back off 8–10 s and retry. Sekwencyjna pętla curl-per-tytuł (kilkadziesiąt wywołań) wywołuje throttling z PUSTYM body (JSONDecodeError) — pusta odpowiedź to NIE „brak artykułu”; batchuj ≤20–40 tytułów na wywołanie, a pełny finałowy przelot linków i tak robi verify_pl_wiki_article.py.
- A MISS in the batch title check can be a FALSE negative from title FORM (case, parenthetical variant: „Vox (partia)” vs „Vox (partia polityczna)”, „socjalistyczna” vs „Socjalistyczna”). Before declaring a link red, run `list=search` on the topic to find the correct PL form; only a search-miss means plain text.

## Przekład z selekcją: duży artykuł EN → limit znaków (nie kalka sekcja po sekcji)

Gdy źródło ma rzędu 150k znaków wikitextu i dziesiątki refów, a cel to hasło 15–20 tys. znaków (standard użytkownika dla tłumaczonych haseł), sekcja-po-sekcji się nie zmieści — pracuj w trybie selekcji:

1. Zbuduj pliki pomocnicze z wikitextu EN: (a) kopię z refami zamienionymi na markery `⟨name⟩` (czytelna proza do mapowania tez), (b) tabelę definicji refów name → url/tytuł/wydawca/data. Mapowanie „zdanie EN → refy” zrób funkcją refs_after(anchor, span): znajdź kotwicę tekstową zdania i wypisz nazwy refów w oknie N znaków za nią — każde zdanie PL musi wiedzieć, który ref EN je dokumentuje.
2. Pisz PL od zera w skróconej strukturze (dla wydarzeń: Tło/Przebieg/Reakcje + Komentarze), wybierając: liczby kluczowe, chronologię, główne stanowiska. Bibliografię refa EN przepisuj do formatu inline użytkownika (SKILL 3.1); nazwy refów dawaj czytelne i tematyczne.
3. Limitem steruj WYBOREM tez, nie ściskaniem wszystkiego: przy przekroczeniu limitu usuwaj CAŁE zdania niskiej wartości RAZEM z ich refami (anegdoty, drobne zatrzymania, wypowiedzi drugorzędnych polityków) — nigdy nie zostawiaj osieroconego `<ref name="x" />`. Po każdej rundzie cięć sprawdzaj bilans (definicje `<ref name="x">` vs skróty `<ref name="x" />`) i brak średników w prozie. Punkt odniesienia: EN 154k znaków/65 refów → PL ~18–19k znaków/44 refy.
4. Bilans ofiar („deaths”) w en.wiki bywa oparty o jeden ref przy infoboxie — w PL podawaj go serią datowaną (np. 72 → 100 → ≥141, każdy krok z datą i źródłem w prozie), nie pojedynczą liczbą; data i źródło ostatniej wartości wprost w tekście.
5. Infobox: `{{Wydarzenie infobox}}` NIE ma pól przyczyna/wynik/ofiary — szczegóły do prozy. Kategoria Commons świeżego wydarzenia często nie istnieje → pomijaj `commons`, zamiast tworzyć czerwoną kategorię.
6. Kategorie: tematyczne typu „Kryzysy migracyjne”, „Stosunki X–Y” często NIE istnieją — sprawdzaj batchem (namespace 0, prefiks `Kategoria:`); pewne są `Kategoria:YYYY w <państwie>`, `Kategoria:Wydarzenia RRRR` i kategoria miejscowości.

## EN wikitext → PL template mappings
- `{{blockquote|text|author=|source=}}` / `{{quote box}}` → `{{Cytat|treść=„…”|autor=…|źródło=…}}` (ref for the source goes INSIDE źródło= or after the template).
- EN `{{reflist|refs=...}}` with bare pointer-refs like `<ref name="Fest 1973, p. 210"/>` — PL uses inline refs: inline the full {{cytuj}} at each use.
- `{{citation needed}}` → `{{fakt}}`; `<ref group="nb">` → `group="uwaga"` + `<references group="uwaga" />`; `{{legend}}` in image caption → plain bullet list; `{{langx|de|X}}` → `(niem. ''X'')`.
- `{{Excerpt|Page|Section}}` w en to transkluzja — NIE przenoś sekcji 1:1. Pobierz wikitext artykułu NADRZĘDNEGO wskazanego w Excerpt (`action=parse&page=<Parent>`), weź właściwe akapity z ich refami i przełóż tylko tezy istotne dla hasła docelowego (sekcja en-owa bywa szersza niż zakres hasła).
- Bare-URL ref (`<ref> https://… </ref>`, bez tytułu/wydawcy) nie dokumentuje tezy: znajdź właściwe cytowanie tej samej tezy (sekcja References en, archiwum) albo usuń tezę; nigdy nie wstawiaj do refa PL samego gołego URL-a.
- Beware EN nested `"` inside quote text — strip stray `''` artifacts.

## Jednostki imperialne
Przeliczaj w Pythonie (akr = 4046,86 m²; galon US = 3,78541 l), zaokrąglaj do 2 miejsc i wstaw w prozie z „ok.” i przecinkiem dziesiętnym: „1200 akrów (ok. 4,9 km²)”, „17 mld galonów (ok. 64 mln m³)”. Jednostka oryginalna + przeliczenie w nawiasie, nie odwrotnie.

## Verified PL titles (GGR session) — reuse, don't re-search
Rabunek dzieci przez III Rzeszę (NOT „Porwanie…”); Plan Germania; Ochotniczy Fiński Batalion Waffen-SS; Korpus Bezpieczeństwa DeVlag; Strefa Wspólnego Dobrobytu Wielkiej Azji Wschodniej; Zjazd NSDAP; Rząd Quislinga; Rasa panów; Machtergreifung; Gleichschaltung; Narodowosocjalistyczny Ruch Holenderski; Hird (organizacja); Królestwo Włoch (1861–1946); Włócznia Przeznaczenia; Mikropaństwo (sg. only).
- „Germanic SS”: no PL article → `''Germańskie SS'' ({{link-interwiki|Germanic SS|Q=Q1108401}})`.
- Categories: use existing Kategoria:III Rzesza / Kategoria:Narodowy socjalizm / Kategoria:Niemcy podczas II wojny światowej; verify with prop=info (many EN-mirrored cat names are MISSING).
- Google Books / archive.org ids can be verified 200 by GET `books.google.com/books?id=X&printsec=frontcover` / `archive.org/details/X` (archive.org may time out; retry).
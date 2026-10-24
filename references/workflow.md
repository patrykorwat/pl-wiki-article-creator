# Workflow tworzenia artykułu

## Kolejność kroków

1. **Badanie tematu** — zbierz źródła (web_search, web_fetch).
2. **Ocena encyklopedyczności** — czy temat ma szansę zostać na Wikipedii.
3. **Wybór infoboxu** — dopasuj do typu hasła.
4. **Szkic** — lead + sekcje + przypisy.
5. **Weryfikacja przypisów** — każdy URL, każdy autor, każda data.
6. **Formatowanie** — cudzysłowy, myślniki, linki, kategorie.
7. **Podgląd** — sprawdź renderowanie (opcjonalnie) oraz wszystkie przypisy/linki/kategorie w pliku.
8. **Deliver** — gotowy wikitekst zostaw w pliku w katalogu `wiki/` i pokaż użytkownikowi do ręcznego wklejenia i zapisania na Wikipedii.

## Główna przestrzeń robocza = plik lokalny

- Cała praca nad artykułem toczy się w **jednym pliku** w katalogu `wiki/` (np. `wiki/Bechtel.wiki`) — to jest główna przestrzeń robocza, a nie brudnopis na Wikipedii (`Wikipedysta:Nazwa/brudnopis`).
- NIE używaj brudnopisów Wikipedii ani edytora WWW do pracy nad treścią. Plik lokalny jest źródłem prawdy (wersjonowanie, review, łatwy powrót).
- **Publikacja** = pokazanie gotowego pliku użytkownikowi. To użytkownik wkleja treść na Wikipedię i klika „Zapisz". Agent NIGDY nie edytuje Wikipedii przez przeglądarkę/API (hCaptcha, a przede wszystkim zasada: treść tylko do wglądu).

## Edycja istniejącego hasła (np. „aktualizuj X o to info")

Kolejność kroków, zanim cokolwiek napiszesz:

1. **Synchronizacja:** pobierz żywą wersję `action=parse&page=<Tytuł>&prop=wikitext&format=json`, NADPISUJ nią plik kanoniczny w `wiki/`. Nie edytuj starej lokalnej kopii.
2. **Sprawdź historię zmian** przed dalszą pracą: `action=query&prop=revisions&titles=...&rvprop=timestamp|user|comment|size`. Między lokalną kopią a wersją żywą mogły wejść obce edycje (boty usuwające `link-interwiki`, poprawki interpunkcji) — dzięki temu nie odtworzysz ich przypadkiem w swojej wersji, a cudzych zmian nie uznasz za własne.
3. **Przeczytaj dostarczone źródło w całości**, potem **skrzyżuj tezę w co najmniej jednym źródłem niezależnym** (agregator i komunikat prasowy to jedno źródło powtarzane, nie dwa). Dodawaj tylko fakty zapisane w źródłach, które otworzyłeś.
4. **Nie przenoś mechaniki transakcji z PR-u jednej strony** (kwoty opcji wyjścia, pakiety akcji, warunki put/call), jeśli nie ma ich w źródle niezależnym i nie prosi o nie użytkownik. Zostaw je na żądanie.
5. **Weryfikuj linki, które dodajesz:** `curl -sL -o /dev/null -w '%{http_code}' https://pl.wikipedia.org/wiki/<Hasło>` → 200. Nowy akapit bez ani jednego `<ref>` jest gorszy niż brak akapitu.
6. Uruchom `scripts/verify_pl_wiki_article.py <plik>.wiki` i domknij zgłoszone problemy.
7. **Deliver:** wskaż ścieżkę pliku i zwięźle opisz, co doszło. Nigdy nie zapisuj na Wikipedii.

## Pozyskiwanie źródłowego wikitekstu z obcej Wikipedii

- **Nie fetchuj zwykłego URL artykułu** (renderowana strona): przy wersjach niełacińskich (zh, ja, ko, ru) ekstrakcja potrafi zwrócić wyłącznie nawigację/menu zamiast treści.
- **Pobierz surowy wikitekst przez `action=raw`**: `web_extract` na `https://<lang>.wikipedia.org/w/index.php?title=<Tytuł_URL-encoded>&action=raw` — zwraca cały wikitekst z przypisami w jednym kawałku; zapisz do pliku w scratch i czytaj stronicowanie.
- **Przypisy oryginału są gotowym materiałem źródłowym.** Zamiast szukać nowych źródeł dla przetłumaczonych tez, przenieś URL/wydawcę/datę/język z przypisów oryginału do formatu pl.wiki (inline refs, patrz 3.1). Zachowaj `data dostępu` z oryginału lub własną bieżącą datę po sprawdzeniu, że link żyje.
- Tytuły źródeł w alfabetach niełacińskich (chińskie, rosyjskie, japońskie) zostawiaj w oryginale w przypisie — to normalna praktyka na pl.wiki.

## Gap-analysis klastra artykułów („co jeszcze brakuje na pl.wiki”)

Gdy projekt obejmuje kilka haseł wokół jednej tezy/strategii, a user pyta „co jeszcze brakuje”:

1. **Istnienie haseł — live API:** batch-check tytułów (`action=query&formatversion=2&redirects=1&titles=A|B|C`, partie po ~10–20, sleep 2 s między wywołaniami). Wypisz EXISTS/MISSING jawnie — to mapa luk, nie domysł.
2. **Rozjazd lokal vs live:** pobierz żywe wersje (`prop=revisions&rvprop=content&rvslots=main`), porównaj z plikami roboczymi (rozmiar + `difflib.unified_diff` z `n=0`), obejrzyj historię (`rvprop=timestamp|user|size|comment`). User często publikuje i redaguje na żywo między sesjami — lokalny plik bywa TYLLEJSZY niż żywy. Przed nową edycją nadpisz plik żywą wersją.
3. **Stan Wikidaty:** dla każdej encji `wbgetentities` (claims + sitelinks), dla tytułów `wbgetentities&sites=plwiki&titles=...` (filtruj klucze-placeholdery zaczynające się od `-`). Stare `.qs` w workspace sprawdź wobec stanu żywego: odpalony/przestarzały batch = usuń plik, nie regeneruj.
4. **Plan z historii sesji:** przeszukaj przeszłe sesje (session_search / state.db po wzmiankach o projekcie) — plan działania z tamtej rozmowy daje listę kandydatów na hasła. KAŻDY kandydat zweryfikuj u żywego źródła zanim go zaproponujesz — zasady higieny źródeł obowiązują też dla propozycji, nie tylko gotowych przypisów.
5. **Kolejność wg twardych terminów:** hasło z datą graniczną (wejście w życie aktu, deadline przetargu) przed hasłem „kiedyś”; terminy podaj userowi w tabeli.
6. **Follow-upy linkowe:** po publikacji nowego hasła w klastrze hasła-sąsiedzi, które wspomniały temat gołym tekstem, stają się kandydatami do wikilinka — dopisuj przy następnej edycji danego hasła, nie w spinanej serii.

## Narzędzia
- `web_search` — znajdź źródła
- `web_fetch` — pobierz treść i zweryfikuj URL
- `web_search site:commons.wikimedia.org` — sprawdź pliki graficzne
- `web_search site:pl.wikipedia.org` — sprawdź czy artykuł/kategoria istnieje
- `curl` + MediaWiki API (`action=parse`, `action=query&prop=revisions`) — wersja żywa i historia zmian

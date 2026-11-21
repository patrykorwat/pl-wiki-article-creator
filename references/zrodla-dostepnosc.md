# Dostępność źródeł — ratunek 403/202/WAF, czytelność BODY, Wayback

Procedury ratunku na etapie odczytu źródła (przed dodaniem przypisu) oraz zasady czytelności BODY (Reuters 401/NYT 403/JS-render, liczby z prozy en.wiki, OCR skanów, Wayback).

## Odwrotne 403/timeout: zamiast odrzucać cytat, znajdź czytalną lokalizację

Bot-blocking na domenie (MDPI 403, DTIC PDF jako HTML-403, Forbes 403) nie oznacza złego źródła. Kolejność ratunku: (1) abstrakt/regesty przez Crossref `api.crossref.org/works/<DOI>` (pole `abstract`) lub OpenAlex `api.openalex.org/works/doi:<DOI>` (`abstract_inverted_index`) — wystarcza do cytowań DOI-owych; (2) repozytorium autorskie/instytucjonalne tego samego papera (np. DTIC ADAxxxx przez repository.up.ac.za); (3) przeglądarka. Awaria backendu `web_extract` (timeout, „extract failed”) też nie jest wyrokiem na URL: pobierz surowy HTML curl-em z UA przeglądarki i grepuj body; `datePublished`/`<title>` daje datę i tytuł do refu. Działa też odwrotnie: curl bywa blokowany (403/406), a `web_extract` przechodzi — sprawdź ekstrakt, zanim uznasz URL za nieczytelny. Książka/podręcznik: `archive.org/download/<item>/<item>_djvu.txt` daje przeszukiwalny tekst do potwierdzania tez (nie tylko metadana). Jeśli tez nie da się potwierdzić w żadnej czytalnej lokalizacji — usuń cytat i tezę, nie zgaduj.

## EUR-Lex: 202 i WAF-challenge ≠ brak dokumentu

eur-lex.europa.eu przy powtarzanych żądaniach curl odpowiada HTTP 202 z pustym body (limit antybotowy), a HTML aktów (CELEX 5xxxxx) potrafi zwrócić challenge WAF: strona ~2 KB z `awsWafCookieDomainList`, zero treści. Ścieżki od najpewniejszej:

1. PDF-y z data.consilium.europa.eu (`ST-<n>-<rok>-INIT/en/pdf`, w tym wnioski KE opublikowane jako dokumenty Rady) pobieraj curl-em i greppuj pymupdfem — przechodzą bez challenge; gdy interpreter systemowy nie ma pymupdf, sprawdź venv workspace.
2. HTML aktów EUR-Lex czytaj przeglądarką (`goto_url` + `document.body.innerText` — pełny tekst aktu, także po polsku pod `/PL/TXT/`).
3. Dopiero potem zwolnij i ponów curl.

Przy nieudanym odczycie nie cytuj treści, której nie widziałeś — przypisz tezę do dokumentu czytelnego (protokoły i traktaty skonsolidowane: CELEX 12016E/TXT, 12016E/PRO/<n>). Sprawdzaj, czy pobrany dokument to właściwy akt: typ aktu musi wynikać z `<title>` (R=rozporządzenie, D=decyzja), a URI `OJ:L_...` to wydanie Dz. Urz., nie CELEX aktu.


## Czytelność BODY, nie tylko HTTP 200

### Czytelność BODY, nie tylko HTTP 200
HTTP 200 nie wystarcza do zacytowania – potwierdź, że BODY jest czytelne poza przeglądarką. Reuters zwraca 401 na curl, NYT 403, consisium.europa.eu ma JS-check (body nieczytelne), NBC renderuje artykuł w JS. Preferuj źródła ze statycznym czytelnym HTML (np. NPR). Gdy body nieczytelne: opieraj się tylko na tezie potwierdzonej TYTUŁEM strony albo znajdź ten sam oficjalny tekst w czytelnej lokalizacji (PDF EEAS/OSCE, archiwum). Jeśli tez nie da się potwierdzić w żadnej czytalnej lokalizacji — usuń cytat i tezę, nie zgaduj.

**Refy przeniesione z en.wiki:** 401/403 na własnym fetchu (Reuters, NYT, FT, AP, Telegraph, WaPo) to bot-walle, nie martwe linki. Przy adaptacji przenoś ref 1:1 razem z jego `access-date` z en.wiki (to dowód żywotności) i nie zamieniaj go na inny domysł.

**Liczby z prozy en.wiki:** procenty, liczby ankietowanych i dokładne cytaty wymagają WŁASNEGO odczytu w czytelnej lokalizacji — en.wiki bywa cytą fragmentu, którego pełny tekst stoi za JS/paywallem (NBC 10.2026: „80% z 746" tylko w en.wiki, w całym dostępnym body go nie było). Przenoś to, co sam widzisz; resztę skróć do potwierdzonej tezy (kierunek porównania zamiast liczby). Cytaty bywają też drobno przekręcone (Ghost Wars: en.wiki „decade-old fantasy", oryginał „decades-old fantasy") — brzmienie weryfikuj w pełnym tekście.

WNP.pl pułapka: URL z błędnym ID artykułu zwraca HTTP 200, ale renderuje INNY artykuł (recykling ID) — zawsze porównaj `<title>`/H1 pobranej strony z tytułem cytowanego źródła przed dodaniem przypisu. biznes.gov.pl (KRS) renderuje wpis JS-em — body puste w curl i w przeglądarce bez JS; do weryfikacji danych rejestrowych użyj cytowania z prasy albo zrezygnuj z faktu.

**Wykres Datawrapper jako źródło liczby:** dane pod `<url>/data.csv` (serie per rok) — przelicz procenty z CSV, nie z wersji językowej; niepełnoroczny ostatni rok zmienia interpretację udziałów.

**Statystyki makro przy aktualizacji artykułu:** nie przenoś starej liczby z artykułu ani liczby z recenzji — dociągnij bieżącą wartość z czytelnego API. IMF datamapper bywa 403 dla prostych klientów; fallback z czytelnym JSON-em: `api.worldbank.org/v2/country/<ISO3>/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1` (analogicznie `PPPGDP`, `NGDPDPC`); udział w PKB światowym licz jako iloraz EUU/WLD z tego samego API. Ludność i demografię UE bierz ze statistics-explained Eurostatu (strona podaje stan na 1 stycznia roku).

**PDF bez warstwy tekstowej (scany urzędowe) — ścieżka OCR:** jeśli `pymupdf` zwraca pusty `get_text()` na rządzie stron, plik jest skanem. Render: `page.get_pixmap(dpi=200).save('p.png')`, potem `tesseract p.png out -l pol --psm 1` (dostępne języki: `tesseract --list-langs`). Tak zweryfikowano treść odpowiedzi MSZ dla Senatu — bez tego źródło wygląda na „nieczytelne” i jest pokusa odrzucenia prawdziwego dokumentu.

**Ratownictwo martwych URL-i cytatów przez Wayback:** dla każdego `url=`, który zwraca 401/403/timeout, sprawdź snapshot: `curl "https://archive.org/wayback/available?url=<kodowany-url>"` (najbliższy) albo indeks `web.archive.org/cdx/search/cdx?url=<url>&output=json&limit=10` (wszystkie, wybierz ten ze statuscode 200 i poprawnym typem MIME — uwaga: dla plików PDF najwcześniejsze snapshoty bywają pełne, późniejsze to „revisit”; wejdź w `id_`/`if_` wersję z 200). Poprawiony przypis: zachowaj `url=` oryginału + dodaj `archiwum=` i `zarchiwizowano=`. NIE usuwaj przypisu tylko dlatego, że domena żyje słabo. `wayback/available` bywa zwraca 429 przy serii zapytań — pewniejszy jest CDX. Encyklopedie online też rotują przy żywym 200: polska Encyklopedia PWN serwuje „Serwis Nieaktywny” — pozycję PWN w „Linkach zewnętrznych” linkuj przez zarchiwizowany snapshot, nie żywy URL. Zanim jednak sięgniesz po Wayback dla linków urzędowych, sprawdź, czy strona nie przeniesiono: stare ścieżki `europa.eu/european-union/...` bywają martwe (404), a żywy odpowiednik stoi na `european-union.europa.eu` pod inną ścieżką — web_search z `site:` zwykle ją podaje; Wayback zostaw na treści, która naprawdę zniknęła.


## Czytelność BODY, nie tylko HTTP 200

### Czytelność BODY, nie tylko HTTP 200
HTTP 200 nie wystarcza do zacytowania – potwierdź, że BODY jest czytelne poza przeglądarką. Reuters zwraca 401 na curl, NYT 403, consisium.europa.eu ma JS-check (body nieczytelne), NBC renderuje artykuł w JS. Preferuj źródła ze statycznym czytelnym HTML (np. NPR). Gdy body nieczytelne: opieraj się tylko na tezie potwierdzonej TYTUŁEM strony albo znajdź ten sam oficjalny tekst w czytelnej lokalizacji (PDF EEAS/OSCE, archiwum). Jeśli tez nie da się potwierdzić w żadnej czytalnej lokalizacji — usuń cytat i tezę, nie zgaduj.

**Refy przeniesione z en.wiki:** 401/403 na własnym fetchu (Reuters, NYT, FT, AP, Telegraph, WaPo) to bot-walle, nie martwe linki. Przy adaptacji przenoś ref 1:1 razem z jego `access-date` z en.wiki (to dowód żywotności) i nie zamieniaj go na inny domysł.

**Liczby z prozy en.wiki:** procenty, liczby ankietowanych i dokładne cytaty wymagają WŁASNEGO odczytu w czytelnej lokalizacji — en.wiki bywa cytą fragmentu, którego pełny tekst stoi za JS/paywallem (NBC 10.2026: „80% z 746" tylko w en.wiki, w całym dostępnym body go nie było). Przenoś to, co sam widzisz; resztę skróć do potwierdzonej tezy (kierunek porównania zamiast liczby). Cytaty bywają też drobno przekręcone (Ghost Wars: en.wiki „decade-old fantasy", oryginał „decades-old fantasy") — brzmienie weryfikuj w pełnym tekście.

WNP.pl pułapka: URL z błędnym ID artykułu zwraca HTTP 200, ale renderuje INNY artykuł (recykling ID) — zawsze porównaj `<title>`/H1 pobranej strony z tytułem cytowanego źródła przed dodaniem przypisu. biznes.gov.pl (KRS) renderuje wpis JS-em — body puste w curl i w przeglądarce bez JS; do weryfikacji danych rejestrowych użyj cytowania z prasy albo zrezygnuj z faktu.

**Wykres Datawrapper jako źródło liczby:** dane pod `<url>/data.csv` (serie per rok) — przelicz procenty z CSV, nie z wersji językowej; niepełnoroczny ostatni rok zmienia interpretację udziałów.

**Statystyki makro przy aktualizacji artykułu:** nie przenoś starej liczby z artykułu ani liczby z recenzji — dociągnij bieżącą wartość z czytelnego API. IMF datamapper bywa 403 dla prostych klientów; fallback z czytelnym JSON-em: `api.worldbank.org/v2/country/<ISO3>/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1` (analogicznie `PPPGDP`, `NGDPDPC`); udział w PKB światowym licz jako iloraz EUU/WLD z tego samego API. Ludność i demografię UE bierz ze statistics-explained Eurostatu (strona podaje stan na 1 stycznia roku).

**PDF bez warstwy tekstowej (scany urzędowe) — ścieżka OCR:** jeśli `pymupdf` zwraca pusty `get_text()` na rządzie stron, plik jest skanem. Render: `page.get_pixmap(dpi=200).save('p.png')`, potem `tesseract p.png out -l pol --psm 1` (dostępne języki: `tesseract --list-langs`). Tak zweryfikowano treść odpowiedzi MSZ dla Senatu — bez tego źródło wygląda na „nieczytelne” i jest pokusa odrzucenia prawdziwego dokumentu.

**Ratownictwo martwych URL-i cytatów przez Wayback:** dla każdego `url=`, który zwraca 401/403/timeout, sprawdź snapshot: `curl "https://archive.org/wayback/available?url=<kodowany-url>"` (najbliższy) albo indeks `web.archive.org/cdx/search/cdx?url=<url>&output=json&limit=10` (wszystkie, wybierz ten ze statuscode 200 i poprawnym typem MIME — uwaga: dla plików PDF najwcześniejsze snapshoty bywają pełne, późniejsze to „revisit”; wejdź w `id_`/`if_` wersję z 200). Poprawiony przypis: zachowaj `url=` oryginału + dodaj `archiwum=` i `zarchiwizowano=`. NIE usuwaj przypisu tylko dlatego, że domena żyje słabo. `wayback/available` bywa zwraca 429 przy serii zapytań — pewniejszy jest CDX. Encyklopedie online też rotują przy żywym 200: polska Encyklopedia PWN serwuje „Serwis Nieaktywny” — pozycję PWN w „Linkach zewnętrznych” linkuj przez zarchiwizowany snapshot, nie żywy URL. Zanim jednak sięgniesz po Wayback dla linków urzędowych, sprawdź, czy strona nie przeniesiono: stare ścieżki `europa.eu/european-union/...` bywają martwe (404), a żywy odpowiednik stoi na `european-union.europa.eu` pod inną ścieżką — web_search z `site:` zwykle ją podaje; Wayback zostaw na treści, która naprawdę zniknęła.


## Czytelność BODY, nie tylko HTTP 200

### Czytelność BODY, nie tylko HTTP 200
HTTP 200 nie wystarcza do zacytowania – potwierdź, że BODY jest czytelne poza przeglądarką. Reuters zwraca 401 na curl, NYT 403, consisium.europa.eu ma JS-check (body nieczytelne), NBC renderuje artykuł w JS. Preferuj źródła ze statycznym czytelnym HTML (np. NPR). Gdy body nieczytelne: opieraj się tylko na tezie potwierdzonej TYTUŁEM strony albo znajdź ten sam oficjalny tekst w czytelnej lokalizacji (PDF EEAS/OSCE, archiwum). Jeśli tez nie da się potwierdzić w żadnej czytalnej lokalizacji — usuń cytat i tezę, nie zgaduj.

**Refy przeniesione z en.wiki:** 401/403 na własnym fetchu (Reuters, NYT, FT, AP, Telegraph, WaPo) to bot-walle, nie martwe linki. Przy adaptacji przenoś ref 1:1 razem z jego `access-date` z en.wiki (to dowód żywotności) i nie zamieniaj go na inny domysł.

**Liczby z prozy en.wiki:** procenty, liczby ankietowanych i dokładne cytaty wymagają WŁASNEGO odczytu w czytelnej lokalizacji — en.wiki bywa cytą fragmentu, którego pełny tekst stoi za JS/paywallem (NBC 10.2026: „80% z 746" tylko w en.wiki, w całym dostępnym body go nie było). Przenoś to, co sam widzisz; resztę skróć do potwierdzonej tezy (kierunek porównania zamiast liczby). Cytaty bywają też drobno przekręcone (Ghost Wars: en.wiki „decade-old fantasy", oryginał „decades-old fantasy") — brzmienie weryfikuj w pełnym tekście.

WNP.pl pułapka: URL z błędnym ID artykułu zwraca HTTP 200, ale renderuje INNY artykuł (recykling ID) — zawsze porównaj `<title>`/H1 pobranej strony z tytułem cytowanego źródła przed dodaniem przypisu. biznes.gov.pl (KRS) renderuje wpis JS-em — body puste w curl i w przeglądarce bez JS; do weryfikacji danych rejestrowych użyj cytowania z prasy albo zrezygnuj z faktu.

**Wykres Datawrapper jako źródło liczby:** dane pod `<url>/data.csv` (serie per rok) — przelicz procenty z CSV, nie z wersji językowej; niepełnoroczny ostatni rok zmienia interpretację udziałów.

**Statystyki makro przy aktualizacji artykułu:** nie przenoś starej liczby z artykułu ani liczby z recenzji — dociągnij bieżącą wartość z czytelnego API. IMF datamapper bywa 403 dla prostych klientów; fallback z czytelnym JSON-em: `api.worldbank.org/v2/country/<ISO3>/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1` (analogicznie `PPPGDP`, `NGDPDPC`); udział w PKB światowym licz jako iloraz EUU/WLD z tego samego API. Ludność i demografię UE bierz ze statistics-explained Eurostatu (strona podaje stan na 1 stycznia roku).

**PDF bez warstwy tekstowej (scany urzędowe) — ścieżka OCR:** jeśli `pymupdf` zwraca pusty `get_text()` na rządzie stron, plik jest skanem. Render: `page.get_pixmap(dpi=200).save('p.png')`, potem `tesseract p.png out -l pol --psm 1` (dostępne języki: `tesseract --list-langs`). Tak zweryfikowano treść odpowiedzi MSZ dla Senatu — bez tego źródło wygląda na „nieczytelne” i jest pokusa odrzucenia prawdziwego dokumentu.

**Ratownictwo martwych URL-i cytatów przez Wayback:** dla każdego `url=`, który zwraca 401/403/timeout, sprawdź snapshot: `curl "https://archive.org/wayback/available?url=<kodowany-url>"` (najbliższy) albo indeks `web.archive.org/cdx/search/cdx?url=<url>&output=json&limit=10` (wszystkie, wybierz ten ze statuscode 200 i poprawnym typem MIME — uwaga: dla plików PDF najwcześniejsze snapshoty bywają pełne, późniejsze to „revisit”; wejdź w `id_`/`if_` wersję z 200). Poprawiony przypis: zachowaj `url=` oryginału + dodaj `archiwum=` i `zarchiwizowano=`. NIE usuwaj przypisu tylko dlatego, że domena żyje słabo. `wayback/available` bywa zwraca 429 przy serii zapytań — pewniejszy jest CDX. Encyklopedie online też rotują przy żywym 200: polska Encyklopedia PWN serwuje „Serwis Nieaktywny” — pozycję PWN w „Linkach zewnętrznych” linkuj przez zarchiwizowany snapshot, nie żywy URL. Zanim jednak sięgniesz po Wayback dla linków urzędowych, sprawdź, czy strona nie przeniesiono: stare ścieżki `europa.eu/european-union/...` bywają martwe (404), a żywy odpowiednik stoi na `european-union.europa.eu` pod inną ścieżką — web_search z `site:` zwykle ją podaje; Wayback zostaw na treści, która naprawdę zniknęła.

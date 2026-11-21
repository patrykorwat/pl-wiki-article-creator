# Źródła — higiena (zabronione, preferowane, rygor absolutny, protokół weryfikacji)

## Rosyjskie źródła — unikanie TASS i domen .ru

Unikaj TASS i domen .ru jako głównych źródeł (kontrola Kremla); strategia alternatyw: `references/zrodla-rosyjskie.md`. Cytuj explainer tylko dla tez, które faktycznie zawiera; brak nie-TASS źródła dla tezy = teza bez przypisu.
## Źródła — higiena

### Źródła zabronione
- fronda.pl – niska wiarygodność
- rejestr.io – komercyjna nakładka na KRS
- krs.infoveriti.pl – komercyjna nakładka na KRS (ta sama kategoria co rejestr.io; nie używać)
- Dane rejestrowe KRS cytuj Z WYŁĄCZNIE oficjalnego źródła: `https://www.biznes.gov.pl/pl/wyszukiwarka-firm/wpis/krs/<numer>` (biznes.gov.pl), NIGDY przez pośredników (rejestr.io, krs.infoveriti, krs-pobierz, infoveriti itp.)
- Demagog (demagog.org.pl) i podobne serwisy fact-checking
- Blogi producenta jako jedyne źródło twierdzeń o produkcie
- Wikipedia jako źródło dla siebie
- **Wszelkie portale typu wiki** (w tym openlist.wiki, wikia/fandom, memory/wiki itp.) – treść edytowalna przez użytkowników, brak recenzji naukowej, nieakceptowalna jako źródło w artykule encyklopedycznym
- Blogi osobiste bez weryfikacji faktów
- Fora internetowe
- Serwisy z treściami generowanymi przez użytkowników
- Klikbajtowe portale informacyjne
- **Nieistniejące domeny** — sprawdź, zanim dodasz URL
- **Książki, których nie ma w żadnym katalogu bibliotecznym** (Open Library, WorldCat) — prawdopodobnie nie istnieją pod taką nazwą

### Źródła preferowane
- Oficjalne strony instytucji (gov.pl, um.warszawa.pl itp.) – do faktów rutynowych
- Sejm API: `api.sejm.gov.pl/sejm/term<KADENCJA>/votings/<posiedzenie>` — JSON z liczbą głosów za/przeciw/wstrzymało się dla każdego głosowania; dokładne wyniki ustaw (np. do hasła o ustawie) bierz stąd, nie z transkryptów ani prasy
- Recenzowane artykuły naukowe
- Renomowane portale: rp.pl, tvn24.pl, onet.pl, polityka.pl, wyborcza.pl
- histmag.org (teksty z podpisem autora i datą, licencja CC BY-SA) — akceptowalny do faktów historycznych; przy klonach rozsyłanych przez większe portale cytuj oryginał
- Biografie i historia w wersji naukowej/muzealnej z pełnym statycznym HTML (czytelne curlem, cytowalne z pełnym URL): kroniki fundacji przy muzeach (np. bismarck-biografie.de — Stiftung Preußische Schlösser: chronik z datowanymi faktami życia), hasła w deutsche-biographie.de (NDB/ADB), LeMO (dhm.de/lemo, Deutsches Historisches Museum), portale dwustronne (deutsche-und-polen.de, rbb). Zamiast przenosić fakty „za en/de.wiki", grepuj te daty właśnie w tych portalach; gdy sekcja haseł tematycznych na portalu jest pod inną ścieżką niż oczywista (np. `/privates/ehe-und-kinder`, nie `/family`), szukaj dokładnego URL przez web_search przed stwierdzeniem, że strona nie istnieje
- Międzynarodowe: Reuters, The Guardian, Politico, Euractiv
- Oficjalne komunikaty prasowe instytucji publicznych
- Publikacje naukowe: Nature, open access journals

### Zasady korzystania ze źródeł — rygor absolutny

Poniższe zasady są BEZWZGLĘDNE. Złamanie którejkolwiek skutkuje odrzuceniem artykułu.

**Zasada 1 – Źródło musisz OTWORZYĆ i PRZECZYTAĆ**
- Nie proponuj źródła, którego nie otworzyłeś.
- Nie zakładaj treści po tytule, autorze ani wydawcy.
- Paywall/licencja = to źródło jest dla ciebie NIEDOSTĘPNE. Nie cytuj go.

**Zasada 2 – Teza musi być POTWIERDZONA w źródle**
- Nie wystarczy, że źródło „pasuje do tematu". Musisz sprawdzić, czy konkretne zdanie/teza, którą chcesz udokumentować, faktycznie występuje w źródle.
- Jeśli źródło ma 200 stron, a ty nie masz dostępu do konkretnej strony — nie cytuj.

**Zasada 3 – Nie wymyślaj danych bibliograficznych**
- Tytuł, rok, wydawca, ISBN, numer strony — każde pole musi być zweryfikowane.
- Sprawdź w Open Library / WorldCat, czy książka istnieje pod dokładnie tym tytułem i rokiem.
- Numer strony podawaj TYLKO jeśli masz książkę w ręku (lub otwarty PDF z widoczną paginacją).

**Zasada 4 – Domeny muszą działać**
- Każdy URL musi zwracać HTTP 200, zanim go dodasz; nieistniejąca domena = nieistniejące źródło.

**Zasada 5 – Zero portali wiki** – treść edytowalna przez użytkowników jest nieakceptowalna jako źródło (przykłady w sekcji Źródła zabronione).

**Zasada 6 – Zero domysłów**
- „To źródło na pewno o tym pisze" to nie jest weryfikacja.
- Jeśli nie możesz znaleźć w źródle konkretnej tezy — nie dodawaj przypisu.

### Protokół weryfikacji nowych źródeł

Zanim zaproponujesz nowy przypis — zwłaszcza gdy edytujesz istniejący artykuł i szukasz dodatkowych źródeł — wykonaj KAŻDY z poniższych kroków:

**Krok 1: Sprawdź, czy źródło istnieje**
- Domena/strona: sprawdź, czy URL resolve'uje się (HTTP 200)
- Książka: sprawdź w Open Library / WorldCat — czy istnieje pod dokładnie tym tytułem, autorem i rokiem?
- Artykuł: sprawdź, czy strona czasopisma go ma (choćby abstrakt)

**Krok 2: Sprawdź dostęp do treści**
- Czy możesz otworzyć pełną treść źródła?
- Paywall = STOP. Nie cytuj tego, czego nie przeczytałeś.
- Tylko abstrakt = STOP. Abstrakt nie udowadnia, że reszta artykułu wspiera twoją tezę.

**Krok 3: Potwierdź zgodność tezy ze źródłem**
- Otwórz źródło i znajdź KONKRETNE ZDANIE potwierdzające tezę.
- Jeśli nie znajdujesz — TEZA NIE JEST UDOKUMENTOWANA. Nie dodawaj przypisu.

**Krok 4: Zweryfikuj dane bibliograficzne**
- Tytuł — dokładnie taki, jak w źródle
- Rok — zgodny z metadanymi źródła
- ISBN — sprawdzony (np. przez Open Library)
- Autor — zgodny z metadanymi
- URL — działający

**Krok 5: Zadaj sobie pytanie kontrolne**
„Czy gdyby ktoś kliknął w ten link, znalazłby dokładnie to, do czego go przypisałem?"
Jeśli odpowiedź brzmi „nie", „nie wiem" lub „może" — nie dodawaj przypisu.

### Przykład porażki — case study: source-verification-case-study.md

Protip: jeśli po protokole nie ma żadnego weryfikowalnego źródła — nie dodawaj nic. Artykuł bez przypisu jest słaby, z fałszywym przypisem — szkodliwy.

### Proza instytucjonalna: zadania i porównania, nie katalogi
Dla haseł jednostek/rodzajów wojsk user oczekuje najpierw sekcji „Zadania” (pełne spektrum działań, obszary, skala — źródła oficjalne: strona jednostki, portal rekrutacyjny, resort) i „Analogiczne jednostki w innych państwach” (po 1–2 zdania na kraj). Katalogi projektów, partnerstwa komercyjne i nazwiska szefów projektów przepisane z komunikatów prasowych to PR, nie encyklopedia — pojedyncze jednostki pomocnicze (np. centrum technologiczne) = max 1 akapit, bez produktów i kontrahentów.
## Odkrywanie źródeł akademickich
- CrossRef: `api.crossref.org/works?query=...&rows=10`; OpenAlex: `api.openalex.org/works/doi:...?select=title,abstract_inverted_index`.
- **Rok w `data=`: print, nie online.** Crossref `issued` to data online-first; przypisanie woluminu/numeru/stron odpowiada edycji drukowanej (`published-print`/`journal-issue`). Realne: Harff NM&S `issued` 2025-04-30 → vol 28(6) = print 2026, cytuj `data=2026`; Hudders IJA `issued` 2020-10-28 → vol 40(3) = print 2021, cytuj `data=2021`.
- Tylko pierwsza strona w Crossref (`page: '61'`) ≠ pełny zakres; zakresu (61–78) szukaj na stronie/JSTOR pracy, a gdy dostępny jest tylko pierwszy — cytuj bez `s=` lub z pojedynczą stroną, nie wymyślaj końca zakresu.
- Polskie czasopisma humanistyczne szukaj w repozytoriach (rcin.org.pl): starsze roczniki (Kwartalnik Historyczny i pod.) są OA jako PDF, a strona publikacji podaje autora i rocznik — tezę potwierdzaj greppem po treści PDF-a, nie po metadanych.
- Tylko peer-reviewed (monografie, czasopisma z IF) do definicji/klasyfikacji. NIE dziennikarze do definicji, NIE prace magisterskie, NIE portale typu wiki.

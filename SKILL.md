---
name: wiki-article-creator
description: "Use when creating, editing, or formatting articles for Polish Wikipedia (pl.wiki). Covers infobox selection, citation formatting with {{cytuj}}, Polish typography, NPOV, and pre-publication verification. Works for persons, institutions, events, concepts, companies, places."
version: 1.5.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wikipedia, polish, wiki, citations, research]
    related_skills: [arxiv, multi-source-web-research, policy-analysis]
---

# Skill: wiki-article-creator — Tworzenie i edycja artykułów na polskiej Wikipedii

Tworzenie, edytowanie i formatowanie artykułów na polskiej Wikipedii. Konwencje pl.wiki różnią się od en.wiki — ta umiejętność dokumentuje je na podstawie analizy faktycznych artykułów z folderu wiki/.

## Kiedy używać

- Tworzenie nowego artykułu na pl.wiki (osoby, instytucje, wydarzenia, pojęcia, produkty, miejsca)
- Edycja istniejącego artykułu — uzupełnianie sekcji, dodawanie przypisów, poprawa formatowania
- Refaktoryzacja wikitekstu — poprawa szablonów cytowań, infoboxów, kategorii
- Weryfikacja przed publikacją — sprawdzanie przypisów, źródeł, formatowania
- Proponowanie pytań do rubryki „Czy wiesz" na stronie głównej

## NIGDY nie edytuj Wikipedii przez przeglądarkę

**ZABRONIONE:** bezpośrednia edycja Wikipedii przez przeglądarkę (browser_navigate do action=edit, wypełnianie formularza, klikanie „Zapisz").

**ZASADA:** każda zmiana w artykule Wikipedii musi iść przez plik w katalogu `wiki/`. Pobierz aktualną treść artykułu (przez API lub z istniejącego pliku), wprowadź zmiany w pliku `.txt` lub `.wiki`, zapisz w `wiki/`. Nigdy nie używaj interfejsu WWW Wikipedii do edycji.

**Dlaczego:**
- Wikipedia blokuje zapis hCaptchą dla niezalogowanych użytkowników
- Praca przez pliki zapewnia wersjonowanie i możliwość review przed publikacją
- Spójność z istniejącym workflow (wszystkie artykuły w `wiki/` są plikami lokalnymi)

### Jedno hasło = jeden plik (single source of truth)

**Jedno hasło = dokładnie jeden plik roboczy `.wiki` w `wiki/`** (nazwa pliku = tytuł hasła, spacje → `_`). NIE twórz wielu kopii tego samego artykułu (np. `X.aktualna`, `X.propozycja`, `X.v2`, `X.backup`, `X_poprawiony`). Wielokrotne kopie prowadzą do rozjazdu wersji i pomyłek przy publikacji.

- **Synchronizacja przed edycją:** zawsze pobieraj **najnowszą żywą wersję** artykułu przez API (`action=parse&page=<Tytuł>&prop=wikitext&format=json`) i NADPISUJ nią ten jedyny plik roboczy. Następnie wprowadzaj zmiany w tym samym pliku.
- **Porównywanie / „przed i po”:** używaj `git diff` na jednym pliku albo odnotuj zamierzone zmiany komentarzem w tekście roboczym – zamiast tworzyć osobne kopie.
- **Sprzątanie:** po scaleniu usuń wszelkie kopie i pliki tymczasowe (`_tmp`, `aktualna`, `propozycja`), zostawiając wyłącznie plik kanoniczny.
- **Publikacja:** treść do ręcznego wklejenia bierz WYŁĄCZNIE z pliku kanonicznego.

## Struktura artykułu

### Kolejność sekcji
```
{{Infobox dopasowany do typu hasła}}   <!-- opcjonalnie -->

[[Plik:Nazwa_pliku.jpg|mały|Opis]]    <!-- opcjonalne grafiki -->

'''Termin''' – definicja jednym-dwoma zdaniami<ref name="zr1">{{cytuj|...}}</ref>.

== [Sekcja tematyczna 1] ==
Treść z przypisami<ref name="zr1" />.

== [Sekcja tematyczna 2] ==
Treść z przypisami<ref name="zr2">{{cytuj|...}}</ref>.

== Zobacz też ==
* [[powiązane hasło]]

== Przypisy ==
{{Przypisy}}

== Bibliografia ==        <!-- tylko gdy używasz książek z wglądem -->
* ...

[[Kategoria:Istniejąca kategoria]]
```

### Typowe sekcje wg typu hasła
- **Osoba:** „Życiorys", „Działalność", „Twórczość", „Odznaczenia"
- **Instytucja/placówka:** „Historia", „Działalność", „Struktura", „Siedziba"
- **Wydarzenie:** „Tło", „Przebieg", „Następstwa", „Reakcje"
- **Pojęcie/teoria:** „Definicja", „Historia", „Charakterystyka", „Krytyka"
- **Produkt/technologia:** „Historia", „Budowa/Zasada działania", „Zastosowania", „Odbiór"
- **Miejscowość:** „Położenie", „Historia", „Demografia", „Zabytki"

## Infoboksy (szablony infoboxów)

Wykryj typ artykułu i dobierz odpowiedni infobox. Infobox jest opcjonalny, ale zalecany.

### Dla osób
```wiki
{{Biogram infobox
 |imię i nazwisko     = 
 |grafika             = 
 |opis grafiki        = 
 |data urodzenia      = 
 |miejsce urodzenia   = 
 |data śmierci        = 
 |miejsce śmierci     = 
 |zawód               = 
 |Alma Mater          = 
 |stanowisko          = 
 |rodzice             = 
 |dzieci              = 
 |odznaczenia         = 
 |commons             = 
 |www                 = 
}}
```

### Dla firm/przedsiębiorstw
```wiki
{{Przedsiębiorstwo infobox
 |nazwa             = 
 |nazwa oryginalna  = 
 |grafika           = 
 |państwo           = POL
 |siedziba          = [[Miasto]]
 |adres             = ul. Przykładowa 12<br />00-123 [[Warszawa]]
 |data założenia    = 
 |data likwidacji   = 
 |forma prawna      = [[spółka akcyjna]]
 |prezes            = 
 |zatrudnienie      = 
 |giełda            = {{tyo|3382}}
 |przychody         = 
 |wynik netto       = 
 |kapitał zakładowy = 
 |commons           = 
}}
```
**Uwagi:**
- Parametry infoboxu sprawdź w rzeczywistym szablonie przez API (`action=parse&page=Szablon:Nazwa_infoboxu&prop=wikitext`). Pola typu `www`, `strona`, `logo_size` często NIE są obsługiwane i powodują błąd „Nieprawidłowe/puste pola".
- Dla tickera na GPW w Tokio używaj `{{tyo|numer}}`, NIE `[[Giełda Papierów Wartościowych w Tokio|TYO]]: numer`.
- `commons` dodawaj w infoboxie, nie jako osobny `{{Commons}}` na dole artykułu.
- `rok` – jeden wiersz z rokiem finansowym w headerze „Dane finansowe" zamiast powtarzania roku i przypisu w każdej linii finansowej. Przypis do źródła danych finansowych daj w `|rok=2023<ref name=Financials />`, a wartości w `przychody`/`wynik netto`/`kapitał zakładowy`/`zatrudnienie` zostaw bez daty i przypisu.

### Dla instytucji państwowych/dyplomatycznych
```wiki
{{Instytucja państwowa infobox
 |nazwa            = 
 |nazwa oryginalna = 
 |grafika          = 
 |opis grafiki     = 
 |państwo          = 
 |data utworzenia  = 
 |data likwidacji  = 
 |siedziba         = 
 |tytuł szefa      = 
 |szef             = 
 |adres            = ul. ...<br />00-000 [[Warszawa]]
 |zatrudnienie     = 
 |commons          = 
 |www              = 
}}
```
**Uwagi:**
- **`budżet` – NIE dodawaj w infoboxie.** Budżet agencji zmienia się corocznie i lepiej umieścić go w sekcji „Zarządzanie" lub „Finanse" w treści artykułu, gdzie można podać dane z kilku lat z przypisami. W infoboxie zostaw tylko stałe dane (nazwa, siedziba, prezes, data utworzenia).
- **`kierownictwo` – nie twórz osobnej sekcji.** Prezes i wiceprezes są już w infoboxie. Sekcja „Kierownictwo" w treści jest zbędnym powieleniem. Jeśli chcesz podać listę historycznych prezesów, umieść ją w sekcji „Zarządzanie" jako podsekcję „Lista prezesów".

### Dla organizacji/fundacji/think-tanków (nie państwowych) — {{Instytucja infobox}}
```wiki
{{Instytucja infobox
 |nazwa                     =
 |nazwa oryginalna          =
 |grafika                   =
 |opis grafiki              =
 |państwo                   = Stany Zjednoczone
 |miejscowość               = [[Waszyngton]]
 |adres                     = 1744 R Street NW
 |data założenia            = 5 czerwca 1972
 |data likwidacji           =
 |dziedzina                 = [[think tank]], polityka publiczna
 |stanowisko zarządzającego = Prezes
 |zarządzający              = {{link-interwiki|...|Q=...}}
 |www                       = https://...
}}
```
To NIE jest ten sam szablon co `{{Instytucja państwowa infobox}}`. Pola poprawne dla `{{Instytucja infobox}}` (zweryfikowane w sesji, sierpień 2026): `nazwa`, `nazwa oryginalna`, `grafika`, `opis grafiki`, `państwo`, `miejscowość`, `adres`, `data założenia`, `data likwidacji`, `dziedzina`, `stanowisko zarządzającego`, `zarządzający`, `kod mapy`, `współrzędne`, `commons`, `www`.
**Nieistniejące pola (dają błąd „Nieznane pola"):** `numer rejestru`, `prezes`, `członkowie`, `siedziba`, `brak mapy`, `rodzaj stowarzyszenia`. Prezesa podajesz jako `|stanowisko zarządzającego=Prezes` + `|zarządzający=Imię`. Siedzibę dzielisz na `miejscowość` i `adres`.

### Dla aktów prawnych/ustaw — {{Akt prawny infobox}}
```wiki
{{Akt prawny infobox
 |tytuł aktu                        = Rosyjska ustawa o organizacjach niepożądanych
 |tytuł oryginalny                  = ... (tytuł w oryginale)
 |państwo                           = Rosja
 |data wydania                      = 23 maja 2015
 |data wejścia w życie              = 23 maja 2015
 |rodzaj aktu                       = ustawa federalna
 |przedmiot regulacji               = ...
 |status                            = obowiązujący
}}
```
Pola poprawne dla `{{Akt prawny infobox}}` (zweryfikowane w sesji, sierpień 2026): `tytuł aktu`, `tytuł oryginalny`, `grafika`, `opis grafiki`, `państwo`, `data wydania`, `miejsce publikacji`, `data wejścia w życie`, `rodzaj aktu`, `przedmiot regulacji`, `status`, `utrata mocy obowiązującej z dniem`, `ostatnio zmieniony przez`, `wejście w życie ostatniej zmiany`, `wikiźródła`, `commons`.
**Nieistniejące pola (błąd „Nieznane pola"):** `nazwa`, `nazwa oryginalna`, `rodzaj`, `data uchwalenia`, `www`. Tytuł podajesz jako `|tytuł aktu=` (nie `|nazwa=`), a datę wejścia jako `|data wejścia w życie=` (nie `|data uchwalenia=`). Ten szablon NIE ma pola `www`.

### Dla seriali/filmów
```wiki
{{Serial infobox}} lub {{Film infobox}}
<!-- pola: tytuł, gatunek, kraj produkcji, twórcy, główne role,
     liczba odcinków, stacja telewizyjna, data premiery -->
```

### Dla miejscowości
```wiki
{{Miejscowość infobox}}
<!-- pola: nazwa, herb, flaga, województwo, powiat, gmina,
     prawa miejskie, powierzchnia, populacja -->
```

### Dla wydarzeń
```wiki
{{Wydarzenie infobox}}
<!-- pola: nazwa, data, miejsce, państwo, przyczyna, wynik -->
```

### Dla pocisków/broni
```wiki
{{Pocisk antybalistyczny infobox}}
<!-- lub dedykowany infobox dla danego typu sprzętu -->
```

### Dla rakiet nośnych (konkretny pojazd, nie koncepcja)
```wiki
{{Rakieta nośna infobox
 |koszt_startu        = 
 |zdolność_wynoszenia = 
 |siła_ciągu          = 
 |długość             = 
 |masa                = 
 |stopnie_rakiety     = {{Rakieta nośna infobox/stopień|Stopień 1.|...}}
}}
```
- Używany dla konkretnych rakiet (np. [[Falcon 9]], [[Starship (rakieta)|Starship]])
- Dla artykułów koncepcyjnych (np. „Rakieta nośna") nie stosuje się infoboxu

### Dla tabel statusu (tak/nie/aktywny/wycofany)
- Do kolorowania komórek tabeli używaj `{{tabela-tak|Aktywny}}` i `{{tabela-nie|Wycofany}}`
- NIE używaj `{{Tak|tekst}}` / `{{Nie|tekst}}` – te szablony wyświetlają tylko ikonę T/N, nie tekst
- Istnieją również: `{{tabela-częściowo|tekst}}` i `{{tabela-?|tekst}}`

### Flagi państw w tabelach
- `{{Flaga|USA}}`, `{{Flaga|Chiny}}`, `{{Flaga|Rosja}}`, `{{Flaga|Hiszpania}}` itd. – szablon istnieje i działa

## Przypisy — formatowanie (najważniejsza sekcja)

### 3.1 Szablon cytowania
Wyłącznie uniwersalny `{{cytuj}}` z **małej litery**. NIE używaj `{{cytuj książkę}}`, `{{cytuj pismo}}`, `{{cytuj stronę}}`, `{{Cytuj}}` (duża litera).

```wiki
<ref name="skrot">{{cytuj
 |autor=Imię Nazwisko
 |tytuł=Tytuł artykułu
 |url=https://example.com
 |opublikowany=Nazwa wydawcy
 |data=2024-01-15
 |data dostępu=2026-07-13
 |język=pl
}}</ref>
```

### 3.2 Pola szablonu {{cytuj}} — lista DOZWOLONYCH parametrów
Tylko poniższe pola są akceptowane. Użycie innego parametru powoduje komunikat „Nieznane pola".

| Parametr | Znaczenie | Uwaga |
|---|---|---|
| `autor=` | Imię Nazwisko (wielu po przecinku, NIE średnikiem) | |
| `tytuł=` | Tytuł artykułu/strony | |
| `url=` | Pełny adres URL | Zweryfikuj przez web_fetch |
| `opublikowany=` / `czasopismo=` / `wydawca=` | Nazwa źródła | |
| `data=` | Data publikacji (YYYY-MM-DD lub YYYY) | NIE `rok=` |
| `data dostępu=` | Data sprawdzenia źródła | |
| `s=` | Numer strony | NIE `strony=` |
| `isbn=` | ISBN | Sprawdź cyfrę kontrolną |
| `archiwum=` | Link do archiwum (web.archive.org) | |
| `zarchiwizowano=` | Data archiwizacji | |
| `język=` | Kod języka (`pl`, `en`, `de`) | |
| `wolumin=` | Wolumin czasopisma | |
| `numer=` | Numer czasopisma | |
| `doi=` | DOI identyfikator | |
| `wydanie=` | Wydanie książki | |
| `miejsce=` | Miejsce wydania | |
| `rozdział=` | Rozdział książki | |
| `pmid=` / `pmc=` | PubMed ID | |
| `oclc=` | OCLC number | |

**Częsty błąd — nieznane parametry, które WYWOŁUJĄ „Nieznane pola":**
- `strony=` → użyj `s=`
- `rok=` → użyj `data=`
- `wydarzenie=` → usuń (nie jest akceptowane)
- `konferencja=` → usuń (nie jest akceptowane)
- `autor r=` → użyj `autor r=` (UWAGA: to jest dozwolone tylko z `rozdział=`)
- `odpowiedzialność=` → rzadkie, ale dozwolone

### 3.3 Definicja przed użyciem
Pierwsze użycie `ref name` MUSI mieć pełną treść. Kolejne użycia są skrócone.

```wiki
tekst<ref name="hist">{{cytuj|autor=Jan Kowalski|tytuł=...|s=302}}</ref>.
...
późniejszy tekst<ref name="hist" />.
```

**Błąd typowy przy tłumaczeniu:** użycie `<ref name="daalder" />` (skrótu) bez wcześniejszej definicji `<ref name="daalder">{{cytuj|...}}</ref>`. Skutek: komunikat „Brak tekstu w przypisie o nazwie daalder / BŁĄD PRZYPISÓW". Zawsze dodaj `name=` do pełnej definicji przy PIERWSZYM wystąpieniu, a nie do skrótu.

### 3.4 Pozycja względem interpunkcji
`<ref>` idzie PRZED kropką i przecinkiem:
- Poprawnie: `tekst<ref name="x" />.`
- Niepoprawnie: `tekst.<ref name="x" />`

### 3.5 Powtórzenia
- `<ref name="x" />` – poprawnie
- `{{r}}` – zdeprecjonowany, NIE używaj

### 3.6 Sekcja przypisów
`{{Przypisy}}` – NIE `<references>`.

### 3.7 Równoważenie źródeł
Jedno źródło maks. 4–5 przypisów. Rozkładaj tezy na różne, niezależne źródła.

### 3.8 Weryfikacja URL-i
Każdy `url=` sprawdź przez web_fetch. Jeśli 404 lub timeout, usuń pole `url=` i zostaw sam opis bibliograficzny.

## Grafiki z Commons

- Sprawdź dokładną pisownię nazw plików (wielkość liter ma znaczenie)
- Weryfikuj: `web_search site:commons.wikimedia.org "Nazwa_pliku.jpg"`
- Format: `[[Plik:Nazwa_pliku.jpg|mały|Opis]]`
- Dla grafik w infoboxie: pole `grafika = Nazwa_pliku.jpg`

## Linki wewnętrzne

- Format: `[[Nazwa artykułu]]` lub `[[Nazwa artykułu|tekst wyświetlany]]`
- Linkuj pierwsze wystąpienie terminu w artykule
- Dla haseł nieistniejących na pl.wiki: nie linkuj ich w ogóle (zostaw jako zwykły tekst) lub użyj `{{link-interwiki|Hasło|Q=Qxxxxx|tekst=wyświetlany tekst}}` jeśli temat jest istotny.
- **NIGDY nie zostawiaj czerwonych linków** do nieistniejących artykułów przy tłumaczeniu z en.wiki. Sprawdź każde hasło przed dodaniem linku – albo link prowadzi do istniejącego artykułu, albo go usuwamy.
- Przed publikacją sprawdź wylinkowane strony: `curl -sL -o /dev/null -w '%{http_code}' 'https://pl.wikipedia.org/wiki/Nazwa_hasla'`. HTTP 200 = istnieje. HTTP 404 = nie ma → usuń link.

### Pułapki szablonu `{{link-interwiki}}` (zweryfikowane w sesji — sierpień 2026)

`{{link-interwiki}}` służy do linkowania haseł, które nie mają polskiej wersji, do ich encji w WIKIDANYCH. Linki międzyjęzykowe między Wikipediami są obsługiwane automatycznie przez Wikidane – NIE używaj `{{link-interwiki}}` do tego celu.

1. **Parametr to `Q=`, NIGDY `en=`.**
   <br>`{{link-interwiki|Hasło|Q=Q12345}}` — poprawnie.
   <br>`{{link-interwiki|Hasło|en=English title}}` — BŁĄD SKRYPTU: „Brakujące pola: Q. Nieznane pola: 'en'."
   <br>Realny błąd z sesji: użycie `en=` dało komunikat o błędzie dla co najmniej 20 wystąpień.

2. **NIE umieszczaj `{{link-interwiki}}` na początku artykułu** (przed infoboxem/leadem). Ten szablon służy do linkowania W TEKŚCIE, w miejscu wystąpienia terminu. Linki międzyjęzykowe (interwiki bottom bar) dodaje się przez połączenie WD z artykułem, nie przez ten szablon. Pytanie użytkownika „dlaczego dajesz na początku link interwiki???" wskazuje na ten błąd.

3. **Zawsze zweryfikuj, czy QID wskazuje na WŁAŚCIWĄ encję.** QID-y łatwo halucynuję. Realne błędy z sesji:
   - `Q756504` to **Atlantik-Brücke**, a nie Atlanticism
   - `Q7970500` to **Warren Steller** (trener sportowy), a nie Warren A. Bechtel
   - `Q1373714` to niemiecka ustawa komunalna, a nie Eurazjatyzm
   <br>Weryfikacja: otwórz `https://www.wikidata.org/wiki/QXXXXXXXX` i sprawdź label/description, ALBO użyj en.wiki API `action=query&prop=pageprops&titles=<Tytul>` (pole `wikibase_item`) — to zwróci poprawny QID dla danego angielskiego tytułu. Poprawne QID-y z sesji: Atlanticism=Q388698, Eurazjatyzm=Q1324222, Proamerykanizm=Q2844831, Warren A. Bechtel=Q7970006.

4. **Termin polski w `{{link-interwiki|Termin|Q=...}}` wpisuj w postaci odpowiedniej do kontekstu** (odmienionej), a Wikidane i tak pokierują w miejsce wpisanej formy — nie musisz podawać formy podstawowej. Realny przykład z sesji: `{{link-interwiki |podsekretarza stanu USA ds. zarządzania |Q=Q7883174}}` (celownik użyty zgodnie ze zdaniem) działa poprawnie.

5. **Jeśli termin w ogóle nie ma encji w Wikidanych** (brak artykułu w żadnej Wikipedii przy tym temacie), zostaw go jako zwykły tekst bez linku. Przykład z sesji: dziennikarz „Max Franke" — brak QID → bez linku.

## Kategorie

- Na samym końcu artykułu
- Format: `[[Kategoria:Nazwa kategorii]]`
- **Przed dodaniem kategorii sprawdź, czy ISTNIEJE na pl.wiki** (przez `https://pl.wikipedia.org/wiki/Kategoria:Nazwa`). W sesji z sierpnia 2026 wszystkie próby „Amerykańskie think tanki", „Stosunki niemiecko-amerykańskie", „Organizacje uznane w Rosji za niepożądane", „Prawo rosyjskie" okazały się NIEISTNIEJĄCE. Istniały np.: „Think tanki w Stanach Zjednoczonych", „Organizacje pozarządowe w Stanach Zjednoczonych", „Przedsiębiorstwa w Stanach Zjednoczonych", „Przedsiębiorstwa budowlane", „Cenzura w Rosji", „Łamanie praw człowieka w Rosji", „Stosunki międzynarodowe", „Teoria stosunków międzynarodowych", „Liberalizm", „Doktryny polityczne", „Geopolityka", „NATO". Nie twórz kategorii-ślepej uliczki.
- Sortowanie dla osób: `{{SORTUJ:Nazwisko, Imię}}`
- Dla biogramów: `{{Kontrola autorytatywna}}` przed kategoriami

## Reguły tekstu polskiego

- **Cudzysłów:** „..." (polskie zamknięte), NIE "..." (angielskie proste)
- **Myślniki (en-dash, U+2013):**
  - **DOZWOLONE w:** definicji w leadzie (`'''Termin''' – definicja`), podpisach grafik, punktach list wypunktowanych `* tekst – opis`, zakresach lat (1981–2011), tytułach cytowanych źródeł.
  - **ZABRONIONE w:** łączeniu zdań/zdań składowych w tekście głównym. Zamiast myślnika między klauzulami używaj kropki (nowe zdanie), przecinka lub średnika. Źle: `technologii – czego przykładami są...`. Dobrze: `technologii. Ich przykładami są...`.
  - **NIE myl z hyphenem (-)** – en-dash jest dłuższy.
- **Lead:** `'''Termin''' – definicja` – to JEDYNY wyjątek, myślnik w leadzie jest dozwolony i standardowy.
- **Tytuły sekcji:** muszą brzmieć naturalnie po polsku. Unikaj dosłownych kalk z angielskiego, zwłaszcza z użyciem „wielokrotnego użytku" jako przydawki przed rzeczownikiem:
  - Źle: `=== W pełni wielokrotnego użytku ===` (brzmi jak tłumaczenie „Fully reusable")
  - Dobrze: `=== Pełna odzyskiwalność ===` 
  - Źle: `=== Częściowo wielokrotnego użytku ===` (brzmi sztucznie)
  - Dobrze: `=== Odzyskiwalność częściowa ===`
  - W treści zdań „wielokrotnego użytku" jest OK jako określnik po rzeczowniku, np. „rakieta nośna wielokrotnego użytku" – ale nie jako przydawka przed nim w nagłówku sekcji.
- **Średniki:** unikaj w tekście encyklopedycznym, łącz zdania kropką lub spójnikiem
- **Autorzy w cytowaniach:** oddzielaj przecinkiem, NIE średnikiem
  - Poprawnie: `autor=Jan Kowalski, Anna Nowak`
  - Niepoprawnie: `autor=Jan Kowalski; Anna Nowak`
- **"i inni" w cytowaniach:** unikaj. Używaj tylko nazwiska pierwszego autora (np. `autor=Heribert Kuczera`, a nie `autor=Heribert Kuczera i in.`). {{cytuj}} automatycznie doda „i in." jeśli podasz więcej niż 5 autorów średnikami – ale w przypadku 2-3 autorów wypisz ich wszystkich.
- **Każde zdanie z faktem wymaga przypisu.** Nie wystarczy, że akapit ma jeden przypis na końcu – każde twierdzenie merytoryczne musi mieć własny `<ref>`. Zdania bez przypisu odbierane są jako nieencyklopedyczne, a o firmach jako promocyjne („reklama").

## Rosyjskie źródła — unikanie TASS i domen .ru

Przy hasłach dotyczących Rosji, rosyjskich instytucji, wydarzeń czy polityki — TASS (Rosyjska Agencja Informacyjna) i domeny .ru są powszechnie używane, ale na pl.wiki należy ich unikać jako głównych źródeł, ponieważ są to źródła państwowe podlegające bezpośredniej kontroli Kremla.

### Strategia znajdowania alternatyw dla TASS/.ru

1. **Artykuły przeglądowe (explainery)** — Al Jazeera, Reuters, BBC, The Moscow Times często publikują obszerne artykuły wyjaśniające, które podsumowują historię danego wydarzenia/instytucji. Jeden taki artykuł może dostarczyć źródło dla wielu wierszy w tabeli (np. Al Jazeera "What is the St Petersburg forum" z 2026 potwierdza pierwsze forum w 1997, liczbę uczestników, gości honorowych dla wielu edycji).

2. **The Moscow Times** (themoscowtimes.com) — niezależne rosyjskie medium w języku angielskim, zarejestrowane poza Rosją. Dobre źródło do faktów o Rosji, które nie jest TASS ani .ru.

3. **Archiwum oficjalnych stron (.com, nie .ru)** — oficjalne strony wydarzeń/instytucji często mają domeny .com (np. forumspb.com dla SPIEF). Są to źródła promocyjne, ale dopuszczalne dla faktów rutynowych (daty, liczby uczestników), gdy nie ma niezależnych mediów. Sprawdź przez Wayback Machine jeśli strona jest zablokowana.

4. **Zachodnie media dla edycji po 2014** — wydarzenia rosyjskie po aneksji Krymu (2014) i inwazji na Ukrainę (2022) są szeroko relacjonowane przez: Reuters, BBC, Financial Times, The Guardian, NPR, CNN, Al Jazeera. Dla tych lat łatwo znaleźć niezależne źródła.

5. **Media krajów uczestników** — jeśli w wydarzeniu brał udział przywódca kraju X, media z kraju X często to relacjonują (np. Indian Express o Modi na SPIEF 2017, NPR o Macronie na SPIEF 2018, ABC News Australia o Prabowo na SPIEF 2025).

6. **Wikipedia EN jako indeks źródeł** — angielska Wikipedia często ma rozbudowane przypisy. Można je wykorzystać jako trop do znalezienia oryginalnego źródła (ale NIE cytować samej Wikipedii). Sprawdź sekcję References przez API: `action=parse&page=Tytul&prop=text&section=N&format=json`.

### Ograniczenia
- Dla wczesnych edycji (przed 2010) wielu rosyjskich wydarzeń nie ma niezależnych zachodnich źródeł dokumentujących szczegółowe dane liczbowe. W takich przypadkach najlepszym dostępnym nie-TASS źródłem jest oficjalna strona wydarzenia (.com).
- Jeśli nie ma ŻADNEGO zweryfikowanego źródła nie-TASS dla danej tezy — lepiej nie dodawać tej tezy, niż cytować TASS. NIGDY nie cytuj artykułu przeglądowego (explainera) dla tezy, której ten artykuł konkretnie nie zawiera — nawet jeśli artykuł dotyczy tego samego tematu.
- TASS FACTBOXY są kuszące, bo kompilują oficjalne dane statystyczne w jednym miejscu. Pamiętaj: jeśli jedynym źródłem dla konkretnej tezy jest TASS, a nie możesz znaleźć alternatywy — teza po prostu nie ma niezależnego potwierdzenia.

### Przykład z sesji (lipiec 2026) — błędy i poprawki

Dla hasła „Petersburskie Międzynarodowe Forum Ekonomiczne" szukano zamienników dla 29 wystąpień TASS w tabeli edycji.

**Błąd (pierwsze podejście):** użyto artykułu Al Jazeera („What is the St Petersburg forum" z 2026) jako źródła dla 20+ wierszy tabeli — dla tez, których ten artykuł w ogóle nie zawiera (np. „Lukaszenka w 1998", konkretne liczby uczestników dla lat 1997–2015). Artykuł Al Jazeera to explainer — potwierdza ogólne fakty („pierwsze forum w 1997", „130+ państw w 2026") ale NIE potwierdza szczegółowych danych statystycznych.

**Poprawka:** cofnięto niesłuszne przypisy. Zastosowano tylko źródła, które faktycznie zawierają daną tezę:

| Edycja | Źródło | Potwierdzona teza |
|---|---|---|
| XXI (2017) | Indian Express | Modi gościem honorowym |
| XXII (2018) | NPR + The Diplomat | Macron i Abe na forum |
| XXVI (2023) | BBC | broń jądrowa na Białorusi |
| XXVIII (2025) | ABC News Australia | Prabowo gościem honorowym |
| XXIX (2026) | Al Jazeera | Arabia Saudyjska państwem-gościem |

Dla pozostałych edycji (I–XX, XXIII–XXV, XXVII) nie znaleziono niezależnych zachodnich źródeł potwierdzających konkretne dane liczbowe (liczba uczestników, konkretni uczestnicy) — te szczegóły istnieją tylko w TASS FACTBOXIE i oficjalnych danych organizatora.

## Źródła — higiena

### Źródła zabronione
- fronda.pl – niska wiarygodność
- rejestr.io – komercyjna nakładka na KRS
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
- Recenzowane artykuły naukowe
- Renomowane portale: rp.pl, tvn24.pl, onet.pl, polityka.pl, wyborcza.pl
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
- Każdy URL musi zwracać HTTP 200, zanim go dodasz.
- Jeśli domena nie resolve'uje się = źródło nie istnieje. Nie dodawaj.

**Zasada 5 – Zero portali wiki**
- Żadnych openlist.wiki, Wikipedia, fandom, memory/wiki itp.
- Treść edytowalna przez użytkowników = nieakceptowalna jako źródło.

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

### Przykład porażki (Stepan Rudnycki — lipiec 2026)

Poniższy przypadek wydarzył się naprawdę i jest udokumentowany. Służy jako przestroga.

**Zadanie:** znajdź dodatkowe przypisy do hasła o Stepanie Rudnyckim na pl.wiki.

**Co zrobiono źle:**

| Propozycja | Co poszło nie tak |
|---|---|
| sandarmoh.org (Юрий Дмитриев) | Domena nie istnieje. Nie sprawdzono przed dodaniem. |
| Engelmann, Albrecht Penck: Geograph und Politiker (1996) | Książka pod tym tytułem i rokiem nie istnieje. Zmyślony wpis bibliograficzny. |
| Ławrinenko, Rozstrilane widrodżennia | Nie sprawdzono, czy książka w ogóle wymienia Rudnyckiego. |
| Seegel, Map Men (2018) | Książka istnieje, ale treść niedostępna (paywall). Nie wiadomo, co pisze o Rudnyckim. |
| Memoriał (openlist.wiki) | Portal typu wiki — treść edytowalna przez użytkowników. |
| Stebelsky, Placing Ukraine on the Map | Książka istnieje, ale sugerowano konkretne numery stron bez dostępu do książki. |

**Lekcja:** z 6 propozycji źródeł, **0 było w pełni zweryfikowanych** — ani istnienie, ani dostęp do treści, ani zgodność z tezą. Każde naruszało co najmniej jedną z Zasad 1–6.

**Protip:** jeśli po przejściu protokołu okaże się, że nie ma żadnego źródła, które możesz zweryfikować — lepiej **nie dodawać nic**, niż dodać zmyślony lub niepotwierdzony przypis. Artykuł bez przypisu jest słaby, ale artykuł z fałszywym przypisem jest szkodliwy.


## NPOV (Neutralny punkt widzenia)

- Ton neutralny, bez pejoratywnych epitetów
- Sporne etykiety („teoria spiskowa", „afera") z atrybucją do źródła, nie w głosie encyklopedii
- Biogram dotyczy osoby, nie jest prasówką — fakty wpleć w „Życiorys"
- Nie zaniżaj kwalifikacji tematu jednym fakt-checkiem
- Dla firm: nie opieraj opisu na materiałach producenta, dodaj wątek krytyczny

### NPOV dla sekcji „Kontrowersje" i sporów

Przy opisywaniu kontrowersji, sporów i zarzutów stosuj dodatkowe reguły:

1. **Due weight (proporcjonalność).** Sekcja kontrowersji nie może dominować artykułu. Jeśli bieżący spór z 2026 r. zajmuje 40% tekstu o instytucji istniejącej od 2014 r. – to za dużo. Skróć o 50–70%, szczegóły przenieś do osobnego artykułu, jeśli kiedykolwiek powstanie.

2. **Parafraza zamiast cytatu.** Nie przytaczaj całych fragmentów wypowiedzi jednej strony sporu. Zamiast:
   > *"uznał działania za 'próbę cenzury, marginalizowania i uciszania głosów krytycznych'"*
   Napisz:
   > *"uznał działania prezes za próbę ograniczenia krytyki i zarzucił kierownictwu błędy w zarządzaniu"*

3. **Nie rozpisuj zarzutów w szczegółach – nawet w parafrazie.** Samo wyliczanie szczegółowych zarzutów jednej strony („brak kompetencji, zaniechania, naruszanie praw, pytania o X bez odpowiedzi, wyjęcie z kontekstu") tworzy wrażenie, że artykuł staje po tej stronie – zwłaszcza gdy druga strona nie przedstawiła stanowiska. Zredukuj do jednego neutralnego sformułowania: „zarzucił błędy w zarządzaniu". Szczegóły należą do osobnego artykułu o danym sporze, jeśli kiedykolwiek powstanie.

4. **Fakty vs zarzuty.** Każde oskarżenie opisz jako zarzut, nie fakt:
   - Źle: *"prawa były łamane"*
   - Dobrze: *"zgłosili podejrzenia naruszeń prawa pracy"*
   - Dobrze: *"Według doniesień medialnych byli pracownicy zgłosili do PIP podejrzenia naruszeń"*
   Używaj: „według doniesień", „rzekome", „podejrzenia", „miał/miała/mieli".

4. **Obie strony (lub adnotacja o ich braku).** Jeśli opisujesz zarzuty wobec instytucji, sprawdź, czy instytucja przedstawiła stanowisko. Jeśli nie – napisz wprost:
   > *"W dostępnych w momencie publikacji źródłach nie przedstawiono oficjalnego stanowiska [instytucji] ani [ministerstwa] w tej sprawie."*
   To jest lepsze niż udawanie, że równowaga istnieje.

5. **Język encyklopedyczny, nie prasowy.** Określenia typu „grzmi", „dziwna awantura", „burza" pochodzą z tytułów prasowych. Nie przenoś ich do encyklopedii. Nawet w tytule źródła (np. w `{{cytuj}}`) popraw tytuł na neutralny, jeśli źródło go ma pod sensowniejszym URL-em.

6. **Źródła do kontrowersji.** Oprócz doniesień medialnych dodawaj (jeśli istnieją):
   - komunikaty ministerstwa nadzorującego
   - stanowisko instytucji
   - dokumenty urzędowe (jeśli publicznie dostępne)

7. **Usuń źródła pierwotne stron sporu.** Jeśli jedna strona sporu publikuje swoje stanowisko na X/Twitterze, nie cytuj tego jako źródła – to jednostronne, niezweryfikowane i nieencyklopedyczne. Używaj wyłącznie doniesień medialnych, które relacjonują spór.

8. **Unikaj dublowania treści między sekcjami.** Nie powtarzaj tych samych wydarzeń w „Historii" i „Zadania i działania". Historia = chronologia (kiedy coś się wydarzyło). Zadania i działania = funkcje (co agencja robi). Jeśli to samo wydarzenie pojawia się w obu, usuń je z jednej sekcji.

## Lista kontrolna przed publikacją

- [ ] Temat jest encyklopedyczny (ma znaczenie poza lokalnym)
- [ ] Dostępne są co najmniej 2 źródła niezależne
- [ ] Infobox dopasowany do typu hasła i wypełniony
- [ ] Każde zdanie z twierdzeniem merytorycznym ma przypis (nie tylko akapit)
- [ ] Żaden przypis nie jest pusty (`<ref name="x" />` bez treści)
- [ ] Każdy nazwany przypis (`name="x"`) ma pełną definicję przy pierwszym użyciu
- [ ] `{{cytuj}}` z małej litery, NIE `{{Cytuj}}` ani `{{cytuj książkę}}`
- [ ] `<ref>` przed kropką i przecinkiem
- [ ] Cudzysłowy polskie „..."
- [ ] Autorzy oddzieleni przecinkiem, nie średnikiem
- [ ] URL-e zweryfikowane (web_fetch)
- [ ] Kategorie istnieją na pl.wiki
- [ ] `{{Przypisy}}`, nie `<references>`
- [ ] Linki wewnętrzne prowadzą do istniejących artykułów (lub użyto `{{link-interwiki}}`)
- [ ] `{{link-interwiki}}` używa `Q=` (NIE `en=`), nie jest na początku artykułu, a QID zweryfikowany, że wskazuje właściwą encję (otwarto QXXXXXXXX w Wikidanych)
- [ ] Kategorie — każda `[[Kategoria:...]]` istnieje na pl.wiki (sprawdzono przez pl.wikipedia.org/wiki/Kategoria:...)
- [ ] Sprawdzono HTTP 200 dla wszystkich linków wewnętrznych (`curl -sL -o /dev/null -w '%{http_code}' 'https://pl.wikipedia.org/wiki/Haslo'`)
- [ ] Opis w Wikidanych ustawiony
- [ ] Brak komentarzy HTML (`<!-- ... -->`) w treści artykułu — plik zawiera wyłącznie wikikod
- [ ] Styl neutralny i encyklopedyczny
- [ ] Nie cytowano źródeł bez dostępu do treści
- [ ] Myślnik w leadzie – tylko w definicji `'''Termin''' – definicja`
- [ ] Brak myślników łączących zdania w tekście głównym (zastąpione kropką lub przecinkiem)
- [ ] Brak czerwonych linków – każde `[[link]]` prowadzi do istniejącego artykułu na pl.wiki
- [ ] Pola infoboxu zweryfikowane z rzeczywistym szablonem (API), żadnych pól `www`, `strona` itp.
- [ ] Nazwane przypisy użyte w infoboxie zdefiniowane w treści (leadzie)
- [ ] Doprecyzowane określenia relacyjne („spółka matka (Ito-Yokado)" a nie samo „spółka matka")
- [ ] Dla firm: `giełda` używa szablonu `{{tyo|numer}}`, nie ręcznego linku
- [ ] `commons` w infoboxie, nie osobny `{{Commons}}` na dole
- [ ] Dane finansowe: `rok` z przypisem, wartości w linijkach bez dat i przypisów
- [ ] Dla {{Instytucja państwowa infobox}}: brak pola `budżet` (przeniesiony do sekcji „Zarządzanie")
- [ ] Brak osobnej sekcji „Kierownictwo" (prezes/wiceprezes są w infoboxie)
- [ ] Lead: każdy akapit ma własny przypis inline
- [ ] Lead: brak oczywistości powielających infobox („Na czele agencji stoi prezes")
- [ ] Pokrewne tematy zgrupowane (siedziba + oddziały + struktura + lista prezesów → „Zarządzanie")
- [ ] Historia: faktyczne kamienie milowe, nie lista politycznych nominacji/dymisji
- [ ] Opis struktury: faktyczne departamenty, nie „trzy piony: prezes i wiceprezesi"
- [ ] Historia i Zadania/działania nie dublują się (Historia = chronologia, Zadania = funkcje)
- [ ] Kontrowersje: proporcjonalne (nie dominują artykułu), zarzuty jako zarzuty, bez szczegółowego wyliczania jednej strony

## Precyzja terminologiczna — pułapki przy tłumaczeniu haseł technicznych

Przy tłumaczeniu artykułów z zakresu astronautyki/inżynierii z en.wiki na pl.wiki uważaj na fałszywe odpowiedniki:
| en.wiki | NIE tłumacz jako | DLACZEGO | Poprawnie po polsku |
|---|---|---|---|
| Space Shuttle | rakieta nośna | Wahadłowiec to **system orbitalny**, nie rakieta. Nazywanie go „rakietą nośną" jest nieprecyzyjne. | „system orbitalny wykorzystujący elementy wielokrotnego użytku" |
| spaceplane glides, parachutes slow it down | „samoloty kosmiczne szybują, a do hamowania służą spadochrony" | Mylisz dwa typy pojazdów: samoloty kosmiczne lądują jak szybowce (bez spadochronów), kapsuły/boostery hamują spadochronami. | „Samoloty kosmiczne lądują poziomo jak szybowce, natomiast człony rakiet i kapsuły hamują za pomocą spadochronów lub silników rakietowych." |
| fully reusable | „w pełni wielokrotnego użytku" jako przydawka w tytule sekcji | Kalka brzmi nienaturalnie po polsku. | tytuł sekcji: „Pełna odzyskiwalność" |
| partially reusable | „częściowo wielokrotnego użytku" w tytule | j.w. | tytuł sekcji: „Odzyskiwalność częściowa" |
| reusability | „wielokrotne użycie" w tytułach | OK w treści, ale w tytułach lepiej „odzyskiwalność" | „odzyskiwalność" w tytułach, „wielokrotne użycie/wykorzystanie" w tekście |
| booster | „booster" (anglicyzm) | Po polsku: „dopalacz", „człon boczny" | „dopalacze", „stopnie boczne", „rakiety pomocnicze" |
| rocket stage | „stopień" (w kontekście odzysku) | Lepiej „człon rakiety" | „człon rakiety", „stopień rakiety" |

**Zasada ogólna:** jeśli tytuł sekcji lub zdanie brzmi jakby było przetłumaczone słowo w słowo z angielskiego (zwłaszcza z długą przydawką przed rzeczownikiem: „w pełni wielokrotnego użytku rakieta"), to znaczy że jest niepoprawne po polsku. Przepisz je tak, by brzmiało naturalnie.

## Naturalny szyk polski i spójność terminologiczna (zweryfikowane w sesji — sierpień 2026)

### Szyk wyrazów: unikaj kalk rosyjskich i angielskich

Polski ma elastyczny, ale nie dowolny szyk. Przy tłumaczeniu nazw pojęć złożonych pilnuj naturalnej kolejności: rzeczownik wiodący + przydawka/dopełniacz.

Realne poprawki z sesji (tworzenie hasła o „liberal international order"):
- **ŹLE:** „Liberalny międzynarodowy ład" — brzmi jak kalka (szyk dwóch przymiotników przed rzeczownikiem).
- **DOBRZE:** „Liberalny ład międzynarodowy" (Liberalny + ład + międzynarodowy).
- Analogicznie: „atlantyzm", nie „atlantycyzm".

Zasadę tę stosuj też do nazw artykułów i tytułów sekcji — jeśli szyk brzmi nie po polsku, przestaw wyrazy.

### Terminologia zgodna z istniejącymi hasłami pl.wiki

Zanim wybierzesz polski odpowiednik terminu-klucz, sprawdź, jak nazywa się istniejące hasło na pl.wiki, i bądź z nim spójny. Przykład z sesji:
- en. „international order" ma na pl.wiki hasło **„Ład międzynarodowy"** — więc w hasłach pochodnych używaj **„ład"** („liberalny ład międzynarodowy"), NIE „porządek".
- Ale rozróżnij terminy techniczne, gdzie „porządek" jest właściwe: „porządek polityczny", „porządek konstytucyjny" (terminologia Ikenberry'ego), „porządek westfalski", „porządek przymusowy". Użyj hasła-nadrzędnego („ład") dla pojęcia wiodącego, a „porządek" dla konkretnych terminów technicznych/cudzych definicji.

Zasada: **dopasuj nomenklaturę do istniejącej struktury kategorii i haseł pl.wiki; nie wymyślaj własnego odpowiednika, jeśli istnieje już przyjęty.**

## Adaptacja artykułów z innych wersji językowych Wikipedii

Podczas tłumaczenia/adaptacji artykułów z obcojęzycznych Wikipedii (niemieckiej, angielskiej itp.) na pl.wiki nie kopiuj ślepo struktury oryginału. Stosuj następujące zasady:

### Struktura — dostosuj, nie kopiuj
- **Lead musi streszczać cały artykuł** — nie wystarczy jednozdaniowa definicja. Lead powinien zawierać: ramy czasowe, patronat, cel, kluczowe kontrowersje/krytykę i ostateczny los/rezultat.
- **Organizacja/struktura wewnętrzna** – sekcje z tabelami przewodniczących, biur, kadencji itp. są typowe dla de.wiki, ale na pl.wiki lepiej wpleść te informacje w tekst główny, zamiast tworzyć osobne podsekcje z tabelami.
- **Tabele wydarzeń** (np. lista corocznych konferencji, edycji, spotkań) – na pl.wiki zastąp je krótkim opisem tekstowym, chyba że dane są niezbędne. Kilka konkretów wystarczy: miasta, ważniejsze inicjatywy, data ostatniego wydarzenia.
- **Osobne sekcje poboczne** (np. „Wystawa X", „Nagroda Y") – jeśli nie są kluczowe dla tematu, usuń je lub skróć do jednego zdania. Treść może trafić do bibliografii.

### Przypisy — adaptacja z obcego oryginału
- Każda teza wymaga własnego przypisu inline. Przetłumaczony akapit z jednym przypisem na końcu to za mało — każde zdanie merytoryczne musi mieć `<ref>`.
- Konwertuj format citation obcej Wikipedii na `{{cytuj}}` zgodny z pl.wiki:
  - `{{Internetquelle}}` (de.wiki) → `{{cytuj}}` z parametrami: `url=`, `tytuł=`, `opublikowany=`, `data=`, `data dostępu=`, `język=`
  - `{{Literatur}}` (de.wiki) → `{{cytuj}}` z parametrami: `autor=`, `tytuł=`, `opublikowany=`/`czasopismo=`, `miejsce=`, `isbn=`, `s=`, `język=`
  - Nazwy refów z oryginału (`<ref name=":0">`) — zamień na czytelne nazwy (`<ref name="sueddeutsche">`) przy pierwszym użyciu.
- Nie dodawaj źródeł, których nie otworzyłeś i nie potwierdziłeś treści (patrz: Źródła — higiena > Protokół weryfikacji). Paywall = brak cytowania.

### Linki wewnętrzne przy adaptacji
- Sprawdź każde hasło, które chcesz zalinkować – linkuj TYLKO istniejące artykuły na pl.wiki. Weryfikuj przez `curl -sL -o /dev/null -w '%{http_code}' 'https://pl.wikipedia.org/wiki/Haslo'`. HTTP 200 = istnieje. HTTP 404 = nie ma → usuń link.
- Nazwiska obcych autorów/komentatorów (np. Otto Luchterhandt, Gemma Pörzgen, Irina Szczerbakowa) często nie mają artykułów na pl.wiki – nie linkuj ich.
- Fundacje zagraniczne (np. Heinrich-Böll-Stiftung) mogą istnieć pod inną nazwą lub wcale – sprawdź przed dodaniem linku.

### Iteracyjne poprawki
- Po pierwszym szkicu spodziewaj się uwag strukturalnych (które sekcje zostawić, które skrócić). To normalne przy adaptacji między Wikipediami.
- User często woli skrócone wersje z mniejszą liczbą sekcji, ale z pełniejszym leadem i przypisami do każdej tezy.

## Najczęstsze błędy

1. **Puste przypisy** – `<ref name="x" />` bez wcześniejszej definicji. Zawsze definiuj przy pierwszym użyciu.
2. **Szablony, które nie istnieją** – ZAWSZE sprawdź, czy szablon istnieje na pl.wiki przed jego użyciem. Przejdź do `https://pl.wikipedia.org/wiki/Szablon:Nazwa_szablonu`. Często zakładane, a nieistniejące: `{{Właściwy tytuł}}`, `{{Krótki opis}}` (Short description z en.wiki), `{{Astronautyka}}`, `{{Nowe technologie}}`, `{{Operacyjny}}`. Istnieją natomiast: `{{Flaga}}`, `{{Commons}}` (nie `{{Commons category}}`), `{{Przypisy}}`, `{{Osobny artykuł}}`, `{{tabela-tak}}`, `{{tabela-nie}}`, `{{Rakieta nośna infobox}}`, `{{tyo|...}}`.
3. **`{{Cytuj}}` z dużej litery** – na pl.wiki szablon jest z małej: `{{cytuj}}`.
4. **`<ref>` po kropce** – idzie przed interpunkcją.
5. **Brak przypisów w akapicie** – każdy akapit wymaga źródła.
6. **Opieranie się na jednym źródle** – maks. 4–5 przypisów na jedno źródło, rozkładaj tezy.
7. **Cytowanie książek bez wglądu** – NIGDY nie podawaj stron z książek bez dostępu.
8. **ISBN bez walidacji** – sprawdź cyfrę kontrolną.
9. **Linki do 404** – każdy URL zweryfikuj przed dodaniem.
10. **Niewypełniony infobox** – wszystkie znane pola powinny być wypełnione.
11. **Pomylenie `{{Commons}}` z `{{Commons category}}`** – na pl.wiki używa się `{{Commons}}`, nie `{{Commons category}}`.
12. **Używanie en.wiki-tytułowych szablonów statusu w tabelach** – zamiast `{{Tak|tekst}}`/`{{Nie|tekst}}` używaj `{{tabela-tak|tekst}}`/`{{tabela-nie|tekst}}`.
13. **Nieistniejące pola w infoboxie** – parametry typu `www`, `strona`, `logo_size` często nie istnieją w szablonie. Sprawdź przez API przed dodaniem (`action=parse&page=Szablon:Nazwa_infoboxu&prop=wikitext`). Nie wprowadzaj pól z en.wiki na ślepo.
14. **Nazwany przypis w infoboxie bez definicji w treści** – jeśli infobox używa `<ref name=X />`, definicja `<ref name=X>{{cytuj|...}}</ref>` musi pojawić się w tekście artykułu (najlepiej w leadzie). Inaczej parser nie znajdzie treści przypisu.
15. **Nieprecyzyjne określenia relacyjne** – frazy „słabnąca spółka matka", „spółka zależna" bez wskazania nazwy firmy są niezrozumiałe. Doprecyzowuj w nawiasie: „słabnąca spółka matka (Ito-Yokado)".
16. **Używanie „i in." / „i inni" w polu `autor=` w {{cytuj}}** – nie pisz tego ręcznie. Podaj tylko pierwsze nazwisko (np. `autor=Heribert Kuczera`) lub wypisz wszystkich autorów po przecinku. {{cytuj}} sam doda „i in." jeśli autorów jest >5. Ręczne „i in." jest zbędne i niezalecane.
17. **Myślnik w zdaniu zamiast kropki** – nie łącz zdań en-dashem (–) w tekście głównym. Źle: „technologia ewoluowała – jej przykładem jest X". Dobrze: „technologia ewoluowała. Jej przykładem jest X".
18. **Tytuły sekcji brzmiące jak kalka z angielskiego** – zamiast „=== W pełni wielokrotnego użytku ===" pisz „=== Pełna odzyskiwalność ===". Jeśli tytuł brzmi nienaturalnie po polsku, znajdź lepsze sformułowanie.
19. **Zdania o firmach/technologiach bez przypisów** – każde twierdzenie merytoryczne (zwłaszcza o planach firm) wymaga przypisu. Brak przypisu sprawia wrażenie promocyjne („reklama").
24. **Ręczny link giełdowy zamiast szablonu `{{tyo}}`** – dla spółek na TYO używaj `{{tyo|numer}}`, nie `[[Giełda Papierów Wartościowych w Tokio|TYO]]: numer`.
25. **`commons` jako osobny szablon zamiast w infoboxie** – dodawaj `|commons=` w infoboxie, nie `{{Commons}}` na dole.
26. **Rok i przypis w każdej linii finansowej** – użyj `|rok=` z przypisem, wartości w linijkach bez dat.
27. **Przypisy bez URL – niedozwolone.** Każdy `{{cytuj}}` MUSI mieć `url=` z działającym linkiem. Źródła z japońskich gazet (Yomiuri, Mainichi itp.) często nie mają publicznie dostępnych URL-i – nie cytuj ich, jeśli nie możesz podać działającego linku. Zastąp oficjalną stroną firmy lub artykułem z otwartego źródła (Reuters, BBC, NYT, Bloomberg, AP).
28. **Usunięcie istniejących przypisów podczas przepisywania sekcji** – podczas zmiany formatu sekcji (np. z bullet pointów na prozę) NIGDY nie usuwaj istniejących `<ref>` bez zastąpienia ich nowymi. Każde stwierdzenie merytoryczne musi mieć własny przypis inline. Jeśli nie masz źródła dla danej tezy – usuń tezę, nie przypis. Zasada: najpierw przenieś wszystkie `<ref>` do nowej wersji, potem dopiero redaguj treść.
29. **Sekcje w formie bullet pointów/listy** – na pl.wiki unika się list punktowanych w sekcjach merytorycznych (zwłaszcza „Zadania i działania", „Działalność" itp.). Lista punktowana sprawia wrażenie broszury promocyjnej, a nie encyklopedii. Przepisz na zwartą prozę: zgrupuj pokrewne tematy w akapity, usuń frazy wartościujące („budowa kompetencji", „rozwój potencjału", „kluczowe inicjatywy"), zachowaj wszystkie przypisy.
30. **Język promocyjny w sekcjach instytucji** – frazy typu „budowa w Polsce kompetencji", „rozwój potencjału", „konkurencyjności na rynku międzynarodowym", „znacznie przyspieszy", „najważniejszych imprez branżowych", „najciekawsze inicjatywy" pochodzą z materiałów PR-owych instytucji. W encyklopedii zastąp je neutralnymi opisami: „koordynacja rozwoju", „organizuje wydarzenia", „zleciła opracowanie".
31. **Źródło pierwotne zamiast wtórnego** – strona internetowej opisywanej instytucji to źródło pierwotne. Preferuj źródła wtórne (niezależne media, dokumenty innych instytucji, akty prawne). Wyjątek: lista umów/porozumień podpisanych przez instytucję – tu źródło pierwotne jest akceptowalne, bo instytucja jest naturalnym depozytariuszem tych informacji.
32. **Usunięcie wikilinków podczas przepisywania** – podczas zmiany formatu sekcji (bullet pointy → proza) zachowaj wszystkie wikilinki do encji (agencji, instytucji, osób). Nie zastępuj ich gołym tekstem ani akronimami bez linków.
33. **Lead bez przypisów** – każdy akapit w leadzie (wstępie) artykułu wymaga własnego przypisu. Lead to streszczenie całego artykułu, ale każde twierdzenie w nim musi być udokumentowane. Nie wystarczy, że treść jest rozwinięta w dalszych sekcjach – lead też wymaga źródeł inline.
34. **Rozbijanie powiązanych treści na osobne sekcje** – siedziba, oddziały, struktura organizacyjna i lista prezesów to pokrewne tematy dotyczące zarządzania instytucją. Zamiast tworzyć osobne sekcje „Siedziba i oddziały" i „Kierownictwo", zgrupuj je w jednej sekcji „Zarządzanie". To samo dotyczy innych typów artykułów: grupuj pokrewne informacje w spójne sekcje.
35. **Sekcja „Kierownictwo" przy instytucjach** – prezes i wiceprezes są już w infoboxie ({{Instytucja państwowa infobox}}). Nie twórz osobnej sekcji „Kierownictwo" w treści – to zbędne powielenie. Listę historycznych prezesów umieść w sekcji „Zarządzanie" jako podsekcję „Lista prezesów".

36. **Oczywistości w leadzie** – nie pisz „Na czele agencji stoi prezes" ani podobnych tautologii. Infobox już pokazuje szefa instytucji. Lead powinien podawać informacje, których nie ma w infoboxie – strukturę organizacyjną, zakres obowiązków, liczbę pionów. Jeśli infobox ma |szef=|, nie powtarzaj tego w tekście.

37. **„Trzy piony: prezes i wiceprezesi" jako opis struktury** – to nie jest opis struktury, tylko tautologia (każda organizacja ma szefa i zastępców). Zamiast tego podaj faktyczne departamenty/jednostki organizacyjne: „W strukturze POLSA funkcjonują departamenty zajmujące się strategią, współpracą międzynarodową, programami kosmicznymi...".

38. **Historia instytucji jako lista politycznych nominacji i dymisji** – sekcja „Historia" powinna pokazywać faktyczne kamienie milowe w życiu instytucji (przystąpienie do konsorcjów, podpisanie kluczowych umów, zmiany kompetencji, przełomowe wydarzenia), a nie polityczną kronikę „kogo premier X odwołał przed końcem kadencji". Lista prezesów należy do sekcji „Zarządzanie/Lista prezesów", nie do „Historii". W „Historii" prezesów wymieniaj tylko w kontekście faktycznych wydarzeń, które za ich kadencji nastąpiły. Unikaj fraz: „odwołany przez premiera X, choć kadencja miała trwać 5 lat", „odwołany przez ministra Y z rządu Z" – to polityczne komentarze, nie fakty encyklopedyczne.

39. **Dublowanie treści między sekcjami „Historia" i „Zadania i działania"** – te sekcje mają różne funkcje: Historia = chronologia (kiedy coś się wydarzyło), Zadania = funkcje (co agencja/instytucja robi). Nie powtarzaj tych samych wydarzeń w obu. Jeśli to samo wydarzenie pojawia się w obu sekcjach, usuń je z jednej.

40. **Szczegółowe wyliczanie zarzutów jednej strony w kontrowersjach** – nawet w parafrazie, samo wyliczanie szczegółów („brak kompetencji, zaniechania, naruszanie praw, pytania bez odpowiedzi") tworzy wrażenie stronniczości, zwłaszcza gdy druga strona nie przedstawiła stanowiska. Zredukuj do jednego neutralnego sformułowania: „zarzucił błędy w zarządzaniu". Szczegóły należą do osobnego artykułu.
41. **Komentarze HTML w treści artykułu/pliku** – nie wstawiaj `<!-- ... -->` (oznaczenia „do uzupełnienia", „źródło do dodania", „sekcja analityczna") do pliku z artykułem. To śmieci edytorskie, nie treść encyklopedyczna. Jeśli tezy nie da się podeprzeć źródłem, usuń ją zamiast oznaczać komentarzem; notatki robocze trzymaj poza plikiem artykułu.

## Propozycje do rubryki „Czy wiesz"

Gdy artykuł jest zgłoszony do „Czy wiesz" na stronie głównej, możesz zostać poproszony o zaproponowanie pytań. Pytania muszą być oparte WYŁĄCZNIE na treści artykułu – nie na źródłach, z których artykuł korzysta.

### Zasady tworzenia pytań

1. **Tylko to, co jest w artykule.** Nie cytuj faktów znalezionych w źródle, jeśli nie zostały przepisane do artykułu. Czytelnik ma kliknąć w artykuł i znaleźć tam odpowiedź.

2. **Zero zakładania wiedzy czytelnika.** Czytelnik nie wie, kim jest opisywana postać ani czym jest koncepcja. Pytanie musi być zrozumiałe bez kontekstu. „…kogo z federacji wykluczył Rudnycki?" – złe, bo czytelnik nie wie kim jest Rudnycki. Dobrze: „…kto proponował federację Ukrainy z Białorusią i krajami bałtyckimi?" – odpowiedzią jest tytuł artykułu.

3. **Unikaj specjalistycznej terminologii.** „Bałtycko-pontyjski", „Międzymorze", „geopolityka" – przeciętny czytelnik może tych słów nie rozumieć. Używaj języka potocznego: „federacja państw od Bałtyku po Morze Czarne", a nie „federacja bałtycko-pontyjska".

4. **Zero redundantnych określeń.** Nie dopisuj „niepodległej" przed „Ukrainą", jeśli kontekst już zakłada niepodległość. Nie pisz „przyszłego państwa ukraińskiego", skoro wiadomo o co chodzi.

5. **Unikaj zdań z „według X".** „…według polskich publicystów koncepcję Rudnyckiego przekreśliła aneksja Krymu?" – brzmi nienaturalnie. Lepiej prosto: „…której koncepcji założenia przekreśliła aneksja Krymu w 2014?".

6. **Krótko i prosto.** Pytanie powinno mieć 8–15 słów. Im krócej, tym lepiej. Jedna myśl na pytanie.

7. **Sprawdź WP:SYNCH.** Upewnij się, że sformułowanie w pytaniu ma bezpośrednie oparcie w treści artykułu, a nie jest twoją interpretacją lub syntezą faktów.

### Przykłady z tej sesji (lipiec 2026)

| Źle | Dlaczego | Dobrze |
|---|---|---|
| …kto jest uważany za twórcę nowoczesnej geografii Ukrainy? | OK (to pierwsze pytanie, które przeszło) | – |
| …kogo z federacji bałtycko-pontyjskiej wykluczył Rudnycki? | Czytelnik nie wie kim jest Rudnycki; „bałtycko-pontyjskiej" – nikt nie rozumie | …kto proponował federację Ukrainy z Białorusią i krajami bałtyckimi? |
| …dlaczego według polskich publicystów aneksja Krymu w 2014 przekreśliła koncepcję Rudnyckiego? | „według polskich publicystów" brzmi dziwnie; czytelnik nie zna Rudnyckiego | …której koncepcji założenia przekreśliła aneksja Krymu w 2014? |
| …kto uważał Morze Czarne za główny kierunek rozwoju niepodległej Ukrainy? | „niepodległej" jest redundantne – oczywiste, że chodzi o niepodległą Ukrainę | …kto uważał Morze Czarne za główny kierunek rozwoju Ukrainy? |

## Złote zasady

1. Definicja przed użyciem (nazwane przypisy), potem rozdzielność źródeł.
2. Weryfikowalność ponad estetyką — lepiej mniej tez z przypisami niż więcej bez.
3. Źródła oficjalne i niezależna prasa ponad materiały stron zainteresowanych.
4. Link do 404 nie jest źródłem.
5. **Zweryfikuj źródło zanim je zaproponujesz** — nigdy nie sugeruj przypisów na podstawie domysłów o treści.
6. Nie wymyślaj szablonów — testuj w podglądzie przed publikacją.
7. Krótsze hasło z 5 czystymi, niezależnymi źródłami bije dłuższe rozdęte słabymi przypisami.
8. **Nie dodawaj komentarzy HTML (`<!-- ... -->`) do treści artykułu/pliku z artykułem.** Komentarze edytorskie („do uzupełnienia", „teza wymaga źródła", „sekcja analityczna") nie są treścią encyklopedyczną — plik z artykułem ma zawierać WYŁĄCZNIE wikikod artykułu. Jeśli nie masz źródła dla tezy, pomiń ją; jeśli masz notatki robocze, trzymaj je poza plikiem artykułu.

## Materiały pomocnicze

Skill zawiera dodatkowe pliki referencyjne:

- `references/template-existence.md` — lista szablonów pl.wiki: które istnieją, które nie, i czym je zastąpić (kluczowe przy tłumaczeniu z en.wiki!)
- `references/checklist.md` — lista kontrolna przed publikacją (z sekcją weryfikacji źródeł)
- `references/citation-guidelines.md` — wytyczne cytowania
- `references/red-flags.md` — ryzyka i ostrzeżenia
- `references/workflow.md` — kolejność kroków tworzenia artykułu
- `references/source-verification.md` — protokół weryfikacji źródeł przed dodaniem przypisu (Open Library, sprawdzanie domen, test zgodności tezy ze źródłem)
- `references/source-verification-case-study.md` — szczegółowy case study: sesja Stepan Rudnycki (lipiec 2026), dokumentująca 6 błędnych propozycji źródeł i ich weryfikację
- `references/section-rewriting-case-study.md` — case study: przepisywanie sekcji POLSA (lipiec 2026) — technika konwersji bullet pointów na prozę, pułapka usuwania przypisów, NPOV dla instytucji
- `references/wikidata-description.md` — jak ustawić polski opis w Wikidanych dla nowego artykułu
- `references/przedsiebiorstwo-infobox.md` — pola i pułapki szablonu {{Przedsiębiorstwo infobox}} (dozwolone/nieistniejące pola, wzorzec danych finansowych, szablony giełdowe, commons w infoboxie)
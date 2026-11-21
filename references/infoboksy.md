# Infoboksy — dobór szablonu wg typu hasła i zweryfikowane pola

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

### Organizacje ponadnarodowe bez jednej stolicy (UE i podobne)
`{{Państwo infobox}}` NIE ma pola na siedziby instytucji. Nie wyliczaj instytucji w `|stolica=` — wygląda to, jakby organizacja miała kilka formalnych stolic. Podaj w polu jedno miasto (siedzibę większości instytucji), a rozkład siedzib opisz w treści z przypisem do protokołu o siedzibach (CELEX 12016E/PRO/06).

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
**Nieistniejące pola (błąd „Nieznane pola"):** `nazwa`, `nazwa oryginalna`, `rodzaj`, `data uchwalenia`, `www`. Tytuł podajesz jako `|tytuł aktu=` (nie `|nazwa=`), a datę wejścia jako `|data wejścia w życie=` (nie `|data uchwalenia=`). Ten szablon NIE ma pola `www`. Projekt nieprzyjętego aktu: domyślnie bez infoboksa — szablon opisuje akt przyjęty; status legislacyjny opisz w prozie.

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
{{Wydarzenie infobox
 | nazwa            = 
 | nazwa oryginalna = 
 | grafika          = 
 | opis grafiki     = 
 | państwo          = 
 | miejscowość      = 
 | data             = 
 | uczestnicy       = 
 | poprzednie       = 
 | następne         = 
 | commons          = 
 | www              = 
}}
```
Pola potwierdzone w źródle szablonu (API): `nazwa`, `nazwa oryginalna`, `grafika`, `opis grafiki`, `motto`, `państwo` (+`wariant flagi`), `miejscowość`, `data`, `uczestnicy`, `poprzednie`/`następne` (+`rok poprzedniego`/`rok następnego`), `kod mapy`, `wariant mapy`, `opis miejsca`, `współrzędne`, `punkty mapy`, `commons`, `wikinews`, `www`. Szablon NIE MA pól `przyczyna`, `wynik`, `ofiary` (w przeciwieństwie do en.wiki `Infobox event`) — przyczynę sporu, bilans ofiar i przebieg opisuj w prozie z przypisami.

### Dla pocisków/broni
```wiki
{{Pocisk antybalistyczny infobox}}
<!-- lub dedykowany infobox dla danego typu sprzętu -->
```

### Dla jednostek wojskowych — {{Jednostka wojskowa infobox}}
Szablon istnieje. Pola potwierdzone na żywym haśle go używającym: `nazwa`, `nazwa oryginalna`, `grafika`, `opis grafiki`, `państwo` (`{{państwo|USA}}`), `wariant flagi`, `sformowanie`, `rozformowanie`, `rodowód`, `kontynuacja`, `podległość`, `dowódca pierwszy`, `dowódca obecny`, `dowódca ostatni`, `dyslokacja`, `motto`, `znak`, `kategoria wojska`, `numer`, `kryptonim`. Jeśli fetch samego szablonu pada, weryfikuj pola na wikitexcie żywego hasła, które go stosuje. Kategoria zamiast nieistniejących wariantów: „Amerykańskie jednostki organizacyjne wojska”.

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

### Baretki odznaczeń w `{{Biogram infobox}}` (pole `odznaczenia`)

Zasady (zweryfikowane październik 2026) przeniesione do references/baretki-odznaczen.md.

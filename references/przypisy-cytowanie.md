# Przypisy — formatowanie: {{cytuj}} i zasady refów

Numeracja 3.x zachowana z SKILL.md (odwołania typu „patrz 3.7" dotyczą sekcji w tym pliku).

## Przypisy — formatowanie (najważniejsza sekcja)

### 3.1 Format cytowania — preferencja użytkownika: zawsze {{cytuj}}

**ZAWSZE stosuj szablon `{{cytuj}}` we wszystkich przypisach** (użytkownik 2026-10-31: „w przypisach ZAWSZE stosuj szablon Cytuj”). WCZEŚNIEJSZE zalecenie o inline refs `[url tytuł], wydawca` jest NIEAKTUALNE — nie twórz refów inline. Dla źródeł internetowych wzorzec:

```wiki
<ref name="skrot">{{cytuj |tytuł = Tytuł artykułu |url = https://example.com |opublikowany = Nazwa wydawcy |data = 2024-01-15 |data dostępu = 2026-10-31 |język = pl}}</ref>
```

- Pola wg tabeli 3.2: `tytuł`, `url`, `opublikowany` (serwis/wydawca), `data` (YYYY-MM-DD), `data dostępu`, `język`; bez znanej daty pomijaj `data =`.
- Autor tylko gdy istotny: `autor = Imię Nazwisko`, wielu po przecinku, NIE pisz „i inni” (szablon sam doda „i in.” przy >5 autorach).
- Prace naukowe: wzorce 3.2a (arXiv: `czasopismo=arXiv` + `doi` + `arxiv`, bez `url`) i 3.2b (konferencje: `rozdział=` + `tytuł=`).
- NIE używaj wariantów `{{cytuj książkę}}`, `{{cytuj pismo}}`, `{{cytuj stronę}}` — do wszystkiego `{{cytuj}}` z odpowiednimi polami.
- Wszystkie pozostałe zasady obowiązują bez zmian: definicja przed użyciem, `<ref>` przed interpunkcją, `{{Przypisy}}`, równoważenie źródeł, weryfikacja URL-i.
- Przy dopisywaniu do żywego artykułu cudze przypisy zostaw bez normalizacji stylu (normalizacja powiększa diff bez korzyści merytorycznej); nowe refy zawsze w `{{cytuj}}`.

### 3.2 Pola szablonu {{cytuj}} — lista DOZWOLONYCH parametrów
Standard dla WSZYSTKICH przypisów (preferencja użytkownika 2026-10-31; wzorce naukowe w 3.2a/3.2b). Tylko poniższe pola są akceptowane. Użycie innego parametru powoduje komunikat „Nieznane pola”.

| Parametr | Znaczenie | Uwaga |
|---|---|---|
| `autor=` | Imię Nazwisko (wielu po przecinku, NIE średnikiem) | |
| `tytuł=` | Tytuł artykułu/strony | |
| `url=` | Pełny adres URL | Zweryfikuj przez web_fetch |
| `opublikowany=` / `czasopismo=` / `wydawca=` | Nazwa źródła | |
| `data=` | Data publikacji (YYYY-MM-DD lub YYYY) | NIE `rok=` |
| `data dostępu=` | Data sprawdzenia źródła | |
| `s=` | Numer strony | NIE `strony=`. Dozwolone tylko w szablonie cytuj — w Cytuj stronę / Cytuj książkę używaj parametru `strony=` (wpadka z renderem Nieznane pola, Influencer 10.2026) |
| `isbn=` | ISBN | Sprawdź cyfrę kontrolną |
| `archiwum=` | Link do archiwum (web.archive.org) | |
| `zarchiwizowano=` | Data archiwizacji | |
| `język=` | Kod języka (`pl`, `en`, `de`) | |
| `wolumin=` | Wolumin czasopisma | |
| `numer=` | Numer czasopisma | |
| `doi=` | DOI identyfikator | Dla arXiv: `10.48550/arXiv.<ID>` |
| `arxiv=` | Identyfikator arXiv (`1406.2661`, bez prefiksu i numeru wersji) | Szablon sam buduje link arxiv.org — wtedy NIE dodawaj `url=` | |
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
- `współautorzy=` → nie istnieje (błąd „Nieznane pola" widoczny dopiero w render-checku serwera); wszystkich autorów wpisz do `autor=` po przecinku
- `autor r=` → użyj `autor r=` (UWAGA: to jest dozwolone tylko z `rozdział=`)
- `odpowiedzialność=` → rzadkie, ale dozwolone

### 3.2a Wzorzec cytowania prac z arXiv (zweryfikowane expandtemplates, wrzesień 2026)

Prace z arXiv cytuj wzorem (styl preferowany przez użytkownika):

```wiki
<ref>{{cytuj|autor=Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio|tytuł=Generative Adversarial Networks|data=2014-06-10|data dostępu=2025-06-28|czasopismo=arXiv|doi=10.48550/arXiv.1406.2661|arxiv=1406.2661}}</ref>
```

Zasady:
- `czasopismo=arXiv` (nie `opublikowany=`) — szablon renderuje to jako cytowanie czasopisma z linkiem do arXiv
- `doi=10.48550/arXiv.<ID>` — oficjalny DataCite DOI każdej pracy arXiv
- `arxiv=<ID>` — goły identyfikator `NNNN.NNNNN`, bez `arXiv:` i bez `vN`
- `data=` pełna data publikacji wersji v1 (z sekcji Submission history na arxiv.org), nie sam rok
- NIE dodawaj `url=` — szablon sam generuje link `[//arxiv.org/abs/<ID> <ID>]`
- NIE używaj pola `eprint=` — pl.wiki `{{cytuj}}` go nie rozpoznaje (inna składnia niż en.wiki)

### 3.2b Paper konferencyjny: `rozdział=` + `tytuł=` (zweryfikowane expandtemplates, wrzesień 2026)

pl.wiki `{{cytuj}}` NIE zna pola `tytuł publikacji=` ani `conference=` (render → „Nieznane pola”). Dla papera w_proceedingsach użyj:

```wiki
<ref>{{cytuj|autor=Yoon Kim, Alexander M. Rush|rozdział=Sequence-Level Knowledge Distillation|tytuł=Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing|data=2016-11|data dostępu=2026-09-11|wydawca=Association for Computational Linguistics|s=1317–1327|doi=10.18653/v1/D16-1139|język=en}}</ref>
```

Zasady: tytuł papera w `rozdział=`, tytuł proceedingsów w `tytuł=`, wydawca w `wydawca=`, strony w `s=`. Po każdej zmianie pól {{cytuj}} uruchom `expandtemplates` ALBO render-check — „Nieznane pola” wychodzi dopiero z serwera.

### 3.3 Definicja przed użyciem
Pierwsze użycie `ref name` MUSI mieć pełną treść. Kolejne użycia są skrócone.

```wiki
tekst<ref name="hist">{{cytuj|autor=Jan Kowalski|tytuł=...|s=302}}</ref>.
...
późniejszy tekst<ref name="hist" />.
```

**Błąd typowy przy tłumaczeniu:** użycie `<ref name="daalder" />` (skrótu) bez wcześniejszej definicji `<ref name="daalder">{{cytuj|...}}</ref>`. Skutek: komunikat „Brak tekstu w przypisie o nazwie daalder / BŁĄD PRZYPISÓW". Zawsze dodaj `name=` do pełnej definicji przy PIERWSZYM wystąpieniu, a nie do skrótu. Dotyczy też pisania nowego artykułu od zera: osadzaj pełną definicję w prozie od razu przy pierwszym użyciu; blok definicji zbierany pod `{{Przypisy}}` i tak trzeba będzie skryptowo roznieść po pierwszych użyciach.

### 3.4 Pozycja względem interpunkcji
`<ref>` idzie PRZED kropką i przecinkiem:
- Poprawnie: `tekst<ref name="x" />.`
- Niepoprawnie: `tekst.<ref name="x" />`
- **Mechaniczny kontrol przy zleceniu „popraw interpunkcję i przypisy”:** skanuj plik regexem `</ref>([.,;:!?])` — łapie zdublowaną interpunkcję STOJĄCĄ PO przypisie. Uwaga na częsty fałszywy układ: przypis grupy `uwaga` kończy się kropką w swojej treści („…Tyrolem.</ref>”), a po nim stoi jeszcze kropka przed kolejnym refem — kropka należy do treści przypisu, duplikat za `</ref>` usuń. Skanuj też ` ([.,;:!?])<ref` (spacja+interpunkcja przed refem). Zwracaj numer linii i kontekst, nie poprawiaj „w głowie”.

### 3.5 Powtórzenia
- `<ref name="x" />` – poprawnie
- `{{r}}` bez argumentu – zdeprecjonowany; `{{r|nazwa}}` działa, ale każdy `{{r|nazwa}}` wymaga definicji `<ref name="nazwa">…</ref>` w pliku. Dopisując kolejne użycie istniejącego, bezimiennego przypisu, najpierw nadaj mu `name=` przy pierwszej definicji — inaczej render serwera zwróci „Brak tekstu w przypisie" (wykrywalne dopiero w verify script, nie w lokalnych grepach).

### 3.6 Sekcja przypisów
`{{Przypisy}}` – NIE `<references>`. Normalizując stary artykuł, w którym definicje refów stoją wewnątrz `<references>`, przenieś pełną definicję do pierwszego użycia w prozie (kolejne użycia to skróty `<ref name="x" />`), a tag zamień na `{{Przypisy}}`.

### 3.7 Równoważenie źródeł
Jedno źródło maks. 4–5 przypisów. Rozkładaj tezy na różne, niezależne źródła.

### 3.8 Weryfikacja URL-i
Każdy `url=` sprawdź przez web_fetch. Jeśli 404 lub timeout, usuń pole `url=` i zostaw sam opis bibliograficzny.

### 3.9 Odsyłacz {{odn}}
`{{odn|Nazwisko|Rok|s=88}}` w tekście wymaga kotwicy `{{odn/id|Nazwisko|Rok}}` na początku pozycji w Bibliografii — bez niej odsyłacz nie dowiąże się do pozycji („refs missing-definition" w verify).

## Grafiki z Commons

- Sprawdź dokładną pisownię nazw plików (wielkość liter ma znaczenie)
- Format: `[[Plik:Nazwa_pliku.jpg|mały|Opis]]`
- Dla grafik w infoboxie: pole `grafika = Nazwa_pliku.jpg`

### Przepis wyszukiwania przez API (sprawdzone, październik 2026)

- **Wyszukiwanie:** `action=query&list=search&srsearch=<hasła>&srnamespace=6&format=json` — zwraca pliki. `generator=search` + `gsrsearch:f=filetype:bitmap` zwraca PUSTE wyniki (przestań używać, nie szukaj dalej tej ścieżki).
- **Wymiary/URL-e:** `action=query&titles=File:A.jpg|File:B.png|...&prop=imageinfo&iiprop=url|size` (wiele plików w jednym wywołaniu).
- **Licencja — MUSISZ ją potwierdzić przed podlinkowaniem:** `prop=imageinfo&iiprop=extmetadata&iiextmetadatafilter=LicenseShortName|Artist`, albo pewniej: przeczytaj wikitext pliku (`prop=revisions&rvprop=content`) — nagłówek `{{self|cc-by-sa-3.0}}` / `{{Information}}` jest miarodajny. Wolne licencje (CC BY/BY-SA/GFDL/PD) — tak; licencja niejaszna lub niesprawdzona — nie podlinkowuj.
- **Treść pliku vs nazwa:** przed użyciem przeczytaj `Description` z extmetadata lub wikitext — obraz o trafnej nazwie może przedstawiać inny obiekt niż potrzeba (np. "gigafactory" trafia na fabryki Tesli).
- **Rate limiting:** Commons API zwraca 429 przy szybkich kolejnych wywołaniach — sleep 5–8 s między wywołaniami i retry na 429.
- **Kategoria Commons bieżącego wydarzenia często nie istnieje** (świeże newsy) — zanim wstawisz `|commons=` w infoboxie lub `{{Commons}}`, sprawdź `Category:...` przez Commons API (`action=query&titles=Category:...`); brak kategorii = pomijaj, zamiast tworzyć czerwoną kategorię.

## Linki wewnętrzne

- Format: `[[Nazwa artykułu]]` lub `[[Nazwa artykułu|tekst wyświetlany]]`
- Linkuj pierwsze wystąpienie terminu w artykule
- Dla haseł nieistniejących na pl.wiki: nie linkuj ich w ogóle (zostaw jako zwykły tekst) lub użyj `{{link-interwiki|Hasło|Q=Qxxxxx|tekst=wyświetlany tekst}}` jeśli temat jest istotny.
- **NIGDY nie zostawiaj czerwonych linków** do nieistniejących artykułów przy tłumaczeniu z en.wiki. Sprawdź każde hasło przed dodaniem linku – albo link prowadzi do istniejącego artykułu, albo go usuwamy.
- Przed publikacją sprawdź wylinkowane strony: `curl -sL -o /dev/null -w '%{http_code}' 'https://pl.wikipedia.org/wiki/Nazwa_hasla'`. HTTP 200 = istnieje. HTTP 404 = nie ma → usuń link.
- Hasła o organizacjach/instytucjach USA bywają na pl.wiki pod tytułami ANGIELSKIMI (`[[United States Strategic Command]]`, `[[National Reconnaissance Office]]`, `[[United States Air Force]]`) obok polskich (`[[Wojna w Zatoce Perskiej]]`). W batch-checku dawaj oba warianty (polski i oryginalny) każdego tytułu — sam polski check daje fałszywe MISSING i prowadzi do usuwania żywych linków.
- **Weryfikacja wsadowa (szybsza):** `action=query&format=json&formatversion=2&redirects=1&titles=A|B|C` — istnienie wraca w polach `pages` (formatversion=2: lista, nie słownik), brakujące mają `missing`. Partuj po ~20 tytułów na wywołanie: pojedyncze wywołanie z kilkudziesięcioma tytułami (zwłaszcza po percent-encoding polskich znaków) potrafi cicho zwrócić błąd zamiast JSON-a. Zawsze z `redirects=1`: cel istniejący pod redirectem o odmiennej nazwie wypadnie wtedy OK, a `[[redirect|etykieta]]` jest poprawnym linkiem; bez tego parametru fałszywie odrzucisz żywy link i usuniesz go. Wywołania API rób przez `curl` z nagłówkiem User-Agent (np. `WikiTask/1.0 (kontakt: local)`) — goły `urllib.request` dostaje 403. Zanim usuniesz termin jako nieistniejące hasło, sprawdź polską nazwę konwencjonalną/egzonim: artykuł bywa pod nią ([[Hakata]] = Deutscher Ostmarkenverein), a pod oryginałem niemieckim (`Ostmarkenverein`) go brak.
- **NIE czytaj wyników batch-checku "na oko".** W ad-hoc wydruku `p.get('missing','OK')` brakujące hasło drukuje się jako `True` (wartość bool), a istniejące jako `OK` — realna wpadka (10.2026, Dwustopniowy przepływ informacji): odczytano `Komunikowanie masowe -> True` jako "istnieje" i wstawiono czerwone linki; wyłapał dopiero render-check. Drukuj jednoznaczne etykiety (`'MISSING' if p.get('missing') else 'EXISTS'`) i po każdej insertcji linków uruchamiaj verify script.
- **Batch-check: porównuj z normalizacją wielkości liter.** API zwraca tytuł w postaci kanonicznej (pierwsza litera wielka), a link w tekście bywa zapisany z małej ([[piechota]], [[zimna wojna]]) — proste porównanie stringów daje fałszywe MISSING i ryzyko skasowania żywego linku (10.2026, Robot wojskowy: 7 false-missing). Kluczuj mapę wyników lowercase-em albo normalizuj przez `query.normalized`.

### Pułapki szablonu `{{link-interwiki}}`

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

6. **Przy aktualizacji istniejącego artykułu audytuj ZASTANE QID-y.** Wcześniejsi edytorzy też zgadywali QID-y — przy touchaniu artykułu wypisz wszystkie `Q=` w pliku i zweryfikuj każdą encję przez sitelinki: `action=wbgetentities&ids=Q...|Q...&format=json` (wraca `sitelinks`; encja bez sitelinków = podejrzana). Realny błąd zastany: `Q134895337` opisywał booster rakietowy, nie superkomputer (`Q141613074`, ma enwiki) — link-interwiki wskazywał złe hasło. Nie lecz złego QID-u przez dodanie drugiego linku — popraw istniejący.

## Pola `{{Cytuj}}` — znane pułapki (wykrywalne tylko przez verify script)
- `{{Cytuj}}` **nie ma** pola `autor2` — użyj `autor=` (wielu po przecinku) lub `autorzy=`; `autor2` przechodzi lokalnie, ale serwerowy render zwraca `Nieznane pola`, dlatego KAŻDA zmiana przypisu wymaga ponownego verify scriptu.
- Poprawne pola: `autor`, `autorzy`, `tytuł`, `opublikowany`, `data`, `url`, `dostęp`, `język`, `cytat`.
- Usuwanie `{{Link-i|en|...}}` (brak tego szablonu na pl.wiki) zamieniaj na gładki opis w tekście, NIE na zagnieżdżony nawias `(... (ang. ...))` — podwójny nawias też jest wadą, choć niewidoczną dla parsera.


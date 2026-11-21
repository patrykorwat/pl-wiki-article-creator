# Linki wewnętrzne, {{link-interwiki}} i grafiki z Commons

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
## URL hygiene
- Polskie znaki (ł, ś, ć, ż, ą, ę, ó, ń) w URL – koduj (procent) albo zamień na ASCII; sprawdzaj, czy URL z polskimi znakami resolve'uje się.
- Backslash-escaped cudzysłowy (`\\\"`) w wikitekście = sygnał copy-paste z API; zamień na polskie „...”.
## Linki i kontrola refów — dopiski

- **Redirect „OK” w batch-checku to nie jeszcze właściwy temat.** Zanim wstawisz link do żywego artykułu, potwierdź, że artykuł-cel opisuje tę samą osobę/rzecz: nazwiska bywają homonimami („Dmitri Markov” na pl.wiki to lekkoatleta, nie poseł do Rady Państwa). Odczyt celu: `index.php?title=X&action=raw` — pewniejszy niż `prop=extracts`, który potrafi zwrócić pusty ekstrakt. Gdy hasła nie ma w żadnej Wikipedii — tekst goły, bez wymyślania linku.
- **Po wstawieniu sekcji do żywego hasła domknij linkowanie pierwszych wystąpień.** Termin użyty w nowej sekcji bywa polinkowany dopiero w zastanej prozie niżej; wstaw link przy pierwszym wystąpieniu w pliku (piped przy odmienionej formie), cudzego linku niżej nie przenoś.
- **Parser refów w samokontroli musi obejmować obie formy nazwy.** Niecytowana (`name=Hawk`) i cytowana (`name="Hawk"`); wzorzec liczony wyłącznie pod cudzysłów wciąga sąsiedni tekst jako „nazwę” i produkuje bzdurne fałszywe alarmy. Sprawdzony wzorzec: `<ref name=(?:"([^"]+)"|'([^']+)'|(\w+))\s*(/?)>` (czwarta grupa niepusta = skrót).

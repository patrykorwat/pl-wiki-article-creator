# Lista kontrolna — przed publikacją

- [ ] Interwiki: termin bez polskiego hasła → `{{link-interwiki|termin|Q=QID|tekst=...}}` z QID zweryfikowanym przez en.wiki `prop=pageprops` (wikibase_item) + kontrola `wbgetentities` (label + sitelinki); brak QID = zwykły tekst (verified > guessed > plain); nigdy surowy `[[:xx:]]`, nigdy parametr `en=`, zero czerwonych linków. Jeśli pl-hasło istnieje (np. [[Sandworm]]) — zwykły link, nie interwiki.

- [ ] Temat jest encyklopedyczny (ma znaczenie poza lokalnym)
- [ ] Dostępne są co najmniej 2 źródła niezależne
- [ ] Infobox dopasowany do typu hasła i wypełniony
- [ ] Każde zdanie z twierdzeniem merytorycznym ma przypis (nie tylko akapit)
- [ ] Żaden przypis nie jest pusty (`<ref name="x" />` bez treści)
- [ ] Każdy nazwany przypis (`name="x"`) ma pełną definicję przy pierwszym użyciu
- [ ] Każdy przypis to szablon `{{cytuj}}` (preferencja użytkownika 2026-10-31; pola wyłącznie z tabeli 3.2 w `references/przypisy-cytowanie.md`, bez `strony=`/`rok=`/„i inni”)
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
- [ ] Przy adaptacji z innej Wikipedii: każde przetłumaczone zdanie ma oparcie w przypisie — zdania niescytowane w oryginale rozłożone na tezy atomowe z własnymi źródłami lub usunięte
- [ ] Myślnik w leadzie – tylko w definicji `'''Termin''' – definicja`
- [ ] Brak myślników łączących zdania w tekście głównym (zastąpione kropką lub przecinkiem)
- [ ] Brak średników (;) w tekście głównym – zdania łączone kropką lub spójnikiem (sprawdź przez `grep -n ";" plik.wiki`)
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


## Dodatkowe kontrole (scalone z dawnego checklist.md)

- [ ] ISBN książek zweryfikowany (cyfra kontrolna; Open Library / WorldCat).
- [ ] Daty pochodzą ze źródeł pierwotnych; nie stosuj dat „około” i „prawdopodobnie” — szukaj dokładnej daty.
- [ ] Render-check wykonany: `python3 scripts/verify_pl_wiki_article.py <Plik>.wiki` + batch-check linków (patrz workflow.md).

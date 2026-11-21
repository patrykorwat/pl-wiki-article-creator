# Mapowanie tytułów pl.wiki i QID-y (weryfikacja 2026-11-15, audytowane skryptem audit_file.py)

## Zasady
- Linki do pl.wiki weryfikuj API `action=query&titles=...&redirects=1` (UA: Mozilla/5.0, batchy ≤40 tytułów); urllib bez UA → HTTP 403.
- REDIR w odpowiedzi = linkuj TYTUŁ ŹRÓDŁOWY (redirect jest OK) albo od razu kanoniczny; wpisuj wyniki tutaj.
- Brak artykułu → `{{link-interwiki|Tytuł EN|Q=Qxxxxx|tekst=...}}`. Każdy QID weryfikuj etykietą (wbgetentities props=labels) PRZED użyciem; QID bez etykiety = martwy (przykład: Q16936001 dla Dorgerloha — zły; poprawny Q1587400).
- QID-y po tytułach en.wiki: `wbgetentities&sites=enwiki&titles=A|B|C` (redirecty zwracają -1); ratunek przy 429: wbsearchentities + sleep 2s.
- Obrazy z lustra markdown: Commons sprawdza się z prefiksem `File:`, en.wiki z `File:` na en.wikipedia.org; prefiks `Plik:` działa tylko na pl.wiki.

## Kanoniczne tytuły PL (częste pułapki, tematyka niemiecka/II WŚ)
- Zagłada Żydów (REDIR z „Holokaust”); Nazizm (z „narodowy socjalizm”); Literatura niemieckojęzyczna (z „literatura niemiecka”); Republika Federalna Niemiec (1949–1990) (z „Niemcy Zachodnie”); Proletariat (z „klasa robotnicza”); Kolonie niemieckie (z „Niemieckie imperium kolonialne”); Partia Narodowa (Południowa Afryka); Theodor Adorno (nie „Teodor”); Joachim II Hektor; Ruch oporu w III Rzeszy; Okupacja aliancka Niemiec; Dachau (KL), Buchenwald (KL), Bergen-Belsen, Flossenbürg; Einsatz Reinhardt (z „Akcja Reinhardt”); Pomnik Pomordowanych Żydów Europy (NIE „zamordowanych”); Atak atomowy na Hiroszimę i Nagasaki; Museumsinsel (stacja metra); Prusy (państwo).
- Uwaga: „Berliner Schloss” istnieje na pl.wiki jako „Zamek w Berlinie” — szukając artykułów testuj różne rzeczowniki (zamek/pałac/gmach), nie tylko dosłowne tłumaczenie. Konwencja pl.wiki: przypisy PRZED znakami interpunkcyjnymi (`tekst<ref/>.,`), nie po (jak en.wiki). Brak na pl.wiki (→ link-interwiki lub tekst): Muzeum Etnologiczne w Berlinie, Muzeum Sztuki Azjatyckiej, Państwowe Muzea Berlińskie, Wilhelm von Bode, Fryderyk I (król w Prusach), Fryderyk Wilhelm (elektor brandenburski), Pandemia COVID-19 w Niemczech, proweniencja, wolność artystyczna.

## QID-y zweryfikowane etykietą
Q170119 Berlin Palace; Q20196262 Humboldt Forum; Q688353 Ethnological Museum Berlin; Q13455339 Franco Stella; Q19276262 Bénédicte Savoy; Q111643 Horst Bredekamp; Q74348 Hubertus Knabe; Q1587400 Hartmut Dorgerloh; Q1980221 Neuer Marstall; Q2301234 Sonderzug nach Pankow; Q989760 Danzig Trilogy; Q697929 Historikerstreit; Q704946 Sonderweg; Q55089343 Stunde Null; Q28221984 Austria victim theory; Q99959001 street name controversy; Q845562 transitional justice; Q24590226 TJ Institute; Q973290 myth of the clean Wehrmacht; Q5976230 I Apologize; Q96616976 Pact of Forgetting; Q16650756 war guilt question; Q4822729 Auschwitz bombing debate; Q6983411 Nazi foreign policy debate; Q4949098 Bottom-Up Approach of the Holocaust; Q1204745 Deutscher Evangelischer Kirchentag; Q315469 Katholikentag; Q679615 Vergangenheitsbewältigung.

## audit_file.py (audyt draftów .wiki)
- 2026-11-15: naprawiony `exist()` — batching po 40 + nagłówek UA + obsługa API ERROR (wcześniej KeyError: query przy >50 tytułach).
- Fałszywe alarmy: „zdefiniowane nieużyte” (łapie tylko samozamykające `<ref name="X"/>`; pełna definicja inline jest użyciem); dywisy „ – ” i cudzysłowy `"` wewnątrz atrybutów refów i tytułów cytowań.
- Prawdziwe sygnały: czerwone linki, średniki poza szablonami, `\w – \w+` w prozie, angielskie cudzysłowy w prozie, anglojęzyczne resztki.

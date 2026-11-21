# Przegląd jakościowy żywego artykułu („przejrzyj i popraw”)

Gdy użytkownik podaje URL żywego hasła z poleceniem typu „przejrzyj, popraw” bez wklejonej recenzji, zadaniem jest audyt jakości istniejącej prozy i faktów, NIE dopisywanie treści. Kolejność:

1. Pobierz wikitekst przez API do pliku kanonicznego (`action=parse&page=<Tytuł>&prop=wikitext`) i pracuj wyłącznie na nim; wklejka @url służy tylko orientacyjnie.
2. Zanim cokolwiek „naprawisz” w wklejce, sprawdź artefakty ekstrakcji: spacje po nawiasie otwierającym przy terminach w italice („( black box)”) i osamotnione słowa („ blue team”) pochodzą z ukrytych spanów renderu, nie z wikitekstu — surowy wikitekst bywa w tych miejscach poprawny.
3. Przeskanuj prozę pod kątem klas wad i popraw klasą, nie pojedynczym przykładem: zdania-monstra (>300–400 znaków z wyliczeniem wyłącznie przecinkami → rozbij na zdania tematyczne); zdania bez orzeczenia („będące kompromisem…” → „są kompromisem…”); ta sama treść w dwóch akapitach (scal przykłady w akapit definicyjny, ref zostaw przy akapicie z zachowanymi tezami); tytuł sekcji szerszy niż jej treść (sekcja tylko o jednym dokumencie nie może nosić ogólnego tytułu — precyzuj tytuł, nie dosypuj treści).
4. Zaudytuj fakty „aktualne” u źródła pierwotnego: wersje standardów przez API wydawnictwa (np. GitHub Releases), DOI przez API repozytorium (Zenodo/Crossref), format i limity egzaminów przez FAQ producenta. Liczby i wersje kopiowane między wersjami językowymi bywają po prostu przestarzałe — obecność w en.wiki nie jest weryfikacją.
5. Znormalizuj wielkość liter szablonów przypisów do {{cytuj}} (także {{Cytuj}}/{{Cytuj stronę}}), nie zmieniając pól ani name-ów.
6. Zamknij verify_pl_wiki_article.py + batch-check linków przed meldunkiem.

Przegląd nie dokłada nowych sekcji ani źródeł; dokładki tylko, gdy poprawka ich wymaga (sprostowany fakt → ref) albo do „Linków zewnętrznych” trafia zweryfikowany, stabilny URL.


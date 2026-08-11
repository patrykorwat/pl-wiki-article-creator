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

## Narzędzia
- `web_search` — znajdź źródła
- `web_fetch` — pobierz treść i zweryfikuj URL
- `web_search site:commons.wikimedia.org` — sprawdź pliki graficzne
- `web_search site:pl.wikipedia.org` — sprawdź czy artykuł/kategoria istnieje

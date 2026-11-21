# Redakcja i skracanie haseł — procedury (uzupełnienie SKILL.md)

## Skracanie z celem procentowym („skróć o X%”)
1. Zmierz prozę przed edycją: usuń `{{...}}` i `<ref...>` regexem, zsumuj znaki, wyznacz cel.
2. Ściskaj prozę: zdania złożone → zagęszczone, dane do nawiasów, duplikaty między sekcjami usuwane. Zachowaj bezwzględnie liczby, wikilinki i definicje przypisów.
3. Gdy zagęszczanie nie domyka celu — usuwaj CAŁE tezy wraz z ich przypisami (nie gołe refy). Polecenie „skróć o X%” jest decyzją użytkownika o wycięciu tez; nie pytaj ponownie, ale wycięte fakty wylicz w meldunku.
4. Zrób `cp`-backup wersji sprzed skrócenia (np. `/opt/data/cache/scratch/<hasło>_backup.wiki`) — cięcia bywają korygowane. Odpal verify script od nowa.
5. Zamelduj osobno % prozy i % całego pliku (aparat cytowań dominuje długość pliku).

## Poprawki dostarczone jako gotowy tekst całego artykułu
1. Porównaj wklejkę z żywą wersją (`difflib.unified_diff`). Liczba `<ref` i ogon pliku (navbox, kategorie) identyczne + różnice tylko w prozie = redakcja stylistyczna; przyjmuj bez ponownej weryfikacji każdego przypisu.
2. Każdą liczbę, przy której redaktor zmienił kontekst czasowy („do roku X” → „w roku X”), sprawdź u źródła pierwotnego.
3. Własna kontrola przed zapisem: wklejka potrafi gubić wikilinki (porównaj liczbę `[[` przed i po) i przywracać wady już naprawione (średniki w prozie — grep po stripie refów i szablonów).
4. Nadpisz plik i odpal verify script. Flagi „UNKNOWN (API flake, verify by hand)” przy QID-ach rozstrzygaj ręcznie przez `wbgetentities` (label + sitelinki) — to fałszywe alarmy sieciowe, nie błędy pliku.

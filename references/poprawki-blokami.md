# Poprawki do żywego artykułu w obcej wersji językowej — bloki do wklejenia

Gdy zadanie brzmi „popraw tę stronę na en.wiki, potem zrób pl” (lub odwrotnie),
nie oddawaj całego przepisanego wikitextu — żywe hasło edytuje się sekcjami.

## Kształt dostawy

- Bloki operacyjne: **USUŃ / ZNAJDŹ / WSTAW po** z dokładnym tekstem do wyszukania.
  Każdy blok musi dać się wykonać przez jedną unikalną podmianę (assert count==1
  na starym tekście, zanim cokolwiek podmienisz).
- Każdy nowy ref z pełnym szablonem cytowania i zweryfikowanym (otwartym) URL-em.
- Nazwa pliku szkicu mówi, co to jest: `<hasło>-poprawiony-szkic.wiki` dla pełnego
  poprawionego tekstu, `<cel>-patch.wiki` dla samych bloków.

## Weryfikacja przed oddaniem

- Bilans refów programowo: liczba otwarcia `<ref...>` (po odjęciu samozamykających
  `<ref ... />`) == liczba `</ref>`. Niezbalansowany licznik = wklejenie wywali parsowanie.
- Skróty `<ref name="x" />` bez pełnej definicji w tym samym pliku = błąd; definicja
  idzie przy pierwszym użyciu w pliku.
- Szablon cytowania sprawdź pod docelową wiki: {{cytuj}} istnieje i na pl i na en
  (jako cite web), ale pola się różnią — nie przenoś 1:1; na en użyj `|publisher=`,
  na pl `|opublikowany=`.
- Nowy artykuł na drugiej wersji językowej pisz dopiero PO checku API, że hasło
  nie istnieje w ŻADNEJ naturalnej formie tytułu (przekład, warianty z/po myślnika,
  forma skrócona i rozwinięta). Brak hasła pod jednym wariantem nie znaczy brak hasła.
- Staleness artykułu sprawdź przez `prop=revisions&rvprop=timestamp` + `prop=info`
  (touched) — decyduje, czy robisz aktualizację, czy tylko wstawki.

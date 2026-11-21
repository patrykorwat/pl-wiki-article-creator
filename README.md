# pl-wiki-article-creator

Skill do Hermesa do tworzenia, edytowania i formatowania artykułów na polskiej Wikipedii (pl.wiki).

## Co robi

Pokrywa cały cykl pracy nad artykułem:
- dobór i wypełnienie **infoboxów** (`{{Przedsiębiorstwo infobox}}`, `{{Instytucja infobox}}`, `{{Akt prawny infobox}}`, `{{Biogram infobox}}` itd.) — z listą poprawnych pól i pułapek „Nieznane pola"
- formatowanie **przypisów** wyłącznie uniwersalnym `{{cytuj}}` (`s=`, `data=`, `autor=`) zamiast `{{cytuj książkę}}`/`{{cytuj stronę}}`
- **polska typografia** (cudzysłowy „...", en-dash, naturalny szyk, unikanie kalk)
- **NPOV** i higiena źródeł (weryfikacja przed dodaniem przypisu, protokół źródłowy)
- `{{link-interwiki}}` — weryfikacja QID (parametr `Q=`, nigdy `en=`), sprawdzanie że identyfikator wskazuje właściwą encję
- kategorie — dopiero istniejące na pl.wiki
- lista kontrolna przed publikacją

## Struktura

Od v1.6.0 SKILL.md jest kompaktowym routerem (zasady nadrzędne + indeks), a szczegółowa dokumentacja leży w plikach referencyjnych:

```
SKILL.md         # zasady nadrzędne, routing po zadaniu, pełny indeks
references/      # 42 pliki szczegółowe: workflow i typy zadań, adaptacja/tłumaczenia,
                 # przypisy i źródła, infoboksy i szablony, język i NPOV,
                 # kontrola jakości, linki/Wikidaty/grafiki
scripts/         # verify_pl_wiki_article.py (render serwerowy + czerwone linki),
                 # verify_render.py (weryfikacja pliku .wiki przed publikacją)
```

## Zasady kluczowe

- **NIGDY nie edytuj Wikipedii przez przeglądarkę/API** — przygotowuj treść w pliku w katalogu `wiki/`, zostaw użytkownikowi do ręcznego zapisania
- **`{{cytuj}}` z małej litery**, pola `s=`, `data=` (nie `strony=`, `rok=`)
- **`{{link-interwiki}}`** używa `Q=`; każdy QID zweryfikuj w Wikidanych (łatwo halucynuję)
- kategorie TYLKO te, które istnieją na pl.wiki
- każde zdanie merytoryczne = własny przypis inline

## Licencja

MIT — patrz [LICENSE](LICENSE).

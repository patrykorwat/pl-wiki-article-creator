# pl-wiki-article-creator

Skill dla Hermes Agent do tworzenia, edytowania i formatowania artykułów na **polskiej Wikipedii (pl.wiki)**.

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

```
SKILL.md                                  # instrukcja główna
references/                               # wytyczne szczegółowe
  checklist.md
  citation-guidelines.md
  template-existence.md
  przedsiebiorstwo-infobox.md
  source-verification.md
  source-verification-case-study.md
  section-rewriting-case-study.md
  wikidata-description.md
  workflow.md
assets/
  wiki-checklist.txt
```

## Zasady kluczowe

- **NIGDY nie edytuj Wikipedii przez przeglądarkę/API** — przygotowuj treść w pliku w katalogu `wiki/`, zostaw użytkownikowi do ręcznego zapisania
- **`{{cytuj}}` z małej litery**, pola `s=`, `data=` (nie `strony=`, `rok=`)
- **`{{link-interwiki}}`** używa `Q=`; każdy QID zweryfikuj w Wikidanych (łatwo halucynuję)
- kategorie TYLKO te, które istnieją na pl.wiki
- każde zdanie merytoryczne = własny przypis inline

## Licencja

MIT — patrz [LICENSE](LICENSE).

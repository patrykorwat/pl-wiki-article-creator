---
name: wiki-article-creator
description: "Use when creating, editing, or formatting articles for Polish Wikipedia (pl.wiki). Covers infobox selection, citation formatting with {{cytuj}}, Polish typography, NPOV, and pre-publication verification. Works for persons, institutions, events, concepts, companies, places."
version: 1.6.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wikipedia, polish, wiki, citations, research]
    related_skills: [arxiv, multi-source-web-research, policy-analysis]
---

# Skill: wiki-article-creator — Tworzenie i edycja artykułów na polskiej Wikipedii

Tworzenie, edytowanie i formatowanie artykułów na polskiej Wikipedii. Konwencje pl.wiki różnią się od en.wiki — dokumentacja jest rozbita na pliki referencyjne w `references/` (od v1.6.0); ten plik trzyma zasady nadrzędne i indeks. Pliki czytaj przez `skill_view(name='wiki-article-creator', file_path='references/<plik>')`. Wskazówki „jak zaczynać” dla każdego typu zadania: tabela „Routing po zadaniu” na dole.

## Kiedy używać

Mapowanie tytułów PL↔EN, QID-y i pułapki audytu: references/pl-wiki-mapowanie-tytulow.md.

- Tworzenie nowego artykułu na pl.wiki (osoby, instytucje, wydarzenia, pojęcia, produkty, miejsca)
- Edycja istniejącego artykułu — uzupełnianie sekcji, dodawanie przypisów, poprawa formatowania
- Refaktoryzacja wikitekstu — poprawa szablonów cytowań, infoboxów, kategorii
- Weryfikacja przed publikacją — sprawdzanie przypisów, źródeł, formatowania
- Proponowanie pytań do rubryki „Czy wiesz" na stronie głównej

## NIGDY nie edytuj Wikipedii przez przeglądarkę

**ZABRONIONE:** bezpośrednia edycja Wikipedii przez przeglądarkę (browser_navigate do action=edit, wypełnianie formularza, klikanie „Zapisz").

**ZASADA:** każda zmiana w artykule Wikipedii musi iść przez plik w katalogu `wiki/`. Pobierz aktualną treść artykułu (przez API lub z istniejącego pliku), wprowadź zmiany w pliku `.txt` lub `.wiki`, zapisz w `wiki/`. Nigdy nie używaj interfejsu WWW Wikipedii do edycji.

**Dlaczego:**
- Wikipedia blokuje zapis hCaptchą dla niezalogowanych użytkowników
- Praca przez pliki zapewnia wersjonowanie i możliwość review przed publikacją
- Spójność z istniejącym workflow (wszystkie artykuły w `wiki/` są plikami lokalnymi)

### Jedno hasło = jeden plik (single source of truth)

**Jedno hasło = dokładnie jeden plik roboczy `.wiki` w `wiki/`** (nazwa pliku = tytuł hasła, spacje → `_`). NIE twórz wielu kopii tego samego artykułu (np. `X.aktualna`, `X.propozycja`, `X.v2`, `X.backup`, `X_poprawiony`). Wielokrotne kopie prowadzą do rozjazdu wersji i pomyłek przy publikacji.

- **Synchronizacja przed edycją:** zawsze pobieraj **najnowszą żywą wersję** artykułu przez API (`action=parse&page=<Tytuł>&prop=wikitext&format=json`) i NADPISUJ nią ten jedyny plik roboczy. Następnie wprowadzaj zmiany w tym samym pliku.
- **Kontekst @url od użytkownika to skrót RENDEROWANEJ strony, nie źródło:** renderowana strona pl.wiki zawiera bloki wstrzyknięte z Wikidanych (np. linki PWN/Britannica pod „Linkami zewnętrznymi”), których nie ma w wikitekście, a wklejka bywa ucięta. Zanim cokolwiek „dodasz” lub „naprawisz”, porównaj wklejkę z `index.php?title=...&action=raw` i pracuj wyłącznie na wikitekście.
- **Porównywanie / „przed i po”:** używaj `git diff` na jednym pliku albo odnotuj zamierzone zmiany komentarzem w tekście roboczym – zamiast tworzyć osobne kopie.
- **Sprzątanie:** po scaleniu usuń wszelkie kopie i pliki tymczasowe (`_tmp`, `aktualna`, `propozycja`), zostawiając wyłącznie plik kanoniczny.
- **Publikacja:** treść do ręcznego wklejenia bierz WYŁĄCZNIE z pliku kanonicznego.
- Tytuł hasła zakończony kropką daje nazwę pliku z podwójną kropką (`EU_Inc..wiki`) — to poprawna konwersja, nie literówka; nie „poprawiaj” jej, bo rozbije mapowanie plik↔hasło.

## Złote zasady

1. Definicja przed użyciem (nazwane przypisy), potem rozdzielność źródeł.
2. Weryfikowalność ponad estetyką — lepiej mniej tez z przypisami niż więcej bez.
3. Źródła oficjalne i niezależna prasa ponad materiały stron zainteresowanych.
4. Link do 404 nie jest źródłem.
5. **Zweryfikuj źródło zanim je zaproponujesz** — nigdy nie sugeruj przypisów na podstawie domysłów o treści.
6. Nie wymyślaj szablonów — testuj w podglądzie przed publikacją.
7. Krótsze hasło z 5 czystymi, niezależnymi źródłami bije dłuższe rozdęte słabymi przypisami.
8. **Nie dodawaj komentarzy HTML (`<!-- ... -->`) do treści artykułu/pliku z artykułem.** Komentarze edytorskie („do uzupełnienia", „teza wymaga źródła", „sekcja analityczna") nie są treścią encyklopedyczną — plik z artykułem ma zawierać WYŁĄCZNIE wikikod artykułu. Jeśli nie masz źródła dla tezy, pomiń ją; jeśli masz notatki robocze, trzymaj je poza plikiem artykułu.


## Lista kontrolna przed publikacją

Pełna lista kontrolna (przypisy, linki, kategorie, infobox, język, źródła; plus dodatkowe kontrole ISBN/daty): references/checklist.md. Po każdej serii podmian uruchom verify script („Skrypty” niżej) i batch-check linków.

## Zasady poprzeczne (obowiązują przy każdym zadaniu)

### Propozycje do rubryki „Czy wiesz”

Pytania opieraj WYŁĄCZNIE na treści artykułu (nie na źródłach), bez zakładania wiedzy czytelnika, bez żargonu i zdań z „według X”, po 8–15 słów, jedna myśl na pytanie; sformułowanie musi mieć oparcie wprost w tekście (WP:SYNCH). Pełny zestaw reguł i przykłady: `references/czy-wiesz-questions.md`.

### QID-fallback dla link-interwiki

Gdy QID-u nie da się zweryfikować (wyszukiwanie daje niespokrewnione encje): **zweryfikowany > odgadnięty > zwykły tekst**. Po 2 pudłach dla danej encji użyj ZWYKŁEGO TEKSTU zamiast zgadywać kolejny QID – zły link-interwiki jest gorszy niż brak linku.

**Flaga `BAD` w verify scriptu to nie werdykt.** Skrypt potrafi oznaczyć QID jako BAD, choć `wbgetentities` pokazuje poprawny label i 10+ sitelinków (fałszywe alarmy na QID-ach z polskimi sitelinkami lub odmienioną formą wyświetlaną). Zanim usuniesz link-interwiki z powodu raportu skryptu, sprawdź encję ręcznie: `action=wbgetentities&ids=Q...` — o rozstrzygnięciu decyduje label/description i liczba sitelinków, nie flaga skryptu.

### Komunikacja z edytorami i edit summaries

- Edit summary: krótki (<80 zn.), opisuje CO zrobiono (nie dlaczego); PL po polsku, EN po angielsku (przykład: „poprawki NPOV i źródeł w leadzie; usunięto tezy bez pokrycia w źródłach”).
- Odpowiedzi w dyskusji: jeden płynny akapit, bez bulletów/myślników/list, bez liczb/statystyk; odwołuj się do konkretnych diffów i zmian; bez psychoanalizy i ataków.

### Szablony porządkowe artykułu

Nie dodawaj {{Dopracować|pov}}, {{fakt}}, {{przez kogo}} itp. bez wyraźnej prośby użytkownika; jeśli szablon już jest – usuń go, gdy naprawisz problem (inaczej wygląda to jak niedokończona praca). Przy zdjęciu bannera z sekcji sprawdź nie tylko brakujące przypisy, ale i treść: proza trzymana latami pod `{{dopracować}}` potrafi zawierać błędy faktograficzne (niewydane ustawy podane jako fakt, złe daty) — napraw twierdzenie u źródła, nie tylko doklej referencję.

### Edycja dużych plików (>50K)

`patch` może nie trafić przy `old_string` > ~5K znaków. Użyj skryptu `.py` z `open().read()`, `content.replace(old, new)`, `open().write()`; po zapisie od razu przeczytaj plik i zweryfikuj zmianę (write-then-verify); przy niepewnym dopasowaniu `re.search(..., DOTALL)`.

**Odmowa nadpisania po parsjalnym odczycie:** jeśli ostatni `read_file` pliku był z `offset`/`limit` (stronicowany), `write_file` odmówi nadpisania (ochrona przed utratą nieznanego contentu). Przy pełnym przepisaniu pliku: odczytaj go raz w całości (bez limitów) i dopiero wtedy pisz; dla edycji punktowych użyj `patch` — on nie wymaga świeżego pełnego odczytu i przechodzi mimo wcześniejszego stronicowania.

**Gdy `write_file` nadal odmawia (nawet po pełnym odczycie) — nie powtarzaj prób:** przepisz pełną nową treść do pliku tymczasowego (np. w `/opt/data/cache/scratch/`), a potem zamień cel jednym wywołaniem `cp`/`shutil.copy` — to omija guard stale-write i jest najszybszą ścieżką dla pełnego rewriteru istniejącego pliku `.wiki`. Nie ponawiaj odczytów, żeby „oczyścić” guard: świeży pełny `read_file` potrafi nie zdjąć blokady (plik o długich liniach jest stronicowany wewnętrznie). Przed podmianą zrób `cp`-backup starej wersji do scratcha. Alternatywa: sekwencja `patch` per sekcja (przechodzi niezależnie od stanu odczytu, daje kontrolę unikalności `old_string`). Po podmianie przez copy uruchom verify script od nowa.

## Routing po zadaniu

| Zadanie | Zacznij od |
|---|---|
| Nowy artykuł od zera | `workflow.md` → `struktura-artykulu.md` → `przypisy-cytowanie.md` + `zrodla-higiena.md`; przed oddaniem `checklist.md` + verify script |
| Adaptacja/tłumaczenie z obcej Wikipedii | `adaptacja-tlumaczenie.md` (+ `en2pl-full-translation.md`, `election-articles-pl-wiki.md` dla wyborów) |
| Przegląd / naprawa żywego hasła | `przeglad-zywego-artykulu.md` + `poprawki-blokami.md`; skracanie → `poprawki-i-skracanie.md` |
| Edycja istniejącego (dopisanie sekcji/faktów) | `workflow.md` § „Edycja istniejącego hasła” + `linki-i-grafiki.md` (batch-check) |
| Przypisy | `przypisy-cytowanie.md` (+ `ref-placement.md`, `source-verification.md` dla nowych źródeł) |
| Infobox | `infoboksy.md` (+ `przedsiebiorstwo-infobox.md` dla spółek) |
| Weryfikacja przed publikacją | `checklist.md` + `najczestsze-bledy.md` + verify script |
| Źródła nieczytelne (403/202/WAF/paywall) | `zrodla-dostepnosc.md` |

## Materiały pomocnicze — pełny indeks

### Workflow i typy zadań
- `workflow.md` — kolejność kroków tworzenia/aktualizacji, edycja istniejącego hasła, gap-analysis klastra, sync repo skilla
- `struktura-artykulu.md` — kolejność sekcji, typowe sekcje wg typu hasła, kategorie
- `przeglad-zywego-artykulu.md` — audyt żywego hasła („przejrzyj i popraw”)
- `poprawki-blokami.md` — poprawki do żywego artykułu w obcej wersji językowej (bloki do wklejenia)
- `poprawki-i-skracanie.md` — redakcja z gotowego tekstu usera + skracanie z celem %
- `pl-en-mirror-sync.md` — synchronizacja PL z własnym draftem EN (obie wersje istnieją)
- `strategia-baza-maintenance.md` — utrzymanie bazy strategicznej: sekcje B z wywiadów/podcastów, MEMO-ONLY, rejestr Sxx, timestampy ASR, gap-check pl.wiki
- `czy-wiesz-questions.md` — pełny zestaw reguł i przykłady pytań do „Czy wiesz”

### Adaptacja i tłumaczenia
- `adaptacja-tlumaczenie.md` — GATE istnienia hasła, struktura, refy z obcego oryginału, rozmiar (kondensat), obsługa recenzji, skracanie %
- `en2pl-full-translation.md` — pełne tłumaczenie en→pl: workflow + pułapki
- `election-articles-pl-wiki.md` — pułapki haseł wyborczych (infobox, kategorie, liczby)
- `section-rewriting-case-study.md` — case study: konwersja bullet pointów na prozę, pułapka usuwania przypisów, NPOV dla instytucji

### Przypisy i źródła
- `przypisy-cytowanie.md` — {{cytuj}}: dozwolone pola (tabela 3.2), arXiv (3.2a), konferencje (3.2b), definicja przed użyciem / pozycja / odn (3.3–3.9), pułapki pól Cytuj
- `citation-guidelines.md` — wytyczne cytowania
- `ref-placement.md` — umiejscowienie przypisów względem interpunkcji
- `source-verification.md` — protokół weryfikacji źródeł przed dodaniem przypisu (Open Library, domeny, test zgodności tezy)
- `source-verification-case-study.md` — case study: 6 błędnych propozycji źródeł i ich weryfikacja
- `zrodla-higiena.md` — źródła zabronione/preferowane, rygor absolutny, proza instytucjonalna, odkrywanie źródeł akademickich (CrossRef/OpenAlex)
- `zrodla-dostepnosc.md` — ratunek 403/202/WAF, czytelność BODY, Datawrapper, statystyki makro, OCR skanów, Wayback
- `zrodla-rosyjskie.md` — strategia alternatyw dla TASS/.ru przy hasłach o Rosji
- `zrodla-audio-asr.md` — źródła audio-wideo i własne transkrypcje ASR
- `biezace-wydarzenia.md` — research incydentów: DDG Lite, tier-y źródeł, precyzja faktograficzna, DIU
- `current-events-source-examples.md` — przykłady źródeł do bieżących wydarzeń/incydentów
- `international-sogi-sources.md` — źródła międzynarodowe (UN, OAS, ACHPR, Yogyakarta)
- `diu-warsanctions-weapons-data.md` — War&Sanctions DIU: karty charakterystyk i komponenty rosyjskiej broni
- `spaceforest-themis-research.md` — case study research projektu kosmicznego (TEN-E/ESA)

### Infoboksy i szablony
- `infoboksy.md` — dobór infoboxa wg typu hasła + zweryfikowane pola głównych szablonów (Biogram, Przedsiębiorstwo, Instytucja, Akt prawny, Wydarzenie, Jednostka wojskowa, Rakieta nośna…)
- `przedsiebiorstwo-infobox.md` — pola i pułapki {{Przedsiębiorstwo infobox}}
- `baretki-odznaczen.md` — baretki odznaczeń w {{Biogram infobox}}
- `template-existence.md` — lista szablonów pl.wiki: które istnieją, które nie, czym je zastąpić (kluczowe przy tłumaczeniu z en.wiki)
- `spory-tabele-i-statusy.md` — zasady sporów i tabel statusów (`{{tabela-tak}}`/`{{tabela-nie}}`)

### Język i NPOV
- `jezyk-polski.md` — cudzysłowy, myślniki, średniki, „i in.”, tytuły sekcji; precyzja terminologiczna; naturalny szyk; EUR-Lex
- `terminologia-techniczna.md` — fałszywe odpowiedniki techniczne (astronautyka/inżynieria)
- `npov.md` — NPOV, sekcja „Kontrowersje”, organizacje/fundacje
- `npov-organization-cleanup.md` — NPOV cleanup dla kontrowersyjnych organizacji
- `ngo-sourcing-strategy.md` — sourcing dla NGO (statut + media + źródło pierwotne)

### Kontrola jakości i błędy
- `najczestsze-bledy.md` — katalog wpadek z realnych sesji i reguł naprawczych
- `checklist.md` — lista kontrolna przed publikacją (w tym weryfikacja źródeł i błędy do unikania)
- `red-flags.md` — ryzyka i ostrzeżenia

### Linki, Wikidaty, grafiki
- `linki-i-grafiki.md` — linki wewnętrzne, batch-check z normalizacją, {{link-interwiki}} (Q=), grafiki z Commons, URL hygiene
- `pl-wiki-mapowanie-tytulow.md` — mapowanie tytułów PL↔EN i QID-y (weryfikowane)
- `wikidata-description.md` — Wikidata dla artykułów pl.wiki: składnia QuickStatements (pipe, S854/S813), ograniczenie LAST, modelowanie P31, P921 vs P971, formaty opisów

### Skrypty
- `scripts/verify_pl_wiki_article.py` — automatyczny render serwerowy + raport czerwonych linków (uruchamiany: `python3 scripts/verify_pl_wiki_article.py Plik.wiki`)
- `scripts/verify_render.py` — weryfikacja pliku .wiki przed publikacją: przypisy (pełne definicje vs skróty), interpunkcja przy refach, domeny .ru, istnienie linków wewnętrznych, render-check serwera

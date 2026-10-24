# Wikidata dla artykułów pl.wiki — opisy i batche QuickStatements

Zasada nadrzędna (preferencja użytkownika): agent NIE tworzy i NIE edytuje encji Wikidanych samodzielnie — przygotowuje pliki `.qs` do odpalenia przez użytkownika w QuickStatements (https://quickstatements.toolforge.org). Wszystkie QID-y weryfikuje się przed użyciem.

## Składnia QuickStatements — składnia pipe, NIE tab+link=

**Używaj wyłącznie składni pipe-delimited z właściwościami referencyjnymi w linii:**
```
CREATE
LAST|P31|Q75880299|S854|"https://www.gov.pl/web/..."|S813|+2026-10-16T00:00:00Z/11
LAST|P17|Q36|S854|"https://..."|S813|+2026-10-16T00:00:00Z/11
pl"Program polskiej energetyki jądrowej"|S854|"https://pl.wikipedia.org/wiki/..."
en"Polish Nuclear Power Programme"|S854|"https://en.wikipedia.org/wiki/..."
LAST|Len"Program polskiej energetyki jądrowej"|Den"rządowy program wieloletni ..."
LAST|Pen"rządowy program wieloletni i dokument strategiczny ..."|Den"rządowy program wieloletni ..."
```

**Pułapka (kosztowała błąd „Attribute value is missing"):** składnia tab-delimited z parametrem `link=` przy wartości-URL (np. `P856<TAB>https://...<TAB>link=...`) psuje parser — zwraca pusty value dla P856 i całego claimu. Składnia pipe z wartością w cudzysłowie przechodzi. Dotyczy też batchy „fix" dla istniejących encji.

- Każde twierdzenie musi mieć referencję: `S854|"<url źródła tezy>"|S813|+<RRRR-MM-DD>T00:00:00Z/11` (data dostępu).
- Daty: `+2014-01-28T00:00:00Z/11` (precision 11 = dzień), `/9` = miesiąc, `/7` = wiek? nie — `/9` lat lat... precyzje: 11=dzień, 10=miesiąc, 9=rok, 6=dziesięciolecie. Dla samego roku użyj `+2036T00:00:00Z/9`.
- Sitelinki: `pl"Tytuł artykułu"|S854|...`, `en"Title"|S854|...`.
- Usunięcie claimu: `Q12345<TAB>P101<TAB>Q11660` z prefiksem `-` w składni pipe: `-Q141740609|P101|Q11660`. (W składni pipe usuwanie: `-Q...|P...|Q...`.)

## Ograniczenie LAST — spinki idą do drugiego batcha

`LAST` działa jako **podmiot** wierszy po `CREATE` w tym samym batchu, ale NIE jest rozwiązywalny jako **wartość** claimu (np. `Q12345|P361|LAST` — „elektrownia jest częścią programu" — zwraca „No last item available").

Procedura:
1. Batch 1: `CREATE` + wszystkie twierdzenia, w których encja jest podmiotem.
2. Po odpaleniu batcha użytkownik dostaje QID nowej encji w podglądzie.
3. Batch 2 (spinki, reverse-linki na sąsiednie encje): napisz z placeholderem `QNEW`, przekaż użytkownikowi do podstawienia QID-u przed odpaleniem. Nie licz, że `LAST` z batcha 1 przejdzie.

## Modelowanie klasy (P31) nowego tematu

Nie wymyślaj klasy. Znajdź istniejącą encję tego samego typu (z sitelinkami) i skopiuj jej P31, albo przeszukaj analog: `action=wbgetclaims&entity=Q...&property=P31`. Przykłady zweryfikowane: narodowy program energetyczny → Q75880299 (*energy policy by country or territory*, wzór: National Energy Policy of Nigeria); artykuł typu „X w Polsce" (aspekt kraju) → Q74817647 (*aspect of a geographic region*, wzór: Science and technology in Germany). NIE używaj całkiem nowych klas bez sitelinków (np. Q130472575 government policy) — słabo się walidują. Akceptowalny stan to też BRAK P31: gdy żadna klasa nie pasuje (np. nazwana inicjatywa finansowa bez encji-rodzica), zostaw P31 pusty z komentarzem w batchu i uzupełnij po znalezieniu klasy — lepsze puste niż zmyślone. Zweryfikowane kształty linii (przechodzą w QS): `LAST|Lpl|"..."`, `LAST|Len|"..."`, `LAST|Dpl|"..."`, `LAST|Den|"..."`, sitelink `LAST|plwiki|"Tytuł hasła"`.

## P921 czy P971

- **P921 (main subject)** — dla artykułu o pojedynczym temacie / hasza opisowego. To domyślny wybór.
- **P971 (subject of the item)** — tylko gdy encja jest podtematem złożonego, wielowątkowego artykułu. Użycie P971 dla monolitycznego tematu to błąd (korygowany w sesji).
- P921 dodawaj z referencją S854 do dokumentu definiującego temat (np. przepis UE, statut).

## Fix batchy dla istniejących encji — najpierw stan żywy

Przed napisaniem batcha „fix" (usuń X, dodaj Y) pobierz aktualne twierdzenia encji: `action=wbgetclaims&entity=Q...&format=json`. Poprzedni batch mógł zadziałać częściowo (np. P279 weszło, P101 zostało, P921 nie doszło) — pisz batch wyłącznie na różnicę między stanem żywym a zamierzonym, nigdy nie regeneruj całego fixa „na wszelki wypadek". Stare pliki `.qs` z poprzednich sesji mogą być już częściowo odpalone.

## Opisy (PL i EN)

- Krótki, rzeczownikowy fragment, 5–12 słów, z małej litery, bez kropki, bez „jest to".
- PL opis ustawiany przez `Pen"..."` w QUICKSTATEMENTS, nie ręcznie na stronie.
- Nie stawiaj opisu w wikitekście artykułu (żaden komentarz HTML nie wpływa na Wikidane).

## Weryfikacja braku encji przed CREATE

Zanim utworzysz encję, sprawdź przez `action=wbgetentities&sites=plwiki&titles=<Tytuł>&languages=pl|en|de|fr|cs&format=json`, czy artykuł ma już `wikibase_item`; dodatkowo przeszukaj Wikidata po nazwie (wbsearchentities) w kilku językach — encja mogła powstać niezależnie bez sitelinka pl.

Ta sama weryfikacja dotyczy STARYCH batchów: `.qs` leżący w workspace może być już odpalony (encja istnieje z sitelinkiem pl) albo nieaktualny wobec stanu żywego — przed każdym odpaleniem porównaj każdy CREATE-batch z `wbgetclaims`/`wbgetentities` i usuń przestarzały plik, zamiast go regenerować. Odpowiedź `wbgetentities` z `sites=`/`titles=` zwraca dla nieistniejących tytułów klucze-placeholdery (`-1`, `-Q...`) — filtruj klucze zaczynające się od `-`, inaczej pusty wynik odczytasz jako „brak encji” albo odwrotnie.

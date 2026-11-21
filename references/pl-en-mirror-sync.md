# Synchronizacja PL z własnym draftem EN (obie wersje istnieją)

Wariant: hasło na pl.wiki jest kondensatem hasła EN, którego wersję EN agent sam utrzymuje (typowy obieg: draft EN → artykuł PL → dalszy rozwój EN). Praca przebiega inaczej niż tłumaczenie od zera.

## Rozjazd wykrywaj przez API, nie przez czytanie

Pobierz PL przez `prop=revisions&rvslots=main&rvprop=content` (redirects=1) i porównaj z EN twierdzenie po twierdzeniu. Sygnał rozjazdu: `data dostępu` w refach PL starsze niż access-dates w drafcie EN — wersja PL nie zawiera faktów, które weszły później (przesunięte terminy, wycofane liczby, nowe sekcje). Refy PL z przeterminowanym „stan na” sprawdzaj pod kątem każdej zmiany, którą EN już opisał.

## Kolejność poprawek

1. **Najpierw JEDEN błąd faktograficzny.** Typowo: zmieszane terminy lub liczby po przesunięciu harmonogramu (termin A przypisany do lotu B). Znajdź zdanie, napraw z pełnym cytowaniem obu źródeł.
2. **Potem przetłumacz 1:1 brakujące elementy EN** — akapity, sekcje, refy, zachowując konwencję {{cytuj}} i konwencję nazw pl.wiki.
3. **Na końcu dołóż z bazy strategicznej materiał, którego EN nie ma** — PL może być celowo bogatszy. Nie spychaj go do pełnego lustra EN i nie wycinkuj tego, czego EN nie zawiera.

## Weryfikacja URL-i przed napisaniem bloku

Każdy nowy URL sprawdź (status + treść) PRZED napisaniem bloku, nie po. Pułapka soft-404 na gov.pl: wyszukany w wyspiarce URL podstrony zwraca 200 z generyczną powłoką (tytuł „Portal Gov.pl”, zero wystąpień szukanej frazy w body) — potwierdź wystąpienie słowa kluczowego w pobranym body, nie sam status. DCD i podobne portale zwracają 403 na curl przy żywym linku (bot-wall ≠ 404) — status z curl nie rozstrzyga, otwórz w przeglądarce albo polegnij na wcześniejszym otwarciu.

Jeśli oryginalny URL depeszy nie wypada z wyszukiwarki, cytuj ją przez czytelną lokalizację z jawnym oznaczeniem („Reuters (przez Yahoo Finance)”) zamiast zgadywać URL.

## Format dostarczenia

- Gotowe bloki „znajdź → zamień”: unikalny fragment PL jako kotwica + pełny {{cytuj}} w konwencji pl. User wkleja je do edytora bez przepisywania.
- Na życzenie: cały poprawiony szkic jako plik .wiki (pełny wikitekst gotowy do wklejenia w całość).
- Przed oddaniem pliku sprawdź programowo bilans refów: liczba `<ref` (bez self-closing) = liczba `</ref>`, brak zdublowanych definicji `name=`, sekcje w konwencjonalnej kolejności. Rozbalansowany ref w wklejce to czerwony błąd renderu i strata zaufania do całej poprawki.
- Zostaw userowi decyzje o treści, której nie da się zweryfikować (np. jednorazowe źródło o wsparciu państw trzecich) — wypunktuj na końcu jako „do Twojej decyzji”, nie usuwaj po cichu.

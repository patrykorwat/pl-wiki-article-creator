# Wytyczne cytowania (pl.wiki)

Na pl.wiki używaj wyłącznie uniwersalnego szablonu `{{cytuj}}` z małej litery.

Dobry przypis ma:
- `tytuł=`
- `opublikowany=` / `czasopismo=` / `wydawca=`
- `data=`
- `autor=` „Imię Nazwisko" (gdy znany)
- `url=` (zweryfikowany przez WebFetch)
- `archiwum=` dla stron nietrwałych
- `data dostępu=`

Pola `{{cytuj}}`: `autor` (nie `nazwisko`/`imię`), `data` (nie `rok`), `s` (nie `strony`). Kolaboracje jako `autor="Nazwa zespołu"`, bez „i in.".

## Gazety w polu `czasopismo=` → ukryta kategoria
`czasopismo = Washington Post` wyzwala kategorię „Szablon cytowania zamienił nazwę czasopisma": Moduł:Cytuj podmienia wartość, gdy pasuje do tabeli w Moduł:Cytuj/czasopisma (kategoria = `altJournal` w Moduł:Cytuj/dane — szukaj frazy kategorii tam, nie w Szablon:Cytuj, który jest 2,5-kilobajtowym wrapperem). Dla prasy używaj `opublikowany=`; `czasopismo=` zarezerwowane dla czasopism naukowych. Po naprawie potwierdź zniknięcie kategorii render-checkiem (expandtemplates całego pliku).

Źródła pierwotne tylko do faktów rutynowych. Encyklopedyczność i oceny opieraj na niezależnym, wtórnym pokryciu.

## Słabe wzorce cytowań
- strona podmiotu cytowana na dowód ważności,
- depesze i komunikaty prasowe na poparcie istotności,
- katalogi i bazy danych cytowane jako narracja,
- gołe adresy URL bez tytułu, wydawcy i daty.

## Źródła zabronione
- rejestr.io (komercyjna nakładka na KRS),
- Demagog (demagog.org.pl) i podobny fact-checking,
- blog producenta jako jedyne źródło twierdzeń o produkcie,
- Wikipedia jako źródło dla siebie.

## Reguły przypisu w tekście
- `<ref>` przed kropką i przecinkiem.
- Powtórzenia przez `<ref name="X" />`, nigdy `{{r}}`.
- Sekcja przypisów: `{{Przypisy}}`, nie `<references>`.

## Domyślnie
Krótsze hasło z 5 czystymi, niezależnymi źródłami bije dłuższe hasło rozdęte słabymi przypisami.

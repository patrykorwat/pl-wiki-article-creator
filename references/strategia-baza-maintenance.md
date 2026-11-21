# Utrzymanie bazy strategicznej (strategia-ai-europa-2026.md i podobne)

Wewnętrzna baza pod przyszłe artykuły — nie encyklopedia. Struktura: Część A (fakty: wymagane źródło pierwotne + wtórne), Część B (stanowisko autora — nie przenosić do Wikipedii), rejestr źródeł Sxx, KPI/punkty kontrolne, changelog z wersją per sesja.

## Wpinanie materiału z wywiadu/podcastu

1. Transkrybuj audio (skill `audio-transcription-cpu`); transkrypt zapisz jako `wiki/zrodla/<data>-<audycja>-<gosć>.md` z timestampami. Timestamp staje się jednostką cytowania jak strona publikacji.
2. Sekcja B-per-źródło: nowa numerowana sekcja B pod wzorem istniejących — tezy gościa + timestampy + status wiarygodności. Jedna audycja = jedna sekcja, nie rozbijaj na wiele sekcji per teza.
3. Status wiarygodności: wypowiedzi gościa są źródłem pierwotnym *samych tez*, ale twierdzenia faktograficzne o własnych projektach gościa (pozycje benchmarkowe, liczby zasobów, zainteresowanie podmiotów trzecich) to MEMO-ONLY do czasu niezależnego potwierdzenia. Cytuj tezę — nie przenoś faktu o własnym produkcie.
4. Nazwy własne z ASR: nie koryguj bez pewności. W rejestrze źródeł wypisz formy wg ASR z przypuszczalną poprawną: „X” (ASR; prawd. Y). Omyłkowa „poprawka” nazwy jest gorsza niż oznaczona forma surowa.
5. Rejestr źródeł: nowy wpis Sxx z pełną metryką (audycja, data, nadawca, gość, link audio + link strony, ścieżka transkryptu). Zasada „cytować akt, nie komunikat” działa też w stronę firm: deklaracja strony zainteresowanej ≠ fakt.
6. Changelog + data nagłówka: każda sesja dopisuje wpis zmian z numerem wersji i zakresem; data „aktualizacji” w nagłówku = data ostatniej sesji, nie data powstania.
7. Krzyżuj z istniejącymi sekcjami: konwergencja dwóch niezależnych głosów (ta sama teza u różnych ekspertów) wzmacnia istniejące KPI — w starych sekcjach odnotuj „patrz Bx.y” zamiast duplikować tezę. Napięcie między tezą bazy a głosem eksperta odnotuj w OBÓJ miejscach (raz jako odnotowane napięcie, raz jako głos).
8. Z każdej nowej sekcji B wyprowadź testowalny KPI (miernik wdrażalny), nie sam wniosek interpretacyjny.

## Pułapki

- Nie podawaj przyszłych głosowań/wyborów terminów jako faktów — artykuł/kandydatura pisana przed terminem wymaga natychmiastowej poprawki. Odnosi się to także do sugestii wiki: nie twórz hasła przed rozstrzygnięciem, jeśli nie przetrwa tygodnia.
- Nie nadpisuj sąsiednich dokumentów bazowych — edytuj tylko plik bazy.
- Kwoty i limity: gdy komunikat prasowy różni się od aktu prawnego, do cytowania bierz akt; rozbieżność flaguj w tekście bazy.

## Gap-check pl.wiki przed sugestią „czym się zająć”

Jeden batchowy call API (do 50 tytułów na raz):

```
https://pl.wikipedia.org/w/api.php?action=query&format=json&prop=info&inprop=url&redirects=1&titles=A|B|C
```

- `missing` = brak hasła; `length` + `touched` = rozmiar i świeżość istniejących (dotknięty niedawno = ktoś już pracuje, nie dubluj).
- `redirects=1` rozwiązuje przekierowania server-side — nie parsuj ich ręcznie.
- Rankuj sugestie: (a) rozbudowa żywego hasła ze zweryfikowanym materiałem — najwyższy stosunek pracy do efektu; (b) nowy artykuł na twardym, podwójnie źródłowanym materiale; (c) nowy artykuł czekający na wydarzenie — odłóż do rozstrzygnięcia; (d) biogram przy źródłach od strony zainteresowanej — WP:BAD + ryzyko COI, odłóż do niezależnego pokrycia.
- Rozróżnienia pojęciowe (np. Factory vs Gigafactory) porządkuj w istniejącym haśle-wieszaku, nie w osobnych stubach.
- Gdy PL istnieje jako kondensat hasła EN, którego wersję EN sam utrzymujesz: `references/pl-en-mirror-sync.md` (rozjazd przez API, kolejność poprawek, soft-404 na gov.pl, format dostarczenia).

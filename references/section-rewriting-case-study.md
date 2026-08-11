# Case study: przepisywanie sekcji „Zadania i działania" POLSA (lipiec 2026)

## Kontekst

Artykuł o Polskiej Agencji Kosmicznej (POLSA) na pl.wiki. Sekcja „Zadania i działania" była sformatowana jako lista bullet pointów z podsekcjami `*;` i zawierała język promocyjny („budowa kompetencji", „rozwój potencjału", „kluczowych inicjatyw", „znacznie przyspieszy", „najważniejszych imprez branżowych").

## Iteracja 1 — błąd: usunięcie przypisów

Przepisano sekcję z 19 punktów na 6 akapitów prozy. Usunięto wszystkie `<ref>` — zarówno te istniejące, jak i te, które były w oryginalnych podsekcjach.

**Skutek:** użytkownik zareagował: *"wtf - każde stwierdzenie ma mieć źródło!!!!"*

**Lekcja:** podczas zmiany formatu sekcji NIGDY nie usuwaj istniejących przypisów. Każde stwierdzenie merytoryczne wymaga własnego `<ref>` inline.

## Iteracja 2 — poprawka: dodanie przypisów

Dodano 6 unikalnych źródeł (1 ustawa + 4 podstrony POLSA) rozłożonych na 8 przypisów inline w 5 akapitach:

| Stwierdzenie | Źródło |
|---|---|
| Ustawowe zadania POLSA | `{{Dziennik Ustaw\|2020\|1957}}` (art. 3 ustawy) |
| Krajowy Program Kosmiczny | `polsa.gov.pl/o-polsa/` |
| 3 programy konsultacji, wyjazdy studyjne | `polsa.gov.pl/o-polsa/` |
| Konsorcjum SST | `polsa.gov.pl/aktywnosci/bezpieczenstwo-kosmiczne/` |
| PERASPERA, EUMETSAT | `polsa.gov.pl/aktywnosci/wspolpraca-miedzynarodowa/` |
| Studia wykonalności 5 projektów | `polsa.gov.pl/o-polsa/` |
| Współpraca z 8 agencjami, Artemis Accords | `polsa.gov.pl/aktywnosci/wspolpraca-miedzynarodowa/` |
| Działalność edukacyjna | `polsa.gov.pl/aktywnosci/promocja-i-edukacja/` |

## Iteracja 3 — poprawka: źródła wtórne zamiast pierwotnych

Po dodaniu przypisów użytkownik zwrócił uwagę: *"ale to źródło pierwotne"* – strona POLSA.gov.pl to źródło pierwotne (sama opisywana instytucja).

**Poprawka:** zastąpiono źródła pierwotne wtórnymi:
- SST: `polsa.gov.pl` → `eusst.eu` (strona UE – inna instytucja)
- EUMETSAT: `polsa.gov.pl` → `eumetsat.int` (inna organizacja)
- Artemis Accords: `polsa.gov.pl` → `nasa.gov` (inna agencja kosmiczna)
- Ustawa (Dz.U.) – pozostawiono, bo akt prawny jest standardem na Wikipedii
- Lista 8 umów bilateralnych – pozostawiono źródło pierwotne (`polsa.gov.pl`), bo użytkownik zaakceptował: *"listy intencyjne lub umowy bilateralne – weź źródło pierwotne"*

**Lekcja:** preferuj źródła wtórne (niezależne media, dokumenty innych instytucji, akty prawne). Wyjątek: lista umów/porozumień podpisanych przez instytucję – tu źródło pierwotne jest akceptowalne.

## Iteracja 4 — przywrócenie wikilinków

Przy przepisywaniu listy 8 agencji kosmicznych zastąpiono wikilinki (`[[Francuska Agencja Kosmiczna|Francuską Agencją Kosmiczną]] (CNES)`) gołym tekstem (`francuską (CNES)`). Użytkownik poprosił o przywrócenie wikilinków.

**Lekcja:** podczas zmiany formatu sekcji zachowaj wszystkie wikilinki do encji. Nie zastępuj ich gołym tekstem ani akronimami bez linków.

## Iteracja 5 — przepisanie sekcji „Historia" (polityka → kamienie milowe)

Po przepisaniu „Zadań i działań" użytkownik zwrócił uwagę na sekcję „Historia": *„ta sekcja historia, pokazuje tylko polityczne całowanie dupy"*.

**Problem:** Historia była kroniką politycznych nominacji i dymisji:
- „Banaszkiewicz został odwołany przez premier Beatę Szydło 7 października 2016, choć jego kadencja miała trwać pięć lat"
- „Grzegorz Wrochna [...] został odwołany przed końcem swej pięcioletniej kadencji; tym razem przez ministra rozwoju w rządzie Donalda Tuska, Krzysztofa Paszyka"

**Poprawka:** zastąpiono polityczną kronikę faktycznymi kamieniami milowymi:
- 2014–2015: utworzenie i rozpoczęcie działalności
- Po 2015: wejście w SST, EUMETSAT, umowy bilateralne z 8 agencjami
- 2021: Artemis Accords
- 2025: budżet 71 mln zł
- IV 2026: ustawa o działalności kosmicznej (kompetencje regulatora)
- VII 2026: IRIS², centrum ESA w Warszawie

Listę prezesów przeniesiono do sekcji „Zarządzanie/Lista prezesów".

**Lekcja:** sekcja „Historia" instytucji powinna pokazywać faktyczne wydarzenia w życiu instytucji, a nie polityczną kronikę nominacji i dymisji. Lista prezesów należy do sekcji „Zarządzanie". Unikaj fraz: „odwołany przez premiera X, choć kadencja miała trwać 5 lat" – to polityczne komentarze, nie fakty encyklopedyczne.

## Iteracja 6 — usunięcie tautologii strukturalnych

Użytkownik zareagował na opis struktury: *„te trzy piony to też jakiś absurd"*.

**Problem:** w leadzie i sekcji „Zarządzanie" napisano: *„Struktura organizacyjna POLSA obejmuje trzy piony: prezesa, wiceprezesa ds. naukowych oraz wiceprezesa ds. obronnych"*.

**Lekcja:** każda organizacja ma szefa i zastępców – opisywanie tego jako „trzech pionów" to tautologia. Zamiast tego podaj faktyczne departamenty/jednostki: *„W strukturze POLSA funkcjonują departamenty zajmujące się strategią, współpracą międzynarodową, programami kosmicznymi..."*.

## Iteracja 8 — usunięcie dublowania między sekcjami

Po przepisaniu Historii i Zadań użytkownik zwrócił uwagę: *„teraz historia trochę dubluję info w zadania i działania"*.

**Problem:** Historia i Zadania i działania zawierały te same informacje (SST, EUMETSAT, Artemis Accords, IRIS², centrum ESA, ustawa o działalności kosmicznej).

**Poprawka:** rozdzielono funkcje sekcji:
- **Historia** = chronologia (kiedy coś się wydarzyło)
- **Zadania i działania** = funkcje (co agencja robi)

Usunięto z Zadań wszystkie daty i wydarzenia historyczne. Zostały tylko opisy kompetencji: „prezes pełni funkcję regulatora" (nie „18 kwietnia 2026 weszła w życie ustawa"), „uczestniczy w SST" (nie „w 2016 Polska dołączyła do SST").

**Lekcja:** Historia i Zadania mają różne funkcje. Nie powtarzaj tych samych faktów w obu.

## Iteracja 9 — radykalne skrócenie kontrowersji (parafraza to za mało)

Po skróceniu sekcji kontrowersji (usunięciu cytatów, dodaniu adnotacji o braku stanowiska POLSA) użytkownik wskazał: *„osoba doświadczona mówi, że chuj tam robią i widać, że to z tego artykułu wynika, co nie?"*.

**Problem:** nawet po usunięciu dosłownych cytatów, szczegółowe wyliczenie zarzutów Uznańskiego („brak strategicznych kompetencji, zaniechania, naruszanie praw pracowniczych, pytania o IRIS² i KPO bez odpowiedzi, wyjęcie z kontekstu") tworzyło wrażenie, że artykuł staje po jego stronie – zwłaszcza że POLSA nie przedstawiła stanowiska. Samo zdanie „W dostępnych źródłach nie przedstawiono stanowiska POLSA" nie równoważyło trzech zdań szczegółowych zarzutów.

**Poprawka:** zredukowano zarzuty do jednego neutralnego sformułowania: „zarzucił kierownictwu POLSA błędy w zarządzaniu". Usunięto cytat z X (Twittera) astronauty – źródło pierwotne, jednostronne. Usunięto zbędne „Na doniesienia te powoływał się również X" w drugiej podsekcji.

**Lekcja:** nawet parafraza szczegółowych zarzutów tworzy stronniczość, gdy druga strona milczy. Zredukuj do absolutnego minimum – jednego neutralnego zdania. Usuń źródła pierwotne stron sporu (posty na X/Twitterze).

## Iteracja 10 — dodanie brakujących sekcji na podstawie enwiki

Użytkownik: *„popatrz na https://en.wikipedia.org/wiki/Polish_Space_Agency, przeciez byly projekty krajowych satelitow!"*.

**Problem:** polski artykuł nie zawierał sekcji o programie załogowym (misja Ignis) i satelitach krajowych (EagleEye, PIAST, Camilla), które były opisane w angielskiej wersji.

**Poprawka:** dodano sekcje „Program załogowy" i „Satelity", korzystając ze źródeł space24.pl (polskie niezależne medium branżowe). Zaktualizowano też Historię o misję Ignis i start PIAST.

**Lekcja:** przy edycji artykułu na pl.wiki warto sprawdzić en.wiki jako indeks brakujących tematów. Nie kopiuj ślepo – zweryfikuj źródła i dostosuj do konwencji pl.wiki (proza zamiast tabel, polskie źródła zamiast angielskich).

## Iteracja 11 — usunięcie 3. akapitu z leadu

Użytkownik: *„usun 3 akapit z leada, na chuj tam to"*.

**Problem:** trzeci akapit leadu zawierał szczegóły struktury organizacyjnej (departamenty), które są już w sekcji „Zarządzanie" w treści artykułu.

## Podsumowanie lekcji z tej sesji

1. **Przypisy:** najpierw przenieś wszystkie `<ref>` do nowej wersji, potem redaguj treść.
2. **Źródła:** preferuj wtórne nad pierwotne. Wyjątek: lista umów instytucji.
3. **Wikilinki:** zachowaj przy przepisywaniu.
4. **NPOV dla kontrowersji:** due weight, parafraza zamiast cytatu, fakty vs zarzuty, adnotacja o braku stanowiska drugiej strony, język encyklopedyczny.
5. **Proza:** grupuj pokrewne tematy, usuwaj frazy wartościujące, skracaj listy.
6. **Budżet w infoboxie:** dla {{Instytucja państwowa infobox}} nie dodawaj pola `budżet` – dane finansowe zmieniają się corocznie i lepiej umieścić je w sekcji „Zarządzanie" w treści.
7. **Lead wymaga przypisów:** każdy akapit w leadzie musi mieć własny przypis inline. Nie wystarczy, że treść jest rozwinięta w dalszych sekcjach.
8. **Grupa „Zarządzanie":** siedziba, oddziały, struktura organizacyjna i lista prezesów to pokrewne tematy. Zamiast osobnych sekcji, zgrupuj je w jednej sekcji „Zarządzanie".
9. **Sekcja „Kierownictwo" jest zbędna:** prezes i wiceprezes są już w infoboxie. Nie powielaj ich w osobnej sekcji.
10. **Historia = kamienie milowe, nie polityka:** sekcja „Historia" instytucji powinna pokazywać faktyczne wydarzenia (przystąpienie do konsorcjów, podpisanie umów, zmiany kompetencji), a nie polityczną kronikę nominacji i dymisji. Lista prezesów → „Zarządzanie/Lista prezesów".
11. **Opis struktury:** nie pisz „trzy piony: prezes i wiceprezesi" – to tautologia. Podaj faktyczne departamenty.
12. **Lead bez szczegółów organizacyjnych:** nie powielaj w leadzie informacji, które są rozwinięte w sekcjach poniżej.
13. **Historia i Zadania nie dublują się:** Historia = chronologia (kiedy), Zadania = funkcje (co). Nie powtarzaj tych samych faktów w obu.
14. **Kontrowersje: nawet parafraza szczegółowych zarzutów tworzy stronniczość:** zredukuj do jednego neutralnego zdania. Usuń źródła pierwotne stron sporu (posty na X/Twitterze).
15. **Sprawdź en.wiki jako indeks brakujących tematów:** angielska Wikipedia często ma sekcje, których brak w polskiej wersji. Nie kopiuj ślepo – zweryfikuj źródła i dostosuj do konwencji pl.wiki.

## Technika: bullet pointy → proza

1. **Zgrupuj pokrewne tematy** — zamiast osobnych podsekcji dla SST, PERASPERA, EUMETSAT → jeden akapit o uczestnictwie w konsorcjach.
2. **Usuń frazy wartościujące** — „budowa w Polsce kompetencji", „rozwój potencjału", „konkurencyjności na rynku", „kluczowych inicjatyw", „znacznie przyspieszy", „najważniejszych imprez", „najciekawsze inicjatywy", „przyczyni się do rozwoju".
3. **Zastąp neutralnymi opisami** — „koordynacja rozwoju", „organizuje wydarzenia", „zleciła opracowanie", „uczestniczy w", „pełni funkcję".
4. **Skróć listy** — 8 agencji kosmicznych: zamiast pełnych rozwlekłych linków (`[[Francuska Agencja Kosmiczna|Francuską Agencją Kosmiczną]]`) → akronimy w nawiasach (`francuską (CNES)`). **Uwaga:** zachowaj wikilinki, nie zastępuj ich gołym tekstem.
5. **Usuń podsekcje promocyjne** — „Promocja krajowego sektora kosmicznego" to czysta autoreklama bez treści merytorycznej. Jeśli nie ma faktów do udokumentowania, nie ma sekcji.
6. **Zachowaj wszystkie `<ref>`** — najpierw przenieś przypisy do nowej wersji, potem redaguj treść.

## Zasady NPOV dla sekcji instytucji

- **Due weight:** wydarzenia opisuj proporcjonalnie do ich znaczenia. Bieżący spór z 2026 nie powinien dominować artykułu o całej instytucji.
- **Fakty vs zarzuty:** „zgłosili podejrzenia naruszeń" a nie „łamali prawo". „Według doniesień medialnych" a nie w głosie encyklopedii.
- **Obie strony:** jeśli opisujesz zarzuty wobec instytucji, zaznacz, czy instytucja przedstawiła stanowisko. Jeśli nie — napisz wprost: „W dostępnych źródłach nie przedstawiono oficjalnego stanowiska".
- **Brak dosłownych cytatów:** nie przytaczaj całych fragmentów wypowiedzi jednej strony sporu. Parafrazuj: „uznał działania za próbę ograniczenia krytyki i zarzucił kierownictwu...".
- **Język:** „grzmi", „dziwna kosmiczna awantura" to tytuły prasowe, nie opis encyklopedyczny. Używaj neutralnych określeń.

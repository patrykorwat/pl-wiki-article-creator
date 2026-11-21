# Reguły tekstu polskiego i terminologia

## Reguły tekstu polskiego

- **Cudzysłów:** „..." (polskie zamknięte), NIE "..." (angielskie proste)
- **Myślniki (en-dash, U+2013):**
  - **DOZWOLONE w:** definicji w leadzie (`'''Termin''' – definicja`), podpisach grafik, punktach list wypunktowanych `* tekst – opis`, zakresach lat (1981–2011), tytułach cytowanych źródeł.
  - **ZABRONIONE w:** łączeniu zdań/zdań składowych w tekście głównym. Zamiast myślnika między klauzulami używaj kropki (nowe zdanie) lub przecinka (średnik też jest zabroniony – patrz reguła o średnikach). Źle: `technologii – czego przykładami są...`. Dobrze: `technologii. Ich przykładami są...`.
  - **NIE myl z hyphenem (-)** – en-dash jest dłuższy.
- **Lead:** `'''Termin''' – definicja` – to JEDYNY wyjątek, myślnik w leadzie jest dozwolony i standardowy.
- **Tytuły sekcji:** muszą brzmieć naturalnie po polsku. Unikaj dosłownych kalk z angielskiego, zwłaszcza z użyciem „wielokrotnego użytku" jako przydawki przed rzeczownikiem:
  - Źle: `=== W pełni wielokrotnego użytku ===` (brzmi jak tłumaczenie „Fully reusable")
  - Dobrze: `=== Pełna odzyskiwalność ===` 
  - Źle: `=== Częściowo wielokrotnego użytku ===` (brzmi sztucznie)
  - Dobrze: `=== Odzyskiwalność częściowa ===`
  - W treści zdań „wielokrotnego użytku" jest OK jako określnik po rzeczowniku, np. „rakieta nośna wielokrotnego użytku" – ale nie jako przydawka przed nim w nagłówku sekcji.
- **Średniki:** NIGDY nie używaj średnika (;) w tekście encyklopedycznym – łącz zdania kropką lub spójnikiem („X; Y” → „X. Y”). Wyjątek: „;” jako separator parametrów wewnątrz szablonów (np. w `{{cytuj}}`). To twarda reguła użytkownika — przed publikacją sprawdź średniki w prozie: najpierw wyciąj wszystkie `{{...}}` (regexem `\{\{[^{}]*\}\}`), bo parametry szablonów legalnie zawierają „;” — grep po surowym pliku daje same fałszywe alarmy, po których przestajesz patrzeć.
- **Autorzy w cytowaniach:** oddzielaj przecinkiem, NIE średnikiem
  - Poprawnie: `autor=Jan Kowalski, Anna Nowak`
  - Niepoprawnie: `autor=Jan Kowalski; Anna Nowak`
- **"i inni" w cytowaniach:** unikaj. Używaj tylko nazwiska pierwszego autora (np. `autor=Heribert Kuczera`, a nie `autor=Heribert Kuczera i in.`). {{cytuj}} automatycznie doda „i in." jeśli podasz więcej niż 5 autorów średnikami – ale w przypadku 2-3 autorów wypisz ich wszystkich.
- **Każde zdanie z faktem wymaga przypisu.** Nie wystarczy, że akapit ma jeden przypis na końcu – każde twierdzenie merytoryczne musi mieć własny `<ref>`. Zdania bez przypisu odbierane są jako nieencyklopedyczne, a o firmach jako promocyjne („reklama").
## Precyzja terminologiczna — pułapki przy tłumaczeniu haseł technicznych

Przy tłumaczeniu artykułów technicznych z en.wiki na pl.wiki: pełna tabela fałszywych odpowiedników (astronautyka/inżynieria) w `references/terminologia-techniczna.md` — kluczowe: wahadłowiec to system orbitalny, nie rakieta nośna; booster → dopalacz; stopień → człon; reusability → odzyskiwalność.

**Zasada ogólna:** jeśli tytuł sekcji lub zdanie brzmi jakby było przetłumaczone słowo w słowo z angielskiego (zwłaszcza z długą przydawką przed rzeczownikiem: „w pełni wielokrotnego użytku rakieta"), to znaczy że jest niepoprawne po polsku. Przepisz je tak, by brzmiało naturalnie.
## Naturalny szyk polski i spójność terminologiczna

### Szyk wyrazów: unikaj kalk rosyjskich i angielskich

Polski ma elastyczny, ale nie dowolny szyk. Przy tłumaczeniu nazw pojęć złożonych pilnuj naturalnej kolejności: rzeczownik wiodący + przydawka/dopełniacz.

Realne poprawki z sesji (tworzenie hasła o „liberal international order"):
- **ŹLE:** „Liberalny międzynarodowy ład" — brzmi jak kalka (szyk dwóch przymiotników przed rzeczownikiem).
- **DOBRZE:** „Liberalny ład międzynarodowy" (Liberalny + ład + międzynarodowy).
- Analogicznie: „atlantyzm", nie „atlantycyzm".

Zasadę tę stosuj też do nazw artykułów i tytułów sekcji — jeśli szyk brzmi nie po polsku, przestaw wyrazy.

### Terminologia zgodna z istniejącymi hasłami pl.wiki

Zanim wybierzesz polski odpowiednik terminu-klucz, sprawdź, jak nazywa się istniejące hasło na pl.wiki, i bądź z nim spójny. Przykład z sesji:
- en. „international order" ma na pl.wiki hasło **„Ład międzynarodowy"** — więc w hasłach pochodnych używaj **„ład"** („liberalny ład międzynarodowy"), NIE „porządek".
- Ale rozróżnij terminy techniczne, gdzie „porządek" jest właściwe: „porządek polityczny", „porządek konstytucyjny" (terminologia Ikenberry'ego), „porządek westfalski", „porządek przymusowy". Użyj hasła-nadrzędnego („ład") dla pojęcia wiodącego, a „porządek" dla konkretnych terminów technicznych/cudzych definicji.

Zasada: **dopasuj nomenklaturę do istniejącej struktury kategorii i haseł pl.wiki; nie wymyślaj własnego odpowiednika, jeśli istnieje już przyjęty.**

Dla prawa UE terminologię bierz z polskiej wersji językowej aktu na EUR-Lex (celex + `/PL/`): oficjalne tłumaczenie stoi w treści dokumentu, a chrome strony bywa po angielsku (tytuł „- EN”) — to nie jest brak wersji PL. Kalkę medialną (np. „28. reżim” wobec oficjalnego „28. system prawny”) podawaj jako wariant, nie termin wiodący.


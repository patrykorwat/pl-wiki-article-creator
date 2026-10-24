# Source verification protocol — weryfikacja źródeł przed dodaniem przypisu

## Dlaczego to ważne

Najczęstszy zarzut wobec edytorów Wikipedii to **przypisy, które nie potwierdzają tezy** lub **nie istnieją**. Fałszywy przypis podważa wiarygodność całego artykułu. Gorzej niż brak przypisu.

## Zasady bezwzględne

**Zasada 1 – Źródło musisz OTWORZYĆ i PRZECZYTAĆ**
- Nie proponuj źródła, którego nie otworzyłeś.
- Nie zakładaj treści po tytule, autorze ani wydawcy.
- Paywall/licencja = to źródło jest dla ciebie NIEDOSTĘPNE. Nie cytuj go.

**Zasada 2 – Teza musi być POTWIERDZONA w źródle**
- Nie wystarczy, że źródło „pasuje do tematu". Musisz sprawdzić, czy konkretne zdanie/teza, którą chcesz udokumentować, faktycznie występuje w źródle.
- Jeśli źródło ma 200 stron, a ty nie masz dostępu do konkretnej strony — nie cytuj.

**Zasada 3 – Nie wymyślaj danych bibliograficznych**
- Tytuł, rok, wydawca, ISBN, numer strony — każde pole musi być zweryfikowane.
- Sprawdź w Open Library / WorldCat, czy książka istnieje pod dokładnie tym tytułem i rokiem.
- Numer strony podawaj TYLKO jeśli masz książkę w ręku (lub otwarty PDF z widoczną paginacją).

**Zasada 4 – Domeny muszą działać**
- Każdy URL musi zwracać HTTP 200, zanim go dodasz.
- Jeśli domena nie resolve'uje się = źródło nie istnieje. Nie dodawaj.

**Zasada 5 – Zero portali wiki**
- Żadnych openlist.wiki, Wikipedia, fandom, memory/wiki itp.
- Treść edytowalna przez użytkowników = nieakceptowalna jako źródło.

**Zasada 6 – Zero domysłów**
- „To źródło na pewno o tym pisze" to nie jest weryfikacja.
- Jeśli nie możesz znaleźć w źródle konkretnej tezy — nie dodawaj przypisu.

## Protokół weryfikacji — 5 kroków

### Krok 1: Czy źródło istnieje?

**Dla stron WWW:**
- Sprawdź, czy domena resolve'uje się (curl -sIL URL / browser_navigate)
- Jeśli domena nie istnieje (ERR_NAME_NOT_RESOLVED, 404) → źródło nie nadaje się
- Jeśli strona istnieje, sprawdź, czy zawiera treść, a nie tylko placeholder

**Dla książek:**
- Sprawdź w Open Library: curl -sL "https://openlibrary.org/search.json?q=..."
- Potwierdza ISBN, wydawcę, rok. Jeśli książki nie ma w żadnym katalogu → prawdopodobnie nie istnieje pod tą nazwą

**Dla artykułów naukowych:**
- Sprawdź, czy DOI/strona czasopisma prowadzi do istniejącej strony
- Jeśli paywall → zaznacz to. Nie możesz potwierdzić konkretnej treści, tylko że strona istnieje.

### Krok 2: Czy masz dostęp do treści?

- Paywall = STOP. Nie cytuj tego, czego nie przeczytałeś.
- Tylko abstrakt = STOP. Abstrakt nie udowadnia, że reszta artykułu wspiera twoją tezę.
- Jeśli źródło jest w języku, którego nie rozumiesz → nie cytuj.

### Krok 3: Czy źródło potwierdza tę konkretną tezę?

To najważniejszy i najczęściej pomijany krok.

- Przeczytaj źródło (lub tyle, ile jest dostępne)
- Znajdź KONKRETNE ZDANIE potwierdzające tezę
- Jeśli nie znajdujesz — TEZA NIE JEST UDOKUMENTOWANA. Nie dodawaj przypisu.
- Nie sugeruj źródeł na podstawie tytułu — tytuł może sugerować coś, czego w tekście nie ma

#### Pułapka: artykuł przeglądowy (explainer)

Artykuł przeglądowy (np. Al Jazeera "What is the St Petersburg forum") może być dobrym źródłem dla ogólnych faktów o temacie („pierwsze forum odbyło się w 1997"), ale NIE nadaje się jako źródło dla szczegółowych danych („liczba uczestników w 1997", „kto uczestniczył w 1998").

**Zasada:** dla każdej tezy sprawdź, czy źródło zawiera JĄ, a nie tylko jej temat. Źródło o Puszkinie nie znaczy, że potwierdza datę jego urodzenia — trzeba sprawdzić konkretną liczbę.

**Przykład porażki (lipiec 2026):** użyto artykułu Al Jazeera o SPIEF jako źródła dla 20+ wierszy w tabeli edycji, podczas gdy artykuł potwierdzał TYLKO:
- „pierwsze forum w 1997" (ogólnie)
- „Arabia Saudyjska państwem gościem w 2026"
- „130+ państw w 2026"

Nie potwierdzał natomiast: konkretnych liczb uczestników dla lat 1997–2015, udziału Łukaszenki w 1998, Zemana w 2001, Sarkozy'ego w 2010, Merkel w 2013, Lenexpo w 2006 itd. Te tezy wymagają własnych, odrębnych źródeł.

### Krok 4: Czy dane bibliograficzne są poprawne?

- Tytuł — dokładnie taki, jak w źródle
- Rok — zgodny z metadanymi źródła
- ISBN — sprawdzony (np. przez Open Library)
- Autor — zgodny z metadanymi
- URL — działający (HTTP 200)

### Techniki dostępu, gdy treść jest trudna do wyciągnięcia

- **Artykuł naukowy za paywallem** → zweryfikuj metadane przez Crossref: `curl -sL https://api.crossref.org/works/<DOI>`. Potwierdza tytuł, autorów, datę, strony, ISSN. Metadane NIE potwierdzają treści — sam artykuł pozostaje niedostępny, więc nie cytuj tez, których nie przeczytałeś.
- **Artykuł prasowy, który wraca pustym/JS-owym body** (np. spiegel.de) → `curl` z normalnym UA, potem w Pythonie usuń `<script>...</script>` i tagi HTML, a następnie wyszukaj frazy-klucze w tekście. Dopiero widoczne zdania liczą się jako przeczytane.
- **Stare artykuły prasowe, których żywy URL znika** → web.archive.org (`https://web.archive.org/web/<rok>/<url>`); archiwum jest czytelne, gdy curl zwraca pełny HTML. Preferuj żywy URL w przypisie, archiwum jako `archiwum=`.
- **Cytat, które krąży wyłącznie w publikacjach strony zainteresowanej** (stowarzyszenia wypędzonych, portale ideologiczne, fandomy, RT) → to NIE jest źródło encyklopedyczne, nawet jeśli cytat bywa powtarzany w mediach głównego nurtu. Można o nim wspomnieć jako o twierdzeniu danej strony (z atrybucją), ale nie dokumentować go jako faktu.
- **Wikipedia w innej wersji językowej** → traktuj wyłącznie jako indeks tropów: jej przypisy prowadzą do źródeł pierwotnych, które samemu trzeba otworzyć i przeczytać. Sam artykuł wiki nigdy nie jest cytowany.
- **ISBN** → przy braku dostępu do Open Library zweryfikuj cyfrę kontrolną ISBN-13 programowo (suma ważona 1/3, modulo 10); poprawna suma dowodzi poprawności wpisu, nie istnienia treści.
- **Data publikacji niewidoczna w body** → wydobądź z metadanych HTML-a, nie zgaduj jej: `curl -sL URL -H "User-Agent: Mozilla/5.0" | grep -oE '<time[^>]*datetime="[^"]+"'` albo `"datePublished"` w JSON-LD. Uwaga: strona zawiera zwykle kilka tagów `<time>` (tasiemka „powiązane aktualności", sidebar) — weź ten z nagłówka/stopki artykułu, a w razie wątpliwości skoryguj o datkę widoczną w tekście lub slug URL-a. Data trafia do `data=` w {{cytuj}}.

### Krok 5: Pytanie kontrolne

„Czy gdyby ktoś kliknął w ten link, znalazłby dokładnie to, do czego go przypisałem?"

Jeśli odpowiedź brzmi „nie", „nie wiem" lub „może" — nie dodawaj przypisu.

## Przykład porażki (Stepan Rudnycki — lipiec 2026)

Poniższy przypadek wydarzył się naprawdę. Służy jako przestroga przed łamaniem zasad 1–6.

**Zadanie:** znajdź dodatkowe przypisy do hasła o Stepanie Rudnyckim na pl.wiki.

**Co zrobiono źle:**

| Propozycja | Co poszło nie tak |
|---|---|
| sandarmoh.org (Юрий Дмитриев) | Domena nie istnieje. Nie sprawdzono przed dodaniem. |
| Engelmann, Albrecht Penck: Geograph und Politiker (1996) | Książka pod tym tytułem i rokiem nie istnieje. Zmyślony wpis bibliograficzny. |
| Ławrinenko, Rozstrilane widrodżennia | Nie sprawdzono, czy książka w ogóle wymienia Rudnyckiego. |
| Seegel, Map Men (2018) | Książka istnieje, ale treść niedostępna (paywall). Nie wiadomo, co pisze o Rudnyckim. |
| Memoriał (openlist.wiki) | Portal typu wiki — treść edytowalna przez użytkowników. |
| Stebelsky, Placing Ukraine on the Map | Książka istnieje, ale sugerowano konkretne numery stron bez dostępu do książki. |

**Lekcja:** z 6 propozycji źródeł, 0 było w pełni zweryfikowanych — ani istnienie, ani dostęp do treści, ani zgodność z tezą. Każde naruszało co najmniej jedną z Zasad 1–6.

**Protip:** jeśli po przejściu protokołu okaże się, że nie ma żadnego źródła, które możesz zweryfikować — lepiej nie dodawać nic, niż dodać zmyślony lub niepotwierdzony przypis.

## Zasada nadrzędna

Lepiej mieć mniej przypisów, z których każdy jest zweryfikowany, niż wiele, które mogą być fałszywe.

Weryfikowalność ponad estetyką. Krótszy artykuł z 5 czystymi źródłami bije dłuższy z 20, z których połowa nie istnieje lub nie pasuje do tezy.

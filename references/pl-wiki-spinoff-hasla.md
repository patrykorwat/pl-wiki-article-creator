# Spin-off hasła nadrzędnego: decyzja, tytuł, plan integracji (pl.wiki)

Procedura dla sytuacji, gdy temat rozwija się wewnątrz dużego hasła nadrzędnego (np. inwestycja opisana w haśle portu) i pojawia się pytanie „osobny artykuł czy rozbudowa istniejącej sekcji".

## 1. Decyzja: osobne hasło vs rozbudowa sekcji

Decyduj po kryteriach obiektywnych, nie po objętości istniejącego tekstu:
- temat ma **dedykowany akt prawny** dotyczący wyłącznie go (własna ustawa, rozporządzenie);
- ma **własną stronę dokumentacji** i samodzielny strumień prasowy obejmujący lata (kilkadziesiąt datowanych materiałów, nie jedna fala przy ogłoszeniu);
- istnieje **precedens tej samej relacji** w tym samym obszarze (np. Port Północny jako osobne hasło wobec Port morski Gdańsk) — przy analogicznej strukturze rozstrzyga.

Brak tych kryteriów = rozbuduj sekcję. Rozbieżność (duży strumień prasowy, ale brak aktu i precedensu) rozstrzygaj po precedensie i skali relacji do hasła nadrzędnego.

## 2. Tytuł i infobox

- Sprawdź zderzenie nazw: nazwa rodzajowa (typu „port zewnętrzny") bywa używana dla kilku inwestycji w różnych miastach — dodaj kwalifikator miejscowy nawet, gdy lokalne media go opuszczają („Port zewnętrzny w Gdyni", nie „Port zewnętrzny").
- Odwzoruj wzorzec siostrzanego hasła w całości: jeśli wzorzec nie ma infoboksu, nie dobieraj szablonu na siłę — ogólne szablony (typu {{Infobox projekt}}) pasują do projektów programowych, nie do obiektów infrastruktury; pola takie jak www/status bywają „Nieznane pola".
- Batch-check istnienia wariantów tytułu (z kwalifikatorem i bez, wraz z przekierowaniami) jednym wywołaniem API z `redirects=1`, zanim napiszesz pierwszy akapit.

## 3. Szkic z nagłówkiem-umową roboczą

W nagłówku pliku `.wiki` (komentarz HTML, USUWANY przy publikacji — reguła „brak komentarzy HTML" dotyczy treści artykułu, nie nagłówka roboczego) zapisz:
- decyzję o rozdzieleniu i jej kryteria;
- plan integracji hasła nadrzędnego: `{{Osobny artykuł|<Tytuł>}}` + jedno-dwa zdania streszczenia zastępujące dotychczasowe akapity o temacie;
- listę zapisów hasła nadrzędnego, których NIE przenosić bez porównania ze świeżymi źródłami (stare kwoty, jednostki — np. „ton" zamiast TEU — i daty); każdy stary zapis porównaj z bieżącym źródłem pierwotnym i popraw w nowym haśle.

## 4. Publikacja i domknięcie

- Wklej treść z pliku kanonicznego bez komentarza nagłówkowego i uruchom render-check (PIASEK) na gotowym tekście.
- Wykonaj plan integracji hasła nadrzędnego w tej samej sesji — publikacja spin-offu bez tej edycji zostawia rozbudowany tekst i zdublowaną treść w haśle nadrzędnym.
- Hasło o inwestycji „na dziś" żyje w rytmie komunikatów: po każdej decyzji instytucji (wybór partnera, rozstrzygnięcie) planuj jednozdaniową aktualizację zamiast prognozy na zapas.

# Szablony pl.wiki — weryfikacja istnienia

Przed użyciem dowolnego szablonu (`{{Nazwa}}`) na pl.wiki ZAWSZE sprawdź, czy istnieje.
Idź do `https://pl.wikipedia.org/wiki/Szablon:Nazwa_szablonu` i zobacz, czy strona istnieje.

## Istnieją (zweryfikowane)

| Szablon | Zastosowanie |
|---|---|
| `{{Flaga|USA}}` / `{{Flaga|POL}}` | Flagi państw w tabelach, infoboxach |
| `{{Commons}}` | Link do Wikimedia Commons (NIE `{{Commons category}}`) |
| `{{Przypisy}}` | Sekcja przypisów (NIE `<references>`) |
| `{{Osobny artykuł|Nazwa}}` | Odnośnik do głównego artykułu w sekcji |
| `{{cytuj}}` | Uniwersalny szablon cytowania (mała litera!) |
| `{{Biogram infobox}}` | Infobox dla osób |
| `{{Przedsiębiorstwo infobox}}` | Infobox dla firm |
| `{{Instytucja państwowa infobox}}` | Infobox dla instytucji |
| `{{Serial infobox}}` / `{{Film infobox}}` | Infobox dla filmów/seriali |
| `{{Miejscowość infobox}}` | Infobox dla miejscowości |
| `{{Wydarzenie infobox}}` | Infobox dla wydarzeń |
| `{{Rakieta nośna infobox}}` | Infobox dla konkretnych rakiet nośnych |
| `{{tabela-tak|tekst}}` | Zielona komórka tabeli z tekstem |
| `{{tabela-nie|tekst}}` | Czerwona komórka tabeli z tekstem |
| `{{tabela-częściowo|tekst}}` | Żółta komórka tabeli z tekstem |
| `{{tabela-?|tekst}}` | Szara komórka tabeli z tekstem |
| `{{SORTUJ:Nazwisko, Imię}}` | Sortowanie kategorii dla biogramów |
| `{{Kontrola autorytatywna}}` | Kontrola autorytatywna (VIAF, LCCN itp.) |
| `{{link-interwiki|Hasło|Q=Qxxxxx|tekst=...}}` | Link do hasła, które nie istnieje na pl.wiki |
| `{{Uwagi}}` | Sekcja „Uwagi” (grupa przypisów `<ref group="uwaga">`) |
| `{{Odsłuchaj|plik=...|tytuł=...}}` | Odtwarzacz pliku audio (np. w „Zobacz też”) |

## NIE istnieją (pomimo pozoru z en.wiki)

| Szablon | Zamiast tego |
|---|---|
| `{{Właściwy tytuł|...}}` | Nie używaj; pl.wiki nie ma tego szablonu |
| `{{Short description|...}}` | Nie używaj; pl.wiki nie ma odpowiednika (`{{Krótki opis}}` też nie istnieje) |
| `{{Astronautyka}}` | Nie istnieje na pl.wiki |
| `{{Nowe technologie|tematyka=...}}` | Nie istnieje na pl.wiki |
| `{{Operacyjny}}` / `{{Dropped}}` / `{{Yes}}` / `{{No}}` | Użyj `{{tabela-tak}}` / `{{tabela-nie}}` w tabelach |
| `{{Commons category|...}}` | Użyj `{{Commons|...}}` |
| `{{Przypisy źródłowe}}` | Użyj `{{Przypisy}}` |
| `{{R}}` (skrócony przypis) | Użyj `<ref name="x" />` |
| `{{Cytuj}}` (z dużej) | Użyj `{{cytuj}}` (z małej) |
| `{{Wayback}}` | Nie istnieje; archiwizację podaj w `{{cytuj}}` (`archiwum=`, `zarchiwizowano=`), a w „Linkach zewnętrznych” linkuj snapshot Wayback bezpośrednio |

## Zasada: zweryfikuj, zanim użyjesz

Nigdy nie zakładaj, że szablon z en.wiki istnieje też na pl.wiki.
Zawsze:
1. Otwórz `https://pl.wikipedia.org/wiki/Szablon:Nazwa`
2. Jeśli strona nie istnieje, szukaj alternatywy
3. Jeśli nie ma alternatywy, zrezygnuj z szablonu (użyj surowego formatowania)

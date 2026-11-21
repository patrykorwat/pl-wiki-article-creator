# Tłumaczenie artykułów o wyborach (en.wiki → pl.wiki)

Zweryfikowano na tłumaczeniu „2026 Russian legislative election” → „Wybory parlamentarne
w Rosji w 2026 roku” (sierpień 2026). Nazwa wzorcowa: `Wybory parlamentarne <Kraj> w <Rok> roku`
(zgodnie z istniejącymi hasłami, np. „Wybory parlamentarne w Rosji w 2016 roku”).

## Sekwencja kroków

1. **Pobierz oryginał**: `action=parse&page=<Tytul>&prop=wikitext&formatversion=2` na en.wiki.
   Uwaga: `read_file` przycina długie linie — długie akapity/tabele wyciągaj przez
   python `print(lines[n-1])`, nie przez czytnik.
2. **Sprawdź, czy pl.wiki hasło już istnieje** (search + `titles=`). Jeśli nie — artykuł może
   być podstawą nowego hasła, ale sam NIGDY nie publikuj (zasada: edycja przez plik do ręcznego
   wklejenia przez użytkownika).
3. **Pobierz artykuł-poprzednik z tej samej serii** (poprzednie wybory) jako wzorzec:
   terminologia (np. Jedna Rosja, Duma Państwowa Federacji Rosyjskiej, Giennadij Ziuganow),
   sposób użycia infoboxu, wzorzec kategorii.
4. **Zweryfikuj hasła do linkowania batchem** (`action=query&titles=a|b|c&redirects=1`,
   40–50 tytułów/zapytanie) — ale NIE ufaj batchowi bez render-check (patrz pitfall o normalizacji
   wielkości liter w references/linki-i-grafiki.md).
5. **Autorytatywna weryfikacja**: render serwerowy pełnego pliku (`action=parse`, POST `text=`)
   i skan HTMLa za `redlink=1` oraz błędy szablonów. Zautomatyzowane: `scripts/verify_pl_wiki_article.py`.
   Render łapie czerwone linki, których batch nie widzi, ORAZ podpowiada, że jakieś hasło ma już
   pl.wiki artykuł (→ zwykły link, nie interwiki).
6. **Kategorie** wg wzorca poprzednika: `[[Kategoria:<Rok> w <Kraju>]]`,
   `[[Kategoria:Wybory parlamentarne w <Kraju>|<rok>]]`, `[[Kategoria:Wybory w <rok>|<Kraj>]]`
   (np. z „Wybory parlamentarne w Rosji w 2016 roku”: `2016 w Rosji` / `Wybory parlamentarne
   w Rosji|2016` / `Wybory w 2016|Rosja`).

## Infobox wyborczy na pl.wiki

- Szablon: **{{Wybory infobox}}** (istnieje). Zweryfikowane parametry (wg „Wybory prezydenckie
  w Rosji w 2024 roku”): `nazwa`, `państwo`, `rodzaj`, `data przeprowadzenia`, `data
  zarządzenia`, `zarządzający`, `podstawa prawna`, `ordynacja wyborcza`, `koszt`, `wyniki 1`,
  `1. komitet 1`, `wynik 1. komitetu 1`, `kolor 1. komitetu 1`, `procent frekwencji`,
  `poprzednie`, `następne`, `wikinews`, `commons`, `www`.
- Dla **wyborów przyszłych/trwających** infobox minimalny: bez wyników; bez `poprzednie`/
  `następne`, jeśli sąsiednie hasło (np. wybory 2021) nie istnieje na pl.wiki (zero czerwonych linków).
- **en.wiki `{{party color|...}}` / `{{abbr}}` NIE mają odpowiedników na pl.wiki**
  („Szablon:Partia polityczna" NIE istnieje). Przy tłumaczeniu tabel partyjnych pomiń kolorowane
  komórki — czysta tabela z nazwami partii to poprawna adaptacja.

## Pułapki specyficzne dla wyborów

- **Liczby**: en. „trillion” = 10¹² = polskie **„bilion”**. „30 trillion rubles” → „30 bilionów
  rubli”. Natomiast 10⁹ = „miliard”. Łatwo pomylić przy kwotach budżetowych.
- **Błędny przypis w tabeli en.wiki**: w oryginale wiersz tabeli o zjeździe jednej partii
  cytował artykuł o zjeździe innej (Sprawiedliwa Rosja → artykuł RBC o Nowych Ludziach).
  Sprawdzaj, czy ref w tabeli faktycznie dotyczy tej partii; podmień na właściwy.
- **Typowe link-interwiki (QID zweryfikowane)**: Nowi Ludzie = Q98842815, Rodina (partia) =
  Q1190255, Partia Demokracji Bezpośredniej = Q108663167, Rosyjska Partia Ekologiczna „Zieloni”
  = Q2634417, Rosyjska Partia Emerytów = Q1435537, Mądre głosowanie (Smart Voting) =
  Q99701164, Południe przeciw Putinowi = Q124726840. (Serhij Arbuzow ma już pl.wiki hasło →
  zwykły [[Serhij Arbuzow|...]], nie interwiki.)
- **Źródła**: artykuły o wyborach cytują głównie media rosyjskie (TASS, RIA, RBK, Kommiersant,
  Wiedomosti) + część niezależnych (Moscow Times, Meduza, Reuters, Amnesty, Nowa Gazieta
  Europa). Przekładając 1:1 zostawiasz refy i oznaczasz użytkownikowi, które są prokremlowskie;
  możesz też od razu podmienić na niezależne tam, gdzie ta sama teza ma niezależne źródło.
- Akapit o opozycji pozasystemowej bywa w en.wiki **bez przypisów** — wierne tłumaczenie tworzy
  na pl.wiki akapit bez źródeł; oznacz to użytkownikowi do decyzji (dodać źródła albo skrócić).

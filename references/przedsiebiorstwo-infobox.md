# {{Przedsiębiorstwo infobox}} — pola i pułapki

Na podstawie rzeczywistego szablonu pl.wiki (zweryfikowane przez API).

## Pola DOZWOLONE

| Pole | Typ wartości | Uwagi |
|---|---|---|
| `nazwa` | string | Nazwa firmy |
| `nazwa oryginalna` | string | w oryginalnym języku |
| `logo` | string | `Nazwa_pliku.png` (bez `[[Plik:]]`) |
| `grafika` | string | Zdjęcie siedziby itp. |
| `opis grafiki` | string | Podpis pod grafiką |
| `państwo` | kod ISO | `POL`, `JPN`, `USA` – szablon {{państwo}} sam generuje flagę |
| `siedziba` | string | Miasto, można linkować |
| `adres` | string | Pełny adres |
| `data założenia` | string | Data |
| `data likwidacji` | string | Data |
| `forma prawna` | string | np. `[[spółka akcyjna]]` |
| `prezes` | string | Imię i nazwisko |
| `dyrektor` | string | Jeśli dotyczy |
| `przewodniczący RN` | string | Przewodniczący rady nadzorczej |
| `udziałowcy` | string | Główni akcjonariusze |
| `numer rejestru` | string | KRS lub podobny |
| `zatrudnienie` | string | Liczba, bez daty |
| `giełda` | string | **UŻYWAJ szablonu** `{{tyo|numer}}`, NIE ręcznego linku |
| `ISIN` | string | Kod ISIN |
| `symbol akcji` | string | Symbol na giełdzie |
| `rok` | string | Rok finansowy w headerze „Dane finansowe". **Tu daj przypis** `<ref name=X />` |
| `przychody` | string | Sama wartość, **bez roku i przypisu** |
| `wynik operacyjny` | string | EBIT, bez roku i przypisu |
| `wynik netto` | string | Zysk netto, bez roku i przypisu |
| `aktywa` | string | Aktywa, bez roku i przypisu |
| `kapitał własny` | string | Kapitał własny, bez roku i przypisu |
| `kapitał zakładowy` | string | Kapitał zakładowy (istnieje osobno od `kapitał własny`!) |
| `commons` | string | `Nazwa_kategorii` – wstawia link do Commons **w infoboxie** |
| `wariant flagi` | string | Wariant flagi państwowej |
| `kod mapy` | string | Do lokalizacji na mapie |
| `opis miejsca` | string | Opis punktu na mapie |
| `współrzędne` | string | Współrzędne geograficzne |

## Pola NIEISTNIEJĄCE (powodują błąd)

- `www` / `strona` / `strona internetowa` → **nie istnieją**
- `logo_size` → **nie istnieje**
- `image` / `caption` → **nie istnieją** (to en.wiki)
- `type` / `traded_as` → **nie istnieją**

## Wzorzec danych finansowych

```
 |rok               = 2023<ref name=Financials />
 |przychody         = 80,125 mld [[Dolar amerykański|USD]]
 |wynik netto       = 1,569 mld USD
 |kapitał zakładowy = 20,290 mld USD
 |zatrudnienie      = 117 540
```

Rok i przypis TYLKO w `|rok=`. Reszta: czyste wartości. Nazwany przypis zdefiniowany w leadzie.

## Szablony giełdowe

- Tokio: `{{tyo|numer}}` (np. `{{tyo|3382}}`)
- Nowy Jork: `{{nyse|symbol}}`
- Londyn: `{{lse|symbol}}`
- Warszawa: `{{gpw|symbol}}`

Zamiast ręcznych linków typu `[[Giełda Papierów Wartościowych w Tokio|TYO]]: 3382`.

## `commons` w infoboxie vs osobny szablon

ZAMIAST:
```
{{Commons|Seven & i Holdings}}
```

RÓB:
```
 |commons           = Seven & i Holdings
```
(w polu infoboxu)

## Znane pułapki

1. **Puste nazwane przypisy** – jeśli infobox używa `<ref name=Financials />`, definicja musi być wcześniej w tekście (leadzie). Inaczej parser zgłasza „Brak tekstu w przypisie".
2. **Duplikaty pól** – nie daj `zatrudnienie` dwa razy.
3. **Red linki** – każde `[[hasło]]` sprawdź HTTP 200. Jeśli 404 → usuń nawiasy, zostaw zwykły tekst.
4. **Relacje** – „słabnąca spółka matka" → doprecyzuj „(Ito-Yokado)".
5. **Dane finansowe w leadzie** – nie powtarzaj danych z infoboxu w tekście.

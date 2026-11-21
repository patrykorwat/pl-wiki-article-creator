# Umiejscowienie przypisów względem interpunkcji (pl.wiki) — błąd powtarzany, korygowany przez użytkownika wielokrotnie

## Reguła
Przypis stoi PRZED znakiem interpunkcyjnym: `tekst<ref name="x" />.`, NIGDY `tekst.<ref name="x" />`.
Dotyczy kropek, przecinków, średników i dwukropków (np. w listach punktowanych).

## Auto-check po KAŻDEJ edycji (nie tylko przy dodawaniu refów)
```python
import re
# 1) kropka przed refem — musi być 0
len(re.findall(r'\.(?=<ref\b)', t)) == 0
# 2) kropka wypadła przy przenoszeniu: ref, potem spacja i wielka litera = nowe zdanie bez kropki
len(re.findall(r'(?:</ref>|/>) (?=[A-ZĄĆĘŁŃÓŚŻ])', t)) == 0
# 3) kropka uwięziona między sąsiednimi refami
len(re.findall(r'(?:</ref>|/>)\.(?=<ref\b)', t)) == 0
# 4) podwójne kropki
len(re.findall(r'\.\.', t)) == 0
```

## Naprawa (kolejność reguł ma znaczenie)
```python
def normalize(t):
    t = re.sub(r'(</ref>|/>)\.(?=<ref\b)', r'\1', t)   # kropka w środku ciągu refów -> połącz
    t = re.sub(r'(?<!\.)\.(?=<ref\b)', '', t)          # kropka przed refem -> usuń
    t = re.sub(r'((?:</ref>|/>))(?=\n)', r'\1.', t)     # ref na końcu akapitu -> dodaj kropkę
    t = re.sub(r'((?:</ref>|/>)) (?=[A-ZĄĆĘŁŃÓŚŻ])', r'\1. ', t)  # ref przed nowym zdaniem -> dodaj kropkę
    t = re.sub(r'((?:</ref>|/>)\.)\.(?= )', r'\1', t)  # nie podwajaj kropek
    return t
```

## Lekcja praktyczna
Kropka wypadająca między refami albo przed nowym zdaniem to typowy skutek masowego przenoszenia refów regexem — po każdej operacji odpal pełną baterię (4 wzorce) i verify_pl_wiki_article.py (łapie `Brak tekstu w przypisie` i `Nieznane pola`, ale nie łapie złego umiejscowienia interpunkcji).
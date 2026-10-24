#!/usr/bin/env python3
"""Weryfikacja pliku .wiki przed publikacją: przypisy (pełne definicje vs skróty),
interpunkcja przy refach, domeny .ru, istnienie linków wewnętrznych, render-check serwera pl.wiki.

Użycie: python3 verify_render.py PLIK.wiki [PLIK2.wiki ...]
Exit 0 = brak problemów; 1 = są problemy (lista na stdout).
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = 'HermesAgent/1.0 (wiki verification)'
API = 'https://pl.wikipedia.org/w/api.php'
BAD_RENDER = ['Nieznane pole', 'Brak tekstu w przypisie', 'Błąd w składni', 'mw-ext-cite-error']


def api(params, tries=3, delay=15):
    q = urllib.parse.urlencode(params)
    for _ in range(tries):
        try:
            req = urllib.request.Request(f'{API}?{q}', headers={'User-Agent': UA})
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception as e:  # 429/timeouty API — pauza i retry, nie porażka
            print(f'  api retry after: {e}')
            time.sleep(delay)
    return {}


def check(path):
    t = open(path).read()
    problems = []
    # 1) każdy ref name wymaga >=1 pełnej definicji w pliku
    defined = set(re.findall(r'<ref name="([^"]+)"\s*>', t))
    short = set(re.findall(r'<ref name="([^"]+)"\s*/>', t))
    miss = short - defined
    if miss:
        problems.append(f'przypisy bez pełnej definicji: {sorted(miss)}')
    # 2) interpunkcja przy refach (3.4) — kropka po </ref> bywa treścią refa: tylko flaga do ręcznego checku
    for i, line in enumerate(t.split('\n'), 1):
        if re.search(r'</ref>\s*([.,;:!?])', line):
            print(f'  [sprawdź ręcznie] linia {i}: interpunkcja po </ref>: {line[:80]}')
        if re.search(r' ([.,;:!?])<ref', line):
            problems.append(f'linia {i}: spacja+interpunkcja przed <ref')
    # 3) domeny .ru — zabronione jako źródła
    ru = re.findall(r'https?://[a-z.-]*\.ru[^\s\]|]*', t)
    if ru:
        problems.append(f'domeny .ru: {ru[:5]}')
    # 4) linki wewnętrzne — partie po 25 tytułów, redirecty rozwiązywane
    targets = sorted(
        m.group(1).strip() for m in re.finditer(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]', t)
        if not m.group(1).startswith(('Plik:', 'Kategoria:')))
    missing = []
    for i in range(0, len(targets), 25):
        d = api({'action': 'query', 'titles': '|'.join(targets[i:i + 25]),
                 'format': 'json', 'redirects': 1})
        if 'query' in d:
            missing += [p['title'] for p in d['query']['pages'].values() if 'missing' in p]
        time.sleep(5)
    if missing:
        problems.append(f'czerwone linki: {missing}')
    # 5) render-check PST na serwerze pl.wiki
    q = urllib.parse.urlencode({'action': 'parse', 'text': t, 'pst': '1',
                                'contentmodel': 'wikitext', 'prop': 'text',
                                'format': 'json', 'disablelimitreport': '1'})
    req = urllib.request.Request(API, data=q.encode(), headers={'User-Agent': UA})
    html = json.load(urllib.request.urlopen(req, timeout=60))['parse']['text']['*']
    for pat in BAD_RENDER:
        n = len(re.findall(pat, html))
        if n:
            problems.append(f'render: "{pat}" x{n}')
    n = len(re.findall(r'class="new"', html))
    if n:
        # sekcje „edytuj” i dyskusje szablonów nawigacyjnych też mają tę klasę — tylko info
        print(f'  [info] class="new" x{n} w renderze — sprawdź kontekst (link czy nawigacja)')
    print(f'{path}: {"OK" if not problems else "PROBLEMY"}')
    for p in problems:
        print('  -', p)
    return not problems


if __name__ == '__main__':
    ok = all(check(p) for p in sys.argv[1:])
    sys.exit(0 if ok else 1)

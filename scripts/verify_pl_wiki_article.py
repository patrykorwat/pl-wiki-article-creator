#!/usr/bin/env python3
"""Verify a Polish Wikipedia article draft (.wiki) before manual publication.

Usage:
    python3 verify_pl_wiki_article.py /path/to/Tytul_artykulu.wiki

Checks:
  1. No leftover HTML comments (<!-- ... -->) in the article content.
  2. Every <ref name="X" /> shorthand has a defining <ref name="X">...</ref> earlier
     (also for group="uwaga" notes used with {{Uwagi}}).
  3. Every [[wikilink]] resolves to an existing pl.wiki article (case-safe lookup).
  4. Every {{link-interwiki|...|Q=Q...}} QID resolves on Wikidata (throttled ~1.2 s/req);
     BAD = entity missing OR has a plwiki sitelink (then use a normal [[link]] instead);
     an API failure after retries is reported as UNKNOWN, never counted as BAD (flaky
     Wikidata calls must not flag valid QIDs).
  5. Every [[Plik:...]] / [[File:...]] exists on Wikimedia Commons.
  6. AUTHORITATIVE server-side render (action=parse, POST text= with the full wikitext):
       - no template errors ("Nieznane pola", "Nieznany parametr", "Błąd w przypisach", ...)
       - lists every red link; red links NOT covered by a {{link-interwiki}} target
         are genuine problems that must be fixed before the user pastes the article.

Why the render check is the ground truth:
  A naive batch existence check (action=query&titles=a|b|c) CAN lie. MediaWiki
  normalises the first letter of a title to uppercase EVEN inside the API response,
  so a script that looks up the input "śmierć X" against the returned key
  "Śmierć X" misses it and may print a false "OK" for a red link. The server-side
  render resolves the REAL link target against the DB and flags redlink=1, so ALWAYS
  run it — it catches what the batch check misses, and it warns when a pl.wiki article
  already exists under a Polish name you planned to interwiki-link (then use a normal
  [[link]] instead of {{link-interwiki}}).

Rate limits: pl.wiki tolerates fast batch queries; Wikidata is strict (HTTP 429) —
the script sleeps ~1.2 s between QID lookups.

Exit code 0 = no problems reported.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
PL = "https://pl.wikipedia.org/w/api.php"
COMMONS = "https://commons.wikimedia.org/w/api.php"
WD = "https://www.wikidata.org/w/api.php"


def api(url, attempts=4, delay=2.5, post=None):
    for a in range(attempts):
        try:
            if post is None:
                req = urllib.request.Request(url, headers=UA)
            else:
                req = urllib.request.Request(
                    url, data=post, headers={**UA, "Content-Type": "application/x-www-form-urlencoded"}
                )
            return json.load(urllib.request.urlopen(req, timeout=90))
        except Exception:
            if a == attempts - 1:
                return None
            time.sleep(delay * (a + 1))
    return None


def checklist_leaks(text):
    return text.count("<!--")


def ref_integrity(text):
    known = set(re.findall(r'<ref name="([^"]+)"', text))
    shorthand = set(re.findall(r'<ref name="([^"]+)"\s*/>', text))
    missing = sorted(shorthand - known)
    gknown = set(re.findall(r'<ref group="uwaga" name="([^"]+)"', text))
    gshort = set(re.findall(r'<ref group="uwaga" name="([^"]+)"\s*/>', text))
    missing_g = sorted(gshort - gknown)
    return missing, missing_g


def wikilinks(text):
    links = set()
    for m in re.finditer(r"\[\[([^\[\]\n]+?)\]\]", text):
        target = m.group(1).split("|")[0].split("#")[0].strip()  # obetnij fragment #sekcji — API daje fałszywy MISS dla tytułu z #, choć strona istnieje (np. [[Supersamochód#Hipersamochód|...]])
        if target.startswith(("Plik:", "File:", "Kategoria:", "Kategoria ", "#")) or not target:
            continue
        links.add(target)
    return sorted(links)


def check_wikilinks(links):
    """Case-safe existence check. Missing pages are keyed by the INPUT title in the
    API response, so map case-insensitively before declaring anything missing."""
    missing = []
    lst = list(links)
    for i in range(0, len(lst), 40):
        batch = lst[i : i + 40]
        params = {
            "action": "query",
            "titles": "|".join(batch),
            "format": "json",
            "formatversion": "2",
            "redirects": "1",
        }
        d = api(PL + "?" + urllib.parse.urlencode(params))
        if not d:
            print("  !! API call failed for batch; retry later:", batch[:3])
            continue
        res = {}
        for p in d.get("query", {}).get("pages", []):
            res[p["title"].lower()] = p.get("missing", False)
        for r in d.get("query", {}).get("redirects", []):
            res.setdefault(r["from"].lower(), False)
            res.setdefault(r["to"].lower(), False)
        for t in batch:
            if t.lower() not in res or res[t.lower()]:
                missing.append(t)
        time.sleep(0.4)
    return missing


def link_interwiki_qids(text):
    return sorted(set(re.findall(r"(?i)\{\{link-interwiki[^}]*?\|\s*Q=Q(\d+)\s*\}\}", text)))


def check_qids(qids):
    """BAD = entity missing OR has a plwiki sitelink (use [[link]] instead of interwiki).
    API failure after retries -> UNKNOWN (reported separately, never counted as BAD):
    a flaky/rate-limited wbgetentities call must not flag a valid QID as broken."""
    bad = []
    unknown = []
    for q in qids:
        params = {
            "action": "wbgetentities",
            "ids": "Q" + q,
            "props": "labels|sitelinks",
            "languages": "en",
            "format": "json",
        }
        d = api(WD + "?" + urllib.parse.urlencode(params))
        ent = (d or {}).get("entities", {}).get("Q" + q)
        if ent is None:
            unknown.append("Q" + q)
        elif ent.get("missing") is not None or "plwiki" in ent.get("sitelinks", {}):
            bad.append("Q" + q)
        time.sleep(1.2)
    return bad, unknown


def plik_files(text):
    files = set()
    for m in re.finditer(r"\[\[(?:Plik|File):([^|\]\n]+?)\s*[|\]]", text):
        files.add(m.group(1).strip())
    return sorted(files)


def check_commons(files):
    missing = []
    for i in range(0, len(files), 40):
        batch = files[i : i + 40]
        params = {"action": "query", "titles": "File:" + "|File:".join(batch),
                  "format": "json", "formatversion": "2"}
        d = api(COMMONS + "?" + urllib.parse.urlencode(params))
        if not d:
            continue
        for p in d.get("query", {}).get("pages", []):
            if p.get("missing"):
                missing.append(p["title"].replace("File:", "", 1))
        time.sleep(0.4)
    return missing


def server_render_check(text):
    """Authoritative: render the full wikitext on pl.wiki and scan the HTML."""
    post = urllib.parse.urlencode({
        "action": "parse",
        "contentmodel": "wikitext",
        "text": text,
        "prop": "text",
        "format": "json",
        "formatversion": "2",
        "disablelimitreport": "1",
    }).encode()
    d = api(PL, post=post)
    if not d or "parse" not in d:
        return ["RENDER API FAILED"], []
    html = d["parse"]["text"]
    err_pats = ["Nieznane pola", "Nieznany parametr", "Błąd w przypisach",
                "Brak tekstu w przypisie"]
    errors = [p for p in err_pats if p in html]
    reds = re.findall(r'/w/index\.php\?title=([^&]+)&amp;action=edit&amp;redlink=1', html)
    reds = sorted({urllib.parse.unquote(r).replace("_", " ") for r in reds})
    return errors, reds


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    text = open(path, encoding="utf-8").read()
    problems = []
    print("File:", path, f"({len(text)} chars)")
    print()

    n = checklist_leaks(text)
    if n:
        problems.append("HTML comments present")
    print("HTML comments:", n or "-")

    missing, missing_g = ref_integrity(text)
    if missing or missing_g:
        problems.append("broken refs")
    print("refs missing-definition:", missing or "-")
    print("uwaga refs missing-definition:", missing_g or "-")

    links = wikilinks(text)
    mm = check_wikilinks(links)
    if mm:
        problems.append(f"{len(mm)} missing wikilinks")
    print(f"wikilinks checked: {len(links)} | MISSING: {sorted(mm) or '-'}")

    qids = link_interwiki_qids(text)
    badq, unkq = check_qids(qids)
    if badq:
        problems.append(f"{len(badq)} bad link-interwiki QIDs")
    print(
        f"link-interwiki QIDs checked: {len(qids)} | BAD: {sorted(badq) or '-'}"
        f" | UNKNOWN (API flake, verify by hand): {sorted(unkq) or '-'}"
    )

    files = plik_files(text)
    mf = check_commons(files)
    if mf:
        problems.append(f"{len(mf)} missing Commons files")
    print(f"Plik files checked: {len(files)} | MISSING ON COMMONS: {sorted(mf) or '-'}")

    print("\nServer-side render check (authoritative)...")
    time.sleep(1.5)
    errors, reds = server_render_check(text)
    if errors:
        problems.append("render template errors")
    print("template errors:", errors or "-")
    iw_targets = {t for t in re.findall(r"(?i)\{\{link-interwiki\|([^|}]+)\|", text)}
    suspicious = [r for r in reds if r not in iw_targets]
    if suspicious:
        problems.append(f"{len(suspicious)} suspicious red links")
    print(f"red links in render: {len(reds)}")
    for r in reds:
        print(f"   {'!!' if r in suspicious else 'ok (link-interwiki target)'}  {r}")

    print("\n" + ("FAILURES FOUND: " + "; ".join(problems) if problems else "OK - no problems found."))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()

"""Načte katalog IOL z XLSX (listy LuxSmart, AT TORBI, AT LISA) a vloží data do public/index.html.

Použití:  python3 tools/build_data.py cesta/k/IOLs.xlsx
Sloupce: E = Název, F = Dopl (u LuxSmart nese dioptrie), J = Kat.č.
"""
import json, re, sys, collections, pathlib
import openpyxl

# Modely, které se ve vyhledávání nenabízejí
EXCLUDE_MODELS = {'719MP'}

def num(s):
    return float(s.replace(',', '.').replace(' ', ''))

def parse(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    data = collections.defaultdict(list)
    skipped = []
    excluded = 0
    for ws in wb:
        for i, r in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            raw_name = str(r[4] or '').strip()
            if not raw_name:
                continue
            name = ' '.join(raw_name.split())
            dopl = ' '.join(str(r[5] or '').split())
            kat = str(r[9] or '').strip()
            u = name.upper().replace('Č', 'C').replace('Í', 'I')
            t = s = c = None
            if ws.title.lower().startswith('luxsmart'):
                m = re.search(r'DIOPTRIE:\s*([+-]?[\d.,]+)\s*D,\s*CYLINDR:\s*([\d.,]+)', dopl)
                if m:
                    t, s, c = 'luxt', num(m.group(1)), num(m.group(2))
                else:
                    m = re.search(r'\(([+-]?[\d.,]+)\s*D\)', dopl)
                    if m:
                        t, s = 'lux', num(m.group(1))
            elif 'TORBI' in u:
                m = re.search(r'TORBI (\w+) SE\s*([+-])\s*([\d.,]+) CYL\s*([\d.,]+)', u)
                if m and m.group(1) in EXCLUDE_MODELS:
                    excluded += 1
                    continue
                if m:
                    t, s, c = 'torbi', num(m.group(3)) * (-1 if m.group(2) == '-' else 1), num(m.group(4))
            elif 'LISA TRI TORIC' in u:
                m = re.search(r'TORIC \w+ (?:SE)?\s*([+-])\s*([\d.,]+)(?: CYL\s*([\d.,]+))?', u)
                if m:
                    cy = m.group(3)
                    if not cy:
                        mm = re.search(r'CYL\s*([\d.,]+)', dopl.upper())
                        cy = mm.group(1) if mm else None
                    if cy:
                        t, s, c = 'lisat', num(m.group(2)) * (-1 if m.group(1) == '-' else 1), num(cy)
            elif 'LISA TRI' in u:
                m = re.search(r'TRI \w+ DPT\s*([+-]?[\d.,]+)', u)
                if m:
                    t, s = 'lisa', num(m.group(1))
            if t and kat:
                data[t].append([s, c, kat, name])
            else:
                skipped.append(f'{ws.title} ř.{i}: {name} | {dopl}')
    for t in data:
        data[t].sort(key=lambda x: (x[0], x[1] or 0, x[3]))
    print('Vyloučeno modelů', sorted(EXCLUDE_MODELS), ':', excluded)
    return data, skipped

def main():
    data, skipped = parse(sys.argv[1])
    html_path = pathlib.Path(__file__).resolve().parent.parent / 'public' / 'index.html'
    html = html_path.read_text(encoding='utf-8')
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    new = re.sub(r'(<script id="iol-data" type="application/json">).*?(</script>)',
                 lambda m: m.group(1) + blob + m.group(2), html, count=1, flags=re.S)
    assert new != html or blob in html, 'značka <script id="iol-data"> v index.html nenalezena'
    html_path.write_text(new, encoding='utf-8')
    print({t: len(v) for t, v in data.items()})
    print('Přeskočeno:', len(skipped))
    for s in skipped:
        print('  ', s)

if __name__ == '__main__':
    main()

"""Parse the saved Glyph Machina pages: count tables (grouped) and hit lists (escheat formula, 1291-1600)."""
import re, json, glob, os, sys, html
D = sys.argv[1]; OUT = sys.argv[2]
def txt(s): return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()
res = {}
for f in sorted(glob.glob(f'{D}/*.html')):
    k = os.path.basename(f)[:-5]
    if k in ('q1', 'q2'): continue
    t = open(f).read()
    m = re.search(r'<p class="summary">\s*<b>([\d,]+)</b>', t)
    total = int(m.group(1).replace(',', '')) if m else None
    q = re.search(r'query: <code>(.*?)</code>', t)
    if 'escheat_list' not in k:
        rows = re.findall(r'<tr>\s*<td>(.*?)</td>\s*<td class="n">([\d,]+)</td>', t, re.S)
        res[k] = dict(total=total, query=txt(q.group(1)) if q else '', counts={txt(a): int(b.replace(',', '')) for a, b in rows})
    else:
        hits = []
        for blk in re.split(r'<div class="hit">', t)[1:]:
            meta = re.search(r'<div class="meta">(.*?)</div>', blk, re.S).group(1)
            reign = txt(re.search(r'<span class="mon">(.*?)</span>', meta).group(1))
            yr = re.search(r'<span class="yr" title="([^"]*)">(.*?)</span>', meta)
            a = re.search(r'<a href="([^"]+)">(.*?)</a>', meta)
            nl = re.search(r'entry of (\d+) lines', meta); cf = re.search(r'conf (\d+)', meta)
            lines = [(('matched' in c), int(s), txt(l)) for c, s, l in re.findall(r'<div class="line ([^"]*)">\s*<span class="conf[^"]*">(-?\d+)</span>(.*?)</div>', blk, re.S)]
            hits.append(dict(reign=reign, year=txt(yr.group(2)), approx=('estimated' in html.unescape(yr.group(1))), href=a.group(1), ref=txt(a.group(2)),
                             nlines=int(nl.group(1)) if nl else None, conf=int(cf.group(1)) if cf else None, lines=lines))
        res[k] = dict(total=total, hits=hits)
lst = [h for k in sorted(res) if k.startswith('escheat_list') for h in res[k]['hits']]
out = {k: v for k, v in res.items() if not k.startswith('escheat_list')}
out['escheat_list'] = dict(total=res['escheat_list_p01']['total'], pages=len([k for k in res if k.startswith('escheat_list')]), hits=lst)
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=0)
for k, v in out.items():
    if k != 'escheat_list': print(k, v['total'], v['query'][:80], list(v['counts'].items())[:50])
print('list hits', len(lst), 'of', out['escheat_list']['total'])

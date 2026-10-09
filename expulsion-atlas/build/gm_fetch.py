"""Glyph Machina queries for the Expulsion atlas. Robots file disallows crawlers, so the run is small
(about 25 queries in all, 15 s apart) and every query is logged with its URL."""
import json, time, urllib.request, urllib.parse, os, sys
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (academic research; low volume; Expulsion atlas)'}
BASE = 'https://glyphmachina.utsc.utoronto.ca/'
IUD = 'iudeus iudei iudeorum iudeo iudea iudee iudeis iudeum'
Q = [
 # key, q, mode, group, extra params
 ('baseline_decade', IUD, 'or', 'decade', {}),
 ('baseline_series', IUD, 'or', 'series', {}),
 ('escheat_decade', 'NEAR(fuerunt iudei, 4)', 'raw', 'decade', {}),
 ('escheat_series', 'NEAR(fuerunt iudei, 4)', 'raw', 'series', {}),
 ('debita_decade', '"debita iudeorum" OR "debitis iudeorum" OR "debitorum iudeorum"', 'raw', 'decade', {}),
 ('archa_decade', 'NEAR(archa* iudeorum, 3) OR "archa cirographorum" OR "archam cirographorum" OR "arche cirographorum"', 'raw', 'decade', {}),
 ('exile_decade', 'NEAR(exilium iudeorum, 8) OR NEAR(exilium iudei, 8) OR NEAR(exilium iudeis, 8)', 'raw', 'decade', {}),
 ('conversorum_series', 'domus conversorum', 'phrase', 'series', {}),
 ('iudaismus_decade', 'iudaism*', 'raw', 'decade', {}),
] + [(f'escheat_list_p{p:02d}', 'NEAR(fuerunt iudei, 4)', 'raw', '', {'yfrom': '1291', 'yto': '1600', 'page': str(p)}) for p in range(2, 16)]
log = []
for i, (k, q, mode, group, ex) in enumerate(Q):
    fn = f'{OUT}/{k}.html'
    p = {'q': q, 'extra': '', 'mode': mode, 'formula': '', 'mfrom': '', 'mto': '', 'series': '', 'yfrom': '', 'yto': '', 'minconf': '', 'order': 'chrono', 'group': group}
    p.update(ex)
    url = BASE + '?' + urllib.parse.urlencode(p)
    if not os.path.exists(fn):
        if i: time.sleep(15)
        try:
            t = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read().decode('utf-8', 'replace')
            open(fn, 'w').write(t)
        except Exception as e:
            print(k, 'ERROR', e, flush=True); log.append(dict(key=k, url=url, error=str(e))); continue
    log.append(dict(key=k, q=q, mode=mode, group=group, extra=ex, url=url, fetched=time.strftime('%Y-%m-%d %H:%M')))
    print(k, 'ok', flush=True)
json.dump(log, open(f'{OUT}/_log.json', 'w'), indent=1)
print('DONE')

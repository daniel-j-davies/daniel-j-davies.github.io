"""TNA Discovery API (open to automated use; catalogue text under OGL v3.0). Splits date ranges to stay under 100 results a page."""
import json, time, urllib.request, urllib.parse, sys
OUT = sys.argv[1]
UA = {'User-Agent': 'ExpulsionAtlasResearch/1.0 (academic; low volume)', 'Accept': 'application/json'}
def q(term, series, a, b):
    p = {'sps.searchQuery': term, 'sps.recordSeries': series, 'sps.dateFrom': f'{a}-01-01', 'sps.dateTo': f'{b}-12-31', 'sps.resultsPageSize': 100, 'sps.sortByOption': 'DATE_ASCENDING'}
    d = json.load(urllib.request.urlopen(urllib.request.Request('https://discovery.nationalarchives.gov.uk/API/search/records?' + urllib.parse.urlencode(p), headers=UA), timeout=90))
    return d['count'], d['records']
def run(term, series, a0, b0, out):
    recs = {}; stack = [(a0, b0)]
    while stack:
        a, b = stack.pop(0)
        n, r = q(term, series, a, b); time.sleep(4)
        if n > 100 and b > a:
            m = (a + b) // 2; stack += [(a, m), (m + 1, b)]; continue
        for x in r: recs[x['id']] = x
    json.dump(list(recs.values()), open(f'{OUT}/{out}', 'w'), ensure_ascii=False, indent=0)
    print(term, series, len(recs), flush=True)
JOBS = [('Jews', 'E 101', 1150, 1560, 'e101_jews.json'),
        ('converts', 'E 101', 1230, 1610, 'e101_converts.json'),
        ('Jews OR Jew OR Jewry', 'SC 8', 1200, 1500, 'sc8_jews.json'),
        ('converts OR convert', 'SC 8', 1230, 1500, 'sc8_converts.json'),
        ('Jews OR Jew', 'SC 1', 1200, 1500, 'sc1_jews.json'),
        ('*', 'E 9', 1200, 1320, 'e9_all.json'),
        ('Jews OR Jew OR Jewry', 'C 47', 1200, 1500, 'c47_jews.json'),
        ('Jews OR Jew OR converts', 'E 401', 1200, 1500, 'e401_jews.json')]
for j in JOBS:
    try: run(*j)
    except Exception as e: print(j[0], j[1], 'ERROR', e, flush=True)
    time.sleep(5)
print('DONE')

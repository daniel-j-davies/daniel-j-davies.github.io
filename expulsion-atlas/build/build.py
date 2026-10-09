"""Assemble data/atlas.json for the Expulsion atlas.

Run from the atlas folder:  python3 build/build.py
Inputs (all in build/src/): Glyph Machina result pages (gm/), TNA Discovery records (tna/), the Patent Roll
entries that name Jews, the Jewry or the converts (cpr/cpr_jews.json, from cpr_jews.py), and the hand-entered
records in build/curated.py.
"""
import json, re, os, sys, subprocess, html, importlib.util
from collections import Counter, defaultdict

B = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(B); S = f'{B}/src'
spec = importlib.util.spec_from_file_location('curated', f'{B}/curated.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

# ------------------------------------------------------------------ Glyph Machina
subprocess.run([sys.executable, '-I', f'{B}/gm_parse.py', f'{S}/gm', f'{S}/gm_parsed.json'], check=True, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, '-I', f'{B}/gm_tag.py', f'{S}/gm_parsed.json', f'{S}/gm_tagged.json'], check=True, stdout=subprocess.DEVNULL)
GP = json.load(open(f'{S}/gm_parsed.json')); GT = json.load(open(f'{S}/gm_tagged.json'))
LOG = {q['key']: q for q in json.load(open(f'{S}/gm/query_log.json'))}
GMBASE = 'https://glyphmachina.utsc.utoronto.ca'
def gmurl(key, q, mode, group, extra=None):
    if key in LOG: return LOG[key]['url']
    import urllib.parse
    p = {'q': q, 'extra': '', 'mode': mode, 'formula': '', 'mfrom': '', 'mto': '', 'series': '', 'yfrom': '', 'yto': '', 'minconf': '', 'order': 'chrono', 'group': group}
    if extra: p.update(extra)
    return GMBASE + '/?' + urllib.parse.urlencode(p)
FORMULAE = [  # key in GP, label, gloss, type
    ('archa_decade', 'archa … iudeorum', 'the chests of chirographs', 'bonds'),
    ('debita_decade', 'debita iudeorum', 'debts of the Jews', 'bonds'),
    ('escheat_decade', 'que fuerunt … iudei', 'houses or rents that were a Jew’s', 'property'),
    ('exile_decade', 'per exilium iudeorum', 'by the exile of the Jews', 'property'),
    ('domus_conversorum_decade', 'domus conversorum', 'the House of Converts', 'domus'),
]
gm_series = []
for k, lab, gloss, t in FORMULAE:
    g = GP[k]
    url = gmurl(k, 'domus conversorum', 'phrase', 'decade') if k == 'domus_conversorum_decade' else LOG[k]['url']
    gm_series.append(dict(key=k, label=lab, gloss=gloss, type=t, total=g['total'], query=g['query'], url=url,
                          decades={int(d): n for d, n in g['counts'].items() if d.isdigit()}))
gm_other = {k: dict(total=GP[k]['total'], query=GP[k]['query'], url=LOG[k]['url'], counts=GP[k]['counts'])
            for k in ['baseline_decade', 'baseline_series', 'escheat_series', 'conversorum_series', 'iudaismus_decade']}
gm_log = [dict(key=q['key'], q=q['q'], mode=q['mode'], group=q['group'], extra=q.get('extra') or {}, url=q['url'], fetched=q.get('fetched', '')) for q in LOG.values()]
gm_log.insert(0, dict(key='domus_conversorum_decade', q='domus conversorum', mode='phrase', group='decade', extra={}, url=gmurl('x', 'domus conversorum', 'phrase', 'decade'), fetched='2026-10-08'))
gm_log.insert(1, dict(key='escheat_list_p01', q='NEAR(fuerunt iudei, 4)', mode='raw', group='', extra={'yfrom': '1291', 'yto': '1600'}, url=gmurl('x', 'NEAR(fuerunt iudei, 4)', 'raw', '', {'yfrom': '1291', 'yto': '1600'}), fetched='2026-10-08'))
gm_log.append(dict(key='baseline_check_cp40_1330s', q='iudeus iudei iudeorum iudeo iudea iudee iudeis iudeum', mode='or', group='', extra={'series': 'CP40', 'yfrom': '1330', 'yto': '1339'},
                   url=gmurl('x', 'iudeus iudei iudeorum iudeo iudea iudee iudeis iudeum', 'or', '', {'series': 'CP40', 'yfrom': '1330', 'yto': '1339'}), fetched='2026-10-08'))

TOWNKEY = {'London': 'london', 'Lincoln': 'lincoln', 'Bristol': 'bristol', 'Oxford': 'oxford', 'Exeter': 'exeter', 'Cambridge': 'cambridge',
           'Winchester': 'winchester', 'York': 'york', 'Northampton': 'northampton', 'Canterbury': 'canterbury', 'Stamford': 'stamford',
           'Norwich': 'norwich', 'Ipswich': 'ipswich', 'Hereford': 'hereford', 'Devizes': 'devizes', 'Colchester': 'colchester', 'Gloucester': 'gloucester'}
def gmref(r): return 'Glyph Machina, ' + r
def clean_line(l): return re.sub(r'^\s*¶\s*', '', re.sub(r'\s+', ' ', l)).strip()

records = []
def rec(**k):
    k.setdefault('town', None); k.setdefault('url', None); k.setdefault('quote', ''); records.append(k); return k

esc_hits = []
KEEP_UNTAGGED = {  # read by hand: Jewish former owner, place not in the matched lines
    'E368 roll 75 fronts, image 0757': (None, 'Goods and chattels that were Saulot son of Samuel’s, a Jew'),
    'E372 roll 164 dorses, image 0189': (None, 'Houses in the suburbs that were Mosse de Clare’s, a Jew'),
    'E368 roll 83 fronts, image 0205': (None, 'Tenements that were Jocei son of Benedict’s, a Jew'),
    'KB27 roll 432 fronts, image 0175': ('york', 'York title case: ‘the Jews were put into exile out of the realm of England, about ninety years since’'),
    'KB27 roll 432 dorses, image 0341': ('york', 'York title case: seisin ‘at the time when the said Jews were put into exile out of the realm of England’'),
}
GM_TITLES = {  # entries read in full for the 1290-93 view
    'E372 roll 139 dorses, image 2320': ('bristol', 'Bristol, constable’s account: houses of hanged Jews in Winchester Street and outside the castle let for less ‘because few will live there’; the cemetery that was the Jews’ let to farm; Peter Miparti’s 5s. for the houses of Jospin'),
    'E372 roll 139 fronts, image 2164': (None, 'Account of Hugh de Kendale for the houses, rents and tenements that were the Jews’ throughout England: London, Lincoln and other towns'),
    'E372 roll 139 fronts, image 2165': (None, 'Account of Hugh de Kendale for the houses, rents and tenements that were the Jews’ (continued)'),
    'E101 roll 250 other, image 0002': ('lincoln', 'Particulars of Hugh de Kendale’s sales: houses that were the Jews’ in Lincoln, except those of Hagin son of Benedict'),
    'E101 roll 250 other, image 0003': ('lincoln', 'Particulars of Hugh de Kendale’s sales (another copy)'),
    'C66 roll 112 fronts, image 0059': ('colchester', 'Grant of houses at Colchester that were Jocey son of Samuel’s and other Jews’ (the Patent Roll entry calendared in CPR 1292–1301, p. 18)'),
    'CP40 roll 122 dorses, image 0634': ('hereford', 'Houses that were Crispin’s, a Jew of Hereford, in the street called the Jews’ street (vicus Judeorum)'),
    'E368 roll 72 dorses, image 0275': ('devizes', 'The sheriff of Wiltshire to enquire into the houses that were a Jew’s at Devizes'),
    'E368 roll 72 dorses, image 0276': ('devizes', 'Yearly value of the houses that were Mosse’s, a Jew, at Devizes, ‘from the time after the exile’'),
}
for h in GT['hits']:
    if not h['town'] and not h['props'] and h['ref'] not in KEEP_UNTAGGED and h['ref'] not in GM_TITLES: continue  # read by hand: not a Jewish former owner
    t = TOWNKEY.get(h['town'])
    if h['ref'] in KEEP_UNTAGGED: t = KEEP_UNTAGGED[h['ref']][0]
    if h['ref'] in GM_TITLES and GM_TITLES[h['ref']][0]: t = GM_TITLES[h['ref']][0]
    esc_hits.append(dict(y=h['year'], approx=h['approx'], ref=h['ref'], url=GMBASE + h['href'], props=h['props'], town=t, line=clean_line(h['line'])[:300],
                         plines={k: clean_line(v)[:300] for k, v in h.get('plines', {}).items()}))
    plab = [C.PROP_META[p]['short'] for p in h['props']]
    rec(y=h['year'], date=('c. ' if h['approx'] else '') + str(h['year']), type='property', town=t, src='GM', status='db',
        title=GM_TITLES[h['ref']][1] if h['ref'] in GM_TITLES else ('Charge on ' + ' and '.join(plab)) if plab else (KEEP_UNTAGGED[h['ref']][1] if h['ref'] in KEEP_UNTAGGED else 'Houses or rents ‘that were’ a Jew’s'),
        ref=gmref(h['ref']), url=GMBASE + h['href'], quote=clean_line(h['line'])[:260])

props = []
for p in GT['props']:
    m = C.PROP_META[p['key']]
    hs = sorted([h for h in esc_hits if p['key'] in h['props'] and h['y']], key=lambda h: h['y'])
    props.append(dict(key=p['key'], label=p['label'], short=m['short'], town=TOWNKEY.get(p['town']), origin=m['origin'], origin_year=m['origin_year'],
                      origin_note=m['origin_note'], n=len(hs), first=hs[0]['y'] if hs else None, last=hs[-1]['y'] if hs else None,
                      hits=[dict(y=h['y'], ref=h['ref'], url=h['url'], line=(h['plines'].get(p['key']) or h['line'])[:220]) for h in hs]))

# ------------------------------------------------------------------ Patent Rolls
CP = json.load(open(f'{S}/cpr/cpr_jews.json'))
def norm(s): return re.sub(r'\s+', ' ', s)
missing = []
for vol, page, key, y, dl, t, town, title in C.CPR:
    cands = [e for e in CP if e['ref'] == vol and str(e['page']) == str(page) and key in e['text']]
    if not cands:
        cands = [e for e in CP if e['ref'] == vol and key in e['text']]
    if not cands: missing.append((vol, page, key)); quote = ''
    else:
        tx = norm(cands[0]['text']); i = tx.find(key); a = max(0, i - 120)
        quote = ('… ' if a else '') + tx[a:a + 330].strip() + ' …'
    rec(y=y, date=dl, type=t, town=town, src='CPR', status='src', title=title, ref=f'{vol}, p. {page}', quote=quote)
if missing: print('CPR not matched:', missing)

# ------------------------------------------------------------------ TNA catalogue
def tna(f): return json.load(open(f'{S}/tna/{f}'))
TN = {}
for f in ['e101_jews.json', 'e101_converts.json', 'sc8_jews.json', 'sc8_converts.json', 'sc1_jews.json', 'e9_all.json', 'c47_jews.json']:
    for r in tna(f):
        if r.get('reference') and r['reference'].count(' ') >= 1 and '/' in r['reference'] or r.get('reference', '').startswith('E 9/'):
            TN[r['id']] = r
EXCLUDE = {'SC 8/343/16173', 'SC 8/290/14493', 'SC 8/145/7213', 'SC 8/293/14646', 'SC 8/78/3893', 'SC 8/221/11030', 'SC 8/267/13313',
           'SC 8/336/15891', 'SC 8/264/13177', 'SC 8/2/86', 'SC 8/28/1356', 'SC 1/49/179', 'SC 1/49/125', 'SC 1/54/114', 'SC 1/18/59', 'SC 1/18/58',
           'SC 1/24/28', 'SC 1/19/4', 'SC 8/220/10975', 'C 47/35/17', 'C 47/35/10/61', 'C 47/35/10/62', 'C 47/35/10/63', 'C 47/14/6/7'}
MANUAL = {  # ref: (type, town)
    'SC 8/97/4813': ('before', 'oxford'), 'SC 8/68/3376': ('bonds', None), 'SC 8/50/2474': ('bonds', None), 'SC 8/180/8966': ('before', 'london'),
    'SC 8/34/1657': ('property', 'bristol'), 'SC 8/329/E909': ('bonds', None), 'SC 8/329/E911': ('property', 'london'), 'SC 8/268/13376': ('bonds', None),
    'SC 8/100/4974': ('property', 'cambridge'), 'SC 8/182/9072': ('bonds', None), 'SC 8/334/E1121': ('bonds', 'lincoln'), 'SC 8/334/E1145': ('bonds', 'lincoln'),
    'SC 8/16/772': ('bonds', 'cricklade'), 'SC 8/127/6326': ('bonds', None), 'SC 8/67/3303': ('property', 'oxford'), 'SC 1/27/35': ('property', 'london'),
    'C 47/41/190': ('name', 'london'), 'SC 1/26/28': ('before', None), 'SC 8/279/13929': ('domus', None),
}
COUNTY = [('Devonshire', 'exeter'), ('Norfolk', 'norwich'), ('Huntingdon and Cambridge', 'cambridge'), ('Hampshire', 'winchester'), ('Kent', 'canterbury'),
          ('Wiltshire', 'devizes'), ('county of Gloucester', 'gloucester'), ('county of Hereford', 'hereford'), ('county of Lincoln', 'lincoln'),
          ('county of Oxford', 'oxford'), ('county of Nottingham', 'nottingham'), ('Rutland', 'rutland')]
TOWNRX = [(k, re.compile(r'\b' + v + r'\b')) for k, v in [('london', 'London|Westminster|Tower of London'), ('york', 'York'), ('lincoln', 'Lincoln'), ('norwich', 'Norwich'),
          ('winchester', 'Winchester'), ('oxford', 'Oxford'), ('cambridge', 'Cambridge'), ('canterbury', 'Canterbury'), ('bristol', 'Bristol'), ('gloucester', 'Gloucester'),
          ('hereford', 'Hereford'), ('worcester', 'Worcester'), ('exeter', 'Exeter'), ('northampton', 'Northampton'), ('nottingham', 'Nottingham|Notts'),
          ('stamford', 'Stamford'), ('colchester', 'Colchester'), ('bedford', 'Bedford'), ('marlborough', 'Marlborough'), ('warwick', 'Warwick'),
          ('bridgnorth', 'Bridgnorth'), ('cricklade', 'Cricklade|Crekelade')]]
def tna_type(ref, d, y):
    if ref in MANUAL: return MANUAL[ref][0]
    dl = d.lower()
    if ref.startswith('E 9'): return 'before'
    if 'conver' in dl or 'keeper' in dl: return 'domus'
    if re.search(r'concealment|condemned|clipping', dl): return 'condemned'
    if re.search(r'starr|chest|archa|chirograph|obligation|debts|bond', dl): return 'bonds'
    if re.search(r'possessions|houses|land of jews|sale', dl): return 'property'
    if 'apostate' in dl: return 'domus'
    return 'before'
def tna_town(ref, d, t):
    if ref in MANUAL: return MANUAL[ref][1]
    if t == 'domus': return 'london'
    if ref.startswith('E 101/250/') and 'obligations and charters' in d:
        for k, v in COUNTY:
            if k in d: return v
    for k, rx in TOWNRX:
        if rx.search(d): return k
    return None
def tna_title(ref, d):
    d = re.sub(r'\s+', ' ', d).strip()
    m = re.search(r'Nature of request:\s*(.*?)(?:Nature of endorsement:|$)', d)
    if ref.startswith('SC 8') and m:
        pet = re.search(r'Petitioners:\s*(.*?)\.\s', d)
        return (pet.group(1) + ': ' if pet else '') + m.group(1).strip()
    return d
tna_recs = []; e9_years = Counter(); keeper_acc = []
for r in TN.values():
    ref = r['reference']
    if ref in EXCLUDE or ref in ('E 101', 'E 9'): continue
    d = html.unescape(re.sub(r'<[^>]+>', '', r.get('description') or ''))
    ys = r.get('numStartDate'); ye = r.get('numEndDate')
    y0 = int(str(ys)[:4]) if ys else None; y1 = int(str(ye)[:4]) if ye else y0
    if y0 is None: continue
    if ref.startswith('SC 1') and ref not in MANUAL and y0 > 1292: continue
    if ref.startswith('SC 8') and ref not in MANUAL and y0 >= 1290 and not re.search(r'onver', d): continue
    t = tna_type(ref, d, y0); town = tna_town(ref, d, t)
    if ref.startswith('E 9/'): e9_years[y0] += 1
    m = re.search(r'account of (?:Sir |the )?(.+?),? (?:keeper|collector)', d)
    if t == 'domus' and m and ref.startswith('E 101'):
        keeper_acc.append(dict(name=m.group(1).replace(' (by his executors)', '').strip(), y0=y0, y1=y1, ref=ref, id=r['id']))
    title = tna_title(ref, d)
    tna_recs.append(dict(ref=ref, id=r['id'], y=y0, y1=y1, dates=r.get('coveringDates', ''), type=t, town=town, desc=title[:600]))
    rec(y=y0, date=r.get('coveringDates', str(y0)), type=t, town=town, src='TNA', status='db', title=title[:240] + ('…' if len(title) > 240 else ''),
        ref=f'TNA {ref}', url=f'https://discovery.nationalarchives.gov.uk/details/r/{r["id"]}')

# ------------------------------------------------------------------ keepers of the Domus: TNA accounts + Patent Roll appointments
ALIAS = {'Richard de Ayrmynne': 'Richard de Ayremynne', 'John de Sancto Paulo': 'John de St Paul', 'John de Sancto Dionisio': 'John de St Denis',
         'Thomas Kyrkeby': 'Thomas Kirkeby', 'John Alcok': 'John Alcock', 'Christopher Halys': 'Christopher Hales', 'Chr. Hales': 'Christopher Hales',
         'Thomas Crumwell': 'Thomas Cromwell', 'John, bishop of Salisbury': 'John Waltham, bishop of Salisbury', 'Robert Bowis': 'Robert Bowes',
         'William Cordall': 'William Cordell', 'Christopher Baynbrigg': 'Christopher Bainbridge', 'John Wakeryng': 'John Wakering'}
for k in keeper_acc: k['name'] = ALIAS.get(k['name'], k['name'])
K = defaultdict(lambda: dict(y0=9999, y1=0, refs=[]))
for k in keeper_acc:
    if k['name'].startswith('John James'): continue  # collector of rents, not keeper
    e = K[k['name']]; e['y0'] = min(e['y0'], k['y0']); e['y1'] = max(e['y1'], k['y1']); e['refs'].append('TNA ' + k['ref'])
for n, y, ref in C.KEEPERS_CPR:
    e = K[n]; e['y0'] = min(e['y0'], y); e['y1'] = max(e['y1'], y); e['refs'].append(ref)
keepers = sorted([dict(name=n, y0=v['y0'], y1=v['y1'], refs=sorted(set(v['refs']))) for n, v in K.items()], key=lambda x: (x['y0'], x['y1']))
for i, k in enumerate(keepers):  # an appointment with no account runs to the next keeper's first date
    nxt = next((x['y0'] for x in keepers[i + 1:] if x['y0'] > k['y0']), k['y1'] + 1)
    k['to'] = max(k['y1'], min(nxt, k['y0'] + 25)) if k['y1'] == k['y0'] else k['y1']

# ------------------------------------------------------------------ events, earlier sweep, places
events = []
for y, mo, d, lab, det, t, town, st, ref in C.EVENTS:
    events.append(dict(y=y, m=mo, d=d, label=lab, detail=det, type=t, town=town, status=st, ref=ref))
    if re.match(r'(CPR|TNA|Glyph)', ref): continue  # the record itself is already in the catalogue
    rec(y=y, date=f'{d} ' if d else '', type=t, town=town, src='Event', status=st, title=lab + '. ' + det, ref=ref)
for r in records:
    if r['src'] == 'Event':
        e = next(x for x in events if r['title'].startswith(x['label']))
        r['date'] = (f"{e['d']} " if e['d'] else '') + (['', 'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.'][e['m']] + ' ' if e['m'] else '') + str(e['y'])

def rkey(s):
    m = re.match(r'(\w+?)\s*roll\s*(\w+)', s); im = re.search(r'image[s]?\s*(\d{4})', s)
    return (m.group(1).upper(), m.group(2), im.group(1) if im else None) if m else None
hitkeys = {}
for h in GT['hits']:
    k = rkey(h['ref'])
    if k: hitkeys.setdefault(k, h); hitkeys.setdefault(k[:2] + (None,), h)
prior = []
for y, t, town, summ, ref, q in C.PRIOR:
    k = rkey(ref); h = hitkeys.get(k) if k else None
    if not h and k and k[2] is None: h = hitkeys.get(k)
    st = 'db' if h else 'verify'
    prior.append(dict(y=y, type=t, town=town, title=summ, ref=ref, quote=q, status=st, matched=(GMBASE + h['href']) if h else None, matched_ref=h['ref'] if h else None))
    rec(y=y or (h['year'] if h else None), date=str(y or (h['year'] if h else 'Undated')), type=t, town=town, src='Sweep', status=st, title=summ,
        ref=gmref(ref) + (' (matched to a hit read for this atlas)' if h else ' (earlier sweep, not re-read)'), url=(GMBASE + h['href']) if h else None, quote=q)

# ------------------------------------------------------------------ the map: what each town has, by type and date
towns = {k: dict(name=v[0], ll=[v[2], v[1]]) for k, v in C.TOWNS.items()}
used = Counter(r['town'] for r in records if r['town'])
towns = {k: v for k, v in towns.items() if used[k]}

records.sort(key=lambda r: (r['y'] is None, r['y'] or 0, r['src'], r['title']))
for i, r in enumerate(records): r['id'] = i

atlas = dict(
    built='8 October 2026',
    types=[dict(key=k, label=l, color=c) for k, l, c in C.TYPES],
    origins=[dict(key=k, label=l) for k, l in C.ORIGINS],
    towns=towns, records=records, events=events, props=props,
    gm_series=gm_series, gm_other=gm_other, gm_log=gm_log, gm_counts=dict(escheat_list_total=GP['escheat_list']['total'], tagged=sum(1 for h in esc_hits)),
    keepers=keepers, residents=[dict(n=n, name=nm, y0=a, y1=b, sex=s, note=nt) for n, nm, a, b, s, nt in C.RESIDENTS], residents_note=C.RESIDENTS_NOTE,
    e9_years=dict(sorted(e9_years.items())), tna_count=len(tna_recs), cpr_count=len(C.CPR), cpr_candidates=len(CP),
    prior=prior, flags=[dict(title=a, text=b) for a, b in C.FLAGS],
)
os.makedirs(f'{ROOT}/data', exist_ok=True)
json.dump(atlas, open(f'{ROOT}/data/atlas.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('records', len(records), Counter(r['src'] for r in records), Counter(r['type'] for r in records))
print('towns', len(towns), 'keepers', len(keepers), 'props', [(p['short'], p['n'], p['first'], p['last']) for p in props])
print('prior matched', sum(1 for p in prior if p['status'] == 'db'), 'of', len(prior))
print('size', os.path.getsize(f'{ROOT}/data/atlas.json'))

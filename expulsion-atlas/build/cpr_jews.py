"""Split every Calendar of Patent Rolls volume into entries (adapted from the merchant atlas's cpr_entries.py,
extended to 1281-1300 and to all years), then keep entries that name Jews, the Jewry or the House of Converts."""
import json, re, glob, os, bisect, sys
W = sys.argv[1]
def norm(t): t = re.sub(r'-\s*\n\s*', '', t); return re.sub(r'\s+', ' ', t)
KW = (r"Commission|Licence|Grant|Pardon|Protection|Appointment|Mandate|Writ|Revocation|Exemption|Inspeximus|Presentation|Ratification|Confirmation|"
      r"Safe-conduct|Safe conduct|Order|Notification|Letters|Signification|Simple protection|Restitution|Release|Respite|Acquittance|Commitment|Power|"
      r"Assignment|Indemnity|Exoneration|Promise|Declaration|Request|Charter|Precept|Cancellation|Discharge|Whereas|Acceptance|Exemplification|Vidimus|"
      r"General pardon|Special pardon|Nomination|Mainprise|Gift|Lease|Demise|Admission|Ratification|Enrolment|Ordinance|Restoration|Remission")
START = re.compile(r"(?:(?<=\. )|(?<=\] )|(?<=\d\. )|(?<=\.\) ))(?=(?:" + KW + r")\b)")
def is_index(t): return len(re.findall(r'\bSee [A-Z]', t)) >= 6 or len(re.findall(r', \d{1,3}(?:, \d{1,3}){3,}', t)) >= 6
def span(vol):
    m = re.search(r'(\d{4})-(\d{2,4})', vol); a = int(m.group(1)); b = m.group(2)
    return a, (int(b) if len(b) == 4 else int(m.group(1)[:2] + b))
def label(vol):
    a, b = span(vol); bb = str(b)[-2:] if str(b)[:2] == str(a)[:2] else str(b)
    return f'CPR {a}–{bb}'
out = []
for f in sorted(glob.glob(f'{W}/srctext/cpr_*.jsonl')):
    vol = os.path.basename(f)[:-6].replace('_search', '')
    y0, y1 = span(vol)
    stream = ''; offs = []; year = y0
    for l in open(f):
        r = json.loads(l); t = norm(r['t'])
        if is_index(t): continue
        ys = [int(x) for x in re.findall(r'\b1[2-5]\d\d\b', t[:260]) if y0 - 1 <= int(x) <= y1 + 1]
        if ys: year = ys[0]
        offs.append((len(stream), r['p'], year)); stream += t + ' '
    starts = [o[0] for o in offs]
    cuts = [m.start() for m in START.finditer(stream)] + [len(stream)]
    for a, b in zip(cuts, cuts[1:]):
        txt = stream[a:b].strip()
        if len(txt) < 40: continue
        k = bisect.bisect_right(starts, a) - 1; _, page, yr = offs[max(0, k)]
        out.append(dict(vol=vol, ref=label(vol), page=page, year=yr, text=txt[:4000]))
print(len(out), 'entries')
PAT = re.compile(r"\bJew(?:s|ess|esses|ry|erie|ish)?\b|\bJudaism|\bconverts?\b|\bconversi\b|\bconversorum\b|converted Jew|House of (?:the )?Converts|domus conversorum|\bexile of the Jews|\bJudei|\bJudeus", re.I)
hits = [e for e in out if PAT.search(e['text'])]
for e in hits: e['terms'] = sorted(set(m.group(0).lower() for m in PAT.finditer(e['text'])))
json.dump(hits, open(f'{W}/cpr_jews.json', 'w'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(hits), 'hits')
print(Counter(e['ref'] for e in hits).most_common())
print(Counter(t for e in hits for t in e['terms']).most_common(30))

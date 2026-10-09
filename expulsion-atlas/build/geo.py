"""Make data/geo.json: simplified land (England, Wales, Scotland, Ireland, Man, and the near Continent) and
England's larger rivers, from Natural Earth 10m (public domain).
Usage: python3 build/geo.py <folder with the Natural Earth geojson files>"""
import json, sys, os
sys.setrecursionlimit(20000)
NE = sys.argv[1]; ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOX = (-8.6, 49.4, 4.6, 56.2)
def rdp(pts, eps):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]; dx, dy = b[0] - a[0], b[1] - a[1]; L = (dx * dx + dy * dy) ** .5 or 1e-12
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        p = pts[i]; d = abs(dy * p[0] - dx * p[1] + b[0] * a[1] - b[1] * a[0]) / L
        if d > dmax: dmax, idx = d, i
    if dmax > eps: return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [a, b]
def inbox(ring): return any(BOX[0] <= x <= BOX[2] and BOX[1] <= y <= BOX[3] for x, y in ring)
def simp(ring, eps):
    h = len(ring) // 2  # a closed ring: simplify the two halves separately
    r = rdp(ring[:h + 1], eps)[:-1] + rdp(ring[h:], eps); return [[round(x, 3), round(y, 3)] for x, y in r] if len(r) >= 4 else None
land = []
for f in json.load(open(f'{NE}/ne_10m_admin_0_map_subunits.geojson'))['features']:
    su = f['properties'].get('SU_A3')
    if su not in ('ENG', 'WLS', 'SCT', 'NIR', 'IRL', 'IMN', 'FXX', 'BFR', 'BWR', 'BCR', 'NLX'): continue
    g = f['geometry']; polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    out = []
    for poly in polys:
        if not inbox(poly[0]): continue
        r = simp(poly[0], 0.006 if su in ('ENG', 'WLS') else 0.012)
        if r: out.append([r])
    if out: land.append(dict(id=su, eng=su in ('ENG', 'WLS'), polys=out))
rivers = []
for f in json.load(open(f'{NE}/ne_10m_rivers_europe.geojson'))['features']:
    g = f['geometry']; lines = g['coordinates'] if g['type'] == 'MultiLineString' else [g['coordinates']]
    for l in lines:
        if all(BOX[0] <= x <= 2.0 and 50.0 <= y <= 55.9 for x, y in l):
            r = rdp(l, 0.004)
            if len(r) >= 2: rivers.append(dict(name=f['properties'].get('name') or '', line=[[round(x, 3), round(y, 3)] for x, y in r]))
json.dump(dict(land=land, rivers=rivers), open(f'{ROOT}/data/geo.json', 'w'), separators=(',', ':'))
print(len(land), 'land units', sum(len(u['polys']) for u in land), 'polygons;', len(rivers), 'river lines;', os.path.getsize(f'{ROOT}/data/geo.json'), 'bytes')

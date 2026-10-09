"""Tag each Glyph Machina escheat-formula hit (1291-1600) with the property it charges, where the HTR text allows,
and otherwise with a town. Patterns allow for the recurrent HTR misreadings seen in the hit list (e.g. Bristoll as
Cristoll/Tristoll/Bustoll; Bonefey as Ronefey/Tonesey/Gonesey). Untagged hits are listed for reading by hand."""
import json, re, sys
G = json.load(open(sys.argv[1])); OUT = sys.argv[2]
hits = G['escheat_list']['hits']
BRI = r'(?:[BCTROUDSHEPVWb]r?[iu]?[sn]?[tc]?[oe]?l+a?|Bri[sc]to|Bristol|stoll|stell|stol\b|Brastell|Brifella|Dystell|Rystol)'
PROPS = [
 ('bri_bonefey', 'Bristol: houses and rents of Bonefey, farmed by Henry le Waleys (12d.)', 'Bristol',
  r'(le (?:Wal|Wel|Bal|Witl|Walye|Ebal)|Banastre|(?:[BRTGCEVDSb]o?n|[BRT]ov|[BR]onf|one )[eo]?[fs]e?[eiyt]+[ry]?\s+iude|[BRG]on[fs]ey|Bonesty|bonesdi|bonese\b|Rouese|Romsey|Ronfey|Gonfey|super pontem)'),
 ('bri_jospin', 'Bristol: houses of Jospin (Joce) of Bristol in Winchester Street, held by Peter Miparty (5s.)', 'Bristol',
  r'([jJiIrRtTcoe]?[eo]?sp[iu]?m?[iu]?[mt]?[iu]?\s+de\s+\S*st[oe]l|[eo]sp\w*\s+de\s+[BOTRSCU]\w*|Iosoii|Jostin|osprimi|M[iyu]p[ae]?r?t[yi]|Mipty|M[eoy]pt[ey]|mopte|imparty|xparty|[SC]uperty|Siperty|Sypety|Siyty|Mipety|Miperty|Myperty|Myparty|Miparty|in parte et heredes)'),
 ('lin_ursel', 'Lincoln: houses of Ursel Levy of Wigford, parish of St Mark, held by Adam Cokerel', 'Lincoln',
  r'(Leny|Lev[yei]\b|Leuy|Leve\b|levi\b|Wi[ck]k?e?ford|Wichkford|Wyckford|Cokere?l|Cokert|[uvp]r[sc]ell|[vV]isell|[vV]icell|Vysell|Viselly|uisell)'),
 ('lin_diabella', 'Lincoln: houses of Diabella and of Benedict son of Diabella, held by Robert de Leverton', 'Lincoln',
  r'(Leverton|Leberton|Loverton|Le ?Berton|leBorton|(?<![IiYy])[DSds]i?a?bell[ei]|\baabell[ei]|Diabel|dicibell|Sutbelle|Siabelle|Dyey Belle|Dyare|Diei Kelle|Asey Belle|Dlei belle|die belle|Dudicibe)'),
 ('lin_belasset', 'Lincoln: houses and rent of Belasset of Wallingford, held by Walter le Fevre of Fulletby', 'Lincoln',
  r'([BRVGvbr]e?[lL][ai]?s+e[ct]|[BRr]elas|[Rr]ela[fs][eo]t|velafet|volasset|Rebaess|Resalel|Relitsect|Rolasect|Relasse|Belaset|Foleteby|Flecby)'),
 ('oxf_mosse', 'Oxford: houses of Mosse son of Jacob of London, parish of St Aldate, rent paid by Walter Burnel', 'Oxford',
  r'(Burnel|Surnell|Buruell|Biruell|Rinruell|Survll|Wenel|Mossi ?f|Mossy ?f|Mosse fili|mosci f|mesci f|mosti f|testi Jatobi|questi cati)'),
 ('oxf_vives', 'Oxford: house in the suburb of Oxford of Vives le Yonge, hanged, kept by John Mareys', 'Oxford',
  r'(Mareys|le [Yy]onge? iudei|[uy]yeus le|Vyensle)'),
 ('cam_jocei', 'Cambridge: houses of Jocei son of Saulot in Bridge Street, held by John But', 'Cambridge',
  r'(?i)(Johanne [BC]ut\b|Briggest|Brugestr|Bingestr|Crugestr)'),
 ('lon_bagard', 'London: houses of Elias Bagard, granted to Isabella de Vescy', 'London',
  r'(Bag+ard|Gagard|Vesc?t?cy|Sesty|Besty)'),
 ('lon_benhagin', 'London: houses of Benedict son of Hagin, Cripplegate ward, parish of St Lawrence Jewry', 'London',
  r'([BRGVvb]e?n[eo]?d\w*\s+fil\w*\s+Ha[gx]\w*)'),
]
TOWNS = [('London', r'London|Londonie|Londoniensi'), ('Lincoln', r'Lincol|Lince\b|Linc\b|Lyncoln|\bLuci?a?\b|\bLune\b|\bLinci\b|\bLuce\b'), ('Bristol', r'Bristol'),
 ('Oxford', r'Oxon'), ('Exeter', r'Exon'), ('Cambridge', r'Cantebr'), ('Winchester', r'Wynton|Winton'), ('York', r'Ebora'),
 ('Northampton', r'Nor?th?amt?on|Norhampton'), ('Canterbury', r'Cantuar'), ('Stamford', r'Sta[uw]?mford|Staunford'),
 ('Norwich', r'Norw[iy]c|Nordic'), ('Ipswich', r'[GTSB]i?ppe?s?wic|Ippeswic'), ('Hereford', r'Hereford'), ('Devizes', r'De[nu][iy]ses|Devises'),
 ('Colchester', r'Colecest|Colcest'), ('Gloucester', r'Glouc')]
out = []
for i, h in enumerate(hits):
    m = ' '.join(l for mm, c, l in h['lines'] if mm)
    a = ' '.join(l for mm, c, l in h['lines'])
    tags = []
    for k, lab, town, pat in PROPS:
        if k == 'bri_bonefey':
            if re.search(r'(?i)(bonef|bonest|bonese|ronef|rovef|gonf|ronf|tonef|tones|rouese|onefe|ronese|rouest|onefei|bovef|bovese|conef|conest|vonef|vonese|bene[fs]e[iyr]|\bgones|\beones|\bciones|\btouef|\btonesei)', m) and not re.search(r'(?i)cri[ck]e?lade|crekelade|lumbard', m) and (re.search(BRI + r'|[A-Za-z]*st[oe]l|Glouc|Shop|defunct|le Wal|le Wel|le Bal|Banastre|super pontem', m)):
                tags.append(k)
            continue
        if re.search(pat, m):
            if k.startswith('bri_') and not re.search(BRI + r'|Glouc|Wynchest|Wyuchest|Bynchest|chester', m): continue
            if k == 'bri_jospin' and not re.search(r'Bristol|stoll|stell|stol|Wynchest|Wyuchest|Bynchest|chest|Glouc', m): continue
            tags.append(k)
    tag = tags[0] if tags else None
    plines = {}
    for k in tags:  # the matched line that names this charge
        pat = [p for p in PROPS if p[0] == k][0][3]
        for mm, c, l in h['lines']:
            if mm and re.search(pat, l) and ('fuerunt' in l or 'fuit' in l):
                plines[k] = l; break
    town = None
    if tag: town = [p[2] for p in PROPS if p[0] == tag][0]
    else:
        for t, pat in TOWNS:
            if re.search(pat, m, re.I if t in ('Hereford',) else 0): town = t; break
    yr = int(re.sub(r'\D', '', h['year'])[:4]) if re.search(r'\d{4}', h['year']) else None
    out.append(dict(i=i, year=yr, approx=h['approx'], ref=h['ref'], href=h['href'], conf=h['conf'], prop=tag, props=tags, plines=plines, town=town,
                    line=next((l for mm, c, l in h['lines'] if mm and re.search(r'fuerunt', l)), next((l for mm, c, l in h['lines'] if mm), ''))))
json.dump(dict(props=[dict(key=k, label=lab, town=t) for k, lab, t, _ in PROPS], hits=out), open(OUT, 'w'), ensure_ascii=False, indent=0)
from collections import Counter
print(Counter(o['prop'] for o in out)); print(Counter(o['town'] for o in out))
for k, *_ in PROPS:
    ys = [o['year'] for o in out if k in o['props'] and o['year']]
    print(k, len(ys), min(ys) if ys else '', max(ys) if ys else '')
print('UNTAGGED:')
for o in out:
    if not o['town']: print(o['i'], o['year'], o['ref'], '|', o['line'][:150])

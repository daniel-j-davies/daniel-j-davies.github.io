"""Turn the review page into the standalone public page for danieldavies.co/expulsion/.

Run from anywhere:  python3 build/make_deploy.py
- Reads the review page index.html in the atlas folder.
- Writes the public folder ../expulsion/ with index.html, data/ and content/commentary.html.
The public page hides every entry marked "To verify" and the review notes (the checking list and the earlier
sweep table), adds a full <head>, a link home and a credits line, and fills the commentary slots from
content/commentary.html, which it creates once and never overwrites.
"""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(ROOT), 'expulsion')
URL = 'https://danieldavies.co/expulsion/'

s = open(f'{ROOT}/index.html').read()
head_new = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>The Expulsion of 1290</title>
<meta name="description" content="Records of the dissolution of England's Jewish community, 1275–1600: the expulsion of 1290, the disposal of houses and bonds, the House of Converts, and the Exchequer charges that outlived the community.">
<meta name="author" content="Daniel Davies">
<link rel="canonical" href="{URL}">
<meta property="og:title" content="The Expulsion of 1290">
<meta property="og:description" content="England's Jews in the records, 1275–1600: the expulsion, the houses and bonds, the House of Converts, and the long Exchequer charges.">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%2334426e'/%3E%3Cpath d='M7 9h18v14H7z' fill='none' stroke='%23fff' stroke-width='2'/%3E%3Cpath d='M7 16l3-2 3 2 3-2 3 2 3-2 3 2' fill='none' stroke='%23fff' stroke-width='1.6'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;1,400&family=Spectral+SC:wght@500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap">
'''
s = head_new + s[s.index('<style>'):]
rep = [
    ('</style>\n\n<div id="app">', '</style>\n</head>\n<body>\n<div id="app">'),
    ('.tab:hover{background:var(--surface-2)}',
     '.tab:hover{background:var(--surface-2)}\n.home{white-space:nowrap;font-size:13.5px;color:var(--ink-2);text-decoration:none;border-left:1px solid var(--rule);padding-left:14px}\n.home:hover{color:var(--accent)}\n@media (max-width:640px){.home{display:none}}'),
    ('''      <button class="tab" role="tab" id="t-sources" aria-selected="false" data-v="sources">Sources &amp; method</button>
    </nav>''', '''      <button class="tab" role="tab" id="t-sources" aria-selected="false" data-v="sources">Sources &amp; method</button>
    </nav>
    <a class="home" href="https://danieldavies.co/">Daniel Davies</a>'''),
    ("const CONFIG={showUnverified:true, commentary:null, review:true};",
     "const CONFIG={showUnverified:false, commentary:'content/commentary.html', review:false};"),
]
for a, b in rep:
    assert s.count(a) == 1, 'MISSING or repeated: ' + a[:80]
    s = s.replace(a, b, 1)
s = s.rstrip() + '\n</body>\n</html>\n'

os.makedirs(f'{OUT}/content', exist_ok=True)
open(f'{OUT}/index.html', 'w').write(s)
if os.path.exists(f'{OUT}/data'):
    shutil.rmtree(f'{OUT}/data')
shutil.copytree(f'{ROOT}/data', f'{OUT}/data')

VIEWS = [('overview', 'Overview'), ('sequence', '1290–93'), ('map', 'Map'), ('houses', 'Houses and rents'),
         ('domus', 'House of Converts'), ('sources', 'Sources and method')]
cpath = f'{OUT}/content/commentary.html'
if not os.path.exists(cpath):
    open(cpath, 'w').write(
        '<!-- Commentary for the Expulsion atlas.\n'
        '     Write inside any section below; plain HTML (<p>, <em>, <a href="...">) is fine.\n'
        '     A section left empty, or holding only comments like this one, stays hidden on the site. -->\n\n'
        + '\n\n'.join(f'<section data-view="{v}">\n  <!-- {label} -->\n</section>' for v, label in VIEWS) + '\n')
n = sum(len(fs) for _, _, fs in os.walk(OUT))
print('deploy page', len(s), 'bytes ->', OUT, f'({n} files)')

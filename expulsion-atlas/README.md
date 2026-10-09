# The Expulsion of 1290: records of the dissolution, 1275–1600 (working draft)

Built 8 October 2026 as an interactive resource on the dissolution of England's Jewish community, in the family of the Berwick and Merchant London atlases. Its starting point was the Glyph Machina assistant sweep pasted into the conversation that day. That sweep's claims were tested against Glyph Machina, the Calendar of Patent Rolls, The National Archives' catalogue, and two public-domain studies, Abrahams (1895) and Adler (1899). Nothing outside this folder and its sibling `../expulsion/` was changed, apart from one preview entry in `AI Sandbox/.claude/launch.json` (see the tooling note).

"The Expulsion of 1290" is a working title.

## Files

- `index.html`: the review version. It shows every entry, including those marked "To verify", together with the empty commentary slots, the checking list and the table of the earlier sweep. It has seven views:
  - **Overview**: a chronology of 30 dated events; small multiples of five Glyph Machina formulae by decade, 1200–1600, with the surviving plea rolls of the Exchequer of the Jews (TNA E 9); and the Patent Roll entries by decade and type.
  - **1290–93**: the expulsion and the disposal of property, in date order, with a chart of the county rolls of obligations (E 101/250/2–12).
  - **Map**: every record that names one place, as discs sized by count and divided by type. Periods: 1275–89, 1290–93, 1294–1400, 1401–1600. The side panel lists each place's records.
  - **Houses & rents**: lifelines of ten Exchequer charges on houses that had been Jews', from their stated origin to the last entry found (1596). A heat table shows the formula's hits by place and decade.
  - **House of Converts**: keepers 1283–1565 (Patent Rolls and the TNA account series), Adler's 48 residents 1330–1608, the phrase's distribution by decade and series, and admissions and petitions.
  - **Records**: all 901 records, searchable and filterable, with links to Discovery and to the Glyph Machina image pages.
  - **Sources & method**.
- `../expulsion/`: the public, website-ready version (see "Publishing on danieldavies.co" below). `build/make_deploy.py` makes it from `index.html`.
- `data/atlas.json`: the records and derived series. `data/geo.json`: the map (Natural Earth 10m land and rivers, simplified).
- `build/`:
  - `gm_fetch.py`: the Glyph Machina queries. `gm_parse.py` parses the saved result pages and `gm_tag.py` tags the escheat-formula hits by charge and town. The pages themselves are in `src/gm/`, with `query_log.json`.
  - `cpr_jews.py`: splits the Patent Roll text (all volumes in `London Merchants/sources/`, as extracted for the merchant atlas) into entries and keeps the 256 that name Jews, the Jewry, Judaism or the converts (`src/cpr/cpr_jews.json`). All 256 were read; 101 are in the atlas.
  - `tna_fetch.py`: the Discovery API searches, saved in `src/tna/` (E 101, SC 8, SC 1, E 9, C 47, E 401).
  - `curated.py`: everything entered by hand, with a docstring on the status marks: the Patent Roll selection with summaries, the dated events, Adler's residents, the keepers' appointments, the origin of each charge, the earlier sweep's items, and the flags below.
  - `build.py`: assembles `data/atlas.json`. `geo.py` makes `data/geo.json`, taking the path to the Natural Earth files as its argument. `make_deploy.py` makes the public folder.
  - `src/ia/`: OCR texts of Abrahams and Adler, cleaned of spacing, as read for page references.

To view locally, serve the folder (it loads its data with `fetch`): for example `python3 -m http.server` from inside this folder, then open http://localhost:8000. Rebuild with `python3 build/build.py`, then `python3 build/make_deploy.py`.

## Sources

| Source | What it gives | How it was used |
|---|---|---|
| Glyph Machina (AALT machine transcriptions) | Formula counts by decade and series; the 374 entries with "que fuerunt … iudei" on rolls dated 1291–1600, all read | 26 spaced queries (25 searches and one sample to check noise) |
| Calendar of Patent Rolls, 1281–1485 and 1547–48 | 101 entries with volume and page | Read by hand from the calendar text; summaries are paraphrase, quotations are the calendar's OCR text |
| TNA Discovery | 393 catalogue entries: the Exchequer of the Jews (E 9), Jews' accounts (E 101/249–250), the Domus accounts (E 101/250–255), petitions (SC 8), letters (SC 1), C 47 | Typed by keyword and by hand; 24 entries excluded by hand as foreign (Gascony, Ponthieu, Lectoure), the surname Jewe, or no Jewish content in the description |
| B. L. Abrahams, *The Expulsion of the Jews from England in 1290* (Oxford, 1895) | The writs of 18 July, the departure of 9 October, 1,335 to Flanders, houses worth about £130 a year, debts of about £9,100 | Page numbers are those of the offprint as read in OCR, given as "c." where the running heads are uncertain |
| M. Adler, *History of the "Domus Conversorum" from 1290 to 1891* (1899) | Foundation (1232), 80 converts in 1290, the inquiry list of 1280–1308, and the 48 residents from 1330 to 1608 (App. XXI) | Residents entered as Adler gives them |

## Status marks

- **Checked in sources**: found in the Patent Rolls (volume and page), Abrahams or Adler.
- **Database**: The National Archives' catalogue, or Glyph Machina's machine transcription.
- **To verify**: reference knowledge, or an item from the earlier sweep that was not re-read.

Of the earlier sweep's 27 items, 8 match a hit read for this atlas (same roll and image). The other 19 stay "To verify" and are hidden on the public site.

## Needs your judgment or checking

1. **The formula is not proof of an Expulsion escheat.** "Que fuerunt … Iudei" marks a Jewish former owner. The two Bristol charges that run longest (to 1529 and 1575) cite pipe rolls of 16 and 27 Henry III and a grant of 16 July 1241. Diabella of Lincoln is "dampnata", and Vives le Yonge "suspensus" (hanged). Only some of the long charges began in 1290. The Houses & rents view sorts each charge by what its own entries say. The sweep's account of "houses forfeited by expelled Jews … copied forward for centuries" needs this qualification.
2. **Wickford is Wigford.** The sweep placed an escheat at Wickford (E368 roll 239, image 0084). The entries name Ursel Levy "de Wikeford in parochia Sancti Marci", and CPR 1461–67, p. 499 puts his houses in Lincoln. That is Wigford, Lincoln's suburb with St Mark's church.
3. **The 1559 roll.** The sweep called E372 roll 401 (image 0032) "Marian" and grouped it with Bristol. The hit read here is dated 1559, under Elizabeth I, and charges Lincoln houses of Diabella and Belasset.
4. **Exonie is Oxonie.** The transcription often reads the Oxford rents as "ville Exonie". The house of Vives le Yonge, hanged, is in "suburbia Oxon" on the same images, and SC 8/67/3303 (1337–38) places the toft of "Vive le Longe … hanged for felony" in the suburb of Oxford. It is mapped at Oxford.
5. **Raw counts after 1290 are mostly noise.** An unanchored search for eight forms of *iudeus* returns 37,683 entries, rising after 1290. A sample of 25 Common Pleas hits from the 1330s shows two misreadings: "Iudeo" for *ideo*, and the feast of SS Simon and Jude. None of the 25 clearly names a Jew. The Overview uses anchored formulae only.
6. **Two keepers in 1327.** The Patent Roll grants the Domus to Richard de Ayremynne for life in March 1327, but a 1341 exemplification recites letters of 7 November, 1 Edward III, appointing Adam de Osgodeby.
7. **Walter of Nottingham.** Adler's first post-Expulsion inmate (1330–36) may be the "Master Walter de Croydon … lately received among the conversi" of a protection dated at Nottingham in March 1331 (CPR 1330–34, p. 82).
8. **Chellesworthy.** The CPR's "Chellesworthy alias Chollesworthy, co. Devon" was in the king's hands "by the exile of the Jews" from 1401 to 1461. It is mapped at Chilsworthy near Holsworthy, which is a guess.
9. **County rolls placed at towns.** The 1291–93 rolls of obligations are by county. Each is placed at its county's main Jewry: Gloucestershire at Gloucester, Wiltshire at Devizes, Huntingdon and Cambridge at Cambridge.
10. **Gascony, 1287.** The year is reference knowledge. The OCR of Abrahams has no year at that point and misprints Edward's departure as 1280.
11. **Machine transcriptions.** Names and sums that come only from Glyph Machina should be read on the image before citing. Tagging used patterns that allow for recurrent misreadings (Bristoll as Cristoll or Tristoll; Bonefey as Ronefey or Gonesey). A few entries may be tagged to the wrong charge. Each dot in the lifeline chart opens its image.
12. **What was not searched.** The pipe rolls before 1291 were not searched for these charges, the "per exilium" hits were counted but not read, and the Close and Fine Rolls are not in the folder. Rigg's calendar of the Exchequer of the Jews and the Select Pleas (both public domain) were downloaded but not used here.

## Two entries worth reading on the image

- **E372 roll 139, dorses, image 2320 (1291), the Bristol constable's account.** Houses of hanged Jews in Winchester Street and outside the castle are let for less "quia pauci inhabitare volunt" (because few will live there), and "cimiterio quod fuit judeorum" (the cemetery that was the Jews') is let to farm. Petition SC 8/34/1657 (c. 1290), from the abbot of St Augustine's, Bristol, concerns the land the Jews held of him for a graveyard, taken into the king's hand after they were driven out.
- **E372 roll 163, fronts, image 0054 (1313).** A pipe-roll list of the London grants of 19 Edward I, street by street: Catte Street, Milk Street, Wood Street, Colechurch Street and the parish of St Lawrence in the Jewry.

## Databases and access

- **Glyph Machina**: its robots file disallows automated access. As for the earlier atlases, use was kept small: 26 queries, 15 seconds apart, all logged with their URLs in `build/src/gm/query_log.json`. The page carries the credit wording Glyph Machina asks for.
- **The National Archives, Discovery API**: open to automated use. Catalogue text is under the Open Government Licence v3.0, credited on the page.
- **Internet Archive**: Abrahams, Adler, Rigg (two volumes) and Jacobs, public domain.

## Rights

Natural Earth is public domain. TNA catalogue text is used under the OGL v3.0. Glyph Machina lines are short quotations with links back. Quotations from the calendars and editions are short. Nothing here needs a copyright permission before publication.

## Left for the author

Each view has a commentary slot. On the review page it shows as a marked empty box; on the public page it stays hidden until filled. The page's labels and figure notes are descriptive; no interpretive prose was written.

## Publishing on danieldavies.co

The atlas goes into the website repository as one folder, `expulsion`, and will live at https://danieldavies.co/expulsion/.

1. Optional: write commentary in `../expulsion/content/commentary.html`, one `<section data-view="…">` per view. Empty sections stay hidden.
2. Copy the whole `expulsion` folder (4 files) into the root of your local copy of the repository. Then commit and push in GitHub Desktop.
3. Add a link from one of your pages: `<a href="expulsion/">The Expulsion of 1290</a>`.

To rebuild the public folder after changing the review page, run `python3 build/make_deploy.py`. It overwrites `../expulsion/index.html` and `data/`, and never overwrites `content/commentary.html`.

## Tooling note

A preview-server entry named `expulsion-atlas` was added to `AI Sandbox/.claude/launch.json` for testing. It serves a copy in a temporary folder, because the preview server could not read the Dropbox folder. Delete the entry when it is no longer wanted.

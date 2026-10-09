"""Hand-entered records for the Expulsion atlas.

Status marks (as in the Berwick and Merchant London atlases):
  src     checked in a printed source read for this atlas: Calendar of Patent Rolls (CPR, volumes in
          London Merchants/sources/), B. L. Abrahams, The Expulsion of the Jews from England in 1290 (Oxford, 1895,
          reprinted from JQR 7), or M. Adler, History of the 'Domus Conversorum' from 1290 to 1891 (London, 1899,
          from Trans. JHSE 4). Page numbers for Abrahams are those of the 1895 offprint, read from OCR text; some are
          approximate and marked 'c.'.
  db      taken from a database: Glyph Machina machine transcription of AALT images, or TNA Discovery catalogue.
  verify  reference knowledge, or a claim from the earlier Glyph Machina assistant sweep (pasted into the
          conversation of 8 Oct 2026) that was not re-read for this atlas.

Record types (used for colour, in this fixed order):
  before     the community before 1290: licences, keepers, tallage, community petitions
  condemned  the coinage trials of 1278-79 and the forfeitures and fines that followed, to 1290
  expulsion  the expulsion itself, 1290
  property   houses, schools, synagogues and rents: grants, sales, and later charges and pleas
  bonds      bonds, chests (archae) and debts
  domus      the House of Converts (Domus Conversorum)
  presence   Jews and converts in England after 1290 outside the Domus
  name       the Jewry as a place-name
"""

TYPES = [
    ('before', 'Before 1290: the community in the records', '--c1'),
    ('condemned', 'Coinage trials and forfeitures, 1278–90', '--c8'),
    ('expulsion', 'The expulsion, 1290', '--c2'),
    ('property', 'Houses, schools and rents', '--c4'),
    ('bonds', 'Bonds, chests and debts', '--c7'),
    ('domus', 'House of Converts', '--c5'),
    ('presence', 'Jews and converts after 1290', '--c3'),
    ('name', 'The Jewry as a place-name', '--c6'),
]

# ------------------------------------------------------------------ places (lat, lon). Placed at the town centre
# (London at Old Jewry). 'chilsworthy' is an identification of the CPR's 'Chellesworthy, co. Devon' and is to verify.
TOWNS = {
    'london': ('London', 51.5145, -0.0918), 'york': ('York', 53.9590, -1.0815), 'lincoln': ('Lincoln', 53.2307, -0.5406),
    'norwich': ('Norwich', 52.6286, 1.2924), 'winchester': ('Winchester', 51.0632, -1.3080), 'oxford': ('Oxford', 51.7520, -1.2577),
    'cambridge': ('Cambridge', 52.2053, 0.1218), 'canterbury': ('Canterbury', 51.2802, 1.0789), 'bristol': ('Bristol', 51.4545, -2.5879),
    'gloucester': ('Gloucester', 51.8642, -2.2382), 'hereford': ('Hereford', 52.0565, -2.7160), 'worcester': ('Worcester', 52.1920, -2.2200),
    'exeter': ('Exeter', 50.7184, -3.5339), 'northampton': ('Northampton', 52.2405, -0.9027), 'nottingham': ('Nottingham', 52.9548, -1.1581),
    'stamford': ('Stamford', 52.6530, -0.4800), 'colchester': ('Colchester', 51.8892, 0.9042), 'bedford': ('Bedford', 52.1360, -0.4667),
    'devizes': ('Devizes', 51.3500, -1.9940), 'huntingdon': ('Huntingdon', 52.3310, -0.1840), 'ipswich': ('Ipswich', 52.0567, 1.1482),
    'marlborough': ('Marlborough', 51.4200, -1.7300), 'warwick': ('Warwick', 52.2820, -1.5850), 'bridgnorth': ('Bridgnorth', 52.5340, -2.4200),
    'montford': ('Montford Bridge', 52.7360, -2.8600), 'cricklade': ('Cricklade', 51.6410, -1.8570), 'wallingford': ('Wallingford', 51.6000, -1.1250),
    'chilsworthy': ('Chellesworthy (Chilsworthy?), Devon', 50.8300, -4.3700), 'ware': ('Ware', 51.8100, -0.0300),
    'dartmouth': ('Dartmouth', 50.3510, -3.5790), 'rutland': ('Rutland', 52.6700, -0.7300), 'lynn': ('Lynn', 52.7520, 0.4040),
    'bury': ('Bury St Edmunds', 52.2460, 0.7120), 'winchelsea': ('Cinque Ports', 50.9250, 0.7090),
}

# ------------------------------------------------------------------ Calendar of Patent Rolls
# (volume label, page, match text in the entry, year, date label, type, town, summary)
CPR = [
    ('CPR 1281–92', '4', 'Isaac de Suthwerk', 1281, '1281', 'before', 'london', 'Licence for Isaac of Southwark, Jew, to sell his houses in Southwark, but not in mortmain.'),
    ('CPR 1281–92', '6', 'goods of condemned Jews', 1281, 'Dec. 1281', 'condemned', 'oxford', 'Acquittance to the late sheriff of Oxford for £50 paid out of the goods of condemned Jews.'),
    ('CPR 1281–92', '15', 'keepers (ctestodes) of the Jews of Hereford', 1282, '1282', 'before', 'hereford', 'Twenty-six burgesses of Hereford appointed keepers of the Jews of Hereford; proclamation that the Jews are not to be molested.'),
    ('CPR 1281–92', '26', 'Jew of Oxford', 1282, '1282', 'before', 'oxford', 'Licence to buy rent in Oxford of Asser son of Leo of Winchester, Jew of Oxford.'),
    ('CPR 1281–92', '56', 'chests of the chirographers of Jewry', 1283, '1283', 'bonds', None, 'Edmund, the king’s brother, to levy all debts owed to Aaron son of Vives found in the chests of the chirographers anywhere in England.'),
    ('CPR 1281–92', '56', 'clippings of the king', 1283, 'Feb. 1283', 'condemned', 'london', 'Commission to enquire into Jews dealing with foreign merchants in plate made from clippings of the coin.'),
    ('CPR 1281–92', '88', 'keeper of tbe Domus Conversorum', 1283, '1283', 'domus', 'london', 'John de St Denis, keeper of the Domus Conversorum, names Thomas de Colchester as his substitute.'),
    ('CPR 1281–92', '107', 'Jew of Worcester', 1283, '1283', 'before', 'worcester', 'Licence for Dyaius son of Sampson, Jew of Worcester, to sell a messuage in the parish of St Andrew.'),
    ('CPR 1281–92', '116', 'every Jew and Jewess crossing', 1284, '1284', 'before', 'montford', 'Pontage for Montford bridge, Shropshire, with a special toll on every Jew and Jewess crossing: 1d. on horseback, ½d. on foot.'),
    ('CPR 1281–92', '116', 'Benedict de London, Jew of Lincoln', 1284, '1284', 'before', 'lincoln', 'Licence for Benedict of London, Jew of Lincoln, and Hagin his son to sell a debt of £100.'),
    ('CPR 1281–92', '173', 'concealed good* of condemned Jews', 1285, 'June 1285', 'condemned', 'london', 'Florentine and Sienese merchants (Bardi and others) fined for concealed goods of condemned Jews, paid to the keeper of the queen’s gold.'),
    ('CPR 1281–92', '173', 'the place in which the Jews arc buried', 1285, 'June 1285', 'before', 'london', 'Licence to buy a messuage in Wood Street of Cresseus son of Cresseus, Jew of London; the bounds name the place where the Jews are buried.'),
    ('CPR 1281–92', '183', 'lately hanged', 1285, '1285', 'condemned', 'bedford', 'Messuage in Bedford of Jacob son of Peytevin, Jew of Bedford, lately hanged, granted to Newnham Priory.'),
    ('CPR 1281–92', '188', "placed in the Jews' chest", 1285, '1285', 'bonds', None, 'Henry de Bray to take recognisances of debts to Jews before the sheriffs, to be placed in the Jews’ chest.'),
    ('CPR 1281–92', '193', 'fine of 1,000/. paid by her', 1285, 'Sept. 1285', 'condemned', 'london', 'Floria, widow of Elias son of Master Moses, Jew of London, freed from tallage after a fine of £1,000 for concealed goods.'),
    ('CPR 1281–92', '212', 'chest of chirographs of Cambrid', 1285, 'Oct. 1285', 'bonds', 'cambridge', 'Enquiry into the chests of chirographs of Cambridge and Bedford, carried to the Isle of Ely in the troubles of Henry III’s reign.'),
    ('CPR 1281–92', '227', 'archat cyrographorum', 1286, '1286', 'bonds', 'london', 'Officials appointed to open and examine all the deed-boxes of Jews (archae cyrographorum Judaeorum) in London and Westminster.'),
    ('CPR 1281–92', '228', 'keeper of the Domus Conversorum, London, by appointment of Henry III', 1286, 'Mar. 1286', 'domus', 'london', 'John de St Denis, keeper of the Domus Conversorum by appointment of Henry III, discharged from accounting at the Exchequer.'),
    ('CPR 1281–92', '236', 'cognisance of personal actions', 1286, '1286', 'before', 'oxford', 'The chancellor of the University of Oxford given cognisance of cases between scholars and the Jews of Oxford.'),
    ('CPR 1281–92', '335', 'Dotims Conveworum', 1289, '1289', 'domus', 'london', 'Richard de Clympinges, king’s clerk, appointed keeper of the Domus Conversorum.'),
    ('CPR 1281–92', '341', 'death of Isaac de Suwerk', 1290, 'Feb. 1290', 'property', 'london', 'Messuage in Southwark of Isaac of Southwark, Jew of London, deceased, granted in fee at a rent of 1d.'),
    ('CPR 1281–92', '398', 'chevage on Jews', 1290, '20 Feb. 1290', 'domus', None, 'John de Havenak and Philip le But, converts of the Domus, commissioned to collect the chevage (poll tax) on Jews of twelve and over, granted for the converts’ maintenance.'),
    ('CPR 1281–92', '366', 'Cattestrete', 1290, '15 June 1290', 'before', 'london', 'Auntera, widow of Vives son of Master Moses, licensed to sell her garden in Catte Street to any Jew willing to buy it.'),
    ('CPR 1281–92', '378', 'Jews quiiting- the realm', 1290, 'July 1290', 'expulsion', 'winchelsea', 'Safe-conduct for the Jews quitting the realm with their wives, children and goods, directed to the bailiffs, barons and sailors of the Cinque Ports.'),
    ('CPR 1281–92', '379', 'Christians he chooses', 1290, 'July 1290', 'expulsion', 'london', 'Aaron son of Vives, the Jew of Edmund the king’s brother, licensed to sell his houses and rents in London and elsewhere to Christians.'),
    ('CPR 1281–92', '379', 'Bonamieus, Jew of', 1290, 'July 1290', 'expulsion', 'york', 'Safe-conduct for Bonamy, Jew of York, his wife, children and household, quitting the realm after the term set for redeeming Christians’ pledges.'),
    ('CPR 1281–92', '381', 'Jew of HorthamptOB', 1290, 'Aug. 1290', 'expulsion', 'northampton', 'The Cinque Ports not to molest Mosse son of James de Oxonia, Jew of Northampton, quitting the realm within the time fixed, but to give him safe passage at moderate charges.'),
    ('CPR 1281–92', '382', 'Jews of York', 1290, '21 Aug. 1290', 'expulsion', 'york', 'The Cinque Ports not to molest Bonamy of York, Jocem his son and the other Jews of York quitting the realm.'),
    ('CPR 1281–92', '384', 'Jew of the king\'s consort', 1290, '1 Sept. 1290', 'expulsion', 'london', 'Cok Hagin, the queen’s Jew, licensed to sell his London houses to any Christians.'),
    ('CPR 1281–92', '392', 'Agmoelesham', 1290, '27 Oct. 1290', 'domus', 'london', 'Walter de Agmodesham appointed keeper of the Domus Conversorum and of the converts.'),
    ('CPR 1281–92', '410', 'value and sell all the houses', 1290, 'Dec. 1290', 'property', None, 'Hugh de Kendale appointed to value and sell all the houses, rents and tenements of the king’s Jews, in London with the counsel of named citizens.'),
    ('CPR 1281–92', '417', 'Writ of aid for Hugh de Kendale', 1291, '1291', 'property', None, 'Writ of aid for Hugh de Kendale to appraise, extend and sell the houses, rents and tenements late of the Jews in England.'),
    ('CPR 1281–92', '417', 'fee city <y£ York', 1291, '1291', 'property', 'york', 'The escheator beyond Trent to sell the houses of Jews in York that were in Queen Eleanor’s hands.'),
    ('CPR 1281–92', '478', '202', 1292, 'Feb. 1292', 'domus', 'london', 'Grant to the converts of London of £202 0s. 4d. yearly at the Exchequer for the keeper, two chaplains, a clerk, and the converts for life; each convert’s portion lapses at death.'),
    ('CPR 1292–1301', '18', 'School of the Jews there', 1293, '1293', 'property', 'colchester', 'The house that was the School of the Jews at Colchester, and houses of Jocey son of Samuel, Aaron, Elias, Dulcia and her daughter Pigga, Bacock, Simon and Hake, granted to William son of Jordan de Brokesburn.'),
    ('CPR 1292–1301', '188', 'Hagin, sometirae Jew of London', 1296, 'May 1296', 'property', 'london', 'Otto de Grandson licensed to demise the London houses late of Hagin, Jew of London, given to him by Queen Eleanor.'),
    ('CPR 1292–1301', '530', 'exile of the Jews', 1300, 'Aug. 1300', 'property', 'norwich', 'A void plot in Norwich, once of Anesterra Hagge and her nephews Vivant and Mosse, Jews, the king’s escheat by the exile of the Jews, licensed to John de Ros.'),
    ('CPR 1301–07', '316', 'synagogue of the Jews', 1305, '1305', 'property', 'london', 'The Friars of the Sack licensed to assign their chapel in Coleman Street, lately the synagogue of the Jews, to Robert son of Walter for a chantry for Queen Eleanor.'),
    ('CPR 1301–07', '393', 'converts of London', 1305, 'Nov. 1305', 'domus', 'london', 'The Exchequer to pay the converts of London what is due on the yearly £202 0s. 4d. of 1292, and to report on the state of the converts and their house.'),
    ('CPR 1307–13', '12', 'John 1& Convert', 1307, '1307', 'domus', None, 'Grant for life to John le Convert, king’s yeoman, of two casks of wine a year confirmed.'),
    ('CPR 1307–13', '201', 'Mljm, the Jew', 1309, 'Dec. 1309', 'presence', None, 'Safe-conduct for Master Elias the Jew, coming from Brabant to England by the king’s command.'),
    ('CPR 1313–17', '39', 'Osgodeby', 1313, 'Nov. 1313', 'domus', 'london', 'Adam de Osgodeby appointed keeper for life of the house of the Conversi; the City to help him levy rents withheld from the house.'),
    ('CPR 1313–17', '199', 'school of ihe Jews of Horhamptoo', 1314, '1314', 'property', 'northampton', 'Inspeximus of Edward I’s grant (April 1291) to St James’s Abbey, Northampton, of the School of the Jews of Northampton and the adjoining houses of Sarra of London, a Jewess, escheated by the exile of the Jews.'),
    ('CPR 1313–17', '356', 'Martin le Convers', 1315, '1315', 'domus', 'london', 'The keeper and Conversi lease a tenement in New Street opposite the house to Alice, daughter of Martin le Convers, and her husband.'),
    ('CPR 1313–17', '511', 'by reason of Judaism', 1316, 'July 1316', 'bonds', None, 'Exemplification of Edward I’s grant (4 July 1291) of lands in Surrey that the king held ‘by reason of Judaism’, that is through a Jewish debt.'),
    ('CPR 1317–21', '254', 'Isaak the Jew', 1318, 'Dec. 1318', 'presence', None, 'Safe-conduct for a year for Isaak the Jew, travelling with Roger de Stanegrave, Hospitaller, a prisoner from the Holy Land raising his ransom; Isaak stays in his train until paid. Extended in 1320.'),
    ('CPR 1317–21', '502', 'lately a Jew and now a convert', 1320, '1320', 'presence', None, 'Safe-conduct for John de St Martin of Tours, lately a Jew and now a convert, going beyond the seas.'),
    ('CPR 1321–24', '1', 'St. Laurence, Jewry', 1321, '1321', 'name', 'london', 'Chantry in the church of St Laurence, Jewry, London.'),
    ('CPR 1321–24', '32', 'house o! the Converts', 1321, '1321', 'domus', 'oxford', 'William de Ayremynne, keeper for life of the House of Converts, appoints a deputy to collect the house’s rents in Oxford.'),
    ('CPR 1321–24', '36', 'chapel of the house of the Converts', 1321, '1321', 'domus', 'london', 'The deodands of the last eyre at the Tower granted for the repair of the chapel and buildings of the House of Converts.'),
    ('CPR 1321–24', '302', 'St. Olave Upwelle, in the Jewry', 1323, '1323', 'name', 'london', 'Chantry licence for the church of St Olave Upwell in the Jewry, London.'),
    ('CPR 1324–27', '176', 'Bobert de Holden', 1325, 'Oct. 1325', 'domus', 'london', 'Robert de Holden granted the custody of the House of Converts in the suburb of London for life.'),
    ('CPR 1327–30', '42', 'Richard de Ayremyn', 1327, 'Mar. 1327', 'domus', 'london', 'Richard de Ayremyn granted the custody of the Domus Conversorum and of the converts for life.'),
    ('CPR 1327–30', '66', "Jews' houses in the same town", 1327, '1327', 'property', 'colchester', 'Queen Isabella’s dower includes £35 0s. 2d. of the farm of Colchester and of the Jews’ houses there.'),
    ('CPR 1327–30', '490', 'all deodands adjudged', 1330, '1330', 'domus', 'london', 'All deodands adjudged to the king in England granted to the Conversi for their sustenance and the repair of their chapel.'),
    ('CPR 1330–34', '82', 'received among the conversi', 1331, 'Mar. 1331', 'domus', 'london', 'Protection for Master Walter de Croydon, lately received among the conversi of London at the king’s charges, going overseas.'),
    ('CPR 1330–34', '452', 'Staunford recovered by the king', 1333, '1333', 'property', 'stamford', 'Exemplification of a lost charter of 1280: houses in Stamford recovered by the king against named Jews (Isaac Mocun, Diey de Holyne, Terca, Blanche, Elias de Beans), granted to Alexander de Tykencote.'),
    ('CPR 1334–38', '259', 'Claricia de Exonia', 1336, 'Apr. 1336', 'domus', 'london', 'Richard and Katherine, children of Claricia of Exeter, one of the Conversi, given a convert’s sustenance for life.'),
    ('CPR 1334–38', '494', 'godson of Edward II', 1337, 'Aug. 1337', 'domus', 'london', 'John and William, sons of Edward de St John, one of the Conversi and godson of Edward II, given converts’ sustenance.'),
    ('CPR 1340–43', '232', 'William de Bristoll', 1341, '1341', 'domus', 'london', 'William de Bristoll given the chamber, garden and 1½d. a day of John de Northampton, deceased, in the House of Converts.'),
    ('CPR 1340–43', '236', 'custody of the House of Converts, in collecting', 1341, 'July 1341', 'domus', 'london', 'Writ of aid for John de St Paul, keeper of the House of Converts, collecting rents withheld from the house.'),
    ('CPR 1343–45', '190', 'Janettus de Ispannia', 1343, 'Jan. 1343', 'domus', 'london', 'Janettus of Spain, a convert, granted the sustenance of the other converts of the Domus for life.'),
    ('CPR 1343–45', '213', 'female converts', 1344, 'Feb. 1344', 'domus', 'london', 'William de Leycestre, king’s clerk, son of Joan, one of the female converts, granted a convert’s allowance.'),
    ('CPR 1343–45', '218', 'John de Haytfeld', 1344, '1344', 'domus', 'london', 'John de Haytfeld granted the usual allowance of a convert in the Domus.'),
    ('CPR 1345–48', '48', 'debts at the Jewry', 1346, 'Feb. 1346', 'property', 'york', 'Inspeximus (1279) discharging two York citizens of debts at the Jewry on land with schools there enfeoffed by Queen Eleanor; confirmed to the present tenant.'),
    ('CPR 1348–50', '87', 'Theobald de Turkie', 1348, '1348', 'domus', 'london', 'Theobald de Turkie, a convert, baptized and destitute, granted a convert’s house and wages.'),
    ('CPR 1348–50', '363', 'Agnes daughter of Edward', 1349, '1349', 'domus', 'london', 'Agnes, daughter of Edward de St John, a convert, given a chamber in the House of Converts for life.'),
    ('CPR 1348–50', '475', 'Henry de Ingelby', 1350, '1350', 'domus', 'london', 'Henry de Ingelby granted the keeping of the House of Converts for life.'),
    ('CPR 1350–54', '503', 'Old Jewry', 1353, 'Oct. 1353', 'name', 'london', 'Chantry of St Olave in Old Jewry, London.'),
    ('CPR 1354–58', '41', 'Boniface the Jew', 1354, 'May 1354', 'property', 'cambridge', 'A messuage in Cambridge, the king’s escheat by a felony of Boniface the Jew, granted in fee to Peter le Fitheler, king’s yeoman.'),
    ('CPR 1358–61', '198', 'school of the Jews of', 1359, '1359', 'property', 'northampton', 'The School of the Jews of Northampton, granted by Edward I to St James’s Abbey, traced through later holders.'),
    ('CPR 1358–61', '211', 'Cok aon of Aaron', 1359, 'May 1359', 'property', 'northampton', 'A house in Cornchepyng, Northampton, escheated to Henry III on the death of Cok son of Aaron, Jew of London, traced through later holders.'),
    ('CPR 1367–70', '91', 'Sancta Maria in Ispannia, a Jewish', 1368, '1368', 'domus', 'london', 'John de Sancta Maria of Spain, a Jewish convert, granted wages and houses in the Domus Conversorum for life.'),
    ('CPR 1367–70', '332', 'Laurence de Sancto Martino', 1369, 'Dec. 1369', 'domus', 'london', 'Laurence de St Martin of Spain, late a Jew and now converted, granted wages and houses in the House of Converts.'),
    ('CPR 1370–74', '128', 'William de Burstall', 1371, '1371', 'domus', 'london', 'William de Burstall granted the wardenship of the House of Converts on Henry de Ingelby’s resignation.'),
    ('CPR 1374–77', '375', 'Old Jewry, London, pertaining to the duchy', 1376, '1376', 'name', 'london', 'The inn of the wardrobe in Old Jewry, London, of the duchy of Cornwall.'),
    ('CPR 1374–77', '450', 'almost totally ruined', 1377, '1377', 'domus', 'london', 'The House of Converts and its chapel found almost totally ruined when William de Burstall took it; recompense for his repairs.'),
    ('CPR 1381–85', '231', "Domus Conversorum ' on the north", 1383, '1383', 'domus', 'london', 'A Fleet Street messuage abutting on the Domus Conversorum to the north and Chancellor’s Lane to the west.'),
    ('CPR 1381–85', '269', 'annexed to that office', 1383, '1383', 'domus', 'london', 'Confirmation of letters of 11 April 1377 annexing the Domus Conversorum for ever to the office of Keeper of the Rolls of Chancery.'),
    ('CPR 1381–85', '491', 'Peter the Convert', 1384, 'Dec. 1384', 'domus', 'london', 'Peter the Convert, once a Jew, and Edmund the Convert granted 1½d. a day each from the Domus Conversorum.'),
    ('CPR 1385–89', '397', 'Judaica pravitate', 1388, '1388', 'domus', 'london', 'Record of the suit between John de Burton, keeper, and the parson of St Dunstan in the West over revenues assigned by Henry III to converts from Judaism.'),
    ('CPR 1388–92', '417', 'Little Jewry', 1391, '1391', 'name', 'london', 'Four messuages in Little Jewry in Aldgate Street, London.'),
    ('CPR 1391–96', '311', 'Jewry-street, Winchester', 1393, 'July 1393', 'name', 'winchester', 'The church of St Michael in Jewry Street, Winchester.'),
    ('CPR 1399–1401', '454', 'exile of the Jews', 1401, 'Mar. 1401', 'property', 'chilsworthy', 'Lands late of Nicholas de Wodegrave in Chellesworthy, Devon, ‘in the king’s hands by the exile of the Jews’.'),
    ('CPR 1401–05', '89', 'houses late of the Jews in the city', 1401, '1401', 'property', 'canterbury', 'Among the City of London’s assigned revenues: the bailiffs of Canterbury owe 8d. of rent of houses late of the Jews in the city.'),
    ('CPR 1401–05', '216', 'Rabi Moyses', 1403, 'Apr. 1403', 'domus', 'london', 'Elizabeth, daughter of Rabbi Moses, ‘bishop of the Jews’, a convert, granted 1d. a day beyond the 1d. she has from the House of Converts.'),
    ('CPR 1405–08', '281', 'exile of the Jews', 1406, '1406', 'property', 'chilsworthy', 'The Chellesworthy lands ‘in the king’s hands by the exile of the Jews’ granted to Richard Gabriel, king’s clerk.'),
    ('CPR 1408–13', '96', 'Seint Jakes', 1409, 'July 1409', 'domus', 'london', 'William de Seint Jakes, lately converted, granted 1d. a day beyond the 1½d. he has as one of the converted Jews.'),
    ('CPR 1441–46', '362', 'Civitasse, Jew of Hereford', 1444, '1444', 'property', 'hereford', 'Inspeximus of grants of October and November 1291: houses in Hereford of Civitasse, and of Elias de Ardre and Aaron le Blund, Jews of Hereford, escheated through the Jews’ exile.'),
    ('CPR 1441–46', '413', 'St. Olave in Old Jewry', 1446, '1446', 'name', 'london', 'Chapel of St Mary in St Olave, Old Jewry, and five messuages in the parish of St Laurence, Old Jewry.'),
    ('CPR 1446–52', '108', 'Domus Conversorum for his dwelling', 1447, 'Oct. 1447', 'domus', 'london', 'Thomas Kirkeby appointed Keeper of the Rolls and granted the Domus Conversorum for his dwelling.'),
    ('CPR 1446–52', '115', 'exile of Jews', 1447, '1447', 'property', 'chilsworthy', 'The Chellesworthy lands ‘in the king’s hand by the exile of Jews’ committed to John Delabere for ten years at 50s.'),
    ('CPR 1446–52', '257', 'All Saints in Jewry, Cambridge', 1449, '1449', 'name', 'cambridge', 'A messuage in the parish of All Saints in Jewry, Cambridge.'),
    ('CPR 1452–61', '476', 'exile of the Jews', 1458, '1458', 'property', 'chilsworthy', 'The Chellesworthy lands ‘by the exile of the Jews’ granted in frank almoin to a provost and scholars.'),
    ('CPR 1461–67', '63', 'exile of the Jews', 1461, 'Sept. 1461', 'property', 'chilsworthy', 'The Chellesworthy lands ‘in the king’s hands by the exile of the Jews’ granted in mortmain to the abbot and convent of Fougères.'),
    ('CPR 1461–67', '147', 'House of the Converts', 1462, 'Feb. 1462', 'domus', 'london', 'Thomas Kirkeby, Keeper of the Rolls, granted the custody of the House of the Converts, ‘set apart of old’ for the keeper’s habitation.'),
    ('CPR 1461–67', '499', 'Ursel Levy', 1465, '1465', 'property', 'lincoln', 'Small sums exacted yearly at the Exchequer from houses in Lincoln late of Ursel Levy of Wickford (Wigford), Diabella, Belasset and others, granted away.'),
    ('CPR 1467–77', '245', 'House of Converts for bis habitation', 1470, '1470', 'domus', 'london', 'William Morland, Keeper of the Rolls, granted the House of Converts for his habitation.'),
    ('CPR 1467–77', '334', 'Master John Morton', 1472, 'Mar. 1472', 'domus', 'london', 'John Morton, Keeper of the Rolls, granted the House or hospital of Converts for his habitation.'),
    ('CPR 1477–85', '71', 'Master Robert Morton', 1477, '1477', 'domus', 'london', 'Reversion of the Rolls and the house or hospital of Converts to Robert Morton.'),
    ('CPR 1477–85', '462', 'Thomas Ba*owe', 1483, 'July 1483', 'domus', 'london', 'Thomas Barowe granted the Rolls and the house or hospital of Converts for his habitation.'),
]

# ------------------------------------------------------------------ dated events for the overview and the 1290 sequence
# (year, month (1-12 or None), day or None, label, detail, type, town, status, reference)
ABR = 'Abrahams, Expulsion (1895)'
EVENTS = [
    (1194, None, None, 'Ordinance of the Jewry', 'Deeds of Jewish lenders to be executed before appointed Christian and Jewish clerks in six or seven towns, one part kept in a public chest (archa).', 'bonds', None, 'src', f'{ABR}, chs. I–II'),
    (1232, 1, 16, 'Domus Conversorum founded', 'Henry III orders a house for converted Jews on what is now Chancery Lane, endowed at 700 marks a year.', 'domus', 'london', 'src', 'Adler, Domus Conversorum (1899), p. 2'),
    (1275, None, None, 'Statute of the Jewry', 'Edward I forbids Jewish moneylending and allows Jews to trade or live by their labour.', 'before', None, 'src', f'{ABR}, ch. VI'),
    (1278, None, None, 'Coinage arrests', 'All the Jews of England imprisoned in one night, their property seized and houses searched, ahead of an inquiry into the coinage.', 'condemned', None, 'src', f'{ABR}, ch. VIII, c. p. 49'),
    (1308, None, None, 'Inquiry into the Domus', 'An inquiry covering 1280 to 1308 lists 34 converts alive in 1280 and since dead, and 23 men and 28 women living.', 'domus', 'london', 'src', 'Adler, Domus Conversorum, App. III, pp. 38–39'),
    (1284, 1, 22, 'Order to remove Jews from towns without chests', 'Draft order to the justices of the Jews that Jews be peaceably removed from cities and towns where there are no archae.', 'before', None, 'db', 'TNA SC 1/13/95'),
    (1287, None, None, 'Expulsion from Gascony', 'Edward I, in Gascony, orders all Jews to leave the duchy.', 'expulsion', None, 'verify', f'{ABR}, ch. XI (the OCR text gives no year; 1287 is reference knowledge)'),
    (1290, 2, 20, 'Chevage for the converts', 'Two converts commissioned to collect the poll tax on Jews of twelve and over for the Domus.', 'domus', None, 'src', 'CPR 1281–92, p. 398'),
    (1290, 7, 18, 'Writs of expulsion', 'Writs to the sheriffs: all Jews to leave England before All Saints (1 November), on pain of death.', 'expulsion', None, 'src', f'{ABR}, ch. XI, c. p. 69'),
    (1290, 7, None, 'Safe-conduct to the Cinque Ports', 'The ports to give the departing Jews, their wives, children and goods safe and speedy passage at moderate charges.', 'expulsion', 'winchelsea', 'src', 'CPR 1281–92, p. 378'),
    (1290, 8, 21, 'The Jews of York', 'Safe-conducts for Bonamy of York, his son Jocem and the other Jews of York.', 'expulsion', 'york', 'src', 'CPR 1281–92, pp. 379, 382'),
    (1290, 10, 9, 'The London Jews leave', 'On St Denis’s Day the Jews of London set out for the coast. A shipmaster drowns a party of the richer exiles at the mouth of the Thames; he and his accomplices are later hanged.', 'expulsion', 'london', 'src', f'{ABR}, ch. XI, c. pp. 70–71'),
    (1290, 10, 27, 'New keeper of the Domus', 'Walter de Agmodesham appointed keeper of the Domus Conversorum.', 'domus', 'london', 'src', 'CPR 1281–92, p. 392'),
    (1290, 11, 1, 'All Saints: the deadline', 'The term set by the writs of 18 July. One party of 1,335, mostly poor, went to Flanders; others reached France, where in 1291 they were ordered to leave.', 'expulsion', None, 'src', f'{ABR}, ch. XI, c. p. 71'),
    (1290, None, None, 'Eighty converts', 'Eighty converted Jews were receiving the king’s alms in the year of the Expulsion: 1½d. a day for a man, 1d. for a woman.', 'domus', 'london', 'src', 'Adler, Domus Conversorum, pp. 2–3 (Patent Roll 1290, m. 19)'),
    (1290, 12, None, 'Sale of the houses', 'Hugh de Kendale appointed to value and sell the houses, rents and tenements of the Jews. Abrahams: their yearly value was about £130; nearly all were given to the king’s friends.', 'property', None, 'src', f'CPR 1281–92, p. 410; {ABR}, ch. XI, c. pp. 72–73'),
    (1291, None, None, 'Chests delivered to the Exchequer', 'Memorandum of the delivery of the chests of chirographs of Jews to the treasurer and barons. Abrahams puts the registered debts at about £9,100.', 'bonds', None, 'db', f'TNA E 101/249/29; {ABR}, ch. XI, c. p. 72'),
    (1291, 4, None, 'Northampton: the School of the Jews', 'Edward I grants the School of the Jews of Northampton to St James’s Abbey.', 'property', 'northampton', 'src', 'CPR 1313–17, p. 199 (inspeximus)'),
    (1291, 10, 22, 'Hereford houses granted', 'Houses of Civitasse, Elias de Ardre and Aaron le Blund, Jews of Hereford, granted at nominal rents.', 'property', 'hereford', 'src', 'CPR 1441–46, p. 362 (inspeximus)'),
    (1292, 2, None, 'The converts’ endowment', '£202 0s. 4d. a year at the Exchequer for the converts, each portion to lapse at the convert’s death.', 'domus', 'london', 'src', 'CPR 1281–92, p. 478'),
    (1293, None, None, 'Colchester: the School of the Jews', 'The School of the Jews and eight Jewish households’ houses at Colchester granted to William son of Jordan de Brokesburn.', 'property', 'colchester', 'src', 'CPR 1292–1301, p. 18'),
    (1305, None, None, 'The London synagogue', 'The chapel of the Friars of the Sack in Coleman Street, ‘lately the synagogue of the Jews’, assigned for a chantry.', 'property', 'london', 'src', 'CPR 1301–07, p. 316'),
    (1315, None, None, 'Debts still outstanding', 'Confirmations of 1315 and 1327 of the renunciation of interest show debts to the Jews still being collected; Edward III gave up the claim.', 'bonds', None, 'src', f'{ABR}, ch. XI, c. p. 73'),
    (1367, None, None, '‘About ninety years’', 'A York title case in King’s Bench pleads back to the time when ‘the Jews were put into exile out of the realm of England, about ninety years since’ (circiter quaterviginti et decem annos elapsos).', 'property', 'york', 'db', 'Glyph Machina, KB27 roll 432, fronts, image 0175, and dorses, image 0341 (dated 1354 and c. 1367 by Glyph Machina)'),
    (1377, 4, 11, 'The Domus annexed to the Rolls', 'The Domus Conversorum annexed for ever to the office of Keeper of the Rolls of Chancery.', 'domus', 'london', 'src', 'CPR 1381–85, p. 269'),
    (1403, 4, 25, 'Elizabeth, daughter of Rabbi Moses', 'A convert in the Domus, daughter of ‘the bishop of the Jews’, given an extra penny a day.', 'domus', 'london', 'src', 'CPR 1401–05, p. 216; Adler, p. 59'),
    (1465, None, None, 'Lincoln: the last small sums', 'Small yearly sums from Lincoln houses late of Ursel Levy, Diabella and Belasset granted away by the Crown.', 'property', 'lincoln', 'src', 'CPR 1461–67, p. 499'),
    (1596, None, None, 'Last escheat charge found', 'The Lincoln charge on the houses of Diabella, held by the heirs of Robert de Leverton, still on the pipe roll.', 'property', 'lincoln', 'db', 'Glyph Machina, E372 roll 405, fronts, image 0032'),
    (1608, None, None, 'Last resident in Adler’s list', 'Nathaniel Menda, formerly Jehooda Menda, in the Domus 1578–1608; Adler counts 48 inmates from 1330 to 1608.', 'domus', 'london', 'src', 'Adler, Domus Conversorum, pp. 58–60'),
    (1656, None, None, 'Readmission', 'Adler’s ‘Middle Period’ of Anglo-Jewish history closes with Cromwell; the date of readmission is reference knowledge.', 'presence', None, 'verify', 'Adler, Domus Conversorum, p. 2 (1290–1656)'),
]

# ------------------------------------------------------------------ the Domus: residents after 1290 (Adler, App. XXI, pp. 59–60)
# (n, name, from, to, sex, note). '?' end years drawn to the start year + 1.
RESIDENTS = [
    (1, 'Walter of Nottingham', 1330, 1336, 'm', ''), (2, 'Richard, son of Claricia of Exeter', 1337, 1350, 'm', ''),
    (3, 'Katherine, daughter of Claricia of Exeter', 1337, None, 'f', ''), (4, 'John, son of Edward St John', 1337, 1337, 'm', ''),
    (5, 'William, son of Edward St John', 1337, 1337, 'm', ''), (6, 'William of Leicester', 1350, 1350, 'm', ''),
    (7, 'John of Hatfield', 1350, 1350, 'm', ''), (8, 'John of Castile', 1356, None, 'm', ''),
    (9, 'John de Sancte Marie of Spain', 1371, 1405, 'm', ''), (10, 'Laurentius de Saint Martin', 1375, 1375, 'm', 'about 1375'),
    (11, 'John of Kingston', 1375, 1375, 'm', 'about 1375'), (12, 'Thomas of Acres', 1375, 1375, 'm', 'about 1375'),
    (13, 'Edmund', 1375, 1375, 'm', 'about 1375'), (14, 'Peter', 1375, 1375, 'm', 'about 1375'),
    (15, 'Aseti Briarti of France', 1386, 1393, 'm', ''), (16, 'Perota, his wife', 1386, 1393, 'f', ''),
    (17, 'Thomas Levyn of Spain', 1393, 1393, 'm', ''), (18, 'Elizabeth, daughter of Rabbi Moses, Episcopus Judaeorum', 1399, 1416, 'f', ''),
    (19, 'William of Leicester', 1401, 1417, 'm', ''), (20, 'Johanna of Dartmouth', 1409, 1449, 'f', ''),
    (21, 'Alice, her daughter', 1409, 1454, 'f', ''), (22, 'William of St Jacques', 1409, 1416, 'm', ''),
    (23, 'Henry of Woodstock', 1413, 1416, 'm', ''), (24, 'Martin, his son', 1413, 1468, 'm', ''),
    (25, 'Peter, his son', 1413, 1416, 'm', ''), (26, 'Henry of Stratford', 1416, 1441, 'm', ''),
    (27, 'John Durdraght', 1425, 1455, 'm', ''), (28, 'Alver Oliver', 1438, 1446, 'm', ''),
    (29, 'John Seyt', 1448, 1488, 'm', ''), (30, 'Henry of Eton', 1450, 1453, 'm', ''),
    (31, 'Edward of Westminster', 1461, 1503, 'm', 'absent three years'), (32, 'Edward Brandon', 1468, 1472, 'm', ''),
    (33, 'Edward Beauchamp', 1482, 1487, 'm', ''), (34, 'John Fernando', 1487, 1503, 'm', ''),
    (35, 'Henry Vaughan', 1487, 1488, 'm', ''), (36, 'Henry of Windsor', 1488, 1509, 'm', ''),
    (37, 'Edward Brampton', 1488, 1488, 'm', ''), (38, 'Elizabeth Portingale', 1492, 1538, 'f', ''),
    (39, 'Edward Scales', 1503, 1527, 'm', ''), (40, 'Elizabeth Baptista', 1504, 1532, 'f', ''),
    (41, 'Katherine Wheteley (formerly Aysa Pudewya)', 1532, 1548, 'f', ''), (42, 'Mary Cook (formerly Omell Faitt Isya)', 1532, 1551, 'f', ''),
    (43, 'Nathaniel Menda (formerly Jehooda Menda)', 1578, 1608, 'm', ''), (44, 'Fortunati Massa (formerly Cooba Massa)', 1581, 1598, 'f', ''),
    (45, 'Philip Ferdinandus', 1598, 1600, 'm', ''), (46, 'Elizabeth Furdinando', 1603, None, 'f', ''),
    (47, 'Arthur Antoe', 1605, None, 'm', ''), (48, 'Jacob Wolfgang', 1606, None, 'm', ''),
]
RESIDENTS_NOTE = ('Adler’s complete list of inmates from 1330, ‘the first record after the Expulsion’: thirty-eight men and ten women, '
                  'besides four men whose residence is doubtful (Edward of Brussels 1339, Janato of Spain 1345, John of St Paul 1345, William Piers 1382). '
                  'Adler assigns sexes by name; Fortunati Massa is listed by him among the ten women.')

# ------------------------------------------------------------------ keepers of the Domus named in the Patent Rolls (appointments)
# (name, year, ref). The TNA account series (E 101/249-255) adds the keepers with surviving accounts; build.py merges the two.
KEEPERS_CPR = [
    ('John de St Denis', 1283, 'CPR 1281–92, pp. 88, 228'), ('Richard de Clympinges', 1289, 'CPR 1281–92, p. 335'),
    ('Walter de Agmodesham', 1290, 'CPR 1281–92, p. 392'), ('Henry de Bluntesdon', 1298, 'CPR 1340–43, p. 236 (exemplification of 10 Apr. 26 Edw. I)'),
    ('Adam de Osgodeby', 1313, 'CPR 1313–17, pp. 39, 356'), ('William de Ayremynne', 1321, 'CPR 1321–24, pp. 32, 36'),
    ('Robert de Holden', 1325, 'CPR 1324–27, pp. 176, 199'), ('Richard de Ayremynne', 1327, 'CPR 1327–30, pp. 42, 334'),
    ('John de St Paul', 1341, 'CPR 1340–43, p. 236'), ('Henry de Ingelby', 1350, 'CPR 1348–50, pp. 475, 481'),
    ('William de Burstall', 1371, 'CPR 1370–74, p. 128'), ('Thomas Kirkeby', 1447, 'CPR 1446–52, p. 108'),
    ('William Morland', 1470, 'CPR 1467–77, p. 245'), ('John Alcock', 1471, 'CPR 1467–77, p. 259 (calendar ‘Alsofe’)'),
    ('John Morton', 1472, 'CPR 1467–77, pp. 334, 515'), ('Robert Morton', 1477, 'CPR 1477–85, p. 71'), ('Thomas Barowe', 1483, 'CPR 1477–85, p. 462'),
]

# ------------------------------------------------------------------ the fossil charges: what the entries say about each charge's origin
PROP_META = {
    'bri_bonefey': dict(origin='henry3', origin_year=1232, origin_note='The entries cite the pipe rolls of 16 and 27 Henry III (1231–32, 1242–43): the charge predates 1290.', short='Bristol · Bonefey'),
    'bri_jospin': dict(origin='henry3', origin_year=1241, origin_note='The entries date the grant to Peter Miparty from 16 July, 25 Henry III (1241): the charge predates 1290.', short='Bristol · Jospin'),
    'lin_ursel': dict(origin='expulsion', origin_year=1291, origin_note='Granted to Adam Cokerel from 27 March, 19 Edward I (1291). ‘Wikeford’ is Wigford, the Lincoln suburb with St Mark’s parish, not Wickford in Essex.', short='Lincoln · Ursel Levy'),
    'lin_diabella': dict(origin='condemned', origin_year=None, origin_note='The entries call Diabella ‘dampnata’, condemned: a forfeiture before 1290, probably of the coinage trials. Robert de Leverton also held houses of Benedict son of Diabella and the School of the Jews.', short='Lincoln · Diabella'),
    'lin_belasset': dict(origin='unknown', origin_year=None, origin_note='Belasset of Wallingford (CPR 1461–67, p. 499; E159 roll 85). How the houses came to the king is not stated in the lines read.', short='Lincoln · Belasset'),
    'oxf_mosse': dict(origin='expulsion', origin_year=1299, origin_note='The entries cite the pipe roll of 27 Edward I (1298–99); the houses in St Aldate’s include the School of the Jews of Oxford.', short='Oxford · Mosse son of Jacob'),
    'cam_jocei': dict(origin='expulsion', origin_year=1291, origin_note='Granted in 19 Edward I (1290–91) to John But of Cambridge.', short='Cambridge · Jocei'),
    'lon_bagard': dict(origin='expulsion', origin_year=1291, origin_note='The houses of Elias Bagard and of his son Mosse are ‘escheats of the king by the exile of the Jews’ (E368 roll 78).', short='London · Elias Bagard'),
    'lon_benhagin': dict(origin='expulsion', origin_year=1291, origin_note='Houses in Catte Street, parish of St Lawrence in the Jewry, among the London grants of 19 Edward I entered on the pipe roll (E372 roll 163); still pleaded as in Cripplegate ward in the 1440s.', short='London · Benedict son of Hagin'),
    'oxf_vives': dict(origin='condemned', origin_year=None, origin_note='Vives le Yonge is called ‘suspensus’, hanged. The HTR reads the town as both Exonie and Oxon; the entries sit with the Oxford rents, and TNA SC 8/67/3303 (1337–38) asks for an inquiry into ‘a toft in the suburb of Oxford, once held by Vive le Longe, a Jew who was hanged for felony’. Custody of the house was let to John Mareys, clerk of the Exchequer.', short='Oxford · Vives le Yonge'),
}
ORIGINS = [('henry3', 'Escheated under Henry III'), ('condemned', 'Forfeited by a condemned Jew'), ('expulsion', 'Escheated at the Expulsion'), ('unknown', 'Origin not stated in the lines read')]

# ------------------------------------------------------------------ the earlier Glyph Machina assistant sweep (pasted 8 Oct 2026)
# (year or None, type, town, summary, reference, quoted HTR text). Matched against this atlas's own hits in build.py.
PRIOR = [
    (None, 'before', 'york', 'Aaron of York on the pipe roll', 'E372 roll 92, image 5849', 'Aaron iudeus Eboracensi'),
    (None, 'before', 'nottingham', 'Vives, Jew of Nottingham', 'E372 roll 86', 'Vives iudeus de Notingham'),
    (None, 'before', None, 'Fine of a gold mark from the community of the Jews of England', 'E372 roll 116, image 2634', 'universitas iudeorum Anglie'),
    (None, 'before', 'winchester', 'Debts of Licoricia of Winchester', 'E372 roll 112, image 0361', ''),
    (1277, 'before', 'winchester', 'Eyre inquest into the killing of Licoricia of Winchester', 'JUST1 roll 784, image 0066', 'catalla diversorum iudeorum et ipsius Licoricie occise in predicta domo'),
    (None, 'before', 'ware', 'Bonamy the Jew, called Baker, and Idonea of Bristol, Jewess, at Ware', 'JUST1 roll 547A, image 5857', 'Bonamy Iudeus dictus Bakere'),
    (None, 'before', None, 'Chattels of slain Jews in the eyre', 'JUST1 rolls 902–903', 'catalla iudeorum occisorum'),
    (None, 'before', None, 'Justices for the custody of the Jews', 'JUST1 roll 616', 'ad custodiam iudeorum'),
    (None, 'domus', None, 'Chevage: 3d. a head on every Jew', 'E101 roll 249, image 0174', 'pro capite cuiuslibet Iudei iij d.'),
    (None, 'bonds', None, 'A starr (Hebrew bond) pleaded', 'E101 roll 249', ''),
    (1302, 'bonds', 'london', 'Last reference to an archa: debts of the London Jews found in the chest', 'E101 roll 249, image 0087', 'debita judeorum Londonium per curiam inventa in Archa loci'),
    (None, 'bonds', 'york', 'Bonds and charters from the old chest of the Jews of England, come to the king after their abjuration; sales of houses in York', 'E101 roll 250, image 0109', 'obligationes et carte de veteri cista iudeorum Anglie que ad manus Regis devenerunt post abiurationem eorundem a Regno'),
    (None, 'property', None, 'Property in the king’s hand by the exile of the Jews (Edward III)', 'E159 roll 132, image 7105', 'in manu Regis per exilium iudeorum'),
    (None, 'bonds', None, 'Pardon of debts of the Jews (Edward III)', 'E159 roll 122, image 3243', 'de debitis iudeorum'),
    (None, 'domus', 'london', 'John de St Paul, keeper; wages of converted men and women', 'E368 roll 116, image 0294', 'conversorum hominum … et mulierum'),
    (None, 'domus', 'london', 'Wages of the converts', 'E159 roll 125, image 8754', ''),
    (1319, 'domus', 'london', 'William de Ayremynne, keeper of the House of Converts, litigating over its free tenements', 'E159 roll 100, image 0204; CP40 roll 240, image 0133', 'custos domus Conversorum London'),
    (None, 'bonds', 'hereford', 'Archa cirographorum at Hereford and Colchester', 'C66 roll 92, image 0063', 'archa cirographorum Judeorum'),
    (None, 'bonds', 'northampton', 'Archa cirographorum at Northampton', 'E159 roll 20, image 0041', 'archa cirographorum Judeorum'),
    (1298, 'property', 'devizes', 'Survey of the houses of Moses, Jew, at Devizes', 'E368 roll 72, dorses, image 0276', 'domorum que fuerunt [Moses] Iudei in villa de Devises de tempore quo post exilium'),
    (1302, 'property', 'london', 'Arrears of rent ‘from the time the houses were in the Jew’s hand or the king’s by escheat’', 'E368 roll 74, fronts, image 0392', 'tempore quo domus illi fuerunt in manu dicti Iudei vel in manu regis per escaetam'),
    (1367, 'property', 'york', 'York title case: Jocens son of Bonaunt seised of a messuage in Castlegate when he was put into exile with the other Jews', 'KB27 roll 432, dorses, image 0341; roll 431, dorses, image 0420', 'tempore quo positus fuit cum aliis Iudeis in exilium extra regnum'),
    (1427, 'property', 'bristol', 'Bristol: houses of Jospin (Iosce), Henry VI', 'E372 roll 285, image 0002', 'firma cuiusdam domus et quorundam redditus que fuerunt [Iosce] iudei in Bristoll'),
    (1462, 'property', 'bristol', 'Bristol: the same charges under Edward IV', 'E372 roll 307, images 0009–10', ''),
    (1518, 'property', 'bristol', 'Bristol: the same charges in 1518', 'E372 roll 370', ''),
    (1559, 'property', 'lincoln', 'A Jewish escheat on the pipe roll of 1559 (the sweep called it Marian and placed it at Bristol; the hit read here is Lincoln, Diabella and Belasset)', 'E372 roll 401, image 0032', ''),
    (1464, 'property', 'lincoln', 'The sweep read ‘Wickford’ as Wickford, Essex; the hit is Ursel Levy of Wigford, Lincoln', 'E368 roll 239, image 0084', ''),
]

FLAGS = [
    ('The formula is not proof of an Expulsion escheat', 'The phrase “que fuerunt … Iudei” marks a Jewish former owner. The two Bristol charges that run longest (to 1529 and 1575) cite pipe rolls of 16 and 27 Henry III and a grant of 1241; Diabella of Lincoln is “dampnata” and Vives le Yonge of Oxford “suspensus”. Only some of the long charges began in 1290. The Houses & rents view sorts each charge by what its own entries say.'),
    ('Wickford is Wigford', 'The earlier sweep placed a Jewish escheat at Wickford (E368 roll 239, image 0084). The entries name Ursel Levy “de Wikeford in parochia Sancti Marci”, and CPR 1461–67, p. 499 puts his houses in Lincoln: Wigford, the suburb with St Mark’s church.'),
    ('The 1559 roll', 'The sweep called E372 roll 401 (image 0032) “Marian” and grouped it with the Bristol charge. The hit read here is dated 1559 (Elizabeth I) and charges Lincoln houses of Diabella and Belasset.'),
    ('Raw counts after 1290 are mostly noise', 'An any-word search for iudeus, iudei, iudeorum and five other forms returns 37,683 entries, more after 1290 than before. In a sample of 25 Common Pleas hits from the 1330s, the matches are “Iudeo” for ideo (“Ideo sicut pluries preceptum est”) and the feast of SS Simon and Jude (“festum apostolorum Simonis et Iude”); none clearly names a Jew. The Overview uses anchored formulae only; the raw curve is shown in Sources & method as a warning.'),
    ('Two keepers in 1327', 'The Patent Roll grants the Domus to Richard de Ayremynne for life in March 1327, but a 1341 exemplification recites letters of 7 November, 1 Edward III, appointing Adam de Osgodeby. One reading is wrong, or the grants overlap.'),
    ('Walter of Nottingham', 'Adler’s first post-Expulsion inmate is “Walter of Nottingham” (1330–36). The Patent Roll protection of March 1331 names “Master Walter de Croydon … lately received among the conversi”, dated at Nottingham. Adler may have taken the place-date for a surname, or worked from a different record.'),
    ('Exonie is Oxonie', 'The HTR often reads the Oxford rents as “ville Exonie”. The house of Vives le Yonge, hanged, at first looked like an Exeter charge; other lines on the same images read “in suburbia Oxon”, and a petition of 1337–38 (SC 8/67/3303) places the toft of “Vive le Longe … hanged for felony” in the suburb of Oxford. It is mapped at Oxford.'),
    ('Chellesworthy', 'The CPR’s “Chellesworthy alias Chollesworthy, co. Devon”, in the king’s hands “by the exile of the Jews” from 1401 to 1461, is mapped at Chilsworthy near Holsworthy. The identification is a guess.'),
    ('County rolls placed at towns', 'The rolls of obligations of 1291–93 (E 101/250/2–12) are by county. They are placed at each county’s main Jewry (Gloucestershire at Gloucester, Wiltshire at Devizes, Huntingdon and Cambridge at Cambridge), which may not be where the chest was kept.'),
    ('Gascony, 1287', 'The year of the Gascon expulsion is reference knowledge: the OCR of Abrahams has no year at that point and misprints Edward’s departure as 1280.'),
    ('Machine transcriptions', 'Every Glyph Machina line is uncorrected HTR. Names and sums in this atlas that come only from Glyph Machina should be read on the image before citing; the links open the image pages.'),
]

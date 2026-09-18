#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento andata e ritorno
Borgo Il Poggiaccio (Sovicille) - Antinori nel Chianti Classico (Bargino)
di sabato 19 settembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_sovicille_antinori.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_sovicille_antinori.py --lingua en --cliente "Client Name"
"""

import argparse
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

# --- identita' visiva GiroMunna -------------------------------------------------
GREEN = colors.HexColor("#1F4636")
GOLD = colors.HexColor("#C9A24B")
INK = colors.HexColor("#2B2B2B")
MUTED = colors.HexColor("#6B6B6B")
RULE = colors.HexColor("#E4E1D8")
CREAM = colors.HexColor("#F5F3EE")

HERE = os.path.dirname(os.path.abspath(__file__))


def _trova_logo():
    """Il logo sta in Preventivi/assets/, condiviso da tutti i preventivi."""
    for base in (HERE, os.path.dirname(HERE)):
        p = os.path.join(base, "assets", "giromunna_logo.png")
        if os.path.exists(p):
            return p
    return os.path.join(HERE, "assets", "giromunna_logo.png")


LOGO = _trova_logo()

MARGIN = 20 * mm
TOP = 30 * mm
BOTTOM = 24 * mm

RIF = "GM-2026-0919-TB"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Borgo Il Poggiaccio (Sovicille) → Antinori nel Chianti Classico (Bargino) e ritorno  ·  sabato 19 settembre 2026",
    meta="Preparato per %s  ·  18 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un solo minibus per il vostro gruppo di 18-20 ospiti, con lo stesso conducente per tutta la giornata."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 18-20 ospiti a bordo restano da sei a otto posti liberi: il gruppo viaggia comodo su un mezzo solo, "
        "senza bisogno di dividerlo. I 7,64 metri contano su entrambi i capi del percorso: la strada di accesso a "
        "Borgo Il Poggiaccio e il piazzale di Antinori si affrontano senza problemi con un mezzo di questa lunghezza, "
        "dove un autobus gran turismo avrebbe più di una difficoltà."
    ),
    h_servizio="Il servizio",
    svc_intro=(
        "Sabato 19 settembre 2026. Distanze e tempi di percorrenza sono stime stradali, traffico escluso."
    ),
    svc_head=["Orario", "Percorso", "Percorrenza"],
    svc=[
        ("09:00",
         "<b>Il mezzo parte a vuoto da Ponte Buggianese (PT), dove ha sede l'azienda.</b> "
         "Circa 115 km fino a Sovicille per essere al Poggiaccio con un quarto d'ora di anticipo. "
         "Nessun passeggero a bordo e nessun addebito a parte: è compreso nel prezzo.",
         "circa 115 km · 1 h 40"),
        ("10:45",
         "<b>Residenza d'Epoca Borgo Il Poggiaccio, Strada Provinciale Maremmana 541, Sovicille (SI).</b> "
         "Si esce verso Siena, si prende il raccordo Firenze-Siena senza entrare in città e si esce a Bargino.",
         "circa 55 km · 55 min"),
        ("11:40 – 16:00",
         "<b>Antinori nel Chianti Classico / Rinuccio 1180, Via Cassia per Siena 133, Bargino (FI).</b> "
         "Arrivo verso le 11:40. Mezzo e conducente restano sul posto a vostra disposizione per tutta la visita "
         "e per il pranzo: non vi lasciamo e non ripartiamo, così gli orari li decidete voi sul momento.",
         "a disposizione"),
        ("15:00 – 16:00",
         "<b>Antinori nel Chianti Classico → Borgo Il Poggiaccio.</b> "
         "Partenza nella finestra che ci indicate, stesso percorso a ritroso, rientro alla struttura entro un'ora.",
         "circa 55 km · 55 min"),
        ("17:00",
         "<b>Il mezzo rientra a vuoto a Ponte Buggianese.</b> "
         "Altri 80 km senza passeggeri a bordo, conducente in base verso le 18:00: nona ora di lavoro "
         "della giornata, anch'essa compresa nel prezzo.",
         "circa 80 km · 1 h 10"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 19 set — giornata a disposizione: Borgo Il Poggiaccio → Antinori nel Chianti Classico → "
         "Borgo Il Poggiaccio, mezzo e conducente con voi dalle 10:45 alle 16:00, viaggio del mezzo da e per "
         "la nostra sede compreso", "€ 1.200,00", "+ IVA 10%"),
        ("Supplemento per conferma e servizio sotto le 24 ore dalla richiesta, 25%", "€ 300,00", "+ IVA 10%"),
        ("Vitto del conducente, il pranzo durante l'attesa", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.500,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.650,00.",
    perhead=("Sono da € 82,50 a € 91,67 a persona secondo il numero definitivo, per l'intera giornata "
             "di un mezzo da 26 posti con conducente."),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi, parcheggi, assicurazione completa e "
        "movimentazione bagagli. Nessun onere di accesso: né Sovicille né Bargino sono in zona a traffico limitato, "
        "il percorso aggira Siena sul raccordo senza entrare in città — quindi non serve il permesso comunale per "
        "i bus turistici — e Antinori nel Chianti Classico dispone di un proprio piazzale. Nessuna voce a sorpresa "
        "il giorno del servizio: il viaggio del mezzo da e per la nostra sede è già in tabella, non arriva dopo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il vitto del conducente, che resta a vostro carico: il pranzo durante l'attesa a Bargino lo prenotate e "
        "pagate voi direttamente. Visita, degustazione, pranzo, guide e mance in cantina. Attesa oltre le 16:00 "
        "alla partenza da Antinori, € 50,00 all'ora. Soste aggiuntive o modifiche al percorso, quotate su richiesta. "
        "Rientro dopo le 02:00, € 250,00."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 495,00", "IVA inclusa"),
        ("Saldo", "€ 1.155,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Il budget che ci avete indicato.</b> € 250-300 per l'andata e ritorno non corrispondono a questo "
         "servizio, e non esiste una versione del preventivo che ci arrivi. Su venti passeggeri la vostra cifra "
         "fa € 12-15 a testa per l'intera giornata di un mezzo da 26 posti con conducente: è il prezzo di una "
         "corsa urbana in taxi, non di quello che ci avete chiesto. Se il budget non è spostabile non ha senso "
         "andare avanti, e ve lo diciamo oggi perché vi resta un giorno per organizzarvi diversamente."),
        ("<b>Perché costa più dei 55 km che avete in mente.</b> La tratta Sovicille-Bargino è di 55 km, ma non "
         "è quello che state comprando. GiroMunna ha sede a Ponte Buggianese, in provincia di Pistoia: per essere "
         "al Poggiaccio alle 10:45 il mezzo parte alle 09:00 e percorre circa 115 km senza nessuno a bordo, e la "
         "sera ne fa altri 80 per rientrare. La giornata del mezzo è di circa 300 km e nove ore di conducente, per "
         "110 km di trasporto passeggeri e quattro ore di attesa ferma a Bargino. È tutto compreso nel prezzo qui "
         "sopra e nessun supplemento vi arriverà dopo: ve lo spieghiamo perché il conto torni, non per "
         "addebitarvelo a parte."),
        ("<b>Il supplemento per le ventiquattr'ore.</b> La vostra richiesta è arrivata ieri sera per domani "
         "mattina. Un servizio confermato con meno di ventiquattro ore di preavviso comporta da noi un "
         "supplemento del 25%, ed è una voce che scriviamo in chiaro invece di nasconderla nel prezzo: significa "
         "rimettere mano al programma del conducente a settimana già chiusa e rinunciare a quello che potrebbe "
         "entrare nel frattempo per una giornata che teniamo bloccata sulla vostra risposta. Nasce dai tempi, non "
         "dal servizio: con due settimane di anticipo lo stesso lavoro questo supplemento non l'avrebbe."),
        ("<b>Liberare il mezzo durante il pranzo costerebbe di più, non di meno.</b> La domanda arriva sempre, "
         "quindi la anticipiamo. Lasciarvi a Bargino, far rientrare il minibus e tornare a prendervi significa "
         "quattro trasferimenti a vuoto invece di due: circa 160 km in più di quelli già in tabella. Tenere mezzo "
         "e conducente fermi sul posto è la formula più economica delle due, oltre che l'unica che vi lascia "
         "decidere l'ora del rientro stando a tavola."),
        ("<b>Il mezzo è libero e ve lo teniamo fino a stasera.</b> Abbiamo verificato: sabato 19 il Beluga è "
         "disponibile e il conducente anche. Lo teniamo fermo per voi <b>fino alle 20:00 di oggi</b>. Oltre "
         "quell'ora il conducente va organizzato diversamente e non possiamo più garantirvelo, quindi se la cosa "
         "vi interessa conviene una telefonata al +39 335 587 4744 e non uno scambio di mail."),
        ("<b>La prenotazione in cantina.</b> Antinori nel Chianti Classico e il ristorante Rinuccio 1180 ricevono "
         "solo su prenotazione, e un gruppo di venti persone di sabato non entra senza. Ci serve l'orario esatto "
         "che vi hanno dato: il ritrovo alle 10:45 è tarato su una visita che comincia verso mezzogiorno. Se "
         "l'orario è un altro spostiamo la partenza, senza variazione di prezzo."),
        ("<b>Il vitto del conducente.</b> La giornata non richiede pernottamenti — si parte e si rientra in serata "
         "— quindi non avete alcun costo di alloggio. Resta il pranzo del conducente durante le quattro ore di "
         "attesa a Bargino, che per prassi è a carico del cliente: non lo mettiamo a preventivo e non lo "
         "organizziamo noi. Il modo più semplice è aggiungere un coperto per lui quando prenotate da Rinuccio 1180."),
        ("<b>Il punto di ritrovo al Poggiaccio.</b> La struttura si raggiunge dalla Strada Provinciale Maremmana "
         "per un tratto di strada di campagna. Il nostro minibus da 7,64 m ci arriva, dove un autobus gran turismo "
         "avrebbe più di una difficoltà, ma fatevi confermare dalla reception il punto esatto di salita e lo spazio "
         "di manovra: meglio stasera che domattina con venti persone e le valigie in mano."),
        ("<b>L'orario di partenza da Antinori.</b> La finestra fra le 15:00 e le 16:00 va bene così e non serve "
         "stringerla adesso: il conducente resta sul posto e parte quando siete pronti entro le 16:00. Oltre "
         "quell'ora si applica l'attesa a € 50,00 all'ora. Se sapete già che il pranzo finirà più tardi, ditecelo "
         "e spostiamo la finestra in preventivo senza sovrapprezzo."),
        ("<b>Pagamento, viste le ventiquattr'ore.</b> Le condizioni di casa prevedono il 30% alla conferma e il "
         "saldo dopo, ma con il servizio domani un bonifico non fa in tempo ad arrivare: per noi la contabile "
         "dell'acconto vale come conferma e il saldo si regola il giorno stesso."),
        ("<b>Cancellazione.</b> La nostra scala di penali prevede il 100% del prezzo nei dieci giorni che "
         "precedono il servizio, e qui ne manca uno. Una volta confermato, il preventivo è dovuto per intero anche "
         "in caso di rinuncia. Vale la pena saperlo prima di dire di sì."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, l'orario della prenotazione in "
         "cantina, un recapito telefonico o WhatsApp della persona che viaggia con il gruppo e i vostri dati di "
         "fatturazione. Preventivo valido fino alle 20:00 di oggi, 18 settembre 2026."),
    ],
    closing=("Il mezzo è fermo e vi aspetta fino a stasera: per confermare o per qualsiasi chiarimento, "
             "il telefono è il canale più rapido.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Borgo Il Poggiaccio (Sovicille) → Antinori nel Chianti Classico (Bargino) and back  ·  Saturday 19 September 2026",
    meta="Prepared for %s  ·  18 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "A single minibus for your group of 18-20 guests, with the same driver for the whole day."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 18-20 guests on board, six to eight seats stay free: the group travels comfortably in one vehicle, "
        "with no need to split it. The 7.64 m length matters at both ends of the route — the access road to "
        "Borgo Il Poggiaccio and the forecourt at Antinori are both straightforward for a vehicle this size, "
        "where a full-size coach would meet more than one difficulty."
    ),
    h_servizio="The service",
    svc_intro=(
        "Saturday 19 September 2026. Distances and journey times are road estimates, traffic excluded."
    ),
    svc_head=["Time", "Route", "Distance"],
    svc=[
        ("09:00",
         "<b>The vehicle leaves Ponte Buggianese (PT), where the company is based, empty.</b> "
         "About 115 km to Sovicille, to be at the Poggiaccio fifteen minutes early. "
         "No passengers on board and nothing charged separately: it is included in the price.",
         "approx. 115 km · 1 h 40"),
        ("10:45",
         "<b>Residenza d'Epoca Borgo Il Poggiaccio, Strada Provinciale Maremmana 541, Sovicille (SI).</b> "
         "Out towards Siena, onto the Florence-Siena dual carriageway without entering the city, "
         "and off at the Bargino exit.",
         "approx. 55 km · 55 min"),
        ("11:40 – 16:00",
         "<b>Antinori nel Chianti Classico / Rinuccio 1180, Via Cassia per Siena 133, Bargino (FI).</b> "
         "Arrival around 11:40. Vehicle and driver stay on site at your disposal for the visit and for lunch: "
         "we do not drop you off and drive away, so you set the timings on the day.",
         "at disposal"),
        ("15:00 – 16:00",
         "<b>Antinori nel Chianti Classico → Borgo Il Poggiaccio.</b> "
         "Departure within the window you give us, the same route back, at the property within the hour.",
         "approx. 55 km · 55 min"),
        ("17:00",
         "<b>The vehicle returns empty to Ponte Buggianese.</b> "
         "Another 80 km with no passengers on board, driver back at base around 18:00: the ninth hour of "
         "his day, included in the price as well.",
         "approx. 80 km · 1 h 10"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sat 19 Sep — day at disposal: Borgo Il Poggiaccio → Antinori nel Chianti Classico → "
         "Borgo Il Poggiaccio, vehicle and driver with you from 10:45 to 16:00, the vehicle's journey to and "
         "from our base included", "€ 1,200.00", "+ VAT 10%"),
        ("Supplement for confirmation and service within 24 hours of enquiry, 25%", "€ 300.00", "+ VAT 10%"),
        ("Driver's meal, lunch during the wait", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,500.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,650.00.",
    perhead=("That is € 82.50 to € 91.67 per person depending on the final count, for a full day of a "
             "26-seat vehicle with driver."),
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, fuel, tolls, parking, full insurance and luggage handling. "
        "No access charges apply: neither Sovicille nor Bargino lies in a restricted traffic zone, the route "
        "skirts Siena on the dual carriageway without entering the city — so no municipal tourist-coach permit "
        "is needed — and Antinori nel Chianti Classico has its own forecourt. Nothing surprises you on the day: "
        "the vehicle's journey to and from our base is already in the table above, not added afterwards."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meal, which remains at your charge: you book and pay for his lunch during the wait at "
        "Bargino directly. Winery visit, tasting, lunch, guides and gratuities. Waiting beyond 16:00 for the "
        "departure from Antinori, € 50.00 per hour. Additional stops or changes to the route, quoted on request. "
        "Return after 02:00, € 250.00."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 495.00", "VAT included"),
        ("Balance", "€ 1,155.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The budget you gave us.</b> € 250-300 for the round trip does not correspond to this service, and "
         "there is no version of this quotation that reaches it. Across twenty passengers your figure works out "
         "at € 12-15 a head for a full day of a 26-seat vehicle with driver: that is the price of a short taxi "
         "ride in town, not of what you have asked for. If the budget cannot move there is no point going further, "
         "and we are telling you today because it leaves you a day to arrange something else."),
        ("<b>Why it costs more than the 55 km you have in mind.</b> The Sovicille-Bargino leg is 55 km, but that "
         "is not what you are buying. GiroMunna is based at Ponte Buggianese, in the province of Pistoia: to be at "
         "the Poggiaccio at 10:45 the vehicle leaves at 09:00 and covers about 115 km with nobody on board, then "
         "another 80 km to get home in the evening. The vehicle's day comes to about 300 km and nine hours of the "
         "driver's time, for 110 km of passenger transport and four hours parked at Bargino. All of it is included "
         "in the price above and no supplement will reach you later: we explain it so the sum adds up, not to "
         "charge it separately."),
        ("<b>The twenty-four-hour supplement.</b> Your enquiry reached us yesterday evening for tomorrow "
         "morning. A service confirmed less than twenty-four hours ahead carries a 25% supplement with us, and it "
         "is a line we set out in plain sight rather than bury in the price: it means reopening the driver's "
         "schedule with the week already closed, and turning away whatever might come in for a day we are holding "
         "against your answer. It comes from the timing, not from the service: at two weeks' notice the same job "
         "would not carry it."),
        ("<b>Releasing the vehicle over lunch would cost more, not less.</b> The question always comes, so here is "
         "the answer in advance. Dropping you at Bargino, sending the minibus home and coming back for you means "
         "four empty runs instead of two: roughly 160 km on top of those already in the table. Keeping vehicle and "
         "driver parked on site is the cheaper of the two arrangements, and the only one that lets you decide the "
         "return time from the table."),
        ("<b>The vehicle is free and we are holding it until this evening.</b> We have checked: on Saturday 19th "
         "the Beluga is available and so is the driver. We are holding it for you <b>until 20:00 today</b>. Beyond "
         "that hour the driver has to be scheduled otherwise and we can no longer guarantee it, so if this is of "
         "interest to you a phone call to +39 335 587 4744 beats an exchange of emails."),
        ("<b>The winery booking.</b> Antinori nel Chianti Classico and the Rinuccio 1180 restaurant receive guests "
         "by reservation only, and a party of twenty on a Saturday will not get in without one. We need the exact "
         "time they have given you: the 10:45 pick-up is set against a visit starting around midday. If the time "
         "is different we move the departure, at no change in price."),
        ("<b>The driver's meal.</b> The day requires no overnight stay — out and back the same evening — so you "
         "have no accommodation cost at all. What remains is the driver's lunch during the four-hour wait at "
         "Bargino, which by custom is at the client's charge: we neither quote it nor arrange it. The simplest "
         "thing is to add a cover for him when you book at Rinuccio 1180."),
        ("<b>The pick-up point at the Poggiaccio.</b> The property is reached from the Strada Provinciale "
         "Maremmana along a stretch of country road. Our 7.64 m minibus manages it, where a full-size coach would "
         "meet more than one difficulty, but do have reception confirm the exact boarding point and the turning "
         "space: better tonight than tomorrow morning with twenty people and their luggage in hand."),
        ("<b>The departure time from Antinori.</b> The window between 15:00 and 16:00 is fine as it stands and "
         "need not be narrowed now: the driver stays on site and leaves when you are ready, up to 16:00. Beyond "
         "that hour the € 50.00 hourly waiting charge applies. If you already know lunch will run later, tell us "
         "and we will move the window in the quotation at no extra cost."),
        ("<b>Payment, given the twenty-four hours.</b> Our house terms are 30% on confirmation and the balance "
         "afterwards, but with the service tomorrow a bank transfer will not clear in time: the deposit's transfer "
         "receipt counts as confirmation for us and the balance is settled on the day."),
        ("<b>Cancellation.</b> Our scale charges 100% of the price within the ten days before the service, and one "
         "day remains. Once confirmed, the quotation is due in full even if you pull out. Worth knowing before "
         "saying yes."),
        ("<b>To confirm we need</b> the final passenger count, the time of the winery booking, a mobile or WhatsApp "
         "contact for the person travelling with the group, and your invoicing details. "
         "Quotation valid until 20:00 today, 18 September 2026."),
    ],
    closing=("The vehicle is standing by for you until this evening: to confirm, or for any clarification, "
             "the phone is the quickest channel.<br/><br/>"
             "Kind regards,<br/>"
             "Girolamo Munna — GiroMunna NCC, Tuscany · +39 335 587 4744 · info@giromunna.com"),
)


def styles():
    base = dict(fontName="Helvetica", textColor=INK, leading=13.2, fontSize=9.2)
    return {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=21,
                                textColor=GREEN, leading=24, spaceAfter=3),
        "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=10.2,
                                   textColor=INK, leading=14, spaceAfter=2),
        "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=8.6,
                               textColor=MUTED, leading=12, spaceAfter=14),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5,
                             textColor=GREEN, leading=15, spaceBefore=13, spaceAfter=6),
        "body": ParagraphStyle("body", alignment=TA_JUSTIFY, spaceAfter=6, **base),
        "cell": ParagraphStyle("cell", **base),
        "cellsm": ParagraphStyle("cellsm", fontName="Helvetica", fontSize=8.6,
                                 textColor=INK, leading=12),
        "cellmut": ParagraphStyle("cellmut", fontName="Helvetica", fontSize=8.6,
                                  textColor=MUTED, leading=12),
        "th": ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7.6,
                             textColor=GREEN, leading=10),
        "grand": ParagraphStyle("grand", fontName="Helvetica-Bold", fontSize=11.5,
                                textColor=GREEN, leading=15, spaceBefore=8),
        "note": ParagraphStyle("note", alignment=TA_JUSTIFY, spaceAfter=7,
                               leftIndent=9, fontName="Helvetica", fontSize=8.8,
                               textColor=INK, leading=12.4),
        "small": ParagraphStyle("small", alignment=TA_JUSTIFY, spaceAfter=5,
                                fontName="Helvetica", fontSize=8.8,
                                textColor=INK, leading=12.4),
    }


def make_chrome(L):
    def chrome(canvas, doc):
        canvas.saveState()
        w, h = A4
        # intestazione
        if os.path.exists(LOGO):
            canvas.drawImage(LOGO, MARGIN, h - TOP + 5 * mm, width=13 * mm, height=13 * mm,
                             mask="auto")
        canvas.setFont("Helvetica-Bold", 13)
        canvas.setFillColor(GREEN)
        canvas.drawString(MARGIN + 16 * mm, h - TOP + 12.5 * mm, "GiroMunna")
        canvas.setFont("Helvetica", 7.4)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN + 16 * mm, h - TOP + 8.4 * mm, L["tagline"])
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(1.1)
        canvas.line(MARGIN, h - TOP + 4 * mm, w - MARGIN, h - TOP + 4 * mm)
        # pie' di pagina
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.6)
        canvas.line(MARGIN, BOTTOM - 4 * mm, w - MARGIN, BOTTOM - 4 * mm)
        canvas.setFont("Helvetica", 6.8)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, BOTTOM - 8.5 * mm, L["footer1"])
        canvas.drawString(MARGIN, BOTTOM - 12 * mm, L["footer2"])
        canvas.drawRightString(w - MARGIN, BOTTOM - 12 * mm, L["page"] % doc.page)
        canvas.restoreState()
    return chrome


def build(lang, cliente, out):
    L = IT if lang == "it" else EN
    S = styles()
    w, _ = A4
    usable = w - 2 * MARGIN

    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=TOP, bottomMargin=BOTTOM,
                          title="GiroMunna %s %s" % (L["title"], RIF),
                          author="GiroMunna")
    frame = Frame(MARGIN, BOTTOM, usable, A4[1] - TOP - BOTTOM, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=make_chrome(L))])

    F = []
    F.append(Paragraph(L["title"], S["title"]))
    F.append(Paragraph(L["subtitle"], S["subtitle"]))
    F.append(Paragraph(L["meta"] % cliente, S["meta"]))

    # --- mezzo
    F.append(Paragraph(L["h_mezzo"], S["h2"]))
    F.append(Paragraph(L["mezzo_intro"], S["body"]))
    bullet = Table([[Paragraph(L["mezzo_bullet"], S["cellsm"])]], colWidths=[usable])
    bullet.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    F.append(bullet)
    F.append(Spacer(1, 7))
    F.append(Paragraph(L["mezzo_close"], S["body"]))

    # --- servizio
    F.append(Paragraph(L["h_servizio"], S["h2"]))
    F.append(Paragraph(L["svc_intro"], S["body"]))
    cols = [25 * mm, usable - 25 * mm - 27 * mm, 27 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for date, desc, eng in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % date, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
            Paragraph(eng, S["cellmut"]),
        ])
    t = Table(data, colWidths=cols, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    F.append(t)

    # --- prezzo (intestazione e tabella non si spezzano fra due pagine)
    pcols = [usable - 30 * mm - 20 * mm, 30 * mm, 20 * mm]
    pdata = []
    for label, amount, vat in L["price_rows"]:
        pdata.append([Paragraph(label, S["cellsm"]),
                      Paragraph(amount, S["cellsm"]),
                      Paragraph(vat, S["cellmut"])])
    pdata.append([Paragraph("<b>%s</b>" % L["price_total_label"], S["cellsm"]),
                  Paragraph("<b>%s</b>" % L["price_total"], S["cellsm"]),
                  Paragraph(L["vat_note"], S["cellmut"])])
    pt = Table(pdata, colWidths=pcols)
    pt.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("LINEABOVE", (0, -1), (-1, -1), 0.9, GREEN),
        ("BACKGROUND", (0, -1), (-1, -1), CREAM),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    # la lista va costruita prima: KeepTogether non tiene il riferimento
    # a una lista vuota passata alla costruzione.
    F.append(KeepTogether([
        Paragraph(L["h_prezzo"], S["h2"]),
        pt,
        Paragraph(L["grand"], S["grand"]),
        Paragraph(L["perhead"], S["small"]),
    ]))
    F.append(Spacer(1, 4))
    F.append(Paragraph("<b>%s</b> %s" % (L["h_incluso"], L["incluso"]), S["small"]))
    F.append(Paragraph("<b>%s</b> %s" % (L["h_nonincluso"], L["nonincluso"]), S["small"]))

    # --- pagamento
    F.append(Paragraph(L["h_pagamento"], S["h2"]))
    ydata = [[Paragraph(a, S["cellsm"]), Paragraph("<b>%s</b>" % b, S["cellsm"]),
              Paragraph(c, S["cellmut"])] for a, b, c in L["pay_rows"]]
    yt = Table(ydata, colWidths=pcols)
    yt.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    F.append(yt)
    F.append(Spacer(1, 6))
    F.append(Paragraph(L["bank"], S["small"]))

    # --- note
    F.append(Paragraph(L["h_note"], S["h2"]))
    for n in L["note"]:
        F.append(Paragraph("·  " + n, S["note"]))

    F.append(Spacer(1, 8))
    F.append(Paragraph(L["closing"], S["small"]))

    doc.build(F)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--cliente", "--client", dest="cliente", default="Trevor Bailey")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Sovicille_Antinori_19_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

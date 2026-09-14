#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasporto privato a Capannori e in
Toscana del 20-24 aprile 2027.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_villa_capannori.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_villa_capannori.py --lingua en --cliente "Client Name"
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

RIF = "GM-2027-0420-LP"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasporto privato a Capannori e in Toscana  ·  20-24 aprile 2027",
    meta="Preparato per %s  ·  13 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus per il vostro gruppo di 12-14 persone, con lo stesso conducente di lingua "
        "inglese per tutta la durata del programma."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 12-14 ospiti a bordo restano fino a 14 posti liberi: spazio ampio per persone e bagagli "
        "su cinque giornate di programma. I 7,64 metri del mezzo raggiungono senza difficoltà la villa "
        "e le strade di campagna intorno a Capannori, oltre ai centri storici di Lucca e Firenze, dove "
        "un autobus gran turismo non arriva."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Mar 20 apr",
         "<b>Stazione di Firenze Santa Maria Novella → villa a Capannori.</b> Ritrovo in stazione "
         "all'orario che ci comunicherete, con una sosta al supermercato di 30-45 minuti lungo il "
         "percorso; circa 80 km in tutto, bagagli del gruppo a bordo. "
         "<br/><b>In serata,</b> ritrovo alla villa verso le 19:30 per la cena in un ristorante della "
         "zona, rientro previsto fra le 21:30 e le 22:00, circa 16 km.",
         "orario da confermare + 19:30 – 22:00"),
        ("Mer 21 apr",
         "<b>Villa a Capannori → Firenze,</b> trasferimento del mattino, circa 80 km; il mezzo resta "
         "libero durante la giornata. <b>Nel pomeriggio,</b> ritrovo a Firenze verso le 16:00 e rientro "
         "alla villa, circa 80 km. Nessun servizio serale.",
         "mattina + circa 16:00 – 17:30"),
        ("Gio 22 apr",
         "<b>Villa → cantine delle Colline Lucchesi, pranzo e alcune ore in zona, rientro in villa.</b> "
         "Mezzo e conducente a disposizione dalle 9:00 alle 16:00 circa, 7 ore, circa 60 km; le tappe "
         "esatte le concordiamo con voi, siamo lieti di suggerire un paio di cantine della zona. "
         "<br/><b>In serata,</b> trasferimento a Lucca per cena: ritrovo in villa verso le 19:30, "
         "rientro previsto fra le 23:00 e mezzanotte, circa 16 km.",
         "circa 9:00 – 16:00 + 19:30 – 00:00"),
        ("Ven 23 apr",
         "<b>Trasporti locali a Capannori e dintorni.</b> Il programma dettagliato è ancora da "
         "definire: restiamo a disposizione per gli spostamenti della giornata fino alle 17:00 circa. "
         "Il prezzo indicato è provvisorio, calcolato su una giornata piena a disposizione in zona; "
         "lo confermiamo appena ricevuto l'itinerario.",
         "circa 9:00 – 17:00 (indicativo)"),
        ("Sab 24 apr",
         "<b>Villa a Capannori → Aeroporto di Firenze.</b> Trasferimento con bagagli, circa 80 km.",
         "orario da confermare in base al volo"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Mar 20 apr — stazione di Firenze S.M.N. → villa, cena in serata", "€ 680,00", "+ IVA 10%"),
        ("Mar 20 apr — permesso bus centro storico di Firenze", "€ 415,00", "+ IVA 10%"),
        ("Mer 21 apr — trasferimenti mattina e pomeriggio da/per Firenze", "€ 800,00", "+ IVA 10%"),
        ("Mer 21 apr — permesso bus centro storico di Firenze", "€ 415,00", "+ IVA 10%"),
        ("Gio 22 apr — giornata a disposizione in zona e cena a Lucca", "€ 1.430,00", "+ IVA 10%"),
        ("Gio 22 apr — permesso bus centro storico di Lucca", "€ 180,00", "+ IVA 10%"),
        ("Ven 23 apr — trasporti locali a Capannori e dintorni (da confermare)", "€ 880,00", "+ IVA 10%"),
        ("Sab 24 apr — villa a Capannori → aeroporto di Firenze", "€ 680,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 5.480,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 6.028,00.",
    perhead=(
        "Sono tra circa € 431,00 e € 502,00 a persona, IVA inclusa, secondo il numero definitivo "
        "dei partecipanti (12-14)."
    ),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente di lingua inglese, carburante, pedaggi autostradali, parcheggi, "
        "assicurazione completa, movimentazione bagagli, la sosta al supermercato del 20 aprile, il "
        "permesso comunale per l'ingresso del bus nel centro di Firenze (20 e 21 aprile) e quello per "
        "il centro di Lucca (22 aprile). L'aeroporto di Firenze del 24 aprile è l'unica giornata che "
        "non comporta questo onere; per il 23 aprile lo valutiamo appena il programma è confermato."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Ingressi, degustazioni, pranzi e cene, guide e mance. Attesa oltre gli orari concordati, "
        "€ 50,00 all'ora per mezzo. Soste aggiuntive o modifiche all'itinerario, quotate su richiesta. "
        "Rientro alla villa dopo le 02:00, € 250,00 per mezzo."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 1.808,40", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 4.219,60", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>I permessi bus per Firenze e Lucca.</b> Ogni giornata con un ritrovo, un rilascio o una "
         "sosta nel centro di queste due città richiede un permesso comunale, che non è evitabile "
         "scegliendo un punto diverso: lo abbiamo messo a preventivo per il 20 e il 21 aprile a Firenze "
         "(€ 415 ciascuno) e per il 22 aprile a Lucca (circa € 180). Fa eccezione solo l'aeroporto "
         "del 24 aprile, che non lo richiede. Fateci sapere dove preferite essere lasciati e ripresi in "
         "città, così vi confermiamo i punti esatti."),
        ("<b>Furgoni invece del minibus.</b> Ci avete chiesto anche il confronto con due furgoni da "
         "6-7 posti ciascuno. La nostra flotta di proprietà è il Mercedes-Benz Beluga: con 12-14 "
         "persone restano fino a 14 posti liberi, ampio spazio per i bagagli, e i suoi 7,64 metri "
         "raggiungono comunque strade e piazzali stretti dove un pullman gran turismo non arriva — lo "
         "stesso vantaggio che due furgoni offrirebbero, ma con un solo conducente e un solo mezzo da "
         "coordinare. Non gestiamo direttamente furgoni di quella taglia: se per voi restasse comunque "
         "preferibile viaggiare su due mezzi più piccoli, è un'opzione da valutare a parte con un "
         "fornitore dedicato e ha un costo aggiuntivo che non abbiamo incluso in questo preventivo. "
         "Ditecelo se volete che la approfondiamo."),
        ("<b>Il 23 aprile.</b> Il programma della giornata è ancora da definire, come segnalato nella "
         "vostra richiesta. Il prezzo che trovate qui è provvisorio, calcolato su una giornata piena a "
         "disposizione in zona: appena ci mandate gli orari e le tappe ve lo confermiamo, in aumento o "
         "in diminuzione a seconda dell'impegno effettivo."),
        ("<b>Il rientro tardi del 22 e la partenza del 23.</b> La cena a Lucca del 22 aprile rientra "
         "fra le 23:00 e mezzanotte. Per rispettare i tempi di riposo del conducente vi chiediamo di "
         "non fissare l'inizio dei trasporti del 23 aprile prima delle 10:00 circa."),
        ("<b>Bagagli del 20 e del 24 aprile.</b> Il vano del Beluga è ampio e con il vostro gruppo di "
         "12-14 persone c'è spazio più che sufficiente. Segnalateci comunque in anticipo bagagli fuori "
         "misura, come sacche da golf o attrezzatura sportiva."),
        ("<b>Orari di treno e volo.</b> Ci servono l'orario del treno in arrivo il 20 aprile a Firenze "
         "Santa Maria Novella e il volo in partenza il 24 aprile dall'aeroporto di Firenze, per "
         "confermare gli orari esatti dei due trasferimenti."),
        ("<b>Le cantine del 22 aprile.</b> Siamo lieti di suggerire un paio di cantine delle Colline "
         "Lucchesi, a pochi minuti dalla villa; fateci sapere se preferite indicarcele voi o affidarvi "
         "a un nostro consiglio."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei partecipanti (tra 12 e 14), "
         "l'indirizzo esatto della villa a Capannori e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero per il 20-24 aprile 2027. "
         "La cancellazione è gratuita oltre 60 giorni prima del primo servizio; da 60 a 30 giorni si "
         "trattiene l'acconto; da 30 a 10 giorni il 50%; negli ultimi 10 giorni il 100%. Mancando più "
         "di sette mesi al primo servizio, siamo naturalmente disponibili a riconfermare il preventivo "
         "più vicino alla data. Preventivo valido fino al 13 ottobre 2026."),
    ],
    closing=("Restiamo a disposizione per qualsiasi chiarimento e in attesa di un vostro riscontro.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Private transport in Capannori and Tuscany  ·  20-24 April 2027",
    meta="Prepared for %s  ·  13 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "One minibus for your group of 12-14, with the same English-speaking driver throughout the "
        "programme."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 12-14 guests on board up to 14 seats stay free — plenty of room for people and luggage "
        "over five days of programme. At 7.64 m the minibus reaches the villa and the country lanes "
        "around Capannori without difficulty, as well as the historic centres of Lucca and Florence, "
        "which a full-size coach cannot manage."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Tue 20 Apr",
         "<b>Florence Santa Maria Novella station → villa in Capannori.</b> Meeting point at the "
         "station at the time you confirm, with a 30-45 minute supermarket stop along the way; about "
         "80 km in all, with the group's luggage on board. "
         "<br/><b>In the evening,</b> pickup at the villa around 19:30 for dinner at a local "
         "restaurant, return expected between 21:30 and 22:00, about 16 km.",
         "time to be confirmed + 19:30 – 22:00"),
        ("Wed 21 Apr",
         "<b>Villa in Capannori → Florence,</b> morning transfer, about 80 km; the vehicle is free "
         "during the day. <b>In the afternoon,</b> pickup in Florence around 16:00 and return to the "
         "villa, about 80 km. No evening service.",
         "morning + approx. 16:00 – 17:30"),
        ("Thu 22 Apr",
         "<b>Villa → wineries in the Colline Lucchesi, lunch and a few hours in the area, return to "
         "the villa.</b> Vehicle and driver at your disposal from 9:00 to about 16:00, 7 hours, about "
         "60 km; we will agree the exact stops with you, and are glad to suggest a couple of local "
         "wineries. <br/><b>In the evening,</b> transfer to Lucca for dinner: pickup at the villa "
         "around 19:30, return expected between 23:00 and midnight, about 16 km.",
         "approx. 9:00 – 16:00 + 19:30 – 00:00"),
        ("Fri 23 Apr",
         "<b>Local transport around Capannori and nearby areas.</b> The detailed schedule is still "
         "being finalised: we stay at your disposal for the day's movements until about 17:00. The "
         "price shown is provisional, based on a full day at disposal locally; we will confirm it once "
         "we receive the itinerary.",
         "approx. 9:00 – 17:00 (indicative)"),
        ("Sat 24 Apr",
         "<b>Villa in Capannori → Florence Airport.</b> Transfer with luggage, about 80 km.",
         "time to be confirmed against the flight"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Tue 20 Apr — Florence S.M.N. station → villa, dinner in the evening", "€ 680.00", "+ VAT 10%"),
        ("Tue 20 Apr — Florence historic-centre bus permit", "€ 415.00", "+ VAT 10%"),
        ("Wed 21 Apr — morning and afternoon transfers to/from Florence", "€ 800.00", "+ VAT 10%"),
        ("Wed 21 Apr — Florence historic-centre bus permit", "€ 415.00", "+ VAT 10%"),
        ("Thu 22 Apr — full day at disposal locally and dinner in Lucca", "€ 1,430.00", "+ VAT 10%"),
        ("Thu 22 Apr — Lucca historic-centre bus permit", "€ 180.00", "+ VAT 10%"),
        ("Fri 23 Apr — local transport around Capannori (to be confirmed)", "€ 880.00", "+ VAT 10%"),
        ("Sat 24 Apr — villa in Capannori → Florence Airport", "€ 680.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 5,480.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 6,028.00.",
    perhead=(
        "That is between about € 431.00 and € 502.00 per person, VAT included, depending on the final "
        "number of participants (12-14)."
    ),
    h_incluso="Included.",
    incluso=(
        "English-speaking driver and vehicle, fuel, motorway tolls, parking, full insurance, luggage "
        "handling, the supermarket stop on 20 April, the municipal permit for the bus to enter central "
        "Florence (20 and 21 April) and the one for central Lucca (22 April). Florence Airport on 24 "
        "April is the only day that does not carry this charge; for 23 April we will confirm once the "
        "programme is set."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Entrance fees, tastings, lunches and dinners, guides and gratuities. Waiting beyond the agreed "
        "times, € 50.00 per hour per vehicle. Additional stops or changes to the itinerary, quoted on "
        "request. Return to the villa after 02:00, € 250.00 per vehicle."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 1,808.40", "VAT included"),
        ("Balance, within 5 days of the service", "€ 4,219.60", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The Florence and Lucca bus permits.</b> Every day with a pickup, drop-off or stop in the "
         "centre of these two cities requires a municipal permit, which cannot be avoided by choosing a "
         "different meeting point: we have included it for 20 and 21 April in Florence (€ 415 "
         "each) and for 22 April in Lucca (about € 180). The only exception is the airport on 24 April, "
         "which does not require it. Let us know where in each city you would like to be dropped off "
         "and picked up, and we will confirm the exact spots."),
        ("<b>Vans instead of the minibus.</b> You also asked us to quote two vans of 6-7 passengers "
         "each for comparison. Our own fleet is the Mercedes-Benz Beluga: with 12-14 people on board up "
         "to 14 seats stay free, there is ample room for luggage, and its 7.64 m still reaches narrow "
         "roads and courtyards a full-size coach cannot manage — the same advantage two vans would "
         "offer, but with a single driver and a single vehicle to coordinate. We do not operate vans of "
         "that size ourselves: if you would still rather travel on two smaller vehicles, that is an "
         "option to look into separately with a dedicated supplier, at an additional cost we have not "
         "included in this quotation. Let us know if you would like us to look into it."),
        ("<b>23 April.</b> The day's programme is still being defined, as noted in your request. The "
         "price shown here is provisional, based on a full day at disposal locally: as soon as you send "
         "us the times and stops we will confirm it, up or down depending on the actual commitment."),
        ("<b>The late return on the 22nd and the start on the 23rd.</b> Dinner in Lucca on 22 April "
         "returns between 23:00 and midnight. To respect the driver's rest periods, we ask that "
         "transport on 23 April not start before about 10:00."),
        ("<b>Luggage on 20 and 24 April.</b> The Beluga's hold is large, and with your group of 12-14 "
         "there is more than enough room. Please still let us know in advance about oversized items, "
         "such as golf bags or sports equipment."),
        ("<b>Train and flight times.</b> We need the arrival time of the train on 20 April at Florence "
         "Santa Maria Novella and the departure time of the flight on 24 April from Florence Airport, "
         "to confirm the exact schedule of both transfers."),
        ("<b>The wineries on 22 April.</b> We are glad to suggest a couple of wineries in the Colline "
         "Lucchesi, a few minutes from the villa; let us know if you would rather name them yourselves "
         "or rely on our recommendation."),
        ("<b>To confirm we need</b> the final number of participants (between 12 and 14), the exact "
         "address of the villa in Capannori, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free for 20-24 April 2027. "
         "Cancellation is free of charge more than 60 days before the first service; from 60 to 30 days "
         "the deposit is retained; from 30 to 10 days, 50%; in the last 10 days, 100%. With more than "
         "seven months to the first service, we are of course happy to reconfirm the quotation closer "
         "to the date. Quotation valid until 13 October 2026."),
    ],
    closing=("We remain at your disposal for any clarification and look forward to hearing from you.<br/><br/>"
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
    cols = [20 * mm, usable - 20 * mm - 30 * mm, 30 * mm]
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Lisa Parks")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Villa_Capannori_20-24_aprile_2027_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

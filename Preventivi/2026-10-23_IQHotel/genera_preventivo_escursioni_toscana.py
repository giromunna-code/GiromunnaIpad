#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per due escursioni in minibus con conducente da Firenze
(iQ Hotel), 23 e 24 ottobre 2026: Pisa e Lucca; Siena, San Gimignano e una cantina del Chianti.

Solo il minibus: la cantina la scelgono e la prenotano le clienti, GiroMunna consiglia.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_escursioni_toscana.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_escursioni_toscana.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1023-IQ"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Due escursioni da Firenze: Pisa e Lucca, Siena, San Gimignano e il Chianti  ·  23 e 24 ottobre 2026",
    meta="Preparato per %s  ·  15 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus riservato al vostro gruppo, con il conducente, per due giornate intere: vi prende "
        "all'iQ Hotel la mattina, vi accompagna di città in città e vi riporta in hotel la sera, senza "
        "altri passeggeri e senza orari da rincorrere."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 25 posti passeggeri più accompagnatore e autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "In dieci su 25 posti viaggiate larghe, con spazio per borse, acquisti e le bottiglie che vorrete "
        "portare a casa dalla cantina. E con meno di 8 metri di lunghezza il Beluga arriva fino ai "
        "parcheggi più vicini ai centri storici e sulle strade bianche delle cantine, dove un autobus "
        "gran turismo non passa."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Programma", "Orario"],
    svc=[
        ("Ven 23 ott",
         "<b>Firenze → Pisa → Lucca → Firenze.</b> Partenza dall'iQ Hotel, Pisa e Piazza dei Miracoli "
         "in mattinata, Lucca per il pranzo e il pomeriggio, rientro in hotel. Circa 190 km, 9 ore.",
         "8:30 – 17:30"),
        ("Sab 24 ott",
         "<b>Firenze → Siena → San Gimignano → cantina nel Chianti → Firenze.</b> Siena in mattinata e "
         "per il pranzo, San Gimignano nel primo pomeriggio, visita e degustazione in cantina, rientro "
         "in hotel. Circa 180 km, 10 ore.",
         "8:30 – 18:30"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Venerdì 23 ottobre, Firenze – Pisa – Lucca – Firenze, 9 ore", "€ 1.150,00", "+ IVA 10%"),
        ("Sabato 24 ottobre, Firenze – Siena – San Gimignano – Chianti – Firenze, 10 ore",
         "€ 1.250,00", "+ IVA 10%"),
        ("Permessi di accesso dei bus turistici: check point di Firenze per due giornate, Pisa, Lucca, "
         "Siena e San Gimignano", "€ 1.320,00", "+ IVA 10%"),
        ("Pranzo del conducente, 23 e 24 ottobre", "a carico vostro", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 3.720,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 4.092,00.",
    perhead=("Su 10 persone sono circa € 409,00 a testa per le due giornate, IVA inclusa. Il prezzo è per "
             "il mezzo, non per persona: non cambia se siete qualcuna in meno."),
    h_incluso="Incluso.",
    incluso=(
        "Minibus con conducente per le due giornate, carburante, pedaggi autostradali, parcheggi, "
        "check point di Firenze e permessi di accesso dei bus turistici a Pisa, Lucca, Siena e San "
        "Gimignano, assicurazione completa."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Pranzo del conducente nelle due giornate, a carico vostro. Pasti del gruppo, ingressi a "
        "monumenti e musei, guide turistiche, visita e degustazione in cantina. Attesa oltre gli orari concordati, "
        "€ 50,00 all'ora. Soste o modifiche di percorso non previste, quotate su richiesta."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 1.227,60", "IVA inclusa"),
        ("Saldo entro il 22 ottobre 2026", "€ 2.864,40", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Disponibilità.</b> Il minibus è libero per entrambe le date, venerdì 23 e sabato 24 "
         "ottobre. Mancano pochi giorni: per tenervelo bloccato ci serve la conferma entro il 17 "
         "ottobre 2026, data di validità del preventivo."),
        ("<b>Firenze e il check point.</b> L'iQ Hotel si trova nell'area della città in cui un bus "
         "turistico può entrare solo pagando il check point comunale, € 421,00 al giorno. È già "
         "compreso nel prezzo, come i permessi di Pisa, Lucca, Siena e San Gimignano: non avrete altri "
         "costi da pagare per strada."),
        ("<b>Venerdì, Pisa e Lucca.</b> A Pisa il minibus vi lascia al parcheggio dei bus di via "
         "Pietrasantina, a cinque minuti a piedi dalla Torre. Verso le 12:30 si riparte per Lucca, "
         "dove vi lasciamo vicino alle mura: il pranzo e il pomeriggio sono vostri, e alle 16:30 si "
         "rientra a Firenze. Se volete salire sulla Torre di Pisa, i biglietti vanno prenotati in "
         "anticipo e con un orario preciso: ditecelo e organizziamo la mattina intorno a quello."),
        ("<b>Sabato, Siena, San Gimignano e la cantina.</b> Arrivo a Siena verso le 9:45: la mattina e "
         "il pranzo in città. Verso le 13:00 si parte per San Gimignano, dove si sta fino alle 15:30 "
         "circa. La cantina è l'ultima tappa, dalle 16:15 alle 17:45 circa, sulla strada del ritorno: "
         "dopo la degustazione nessuna di voi deve guidare e in mezz'ora siete in hotel. A Siena e a "
         "San Gimignano i bus si fermano fuori dalle mura: dal parcheggio al centro sono una decina di "
         "minuti a piedi, in salita. Conviene avere scarpe comode."),
        ("<b>Le cantine che vi consigliamo.</b> La scelta e la prenotazione sono vostre; qui qualche "
         "indirizzo sulla strada fra San Gimignano e Firenze, tutte con visita guidata, degustazione e "
         "vista sui vigneti. <b>Antinori nel Chianti Classico</b>, a Bargino: cantina moderna scavata "
         "nella collina, con il tetto coperto di vigne, a mezz'ora da Firenze. <b>Badia a Passignano</b>, "
         "vicino a Tavarnelle: un'abbazia dell'XI secolo in mezzo ai filari, con le cantine storiche dei "
         "monaci. <b>Castello di Verrazzano</b>, sopra Greve in Chianti: castello e giardini con la "
         "vista sulla valle, degustazioni accompagnate da prodotti tipici. Prenotate per sabato 24 "
         "verso le 16:15 e diteci il nome della cantina e l'orario: il resto della giornata lo "
         "organizziamo noi intorno a quello. Il Beluga arriva senza problemi a tutte e tre."),
        ("<b>Il pranzo del conducente.</b> Nelle due giornate il conducente rientra in sede la sera, "
         "quindi non servono pernottamenti. Il suo pranzo è a carico vostro: potete invitarlo al "
         "vostro tavolo oppure lasciargli la cifra di un pasto, come preferite."),
        ("<b>Orari flessibili.</b> Gli orari indicati sono una proposta: dentro le 9 e le 10 ore della "
         "giornata potete spostare le soste come volete. Oltre l'orario concordato l'attesa si "
         "conteggia a € 50,00 all'ora."),
        ("<b>Per confermare ci servono</b> il nome e il cellulare di una referente, il numero esatto di "
         "partecipanti e i dati per la fattura."),
        ("<b>Cancellazione.</b> La prenotazione diventa definitiva alla ricezione dell'acconto. Mancando "
         "meno di 10 giorni al servizio, dopo la conferma la cancellazione comporta l'addebito "
         "dell'intero importo."),
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
    subtitle="Two day trips from Florence: Pisa and Lucca, Siena, San Gimignano and Chianti  ·  23 and 24 October 2026",
    meta="Prepared for %s  ·  15 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "A minibus reserved for your group, with its driver, for two full days: it picks you up at the "
        "iQ Hotel in the morning, takes you from town to town and brings you back to the hotel in the "
        "evening, with no other passengers and no timetables to chase."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 25 passenger seats plus guide seat and driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "Ten of you on 25 seats travel in comfort, with room for bags, shopping and the bottles you will "
        "want to take home from the winery. And at under 8 metres long the Beluga reaches the car parks "
        "closest to the historic centres and the gravel roads to the wineries, where a full-size coach "
        "cannot go."
    ),
    h_servizio="The service",
    svc_head=["Date", "Programme", "Time"],
    svc=[
        ("Fri 23 Oct",
         "<b>Florence → Pisa → Lucca → Florence.</b> Departure from the iQ Hotel, Pisa and the Piazza dei "
         "Miracoli in the morning, Lucca for lunch and the afternoon, return to the hotel. About 190 km, 9 hours.",
         "8:30 – 17:30"),
        ("Sat 24 Oct",
         "<b>Florence → Siena → San Gimignano → Chianti winery → Florence.</b> Siena in the morning and for "
         "lunch, San Gimignano in the early afternoon, winery tour and tasting, return to the hotel. "
         "About 180 km, 10 hours.",
         "8:30 – 18:30"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Friday 23 October, Florence – Pisa – Lucca – Florence, 9 hours", "€ 1,150.00", "+ VAT 10%"),
        ("Saturday 24 October, Florence – Siena – San Gimignano – Chianti – Florence, 10 hours",
         "€ 1,250.00", "+ VAT 10%"),
        ("Tourist coach access permits: Florence check point for two days, Pisa, Lucca, Siena and "
         "San Gimignano", "€ 1,320.00", "+ VAT 10%"),
        ("Driver's lunch, 23 and 24 October", "at your charge", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 3,720.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 4,092.00.",
    perhead=("Across 10 people that is about € 409.00 each for the two days, VAT included. The price is "
             "for the vehicle, not per person: it does not change if one or two of you are missing."),
    h_incluso="Included.",
    incluso=(
        "Minibus with driver for both days, fuel, motorway tolls, parking, the Florence check point and "
        "the tourist coach access permits for Pisa, Lucca, Siena and San Gimignano, full insurance."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's lunch on both days, at your charge. Group meals, entrance fees to monuments and "
        "museums, tour guides, the winery tour and tasting. Waiting beyond the agreed times, € 50.00 per "
        "hour. Unplanned stops or route changes, quoted on request."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 1,227.60", "VAT included"),
        ("Balance by 22 October 2026", "€ 2,864.40", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Availability.</b> The minibus is free on both dates, Friday 23 and Saturday 24 October. "
         "Time is short: to hold it for you we need your confirmation by 17 October 2026, the validity "
         "date of this quotation."),
        ("<b>Florence and the check point.</b> The iQ Hotel lies within the part of the city that a tourist "
         "coach may enter only by paying the municipal check point, € 421.00 per day. It is already "
         "included in the price, as are the permits for Pisa, Lucca, Siena and San Gimignano: there is "
         "nothing else to pay along the way."),
        ("<b>Friday, Pisa and Lucca.</b> In Pisa the minibus drops you at the coach park in Via "
         "Pietrasantina, a five-minute walk from the Tower. Around 12:30 we leave for Lucca, where we drop "
         "you near the city walls: lunch and the afternoon are yours, and at 16:30 we head back to Florence. "
         "If you wish to climb the Leaning Tower, tickets must be booked in advance for a set time: let us "
         "know and we will plan the morning around it."),
        ("<b>Saturday, Siena, San Gimignano and the winery.</b> Arrival in Siena around 9:45: the morning "
         "and lunch in town. Around 13:00 we leave for San Gimignano, where you stay until about 15:30. The "
         "winery is the last stop, from about 16:15 to 17:45, on the way back: after the tasting none of "
         "you has to drive, and half an hour later you are at your hotel. In Siena and San Gimignano coaches "
         "stop outside the walls: from the car park to the centre is about ten minutes on foot, uphill. "
         "Comfortable shoes are a good idea."),
        ("<b>The wineries we recommend.</b> The choice and the booking are yours; here are a few "
         "addresses on the way between San Gimignano and Florence, all with guided tours, tastings and "
         "vineyard views. <b>Antinori nel Chianti Classico</b>, in Bargino: a modern winery carved into the "
         "hillside, its roof covered in vines, half an hour from Florence. <b>Badia a Passignano</b>, near "
         "Tavarnelle: an 11th-century abbey surrounded by vineyards, with the monks' historic cellars. "
         "<b>Castello di Verrazzano</b>, above Greve in Chianti: a castle and gardens overlooking the "
         "valley, with tastings accompanied by local products. Book for Saturday 24 at around 16:15 "
         "and tell us the winery and the time: we will plan the rest of the day around it. The Beluga "
         "reaches all three without any problem."),
        ("<b>The driver's lunch.</b> On both days the driver returns to base in the evening, so no overnight "
         "stay is needed. His lunch is at your charge: you can invite him to your table or give him the "
         "cost of a meal, whichever you prefer."),
        ("<b>Flexible times.</b> The times shown are a suggestion: within the 9 and 10 hours of each day you "
         "can move the stops as you like. Beyond the agreed time, waiting is charged at € 50.00 per hour."),
        ("<b>To confirm we need</b> the name and mobile number of a contact person, the exact number of "
         "participants and your invoicing details."),
        ("<b>Cancellation.</b> The booking becomes firm on receipt of the deposit. With less than 10 days to "
         "the service, once confirmed a cancellation is charged at the full amount."),
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
                             textColor=GREEN, leading=15, spaceBefore=13, spaceAfter=6,
                             keepWithNext=1),
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=9.6,
                             textColor=GREEN, leading=13, spaceBefore=4, spaceAfter=4,
                             keepWithNext=1),
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


def price_table(rows, total_label, total, total_note, S, cols):
    data = []
    for label, amount, vat in rows:
        data.append([Paragraph(label, S["cellsm"]),
                     Paragraph(amount, S["cellsm"]),
                     Paragraph(vat, S["cellmut"])])
    data.append([Paragraph("<b>%s</b>" % total_label, S["cellsm"]),
                 Paragraph("<b>%s</b>" % total, S["cellsm"]),
                 Paragraph(total_note, S["cellmut"])])
    t = Table(data, colWidths=cols)
    t.setStyle(TableStyle([
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
    return t


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
    cols = [23 * mm, usable - 23 * mm - 27 * mm, 27 * mm]
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
    pcols = [usable - 42 * mm - 20 * mm, 42 * mm, 20 * mm]
    F.append(KeepTogether([
        Paragraph(L["h_prezzo"], S["h2"]),
        price_table(L["price_rows"], L["price_total_label"], L["price_total"], L["vat_note"],
                    S, pcols),
        Paragraph(L["grand"], S["grand"]),
        Paragraph(L["perhead"], S["small"]),
    ]))
    F.append(Spacer(1, 4))
    F.append(Paragraph("<b>%s</b> %s" % (L["h_incluso"], L["incluso"]), S["small"]))
    F.append(Paragraph("<b>%s</b> %s" % (L["h_nonincluso"], L["nonincluso"]), S["small"]))

    # --- pagamento
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
    F.append(KeepTogether([Paragraph(L["h_pagamento"], S["h2"]), yt]))
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="gruppo ospite dell'iQ Hotel Firenze")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Escursioni_Toscana_23-24_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

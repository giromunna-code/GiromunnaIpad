#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per l'escursione culturale del 26 settembre 2026
(Firenze - Siena - San Gimignano - Pisa - Firenze).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_escursione.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_escursione.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0926-MJV"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Escursione culturale in Toscana: Siena, San Gimignano e Pisa  ·  26 settembre 2026",
    meta="Preparato per %s  ·  14 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo, fino a 26 persone, con lo stesso conducente per tutta la giornata.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con il gruppo al completo il Beluga è alla sua capienza massima, senza posti liberi di margine: "
        "vi chiediamo per questo il numero definitivo dei partecipanti appena possibile. "
        "I suoi 7,64 metri restano comunque un vantaggio concreto per la giornata: il mezzo raggiunge i "
        "parcheggi bus vicino alle mura di Siena e San Gimignano, dove un autobus gran turismo fatica a "
        "manovrare o non arriva affatto."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Sab 26 set",
         "<b>Firenze → Siena → San Gimignano → Pisa → Firenze.</b> "
         "Ritrovo alle 07:30 nel punto che ci indicherete a Firenze. Partenza per Siena, circa 70 km, arrivo "
         "alle 08:45: mezzo e conducente restano a disposizione per la visita del centro storico e di Piazza "
         "del Campo fino alle 11:00. Si prosegue poi per San Gimignano, circa 42 km, arrivo alle 11:50, con "
         "tempo libero per il pranzo e la visita delle Torri fino alle 14:30. Il pomeriggio si passa a Pisa, "
         "circa 62 km, arrivo alle 15:35, per la visita di Piazza dei Miracoli e della Torre pendente fino alle "
         "17:45. Rientro a Firenze alle 18:55, circa 80 km.",
         "circa 07:30 – 18:55"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 26 set — Firenze → Siena → San Gimignano → Pisa → Firenze, giornata intera a disposizione (circa 254 km)",
         "€ 2.450,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.450,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.695,00.",
    perhead="Sono circa € 103,65 a persona, per il gruppo al completo di 26 partecipanti.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi autostradali, parcheggi bus a Siena, "
        "San Gimignano e Pisa, il permesso comunale per l'accesso dei bus turistici a Siena (circa € 160), "
        "assicurazione completa."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Pranzo e ingressi ai monumenti (Duomo di Siena, Torri di San Gimignano, Torre di Pisa), guide "
        "turistiche e mance. L'eventuale permesso per l'accesso di un bus turistico nel centro storico di "
        "Firenze (circa € 423,50), dovuto solo se il ritrovo o il rientro cadono dentro la ZTL: lo confermiamo "
        "appena sappiamo l'indirizzo esatto. Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. "
        "Soste aggiuntive o modifiche all'itinerario, quotate su richiesta. Rientro dopo le 02:00, € 250,00."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 808,50", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.886,50", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Punto di ritiro a Firenze.</b> Ci serve l'indirizzo esatto di partenza, hotel o punto di incontro: "
         "se si trova all'interno della ZTL del centro storico, l'ingresso di un bus turistico richiede un "
         "permesso a parte, circa € 423,50, non compreso nel prezzo. Fuori dalla ZTL non ci sono oneri "
         "aggiuntivi. Confermateci l'indirizzo e vi diciamo subito se il permesso serve."),
        ("<b>Numero di passeggeri.</b> Il preventivo è calcolato sul gruppo al completo, 26 persone: è la "
         "capienza massima del Beluga, senza posti liberi di margine. Se il numero definitivo fosse inferiore, "
         "il prezzo del mezzo resta invariato — è un costo a giornata, non a persona — ma vi chiediamo comunque "
         "di confermarci il numero esatto prima della partenza."),
        ("<b>Accessibilità di Siena e San Gimignano.</b> Il Beluga misura 7,64 m, sotto la soglia degli 8 "
         "metri: raggiunge i parcheggi bus dedicati vicino alle mura di entrambe le città, dove un autobus "
         "gran turismo fatica a manovrare o non arriva affatto. Da lì il centro storico si raggiunge a piedi "
         "in pochi minuti."),
        ("<b>Pranzo e ingressi.</b> Il tempo libero a San Gimignano, dalle 11:50 alle 14:30, è pensato anche "
         "per il pranzo, che organizzate voi liberamente. Ingressi ai monumenti, degustazioni e guide "
         "turistiche non sono compresi nel prezzo del trasporto."),
        ("<b>Una giornata lunga.</b> Dal ritrovo delle 07:30 al rientro delle 18:55 passano circa 11 ore e "
         "mezza, ma restando entro i limiti di guida di un solo conducente: non serve alcun cambio né alcun "
         "pernottamento fuori sede."),
        ("<b>Orari indicativi.</b> Gli orari di questo programma sono una base di lavoro: li confermiamo con "
         "voi in base agli orari di apertura dei monumenti e al traffico previsto per il 26 settembre, senza "
         "costi aggiuntivi per piccoli aggiustamenti."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, l'indirizzo esatto di ritrovo "
         "e di rientro a Firenze, un recapito telefonico o WhatsApp della persona che viaggia con il gruppo e "
         "i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla ricezione "
         "dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene "
         "trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il "
         "100%. Mancando oggi 43 giorni al servizio, questa prenotazione ricade nella fascia da 60 a 30 giorni, "
         "e dal 27 agosto passerà in quella da 30 a 10. Preventivo valido fino al 28 agosto 2026."),
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
    subtitle="Cultural excursion in Tuscany: Siena, San Gimignano and Pisa  ·  26 September 2026",
    meta="Prepared for %s  ·  14 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group, up to 26 people, with the same driver for the whole day.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With the group at full strength the Beluga is at its maximum capacity, with no spare seats: we ask "
        "you for this reason to confirm the final headcount as soon as you can. Its 7.64 metres remain a real "
        "advantage for the day all the same: the vehicle reaches the coach parks near the walls of both Siena "
        "and San Gimignano, where a full-size coach struggles to manoeuvre or cannot get in at all."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sat 26 Sep",
         "<b>Florence → Siena → San Gimignano → Pisa → Florence.</b> "
         "Meeting point 07:30 at the address you provide us in Florence. Departure for Siena, about 70 km, "
         "arriving 08:45: vehicle and driver stay at your disposal for the visit of the historic centre and "
         "Piazza del Campo until 11:00. On to San Gimignano, about 42 km, arriving 11:50, with free time for "
         "lunch and the visit of the towers until 14:30. The afternoon is spent in Pisa, about 62 km, arriving "
         "15:35, for the visit of Piazza dei Miracoli and the Leaning Tower until 17:45. Return to Florence at "
         "18:55, about 80 km.",
         "approx. 07:30 – 18:55"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sat 26 Sep — Florence → Siena → San Gimignano → Pisa → Florence, full day at disposal (about 254 km)",
         "€ 2,450.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,450.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,695.00.",
    perhead="That is about € 103.65 per person, for the full group of 26 participants.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, fuel, motorway tolls, coach parking in Siena, San Gimignano and "
        "Pisa, the municipal permit for tourist coach access to Siena (about € 160), full insurance."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Lunch and entrance fees (Siena Cathedral, the Towers of San Gimignano, the Leaning Tower of Pisa), "
        "guides and gratuities. Any permit required for a tourist coach to enter the historic centre of "
        "Florence (about € 423.50), due only if the meeting or drop-off point falls inside the restricted traffic "
        "zone: we confirm this as soon as we know the exact address. Waiting beyond the times set out here, "
        "€ 50.00 per hour per vehicle. Additional stops or changes to the itinerary, quoted on request. Return "
        "after 02:00, € 250.00."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 808.50", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,886.50", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Pick-up point in Florence.</b> We need the exact departure address, hotel or meeting point: if it "
         "sits inside the historic centre's restricted traffic zone, a tourist coach entering it needs a "
         "separate permit, about € 423.50, not included in the price. Outside that zone there are no extra "
         "charges. Confirm the address and we will tell you right away whether the permit is needed."),
        ("<b>Passenger count.</b> This quotation is calculated on the full group, 26 people: that is the "
         "Beluga's maximum capacity, with no spare seats. If the final number were lower, the vehicle price "
         "stays the same — it is a per-day cost, not a per-person one — but we still ask you to confirm the "
         "exact number before departure."),
        ("<b>Access at Siena and San Gimignano.</b> The Beluga measures 7.64 m, under the 8-metre threshold: "
         "it reaches the dedicated coach parks near the walls of both towns, where a full-size coach struggles "
         "to manoeuvre or cannot get in at all. From there the historic centre is a few minutes' walk."),
        ("<b>Lunch and entrance fees.</b> The free time in San Gimignano, from 11:50 to 14:30, is also meant "
         "for lunch, which you arrange freely. Entrance fees, tastings and guides are not included in the "
         "transport price."),
        ("<b>A long day.</b> From the 07:30 meeting point to the 18:55 return, about eleven and a half hours "
         "go by, but it stays within a single driver's permitted hours: no change of driver and no overnight "
         "stay away from base are needed."),
        ("<b>Indicative timings.</b> The times in this programme are a working basis: we confirm them with you "
         "based on the opening hours of the sights and the traffic expected on 26 September, at no extra cost "
         "for small adjustments."),
        ("<b>To confirm we need</b> the final passenger count, the exact meeting and drop-off address in "
         "Florence, a mobile or WhatsApp contact for the person travelling with the group, and your invoicing "
         "details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you for the "
         "whole validity of this quotation; the booking becomes firm on receipt of the deposit. Cancellation "
         "is free of charge more than 60 days before the service; from 60 to 30 days the deposit is retained; "
         "from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. With 43 days to the "
         "service today, this booking falls in the 60-to-30-day band, and from 27 August it moves into the "
         "30-to-10 band. Quotation valid until 28 August 2026."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Maria Juliana Veron")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Escursione_Siena_San_Gimignano_Pisa_26_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per l'uscita didattica delle Scuole Pie Fiorentine:
piazza Savonarola (Firenze) - Osservatorio astronomico di Impruneta, andata e ritorno,
6 novembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_osservatorio_impruneta.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_osservatorio_impruneta.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1106-SP"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Uscita didattica Firenze – Osservatorio astronomico di Impruneta, andata e ritorno  ·  6 novembre 2026",
    meta="Preparato per %s  ·  16 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus riservato alla classe, con il conducente: da piazza Savonarola all'osservatorio, "
        "attesa durante la visita e ritorno al punto di partenza, senza fermate intermedie e senza "
        "altri passeggeri."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 25 posti passeggeri più accompagnatore e autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili con cinture di sicurezza, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Per 13 ragazzi e i loro accompagnatori i posti sono più che sufficienti: ognuno siede comodo e "
        "zaini e giacche trovano posto senza ingombrare il corridoio. Con meno di 8 metri di lunghezza "
        "il minibus percorre senza problemi le strade collinari di Impruneta fino all'osservatorio, "
        "dove un autobus gran turismo faticherebbe a salire."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Orario"],
    svc=[
        ("Ven 6 nov",
         "<b>Piazza Savonarola (Firenze) → Osservatorio astronomico «Ermanno lo Storpio», via della "
         "Sodera 2, Impruneta.</b> Circa 17 km, arrivo verso le 10:50, in tempo per la visita delle 11:00.",
         "partenza 10:15"),
        ("Ven 6 nov",
         "<b>Osservatorio → piazza Savonarola.</b> Il minibus attende il gruppo durante la visita. "
         "Arrivo verso le 13:30.",
         "partenza 13:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Minibus con conducente, piazza Savonarola – Osservatorio di Impruneta e ritorno, con attesa "
         "durante la visita", "€ 550,00", "+ IVA 10%"),
        ("Check point del Comune di Firenze per l'ingresso del minibus in piazza Savonarola",
         "€ 421,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 971,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.068,10.",
    perhead=("Il prezzo è per il mezzo, non per persona: non cambia se il giorno dell'uscita qualche "
             "ragazzo è assente. Con un ritrovo fuori dall'area del check point il totale scende a "
             "€ 605,00 IVA inclusa: lo spieghiamo nelle note."),
    h_incluso="Incluso.",
    incluso=(
        "Minibus con conducente, carburante, pedaggi, parcheggi, check point di Firenze, attesa durante "
        "la visita e assicurazione completa. Il servizio finisce prima di pranzo: non ci sono pasti del "
        "conducente a vostro carico."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Ingresso e visita all'osservatorio. Attesa oltre la partenza delle 13:00, € 50,00 all'ora. "
        "Fermate aggiuntive, quotate su richiesta."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 320,43", "IVA inclusa"),
        ("Saldo, entro il 6 novembre 2026, giorno del servizio", "€ 747,67", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05. "
          "Emettiamo fattura elettronica intestata alla scuola."),
    h_note="Note",
    note=[
        ("<b>Il check point di Firenze.</b> Piazza Savonarola si trova nell'area della città in cui un "
         "bus turistico può entrare solo pagando il check point comunale, € 421,00 per la giornata. È "
         "la voce che pesa di più su un'uscita di mezza giornata. Se per la classe è comodo ritrovarsi "
         "in un punto appena fuori da quell'area, ve lo indichiamo noi: il check point non si paga e il "
         "totale scende a € 605,00 IVA inclusa. Se invece preferite restare in piazza Savonarola, il "
         "prezzo è quello indicato sopra e non avrete altri costi."),
        ("<b>Gli orari.</b> Partendo alle 10:15 il gruppo arriva all'osservatorio verso le 10:50: il "
         "venerdì mattina il traffico in uscita da Firenze verso Galluzzo e Tavarnuzze può rallentare, "
         "e con questo margine siete in tempo per la visita delle 11:00. Si riparte alle 13:00 e si è in "
         "piazza Savonarola verso le 13:30. Se la visita finisce prima, basta dirlo al conducente."),
        ("<b>All'osservatorio.</b> Via della Sodera è una strada collinare stretta: il minibus vi lascia "
         "all'ingresso e resta in attesa nelle vicinanze per tutta la visita, pronto per il ritorno. Vi "
         "chiediamo un recapito dell'osservatorio per l'arrivo."),
        ("<b>Il numero delle persone.</b> 13 ragazzi e 1 o 2 accompagnatori sono 14–15 persone su 25 "
         "posti: c'è spazio anche se si aggiunge qualcuno."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei partecipanti, il nome e il cellulare "
         "dell'insegnante referente per il giorno dell'uscita e i dati della scuola per la fattura "
         "elettronica (codice destinatario o PEC)."),
        ("<b>Validità, disponibilità e cancellazione.</b> Il preventivo è valido fino al 26 ottobre "
         "2026, per lasciare alla dirigenza il tempo di decidere; fino ad allora il mezzo resta a "
         "vostra disposizione. La prenotazione diventa definitiva alla ricezione dell'acconto. Dopo la "
         "conferma, la cancellazione comporta l'addebito del 50% dell'importo fino a 10 giorni "
         "dall'uscita, e dell'intero importo negli ultimi 10 giorni."),
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
    subtitle="School trip Florence – Impruneta Astronomical Observatory, outbound and return  ·  6 November 2026",
    meta="Prepared for %s  ·  16 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "A minibus reserved for the class, with its driver: from Piazza Savonarola to the observatory, "
        "waiting during the visit and back to the starting point, with no intermediate stops and no "
        "other passengers."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 25 passenger seats plus guide seat and driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats with seat belts, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "For 13 students and their teachers there are more than enough seats: everyone sits comfortably "
        "and backpacks and coats fit without blocking the aisle. At under 8 metres long the minibus has "
        "no trouble on the hilly roads of Impruneta up to the observatory, where a full-size coach would "
        "struggle."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Time"],
    svc=[
        ("Fri 6 Nov",
         "<b>Piazza Savonarola (Florence) → «Ermanno lo Storpio» Astronomical Observatory, Via della "
         "Sodera 2, Impruneta.</b> About 17 km, arrival around 10:50, in time for the 11:00 visit.",
         "departure 10:15"),
        ("Fri 6 Nov",
         "<b>Observatory → Piazza Savonarola.</b> The minibus waits for the group during the visit. "
         "Arrival around 13:30.",
         "departure 13:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Minibus with driver, Piazza Savonarola – Impruneta Observatory and return, with waiting during "
         "the visit", "€ 550.00", "+ VAT 10%"),
        ("Florence municipal check point for the minibus to enter Piazza Savonarola",
         "€ 421.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 971.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,068.10.",
    perhead=("The price is for the vehicle, not per person: it does not change if a student is absent on "
             "the day. With a meeting point outside the check point area the total drops to € 605.00 VAT "
             "included: see the notes."),
    h_incluso="Included.",
    incluso=(
        "Minibus with driver, fuel, tolls, parking, the Florence check point, waiting during the visit and "
        "full insurance. The service ends before lunch: there are no driver's meals at your charge."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Entrance and visit to the observatory. Waiting beyond the 13:00 departure, € 50.00 per hour. "
        "Additional stops, quoted on request."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 320.43", "VAT included"),
        ("Balance, by 6 November 2026, the day of the service", "€ 747.67", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05. "
          "We issue an electronic invoice made out to the school."),
    h_note="Notes",
    note=[
        ("<b>The Florence check point.</b> Piazza Savonarola lies within the part of the city that a "
         "tourist coach may enter only by paying the municipal check point, € 421.00 for the day. It is "
         "the heaviest item on a half-day trip. If a meeting point just outside that area suits the "
         "class, we will suggest one: no check point is due and the total drops to € 605.00 VAT "
         "included. If you prefer to stay in Piazza Savonarola, the price is the one shown above, with "
         "no other costs."),
        ("<b>The times.</b> Leaving at 10:15 the group reaches the observatory around 10:50: on a Friday "
         "morning the traffic out of Florence towards Galluzzo and Tavarnuzze can be slow, and this margin "
         "gets you there in time for the 11:00 visit. We leave again at 13:00 and are in Piazza "
         "Savonarola around 13:30. If the visit ends earlier, just tell the driver."),
        ("<b>At the observatory.</b> Via della Sodera is a narrow hill road: the minibus drops you at the "
         "entrance and waits nearby for the whole visit, ready for the return. Please give us a contact "
         "at the observatory for the arrival."),
        ("<b>Number of people.</b> 13 students and 1 or 2 teachers make 14–15 people on 25 seats: there "
         "is room even if someone joins."),
        ("<b>To confirm we need</b> the final number of participants, the name and mobile number of the "
         "teacher in charge on the day and the school's details for the electronic invoice (recipient "
         "code or PEC)."),
        ("<b>Validity, availability and cancellation.</b> This quotation is valid until 26 October 2026, "
         "to give the school management time to decide; until then the vehicle is held for you. The "
         "booking becomes firm on receipt of the deposit. Once confirmed, a cancellation is charged at "
         "50% of the amount up to 10 days before the trip, and at the full amount in the last 10 days."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Scuole Pie Fiorentine, prof. Giorgio Rotellini")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Osservatorio_Impruneta_6_novembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

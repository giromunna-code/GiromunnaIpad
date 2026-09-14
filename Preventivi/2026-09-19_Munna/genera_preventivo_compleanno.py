#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il servizio serale del compleanno di sabato
19 settembre 2026 (Prato -> Piazzale Michelangelo, Firenze -> Prato).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_compleanno.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_compleanno.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0919-PM"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Serata di compleanno · Prato → Piazzale Michelangelo (Firenze) · 19 settembre 2026",
    meta="Preparato per %s  ·  14 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il gruppo di 10 ragazzi, con lo stesso conducente per tutta la serata.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 10 ragazzi a bordo restano ampiamente liberi i due terzi dei posti: spazio per stare comodi "
        "tutta la sera. I 7,64 metri del mezzo non creano alcun problema nei pressi di Piazzale Michelangelo, "
        "dove i bus turistici sostano abitualmente."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Sab 19 set",
         "<b>Prato → Piazzale Michelangelo (Firenze) → Prato.</b> "
         "Partenza alle 23:00 dal punto di ritrovo a Prato (indirizzo da confermare). Circa 20 km fino a "
         "Piazzale Michelangelo, arrivo previsto verso le 23:25. Mezzo e conducente restano a disposizione "
         "sul posto per tutta la serata; rientro verso le 02:30, arrivo a Prato verso le 03:00.",
         "circa 23:00 – 03:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 19 set — serata a disposizione: Prato → Piazzale Michelangelo → Prato, ore 23:00-03:00 circa",
         "€ 480,00", "+ IVA 10%"),
        ("Supplemento rientro dopo le 02:00 (per mezzo)", "€ 250,00", "+ IVA 10%"),
        ("Permesso ZTL Bus per la sosta a Piazzale Michelangelo (Firenze)",
         "€ 415,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.145,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.259,50.",
    perhead="Sono circa € 125,95 a persona per la serata.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi, parcheggio, assicurazione completa, permesso ZTL Bus per la "
        "sosta a Piazzale Michelangelo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Cibo e bevande per i ragazzi. Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. "
        "Eventuali soste aggiuntive o cambi di programma, quotati su richiesta."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 377,85", "IVA inclusa"),
        ("Saldo, entro il 18 settembre 2026", "€ 881,65", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Il supplemento per il rientro dopo le 02:00.</b> Il programma richiesto riporta il gruppo a Prato "
         "verso le 03:00, oltre l'orario delle 02:00 dal quale scatta la maggiorazione notturna di € 250,00 "
         "per mezzo. È già compresa nel prezzo qui sopra: se gli orari restano questi non si aggiunge altro."),
        ("<b>Il permesso ZTL Bus per Piazzale Michelangelo.</b> La sosta per salita e discesa a Piazzale "
         "Michelangelo rientra nella ZTL Bus del Comune di Firenze, che copre l'intero centro abitato ed è "
         "attiva 24 ore su 24: serve un permesso a pagamento, € 415,00 per il nostro minibus, che acquistiamo "
         "noi ed è già compreso nel prezzo qui sopra."),
        ("<b>Un gruppo di soli minorenni.</b> Per tutta la serata il conducente resta con il mezzo parcheggiato "
         "nei pressi di Piazzale Michelangelo ed è raggiungibile al telefono. Ci è utile avere, prima della "
         "partenza, il numero di un genitore o di un accompagnatore di riferimento per la serata."),
        ("<b>Punto di ritrovo a Prato e punto di sosta a Firenze.</b> Ci serve l'indirizzo esatto da cui "
         "partire a Prato e, se possibile, un riferimento preciso per la sosta del mezzo a Piazzale "
         "Michelangelo: lo confermiamo con il conducente prima del 19."),
        ("<b>Orari di massima.</b> Gli orari indicati, 23:00-03:00, sono quelli richiesti: se il programma "
         "della serata slitta anche di mezz'ora basta avvisarci, senza costi aggiuntivi entro un margine "
         "ragionevole. Oltre, si applica l'attesa di € 50,00 all'ora per mezzo indicata sopra."),
        ("<b>Tempi stretti e cancellazione.</b> Mancano 5 giorni al servizio: la prenotazione rientra già "
         "nella fascia di cancellazione più stretta, quella degli ultimi 10 giorni, per cui in caso di "
         "disdetta è dovuto il 100% del prezzo. Conviene perciò confermare al più presto per bloccare mezzo "
         "e conducente; per lo stesso motivo chiediamo il saldo entro il 18 settembre, invece dei soliti "
         "termini più lunghi."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei partecipanti, l'indirizzo di partenza a "
         "Prato, un recapito telefonico del genitore o accompagnatore di riferimento e i dati per la fattura."),
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
    subtitle="Birthday evening · Prato → Piazzale Michelangelo (Florence) · 19 September 2026",
    meta="Prepared for %s  ·  14 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for the group of 10 teenagers, with the same driver throughout the evening.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 10 teenagers on board, two thirds of the seats stay free: plenty of room to be comfortable "
        "all evening. At 7.64 m the minibus has no trouble near Piazzale Michelangelo, where tour coaches "
        "stop every day."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sat 19 Sep",
         "<b>Prato → Piazzale Michelangelo (Florence) → Prato.</b> "
         "Departure at 23:00 from the meeting point in Prato (address to be confirmed). About 20 km to "
         "Piazzale Michelangelo, expected arrival around 23:25. Vehicle and driver stay at your disposal on "
         "site for the whole evening; return around 02:30, arriving back in Prato around 03:00.",
         "approx. 23:00 – 03:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sat 19 Sep — evening at disposal: Prato → Piazzale Michelangelo → Prato, approx. 23:00-03:00",
         "€ 480.00", "+ VAT 10%"),
        ("Surcharge for return after 02:00 (per vehicle)", "€ 250.00", "+ VAT 10%"),
        ("Florence ZTL Bus permit for the stop at Piazzale Michelangelo",
         "€ 415.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,145.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,259.50.",
    perhead="That is about € 125.95 per person for the evening.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, tolls, parking, full insurance, the Florence ZTL Bus permit for the stop "
        "at Piazzale Michelangelo."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Food and drinks for the group. Waiting beyond the times set out here, € 50.00 per hour per vehicle. "
        "Any additional stops or changes to the plan, quoted on request."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 377.85", "VAT included"),
        ("Balance, by 18 September 2026", "€ 881.65", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The surcharge for returning after 02:00.</b> The requested plan brings the group back to Prato "
         "around 03:00, past the 02:00 threshold at which the € 250.00 per-vehicle night surcharge applies. "
         "It is already included in the price above: if the times stay as they are, nothing further is added."),
        ("<b>The Florence ZTL Bus permit for Piazzale Michelangelo.</b> Stopping for pick-up and drop-off at "
         "Piazzale Michelangelo falls inside Florence's city-wide ZTL Bus zone, which covers the whole "
         "built-up area and is active 24 hours a day: a paid permit is required, € 415.00 for our minibus, "
         "which we purchase and which is already included in the price above."),
        ("<b>A group of minors only.</b> Throughout the evening the driver stays with the vehicle parked near "
         "Piazzale Michelangelo and can be reached by phone. It is useful to have, before departure, the "
         "number of a parent or adult responsible for the evening."),
        ("<b>Meeting point in Prato and waiting spot in Florence.</b> We need the exact pick-up address in "
         "Prato and, if possible, a precise reference for where the vehicle will wait at Piazzale "
         "Michelangelo: we will confirm this with the driver before the 19th."),
        ("<b>Approximate timing.</b> The times shown, 23:00-03:00, are those requested: if the evening's plan "
         "shifts by half an hour or so, just let us know, at no extra cost within a reasonable margin. "
         "Beyond that, the € 50.00 per hour per vehicle waiting rate above applies."),
        ("<b>Short notice and cancellation.</b> Only 5 days remain before the service: the booking already "
         "falls in the tightest cancellation band, the last 10 days, where 100% of the price is due in case "
         "of cancellation. It is therefore worth confirming as soon as possible to secure the vehicle and "
         "driver; for the same reason we are asking for the balance by 18 September, rather than the usual "
         "longer terms."),
        ("<b>To confirm we need</b> the final number of participants, the pick-up address in Prato, a phone "
         "contact for the parent or adult responsible, and your invoicing details."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Munna")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Compleanno_19_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

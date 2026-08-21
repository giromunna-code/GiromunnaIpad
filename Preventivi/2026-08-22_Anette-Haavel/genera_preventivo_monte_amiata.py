#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la giornata aggiuntiva sul Monte Amiata del
22 agosto 2026, per il gruppo di Anette Haavel a Corte Francigena (Rif. GM-2026-0819-CF).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_monte_amiata.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_monte_amiata.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0822-CF"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Giornata aggiuntiva sul Monte Amiata  ·  Corte Francigena (Montalcino)  ·  sabato 22 agosto 2026",
    meta="Preparato per %s  ·  21 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="I mezzi",
    mezzo_intro=(
        "Aggiunta al vostro programma di Corte Francigena (Rif. GM-2026-0819-CF): gli stessi due minibus "
        "già con il vostro gruppo restano a vostra disposizione per questa giornata in più."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, ampio vano bagagli.<br/>"
        "<b>Mercedes-Benz Tourengo</b> — 28 posti passeggeri più l'autista, 7,86 m. Aria condizionata, "
        "sedili reclinabili, vano bagagli."
    ),
    mezzo_close=(
        "Entrambi i mezzi raggiungono Corte Francigena, e allo stesso modo arrivano ai borghi e ai punti "
        "panoramici del Monte Amiata, dove un autobus gran turismo non passa."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", ""],
    svc=[
        ("Sab 22 ago",
         "<b>Corte Francigena → Monte Amiata → Corte Francigena.</b> Orario di partenza da concordare "
         "con voi più vicino alla data. Mezzi e conducenti restano a vostra disposizione per l'intera "
         "giornata, fra i borghi e i punti panoramici del monte, con rientro in serata alla tenuta.",
         "2 mezzi"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 22 ago — Mercedes-Benz Beluga, mezzo e conducente per l'intera giornata",
         "€ 750,00", "+ IVA 10%"),
        ("Sab 22 ago — Mercedes-Benz Tourengo, mezzo e conducente per l'intera giornata",
         "€ 750,00", "+ IVA 10%"),
        ("Hotel autisti",
         "€ 150,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.650,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.815,00.",
    h_incluso="Incluso.",
    incluso=(
        "Entrambi i mezzi e i rispettivi conducenti, carburante, pedaggi autostradali, assicurazione completa "
        "— come già previsto dal vostro preventivo Corte Francigena (Rif. GM-2026-0819-CF), di cui questa "
        "giornata fa parte a tutti gli effetti. Il pernottamento dei conducenti per questa giornata è incluso "
        "nel prezzo, come indicato in tabella."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Ingressi, pranzi, guide e mance. Attesa oltre gli orari concordati, € 50,00 all'ora per mezzo. Soste "
        "aggiuntive o modifiche di percorso, quotate su richiesta. Rientro alla tenuta dopo le 02:00, "
        "€ 250,00 per mezzo — le stesse condizioni già valide per il resto del vostro programma."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Saldo, entro 5 giorni dal servizio", "€ 1.815,00", "IVA inclusa"),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Conferma.</b> Girolamo vi richiama a breve per confermare la disponibilità di entrambi i "
         "mezzi per sabato: fino a quella telefonata questo è un prezzo, non una prenotazione."),
        ("<b>Itinerario e orario.</b> Concordiamo insieme a voi l'orario di partenza e le tappe sul monte "
         "più vicino alla data; i due mezzi viaggiano insieme per tutta la giornata, come già per la gita "
         "di giovedì a Pienza."),
        ("<b>Per confermare</b> ci basta la vostra conferma e, se cambia, il numero dei passeggeri per "
         "sabato."),
    ],
    closing=("Restiamo a disposizione per qualsiasi chiarimento.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Additional day on Monte Amiata  ·  Corte Francigena (Montalcino)  ·  Saturday 22 August 2026",
    meta="Prepared for %s  ·  21 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicles",
    mezzo_intro=(
        "An addition to your Corte Francigena programme (Ref. GM-2026-0819-CF): the same two minibuses "
        "already with your group remain at your disposal for this extra day."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, large luggage compartment.<br/>"
        "<b>Mercedes-Benz Tourengo</b> — 28 passenger seats plus driver, 7.86 m. Air conditioning, "
        "reclining seats, luggage compartment."
    ),
    mezzo_close=(
        "Both vehicles reach Corte Francigena, and in the same way reach the villages and viewpoints of "
        "Monte Amiata, which a full-size coach cannot."
    ),
    h_servizio="Service",
    svc_head=["Date", "Route", ""],
    svc=[
        ("Sat 22 Aug",
         "<b>Corte Francigena → Monte Amiata → Corte Francigena.</b> Departure time to be agreed with "
         "you closer to the date. Both vehicles and drivers remain at your disposal for the whole day, "
         "among the villages and viewpoints of the mountain, returning to the property in the evening.",
         "2 vehicles"),
    ],
    h_prezzo="Price",
    price_rows=[
        ("Sat 22 Aug — Mercedes-Benz Beluga, vehicle and driver for the whole day",
         "€ 750.00", "+ VAT 10%"),
        ("Sat 22 Aug — Mercedes-Benz Tourengo, vehicle and driver for the whole day",
         "€ 750.00", "+ VAT 10%"),
        ("Drivers' hotel",
         "€ 150.00", "+ VAT 10%"),
    ],
    price_total_label="Total, net of VAT",
    price_total="€ 1,650.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,815.00.",
    h_incluso="Included.",
    incluso=(
        "Both vehicles and their drivers, fuel, motorway tolls, full insurance — as already covered by your "
        "Corte Francigena quotation (Ref. GM-2026-0819-CF), of which this day is a part. The drivers' "
        "overnight stay for this day is included in the price, as shown in the table."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Entrance fees, lunches, guides and gratuities. Waiting beyond the agreed times, € 50.00 per hour "
        "per vehicle. Additional stops or changes to the itinerary, quoted on request. Return to the "
        "property after 02:00, € 250.00 per vehicle — the same terms already in place for the rest of your "
        "programme."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Balance, within 5 days of service", "€ 1,815.00", "VAT included"),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Confirmation.</b> Girolamo will call you shortly to confirm both vehicles are available for "
         "Saturday: until that call, this is a price, not a booking."),
        ("<b>Itinerary and timing.</b> We will agree the departure time and the stops on the mountain with "
         "you closer to the date; the two vehicles travel together for the whole day, as for Thursday's "
         "excursion to Pienza."),
        ("<b>To confirm,</b> your go-ahead is enough, and, if it changes, the number of passengers for "
         "Saturday."),
    ],
    closing=("We remain at your disposal for any clarification.<br/><br/>"
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
        "foot": ParagraphStyle("foot", alignment=TA_JUSTIFY, spaceBefore=6, spaceAfter=2,
                               fontName="Helvetica", fontSize=8.2,
                               textColor=MUTED, leading=11.4),
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
    cols = [26 * mm, usable - 26 * mm - 22 * mm, 22 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for giorno, desc, mezzi in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % giorno, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
            Paragraph(mezzi, S["cellmut"]),
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

    # --- note (intestazione ed elenco non si spezzano fra due pagine)
    note_block = [Paragraph(L["h_note"], S["h2"])]
    for n in L["note"]:
        note_block.append(Paragraph("·  " + n, S["note"]))
    F.append(KeepTogether(note_block))

    F.append(Spacer(1, 8))
    F.append(Paragraph(L["closing"], S["small"]))

    doc.build(F)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--cliente", "--client", dest="cliente", default="Anette Haavel")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Monte_Amiata_22_agosto_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

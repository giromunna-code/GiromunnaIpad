#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento Massarosa (LU) -> Milano Malpensa
del 1 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_massarosa_malpensa.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_massarosa_malpensa.py --lingua en --cliente "Client Name"

Senza --cliente il preventivo esce senza intestatario: la richiesta e' arrivata
senza nome, quindi va rigenerato appena si conosce.
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

RIF = "GM-2026-1001-MM"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferimento privato Massarosa (LU) → Aeroporto di Milano Malpensa  ·  giovedì 1° ottobre 2026, partenza ore 02:00  ·  16 passeggeri",
    meta="Preparato per %s  ·  20 agosto 2026  ·  Rif. " + RIF,
    meta_nocliente="Preparato il 20 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo di 16 persone, con un solo conducente.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 16 passeggeri restano dieci posti liberi: spazio comodo per un viaggio notturno e per i "
        "bagagli di sedici persone in partenza. I 7,64 metri del mezzo entrano dove un autobus gran "
        "turismo non passa."
    ),
    h_servizio="Il servizio",
    svc_head=["Orario", "Percorso", "Distanza"],
    svc=[
        ("01:45",
         "<b>L'autista è sul posto a Massarosa (LU)</b>, quindici minuti prima della partenza.",
         "—"),
        ("02:00",
         "<b>Massarosa (LU) → Aeroporto di Milano Malpensa.</b> A11, A12 direzione Genova, A26 e uscita "
         "per l'aeroporto. A quest'ora la strada è libera e si evita il nodo di Milano.",
         "circa 330 km<br/>3 h 30"),
        ("05:30",
         "<b>Arrivo al terminal di partenza.</b> Il conducente scarica i bagagli.",
         "—"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Gio 1 ott — Massarosa (LU) → Aeroporto di Milano Malpensa, circa 330 km", "€ 1.550,00", "+ IVA 10%"),
        ("Maggiorazione per la partenza notturna delle 02:00", "€ 250,00", "+ IVA 10%"),
        ("Parcheggio bus a Malpensa, prima ora", "€ 35,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente — nessun pernottamento necessario",
         "<i>nessun onere</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.835,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.018,50.",
    perhead="Sono circa € 126,00 a persona.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, assicurazione completa e movimentazione "
        "dei bagagli. Sull'orario di partenza da Massarosa vi lasciamo una tolleranza di 30 minuti."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre gli orari concordati, € 50,00 all'ora per mezzo. La sosta a Malpensa oltre la "
        "prima ora. Soste aggiuntive o modifiche all'itinerario, quotate su richiesta. Il viaggio di "
        "ritorno da Malpensa, che quotiamo volentieri a parte. Su questo servizio non serve alcun "
        "pernottamento del conducente e non vi addebitiamo nulla a questo titolo."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 605,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.413,50", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>L'orario del volo.</b> Partendo alle 02:00 siete al terminal verso le 05:30, giusto per un "
         "volo dalle 07:30 in poi. Se il vostro parte più tardi conviene spostare la partenza: mandateci "
         "numero e orario del volo e ve lo confermiamo."),
        ("<b>Il terminal.</b> Il Terminal 1 e il Terminal 2 si raggiungono da svincoli diversi. "
         "Ci basta il numero del volo e lo verifichiamo noi."),
        ("<b>Il punto di carico a Massarosa.</b> Il CAP 55054 copre tutto il comune, piana e collina. "
         "Mandateci l'indirizzo esatto, o una posizione WhatsApp: alle due di notte è meglio avere "
         "verificato prima il punto di salita."),
        ("<b>I bagagli.</b> Il vano prende senza problemi sedici valigie da stiva. Segnalateci in "
         "anticipo sci, sacche da golf o altri colli fuori misura."),
        ("<b>Per confermare ci servono</b> l'indirizzo di carico, numero e orario del volo, il numero "
         "definitivo dei passeggeri e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è libero e lo teniamo a vostra disposizione per "
         "tutta la validità del preventivo. Cancellazione gratuita oltre 60 giorni prima del servizio; "
         "da 60 a 30 giorni viene trattenuto l'acconto; da 30 a 10 giorni il 50%; negli ultimi 10 giorni "
         "il 100%. Preventivo valido fino al 3 settembre 2026."),
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
    subtitle="Private transfer Massarosa (LU) → Milan Malpensa Airport  ·  Thursday 1 October 2026, departure 02:00  ·  16 passengers",
    meta="Prepared for %s  ·  20 August 2026  ·  Ref. " + RIF,
    meta_nocliente="Prepared on 20 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of 16, with a single driver.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 16 passengers ten seats stay free: comfortable room for a night journey and for the "
        "luggage of sixteen people flying out. At 7.64 m the minibus goes where a full-size coach cannot."
    ),
    h_servizio="The service",
    svc_head=["Time", "Route", "Distance"],
    svc=[
        ("01:45",
         "<b>The driver is on site in Massarosa (LU)</b>, fifteen minutes before departure.",
         "—"),
        ("02:00",
         "<b>Massarosa (LU) → Milan Malpensa Airport.</b> A11, A12 towards Genoa, A26 and the airport "
         "exit. At this hour the road is clear and the Milan ring is avoided.",
         "approx. 330 km<br/>3 h 30"),
        ("05:30",
         "<b>Arrival at your departure terminal.</b> The driver unloads the luggage.",
         "—"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Thu 1 Oct — Massarosa (LU) → Milan Malpensa Airport, about 330 km", "€ 1,550.00", "+ VAT 10%"),
        ("Night departure supplement, 02:00 start", "€ 250.00", "+ VAT 10%"),
        ("Coach parking at Malpensa, first hour", "€ 35.00", "+ VAT 10%"),
        ("Driver's board and lodging — no overnight stay required",
         "<i>no charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,835.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,018.50.",
    perhead="That is about € 126.00 per person.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, full insurance and luggage handling. On the departure "
        "time from Massarosa we allow you 30 minutes of grace."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the agreed times, € 50.00 per hour per vehicle. Parking at Malpensa beyond the "
        "first hour. Additional stops or changes to the itinerary, quoted on request. The return journey "
        "from Malpensa, which we are glad to quote separately. This service requires no overnight stay "
        "for the driver and we charge you nothing on that count."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 605.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,413.50", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Your flight time.</b> Leaving at 02:00 puts you at the terminal around 05:30, right for a "
         "flight from 07:30 onwards. If yours leaves later it is worth moving the departure: send us the "
         "flight number and time and we will confirm it."),
        ("<b>The terminal.</b> Terminal 1 and Terminal 2 are reached from different exits. "
         "Just send us the flight number and we will check it."),
        ("<b>The pick-up point in Massarosa.</b> Postcode 55054 covers the whole municipality, plain and "
         "hills alike. Send us the exact address, or a WhatsApp location: at two in the morning it is "
         "better to have checked the boarding point beforehand."),
        ("<b>Luggage.</b> The hold takes sixteen checked suitcases without difficulty. Do tell us in "
         "advance about skis, golf bags or other oversized items."),
        ("<b>To confirm we need</b> the pick-up address, the flight number and time, the final passenger "
         "count and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is free and we hold it for you for the whole "
         "validity of this quotation. Cancellation is free of charge more than 60 days before the "
         "service; from 60 to 30 days the deposit is retained; from 30 to 10 days 50%; in the last 10 "
         "days 100%. Quotation valid until 3 September 2026."),
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
    # la richiesta e' arrivata senza nome: senza --cliente l'intestatario si omette
    meta = (L["meta"] % cliente) if cliente else L["meta_nocliente"]
    F.append(Paragraph(meta, S["meta"]))

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
    cols = [17 * mm, usable - 17 * mm - 30 * mm, 30 * mm]
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Transfer_Massarosa_Malpensa_1_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

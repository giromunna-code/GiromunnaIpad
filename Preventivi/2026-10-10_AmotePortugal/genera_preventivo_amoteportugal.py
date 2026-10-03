#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasporto AMOTEPORTUGAL, 10-11 ottobre 2026
(due giornate del loro tour di 8 giorni in Toscana, le uniche con mezzo disponibile).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_amoteportugal.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_amoteportugal.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1010-AP"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Val d'Orcia e Maremma, nel tour AMOTEPORTUGAL  ·  10-11 ottobre 2026",
    meta="Preparato per %s  ·  3 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus per il vostro gruppo di 22 persone (21 ospiti più 1 accompagnatore), con lo "
        "stesso conducente per i due giorni di servizio."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 22 ospiti a bordo restano quattro posti liberi, utili anche per i bagagli del "
        "trasferimento del 10 ottobre."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Sab 10 ott",
         "<b>Borgo Elissa (Certaldo) → Pienza → La Boutique del Pastore → Montepulciano → Hotel Dei "
         "Capitani (Montalcino).</b> Partenza alle 9:30, circa 95 km fino a Pienza, arrivo in tempo per "
         "la visita guidata delle 11:30. Alle 13:30 breve trasferimento a La Boutique del Pastore per "
         "la sosta gastronomica, poi a Montepulciano per la passeggiata e la degustazione delle 17:00. "
         "Partenza alle 18:30, 28 km fino a Montalcino, arrivo in hotel verso le 19:00. Il mezzo "
         "trasporta anche i bagagli del gruppo per il trasferimento di struttura.",
         "circa 9:30 – 19:00"),
        ("Dom 11 ott",
         "<b>Hotel Dei Capitani (Montalcino) → Saturnia → Pitigliano → Piombaia → Hotel Dei "
         "Capitani.</b> Partenza alle 8:30, circa 85 km fino alle terme libere di Saturnia. "
         "Prosecuzione per Pitigliano, 25 km, per il pranzo. Nel pomeriggio si risale verso Montalcino "
         "per la degustazione delle 17:00 a Piombaia; rientro in hotel verso le 19:00. La giornata più "
         "lunga del servizio, circa 195 km.",
         "circa 8:30 – 19:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 10 ott — Borgo Elissa → Pienza → Montepulciano → Montalcino", "€ 1.050,00", "+ IVA 10%"),
        ("Dom 11 ott — Montalcino → Saturnia → Pitigliano → Montalcino", "€ 1.250,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente, 1 notte (10 ottobre)",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.300,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.530,00.",
    perhead="Sono circa € 115,00 a persona per i due giorni, sul gruppo di 22 persone indicato.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggi, assicurazione completa, "
        "movimentazione bagagli per il trasferimento del 10 ottobre."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio del conducente per la notte del 10 ottobre, a vostro carico: la prenotazione "
        "e il pagamento li curate voi direttamente. Ingressi, pranzi, degustazioni, guide e mance. "
        "Attesa oltre gli orari qui indicati, € 50,00 all'ora. Soste aggiuntive o modifiche "
        "all'itinerario, quotate su richiesta. Rientro dopo le 02:00, € 250,00. Eventuali permessi per "
        "l'accesso dei bus ai centri storici di Montepulciano o Pitigliano, se richiesti dai rispettivi "
        "comuni."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 760,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.770,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Il nostro servizio copre solo il 10 e l'11 ottobre.</b> Il programma che ci avete inviato "
         "copre otto giornate, dal 7 al 14 ottobre: al momento abbiamo disponibilità solo per queste "
         "due. Per il 7-9 e il 12-14 ottobre vi serve un altro fornitore di trasporto; fatecelo sapere "
         "se vi può essere utile un consiglio."),
        ("<b>Il trasferimento del 10 ottobre.</b> Il gruppo lascia Borgo Elissa con tutti i bagagli e "
         "arriva in hotel a Montalcino solo alla sera, dopo tre tappe. Il vano del Beluga porta senza "
         "problemi i bagagli di 22 persone per un soggiorno di una settimana, ma segnalateci in "
         "anticipo eventuali colli fuori misura."),
        ("<b>Accesso ai centri storici di Montepulciano e Pitigliano.</b> Sono entrambi borghi con "
         "strade stretto e centri storici regolamentati. Il Beluga, sotto gli 8 metri, raggiunge punti "
         "che un autobus gran turismo non può toccare, ma vi chiediamo di farvi confermare dalle guide "
         "locali il punto di discesa e un eventuale permesso comunale, così lo verifichiamo per tempo."),
        ("<b>L'11 ottobre è la giornata più lunga,</b> circa 195 km fra andata e ritorno su Saturnia e "
         "Pitigliano: gli orari indicati nel programma (8:30-19:00) sono già una buona base, ma se la "
         "sosta alle terme o il pranzo a Pitigliano si allungano, segnalatecelo per tenere il "
         "conducente informato."),
        ("<b>Vitto e alloggio del conducente.</b> Serve una notte, quella del 10 ottobre a Montalcino: "
         "resta a vostro carico, la prenotate e pagate voi direttamente. La soluzione più comoda è lo "
         "stesso Hotel Dei Capitani dove soggiorna il gruppo."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero per il 10 e l'11 ottobre e "
         "lo teniamo a vostra disposizione fino alla validità di questo preventivo; la prenotazione "
         "diventa definitiva alla ricezione dell'acconto. Mancano oggi 7 giorni al primo servizio: la "
         "prenotazione rientra già nella fascia degli ultimi 10 giorni, quindi un'eventuale "
         "cancellazione dopo la conferma comporta il 100% del prezzo. Preventivo valido fino al "
         "9 ottobre 2026."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, un recapito telefonico "
         "o WhatsApp della persona che viaggia con il gruppo, e i vostri dati di fatturazione."),
    ],
    closing=("Restiamo a disposizione per qualsiasi chiarimento e in attesa di un vostro riscontro.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Giuseppe Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Val d'Orcia and the Maremma, within the AMOTEPORTUGAL tour  ·  10-11 October 2026",
    meta="Prepared for %s  ·  3 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "One minibus for your group of 22 (21 guests plus 1 tour leader), with the same driver for "
        "both days of service."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 22 guests on board four seats stay free, which also helps with luggage on the "
        "10 October transfer."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sat 10 Oct",
         "<b>Borgo Elissa (Certaldo) → Pienza → La Boutique del Pastore → Montepulciano → Hotel Dei "
         "Capitani (Montalcino).</b> Departure at 9:30 am, about 95 km to Pienza, arriving in time for "
         "the 11:30 am guided visit. At 1:30 pm a short transfer to La Boutique del Pastore for the "
         "culinary stop, then on to Montepulciano for the walking tour and the 5:00 pm tasting. "
         "Departure at 6:30 pm, 28 km to Montalcino, reaching the hotel around 7:00 pm. The coach also "
         "carries the group's luggage for the change of accommodation.",
         "approx. 9:30 am – 7:00 pm"),
        ("Sun 11 Oct",
         "<b>Hotel Dei Capitani (Montalcino) → Saturnia → Pitigliano → Piombaia → Hotel Dei "
         "Capitani.</b> Departure at 8:30 am, about 85 km to the free outdoor thermal pools at "
         "Saturnia. On to Pitigliano, 25 km, for lunch. In the afternoon back up towards Montalcino for "
         "the 5:00 pm tasting at Piombaia; return to the hotel around 7:00 pm. The longest day of the "
         "service, about 195 km.",
         "approx. 8:30 am – 7:00 pm"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sat 10 Oct — Borgo Elissa → Pienza → Montepulciano → Montalcino", "€ 1,050.00", "+ VAT 10%"),
        ("Sun 11 Oct — Montalcino → Saturnia → Pitigliano → Montalcino", "€ 1,250.00", "+ VAT 10%"),
        ("Driver's board and lodging, 1 night (10 October)",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,300.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,530.00.",
    perhead="That is about € 115.00 per person for the two days, for the group of 22 indicated.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, parking, full insurance, luggage handling for the "
        "10 October transfer."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's board and lodging for the night of 10 October, which remain at your charge: you "
        "book and pay for them directly. Entrance fees, lunches, tastings, guides and gratuities. "
        "Waiting beyond the times set out here, € 50.00 per hour. Additional stops or changes to the "
        "itinerary, quoted on request. Return to the hotel after 2:00 am, € 250.00. Any permit for "
        "coach access to the historic centres of Montepulciano or Pitigliano, should the local "
        "municipalities require one."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 760.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,770.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Our service covers only 10 and 11 October.</b> The programme you sent runs over eight "
         "days, from 7 to 14 October: at the moment we only have availability for these two. For "
         "7-9 and 12-14 October you will need another transport provider; let us know if a "
         "recommendation would help."),
        ("<b>The transfer on 10 October.</b> The group leaves Borgo Elissa with all the luggage and "
         "only reaches the hotel in Montalcino in the evening, after three stops. The Beluga's hold "
         "takes a week's luggage for 22 guests without difficulty, but do tell us in advance about any "
         "oversized items."),
        ("<b>Access to the historic centres of Montepulciano and Pitigliano.</b> Both are hill towns "
         "with narrow streets and regulated historic centres. The Beluga, under 8 metres, reaches "
         "points a full-size coach cannot, but please have the local guides confirm the drop-off point "
         "and any municipal permit, so we can verify it in good time."),
        ("<b>11 October is the longest day,</b> about 195 km there and back to Saturnia and "
         "Pitigliano: the times in the programme (8:30 am – 7:00 pm) are a solid base, but if the stop "
         "at the thermal pools or lunch in Pitigliano run long, let us know so we can keep the driver "
         "informed."),
        ("<b>The driver's board and lodging.</b> One night is needed, that of 10 October in Montalcino: "
         "it remains at your charge, and you book and pay for it directly. The easiest solution is the "
         "same Hotel Dei Capitani where the group is staying."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free for 10 and 11 October and "
         "we hold it for you until this quotation's validity date; the booking becomes firm on receipt "
         "of the deposit. With 7 days to the first service today, this booking already falls in the "
         "last-10-days band, so any cancellation after confirmation incurs 100% of the price. "
         "Quotation valid until 9 October 2026."),
        ("<b>To confirm we need</b> the final passenger count, a mobile or WhatsApp contact for the "
         "person travelling with the group, and your invoicing details."),
    ],
    closing=("We remain at your disposal for any clarification and look forward to hearing from you.<br/><br/>"
             "Kind regards,<br/>"
             "Giuseppe Munna — GiroMunna NCC, Tuscany · +39 335 587 4744 · info@giromunna.com"),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="AMOTEPORTUGAL s.r.o.")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_AmotePortugal_10-11_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

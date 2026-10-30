#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la gita del Cral A.T. Pistoia, 8 dicembre 2026:
Pistoia - Castiglione del Lago - Arezzo - Pistoia, giornata intera.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_cral_at_pistoia.py --lingua it --cliente "Natascia, Cral A.T. Pistoia"
    python3 genera_preventivo_cral_at_pistoia.py --lingua en --cliente "Natascia, Cral A.T. Pistoia"
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

RIF = "GM-2026-1208-AT"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Gita del Cral A.T. Pistoia: Pistoia – Castiglione del Lago – Arezzo – Pistoia  ·  martedì 8 dicembre 2026",
    meta="Preparato per %s  ·  30 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un autobus gran turismo riservato al vostro gruppo, con il conducente, per tutta la giornata: "
        "da Pistoia al lago Trasimeno, poi ad Arezzo per il pomeriggio e la sera, e ritorno a Pistoia. "
        "Il mezzo resta con voi a ogni tappa, senza altri passeggeri."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Tourismo</b> — autobus gran turismo, 51 posti passeggeri più accompagnatore e autista (51+1+1). Aria condizionata, "
        "sedili reclinabili, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Un autobus da turismo vero e proprio, comodo per una giornata con circa quattro ore di viaggio: "
        "c'è posto per tutto il gruppo e lo spazio per muoversi senza stare stretti."
    ),
    h_servizio="Il servizio",
    svc_head=["Orario", "Percorso", "Note"],
    svc=[
        ("ore 9:30",
         "<b>Pistoia, via dell'Annone.</b> Ritrovo alle 9:30, partenza alle 9:45. Il bus è sul posto dalle 9:20.",
         "ritrovo e partenza"),
        ("ore 9:45",
         "<b>Pistoia → Castiglione del Lago.</b> Circa 185 km, A11 e A1 fino a Valdichiana, poi lungo il Trasimeno. "
         "Arrivo verso le 12:00.",
         "circa 2 ore e 15"),
        ("ore 14:00",
         "<b>Castiglione del Lago → Arezzo.</b> Circa 50 km. Arrivo verso le 15:00.",
         "partenza 14:00"),
        ("ore 20:00",
         "<b>Arezzo → Pistoia, via dell'Annone.</b> Circa 125 km, A1 e A11. Arrivo verso le 21:45.",
         "partenza 20:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Autobus con conducente a disposizione per la giornata di martedì 8 dicembre: Pistoia – "
         "Castiglione del Lago – Arezzo – Pistoia, circa 400 km", "€ 1.000,00", "+ IVA 10%"),
        ("Eventuali parcheggi del mezzo", "a carico vostro", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.000,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.100,00.",
    perhead=("Il prezzo è per il mezzo, non per persona: non cambia se siete qualcuno in meno."),
    h_incluso="Incluso.",
    incluso=(
        "Autobus con conducente per tutta la giornata, carburante, pedaggi autostradali e "
        "assicurazione completa. Le soste a Castiglione del Lago e ad Arezzo sono comprese: il "
        "conducente resta a vostra disposizione."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Eventuali parcheggi del mezzo, pagati sul posto. Attesa oltre la partenza da Arezzo delle 20:00, € 50,00 all'ora. "
        "Ingressi, visite guidate, pasti del gruppo e fermate aggiuntive non previste dal programma."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 330,00", "IVA inclusa"),
        ("Saldo, entro l'8 dicembre 2026, giorno del servizio", "€ 770,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>L'8 dicembre sulla A1.</b> È festa e chiude il ponte dell'Immacolata: al mattino il traffico "
         "verso sud è in genere scorrevole, mentre la sera il rientro verso Firenze è spesso rallentato, "
         "soprattutto fra Valdarno e Firenze Sud. L'arrivo a Pistoia previsto verso le 21:45 può slittare "
         "verso le 22:15: vi consigliamo di dirlo ai partecipanti, per chi viene a riprenderli."),
        ("<b>Ad Arezzo con i mercatini di Natale.</b> Il giorno dell'Immacolata la città è piena e "
         "l'accesso dei mezzi verso il centro è regolato. Vi lasciamo e vi riprendiamo nel punto "
         "consentito ai bus turistici più vicino alla città alta e ve lo indichiamo prima della partenza, insieme al "
         "numero del conducente. Se in quel punto la sosta dei bus è a pagamento, il costo è a "
         "carico vostro, come gli altri eventuali parcheggi della giornata. Per ripartire puntuali alle 20:00 conviene fissare il ritrovo al "
         "bus per le 19:45: con la folla della sera ci vuole qualche minuto in più."),
        ("<b>Castiglione del Lago.</b> Arrivando verso le 12:00 avete due ore: il tempo per il pranzo "
         "e una passeggiata nel borgo fino alla Rocca. Se avete prenotato un ristorante, indicateci quale: "
         "vi lasciamo all'area di sosta dei bus più comoda."),
        ("<b>Il ritrovo in via dell'Annone.</b> Indicateci il punto preciso (numero civico o "
         "riferimento) dove volete che il bus si fermi per la salita e per il rientro della sera: deve essere "
         "un punto dove un autobus gran turismo possa accostare e sostare qualche minuto."),
        ("<b>Per confermare ci servono</b> il nome e il "
         "cellulare di un referente che viaggia con il gruppo e i dati per la fattura."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione fino al 6 novembre 2026, data di validità del preventivo; la prenotazione diventa "
         "definitiva alla ricezione dell'acconto. Dopo la conferma, fino all'8 novembre la "
         "cancellazione comporta la perdita dell'acconto; dal 9 al 28 novembre si addebita il 50% "
         "dell'importo, negli ultimi 10 giorni l'intero importo."),
    ],
    closing=("Grazie Natascia, per qualsiasi cosa chiamami pure. A presto!<br/><br/>"
             "Un abbraccio,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Cral A.T. Pistoia day trip: Pistoia – Castiglione del Lago – Arezzo – Pistoia  ·  Tuesday 8 December 2026",
    meta="Prepared for %s  ·  30 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "A coach reserved for your group, with its driver, for the whole day: from Pistoia to Lake "
        "Trasimeno, then to Arezzo for the afternoon and evening, and back to Pistoia. The vehicle stays "
        "with you at every stop, with no other passengers."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Tourismo</b> — touring coach, 51 passenger seats plus guide seat and driver (51+1+1). Air conditioning, "
        "reclining seats, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "A proper touring coach, comfortable for a day with about four hours on the road: there is "
        "room for the whole group and space to move without feeling cramped."
    ),
    h_servizio="The service",
    svc_head=["Time", "Route", "Notes"],
    svc=[
        ("9:30",
         "<b>Pistoia, via dell'Annone.</b> Meeting at 9:30, departure at 9:45. The coach is there from 9:20.",
         "meeting and departure"),
        ("9:45",
         "<b>Pistoia → Castiglione del Lago.</b> About 185 km, A11 and A1 to Valdichiana, then along Lake "
         "Trasimeno. Arrival around 12:00.",
         "about 2 h 15"),
        ("14:00",
         "<b>Castiglione del Lago → Arezzo.</b> About 50 km. Arrival around 15:00.",
         "departure 14:00"),
        ("20:00",
         "<b>Arezzo → Pistoia, via dell'Annone.</b> About 125 km, A1 and A11. Arrival around 21:45.",
         "departure 20:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Coach with driver at your disposal for the day on Tuesday 8 December: Pistoia – "
         "Castiglione del Lago – Arezzo – Pistoia, about 400 km", "€ 1,000.00", "+ VAT 10%"),
        ("Any vehicle parking fees", "at your charge", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,000.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,100.00.",
    perhead=("The price is for the vehicle, not per person: it does not change if a few of you are missing."),
    h_incluso="Included.",
    incluso=(
        "Coach with driver for the whole day, fuel, motorway tolls and full insurance. "
        "The stops in Castiglione del Lago and Arezzo are included: the driver remains at your disposal."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Any vehicle parking fees, paid on the spot. Waiting beyond the 20:00 departure from Arezzo, € 50.00 per hour. "
        "Entrance fees, guided tours, the group's meals and additional stops not in the programme."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 330.00", "VAT included"),
        ("Balance, by 8 December 2026, the day of the service", "€ 770.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>8 December on the A1.</b> It is a public holiday and the end of the Immacolata long weekend: "
         "in the morning southbound traffic is usually light, while in the evening the return towards "
         "Florence is often slow, especially between Valdarno and Firenze Sud. The arrival in Pistoia "
         "planned for around 21:45 may slip towards 22:15: we suggest telling participants, for whoever "
         "is collecting them."),
        ("<b>Arezzo with the Christmas markets.</b> On the Immacolata holiday the city is packed and "
         "vehicle access towards the centre is regulated. We drop you off and pick you up at the "
         "point permitted for coaches closest to the upper town and will tell you where before departure, together "
         "with the driver's number. If parking for coaches there is charged, the cost is at your charge, "
         "like any other parking fees during the day. To leave on time at 20:00 it is best to meet at the coach at 19:45: "
         "with the evening crowds it takes a few extra minutes."),
        ("<b>Castiglione del Lago.</b> Arriving around 12:00 you have two hours: time for lunch and a "
         "walk through the old town up to the Rocca. If you have booked a restaurant, tell us which one: "
         "we will drop you at the most convenient coach stop."),
        ("<b>The meeting point in via dell'Annone.</b> Please give us the exact spot (street number or "
         "landmark) where you want the coach to stop for boarding and for the evening return: it must be a "
         "place where a full-size coach can pull in and wait a few minutes."),
        ("<b>To confirm we need</b> the name and mobile number of a "
         "contact person travelling with the group and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you until "
         "6 November 2026, the validity date of this quotation; the booking becomes firm on receipt of the "
         "deposit. Once confirmed, a cancellation up to 8 November forfeits the deposit; from 9 to "
         "28 November 50% of the amount is charged, and the full amount in the last 10 days."),
    ],
    closing=("Thank you Natascia, call me any time if you need anything. Talk soon!<br/><br/>"
             "A big hug,<br/>"
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Natascia, Cral A.T. Pistoia")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Pistoia_Castiglione_Arezzo_8_dicembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

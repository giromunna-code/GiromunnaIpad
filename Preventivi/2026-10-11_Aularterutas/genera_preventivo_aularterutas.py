#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la giornata Siena · Monteriggioni · San Gimignano · Firenze
dell'11 ottobre 2026 (Aularterutas, fino a 25 persone).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_aularterutas.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_aularterutas.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1011-LA"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Giornata a disposizione Siena · Monteriggioni · San Gimignano · Firenze  ·  domenica 11 ottobre 2026",
    meta="Preparato per %s  ·  30 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo fino a 25 persone, a disposizione per tutta la giornata.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 25 ospiti a bordo resta un posto libero, per esempio per la vostra guida o l'accompagnatore. "
        "Sotto gli 8 metri di lunghezza, il Beluga si muove bene fra i piazzali ai piedi dei borghi e le vie "
        "del centro di Firenze, dove un autobus gran turismo fatica o non arriva."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Dom 11 ott",
         "<b>NH Siena (Via La Lizza 1) → Monteriggioni → San Gimignano → Grand Hotel Adriatico, "
         "Via Maso Finiguerra 9, Firenze.</b> "
         "Il mezzo è davanti all'hotel dalle 08:15; partenza alle 08:30, circa 20 km e 25 minuti fino al "
         "parcheggio bus ai piedi delle mura di Monteriggioni. Ripartenza alle 11:00 per San Gimignano, circa "
         "30 km, arrivo verso le 11:40 al terminal bus di Porta San Giovanni. Ripartenza alle 16:00 per "
         "Firenze, circa 55 km, arrivo all'hotel verso le 17:15-17:30. Mezzo e conducente a vostra disposizione "
         "per tutta la giornata, con i bagagli a bordo.",
         "circa 08:15 – 17:30"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Dom 11 ott — giornata a disposizione: Siena → Monteriggioni → San Gimignano → Firenze",
         "€ 1.250,00", "+ IVA 10%"),
        ("Permesso bus turistici del Comune di Siena", "€ 160,00", "+ IVA 10%"),
        ("Checkpoint bus del Comune di San Gimignano", "€ 220,00", "+ IVA 10%"),
        ("Permesso di accesso bus al centro di Firenze, fino all'hotel", "€ 450,00", "+ IVA 10%"),
        ("Vitto del conducente, pranzo dell'11 ottobre (nessun pernottamento)",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.080,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.288,00.",
    perhead="Sono circa € 92,00 a persona con 25 partecipanti.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per tutta la giornata, avvicinamento a Siena e rientro dalla nostra base, carburante, "
        "pedaggi, parcheggio bus a Monteriggioni, assicurazione completa, carico e scarico dei "
        "bagagli. I permessi di Siena e Firenze e il checkpoint di San Gimignano sono indicati a parte nella tabella del prezzo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il pranzo del conducente, che resta a vostro carico. Ingressi, guide, pasti e mance. Attesa oltre gli "
        "orari qui indicati, € 50,00 all'ora. Soste aggiuntive o modifiche all'itinerario, quotate su richiesta. "
        "Un eventuale mezzo di supporto per i bagagli, quotato su richiesta."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 680,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.608,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>I bagagli sono il punto da guardare per primo.</b> Il gruppo lascia l'hotel di Siena e arriva a "
         "Firenze solo la sera: le valigie viaggiano con voi tutto il giorno. Il vano del Beluga porta bene una "
         "ventina di valigie di misura normale; venticinque valigie grandi non ci stanno tutte. Ci servono quindi "
         "il numero e la misura dei bagagli. Se sono troppi, le soluzioni sono due: chiedere agli ospiti una "
         "valigia media a testa, oppure far viaggiare i bagagli a parte con un furgone direttamente da Siena "
         "all'hotel di Firenze, che vi quotiamo su richiesta. Durante le visite il mezzo resta chiuso nel "
         "parcheggio bus: gli oggetti di valore conviene tenerli con sé."),
        ("<b>Gli orari.</b> Abbiamo letto le 11:00 e le 16:00 come orari di <i>partenza</i> da Monteriggioni e "
         "da San Gimignano. Da Siena a Monteriggioni bastano 25 minuti, quindi il gruppo resta nel borgo circa "
         "due ore e mezza, e a San Gimignano più di quattro. Se invece le 11:00 sono l'orario di arrivo a "
         "Monteriggioni, spostiamo la partenza da Siena alle 10:30 senza variazioni di prezzo: ditecelo e "
         "aggiorniamo il programma."),
        ("<b>L'arrivo a Firenze.</b> Via Maso Finiguerra è nel centro storico, dove un bus turistico entra "
         "solo con un permesso comunale a parte. Lo abbiamo messo a preventivo per portarvi davanti all'hotel "
         "con le valigie. In alternativa possiamo lasciarvi al punto di discesa bus autorizzato più vicino, a "
         "10-15 minuti a piedi, e togliere i € 450,00 del permesso: con i bagagli al seguito ve lo sconsigliamo."),
        ("<b>La partenza da Siena.</b> L'NH Siena è in Via La Lizza, fuori dalle mura e raggiungibile dal mezzo. "
         "Il Comune di Siena richiede comunque il permesso per i bus turistici anche solo per una salita di "
         "passeggeri: è la voce da € 160,00 in tabella, la sbrighiamo noi."),
        ("<b>San Gimignano.</b> I bus lasciano il gruppo al terminal di Porta San Giovanni, all'ingresso del "
         "centro storico, e lì lo riprendono alle 16:00. L'accesso passa dal checkpoint comunale per i bus "
         "turistici: è la voce da € 220,00 in tabella, la sbrighiamo noi. Il conducente vi lascia il suo numero alla partenza, "
         "così ci si ritrova senza problemi."),
        ("<b>Vitto del conducente.</b> Non serve alcun pernottamento: il conducente parte la mattina dalla nostra "
         "base e ci rientra la sera. Resta a vostro carico il suo pranzo dell'11 ottobre, che organizzate e pagate "
         "voi: la cosa più semplice è aggiungerlo al pranzo del gruppo a San Gimignano."),
        ("<b>Il numero dei passeggeri.</b> Il Beluga ha 26 posti oltre all'autista. Con 25 ospiti resta un posto "
         "per la guida o l'accompagnatore; se a bordo foste più di 26, avvisateci subito."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, numero e misura dei bagagli, un "
         "recapito telefonico o WhatsApp della persona che accompagna il gruppo e i vostri dati di fatturazione."),
        ("<b>Prenotazione e cancellazione.</b> La prenotazione diventa definitiva alla ricezione dell'acconto. "
         "La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene trattenuto "
         "l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. "
         "Mancando oggi 11 giorni al servizio, la prenotazione ricade nella fascia da 30 a 10 giorni, e dal "
         "1° ottobre passerà negli ultimi 10 giorni. Preventivo valido fino al 3 ottobre 2026."),
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
    subtitle="Full day at disposal Siena · Monteriggioni · San Gimignano · Florence  ·  Sunday 11 October 2026",
    meta="Prepared for %s  ·  30 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of up to 25, at your disposal for the whole day.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 25 guests on board one seat stays free, for your guide or tour leader. At under 8 metres the "
        "Beluga moves easily between the coach parks below the hill towns and the streets of central Florence, "
        "where a full-size coach struggles or cannot go."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sun 11 Oct",
         "<b>NH Siena (Via La Lizza 1) → Monteriggioni → San Gimignano → Grand Hotel Adriatico, "
         "Via Maso Finiguerra 9, Florence.</b> "
         "The vehicle is at the hotel from 08:15; departure at 08:30, about 20 km and 25 minutes to the coach "
         "park below the walls of Monteriggioni. Departure at 11:00 for San Gimignano, about 30 km, reaching the "
         "Porta San Giovanni coach terminal around 11:40. Departure at 16:00 for Florence, about 55 km, reaching "
         "the hotel around 17:15-17:30. Vehicle and driver at your disposal all day, with the luggage on board.",
         "approx. 08:15 – 17:30"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sun 11 Oct — full day at disposal: Siena → Monteriggioni → San Gimignano → Florence",
         "€ 1,250.00", "+ VAT 10%"),
        ("City of Siena tourist coach permit", "€ 160.00", "+ VAT 10%"),
        ("City of San Gimignano coach checkpoint", "€ 220.00", "+ VAT 10%"),
        ("Coach access permit for central Florence, to the hotel door", "€ 450.00", "+ VAT 10%"),
        ("Driver's meal, lunch on 11 October (no overnight stay)",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,080.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,288.00.",
    perhead="That is about € 92.00 per person with 25 participants.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, positioning to Siena and return to our base, fuel, tolls, coach "
        "parking at Monteriggioni, full insurance, luggage loading and unloading. The Siena and Florence permits "
        "and the San Gimignano checkpoint are shown separately in the price table."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's lunch, which remains at your charge. Entrance fees, guides, meals and gratuities. Waiting "
        "beyond the times set out here, € 50.00 per hour. Additional stops or changes to the itinerary, quoted on "
        "request. A separate luggage vehicle, if needed, quoted on request."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 680.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,608.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Luggage is the first thing to look at.</b> The group checks out in Siena and only reaches Florence "
         "in the evening, so the suitcases travel with you all day. The Beluga's hold takes about twenty "
         "normal-size suitcases comfortably; twenty-five large ones will not all fit. We therefore need the number "
         "and size of the bags. If there are too many, there are two solutions: ask guests for one medium "
         "suitcase each, or send the luggage separately by van straight from Siena to the Florence hotel, which we "
         "can quote on request. During the visits the vehicle stays locked in the coach park: valuables are best "
         "kept with you."),
        ("<b>Timings.</b> We have read 11:00 and 16:00 as <i>departure</i> times from Monteriggioni and San "
         "Gimignano. Siena to Monteriggioni takes only 25 minutes, so the group has about two and a half hours in "
         "the village and more than four in San Gimignano. If 11:00 is instead your arrival time in Monteriggioni, "
         "we move the Siena departure to 10:30 at no change in price: just let us know and we will update the "
         "programme."),
        ("<b>Arriving in Florence.</b> Via Maso Finiguerra is in the historic centre, which a tourist coach may "
         "only enter with a separate city permit. We have included it so we can bring you to the hotel door with "
         "your luggage. Alternatively we can drop you at the nearest authorised coach stop, 10-15 minutes' walk "
         "away, and remove the € 450.00 permit: with luggage in tow we would not recommend it."),
        ("<b>Leaving Siena.</b> The NH Siena is on Via La Lizza, outside the walls and reachable by the vehicle. "
         "The City of Siena still requires its tourist coach permit even for a passenger pick-up: that is the "
         "€ 160.00 line in the table, and we take care of it."),
        ("<b>San Gimignano.</b> Coaches drop groups at the Porta San Giovanni terminal, at the entrance to the "
         "historic centre, and collect them there at 16:00. Access goes through the town's checkpoint for "
         "tourist coaches: that is the € 220.00 line in the table, and we take care of it. The driver will give you his number on departure so "
         "meeting up again is straightforward."),
        ("<b>The driver's meal.</b> No overnight stay is needed: the driver leaves our base in the morning and "
         "returns in the evening. His lunch on 11 October remains at your charge, arranged and paid for by you: "
         "the simplest option is to add him to the group lunch in San Gimignano."),
        ("<b>Passenger numbers.</b> The Beluga has 26 seats besides the driver. With 25 guests one seat remains "
         "for the guide or tour leader; if there would be more than 26 on board, please tell us straight away."),
        ("<b>To confirm we need</b> the final passenger count, the number and size of the bags, a mobile or "
         "WhatsApp contact for the person accompanying the group, and your invoicing details."),
        ("<b>Booking and cancellation.</b> The booking becomes firm on receipt of the deposit. Cancellation is "
         "free of charge more than 60 days before the service; from 60 to 30 days the deposit is retained; from "
         "30 to 10 days 50% of the price is charged; in the last 10 days, 100%. With 11 days to the service today, "
         "this booking falls in the 30-to-10-day band, and from 1 October it moves into the last 10 days. "
         "Quotation valid until 3 October 2026."),
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
    F.append(KeepTogether([
        Paragraph(L["h_pagamento"], S["h2"]),
        yt,
        Spacer(1, 6),
        Paragraph(L["bank"], S["small"]),
    ]))

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Aularterutas")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Siena_San_Gimignano_Firenze_11_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

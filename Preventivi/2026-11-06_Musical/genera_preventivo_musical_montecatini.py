#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento Firenze - Teatro Verdi di Montecatini
Terme, andata e ritorno, 6 novembre 2026 (compagnia di musical).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_musical_montecatini.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_musical_montecatini.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1106-MF"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferimento Firenze – Teatro Verdi di Montecatini Terme, andata e ritorno  ·  6 novembre 2026",
    meta="Preparato per %s  ·  6 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus riservato alla compagnia, con il conducente, per 22–23 persone: al mattino da "
        "Firenze direttamente al teatro, a fine spettacolo dal teatro di nuovo a Firenze, senza "
        "fermate intermedie e senza altri passeggeri."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con meno di 8 metri di lunghezza il Beluga arriva fin davanti al teatro, anche nelle vie del "
        "centro di Montecatini dove un autobus gran turismo non si ferma. E al ritorno, alle due di "
        "notte dopo una giornata di prove e di spettacolo, i sedili reclinabili si apprezzano."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Orario"],
    svc=[
        ("Ven 6 nov",
         "<b>Firenze → Teatro Verdi, Montecatini Terme.</b> Circa 50 km, autostrada A11. "
         "Arrivo al teatro entro le 10:00.",
         "partenza 8:30"),
        ("Notte 6–7 nov",
         "<b>Teatro Verdi, Montecatini Terme → Firenze.</b> Arrivo a Firenze verso le 2:50.",
         "partenza 2:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Venerdì 6 novembre — Firenze → Montecatini Terme", "€ 500,00", "+ IVA 10%"),
        ("Notte 6–7 novembre — Montecatini Terme → Firenze", "€ 500,00", "+ IVA 10%"),
        ("Supplemento rientro dopo le 02:00", "€ 250,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.250,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.375,00.",
    perhead=("Su 23 persone sono circa € 60,00 a testa per andata e ritorno, IVA inclusa. "
             "Il prezzo è per il mezzo, non per persona: non cambia se siete qualcuno in meno."),
    h_incluso="Incluso.",
    incluso=(
        "Minibus con conducente, carburante, pedaggi autostradali, parcheggi e assicurazione completa: "
        "nessun altro costo. Fra l'andata e il ritorno il mezzo rientra in sede: il conducente non resta "
        "in attesa al teatro e non ci sono pasti o pernottamenti a vostro carico."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre la partenza delle 2:00, € 50,00 all'ora. Fermate aggiuntive a Firenze, quotate "
        "su richiesta. L'eventuale permesso per entrare nella zona a traffico limitato di Firenze, "
        "per cui vedete le note."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 412,50", "IVA inclusa"),
        ("Saldo, entro il 6 novembre 2026, giorno del servizio", "€ 962,50", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Costumi, attrezzatura e strumenti.</b> Una compagnia di musical di solito non viaggia "
         "solo con le borse personali. Il vano del Beluga è ampio, ma se portate costumi, bauli, "
         "strumenti o parti di scenografia diteci quanti e quanto ingombranti: se non entrano, è "
         "meglio saperlo adesso e organizzare un trasporto a parte per il materiale."),
        ("<b>Il punto di partenza a Firenze.</b> Il centro di Firenze è zona a traffico limitato e per "
         "un bus turistico l'ingresso richiede il pagamento del check point, circa € 350 per ogni "
         "giornata. Qui le giornate sarebbero due, il 6 per l'andata e il 7 per il ritorno, che "
         "arriva dopo mezzanotte: circa € 700 in più. Vi proponiamo "
         "quindi un punto di ritrovo appena fuori dalla ZTL, comodo per tutti: indicateci la zona da "
         "cui partite e ve lo suggeriamo noi. Lo stesso vale per la discesa al ritorno."),
        ("<b>L'orario del mattino.</b> Per arrivare al teatro entro le 10:00 partiamo da Firenze alle "
         "8:30. Il venerdì mattina l'uscita di Firenze Nord e la A11 sono spesso trafficate: con questo "
         "margine arriviamo in tempo anche con qualche rallentamento. Se volete essere in teatro prima, "
         "anticipiamo senza costi aggiuntivi."),
        ("<b>Il ritorno alle 2:00.</b> Il rientro dopo le 02:00 comporta un supplemento di € 250,00, che "
         "abbiamo già messo a preventivo, così non ci sono sorprese. Il conducente è al teatro dalle "
         "1:45. Fra smontaggio, struccatura e saluti la sera dello spettacolo i tempi si allungano "
         "facilmente: se pensate di partire più tardi, ditecelo prima, perché l'attesa oltre le 2:00 "
         "si conteggia a € 50,00 all'ora. Vi chiediamo il nome di chi darà al conducente il via alla "
         "partenza."),
        ("<b>Il numero delle persone.</b> Il Beluga ha 26 posti: per 22–23 persone resta un piccolo "
         "margine, utile se si aggiunge qualcuno dello staff tecnico. Oltre i 26 non basta: in quel caso "
         "avvisateci prima della conferma."),
        ("<b>Al teatro.</b> Indicateci se il gruppo deve scendere all'ingresso degli artisti o a quello "
         "principale, e un recapito del teatro per l'arrivo del mattino."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, il punto di partenza e di "
         "arrivo a Firenze, cosa portate come materiale, il nome e il cellulare di un referente e i dati "
         "per la fattura."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione fino al 13 ottobre 2026, data di validità del preventivo; la prenotazione diventa "
         "definitiva alla ricezione dell'acconto. Mancando meno di 30 giorni al servizio, dopo la "
         "conferma la cancellazione comporta l'addebito del 50% dell'importo, e dell'intero importo "
         "negli ultimi 10 giorni."),
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
    subtitle="Transfer Florence – Teatro Verdi, Montecatini Terme, outbound and return  ·  6 November 2026",
    meta="Prepared for %s  ·  6 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "A minibus reserved for the company, with its driver, for 22–23 people: in the morning from "
        "Florence straight to the theatre, after the show from the theatre back to Florence, with no "
        "intermediate stops and no other passengers."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "At under 8 metres long the Beluga drives right up to the theatre, even in the streets of "
        "central Montecatini where a full-size coach cannot stop. And on the way back, at two in the "
        "morning after a day of rehearsals and performance, the reclining seats are welcome."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Time"],
    svc=[
        ("Fri 6 Nov",
         "<b>Florence → Teatro Verdi, Montecatini Terme.</b> About 50 km, A11 motorway. "
         "Arrival at the theatre by 10:00.",
         "departure 8:30"),
        ("Night 6–7 Nov",
         "<b>Teatro Verdi, Montecatini Terme → Florence.</b> Arrival in Florence around 2:50.",
         "departure 2:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Friday 6 November — Florence → Montecatini Terme", "€ 500.00", "+ VAT 10%"),
        ("Night 6–7 November — Montecatini Terme → Florence", "€ 500.00", "+ VAT 10%"),
        ("Supplement for return after 02:00", "€ 250.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,250.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,375.00.",
    perhead=("Across 23 people that is about € 60.00 each for the round trip, VAT included. "
             "The price is for the vehicle, not per person: it does not change if a few of you are missing."),
    h_incluso="Included.",
    incluso=(
        "Minibus with driver, fuel, motorway tolls, parking and full insurance: no other costs. Between "
        "the outbound and the return runs the vehicle goes back to base: the driver does not wait at the "
        "theatre and there are no meals or overnight stays at your charge."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the 2:00 departure, € 50.00 per hour. Additional stops in Florence, quoted on "
        "request. Any permit to enter the Florence restricted traffic zone — see the notes."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 412.50", "VAT included"),
        ("Balance, by 6 November 2026, the day of the service", "€ 962.50", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Costumes, equipment and instruments.</b> A musical company rarely travels with personal "
         "bags only. The Beluga's hold is large, but if you are bringing costumes, trunks, instruments "
         "or pieces of set, tell us how many and how bulky: if they do not fit, it is better to know now "
         "and arrange separate transport for the material."),
        ("<b>The departure point in Florence.</b> The centre of Florence is a restricted traffic zone, and "
         "entry for a tourist coach requires a check-point fee of about € 350 per day. Here it would be "
         "two days, the 6th for the outbound run and the 7th for the return, which arrives after "
         "midnight: about € 700 extra. We therefore suggest a "
         "meeting point just outside the zone, convenient for everyone: tell us the area you are leaving "
         "from and we will propose one. The same applies to the drop-off on the way back."),
        ("<b>The morning schedule.</b> To reach the theatre by 10:00 we leave Florence at 8:30. On a Friday "
         "morning the Firenze Nord junction and the A11 are often busy: this margin gets us there on time "
         "even with some delays. If you want to be at the theatre earlier, we bring it forward at no extra "
         "cost."),
        ("<b>The 2:00 return.</b> A return after 02:00 carries a supplement of € 250.00, already included "
         "in this quotation so there are no surprises. The driver is at the theatre from 1:45. Between "
         "get-out, make-up removal and goodbyes, times easily stretch on show night: if you expect to "
         "leave later, tell us in advance, as waiting beyond 2:00 is charged at € 50.00 per hour. Please "
         "let us know who will give the driver the signal to leave."),
        ("<b>Number of people.</b> The Beluga has 26 seats: for 22–23 people that leaves a small margin, "
         "useful if a member of the technical crew joins. Beyond 26 it is not enough: in that case please "
         "let us know before confirming."),
        ("<b>At the theatre.</b> Tell us whether the group should be dropped at the stage door or the main "
         "entrance, and give us a theatre contact for the morning arrival."),
        ("<b>To confirm we need</b> the final number of passengers, the departure and arrival point in "
         "Florence, what material you are bringing, the name and mobile number of a contact person and "
         "your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you until "
         "13 October 2026, the validity date of this quotation; the booking becomes firm on receipt of the "
         "deposit. With less than 30 days to the service, once confirmed a cancellation is charged at 50% "
         "of the amount, and at the full amount in the last 10 days."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Gianna, compagnia di musical di Firenze")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Firenze_Montecatini_6_novembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

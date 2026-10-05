#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento Prato - Milano Malpensa,
andata 7 novembre 2026 e ritorno 14 novembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_malpensa.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_malpensa.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1107-FG"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferimento Prato – Aeroporto di Milano Malpensa, andata e ritorno  ·  7 e 14 novembre 2026",
    meta="Preparato per %s  ·  5 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus riservato al vostro gruppo, fino a 25 passeggeri, con il conducente: partenza "
        "da Prato direttamente sotto casa o al punto di ritrovo che ci indicate, discesa davanti al "
        "terminal di Malpensa, e al ritorno lo stesso viaggio al contrario, senza fermate intermedie "
        "e senza altri passeggeri."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Per un viaggio di quasi quattro ore, e al ritorno di notte dopo un volo, i sedili reclinabili "
        "fanno la differenza. E con meno di 8 metri di lunghezza il Beluga entra nelle vie di Prato "
        "dove un autobus gran turismo non passa: il ritiro può avvenire molto più vicino a casa."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Orario"],
    svc=[
        ("Sab 7 nov",
         "<b>Prato → Aeroporto di Milano Malpensa.</b> Circa 320 km, in gran parte autostrada "
         "(A1 e A8). Arrivo al terminal intorno alle 8:45, traffico permettendo.",
         "partenza 5:00"),
        ("Sab 14 nov",
         "<b>Aeroporto di Milano Malpensa → Prato.</b> Il conducente vi aspetta agli arrivi con il "
         "cartello. Arrivo a Prato intorno alle 2:30–3:00 di notte.",
         "atterraggio 23:00 circa"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sabato 7 novembre — Prato → Malpensa", "€ 1.650,00", "+ IVA 10%"),
        ("Sabato 14 novembre — Malpensa → Prato", "€ 1.650,00", "+ IVA 10%"),
        ("Supplemento rientro dopo le 02:00 (14 novembre)", "€ 250,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 3.550,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 3.905,00.",
    perhead=("Su 25 passeggeri sono € 156,20 a persona per andata e ritorno, IVA inclusa. "
             "Il prezzo è per il mezzo, non per persona: non cambia se il gruppo è più piccolo."),
    h_incluso="Incluso.",
    incluso=(
        "Minibus con conducente, carburante, pedaggi autostradali, parcheggi e assicurazione completa. "
        "Attesa gratuita a Malpensa fino a 90 minuti dall'atterraggio effettivo, per quanto il volo "
        "ritardi. Il mezzo rientra in sede dopo ogni trasferimento: non ci sono pasti né pernottamenti "
        "del conducente a vostro carico."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre i 90 minuti dall'atterraggio, € 50,00 all'ora. Fermate o deviazioni non "
        "previste dal percorso, quotate su richiesta."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 1.171,50", "IVA inclusa"),
        ("Saldo, entro il 7 novembre 2026, giorno della partenza", "€ 2.733,50", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>L'orario del volo di andata.</b> Partendo da Prato alle 5:00 si arriva a Malpensa "
         "verso le 8:45. Per un volo internazionale è un margine sicuro se il decollo è dalle "
         "11:30 in poi; se il vostro volo parte prima, la partenza da Prato va anticipata. "
         "Mandateci il numero e l'orario del volo e fissiamo l'ora giusta insieme."),
        ("<b>Il volo di ritorno.</b> Ci serve il numero del volo del 14 novembre: lo seguiamo in "
         "tempo reale e il conducente si regola sull'atterraggio effettivo. L'attesa è gratuita "
         "fino a 90 minuti dall'atterraggio, quanto basta di solito per bagagli e controlli; "
         "per un volo extra Schengen, con il controllo passaporti, conviene avvisarci."),
        ("<b>Il rientro di notte.</b> Con l'atterraggio verso le 23:00, fra ritiro bagagli e circa "
         "tre ore e mezza di strada si arriva a Prato fra le 2:30 e le 3:00. Per questo abbiamo già "
         "messo a preventivo il supplemento per il rientro dopo le 02:00, così non ci sono sorprese. "
         "Se il volo arrivasse prima, il supplemento non si applica e ve lo togliamo."),
        ("<b>I bagagli.</b> Per una settimana di viaggio ognuno avrà la sua valigia. Il vano del "
         "Beluga è ampio, ma 25 valigie grandi più i bagagli a mano lo riempiono. Indicateci quante "
         "valigie da stiva e quanti bagagli a mano porterete in tutto: se il carico supera lo spazio, "
         "è meglio saperlo ora che alle cinque di mattina."),
        ("<b>Il punto di partenza a Prato.</b> Ci serve l'indirizzo esatto di ritiro e di arrivo. "
         "Se si trova dentro le mura, nella zona a traffico limitato, vi proponiamo un punto di "
         "ritrovo appena fuori, comodo da raggiungere con le valigie."),
        ("<b>Il numero dei passeggeri.</b> Il Beluga ha 26 posti: per un gruppo fino a 25 persone "
         "va benissimo. Ogni bambino, anche piccolo, conta come un passeggero. Se il gruppo dovesse "
         "crescere oltre i 26, avvisateci prima della conferma."),
        ("<b>Per confermare ci servono</b> i numeri e gli orari dei due voli, l'indirizzo di ritiro "
         "a Prato, il numero definitivo dei passeggeri e dei bagagli, il nome e il cellulare di un "
         "referente del gruppo, e i dati per la fattura."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero nelle due date e lo "
         "teniamo a vostra disposizione fino al 19 ottobre 2026, data di validità del preventivo; la "
         "prenotazione diventa definitiva alla ricezione dell'acconto. Le penali si calcolano dalla "
         "data della partenza, il 7 novembre: da 60 a 30 giorni prima si trattiene l'acconto, da 30 "
         "a 10 giorni prima il 50% dell'importo, negli ultimi 10 giorni l'intero importo."),
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
    subtitle="Transfer Prato – Milan Malpensa Airport, outbound and return  ·  7 and 14 November 2026",
    meta="Prepared for %s  ·  5 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "A minibus reserved for your group, up to 25 passengers, with its driver: departure from "
        "Prato right at your door or at the meeting point you choose, drop-off in front of the "
        "Malpensa terminal, and on the way back the same journey in reverse, with no intermediate "
        "stops and no other passengers."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "On a journey of almost four hours, and on the way back at night after a flight, reclining "
        "seats make a real difference. And at under 8 metres long the Beluga gets into Prato streets "
        "where a full-size coach cannot go: pick-up can be much closer to home."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Time"],
    svc=[
        ("Sat 7 Nov",
         "<b>Prato → Milan Malpensa Airport.</b> About 320 km, mostly motorway (A1 and A8). "
         "Arrival at the terminal around 8:45, traffic permitting.",
         "departure 5:00"),
        ("Sat 14 Nov",
         "<b>Milan Malpensa Airport → Prato.</b> The driver meets you in arrivals with a name sign. "
         "Arrival in Prato around 2:30–3:00 at night.",
         "landing around 23:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Saturday 7 November — Prato → Malpensa", "€ 1,650.00", "+ VAT 10%"),
        ("Saturday 14 November — Malpensa → Prato", "€ 1,650.00", "+ VAT 10%"),
        ("Supplement for return after 02:00 (14 November)", "€ 250.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 3,550.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 3,905.00.",
    perhead=("Across 25 passengers that is € 156.20 per person for the round trip, VAT included. "
             "The price is for the vehicle, not per person: it does not change if the group is smaller."),
    h_incluso="Included.",
    incluso=(
        "Minibus with driver, fuel, motorway tolls, parking and full insurance. Free waiting at "
        "Malpensa up to 90 minutes from actual landing, however late the flight. The vehicle returns "
        "to base after each transfer: there are no driver meals or overnight stays at your charge."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond 90 minutes from landing, € 50.00 per hour. Stops or detours not included in "
        "the route, quoted on request."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 1,171.50", "VAT included"),
        ("Balance, by 7 November 2026, the day of departure", "€ 2,733.50", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The outbound flight time.</b> Leaving Prato at 5:00 we reach Malpensa around 8:45. "
         "For an international flight that is a safe margin if take-off is from 11:30 onwards; if "
         "your flight leaves earlier, the departure from Prato must be brought forward. Send us the "
         "flight number and time and we will set the right hour together."),
        ("<b>The return flight.</b> We need the flight number for 14 November: we track it in real "
         "time and the driver works to the actual landing. Waiting is free up to 90 minutes from "
         "landing, usually enough for baggage and checks; for a non-Schengen flight, with passport "
         "control, please let us know."),
        ("<b>The night-time return.</b> With landing around 23:00, between baggage claim and about "
         "three and a half hours on the road you reach Prato between 2:30 and 3:00. That is why we "
         "have already included the supplement for a return after 02:00, so there are no surprises. "
         "If the flight lands earlier, the supplement does not apply and we will remove it."),
        ("<b>Luggage.</b> For a week away everyone will have a suitcase. The Beluga's hold is large, "
         "but 25 big suitcases plus hand luggage fill it. Please tell us how many checked suitcases "
         "and how many carry-on bags you will bring in total: if the load exceeds the space, it is "
         "better to know now than at five in the morning."),
        ("<b>The pick-up point in Prato.</b> We need the exact pick-up and drop-off address. If it "
         "is inside the city walls, in the restricted traffic zone, we will suggest a meeting point "
         "just outside, easy to reach with suitcases."),
        ("<b>Number of passengers.</b> The Beluga has 26 seats: for a group of up to 25 it is ideal. "
         "Every child, however small, counts as a passenger. If the group should grow beyond 26, "
         "please let us know before confirming."),
        ("<b>To confirm we need</b> the numbers and times of both flights, the pick-up address in "
         "Prato, the final number of passengers and pieces of luggage, the name and mobile number of "
         "a group contact, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free on both dates and we "
         "hold it for you until 19 October 2026, the validity date of this quotation; the booking "
         "becomes firm on receipt of the deposit. Cancellation charges run from the departure date, "
         "7 November: from 60 to 30 days before, the deposit is retained; from 30 to 10 days before, "
         "50% of the amount; in the last 10 days, the full amount."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Francesca Gori")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Prato_Malpensa_7-14_novembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

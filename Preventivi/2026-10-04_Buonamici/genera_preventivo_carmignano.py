#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento Tenuta di Artimino <-> Tenuta di
Capezzana, Carmignano (PO), del 4 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_carmignano.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_carmignano.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1004-CB"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferimento Tenuta di Artimino ↔ Tenuta di Capezzana, Carmignano (PO)  ·  4 ottobre 2026",
    meta="Preparato per %s  ·  16 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Il nostro mezzo di proprietà per il trasferimento del vostro gruppo tra le due tenute.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Il Beluga ha 26 posti passeggeri più l'autista: con un gruppo di circa 30 persone la capienza di "
        "un solo mezzo non basta. Questo preventivo è riferito a un solo Beluga; vi chiediamo il numero "
        "esatto dei partecipanti, così da confermarvi se serve un secondo minibus di supporto, con il "
        "relativo costo aggiuntivo da concordare a parte. I suoi 7,64 metri restano comunque un vantaggio "
        "per l'accesso ai piazzali delle due tenute, dove un autobus gran turismo fatica a entrare."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Dom 4 ott",
         "<b>Tenuta di Artimino → Tenuta di Capezzana</b>, Carmignano (PO). Trasferimento di circa 10 km "
         "tra le due tenute, con mezzo e conducente a disposizione indicativamente dalle 10:00 alle 12:00.",
         "circa 10:00 – 12:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Dom 4 ott — trasferimento Tenuta di Artimino → Tenuta di Capezzana (~10 km), "
         "mezzo a disposizione 10:00–12:00 circa", "€ 450,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 450,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 495,00.",
    perhead="Sono circa € 16,50 a persona su 30 partecipanti (il numero esatto resta da confermare).",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi, parcheggi e assicurazione completa per il trasferimento "
        "indicato. Non risulta alcun onere di accesso per le due tenute; ve lo confermiamo se una delle due "
        "strutture ne richiedesse uno."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre l'orario concordato, € 50,00 all'ora per mezzo. Soste aggiuntive, deviazioni di "
        "percorso o servizi oltre le 12:00, quotati a parte. Rientro dopo le 02:00, € 250,00 per mezzo. "
        "L'eventuale secondo minibus per la quota di gruppo che eccede i 26 posti del Beluga, da concordare "
        "separatamente in base al numero esatto dei partecipanti."
    ),
    h_pagamento="Pagamento e prenotazione",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 148,50", "IVA inclusa"),
        ("Saldo, il giorno del servizio", "€ 346,50", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. La prenotazione diventa "
          "definitiva alla ricezione dell'acconto: basta una vostra conferma via email e il bonifico, "
          "vi rispondiamo con la conferma scritta del servizio."),
    h_note="Note",
    note=[
        ("<b>Numero dei partecipanti.</b> La richiesta indica circa 30 persone, sopra i 26 posti del "
         "Beluga. Fateci sapere il numero esatto: se supera i 26, valutiamo insieme se e come inserire un "
         "secondo mezzo di supporto, con il relativo costo. Nel frattempo questo preventivo resta riferito "
         "a un solo Beluga."),
        ("<b>Accesso alle due tenute.</b> Le strade interne delle tenute vinicole sono spesso strette: vi "
         "chiediamo di far confermare a Tenuta di Artimino e a Tenuta di Capezzana il punto di carico e "
         "scarico e lo spazio di manovra per un mezzo di 7,64 m. Meglio saperlo ora che il giorno stesso."),
        ("<b>Percorso e orario.</b> L'orario indicato, 10:00–12:00, lo abbiamo preso come finestra di "
         "servizio per il trasferimento fra le due tenute. Confermateci se si tratta di un trasferimento "
         "di sola andata o se serve anche il rientro, e l'orario preciso di partenza da Artimino."),
        ("<b>Come si prenota.</b> Basta una vostra email di conferma di questo preventivo e il bonifico "
         "dell'acconto del 30% sull'IBAN sopra indicato; rispondiamo con la conferma scritta del servizio "
         "e blocchiamo il mezzo per il 4 ottobre."),
        ("<b>Validità e cancellazione.</b> Preventivo valido fino al 30 settembre 2026. Mancano oggi 18 "
         "giorni al servizio: la prenotazione rientra già nella fascia da 30 a 10 giorni, con trattenuta "
         "del 50% in caso di cancellazione; dal 24 settembre passa nell'ultima fascia, con trattenuta del "
         "100%. Conviene confermare al più presto per bloccare il mezzo."),
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
    subtitle="Transfer Tenuta di Artimino ↔ Tenuta di Capezzana, Carmignano (PO)  ·  4 October 2026",
    meta="Prepared for %s  ·  16 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="Our own vehicle for your group's transfer between the two estates.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "The Beluga seats 26 passengers plus the driver: with a group of about 30 people, one vehicle is "
        "not enough on its own. This quotation is for one Beluga only; please let us know the exact number "
        "of participants so we can confirm whether a second support minibus is needed, with its additional "
        "cost agreed separately. At 7.64 m it is still an advantage for reaching the courtyards of both "
        "estates, where a full-size coach struggles to get in."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sun 4 Oct",
         "<b>Tenuta di Artimino → Tenuta di Capezzana</b>, Carmignano (PO). A transfer of about 10 km "
         "between the two estates, with vehicle and driver at your disposal from approximately 10:00 to "
         "12:00.",
         "approx. 10:00 – 12:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sun 4 Oct — transfer Tenuta di Artimino → Tenuta di Capezzana (~10 km), "
         "vehicle at disposal approx. 10:00–12:00", "€ 450.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 450.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 495.00.",
    perhead="That is about € 16.50 per person for 30 participants (exact number to be confirmed).",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, tolls, parking and full insurance for the transfer described above. No "
        "access charge is currently known for either estate; we will confirm if one of the two properties "
        "requires one."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the agreed time, € 50.00 per hour per vehicle. Additional stops, route changes or "
        "service beyond 12:00, quoted separately. Return after 02:00, € 250.00 per vehicle. Any second "
        "minibus needed for the share of the group above the Beluga's 26 seats, to be agreed separately "
        "once the exact number of participants is known."
    ),
    h_pagamento="Payment and booking",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 148.50", "VAT included"),
        ("Balance, on the day of the service", "€ 346.50", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. The booking becomes firm on "
          "receipt of the deposit: an email confirming this quotation and the deposit transfer are all we "
          "need, and we will reply with written confirmation of the service."),
    h_note="Notes",
    note=[
        ("<b>Number of participants.</b> The request states about 30 people, above the Beluga's 26 seats. "
         "Please let us know the exact number: if it is above 26, we will work out together whether a "
         "second support vehicle is needed and its cost. In the meantime this quotation covers one Beluga "
         "only."),
        ("<b>Access at both estates.</b> The internal roads of wine estates are often narrow: please have "
         "Tenuta di Artimino and Tenuta di Capezzana confirm the pick-up/drop-off point and the manoeuvring "
         "space for a 7.64 m vehicle. Better settled now than on the day itself."),
        ("<b>Route and timing.</b> We have read the stated 10:00–12:00 as the service window for the "
         "transfer between the two estates. Please confirm whether this is a one-way transfer only or "
         "whether a return is also needed, and the precise departure time from Artimino."),
        ("<b>How to book.</b> An email confirming this quotation plus the 30% deposit transfer to the IBAN "
         "above are all we need; we will reply with written confirmation of the service and hold the "
         "vehicle for 4 October."),
        ("<b>Validity and cancellation.</b> Quotation valid until 30 September 2026. With 18 days to the "
         "service today, this booking already falls in the 30-to-10-day band: cancelling now retains 50% "
         "of the price; from 24 September it moves into the last band, with 100% retained. It is worth "
         "confirming soon to hold the vehicle."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Chiara Buonamici")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Carmignano_4_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

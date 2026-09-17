#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento del 18 settembre 2026:
aeroporto di Firenze → Casa Rufina, per i cinque ospiti del gruppo Alvora che
restano in Toscana dopo la partenza degli altri.

Integra il preventivo GM-2026-0913-BI (wine tour 13-18 settembre) e ne riprende
l'impaginazione.

    python3 genera_preventivo_casa_rufina.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_casa_rufina.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0918-BI"
RIF_MADRE = "GM-2026-0913-BI"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Aeroporto di Firenze → Casa Rufina  ·  venerdì 18 settembre 2026",
    meta=("Preparato per %s  ·  17 settembre 2026  ·  Rif. " + RIF +
          "  ·  Integra il preventivo " + RIF_MADRE),
    intro=(
        "Ecco il preventivo per il proseguimento che ci avete chiesto: dopo l'aeroporto, i cinque ospiti che "
        "restano in Toscana vengono accompagnati a Casa Rufina. Il ritiro anticipato alle 11:30 dall'hotel di "
        "Forte dei Marmi è confermato e non comporta alcun addebito."
    ),
    h_mezzo="Il mezzo",
    mezzo_intro="Lo stesso mezzo e lo stesso conducente già in servizio con voi dal 13 settembre.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    h_servizio="Il servizio",
    svc_head=["Data e ora", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Ven 18 set<br/>12:50",
         "<b>Sosta alle partenze dell'aeroporto di Firenze (FLR).</b> Discesa dei passeggeri in partenza e "
         "scarico dei loro bagagli; i cinque ospiti che proseguono restano a bordo con i propri.",
         "circa 20 minuti"),
        ("Ven 18 set<br/>13:10",
         "<b>Aeroporto di Firenze (FLR) → Casa Rufina.</b> Circa 30 km, arrivo verso le 14:00. "
         "Il conducente rientra poi alla base in giornata.",
         "circa 13:10 – 14:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Aeroporto di Firenze → Casa Rufina, 5 passeggeri, circa 30 km", "€ 350,00", "+ IVA 10%"),
        ("Ritiro dall'hotel alle 11:30 anziché alle 12:30", "<i>nessun addebito</i>", ""),
        ("Vitto e alloggio del conducente — nessuna notte aggiuntiva", "<i>invariato</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 350,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 385,00.",
    perhead=(
        "Il programma 13-18 settembre risulta già saldato per intero, e ve ne ringraziamo: questo è quindi "
        "l'unico importo che resta da corrispondere."
    ),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggio all'aeroporto di Firenze, assicurazione "
        "completa e movimentazione dei bagagli, sia di chi parte sia di chi prosegue. La sosta all'aeroporto è "
        "compresa fino a 30 minuti. L'aeroporto di Firenze non comporta oneri di accesso e la destinazione non si "
        "trova in zona a traffico limitato: non sono dovuti altri oneri."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre gli orari qui indicati, € 50,00 all'ora. Soste aggiuntive o cambi di destinazione, quotati su "
        "richiesta. Vitto e alloggio del conducente, che restano a vostro carico come da preventivo: questo "
        "trasferimento non aggiunge però alcuna notte, perché il 18 il conducente rientra alla base in giornata."
    ),
    h_pagamento="Pagamento",
    pay_text=(
        "Potete regolare l'importo con un bonifico dopo il servizio, con la relativa fattura: non c'è nulla da "
        "anticipare. Bonifico bancario intestato a Munna Girolamo Giuseppe — "
        "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."
    ),
    h_note="Note",
    note=[
        ("<b>L'indirizzo esatto di Casa Rufina.</b> Ci serve per confermare l'orario. I 30 km che ci avete indicato "
         "portano nella zona a sud-est di Firenze; se invece la destinazione è su nella valle della Sieve, verso "
         "Rufina e Pontassieve, sono una quarantina di chilometri e l'arrivo slitta di un quarto d'ora circa. "
         "Il prezzo non cambia in nessuno dei due casi: mandateci l'indirizzo e vi confermiamo l'orario esatto."),
        ("<b>L'ordine delle due tappe è quello giusto.</b> Prima l'aeroporto e poi Casa Rufina, come lo avete "
         "impostato voi: la destinazione si trova dall'altra parte di Firenze rispetto all'aeroporto, e passarci "
         "prima allungherebbe di oltre un'ora la corsa di chi deve imbarcarsi."),
        ("<b>I bagagli all'aeroporto.</b> È l'unico punto che può far perdere tempo. Al check-out dell'hotel fate "
         "caricare per ultime le valigie dei cinque ospiti che proseguono: restano davanti nel vano e all'aeroporto "
         "si scarica solo quello che parte, senza svuotare tutto il bagagliaio sul marciapiede delle partenze."),
        ("<b>Quante persone.</b> Abbiamo capito 16 ospiti in partenza e 5 che proseguono, per i 21 del programma: "
         "confermateci i numeri, perché il conducente controlla i passeggeri prima di lasciare l'aeroporto."),
        ("<b>Per confermare.</b> Trattandosi del servizio di domani basta un messaggio o un WhatsApp al "
         "+39 335 587 4744 con l'indirizzo di Casa Rufina e il numero dei passeggeri."),
    ],
    closing=("Grazie del saldo, che abbiamo ricevuto. Restiamo a disposizione e vi auguriamo "
             "buon ultimo giorno in Toscana.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Florence Airport → Casa Rufina  ·  Friday 18 September 2026",
    meta=("Prepared for %s  ·  17 September 2026  ·  Ref. " + RIF +
          "  ·  Supplements quotation " + RIF_MADRE),
    intro=(
        "Here is the quotation for the onward leg you asked about: after the airport, the five guests staying on "
        "in Tuscany are taken to Casa Rufina. The earlier 11:30 pick-up from the hotel in Forte dei Marmi is "
        "confirmed and carries no charge."
    ),
    h_mezzo="The vehicle",
    mezzo_intro="The same vehicle and the same driver who have been with you since 13 September.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    h_servizio="The service",
    svc_head=["Date and time", "Route", "Vehicle engaged"],
    svc=[
        ("Fri 18 Sep<br/>12:50",
         "<b>Stop at Florence Airport (FLR) departures.</b> Departing passengers get off and their luggage is "
         "unloaded; the five guests travelling on stay aboard with theirs.",
         "approx. 20 minutes"),
        ("Fri 18 Sep<br/>13:10",
         "<b>Florence Airport (FLR) → Casa Rufina.</b> About 30 km, reaching the property around 14:00. "
         "The driver then returns to base the same day.",
         "approx. 13:10 – 14:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Florence Airport → Casa Rufina, 5 passengers, about 30 km", "€ 350.00", "+ VAT 10%"),
        ("Pick-up from the hotel at 11:30 instead of 12:30", "<i>no charge</i>", ""),
        ("Driver's board and lodging — no additional night", "<i>unchanged</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 350.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 385.00.",
    perhead=(
        "The 13-18 September programme is already settled in full, for which our thanks: this is therefore the "
        "only amount left to pay."
    ),
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, parking at Florence Airport, full insurance and luggage handling "
        "for both the departing and the continuing guests. The airport stop is included for up to 30 minutes. "
        "Florence Airport carries no access fee and the destination does not sit inside a restricted traffic zone: "
        "no other charges apply."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the times set out here, € 50.00 per hour. Additional stops or a change of destination, "
        "quoted on request. The driver's board and lodging, which remain at your charge as per the quotation: this "
        "transfer adds no night at all, as on 18 September the driver returns to base the same day."
    ),
    h_pagamento="Payment",
    pay_text=(
        "You can settle the amount by bank transfer after the service, with its invoice: there is nothing to pay "
        "in advance. Bank transfer to Munna Girolamo Giuseppe — "
        "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."
    ),
    h_note="Notes",
    note=[
        ("<b>The exact address of Casa Rufina.</b> We need it to confirm the timing. The 30 km you mention point to "
         "the area south-east of Florence; if the destination is instead up the Sieve valley, towards Rufina and "
         "Pontassieve, it is about forty kilometres and the arrival shifts by roughly a quarter of an hour. "
         "The price is the same either way: send us the address and we will confirm the exact time."),
        ("<b>The order of the two stops is the right one.</b> Airport first and Casa Rufina afterwards, just as you "
         "set it out: the destination lies on the far side of Florence from the airport, and calling there first "
         "would add more than an hour to the run for those catching a flight."),
        ("<b>Luggage at the airport.</b> This is the one thing that can cost time. At hotel check-out, have the "
         "suitcases of the five guests travelling on loaded last: they stay at the front of the hold, and at the "
         "airport only the departing luggage comes out, without emptying the whole hold onto the departures kerb."),
        ("<b>How many guests.</b> We have understood 16 departing and 5 travelling on, out of the 21 on the "
         "programme: please confirm the numbers, as the driver counts passengers before leaving the airport."),
        ("<b>To confirm.</b> As this is tomorrow's service, a text or WhatsApp to +39 335 587 4744 with the Casa "
         "Rufina address and the passenger numbers is all we need."),
    ],
    closing=("Thank you for the balance, which has reached us. We remain at your disposal and wish you "
             "a fine last day in Tuscany.<br/><br/>"
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
    F.append(Paragraph(L["intro"], S["body"]))

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
    F.append(Paragraph(L["pay_text"], S["small"]))

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Alvora")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_18_settembre_2026_Casa_Rufina_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

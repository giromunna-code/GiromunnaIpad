#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il transfer serale Pescia -> Mantova
(Discoteca Mascara) di domenica 25 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_mantova.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_mantova.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1025-MN"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Transfer serale Pescia → Mantova, Discoteca Mascara  ·  domenica 25 ottobre 2026",
    meta="Preparato per %s  ·  16 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo di 14 persone, con lo stesso conducente per tutta la serata e per il rientro notturno.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 14 ospiti a bordo restano dodici posti liberi: comodità piena per un viaggio lungo, con i sedili "
        "reclinabili utili anche per riposare durante il rientro notturno."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Dom 25 ott",
         "<b>Via della Stazione, 76, Pescia → Mantova, Discoteca Mascara (Viale della Favorita, 17).</b> "
         "Partenza alle 15:00 circa, circa 240 km, arrivo verso le 18:15. Mezzo e conducente restano sul posto a "
         "vostra disposizione per tutta la serata; ripartenza verso mezzanotte, con arrivo a Pescia verso le "
         "03:15, nella notte tra il 25 e il 26 ottobre.",
         "circa 15:00 – 03:15"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Dom 25 ott — trasferimento Pescia → Mantova → Pescia, mezzo e conducente a disposizione dalle 15:00 a "
         "fine servizio (~480 km)", "€ 1.750,00", "+ IVA 10%"),
        ("Supplemento rientro dopo le 02:00 (arrivo a Pescia previsto verso le 03:15)", "€ 250,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.000,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.200,00.",
    perhead="Sono circa € 157,00 a persona.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, assicurazione completa. L'attesa a Mantova, dalle "
        "18:15 a mezzanotte circa, è già compresa nel prezzo. Il conducente rientra in giornata: non è previsto "
        "alcun pernottamento."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre gli orari concordati, € 50,00 all'ora per mezzo: se il rientro dalla discoteca slitta oltre "
        "mezzanotte, l'attesa aggiuntiva si conteggia da lì. Soste per cena o altre tappe non comprese nel "
        "percorso indicato, quotate su richiesta. L'eventuale ingresso del mezzo in una zona a traffico limitato "
        "del centro di Mantova, se necessario, che comporterebbe un permesso a parte."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 660,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.540,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Indirizzo di rientro.</b> Il rientro è quotato fino allo stesso indirizzo di partenza, via della "
         "Stazione 76 a Pescia. Se il gruppo deve essere lasciato in punti diversi, anche nello stesso comune, "
         "comunicatecelo: il prezzo non cambia, ma ci aiuta a organizzare bene l'ultima parte della serata."),
        ("<b>Il punto di sosta alla discoteca.</b> Vi chiediamo di farvi confermare dalla Discoteca Mascara il "
         "punto esatto dove il mezzo può fermarsi per far scendere il gruppo e dove può sostare durante le ore di "
         "attesa: è un dettaglio meglio chiarirlo prima della serata, non sul posto."),
        ("<b>Il rientro dopo le 02:00.</b> Con partenza da Mantova verso mezzanotte, l'arrivo a Pescia è previsto "
         "intorno alle 03:15: il preventivo include già il supplemento corrispondente. Se il gruppo dovesse "
         "trattenersi oltre l'orario indicato, si aggiunge l'attesa di € 50,00 all'ora per mezzo."),
        ("<b>Le ore di attesa a Mantova.</b> Le quasi sei ore fra l'arrivo e la ripartenza non sono tempo perso: "
         "servono anche al conducente per riposare prima del viaggio di rientro, lungo quanto quello di andata. "
         "Per questo il servizio resta su una sola giornata, senza bisogno di alcun pernottamento."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, un recapito telefonico o WhatsApp "
         "della persona che viaggia con il gruppo e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra disposizione "
         "per tutta la validità del preventivo; la prenotazione diventa definitiva alla ricezione dell'acconto. "
         "La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene trattenuto "
         "l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. "
         "Mancando oggi 39 giorni al servizio, questa prenotazione ricade nella fascia da 60 a 30 giorni, e dal "
         "25 settembre passerà in quella da 30 a 10. Preventivo valido fino al 30 settembre 2026."),
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
    subtitle="Evening transfer Pescia → Mantua, Discoteca Mascara  ·  Sunday 25 October 2026",
    meta="Prepared for %s  ·  16 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of 14, with the same driver for the whole evening and the night return.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 14 guests on board twelve seats stay free — full comfort for a long trip, with the reclining seats "
        "useful for resting on the way back."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sun 25 Oct",
         "<b>Via della Stazione, 76, Pescia → Mantua, Discoteca Mascara (Viale della Favorita, 17).</b> "
         "Departure around 15:00, about 240 km, arriving around 18:15. Vehicle and driver stay on site at your "
         "disposal for the whole evening; departure around midnight, arriving back in Pescia around 03:15, in "
         "the night between 25 and 26 October.",
         "approx. 15:00 – 03:15"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sun 25 Oct — transfer Pescia → Mantua → Pescia, vehicle and driver at your disposal from 15:00 to end "
         "of service (~480 km)", "€ 1,750.00", "+ VAT 10%"),
        ("Late-return surcharge after 02:00 (arrival in Pescia expected around 03:15)", "€ 250.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,000.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,200.00.",
    perhead="That is about € 157.00 per person.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, full insurance. The wait in Mantua, from 18:15 to around "
        "midnight, is already included in the price. The driver returns the same day: no overnight stay is "
        "planned."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the agreed times, € 50.00 per hour per vehicle: if the return from the club runs past "
        "midnight, the extra wait is counted from there. Stops for dinner or other stops outside the route shown "
        "here, quoted on request. Any entry of the vehicle into a restricted traffic zone in central Mantua, if "
        "needed, which would require a separate permit."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 660.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,540.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Return address.</b> The return is quoted to the same address as departure, Via della Stazione 76 in "
         "Pescia. If the group needs to be dropped at different points, even within the same town, let us know: "
         "the price does not change, but it helps us plan the last part of the evening."),
        ("<b>The stop at the club.</b> Please have Discoteca Mascara confirm the exact point where the vehicle "
         "can stop to drop off the group and where it can wait during the hours in between: better settled "
         "before the evening than on the spot."),
        ("<b>The return after 02:00.</b> With departure from Mantua around midnight, arrival in Pescia is "
         "expected around 03:15: the quotation already includes the corresponding surcharge. Should the group "
         "stay on past the time shown here, waiting is added at € 50.00 per hour per vehicle."),
        ("<b>The hours of waiting in Mantua.</b> The nearly six hours between arrival and departure are not dead "
         "time: they also let the driver rest before the return drive, which is as long as the outbound one. "
         "That is why the job stays within a single day, with no overnight stay needed."),
        ("<b>To confirm we need</b> the final passenger count, a mobile or WhatsApp contact for the person "
         "travelling with the group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you for the "
         "whole validity of this quotation; the booking becomes firm on receipt of the deposit. Cancellation is "
         "free of charge more than 60 days before the service; from 60 to 30 days the deposit is retained; from "
         "30 to 10 days 50% of the price is charged; in the last 10 days, 100%. With 39 days to the service "
         "today, this booking falls in the 60-to-30-day band, and from 25 September it moves into the "
         "30-to-10 band. Quotation valid until 30 September 2026."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    cliente = a.cliente or ("il gruppo di 14 persone" if a.lang == "it" else "the group of 14")
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Pescia_Mantova_25_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, cliente, name))

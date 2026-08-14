#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento privato Aeroporto di Pisa (PSA) ->
Castello di San Ruffino, Lari (PI), venerdi 4 settembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_transfer_pisa_lari.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_transfer_pisa_lari.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0904-MS"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferimento privato · Aeroporto di Pisa (PSA) → Castello di San Ruffino, Lari (PI) · venerdì 4 settembre 2026",
    meta="Preparato per %s  ·  14 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un unico minibus per il vostro gruppo di 20 persone, dall'aeroporto di Pisa fino al Castello di San Ruffino.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 20 ospiti a bordo restano sei posti liberi, comodi anche per i bagagli. I 7,64 metri del "
        "Beluga raggiungono le strade di campagna e i vialetti stretti tipici delle location come il "
        "Castello di San Ruffino, dove un pullman gran turismo fatica ad arrivare: un unico mezzo per "
        "tutto il gruppo, senza smistare i passeggeri su più veicoli."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Ven 4 set",
         "<b>Aeroporto di Pisa (PSA), arrivi → Castello di San Ruffino, Lari (PI).</b> "
         "Il conducente vi attende in sala arrivi con il cartello GiroMunna dall'orario di atterraggio "
         "previsto (13:45); si parte non appena il gruppo e i bagagli sono pronti. Circa 30 km, "
         "40 minuti di percorrenza stradale.",
         "circa 13:45 – 15:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Ven 4 set — Aeroporto di Pisa (PSA) → Castello di San Ruffino, Lari", "€ 480,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 480,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 528,00.",
    perhead="Sono circa € 26,40 a persona.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggio bus dell'aeroporto di Pisa, "
        "assicurazione completa e movimentazione dei bagagli. Monitoriamo il volo e l'autista attende "
        "senza costi aggiuntivi fino a 90 minuti dall'orario di atterraggio effettivo, per quanto il "
        "volo ritardi."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre i 90 minuti gratuiti, € 50,00 all'ora per mezzo. Soste aggiuntive o deviazioni "
        "dal percorso diretto, quotate su richiesta. Il viaggio di ritorno: questo preventivo copre solo "
        "il trasferimento di andata. Mance e spese personali dei passeggeri."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 158,40", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 369,60", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Numero e orario del volo.</b> Ci servono numero di volo e compagnia per monitorare "
         "l'orario reale di atterraggio. Le 13:45 indicate le prendiamo come stima: il conducente vi "
         "aspetta in sala arrivi fino a 90 minuti dopo l'atterraggio effettivo, senza alcun costo "
         "aggiuntivo, per quanto il volo ritardi."),
        ("<b>Bagagli.</b> Con 20 passeggeri e fino a 40 colli tra valigie e bagagli a mano, il vano del "
         "Beluga li ospita comodamente. Segnalateci comunque in anticipo eventuali colli fuori misura o "
         "voluminosi, così organizziamo il carico."),
        ("<b>Un mezzo solo, non due minivan.</b> Nella richiesta chiedevate in alternativa due minivan "
         "da 8-9 posti: non ne avete bisogno. Il nostro Beluga da 26 posti porta comodamente tutto il "
         "gruppo e i bagagli in un unico mezzo, senza smistamenti né il rischio di separare i "
         "passeggeri su due veicoli diversi."),
        ("<b>Accesso al Castello di San Ruffino.</b> Trattandosi di una location in campagna, l'ultimo "
         "tratto di strada potrebbe essere stretto. I 7,64 metri del Beluga arrivano dove un pullman "
         "gran turismo non passa, ma vi chiediamo di farvi confermare dalla location il punto esatto di "
         "discesa e lo spazio di manovra per un mezzo di questa lunghezza."),
        ("<b>Solo andata.</b> Questo preventivo copre esclusivamente il trasferimento di andata da Pisa "
         "a Lari. Se vi serve anche un rientro, verso l'aeroporto o un'altra destinazione, fatecelo "
         "sapere e vi prepariamo il preventivo per il servizio completo."),
        ("<b>Per confermare ci servono</b> numero e orario del volo, la conferma definitiva dei 20 "
         "passeggeri, un recapito telefonico o WhatsApp della persona che viaggia con il gruppo e i "
         "vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla "
         "ricezione dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 "
         "a 30 giorni viene trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; "
         "negli ultimi 10 giorni il 100%. Mancando oggi 21 giorni al servizio, questa prenotazione "
         "ricade già nella fascia da 30 a 10 giorni, e dal 25 agosto passerà in quella degli ultimi 10 "
         "giorni. Preventivo valido fino al 25 agosto 2026."),
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
    subtitle="Private transfer · Pisa Airport (PSA) → Castello di San Ruffino, Lari (PI) · Friday, 4 September 2026",
    meta="Prepared for %s  ·  14 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of 20, from Pisa Airport to Castello di San Ruffino.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 20 guests on board six seats stay free, useful room for luggage too. At 7.64 m the "
        "Beluga reaches the country lanes and narrow driveways typical of venues like Castello di San "
        "Ruffino, where a full-size coach struggles to get through: a single vehicle for the whole "
        "group, with nobody split across two vehicles."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Fri 4 Sep",
         "<b>Pisa Airport (PSA), arrivals → Castello di San Ruffino, Lari (PI).</b> "
         "The driver waits for you in the arrivals hall with the GiroMunna sign from the scheduled "
         "landing time (13:45); departure as soon as the group and luggage are ready. About 30 km, "
         "40 minutes' driving time.",
         "approx. 13:45 – 15:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Fri 4 Sep — Pisa Airport (PSA) → Castello di San Ruffino, Lari", "€ 480.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 480.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 528.00.",
    perhead="That is about € 26.40 per person.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, Pisa Airport bus parking, full insurance and "
        "luggage handling. We monitor the flight and the driver waits at no extra cost for up to 90 "
        "minutes from the actual landing time, however late the flight arrives."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the 90 free minutes, € 50.00 per hour per vehicle. Additional stops or "
        "detours from the direct route, quoted on request. The return journey: this quotation covers "
        "the outbound transfer only. Gratuities and passengers' personal expenses."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 158.40", "VAT included"),
        ("Balance, within 5 days of the service", "€ 369.60", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Flight number and time.</b> We need the flight number and airline to monitor the actual "
         "landing time. We have taken the 13:45 you gave us as an estimate: the driver waits in the "
         "arrivals hall for up to 90 minutes after the actual landing time, at no extra cost, however "
         "late the flight arrives."),
        ("<b>Luggage.</b> With 20 passengers and up to 40 pieces between suitcases and carry-ons, the "
         "Beluga's hold takes them comfortably. Please still tell us in advance about any oversized or "
         "bulky items, so we can plan the loading."),
        ("<b>One vehicle, not two minivans.</b> Your request asked, as an alternative, about two 8-9 "
         "seater minivans: you do not need them. Our 26-seat Beluga carries the whole group and all "
         "the luggage comfortably in a single vehicle, with no splitting the group across two "
         "vehicles."),
        ("<b>Access at Castello di San Ruffino.</b> As a countryside venue, the final stretch of road "
         "may be narrow. Our 7.64 m Beluga reaches places a full-size coach cannot, but please still "
         "have the venue confirm the exact drop-off point and manoeuvring space for a vehicle of this "
         "length."),
        ("<b>Outbound only.</b> This quotation covers the outbound transfer from Pisa to Lari only. If "
         "you also need a return journey, to the airport or elsewhere, let us know and we will prepare "
         "a quotation for the complete service."),
        ("<b>To confirm we need</b> the flight number and time, the final confirmed count of 20 "
         "passengers, a mobile or WhatsApp contact for the person travelling with the group, and your "
         "invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you "
         "for the whole validity of this quotation; the booking becomes firm on receipt of the "
         "deposit. Cancellation is free of charge more than 60 days before the service; from 60 to 30 "
         "days the deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 "
         "days, 100%. With 21 days to the service today, this booking already falls in the 30-to-10-day "
         "band, and from 25 August it moves into the last-10-days band. Quotation valid until 25 August "
         "2026."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Michelle Synnott")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Transfer_Pisa_Lari_4_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

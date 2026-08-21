#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la giornata sul Monte Amiata del 22 agosto 2026,
per il gruppo al Grand Hotel Impero di Castel del Piano (GR).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_monte_amiata.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_monte_amiata.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0822-GI"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Giornata sul Monte Amiata  ·  Castel del Piano (GR)  ·  sabato 22 agosto 2026",
    meta="Preparato per %s  ·  21 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="I mezzi",
    mezzo_intro=(
        "Due minibus con conducente a vostra disposizione per l'intera giornata di sabato 22 agosto, "
        "a Castel del Piano e sul Monte Amiata."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli.<br/>"
        "<b>Mercedes-Benz Tourengo</b> — 28 posti passeggeri più l'autista, 7,86 m."
    ),
    mezzo_close=(
        "Insieme, i due mezzi portano fino a 54 passeggeri. Con i suoi 7,64 metri il Beluga arriva ai "
        "piazzali dei borghi del monte, dove un autobus gran turismo non passa. "
        "Ci serve il numero esatto dei passeggeri per confermare la ripartizione fra i due mezzi."
    ),
    h_servizio="Il servizio",
    svc_head=["Quando", "Programma"],
    svc=[
        ("Sabato 22 agosto",
         "<b>Due minibus a vostra disposizione per l'intera giornata</b>, per l'escursione sul Monte "
         "Amiata. Orario di partenza e tappe si concordano insieme a voi più vicino alla data."),
    ],
    svc_foot=(
        "L'orario di partenza e le tappe sul monte si confermano insieme a voi."
    ),
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 22 ago — Beluga: mezzo e conducente a disposizione per la giornata sul Monte Amiata",
         "€ 900,00", "+ IVA 10%"),
        ("Sab 22 ago — Tourengo: mezzo e conducente a disposizione per la giornata sul Monte Amiata",
         "€ 900,00", "+ IVA 10%"),
        ("Vitto dei due conducenti", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.800,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.980,00.",
    perhead=(
        "Il prezzo è per mezzo e non a persona."
    ),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi autostradali, parcheggi e assicurazione "
        "completa. Sull'itinerario proposto sul Monte Amiata non risultano oneri di accesso o permessi a "
        "pagamento; se una tappa che ci chiederete dovesse richiedere un parcheggio bus a pagamento, ve lo "
        "segnaliamo prima e non dopo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il vitto del conducente, che resta a vostro carico. Pranzi, ingressi, guide e mance. "
        "Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. Soste aggiuntive o modifiche di percorso "
        "fuori dall'Amiata, quotate su richiesta. Rientro dopo le 02:00, € 250,00. L'eventuale pernottamento del "
        "conducente a Castel del Piano, se il programma si prolunga la sera: anche quello è a vostro carico."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Alla conferma — nessun acconto, il servizio è a meno di 24 ore", "€ 0,00", ""),
        ("Saldo unico, entro il 26 agosto 2026", "€ 1.980,00", "IVA inclusa"),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Prima di tutto: la conferma a voce.</b> Girolamo vi richiama a breve per confermarvi la "
         "disponibilità dei due mezzi per sabato: fino a quella telefonata questo preventivo è un prezzo, "
         "non una prenotazione."),
        ("<b>Quanti siete.</b> Il Beluga porta 26 passeggeri più l'autista, il Tourengo 28 più l'autista: "
         "insieme, fino a 54. Mandateci il numero esatto per confermare la ripartizione fra i due mezzi."),
        ("<b>Le strade del monte.</b> Le strade dell'Amiata sono spesso tornanti, e i centri storici dei borghi "
         "sono in diversi punti stretti: normalmente si scende ai piazzali all'ingresso e si prosegue a piedi. "
         "Il Beluga, 7,64 m, ci arriva senza problemi; il Tourengo, 7,86 m, dovrebbe passare comunque, ma sui "
         "tratti più stretti verifichiamo il punto di discesa prima di partire, con il Beluga che apre la "
         "strada. Se avete in mente una tappa precisa, diteci quale."),
        ("<b>Il vitto dei conducenti.</b> Il pranzo di sabato resta sempre a carico del cliente per entrambi "
         "gli autisti: non lo mettiamo a preventivo e non lo organizziamo noi. Se voleste tenere i mezzi anche "
         "la sera — una cena sul monte, un rientro dopo le 20:00 — i conducenti dovrebbero pernottare a Castel "
         "del Piano, anche quello a vostro carico: fatecelo sapere per tempo. La soluzione più comoda, e quella "
         "che scelgono quasi tutti i nostri clienti, è farli mangiare nella stessa struttura del gruppo."),
        ("<b>Per confermare ci servono</b> il numero dei passeggeri e come sono ripartiti fra i due mezzi, "
         "l'ora di partenza che preferite per il monte, un recapito WhatsApp di chi viaggia con il gruppo e i "
         "vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> La cancellazione è gratuita oltre 60 giorni prima del servizio; "
         "da 60 a 30 giorni viene trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; "
         "negli ultimi 10 giorni il 100%. Mancando meno di ventiquattr'ore al servizio, questa prenotazione "
         "ricade per intero nell'ultima fascia. Preventivo valido fino alle 20:00 del 21 agosto 2026, "
         "che è il momento oltre il quale i mezzi non fanno più in tempo a organizzarsi per domani."),
    ],
    closing=("Restiamo a disposizione per qualsiasi chiarimento e vi confermiamo l'orario di partenza appena "
             "possibile.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="A day on Monte Amiata  ·  Castel del Piano (GR)  ·  Saturday 22 August 2026",
    meta="Prepared for %s  ·  21 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicles",
    mezzo_intro=(
        "Two minibuses with driver at your disposal for the whole day of Saturday 22 August, "
        "in Castel del Piano and on Monte Amiata."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold.<br/>"
        "<b>Mercedes-Benz Tourengo</b> — 28 passenger seats plus driver, 7.86 m."
    ),
    mezzo_close=(
        "Together, the two vehicles carry up to 54 passengers. At 7.64 m the Beluga reaches the parking "
        "areas of the mountain villages, where a full-size coach cannot go. "
        "We need the exact number of passengers to confirm how the group splits between the two vehicles."
    ),
    h_servizio="The service",
    svc_head=["When", "Programme"],
    svc=[
        ("Saturday 22 August",
         "<b>Two minibuses at your disposal for the whole day</b>, for the excursion on Monte Amiata. "
         "Departure time and stops will be agreed with you closer to the date."),
    ],
    svc_foot=(
        "The departure time and the stops on the mountain will be confirmed with you."
    ),
    h_prezzo="The price",
    price_rows=[
        ("Sat 22 Aug — Beluga: vehicle and driver at your disposal for the day on Monte Amiata",
         "€ 900.00", "+ VAT 10%"),
        ("Sat 22 Aug — Tourengo: vehicle and driver at your disposal for the day on Monte Amiata",
         "€ 900.00", "+ VAT 10%"),
        ("Both drivers' meals", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,800.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,980.00.",
    perhead=(
        "The price is per vehicle, not per person."
    ),
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, fuel, motorway tolls, parking and full insurance. The proposed "
        "Monte Amiata itinerary carries no known access charges or paid permits; should a stop you ask for "
        "require a paid coach car park, we will tell you beforehand rather than afterwards."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meals, which remain at your charge. Lunches, entrance fees, guides and gratuities. "
        "Waiting beyond the times set out here, € 50.00 per hour per vehicle. Additional stops or route changes "
        "outside the Amiata, quoted on request. Return after 02:00, € 250.00. Any overnight stay for the driver "
        "in Castel del Piano, should the programme run into the evening: that too is at your charge."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("On confirmation — no deposit, the service is less than 24 hours away", "€ 0.00", ""),
        ("Single payment, by 26 August 2026", "€ 1,980.00", "VAT included"),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>First of all: confirmation by phone.</b> Girolamo will call you shortly to confirm both "
         "vehicles are available on Saturday: until that call, this quotation is a price, not a booking."),
        ("<b>How many of you there are.</b> The Beluga carries 26 passengers plus the driver, the Tourengo 28 "
         "plus the driver: together, up to 54. Send us the exact number to confirm how the group splits "
         "between the two vehicles."),
        ("<b>The mountain roads.</b> The Amiata's roads are often one hairpin after another, and several of "
         "the old village centres are narrow: usually you get off at the car park by the entrance and walk in. "
         "The Beluga, at 7.64 m, gets there without trouble; the Tourengo, at 7.86 m, should manage too, but "
         "on the tightest stretches we will check the drop-off point before we set off, with the Beluga "
         "leading the way. If you have a particular stop in mind, tell us which."),
        ("<b>The drivers' meals.</b> Saturday lunch always stays at the client's charge for both drivers: we "
         "do not put it in the quotation and we do not arrange it. Should you want to keep the vehicles for "
         "the evening too — dinner on the mountain, a return after 20:00 — the drivers would need to stay "
         "overnight in Castel del Piano, also at your charge: let us know in good time. The easiest "
         "arrangement, and the one almost all our clients choose, is to have them eat at the same property as "
         "the group."),
        ("<b>To confirm we need</b> the number of passengers and how they split between the two vehicles, "
         "your preferred departure time for the mountain, a WhatsApp contact for the person travelling with "
         "the group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> Cancellation is free of charge more than 60 days before the "
         "service; from 60 to 30 days the deposit is retained; from 30 to 10 days 50% of the price is charged; in "
         "the last 10 days, 100%. With less than twenty-four hours to the service, this booking falls entirely "
         "within the last band. Quotation valid until 20:00 on 21 August 2026, the point beyond which the "
         "vehicles can no longer be organised in time for tomorrow."),
    ],
    closing=("We remain at your disposal for any clarification and will confirm the departure time as soon "
             "as possible.<br/><br/>"
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
        "foot": ParagraphStyle("foot", alignment=TA_JUSTIFY, spaceBefore=6, spaceAfter=2,
                               fontName="Helvetica", fontSize=8.2,
                               textColor=MUTED, leading=11.4),
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
    cols = [26 * mm, usable - 26 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for orario, desc in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % orario, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
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
    F.append(Paragraph(L["svc_foot"], S["foot"]))

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Grand Hotel Impero, Castel del Piano")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Monte_Amiata_22_agosto_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

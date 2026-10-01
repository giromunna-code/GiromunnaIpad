#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il matrimonio alla Tenuta di Artimino, 11 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_matrimonio_artimino.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_matrimonio_artimino.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1011-AW"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Navetta ospiti per il matrimonio alla Tenuta di Artimino  ·  domenica 11 ottobre 2026",
    meta="Preparato per %s  ·  1 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="I mezzi",
    mezzo_intro=(
        "<b>Il servizio riguarda soltanto due gruppi: i 18 ospiti del Borgo di Villa Castelletti e i 26 "
        "di Villa la Malva.</b> Non sono compresi i 7 ospiti dell'Airbnb di Lastra a Signa né i 3 di "
        "Villa le Farnette a Comeano, per i quali non abbiamo disponibilità.<br/><br/>"
        "Due minibus, uno per ciascuna struttura, ognuno con il proprio conducente: gli ospiti salgono "
        "davanti alla propria villa e scendono alla Tenuta senza cambi e senza giri intermedi."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Per i 26 ospiti di "
        "Villa la Malva.<br/>"
        "<b>Mercedes-Benz Tourengo</b> — 28 posti passeggeri più l'autista, 7,86 m. Per i 18 ospiti del "
        "Borgo di Villa Castelletti.<br/>"
        "Entrambi con aria condizionata, sedili ultra comfort reclinabili, frigo bar e impianto audio di bordo."
    ),
    mezzo_close=(
        "Tutti e due i mezzi stanno sotto gli 8 metri: salgono sulle strade collinari di Carmignano e "
        "arrivano fino all'ingresso della Tenuta di Artimino e delle ville, dove un autobus gran turismo "
        "dovrebbe fermarsi più in basso e lasciare gli ospiti a piedi, in abito da cerimonia."
    ),
    h_servizio="Il servizio",
    svc_head=["Dom 11 ott", "Percorso", "Partenza"],
    svc=[
        ("Andata",
         "<b>Borgo di Villa Castelletti (Signa) → Tenuta di Artimino.</b> Tourengo, 18 ospiti. "
         "Circa 15 km, arrivo verso le 14:55.",
         "14:30"),
        ("Andata",
         "<b>Villa la Malva (Carmignano) → Tenuta di Artimino.</b> Beluga, 26 ospiti. "
         "Circa 6 km, arrivo verso le 15:00.",
         "14:45"),
        ("Ritorno",
         "<b>Tenuta di Artimino → Borgo di Villa Castelletti.</b> Tourengo, 18 ospiti. "
         "Arrivo verso le 03:25.",
         "03:00"),
        ("Ritorno",
         "<b>Tenuta di Artimino → Villa la Malva.</b> Beluga, 26 ospiti. "
         "Arrivo verso le 03:15.",
         "03:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Beluga — Villa la Malva – Tenuta di Artimino, andata e ritorno alle 03:00", "€ 1.100,00", "+ IVA 10%"),
        ("Tourengo — Borgo di Villa Castelletti – Tenuta di Artimino, andata e ritorno alle 03:00", "€ 1.100,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.200,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.420,00.",
    perhead="Sono € 55,00 a ospite per andata e ritorno, su 44 ospiti.",
    h_incluso="Incluso.",
    incluso=(
        "Due mezzi con i rispettivi conducenti, carburante, pedaggi, parcheggi e assicurazione completa. "
        "Nessun onere di accesso: né la Tenuta né le due ville si trovano in zona a traffico limitato. "
        "Fra l'andata e il ritorno i mezzi rientrano alla base: il conducente non resta in attesa alla Tenuta "
        "e non ci sono pasti o pernottamenti a vostro carico."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. Corse aggiuntive, per esempio un "
        "rientro anticipato per una parte degli ospiti, quotate su richiesta. Il trasporto degli ospiti "
        "alloggiati a Lastra a Signa e a Villa le Farnette, per cui vedete le note."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 726,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.694,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Gli ospiti di Lastra a Signa e di Villa le Farnette.</b> Per i 7 ospiti dell'Airbnb di Via "
         "Livornese e i 3 di Villa le Farnette a Comeano non abbiamo un mezzo disponibile in quella fascia "
         "oraria: il preventivo copre i 44 ospiti delle altre due strutture. Per questi 10 ospiti vi "
         "consigliamo di organizzare per tempo un servizio a parte, perché a una settimana dal matrimonio "
         "la disponibilità in zona è già scarsa."),
        ("<b>Il Beluga è pieno.</b> I 26 ospiti di Villa la Malva occupano tutti i 26 posti del mezzo, "
         "senza un posto libero. Ogni bambino conta come un passeggero, anche se piccolo. Se il numero "
         "dovesse crescere anche di una sola persona, avvisateci subito: non è un problema che si risolve "
         "la sera stessa. Sul Tourengo, con 18 ospiti, restano invece 10 posti liberi."),
        ("<b>Un solo ritorno alle 03:00.</b> A un matrimonio non tutti restano fino alla fine: anziani, "
         "famiglie con bambini e chi ha un volo il giorno dopo di solito vogliono rientrare prima. "
         "Se pensate che serva, possiamo aggiungere una corsa di ritorno intorno a mezzanotte e mezza: "
         "ditecelo prima della conferma e ve la quotiamo."),
        ("<b>Il rientro notturno è compreso.</b> Di norma un rientro dopo le 02:00 comporta un "
         "supplemento di € 250,00 per mezzo: per questo servizio lo abbiamo già compreso nel prezzo, "
         "con la partenza dalla Tenuta alle 03:00."),
        ("<b>Ritardi a fine serata.</b> I mezzi sono pronti alla Tenuta dalle 02:45. Se la festa si "
         "prolunga, l'attesa oltre le 03:00 si conteggia a € 50,00 all'ora per mezzo. Vi chiediamo di "
         "indicarci chi, fra voi coordinatrici o gli sposi, può dare al conducente il via alla partenza."),
        ("<b>Punto di salita e di discesa.</b> Alla Tenuta di Artimino vi chiediamo di confermarci "
         "l'ingresso da usare, il Borgo o la Villa Medicea, e dove far scendere gli ospiti. Per le due ville "
         "ci basta l'indirizzo esatto e il punto di raccolta davanti al cancello."),
        ("<b>Per confermare ci servono</b> il numero definitivo degli ospiti per ciascuna villa, il nome e il "
         "cellulare di un referente per ogni gruppo, e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> I due mezzi sono al momento liberi e li teniamo a vostra "
         "disposizione fino al 3 ottobre 2026, data di validità del preventivo; la prenotazione diventa "
         "definitiva alla ricezione dell'acconto. Mancando 10 giorni al servizio, una volta confermata la "
         "prenotazione la cancellazione comporta l'addebito dell'intero importo."),
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
    subtitle="Guest shuttle for the wedding at Tenuta di Artimino  ·  Sunday 11 October 2026",
    meta="Prepared for %s  ·  1 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicles",
    mezzo_intro=(
        "<b>The service covers only two groups: the 18 guests at Borgo di Villa Castelletti and the 26 at "
        "Villa la Malva.</b> It does not include the 7 guests at the Airbnb in Lastra a Signa or the 3 at "
        "Villa le Farnette in Comeano, for whom we have no availability.<br/><br/>"
        "Two minibuses, one for each property, each with its own driver: guests board in front of their own "
        "villa and step off at the Tenuta, with no changes and no detours."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. For the 26 guests at "
        "Villa la Malva.<br/>"
        "<b>Mercedes-Benz Tourengo</b> — 28 passenger seats plus driver, 7.86 m. For the 18 guests at "
        "Borgo di Villa Castelletti.<br/>"
        "Both with air conditioning, reclining ultra-comfort seats, fridge bar and on-board audio system."
    ),
    mezzo_close=(
        "Both vehicles are under 8 metres: they climb the Carmignano hill roads and drive right up to the "
        "entrance of Tenuta di Artimino and of the villas, where a full-size coach would have to stop further "
        "down and leave guests to walk in their wedding clothes."
    ),
    h_servizio="The service",
    svc_head=["Sun 11 Oct", "Route", "Departure"],
    svc=[
        ("Outbound",
         "<b>Borgo di Villa Castelletti (Signa) → Tenuta di Artimino.</b> Tourengo, 18 guests. "
         "About 15 km, arriving around 14:55.",
         "14:30"),
        ("Outbound",
         "<b>Villa la Malva (Carmignano) → Tenuta di Artimino.</b> Beluga, 26 guests. "
         "About 6 km, arriving around 15:00.",
         "14:45"),
        ("Return",
         "<b>Tenuta di Artimino → Borgo di Villa Castelletti.</b> Tourengo, 18 guests. "
         "Arriving around 03:25.",
         "03:00"),
        ("Return",
         "<b>Tenuta di Artimino → Villa la Malva.</b> Beluga, 26 guests. "
         "Arriving around 03:15.",
         "03:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Beluga — Villa la Malva – Tenuta di Artimino, outbound and return at 03:00", "€ 1,100.00", "+ VAT 10%"),
        ("Tourengo — Borgo di Villa Castelletti – Tenuta di Artimino, outbound and return at 03:00", "€ 1,100.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,200.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,420.00.",
    perhead="That is € 55.00 per guest for the round trip, across 44 guests.",
    h_incluso="Included.",
    incluso=(
        "Two vehicles with their drivers, fuel, tolls, parking and full insurance. No access charges apply: "
        "neither the Tenuta nor the two villas lie inside a restricted traffic zone. Between the outbound and "
        "the return runs the vehicles go back to base: the drivers do not wait at the Tenuta, and there are no "
        "meals or overnight stays at your charge."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the times set out here, € 50.00 per hour per vehicle. Additional runs, such as an "
        "earlier return for some of the guests, quoted on request. Transport for the guests staying in Lastra "
        "a Signa and at Villa le Farnette — see the notes."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 726.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,694.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The guests in Lastra a Signa and at Villa le Farnette.</b> For the 7 guests at the Airbnb on Via "
         "Livornese and the 3 at Villa le Farnette in Comeano we have no vehicle available in that time slot: "
         "this quotation covers the 44 guests at the other two properties. For these 10 guests we suggest "
         "arranging a separate service soon, as with the wedding a week away availability in the area is "
         "already tight."),
        ("<b>The Beluga is full.</b> The 26 guests at Villa la Malva take all 26 seats, with none to spare. "
         "Every child counts as a passenger, however small. If the number grows by even one person, please "
         "tell us straight away: it is not something that can be solved on the night. On the Tourengo, with "
         "18 guests, 10 seats remain free."),
        ("<b>A single return at 03:00.</b> At a wedding not everyone stays to the end: older guests, families "
         "with children and anyone flying the next day usually want to leave earlier. If you think it is "
         "needed, we can add a return run around half past midnight: let us know before confirming and we "
         "will quote it."),
        ("<b>The late-night return is included.</b> A return after 02:00 normally carries a supplement of "
         "€ 250.00 per vehicle: for this service it is already included in the price, with departure from the "
         "Tenuta at 03:00."),
        ("<b>Delays at the end of the evening.</b> The vehicles are ready at the Tenuta from 02:45. If the party "
         "runs on, waiting beyond 03:00 is charged at € 50.00 per hour per vehicle. Please tell us who — one of "
         "you coordinators or the couple — can give the drivers the signal to leave."),
        ("<b>Pick-up and drop-off points.</b> At Tenuta di Artimino please confirm which entrance to use, the "
         "Borgo or the Medici Villa, and where guests should step off. For the two villas we only need the "
         "exact address and the meeting point at the gate."),
        ("<b>To confirm we need</b> the final number of guests for each villa, the name and mobile number of a "
         "contact person for each group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> Both vehicles are currently free and we hold them for you until "
         "3 October 2026, the validity date of this quotation; the booking becomes firm on receipt of the "
         "deposit. With 10 days to the service, once the booking is confirmed a cancellation is charged at the "
         "full amount."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Aries Weddings Tuscany")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Matrimonio_Artimino_11_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

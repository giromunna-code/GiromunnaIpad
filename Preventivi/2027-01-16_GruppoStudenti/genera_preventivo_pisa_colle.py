#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per i trasferimenti dall'aeroporto di Pisa a Colle di Val d'Elsa
(16 gennaio 2027) e ritorno (23 gennaio 2027).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_pisa_colle.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_pisa_colle.py --lingua en --cliente "Client Name"
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


RIF = "GM-2027-0116-GS"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferimenti dall'aeroporto di Pisa a Colle di Val d'Elsa e ritorno  ·  16 e 23 gennaio 2027",
    meta="Preparato per %s  ·  30 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo di 17-22 persone (studenti e insegnanti), con conducente professionista.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Anche con il gruppo al completo (20 studenti e 2 insegnanti, 22 persone) restano quattro posti liberi. "
        "I 7,64 metri del mezzo arrivano dove un autobus gran turismo non entra, e questo conta a Colle di Val d'Elsa, "
        "dove le strade intorno al centro storico sono strette."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Sab 16 gen 2027",
         "<b>Aeroporto di Pisa (PSA) → Colle di Val d'Elsa.</b> "
         "L'autista vi accoglie in sala arrivi con il cartello GiroMunna e vi aiuta con i bagagli. Circa 100 km, poco "
         "più di un'ora di viaggio, fino all'indirizzo del vostro alloggio. L'orario di partenza segue quello "
         "di atterraggio del volo, che ci serve conoscere.",
         "da confermare sul volo"),
        ("17-22 gen",
         "<b>Nessun servizio richiesto.</b> Il mezzo rientra alla base e non viene tenuto in stand-by: "
         "questi giorni non comportano alcun addebito.",
         "—"),
        ("Sab 23 gen 2027",
         "<b>Colle di Val d'Elsa → Aeroporto di Pisa (PSA).</b> "
         "Partenza dall'alloggio con il gruppo, circa 100 km fino alle partenze di Pisa. L'orario di partenza "
         "si calcola sul volo, lasciando al gruppo il tempo del check-in.",
         "da confermare sul volo"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 16 gen — aeroporto di Pisa → Colle di Val d'Elsa", "€ 900,00", "+ IVA 10%"),
        ("Sab 23 gen — Colle di Val d'Elsa → aeroporto di Pisa", "€ 900,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente (nessuna notte prevista, vedi Note)",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.800,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.980,00.",
    perhead="Sono circa € 90,00 a persona con 22 partecipanti e circa € 116,00 con 17, per andata e ritorno.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggi (compreso il parcheggio bus "
        "dell'aeroporto di Pisa), assicurazione completa, movimentazione dei bagagli e monitoraggio del volo. "
        "Il 16 gennaio l'autista attende senza costi aggiuntivi fino a 90 minuti dall'orario di atterraggio "
        "effettivo, per quanto il volo arrivi in ritardo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio del conducente, che restano a vostro carico se servono (vedi Note): la prenotazione e il "
        "pagamento li curate voi direttamente. Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. "
        "Rientro dopo le 02:00, € 250,00. Escursioni e spostamenti durante la settimana, quotati su richiesta: "
        "l'ingresso di un bus turistico nel centro di Firenze richiede un permesso a parte (circa € 350) e quello "
        "nel centro di Siena pure (circa € 160)."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 594,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio del 23 gennaio", "€ 1.386,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Bagagli.</b> È il punto da guardare con più attenzione. Il vano del Beluga porta senza problemi una "
         "ventina di valigie normali, ma per una settimana di soggiorno con 17-22 persone il conto si fa stretto se "
         "ognuno ha un trolley grande, più zaino e bagaglio a mano. Mandateci il numero approssimativo di valigie e "
         "segnalateci eventuali colli fuori misura: se servisse più spazio lo organizziamo prima, non al momento "
         "del carico. Zaini e bagagli a mano viaggiano in cabina, sotto i sedili e nelle cappelliere."),
        ("<b>Numero dei passeggeri.</b> Il preventivo vale per un mezzo e copre fino a 26 persone. Il numero che "
         "ci avete indicato, 15-20 studenti e due insegnanti, sta comodamente a bordo: ci serve il numero "
         "definitivo per confermare."),
        ("<b>Il volo in arrivo del 16 gennaio.</b> Ci servono numero del volo e orario di atterraggio. "
         "Se gli studenti e le insegnanti arrivano con voli diversi, diteci gli orari: attendiamo tutti senza "
         "costi fino a 90 minuti dall'atterraggio del primo volo in arrivo, oltre si applicano € 50,00 all'ora."),
        ("<b>Il volo in partenza del 23 gennaio.</b> Da Colle di Val d'Elsa all'aeroporto di Pisa servono poco "
         "più di un'ora di strada e ci vuole un margine per il check-in di un gruppo. Mandateci numero e orario "
         "del volo e fissiamo la partenza su quello. Se il volo parte prima delle 09:00, conviene far "
         "partire il gruppo nella notte: in quel caso il conducente deve dormire a Colle la sera del 22 (vedi sotto)."),
        ("<b>Vitto e alloggio del conducente.</b> Con il volo in arrivo e in partenza a orari normali il conducente "
         "parte e rientra in giornata dalla nostra base, e non serve alcuna notte. Se il volo del 23 gennaio "
         "parte alla mattina presto, serve una notte a Colle di Val d'Elsa, la sera del 22: in quel caso la "
         "camera con la cena sono a vostro carico e le prenotate e pagate voi direttamente. Molti dei nostri "
         "clienti sistemano il conducente nella stessa struttura del gruppo, che è la soluzione più comoda per tutti."),
        ("<b>Dove può arrivare il mezzo a Colle di Val d'Elsa.</b> Colle Alta, il centro storico, ha accessi limitati. "
         "Mandateci l'indirizzo esatto dell'alloggio: verifichiamo il punto di discesa più vicino "
         "raggiungibile con un minibus da 7,64 m, e vi diciamo se il gruppo dovrà fare un tratto a piedi con i "
         "bagagli. Meglio chiarirlo ora che il giorno stesso."),
        ("<b>Durante la settimana.</b> Non è richiesto alcun servizio e non addebitiamo nulla. Se insegnanti e studenti "
         "volessero organizzare gite di un giorno, per esempio a Siena, San Gimignano, Firenze o Pisa, "
         "il mezzo è a vostra disposizione: quotiamo ogni escursione su richiesta."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, l'indirizzo esatto dell'alloggio "
         "a Colle di Val d'Elsa, gli orari dei due voli, il numero approssimativo di valigie, un recapito "
         "telefonico o WhatsApp della persona che viaggia con il gruppo e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla ricezione "
         "dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio, cioè fino al "
         "17 novembre 2026; da 60 a 30 giorni viene trattenuto l'acconto; da 30 a 10 giorni viene addebitato "
         "il 50% del prezzo; negli ultimi 10 giorni il 100%. Preventivo valido fino al 14 ottobre 2026."),
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
    subtitle="Transfers from Pisa airport to Colle di Val d'Elsa and back  ·  16 and 23 January 2027",
    meta="Prepared for %s  ·  30 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of 17-22 people (students and teachers), with a professional driver.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "Even with the full group on board (20 students and 2 teachers, 22 people) four seats stay free. "
        "At 7.64 m the minibus gets where a full-size coach cannot, which matters in Colle di Val d'Elsa, "
        "where the streets around the old town are narrow."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sat 16 Jan 2027",
         "<b>Pisa Airport (PSA) → Colle di Val d'Elsa.</b> "
         "The driver welcomes you in the arrivals hall with the GiroMunna sign and helps with the luggage. About 100 km, "
         "a little over an hour on the road, to the address of your accommodation. The departure time follows the "
         "landing time of your flight, which we need to know.",
         "to be confirmed on the flight"),
        ("17-22 Jan",
         "<b>No service requested.</b> The vehicle returns to base and is not held on stand-by: "
         "nothing is charged for these days.",
         "—"),
        ("Sat 23 Jan 2027",
         "<b>Colle di Val d'Elsa → Pisa Airport (PSA).</b> "
         "Departure from your accommodation with the group, about 100 km to Pisa departures. The departure time is "
         "calculated on the flight, leaving the group time for check-in.",
         "to be confirmed on the flight"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sat 16 Jan — Pisa airport → Colle di Val d'Elsa", "€ 900.00", "+ VAT 10%"),
        ("Sat 23 Jan — Colle di Val d'Elsa → Pisa airport", "€ 900.00", "+ VAT 10%"),
        ("Driver's board and lodging (no nights foreseen, see Notes)",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,800.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,980.00.",
    perhead="That is about € 90.00 per person with 22 participants and about € 116.00 with 17, round trip.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, parking (including the coach parking at Pisa airport), full "
        "insurance, luggage handling and flight monitoring. On 16 January the driver waits at no extra cost "
        "for up to 90 minutes from the actual landing time, however late the flight arrives."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's board and lodging, which remain at your charge if needed (see Notes): you book and pay for "
        "them directly. Waiting beyond the times set out here, € 50.00 per hour per vehicle. Return after 02:00, "
        "€ 250.00. Excursions and journeys during the week, quoted on request: a tourist coach entering the "
        "centre of Florence requires a separate permit (about € 350), as does the centre of Siena (about € 160)."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 594.00", "VAT included"),
        ("Balance, within 5 days of the 23 January service", "€ 1,386.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Luggage.</b> This is the point worth the closest look. The Beluga's hold takes around twenty normal "
         "suitcases without difficulty, but for a week's stay with 17-22 people the count gets tight if everyone has "
         "a large trolley plus a backpack and hand luggage. Send us the approximate number of suitcases and tell us "
         "about any oversized items: if more space is needed we arrange it beforehand, not at loading time. "
         "Backpacks and hand luggage travel in the cabin, under the seats and in the overhead racks."),
        ("<b>Number of passengers.</b> This quotation is for one vehicle and covers up to 26 people. The figure "
         "you gave us, 15-20 students and two teachers, sits comfortably on board: we need the final "
         "number to confirm."),
        ("<b>The arriving flight on 16 January.</b> We need the flight number and landing time. If students and "
         "teachers arrive on different flights, tell us the times: we wait for everyone at no cost for up to "
         "90 minutes from the landing of the first arriving flight; beyond that € 50.00 per hour applies."),
        ("<b>The departing flight on 23 January.</b> Colle di Val d'Elsa to Pisa airport takes a little over an hour "
         "on the road and a group needs a margin for check-in. Send us the flight number and time and we will set "
         "the departure on that. If the flight leaves before 09:00, the group would need to leave during the night: "
         "in that case the driver has to sleep in Colle on the evening of the 22nd (see below)."),
        ("<b>The driver's board and lodging.</b> With the arriving and departing flights at normal hours the driver "
         "leaves and returns the same day from our base, and no night is needed. If the 23 January flight leaves "
         "early in the morning, one night in Colle di Val d'Elsa is needed, on the evening of the 22nd: in that case the "
         "room and dinner are at your charge and you book and pay for them directly. Many of our clients put the "
         "driver up at the same property as the group, which is the easiest arrangement for everyone."),
        ("<b>Where the vehicle can go in Colle di Val d'Elsa.</b> Colle Alta, the old town, has restricted access. "
         "Send us the exact address of the accommodation: we will check the closest drop-off point a 7.64 m minibus "
         "can reach, and tell you whether the group will have to walk a stretch with their luggage. Far better "
         "settled now than on the day itself."),
        ("<b>During the week.</b> No service is required and nothing is charged. Should teachers and students want to "
         "arrange day trips, for example to Siena, San Gimignano, Florence or Pisa, the vehicle is at your "
         "disposal: we quote each excursion on request."),
        ("<b>To confirm we need</b> the final passenger count, the exact address of the accommodation in Colle di "
         "Val d'Elsa, both flight times, the approximate number of suitcases, a mobile or WhatsApp contact for the "
         "person travelling with the group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you for the whole "
         "validity of this quotation; the booking becomes firm on receipt of the deposit. Cancellation is free of "
         "charge more than 60 days before the service, that is up to 17 November 2026; from 60 to 30 days the "
         "deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. "
         "Quotation valid until 14 October 2026."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Gruppo studenti")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Pisa-Colle_16-23_gennaio_2027_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per l'escursione alle Cinque Terre dell'11 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_cinque_terre.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_cinque_terre.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1011-VT"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Escursione alle Cinque Terre · Nievole (Villa Ginevra) – La Spezia Migliarina  ·  domenica 11 ottobre 2026",
    meta="Preparato per %s  ·  21 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus gran turismo per i vostri 10 passeggeri, con lo stesso conducente per tutta la giornata.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Ci avete chiesto un 20-22 posti: il Beluga ne ha 26, quindi i dieci ospiti viaggiano con tutto lo spazio "
        "che vogliono e il vano bagagli resta libero per zaini, giacche e per quello che si compra durante la "
        "giornata. I 7,64 metri di lunghezza contano sulle strade di Nievole e sul piazzale della stazione di "
        "Migliarina, dove un autobus gran turismo si muove con molta più difficoltà."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Dom 11 ott<br/>andata",
         "<b>Nievole, Villa Ginevra (Monsummano Terme, PT) → La Spezia, stazione di Migliarina.</b> "
         "Il mezzo è sul posto qualche minuto prima delle 8:00, partenza alle 8:00 in punto. "
         "Circa 110 km per l'A11 e l'A12, con arrivo a Migliarina intorno alle 9:40, dove la vostra guida "
         "attende il gruppo.",
         "08:00 – 09:40 circa"),
        ("Dom 11 ott<br/>in giornata",
         "<b>Mezzo e conducente restano alla Spezia per tutta la durata dell'escursione.</b> "
         "Il minibus sosta nell'area autorizzata ai bus turistici e il conducente resta raggiungibile al telefono: "
         "se il gruppo rientra prima del previsto bastano una trentina di minuti di preavviso per averlo "
         "sotto la stazione.",
         "a vostra disposizione"),
        ("Dom 11 ott<br/>ritorno",
         "<b>La Spezia, stazione di Migliarina → Nievole, Villa Ginevra.</b> "
         "Ripartenza alle 18:00, gli stessi 110 km a ritroso, arrivo a Villa Ginevra verso le 19:45.",
         "18:00 – 19:45 circa"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Dom 11 ott — Nievole → La Spezia Migliarina, mezzo a disposizione per la giornata e rientro "
         "(circa 220 km, dalle 8:00 alle 19:45)", "€ 1.250,00", "+ IVA 10%"),
        ("Vitto del conducente durante la sosta alla Spezia — nessun pernottamento",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.250,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.375,00.",
    perhead="Sono € 137,50 a persona per i dieci partecipanti, andata e ritorno compresi.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi autostradali, ticket di accesso e sosta del "
        "bus turistico alla Spezia, assicurazione completa e movimentazione dei bagagli a mano. Non sono dovuti "
        "altri oneri: né Villa Ginevra né la stazione di Migliarina comportano permessi ulteriori. Se il treno del "
        "ritorno ritarda, il conducente attende senza costi aggiuntivi fino a 45 minuti oltre l'orario concordato."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il pasto del conducente durante la sosta alla Spezia, che resta a vostro carico. Biglietti del treno, "
        "Cinque Terre Card, ingressi, pasti, guida e mance del gruppo. Attesa oltre i 45 minuti di tolleranza, "
        "€ 50,00 all'ora. Soste, deviazioni o modifiche al programma, quotate su richiesta. Rientro a Nievole dopo "
        "le 02:00, € 250,00."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 412,50", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 962,50", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Il budget di € 700 + IVA.</b> Ve lo diciamo con franchezza: copre poco più della metà "
         "della giornata. Il servizio è di circa 220 km e tiene mezzo e "
         "conducente impegnati dalle 8:00 alle 19:45 di una domenica, il che significa che in quella giornata il "
         "mezzo non può fare altro. Il prezzo qui indicato è il nostro migliore per questo servizio. Se però avete "
         "altri movimenti nello stesso periodo — trasferimenti da o per gli aeroporti, altre escursioni — "
         "mandateceli e guardiamo l'insieme: su più servizi il discorso cambia."),
        ("<b>L'orario del rientro.</b> Abbiamo letto le «ore 18 circa» come l'ora di ripartenza da Migliarina: "
         "con quell'orario il gruppo è a Villa Ginevra verso le 19:45. Se invece le 18:00 sono l'ora in cui volete "
         "essere già rientrati a Nievole, il ritrovo in stazione si sposta alle 16:15 e il prezzo non cambia. "
         "Fateci sapere quale delle due, così fissiamo l'orario definitivo con la vostra guida."),
        ("<b>Migliarina è la scelta giusta.</b> Dal 2025 la stazione di Migliarina è l'hub del Cinque Terre Express, "
         "con un binario dedicato e trentacinque collegamenti al giorno verso Levanto e le Cinque Terre, e il suo "
         "piazzale è molto più agevole per un mezzo turistico rispetto alla Spezia Centrale. Ci serve soltanto il "
         "punto esatto di discesa concordato con la vostra guida e un suo recapito telefonico: il conducente si "
         "coordina direttamente con lei, sia all'arrivo sia al ritorno."),
        ("<b>Il mezzo resta alla Spezia tutto il giorno.</b> È la soluzione più conveniente per voi: due "
         "trasferimenti separati, con il mezzo che rientra a vuoto in Toscana e riparte nel pomeriggio, "
         "costerebbero sensibilmente di più. Il Comune della Spezia applica un ticket per la salita e la discesa "
         "dei passeggeri e una tariffa di sosta per i bus turistici: sono già compresi nel prezzo, non c'è nulla "
         "da pagare sul posto."),
        ("<b>Se il treno del ritorno ritarda.</b> Sulla linea delle Cinque Terre capita, soprattutto nei fine "
         "settimana d'ottobre. Il conducente attende senza costi aggiuntivi fino a 45 minuti oltre l'orario "
         "concordato; oltre quella soglia l'attesa è di € 50,00 all'ora. Basta una telefonata della guida e ci "
         "riorganizziamo."),
        ("<b>Il carico a Villa Ginevra.</b> Confermateci l'indirizzo esatto e il punto in cui sale il gruppo. "
         "Il nostro minibus arriva dove un autobus gran turismo non passa, ma conviene sapere in anticipo "
         "se possiamo accostare all'ingresso della villa o se è meglio darvi appuntamento sulla via principale. Confermateci anche che i dieci passeggeri salgono tutti a Villa Ginevra."),
        ("<b>Vitto del conducente.</b> Il servizio si apre e si chiude in giornata: non serve alcun "
         "pernottamento e non c'è nessun costo di albergo. Resta a vostro carico il solo pasto del "
         "conducente durante le ore di sosta alla Spezia: non lo mettiamo a preventivo e non lo organizziamo noi. "
         "Il modo più semplice è aggiungerlo alla sistemazione del gruppo, se ne avete una."),
        ("<b>Per confermare ci servono</b> l'indirizzo esatto e il punto di ritrovo a Villa Ginevra, l'orario "
         "definitivo del rientro, il recapito telefonico della vostra guida alla Spezia e del referente del gruppo, "
         "il numero definitivo dei passeggeri e i dati di fatturazione dell'agenzia."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è oggi libero per l'11 ottobre e lo teniamo a vostra "
         "disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla ricezione "
         "dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene "
         "trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il "
         "100%. Mancando oggi 51 giorni al servizio, questa prenotazione ricade già nella fascia da 60 a 30 giorni, "
         "e dall'11 settembre passerà in quella da 30 a 10. Preventivo valido fino al 4 settembre 2026."),
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
    subtitle="Cinque Terre day excursion · Nievole (Villa Ginevra) – La Spezia Migliarina  ·  Sunday 11 October 2026",
    meta="Prepared for %s  ·  21 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One touring minibus for your 10 passengers, with the same driver throughout the day.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "You asked for a 20-22 seater: the Beluga has 26, so your ten guests travel with all the room they could "
        "want and the hold stays free for daypacks, jackets and whatever gets bought along the way. Its 7.64 m "
        "matter on the roads around Nievole and in the forecourt of Migliarina station, where a full-size coach "
        "manoeuvres with far more difficulty."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sun 11 Oct<br/>outward",
         "<b>Nievole, Villa Ginevra (Monsummano Terme, PT) → La Spezia, Migliarina station.</b> "
         "The vehicle is on site a few minutes before 8:00 and leaves at 8:00 sharp. "
         "About 110 km along the A11 and A12 motorways, reaching Migliarina around 9:40, where your guide "
         "meets the group.",
         "approx. 08:00 – 09:40"),
        ("Sun 11 Oct<br/>during the day",
         "<b>Vehicle and driver stay in La Spezia for the whole excursion.</b> "
         "The minibus waits in the authorised tourist-coach area and the driver stays reachable by phone: "
         "if the group comes back earlier than planned, about thirty minutes' notice is enough to have him "
         "at the station.",
         "at your disposal"),
        ("Sun 11 Oct<br/>return",
         "<b>La Spezia, Migliarina station → Nievole, Villa Ginevra.</b> "
         "Departure at 18:00, the same 110 km back, reaching Villa Ginevra around 19:45.",
         "approx. 18:00 – 19:45"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sun 11 Oct — Nievole → La Spezia Migliarina, vehicle at disposal for the day and return "
         "(about 220 km, from 8:00 to 19:45)", "€ 1,250.00", "+ VAT 10%"),
        ("Driver's meal during the wait in La Spezia — no overnight stay required",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,250.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,375.00.",
    perhead="That is € 137.50 per person for the ten participants, both legs included.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, fuel, motorway tolls, the tourist-coach access ticket and parking "
        "charge in La Spezia, full insurance and hand-luggage handling. No other charges apply: neither Villa "
        "Ginevra nor Migliarina station requires any further permit. Should the return train run late, the driver "
        "waits at no extra cost for up to 45 minutes beyond the agreed time."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meal during the wait in La Spezia, which remains at your charge. Train tickets, Cinque Terre "
        "Card, entrance fees, meals, guide and the group's gratuities. Waiting beyond the 45-minute allowance, "
        "€ 50.00 per hour. Additional stops, detours or changes to the programme, quoted on request. Return to "
        "Nievole after 02:00, € 250.00."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 412.50", "VAT included"),
        ("Balance, within 5 days of the service", "€ 962.50", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The € 700 + VAT budget.</b> We will be straightforward about it: it covers a little over half the day. The service runs about 220 km and keeps "
         "vehicle and driver engaged from 8:00 to 19:45 on a Sunday, which means the vehicle can do nothing else "
         "that day. The price quoted here is our best for this service. If you have other movements in the same "
         "period, though — airport transfers, other excursions — send them over and we will look at the whole "
         "picture: across several services the conversation changes."),
        ("<b>The return time.</b> We have read the \"around 18:00\" as the departure time from Migliarina: on that "
         "basis the group is back at Villa Ginevra around 19:45. If instead 18:00 is the time you want to be back "
         "in Nievole, the pick-up at the station moves to 16:15 and the price does not change. Let us know which "
         "of the two, so we can set the final timing with your guide."),
        ("<b>Migliarina is the right choice.</b> Since 2025 Migliarina station has been the Cinque Terre Express "
         "hub, with a dedicated platform and thirty-five daily connections towards Levanto and the Cinque Terre, "
         "and its forecourt is far easier for a tourist vehicle than La Spezia Centrale. All we need is the exact "
         "drop-off point agreed with your guide and a mobile number for her: the driver will coordinate directly "
         "with the guide, both on arrival and for the return."),
        ("<b>The vehicle stays in La Spezia all day.</b> This is the cheaper arrangement for you: two separate "
         "transfers, with the vehicle running back empty to Tuscany and setting off again in the afternoon, would "
         "cost appreciably more. The City of La Spezia charges a ticket for picking up and setting down passengers "
         "and a parking fee for tourist coaches: both are already included in the price, with nothing to settle "
         "on site."),
        ("<b>If the return train runs late.</b> It happens on the Cinque Terre line, especially on October "
         "weekends. The driver waits at no extra cost for up to 45 minutes beyond the agreed time; past that, "
         "waiting is € 50.00 per hour. A phone call from the guide is all it takes for us to reorganise."),
        ("<b>Pick-up at Villa Ginevra.</b> Please confirm the exact address and the point where the group boards. "
         "Our minibus reaches places a full-size coach cannot, but it is worth knowing in advance whether we can "
         "pull up at the villa entrance or whether it is better to meet you on the main road. Please also confirm that all ten passengers board at Villa Ginevra."),
        ("<b>The driver's meal.</b> The service starts and ends within the day: no overnight stay is needed and "
         "there is no hotel cost to bear. Only the driver's meal during the waiting hours in La Spezia remains at "
         "your charge: we neither quote it nor arrange it. The simplest way is to add him to the group's arrangements, if you have any."),
        ("<b>To confirm we need</b> the exact address and meeting point at Villa Ginevra, the final return time, "
         "a mobile number for your guide in La Spezia and for the group leader, the final passenger count and your "
         "agency's invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free on 11 October and we hold it for you "
         "for the whole validity of this quotation; the booking becomes firm on receipt of the deposit. "
         "Cancellation is free of charge more than 60 days before the service; from 60 to 30 days the deposit is "
         "retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. With 51 days to the "
         "service today, this booking already falls in the 60-to-30-day band, and from 11 September it moves into "
         "the 30-to-10 band. Quotation valid until 4 September 2026."),
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
    cols = [26 * mm, usable - 26 * mm - 27 * mm, 27 * mm]
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Viaggi Tigullio Marcone")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Cinque_Terre_11_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

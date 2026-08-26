#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il tour in Toscana del 30 settembre - 2 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_tuscany_tour.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_tuscany_tour.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0930-SC"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Tour in Toscana: Montalcino, Firenze, Chianti, Siena  ·  30 settembre - 2 ottobre 2026",
    meta="Preparato per %s  ·  26 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un Beluga per il vostro gruppo di 24 persone, con lo stesso conducente per tutta la durata del programma.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 24 ospiti a bordo restano due posti liberi: comodi per le giornate fra le cantine, un margine "
        "più risicato per i bagagli dell'arrivo e della partenza in aeroporto. I 7,64 metri del mezzo "
        "raggiungono senza difficoltà i piazzali delle cantine in programma e il parcheggio bus autorizzato "
        "di Siena."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Mer 30 set",
         "<b>Aeroporto di Pisa (PSA) → sosta pranzo lungo il percorso (località da confermare) → "
         "Le Ragnaie (Montalcino).</b> "
         "Ritrovo alle 10:30 in aeroporto, l'autista vi accoglie in sala arrivi con il cartello GiroMunna. "
         "Circa 70 km fino al locale della sosta pranzo, 60-90 minuti di viaggio; dalle 12:00 alle 14:00 il "
         "mezzo e il conducente attendono durante il pranzo. Si riparte per gli ultimi 100 km circa, 120 "
         "minuti, con arrivo a Le Ragnaie (Montalcino) verso le 16:00. Da qui mezzo e conducente si liberano "
         "fino al ritrovo del giorno dopo.",
         "circa 10:30 – 16:00"),
        ("Gio 1 ott",
         "<b>Le Ragnaie → Vineria Aperta (Montalcino) → Antinori nel Chianti Classico (San Casciano in Val "
         "di Pesa) → hotel a Montalcino → ristorante Saloni → hotel.</b> "
         "Partenza alle 11:45, 15 minuti fino a Vineria Aperta per il pranzo dalle 12:00 alle 14:15. Alle "
         "15:45 si parte per la cantina Antinori, 90 minuti di strada; mezzo e conducente attendono durante "
         "visita e degustazione fino alle 18:30. Altri 90 minuti di rientro verso l'hotel, con una breve "
         "sosta di 20 minuti alle 20:00 per il cambio; alle 20:30 si riparte, 10 minuti, per la cena da "
         "Saloni fino alle 23:30, con rientro in hotel alle 23:40. La giornata più lunga del programma, "
         "quasi 12 ore di impegno.",
         "circa 11:45 – 23:40"),
        ("Ven 2 ott",
         "<b>Hotel a Montalcino → Siena, ristorante Le Logge → Querciabella (Greve in Chianti) → Aeroporto "
         "di Pisa (PSA).</b> "
         "Partenza alle 09:30, 60 minuti fino a Siena; visita del centro e pranzo da Le Logge dalle 10:30 "
         "alle 14:15, con il mezzo al parcheggio bus autorizzato. Alle 15:15 altri 60 minuti fino a "
         "Querciabella per la visita, fino alle 17:15. Ultimo trasferimento di 105 minuti verso l'aeroporto "
         "di Pisa, arrivo previsto alle 19:00, fine del servizio.",
         "circa 09:30 – 19:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Mer 30 set — aeroporto di Pisa → sosta pranzo → Le Ragnaie (Montalcino)", "€ 990,00", "+ IVA 10%"),
        ("Gio 1 ott — giornata intera: Vineria Aperta, Antinori, cena da Saloni", "€ 1.480,00", "+ IVA 10%"),
        ("Ven 2 ott — Siena (Le Logge) → Querciabella → aeroporto di Pisa, permesso Comune di Siena incluso",
         "€ 1.230,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente, 1 notte (1 ottobre)", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 3.700,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 4.070,00.",
    perhead="Sono circa € 170,00 a persona per l'intero programma.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, assicurazione completa, movimentazione "
        "bagagli e monitoraggio dei due voli. Sono compresi anche il parcheggio bus dell'aeroporto di Pisa "
        "(circa € 61,00 complessivi per i due transiti) e il permesso comunale per i bus turistici di Siena "
        "(circa € 160,00). Il 30 settembre l'autista attende senza costi aggiuntivi fino a 90 minuti "
        "dall'orario di atterraggio effettivo, per quanto il volo ritardi."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio del conducente per la notte dell'1 ottobre, che resta a vostro carico: la "
        "prenotazione e il pagamento li curate voi direttamente. Ingressi, degustazioni, pasti, guide e "
        "mance in cantina e nei ristoranti. Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. "
        "Soste aggiuntive o modifiche all'itinerario, quotate su richiesta. Rientro alla struttura dopo le "
        "02:00, € 250,00."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 1.221,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 2.849,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Il riposo del conducente fra giovedì e venerdì.</b> Tra il rientro in hotel di giovedì (23:40) "
         "e la partenza di venerdì (09:30) restano 9 ore e 50 minuti: sotto le 11 ore di riposo giornaliero "
         "previste per un autista professionista. Si risolve facilmente spostando di un'ora la cerniera fra "
         "le due giornate — partenza di venerdì alle 10:40, oppure rientro dalla cena di giovedì entro le "
         "22:30 — a scelta vostra e senza alcun costo aggiuntivo. Confermatecelo prima che vi mandiamo il "
         "programma definitivo."),
        ("<b>Le Ragnaie e l'hotel del giovedì.</b> Il programma indica l'arrivo di mercoledì e la partenza "
         "di giovedì mattina da Le Ragnaie, e un \"hotel\" a parte per la notte di giovedì: sono la stessa "
         "struttura o due diverse? Ci serve saperlo per fissare i punti di ritrovo esatti e, per la notte di "
         "giovedì, anche per prenotare il pernottamento del conducente."),
        ("<b>La sosta pranzo di mercoledì 30 settembre.</b> Non avendo ancora il locale esatto, abbiamo "
         "stimato il percorso Pisa–Montalcino con una sosta intermedia sulla direttrice Siena–Grosseto, "
         "zona San Gimignano/Colle di Val d'Elsa. Il prezzo indicato è su questa base: appena scegliete il "
         "locale verifichiamo che il mezzo acceda senza difficoltà e correggiamo percorso e prezzo se serve."),
        ("<b>Quale cantina Antinori.</b> Abbiamo quotato Antinori nel Chianti Classico a San Casciano in Val "
         "di Pesa, la sede storica del gruppo, a mezz'ora da Firenze. Confermatecelo: un'altra sede Antinori "
         "cambierebbe percorso e tempi di giovedì."),
        ("<b>Il permesso di Siena.</b> Il centro storico, dove si trova il ristorante Le Logge, è area "
         "pedonale: il mezzo vi lascia al parcheggio bus autorizzato e da lì si cammina pochi minuti. Il "
         "permesso comunale per i bus turistici, circa € 160,00, è già compreso nel prezzo di venerdì."),
        ("<b>Bagagli del 30 settembre.</b> Con 24 ospiti a bordo restano due posti liberi sul Beluga: "
         "comodo per il tour, più risicato per i bagagli da aeroporto. Segnalateci se ci sono valigie grandi "
         "o colli fuori misura, così organizziamo il carico."),
        ("<b>I due voli.</b> Ci servono numero e orario sia dell'arrivo del 30 settembre sia della partenza "
         "del 2 ottobre. Per l'arrivo l'attesa è gratuita fino a 90 minuti dall'atterraggio effettivo, per "
         "quanto il volo ritardi; per la partenza verifichiamo che le 19:00 di arrivo a Pisa lascino un "
         "margine adeguato rispetto al check-in."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, il nome e l'indirizzo "
         "dell'hotel/degli hotel a Montalcino, il locale scelto per il pranzo di mercoledì, la conferma "
         "della cantina Antinori, gli orari dei due voli e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla "
         "ricezione dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 "
         "giorni viene trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli "
         "ultimi 10 giorni il 100%. Mancando oggi 35 giorni al primo servizio, questa prenotazione ricade "
         "nella fascia da 60 a 30 giorni, e dal 31 agosto passerà in quella da 30 a 10. Preventivo valido "
         "fino al 9 settembre 2026."),
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
    subtitle="Tuscany tour: Montalcino, Florence, Chianti, Siena  ·  30 September - 2 October 2026",
    meta="Prepared for %s  ·  26 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One Beluga for your group of 24, with the same driver throughout the programme.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 24 guests on board two seats stay free: comfortable for the days among the wineries, a "
        "tighter margin for the luggage on the airport transfers. At 7.64 m the vehicle reaches the "
        "courtyard of every winery on the programme, and the authorised coach park in Siena, without "
        "difficulty."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Wed 30 Sep",
         "<b>Pisa Airport (PSA) → lunch stop along the way (venue to be confirmed) → Le Ragnaie "
         "(Montalcino).</b> "
         "Meeting point 10:30 at the airport, where the driver welcomes you in the arrivals hall with the "
         "GiroMunna sign. About 70 km to the lunch venue, 60-90 minutes of driving; from 12:00 to 14:00 "
         "vehicle and driver wait during lunch. On for the remaining 100 km or so, 120 minutes, reaching Le "
         "Ragnaie (Montalcino) around 16:00. From there vehicle and driver are released until the following "
         "day's pick-up.",
         "approx. 10:30 – 16:00"),
        ("Thu 1 Oct",
         "<b>Le Ragnaie → Vineria Aperta (Montalcino) → Antinori nel Chianti Classico (San Casciano in Val "
         "di Pesa) → hotel in Montalcino → Saloni restaurant → hotel.</b> "
         "Departure at 11:45, 15 minutes to Vineria Aperta for lunch from 12:00 to 14:15. At 15:45 on to the "
         "Antinori winery, 90 minutes of driving; vehicle and driver wait through the visit and tasting "
         "until 18:30. Another 90 minutes back to the hotel, with a brief 20-minute stop at 20:00 to freshen "
         "up; at 20:30 on again, 10 minutes, for dinner at Saloni until 23:30, back at the hotel at 23:40. "
         "The longest day of the programme, close to 12 hours of engagement.",
         "approx. 11:45 – 23:40"),
        ("Fri 2 Oct",
         "<b>Hotel in Montalcino → Siena, Le Logge restaurant → Querciabella (Greve in Chianti) → Pisa "
         "Airport (PSA).</b> "
         "Departure at 09:30, 60 minutes to Siena; a visit to the centre and lunch at Le Logge from 10:30 to "
         "14:15, with the vehicle at the authorised coach park. At 15:15 another 60 minutes to Querciabella "
         "for the visit, until 17:15. A final 105-minute transfer to Pisa Airport, arriving around 19:00, "
         "end of service.",
         "approx. 09:30 – 19:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Wed 30 Sep — Pisa airport → lunch stop → Le Ragnaie (Montalcino)", "€ 990.00", "+ VAT 10%"),
        ("Thu 1 Oct — full day: Vineria Aperta, Antinori, dinner at Saloni", "€ 1,480.00", "+ VAT 10%"),
        ("Fri 2 Oct — Siena (Le Logge) → Querciabella → Pisa airport, Siena municipal permit included",
         "€ 1,230.00", "+ VAT 10%"),
        ("Driver's board and lodging, 1 night (1 October)", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 3,700.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 4,070.00.",
    perhead="That is about € 170.00 per person for the complete programme.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, full insurance, luggage handling and flight monitoring "
        "on both flights. Also included are the coach parking fee at Pisa Airport (about € 61.00 total for "
        "the two transits) and the municipal permit for tourist coaches in Siena (about € 160.00). On 30 "
        "September the driver waits at no extra cost for up to 90 minutes from the actual landing time, "
        "however late the flight arrives."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's board and lodging for the night of 1 October, which remain at your charge: you book "
        "and pay for them directly. Winery entrance fees, tastings, meals, guides and gratuities at the "
        "wineries and restaurants. Waiting beyond the times set out here, € 50.00 per hour per vehicle. "
        "Additional stops or changes to the itinerary, quoted on request. Return to the property after "
        "02:00, € 250.00."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 1,221.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 2,849.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The driver's rest between Thursday and Friday.</b> Between Thursday's return to the hotel "
         "(23:40) and Friday's departure (09:30) only 9 hours and 50 minutes remain: below the 11 hours of "
         "daily rest required for a professional driver. It is easily solved by shifting the hinge between "
         "the two days by about an hour — a 10:40 departure on Friday, or returning from Thursday's dinner "
         "by 22:30 — whichever you prefer, at no extra cost. Please confirm before we send the final "
         "programme."),
        ("<b>Le Ragnaie and Thursday's hotel.</b> The programme shows Wednesday's arrival and Thursday "
         "morning's departure at Le Ragnaie, and a separate \"hotel\" for Thursday night: are these the "
         "same property or two different ones? We need to know to fix the exact meeting points and, for "
         "Thursday night, to book the driver's accommodation."),
        ("<b>Wednesday 30 September's lunch stop.</b> Without the exact venue yet, we have estimated the "
         "Pisa–Montalcino route with a stop along the Siena–Grosseto road, around San Gimignano/Colle di "
         "Val d'Elsa. The price quoted is on this basis: once you choose the venue we will check the "
         "vehicle can access it without difficulty and adjust the route and price if needed."),
        ("<b>Which Antinori estate.</b> We have quoted Antinori nel Chianti Classico at San Casciano in Val "
         "di Pesa, the group's flagship estate, half an hour from Florence. Please confirm: a different "
         "Antinori venue would change Thursday's route and timing."),
        ("<b>The Siena permit.</b> The historic centre, home to the restaurant Le Logge, is a pedestrian "
         "area: the vehicle drops you at the authorised coach park and it is a short walk from there. The "
         "municipal permit for tourist coaches, about € 160.00, is already included in Friday's price."),
        ("<b>Luggage on 30 September.</b> With 24 guests on board only two seats stay free on the Beluga: "
         "comfortable for the tour, tighter for airport luggage. Let us know about any large suitcases or "
         "oversized items so we can plan the loading."),
        ("<b>The two flights.</b> We need the number and time for both the arrival on 30 September and the "
         "departure on 2 October. For the arrival, waiting is free for up to 90 minutes from actual "
         "landing, however late the flight; for the departure we will check that reaching Pisa at 19:00 "
         "leaves an adequate margin before check-in."),
        ("<b>To confirm we need</b> the final passenger count, the name and address of the hotel(s) in "
         "Montalcino, the venue chosen for Wednesday's lunch, confirmation of the Antinori estate, both "
         "flight times, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you for "
         "the whole validity of this quotation; the booking becomes firm on receipt of the deposit. "
         "Cancellation is free of charge more than 60 days before the service; from 60 to 30 days the "
         "deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. "
         "With 35 days to the first service today, this booking falls in the 60-to-30-day band, and from "
         "31 August it moves into the 30-to-10 band. Quotation valid until 9 September 2026."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Sir Catering")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Tuscany_Tour_30_settembre-2_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

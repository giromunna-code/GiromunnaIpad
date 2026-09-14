#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per Keshav Menon — due trasferimenti Castel Monastero
-> Castelfalfi e Castelfalfi -> Cape of Senses, Lago di Garda.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_menon.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_menon.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-MENON"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Due trasferimenti privati — Castel Monastero → Castelfalfi (20) e Castelfalfi → Cape of Senses, Lago di Garda (23)",
    meta="Preparato per %s  ·  9 settembre 2026, aggiornato il 14 settembre 2026  ·  Rif. " + RIF + "  ·  valido fino al 24 settembre 2026",
    intro=(
        "Grazie per averci confermato i bagagli — 23 valigie da stiva e 15 bagagli a mano: il carico rientra "
        "nella capienza del minibus, come spiegato sotto. Era l'unico punto rimasto aperto nella prima versione "
        "di questo preventivo, che ora è risolto. Confermiamo due dei quattro tratti richiesti: il 20 (Castel "
        "Monastero → Castelfalfi) e il 23 (Castelfalfi → Cape of Senses, Lago di Garda). Il 17 e il 26 — i due "
        "tratti da e per Milano — non rientrano purtroppo fra i servizi che possiamo offrire. Per i due "
        "trasferimenti che possiamo effettuare useremmo il nostro minibus. I prezzi sono per singolo "
        "trasferimento, come richiesto, non a giornata intera."
    ),
    h_mezzo="Il mezzo",
    mezzo_rows=[
        ("Mezzo",
         "Mercedes-Benz Beluga — 26 posti passeggeri più l'autista. È la misura giusta per un gruppo di 16: i "
         "dieci posti liberi lasciano spazio a bordo, e la carrozzeria compatta raggiunge resort e strade di "
         "collina dove un autobus gran turismo non arriva."),
        ("Bagagli",
         "<b>Confermato.</b> Le 23 valigie da stiva riempiono esattamente il vano bagagli dedicato, al limite "
         "della sua capienza comoda (circa 23 valigie della misura indicata, ~30 kg ciascuna): non resta margine "
         "per altro nel vano. I 15 bagagli a mano viaggiano con il gruppo nell'abitacolo — con 16 persone su 26 "
         "posti, i dieci sedili liberi lasciano ampio spazio per sistemarli."),
        ("Comfort",
         "Aria condizionata, sedili reclinabili con cinture di sicurezza, frigo bar, impianto audio di bordo."),
        ("Autista",
         "Conducente professionista. Parla italiano e spagnolo, non inglese — lo segnaliamo in anticipo perché "
         "non ci siano sorprese il giorno del servizio."),
    ],
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Durata"],
    svc=[
        ("20",
         "<b>Castel Monastero → Castelfalfi.</b> Ritrovo a Castel Monastero, Castelnuovo Berardenga (SI), carico "
         "dei bagagli e trasferimento diretto a Castelfalfi, Montaione (FI). Sola andata: una volta lasciato il "
         "gruppo, il minibus rientra alla base senza passeggeri.",
         "circa 1 h 45, orario da definire"),
        ("23",
         "<b>Castelfalfi → Cape of Senses Hideaway, Lago di Garda.</b> Ritrovo a Castelfalfi e trasferimento al "
         "Cape of Senses Hideaway, Torri del Benaco (VR), sulla sponda veronese del Lago di Garda. Sola andata, "
         "con sosta obbligatoria lungo il percorso e il minibus che rientra vuoto.",
         "circa 4 h, orario da definire"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("20 — Castel Monastero → Castelfalfi. Minibus con conducente professionista, trasferimento di sola "
         "andata. Carburante, pedaggi, assicurazione e riposizionamento del mezzo da e per la nostra base inclusi.",
         "€ 950,00", "+ IVA 10%"),
        ("23 — Castelfalfi → Cape of Senses, Torri del Benaco (VR). Minibus con conducente professionista, "
         "trasferimento di sola andata. Carburante, pedaggi, assicurazione e riposizionamento del mezzo da e per "
         "la nostra base inclusi.",
         "€ 1.650,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.600,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.860,00.",
    price_note=(
        "Prezzo fisso per i due trasferimenti: nessun altro addebito oltre a quanto elencato in «Non incluso». "
        "Ogni trasferimento è quotato singolarmente: potete confermarli entrambi o uno solo. Prezzo calcolato "
        "sui bagagli ora confermati — 23 valigie da stiva, al limite della capienza del vano, e 15 bagagli a "
        "mano nell'abitacolo con il gruppo."
    ),
    h_incluso="Incluso.",
    incluso=(
        "Minibus con conducente professionista a disposizione esclusiva del gruppo per ciascuno dei due "
        "trasferimenti. Carico e trasporto dei bagagli: 23 valigie nel vano bagagli e 15 bagagli a mano "
        "nell'abitacolo. Carburante, pedaggi autostradali e assicurazione. Riposizionamento del mezzo da e per "
        "la nostra base, prima e dopo ciascun servizio. Tutte le imposte applicabili: l'IVA al 10% è indicata "
        "separatamente sopra ed è già compresa nel totale da corrispondere."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "I trasferimenti del 17 (Milano → Castel Monastero) e del 26 (Cape of Senses → Milano), che non siamo "
        "in grado di coprire. Attesa oltre l'orario di partenza concordato, € 50,00 all'ora. Soste o destinazioni "
        "aggiuntive rispetto al trasferimento diretto, in particolare quelle che richiederebbero un permesso di "
        "accesso in città. Tutto quanto non espressamente elencato sopra."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 858,00", ""),
        ("Saldo, 5 giorni prima del primo trasferimento", "€ 2.002,00", "data da fissare col mese"),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. La prenotazione diventa definitiva "
          "alla ricezione dell'acconto. La fattura viene emessa un'unica volta, per l'importo totale, al momento "
          "del saldo."),
    h_note="Note",
    note=[
        ("<b>Bagagli — confermato.</b> Le 23 valigie da stiva e i 15 bagagli a mano che ci avete indicato "
         "rientrano nella capienza del minibus: le valigie riempiono il vano fino al limite della sua capienza "
         "comoda, i bagagli a mano viaggiano con voi nell'abitacolo sui sedili liberi. Non c'è margine per bagagli "
         "ulteriori il giorno della partenza: se il numero dovesse cambiare, fatecelo sapere prima di confermare."),
        ("<b>Trasferimenti non coperti.</b> Il 17 (Milano → Castel Monastero) e il 26 (Cape of Senses → Milano) "
         "non rientrano fra i servizi che possiamo offrire."),
        ("<b>Oneri di accesso in città.</b> Molte città italiane prevedono un permesso giornaliero per l'ingresso "
         "di autobus; quando è dovuto lo indichiamo in preventivo alla tariffa ufficiale. Per i due trasferimenti "
         "qui quotati non è dovuto alcun onere: Castel Monastero e Castelfalfi sono tenute di campagna fuori da "
         "ogni zona a traffico limitato, e Torri del Benaco non ha un permesso bus registrato. Se dovesse "
         "emergere, ve lo segnaliamo prima del servizio e lo giriamo alla tariffa ufficiale, senza alcun ricarico."),
        ("<b>Il mese e l'anno.</b> La vostra richiesta indica il 17, il 20, il 23 e il 26, ma non il mese: ci "
         "serve per fissare le date in modo definitivo."),
        ("<b>Gli orari di partenza</b> di ciascun trasferimento, ancora da concordare."),
        ("<b>Accesso al Cape of Senses Hideaway.</b> La struttura sorge sulla collina sopra Torri del Benaco: "
         "vorremmo verificare con voi, o direttamente con l'hotel, che la strada di accesso sia percorribile dal "
         "mezzo. In caso contrario, concordiamo un punto di sbarco a Torri del Benaco."),
        ("<b>Un numero di cellulare del gruppo</b>, da passare all'autista il giorno del servizio."),
        ("<b>Validità e cancellazione.</b> Il preventivo è valido fino al 24 settembre 2026. Alla conferma le "
         "date restano bloccate 48 ore: trascorse senza l'acconto, vengono rilasciate. La cancellazione è "
         "gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni si trattiene l'acconto; da 30 a 10 giorni "
         "il 50%; negli ultimi 10 giorni il 100%."),
    ],
    closing=("Restiamo a vostra disposizione per confermare il servizio. Per procedere basta rispondere a questo "
             "preventivo: vi invieremo la richiesta dell'acconto e, più vicino alla data, nome e recapito diretto "
             "del vostro autista.<br/><br/>"
             "GiroMunna · Munna Girolamo Giuseppe · Ponte Buggianese (PT), Toscana · +39 335 587 4744 · "
             "info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Two point-to-point transfers — Castel Monastero → Castelfalfi (20th) and Castelfalfi → Cape of Senses, Lake Garda (23rd)",
    meta="Prepared for %s  ·  9 September 2026, updated 14 September 2026  ·  Ref. " + RIF + "  ·  valid until 24 September 2026",
    intro=(
        "Thank you for confirming the luggage — 23 check-in suitcases and 15 cabin bags: the load fits within "
        "the minibus, as explained below. That was the one point left open in the first version of this "
        "quotation, and it is now resolved. Of the four legs you asked about, we can confirm two: the 20th "
        "(Castel Monastero to Castelfalfi) and the 23rd (Castelfalfi to Cape of Senses, Lake Garda). The 17th and "
        "the 26th — the two legs from and to Milan — are unfortunately not among the services we are able to "
        "offer. For the two transfers we can operate we would use our minibus. These are priced as individual "
        "point-to-point transfers, as you asked, not as full-day hire."
    ),
    h_mezzo="The vehicle",
    mezzo_rows=[
        ("Vehicle",
         "Mercedes-Benz Beluga — 26 passenger seats plus the driver. It is the right size for a group of 16: "
         "the ten spare seats leave room on board, and its compact body reaches resorts and hill roads that a "
         "full-size touring coach cannot."),
        ("Luggage",
         "<b>Now confirmed.</b> The 23 check-in bags fill the dedicated hold exactly at its comfortable limit "
         "(around 23 suitcases of the size you mentioned, ~30 kg each): there is no spare room left in the hold. "
         "The 15 cabin bags travel with the group inside the passenger cabin — with 16 of you on 26 seats, the "
         "ten spare seats give plenty of room for them."),
        ("Comfort",
         "Air conditioning, reclining seats with seatbelts, fridge bar, on-board sound system."),
        ("Driver",
         "Professional driver. He speaks Italian and Spanish, not English — we mention it in advance so there "
         "are no surprises on the day."),
    ],
    h_servizio="Programme",
    svc_head=["Date", "Route", "Duration"],
    svc=[
        ("20th",
         "<b>Castel Monastero → Castelfalfi.</b> Pick-up at Castel Monastero, Castelnuovo Berardenga (SI), "
         "loading of the luggage and direct transfer to Castelfalfi, Montaione (FI). One way: once the group has "
         "been dropped off, the minibus returns to our base with no passengers on board.",
         "approx. 1 h 45, time to be agreed"),
        ("23rd",
         "<b>Castelfalfi → Cape of Senses Hideaway, Lake Garda.</b> Pick-up at Castelfalfi and transfer to the "
         "Cape of Senses Hideaway, Torri del Benaco (VR), on the Verona shore of Lake Garda. One way as well, "
         "plus the statutory rest stop along the way, with the minibus returning empty.",
         "approx. 4 h, time to be agreed"),
    ],
    h_prezzo="Price",
    price_rows=[
        ("20th — Castel Monastero → Castelfalfi. Minibus with professional driver, one-way transfer. Fuel, "
         "tolls, insurance and repositioning of the vehicle to and from our base included.",
         "€ 950.00", "+ VAT 10%"),
        ("23rd — Castelfalfi → Cape of Senses, Torri del Benaco (VR). Minibus with professional driver, "
         "one-way transfer. Fuel, tolls, insurance and repositioning of the vehicle to and from our base "
         "included.",
         "€ 1,650.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,600.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,860.00.",
    price_note=(
        "Fixed price for the two transfers: no further charges beyond those listed under “Not included” "
        "below. Each transfer is priced on its own: you may confirm both or just one. Priced for luggage as now "
        "confirmed — 23 check-in bags in the hold, at its full capacity, and 15 cabin bags carried with the "
        "group in the passenger cabin."
    ),
    h_incluso="Included.",
    incluso=(
        "Minibus with professional driver at your group's exclusive disposal for each of the two transfers. "
        "Loading and carriage of the luggage: 23 bags in the hold and 15 cabin bags in the passenger cabin. "
        "Fuel, motorway tolls and insurance. Repositioning of the vehicle to and from our base, before and after "
        "each service. All applicable taxes: VAT at 10% is shown separately above and is already included in the "
        "total payable."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The transfers on the 17th (Milan → Castel Monastero) and on the 26th (Cape of Senses → Milan), which we "
        "are unable to cover. Waiting beyond the agreed departure time, € 50.00 per hour. Any additional stops or "
        "destinations beyond the direct transfer, in particular any that would require a city access permit. "
        "Anything not expressly listed above."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 858.00", ""),
        ("Balance, 5 days before the first transfer", "€ 2,002.00", "exact date once the month is confirmed"),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. The booking becomes firm once the "
          "deposit is received. The invoice is issued once, for the full amount, at the time of the balance "
          "payment."),
    h_note="Notes",
    note=[
        ("<b>Luggage — confirmed.</b> The 23 check-in bags and 15 cabin bags you gave us fit the minibus's "
         "capacity: the suitcases fill the hold up to its comfortable limit, and the cabin bags travel with you "
         "inside the passenger cabin, on the spare seats. There is no margin for extra luggage on the day: if "
         "the count changes, please let us know before confirming."),
        ("<b>Transfers we cannot cover.</b> The 17th (Milan → Castel Monastero) and the 26th (Cape of Senses → "
         "Milan) are not among the services we are able to offer."),
        ("<b>On city access charges.</b> Many Italian towns charge coaches a daily permit to enter, and whenever "
         "one applies we show it in the quotation at the official rate. For the two transfers quoted here no such "
         "charge is due: Castel Monastero and Castelfalfi are countryside estates, outside any restricted traffic "
         "zone, and Torri del Benaco has no coach access permit on record. Should one emerge, we will tell you "
         "before the service and pass it on at the official rate, with no mark-up."),
        ("<b>The month and year.</b> Your enquiry gives the 17th, 20th, 23rd and 26th but not the month: we need "
         "it to fix the dates for good."),
        ("<b>The departure time</b> for each transfer, still to be agreed."),
        ("<b>Access to the Cape of Senses Hideaway.</b> The property sits on the hillside above Torri del "
         "Benaco, and we would like to check with you, or directly with the hotel, that the approach road is "
         "suitable for the vehicle. If it is not, we will agree a workable drop-off point in Torri del Benaco."),
        ("<b>A mobile number for the group</b>, to pass to the driver on the day."),
        ("<b>Validity and cancellation.</b> This quotation is valid until 24 September 2026. On confirmation the "
         "dates are held for 48 hours: after that, without the deposit, they are released. Cancellation is free "
         "of charge more than 60 days before the service; from 60 to 30 days the deposit is retained; from 30 to "
         "10 days 50% of the price is charged; in the last 10 days, 100%."),
    ],
    closing=("We remain at your disposal to confirm the service. To go ahead, simply reply to this quotation: we "
             "will send the deposit request and, closer to the date, the name and direct number of your "
             "driver.<br/><br/>"
             "GiroMunna · Munna Girolamo Giuseppe · Ponte Buggianese (PT), Tuscany · +39 335 587 4744 · "
             "info@giromunna.com"),
)


def styles():
    base = dict(fontName="Helvetica", textColor=INK, leading=13.2, fontSize=9.2)
    return {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=21,
                                textColor=GREEN, leading=24, spaceAfter=3),
        "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=10.2,
                                   textColor=INK, leading=14, spaceAfter=2),
        "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=8.6,
                               textColor=MUTED, leading=12, spaceAfter=10),
        "intro": ParagraphStyle("intro", alignment=TA_JUSTIFY, spaceAfter=8, **base),
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
        "lbl": ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=8.6,
                              textColor=GREEN, leading=12),
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
    F.append(Paragraph(L["intro"], S["intro"]))

    # --- mezzo (tabella descrittiva)
    F.append(Paragraph(L["h_mezzo"], S["h2"]))
    mcols = [24 * mm, usable - 24 * mm]
    mdata = [[Paragraph(lbl, S["lbl"]), Paragraph(txt, S["cellsm"])] for lbl, txt in L["mezzo_rows"]]
    mt = Table(mdata, colWidths=mcols)
    mt.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    F.append(mt)

    # --- servizio
    F.append(Paragraph(L["h_servizio"], S["h2"]))
    cols = [18 * mm, usable - 18 * mm - 32 * mm, 32 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for date, desc, dur in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % date, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
            Paragraph(dur, S["cellmut"]),
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
    price_note_box = Table([[Paragraph(L["price_note"], S["cellsm"])]], colWidths=[usable])
    price_note_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    # la lista va costruita prima: KeepTogether non tiene il riferimento
    # a una lista vuota passata alla costruzione.
    F.append(KeepTogether([
        Paragraph(L["h_prezzo"], S["h2"]),
        pt,
        Paragraph(L["grand"], S["grand"]),
        Spacer(1, 6),
        price_note_box,
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Keshav Menon")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Keshav_Menon_Castel_Monastero_Castelfalfi_Lago_di_Garda_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

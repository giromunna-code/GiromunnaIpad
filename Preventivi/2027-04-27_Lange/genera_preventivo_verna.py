#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per l'escursione giornaliera Firenze - Santuario della Verna -
Firenze, martedi' 27 aprile 2027 (gruppo di 25 persone, Alexandra Lange).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_verna.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_verna.py --lingua en --cliente "Client Name"
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

RIF = "GM-2027-0427-AL"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Escursione giornaliera Firenze – Santuario della Verna – Firenze  ·  martedì 27 aprile 2027",
    meta="Preparato per %s  ·  15 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus riservato al vostro gruppo di 25 persone, con il conducente a disposizione per tutta "
        "la giornata: al mattino da Firenze al Santuario della Verna, la sosta al santuario con il mezzo "
        "che vi aspetta, e in serata il rientro a Firenze, senza altri passeggeri."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 25 posti passeggeri più accompagnatore e autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "La Verna si raggiunge con una strada di montagna, stretta e con molte curve nell'ultimo tratto "
        "che sale al santuario. Con meno di 8 metri di lunghezza il Beluga la percorre con agio, dove un "
        "autobus gran turismo procede a fatica: il viaggio è più sciolto e più comodo per chi sta a bordo."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Orario"],
    svc=[
        ("Mar 27 apr",
         "<b>Parcheggio Villa Costanza (A1, Scandicci) → Santuario della Verna, Chiusi della Verna (AR).</b> "
         "Circa 105 km per l'A1, Pontassieve, il passo della Consuma e Bibbiena; arrivo verso le 9:45.",
         "partenza 7:45"),
        ("",
         "<b>Sosta al santuario.</b> Il minibus e il conducente restano a vostra disposizione alla Verna "
         "per tutta la visita.",
         "circa 7 ore"),
        ("",
         "<b>Santuario della Verna → Parcheggio Villa Costanza.</b> Stesso percorso; arrivo "
         "verso le 19:00, poi tramvia per il centro.",
         "partenza 17:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Escursione Firenze – Santuario della Verna – Firenze, minibus con conducente a disposizione "
         "dalle 7:45 alle 19:00", "€ 1.300,00", "+ IVA 10%"),
        ("Pranzo del conducente", "a carico vostro", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.300,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.430,00.",
    perhead=("Su 25 persone sono circa € 57,20 a testa per l'intera giornata, IVA inclusa. "
             "Il prezzo è per il mezzo, non per persona: non cambia se siete qualcuno in meno."),
    h_incluso="Incluso.",
    incluso=(
        "Minibus con conducente per tutta la giornata, carburante, eventuali pedaggi, parcheggi, "
        "permessi e assicurazione completa. Con il ritrovo a Villa Costanza il minibus non entra in "
        "città e non ci sono costi di accesso a Firenze: nessun altro costo oltre a quelli indicati."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il pranzo del conducente, a carico vostro (vedi le note). Attesa oltre il rientro delle 19:00, "
        "€ 50,00 all'ora. I biglietti della tramvia per Villa Costanza. Fermate o deviazioni "
        "aggiuntive, quotate su richiesta. Se si preferisce un ritrovo in centro a Firenze, il check "
        "point per i bus turistici, € 421,00."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 429,00", "IVA inclusa"),
        ("Saldo, entro il 27 aprile 2027, giorno del servizio", "€ 1.001,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Il punto di ritrovo: parcheggio Villa Costanza.</b> È il parcheggio scambiatore sull'A1 fra "
         "Firenze e Scandicci, capolinea della tramvia T1. Da Santo Spirito si va a piedi alla fermata "
         "Alamanni – Stazione, attraversando l'Arno al Ponte alla Carraia (circa 15 minuti), e da lì "
         "il tram porta a Villa Costanza in circa 20 minuti, con corse frequenti fin dal primo mattino. "
         "Vi consigliamo di uscire da Santo Spirito alle 7:00; il minibus vi aspetta dalle 7:30. "
         "Così il mezzo non entra in città: niente check point per i bus turistici (€ 421,00 al giorno), "
         "niente traffico cittadino, e si parte direttamente in autostrada, con orari più sicuri sia al "
         "mattino sia al rientro della sera. In serata vi riportiamo a Villa Costanza, da dove il tram "
         "vi riporta in centro."),
        ("<b>La strada.</b> Il percorso più diretto passa per il passo della Consuma: circa due ore, "
         "con un lungo tratto di curve dopo Pontassieve. Chi soffre il mal d'auto si trova meglio nei posti davanti; il "
         "conducente conosce la strada e procede con calma. Se qualcuno lo preferisce, al ritorno si "
         "può fare il giro per Arezzo e l'autostrada: è più lungo in chilometri, ma con meno curve, e "
         "il prezzo non cambia."),
        ("<b>Gli orari.</b> Con la partenza alle 7:45 siete al santuario verso le 9:45, con circa sette "
         "ore per la visita, la messa e il pranzo. Al santuario i frati salgono ogni giorno in "
         "processione alla Cappella delle Stimmate nel primo pomeriggio: se volete assistervi, vi "
         "consigliamo di verificare l'orario con il santuario. Ripartendo alle 17:00 siete a Firenze "
         "verso le 19:00, a Villa Costanza, senza il traffico serale del centro. Gli orari si "
         "possono spostare senza costi, purché la giornata resti entro le 19:00."),
        ("<b>Il pranzo, e quello del conducente.</b> Il santuario ha un refettorio per i pellegrini, che "
         "per un gruppo di 25 persone va prenotato con anticipo. Il pranzo del conducente è a carico "
         "vostro e non compare come importo nel preventivo: la soluzione più semplice è includerlo nella "
         "vostra prenotazione, al refettorio o nel ristorante che sceglierete. Il servizio si svolge "
         "in giornata, quindi non servono pernottamenti."),
        ("<b>Il clima.</b> La Verna è a circa 1.100 metri: a fine aprile, anche con una bella giornata a "
         "Firenze, lassù fa decisamente più fresco e può esserci nebbia. Conviene avvisare il gruppo di "
         "portare una giacca e scarpe comode per i sentieri attorno al santuario."),
        ("<b>Il numero delle persone.</b> Il Beluga ha 25 posti passeggeri più il posto "
         "dell'accompagnatore: per 25 persone è al completo, e resta solo il posto accanto al conducente "
         "per un'eventuale guida o accompagnatore. Se il gruppo dovesse crescere, avvisateci prima della "
         "conferma."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, il nome e il cellulare di "
         "un referente per il giorno del servizio e i dati per la fattura."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero per il 27 aprile 2027 e lo "
         "teniamo a vostra disposizione fino al 30 ottobre 2026, data di validità del preventivo; la "
         "prenotazione diventa definitiva alla ricezione dell'acconto. La cancellazione è gratuita fino "
         "a 60 giorni dal servizio; da 60 a 30 giorni si trattiene l'acconto; da 30 a 10 giorni si "
         "addebita il 50% dell'importo, negli ultimi 10 giorni l'intero importo."),
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
    subtitle="Day excursion Florence – Sanctuary of La Verna – Florence  ·  Tuesday 27 April 2027",
    meta="Prepared for %s  ·  15 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "A minibus reserved for your group of 25 people, with the driver at your disposal for the whole "
        "day: in the morning from Florence to the Sanctuary of La Verna, the stay at the sanctuary with "
        "the vehicle waiting for you, and in the evening the return to Florence, with no other passengers."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 25 passenger seats plus guide seat and driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "La Verna is reached by a mountain road, narrow and winding on the last stretch up to the "
        "sanctuary. At under 8 metres long the Beluga handles it with ease, where a full-size coach "
        "struggles: the journey is smoother and more comfortable for everyone on board."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Time"],
    svc=[
        ("Tue 27 Apr",
         "<b>Villa Costanza car park (A1, Scandicci) → Sanctuary of La Verna, Chiusi della Verna (AR).</b> "
         "About 105 km via the A1, Pontassieve, the Consuma pass and Bibbiena; arrival around 9:45.",
         "departure 7:45"),
        ("",
         "<b>Stay at the sanctuary.</b> The minibus and driver remain at your disposal at La Verna "
         "throughout the visit.",
         "about 7 hours"),
        ("",
         "<b>Sanctuary of La Verna → Villa Costanza car park.</b> Same route; arrival "
         "around 19:00, then tram to the centre.",
         "departure 17:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Excursion Florence – Sanctuary of La Verna – Florence, minibus with driver at your disposal "
         "from 7:45 to 19:00", "€ 1,300.00", "+ VAT 10%"),
        ("Driver's lunch", "at your charge", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,300.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,430.00.",
    perhead=("Across 25 people that is about € 57.20 each for the whole day, VAT included. "
             "The price is for the vehicle, not per person: it does not change if a few of you are missing."),
    h_incluso="Included.",
    incluso=(
        "Minibus with driver for the whole day, fuel, any tolls, parking, permits and full insurance. "
        "With the meeting point at Villa Costanza the minibus does not enter the city and there are no "
        "access charges in Florence: no costs other than those shown."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's lunch, at your charge (see the notes). Waiting beyond the 19:00 return, € 50.00 "
        "per hour. Tram tickets to Villa Costanza. Additional stops or detours, quoted on request. If a "
        "meeting point in central Florence is preferred, the tourist-coach check point, € 421.00."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 429.00", "VAT included"),
        ("Balance, by 27 April 2027, the day of the service", "€ 1,001.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The meeting point: Villa Costanza car park.</b> It is the park-and-ride on the A1 between "
         "Florence and Scandicci, terminus of tram line T1. From Santo Spirito you walk to the Alamanni – "
         "Stazione stop, crossing the Arno at Ponte alla Carraia (about 15 minutes), and from there the "
         "tram reaches Villa Costanza in about 20 minutes, with frequent services from early morning. "
         "We suggest leaving Santo Spirito at 7:00; the minibus will be waiting from 7:30. This way the "
         "vehicle does not enter the city: no tourist-coach check point (€ 421.00 per day), no city "
         "traffic, and we start directly on the motorway, with more reliable times both in the morning "
         "and on the evening return. In the evening we bring you back to Villa Costanza, where the tram "
         "takes you back to the centre."),
        ("<b>The road.</b> The most direct route crosses the Consuma pass: about two hours, with a long "
         "winding stretch after Pontassieve. Anyone prone to travel sickness is better off in the front seats; the driver "
         "knows the road and takes it calmly. If preferred, the return can go via Arezzo and the "
         "motorway: longer in kilometres but with fewer bends, and the price does not change."),
        ("<b>The schedule.</b> Leaving at 7:45 you reach the sanctuary around 9:45, with about seven hours "
         "for the visit, Mass and lunch. Every day the friars walk in procession to the Chapel of the "
         "Stigmata in the early afternoon: if you wish to attend, we suggest checking the time with the "
         "sanctuary. Leaving at 17:00 you are back at Villa Costanza around 19:00, avoiding evening "
         "traffic in the centre. Times can be moved at no cost, as long as the day ends by 19:00."),
        ("<b>Lunch, and the driver's lunch.</b> The sanctuary has a pilgrims' refectory, which for a "
         "group of 25 should be booked in advance. The driver's lunch is at your charge and is not "
         "priced in this quotation: the simplest solution is to include it in your own booking, at the "
         "refectory or at the restaurant you choose. The service is a day trip, so no overnight stay "
         "is needed."),
        ("<b>The weather.</b> La Verna stands at about 1,100 metres: at the end of April, even on a fine "
         "day in Florence, it is noticeably cooler up there and there may be fog. It is worth telling "
         "the group to bring a jacket and comfortable shoes for the paths around the sanctuary."),
        ("<b>Number of people.</b> The Beluga has 25 passenger seats plus the guide seat: with 25 people "
         "it is full, leaving only the seat next to the driver for a guide or tour leader, if any. If "
         "the group grows, please let us know before confirming."),
        ("<b>To confirm we need</b> the final number of passengers, the name and mobile number of a "
         "contact person for the day of the service and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free on 27 April 2027 and we hold "
         "it for you until 30 October 2026, the validity date of this quotation; the booking becomes firm "
         "on receipt of the deposit. Cancellation is free up to 60 days before the service; from 60 to 30 "
         "days the deposit is retained; from 30 to 10 days 50% of the amount is charged, and the full "
         "amount in the last 10 days."),
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
                             textColor=GREEN, leading=15, spaceBefore=13, spaceAfter=6,
                             keepWithNext=1),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Alexandra Lange")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Firenze_La_Verna_27_aprile_2027_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

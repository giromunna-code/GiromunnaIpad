#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la trasferta Montecatini Terme - Siena
della partita di basket di domenica 27 settembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_basket_siena.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_basket_siena.py --lingua en --cliente "Client Name"
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

# Le iniziali del riferimento vanno cambiate con quelle del cliente appena si sa
# chi intesta la trasferta: --rif GM-2026-0927-XX
RIF = "GM-2026-0927-BS"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferta per la partita di basket a Siena  ·  Montecatini Terme → Siena e ritorno  ·  domenica 27 settembre 2026",
    meta="Preparato per %s  ·  17 settembre 2026  ·  Rif. %s",
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per tutto il gruppo, con lo stesso conducente dalla partenza al rientro.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Fino a 26 persone viaggiano insieme su un mezzo solo, andata e ritorno, senza cambi e senza mezzi di appoggio. "
        "I sedili reclinabili contano sul rientro in nottata, e il vano bagagli porta senza problemi sacche, palloni e "
        "materiale. Con i suoi 7,64 metri il Beluga sta sotto gli otto metri: arriva ai piazzali del palasport e alle "
        "aree di sosta riservate dove un autobus gran turismo non entra e deve fermarsi lontano."
    ),
    h_servizio="Il servizio",
    svc_head=["Momento", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Dom 27 set<br/>andata",
         "<b>Montecatini Terme → palasport di Siena.</b> "
         "Ritrovo alle 17:15 nel punto che ci indicate, partenza alle 17:30. Circa 110 km per l'A11 e il raccordo "
         "Firenze-Siena, un'ora e quaranta di viaggio, arrivo al palasport verso le 19:10: un'ora abbondante prima "
         "della palla a due delle 20:30.",
         "circa 17:15 – 19:15"),
        ("Dom 27 set<br/>partita",
         "<b>Attesa a Siena per tutta la durata della partita.</b> "
         "Mezzo e conducente restano nell'area di sosta del palasport a vostra disposizione: nessuno deve pensare a "
         "come rientrare e le borse possono restare a bordo. Al termine ci si ritrova al mezzo con calma.",
         "circa 19:15 – 23:00"),
        ("Dom 27 set<br/>ritorno",
         "<b>Palasport di Siena → Montecatini Terme.</b> "
         "Ripartenza verso le 23:00, mezz'ora dopo la fine della partita, per lasciare il tempo di uscire dal "
         "palasport senza corse. Rientro a Montecatini verso le 00:40, al punto di partenza.",
         "circa 23:00 – 00:45"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Dom 27 set — Montecatini Terme → Siena, attesa per tutta la partita, rientro a Montecatini "
         "(circa 220 km, mezzo impegnato fino a nove ore)", "€ 1.200,00", "+ IVA 10%"),
        ("Vitto del conducente durante l'attesa serale", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.200,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.320,00.",
    perhead="Viaggiando in 26 sono circa € 51,00 a persona, andata e ritorno.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggio del mezzo a Siena, assicurazione completa, "
        "carico di sacche e materiale e l'attesa a Siena per tutta la durata della partita entro gli orari indicati. "
        "Non sono dovuti oneri di accesso: il palasport di Siena si trova fuori dalle mura, quindi non serve il "
        "permesso comunale per i bus turistici."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il vitto del conducente, che resta a vostro carico. I biglietti della partita. Attesa oltre gli orari "
        "concordati, € 50,00 all'ora. Rientro a Montecatini dopo le 02:00, € 250,00. Soste, deviazioni o riprese "
        "aggiuntive rispetto al percorso qui descritto, quotate su richiesta. L'eventuale permesso comunale per "
        "entrare nel centro storico di Siena, circa € 160,00, se voleste una sosta dentro le mura."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 396,00", "IVA inclusa"),
        ("Saldo, entro il 25 settembre 2026", "€ 924,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>L'orario della partita.</b> È il dato su cui gira tutto e ci manca: sappiamo che si gioca in serata e "
         "abbiamo costruito il programma sulla palla a due delle 20:30, l'orario serale più frequente. Mandateci "
         "l'orario esatto e fissiamo gli orari su quello, senza variazioni di prezzo: se per esempio si giocasse "
         "alle 18:00, la partenza da Montecatini si sposterebbe alle 15:00 e il rientro sarebbe intorno alle 22:15."),
        ("<b>Il rientro dopo le 02:00.</b> Con gli orari qui sopra si rientra ampiamente prima e non c'è alcun "
         "supplemento. Va tenuto d'occhio solo se dopo la partita volete fermarvi a mangiare o se la gara va per le "
         "lunghe: oltre le 02:00 scatta un supplemento di € 250,00. Se pensate a una sosta dopo la partita ditecelo "
         "adesso, così la mettiamo in programma e vi diciamo subito come cambia il rientro."),
        ("<b>Dove si ferma il mezzo a Siena.</b> Abbiamo quotato il palasport di Siena, fuori dalle mura: "
         "confermateci l'impianto esatto e, se lo conoscete, il punto di discesa. Per le partite serali con un gruppo "
         "organizzato capita che la società o le forze dell'ordine indichino un'area di sosta obbligata per il "
         "pullman: se è il vostro caso segnalatecelo prima, così il conducente arriva già con le istruzioni giuste. "
         "Il Beluga, sotto gli otto metri, sta in spazi dove un gran turismo non entra."),
        ("<b>Il centro storico di Siena.</b> Se prima della partita voleste una sosta dentro le mura, l'ingresso di "
         "un bus turistico richiede il permesso del Comune, circa € 160,00, da chiedere in anticipo e non ottenibile "
         "in giornata. Fatecelo sapere entro la conferma: fuori dalle mura, invece, ci muoviamo liberamente."),
        ("<b>Il vitto del conducente.</b> Durante la partita il conducente resta a Siena per circa quattro ore: la "
         "sua cena è a vostro carico, come d'uso, e l'organizzate voi. Il modo più semplice è farlo mangiare con il "
         "gruppo o lasciargli un buono. <b>Non serve invece alcun pernottamento:</b> si rientra in nottata e la "
         "nostra base di Ponte Buggianese è a quindici chilometri da Montecatini."),
        ("<b>Quante persone e quanto materiale.</b> Il Beluga ha 26 posti passeggeri più l'autista. Confermateci il "
         "numero definitivo dei partecipanti e diteci se viaggiano borse, sacche, palloni, materiale sanitario o "
         "striscioni e tamburi: entrano nel vano bagagli, ma sapendolo prima organizziamo il carico e i tempi di "
         "salita. Se doveste superare i 26 partecipanti avvisateci subito, perché servirebbe un secondo minibus e va "
         "concordato prima."),
        ("<b>Punto di ritrovo e un recapito.</b> Ci servono l'indirizzo esatto del ritrovo a Montecatini Terme e un "
         "numero di telefono o WhatsApp della persona che viaggia con il gruppo, per tenerci in contatto la sera "
         "della partita."),
        ("<b>Disponibilità e cancellazione.</b> Alla partita mancano dieci giorni: il mezzo oggi è libero e ve lo "
         "teniamo per tutta la validità di questo preventivo, ma una domenica sera di campionato è una data "
         "richiesta e non possiamo bloccarla a lungo. La prenotazione diventa definitiva alla ricezione dell'acconto. "
         "La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene trattenuto "
         "l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. "
         "Oggi la prenotazione ricade nella fascia da 30 a 10 giorni e dal 18 settembre entra negli ultimi dieci "
         "giorni. Preventivo valido fino al 21 settembre 2026."),
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
    subtitle="Away trip for the basketball game in Siena  ·  Montecatini Terme → Siena and back  ·  Sunday 27 September 2026",
    meta="Prepared for %s  ·  17 September 2026  ·  Ref. %s",
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for the whole group, with the same driver from departure to return.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "Up to 26 people travel together in a single vehicle, there and back, with no changes and no support car. "
        "The reclining seats count on a late-night return, and the hold takes kit bags, balls and equipment without "
        "difficulty. At 7.64 m the Beluga stays under eight metres: it reaches the arena forecourt and the reserved "
        "parking areas a full-size coach cannot enter, where a coach has to stop further away."
    ),
    h_servizio="The service",
    svc_head=["Stage", "Route", "Vehicle engaged"],
    svc=[
        ("Sun 27 Sep<br/>outward",
         "<b>Montecatini Terme → Siena arena.</b> "
         "Meeting point 17:15 at the address you give us, departure at 17:30. About 110 km along the A11 and the "
         "Florence-Siena link road, one hour and forty minutes, reaching the arena around 19:10 — a good hour before "
         "the 20:30 tip-off.",
         "approx. 17:15 – 19:15"),
        ("Sun 27 Sep<br/>game",
         "<b>Waiting in Siena for the whole game.</b> "
         "Vehicle and driver stay in the arena parking area at your disposal: nobody has to think about getting back "
         "and bags can stay on board. Afterwards you make your way to the vehicle without rushing.",
         "approx. 19:15 – 23:00"),
        ("Sun 27 Sep<br/>return",
         "<b>Siena arena → Montecatini Terme.</b> "
         "Departure around 23:00, half an hour after the final buzzer, to allow time to leave the arena unhurried. "
         "Back in Montecatini around 00:40, at the same meeting point.",
         "approx. 23:00 – 00:45"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sun 27 Sep — Montecatini Terme → Siena, waiting throughout the game, return to Montecatini "
         "(about 220 km, vehicle engaged up to nine hours)", "€ 1,200.00", "+ VAT 10%"),
        ("Driver's meal during the evening wait", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,200.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,320.00.",
    perhead="With 26 travelling that is about € 51.00 per person, return trip included.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, parking in Siena, full insurance, loading of bags and equipment, "
        "and waiting in Siena for the whole game within the times set out here. No access charges apply: the Siena "
        "arena lies outside the city walls, so the municipal permit for tourist coaches is not required."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meal, which remains at your charge. Match tickets. Waiting beyond the agreed times, € 50.00 per "
        "hour. Return to Montecatini after 02:00, € 250.00. Additional stops, detours or pick-ups beyond the route "
        "described here, quoted on request. Any municipal permit to enter the historic centre of Siena, about "
        "€ 160.00, should you want a stop inside the walls."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 396.00", "VAT included"),
        ("Balance, by 25 September 2026", "€ 924.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The tip-off time.</b> Everything turns on it and we do not have it yet: we know the game is in the "
         "evening and have built the programme around a 20:30 tip-off, the most common evening slot. Send us the "
         "exact time and we will set the schedule against it at no change in price: if the game were at 18:00, for "
         "instance, departure from Montecatini would move to 15:00 and the return would be around 22:15."),
        ("<b>Returning after 02:00.</b> With the times above you are back well before then and no surcharge applies. "
         "It only needs watching if you want to stop for a meal after the game or if the game runs long: after 02:00 "
         "a supplement of € 250.00 applies. If you are thinking of a stop afterwards, tell us now so we can build it "
         "into the programme and show you straight away how the return changes."),
        ("<b>Where the vehicle stops in Siena.</b> We have quoted the Siena arena, outside the city walls: please "
         "confirm the exact venue and, if you know it, the drop-off point. For evening games with an organised group "
         "the club or the police sometimes assign a compulsory parking area for the bus: if that applies to you, let "
         "us know in advance so the driver arrives with the right instructions. The Beluga, under eight metres, fits "
         "where a full-size coach does not."),
        ("<b>The historic centre of Siena.</b> Should you want a stop inside the walls before the game, taking a "
         "tourist coach in requires the municipal permit, about € 160.00, applied for in advance and not obtainable "
         "on the day. Let us know by confirmation; outside the walls we move freely."),
        ("<b>The driver's meal.</b> During the game the driver stays in Siena for about four hours: his dinner is at "
         "your charge, as is standard, and you arrange it. The simplest thing is to have him eat with the group or "
         "give him a voucher. <b>No overnight stay is needed:</b> we return the same night and our base at Ponte "
         "Buggianese is fifteen kilometres from Montecatini."),
        ("<b>How many people and how much kit.</b> The Beluga has 26 passenger seats plus the driver. Please confirm "
         "the final number of participants and tell us whether bags, kit bags, balls, medical equipment or banners "
         "and drums are travelling: they fit in the hold, but knowing in advance lets us plan the loading and the "
         "boarding time. If you go beyond 26 participants, tell us at once: a second minibus would be needed and has "
         "to be arranged beforehand."),
        ("<b>Meeting point and a contact number.</b> We need the exact meeting address in Montecatini Terme and a "
         "mobile or WhatsApp number for the person travelling with the group, so we can stay in touch on the evening "
         "of the game."),
        ("<b>Availability and cancellation.</b> The game is ten days away: the vehicle is free today and we hold it "
         "for you for the whole validity of this quotation, but a Sunday evening in the season is a date in demand "
         "and we cannot block it for long. The booking becomes firm on receipt of the deposit. Cancellation is free "
         "of charge more than 60 days before the service; from 60 to 30 days the deposit is retained; from 30 to 10 "
         "days 50% of the price is charged; in the last 10 days, 100%. Today the booking falls in the 30-to-10-day "
         "band, and from 18 September it moves into the last ten days. Quotation valid until 21 September 2026."),
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


def build(lang, cliente, out, rif=RIF):
    L = IT if lang == "it" else EN
    S = styles()
    w, _ = A4
    usable = w - 2 * MARGIN

    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=TOP, bottomMargin=BOTTOM,
                          title="GiroMunna %s %s" % (L["title"], rif),
                          author="GiroMunna")
    frame = Frame(MARGIN, BOTTOM, usable, A4[1] - TOP - BOTTOM, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=make_chrome(L))])

    F = []
    F.append(Paragraph(L["title"], S["title"]))
    F.append(Paragraph(L["subtitle"], S["subtitle"]))
    F.append(Paragraph(L["meta"] % (cliente, rif), S["meta"]))

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Gruppo trasferta basket")
    ap.add_argument("--rif", dest="rif", default=RIF,
                    help="riferimento del preventivo, per es. GM-2026-0927-XX")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Trasferta_Basket_Siena_27_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name, a.rif))

#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il servizio navetta a Villa Cini (Bucine),
26-29 maggio 2027.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_villa_cini.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_villa_cini.py --lingua en --cliente "Client Name"
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

RIF = "GM-2027-0526-VC"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Servizio navetta a Villa Cini, Bucine (AR)  ·  26-29 maggio 2027",
    meta="Preparato per %s  ·  15 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="I mezzi",
    mezzo_intro="Due pullman a noleggio per il vostro gruppo, scelti per la strada di accesso a Villa Cini.",
    mezzo_bullet=(
        "<b>Due pullman da 25 e 27 posti passeggeri più il conducente</b>, forniti da Tuscany T.O. & "
        "Munna Bus Operator (Montecatini Terme). Le dimensioni non sono casuali: l'ultimo tratto di accesso "
        "a Villa Cini, circa 800 metri, non è asfaltato, e il pullman gran turismo da 51 posti inizialmente "
        "previsto non può percorrerlo. I due mezzi più piccoli entrano senza difficoltà."
    ),
    mezzo_close=(
        "I due mezzi lavorano insieme nelle giornate con più movimento — l'arrivo principale del 27 maggio e "
        "il giorno della cerimonia il 28 — mentre uno solo basta per le corse più leggere del 26 e del 29."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Mer 26 mag",
         "<b>Stazione di Bucine → alloggi (Villa Cini e dintorni).</b> Primo ritiro alle 15:00, ultimo alle "
         "23:00: un mezzo resta a disposizione per tutta la finestra, accompagnando agli alloggi gli ospiti "
         "in arrivo in treno.",
         "15:00 – 23:00, un mezzo"),
        ("Gio 27 mag",
         "<b>Stazione di Bucine → alloggi, cinque corse nella giornata.</b> Primo ritiro alle 10:00, ultimo "
         "alle 23:00: è la giornata di arrivo principale, tredici ore di disponibilità in cui i due mezzi "
         "fanno la spola più volte fra la stazione e gli alloggi, scaglionando gli arrivi.",
         "10:00 – 23:00, due mezzi"),
        ("Ven 28 mag",
         "<b>Alloggi → Villa Cini → alloggi.</b> Primo ritiro alle 16:15 per la cerimonia, ultimo alle 24:00 "
         "per il rientro dalla festa: i due mezzi restano a disposizione per tutta la serata.",
         "16:15 – 00:00, due mezzi"),
        ("Sab 29 mag",
         "<b>Alloggi → stazione di Bucine.</b> Un'unica corsa di ritiro e riconsegna alle 11:00, la stessa "
         "stazione usata per gli arrivi.",
         "ore 11:00, due mezzi"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Mer 26 mag — arrivo, stazione di Bucine → alloggi (15:00 – 23:00)", "€ 650,00", "+ IVA 10%"),
        ("Gio 27 mag — arrivi, stazione di Bucine ↔ alloggi (10:00 – 23:00)", "€ 2.800,00", "+ IVA 10%"),
        ("Ven 28 mag — cerimonia a Villa Cini (16:15 – 00:00)", "€ 1.600,00", "+ IVA 10%"),
        ("Sab 29 mag — partenza, alloggi → stazione di Bucine (ore 11:00)", "€ 1.200,00", "+ IVA 10%"),
        ("Vitto e alloggio dei due conducenti, 3 notti (26, 27 e 28 maggio)",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 6.250,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 6.875,00.",
    perhead=(
        "Sono circa € 107,00 a persona sul gruppo di circa 64 ospiti indicato; la cifra si aggiorna se il "
        "numero finale cambia."
    ),
    h_incluso="Incluso.",
    incluso=(
        "Due mezzi e conducenti, carburante, pedaggi, parcheggi, assicurazione completa. Attesa gratuita fino "
        "a 90 minuti dall'orario di arrivo del treno sulle corse del 26 e del 27 maggio, per quanto il treno "
        "sia in ritardo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio dei due conducenti per le notti del 26, 27 e 28 maggio, a vostro carico: la "
        "prenotazione e il pagamento li curate voi direttamente. Attesa oltre gli orari qui indicati, "
        "€ 50,00 all'ora per mezzo. Eventuali corse aggiuntive, se gli alloggi risultassero più sparsi di "
        "quanto previsto, da confermare quando le prenotazioni saranno definitive. Rientro dopo le 02:00, "
        "€ 250,00 per mezzo."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 2.000,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 4.875,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>La strada di accesso a Villa Cini.</b> Gli ultimi 800 metri non sono asfaltati: per questo "
         "abbiamo previsto i due mezzi da 25 e 27 posti invece del pullman da 51. Vi chiediamo comunque di "
         "farvi confermare dalla struttura il punto esatto di discesa e lo spazio di manovra, così lo "
         "verifichiamo prima del 26 maggio."),
        ("<b>Gli alloggi non sono ancora definitivi.</b> Il prezzo è costruito su un servizio a raggiera "
         "nella zona di Bucine, fra Palazzo Vanneschi e le nove strutture che avete indicato. Se le "
         "prenotazioni finali risultassero più sparse nel territorio potrebbero servire corse aggiuntive o "
         "un adeguamento del prezzo: fatecelo sapere appena i vostri ospiti avranno confermato dove alloggiano."),
        ("<b>Le cinque corse del 27 maggio.</b> Con circa 64 ospiti attesi e 52 posti complessivi sui due "
         "mezzi, nessuna corsa porta tutti insieme: è normale scaglionare gli arrivi nelle tredici ore fra le "
         "10:00 e le 23:00, e il prezzo lo prevede già. Se ci mandate gli orari dei treni possiamo organizzare "
         "le corse in anticipo."),
        ("<b>L'ultimo ritiro del 28 maggio, a mezzanotte.</b> Se le corse di rientro agli alloggi dopo "
         "l'ultimo ritiro si protraggono oltre le 02:00, si applica il supplemento per rientro notturno "
         "indicato sotto, € 250,00 per mezzo. Fatecelo sapere se prevedete che la festa finisca più tardi, "
         "così lo teniamo in conto fin da ora."),
        ("<b>Vitto e alloggio dei due conducenti.</b> Le notti del 26, 27 e 28 maggio restano a vostro "
         "carico: la prenotazione e il pagamento li curate voi direttamente. La soluzione più comoda è "
         "sistemarli a Palazzo Vanneschi o in una struttura vicina a Villa Cini."),
        ("<b>Per confermare ci servono</b> il numero definitivo degli ospiti (o almeno una stima "
         "aggiornata), gli orari dei treni in arrivo il 26 e il 27 maggio, l'orario effettivo di fine della "
         "festa del 28 per organizzare il rientro serale, e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> I due mezzi sono al momento liberi e li teniamo a vostra "
         "disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla "
         "ricezione dell'acconto. Cancellazione gratuita oltre 60 giorni prima del servizio; da 60 a 30 "
         "giorni si trattiene l'acconto; da 30 a 10 giorni il 50%; negli ultimi 10 giorni il 100%. "
         "Preventivo valido fino al 29 settembre 2026."),
    ],
    closing=("Restiamo a disposizione per qualsiasi chiarimento e in attesa di un vostro riscontro.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Giuseppe Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Shuttle service to Villa Cini, Bucine (AR)  ·  26-29 May 2027",
    meta="Prepared for %s  ·  15 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicles",
    mezzo_intro="Two hired coaches for your group, chosen for Villa Cini's access road.",
    mezzo_bullet=(
        "<b>Two coaches, 25 and 27 passenger seats plus driver</b>, supplied by Tuscany T.O. & Munna Bus "
        "Operator (Montecatini Terme). The sizes are not incidental: the final 800 metres of the access road "
        "to Villa Cini are unpaved, and the 51-seat coach originally planned cannot get through. The two "
        "smaller vehicles manage it without difficulty."
    ),
    mezzo_close=(
        "The two vehicles work together on the busier days — the main arrival on 27 May and the ceremony day "
        "on the 28th — while a single one covers the lighter runs on the 26th and the 29th."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Wed 26 May",
         "<b>Bucine train station → accommodations (Villa Cini area).</b> First pickup at 3:00 pm, last at "
         "11:00 pm: one coach stays at your disposal for the whole window, taking guests arriving by train "
         "to their accommodation.",
         "3:00 pm – 11:00 pm, one coach"),
        ("Thu 27 May",
         "<b>Bucine train station → accommodations, five runs during the day.</b> First pickup at 10:00 am, "
         "last at 11:00 pm: this is the main arrival day, thirteen hours of availability in which the two "
         "coaches shuttle back and forth between the station and the accommodations several times, "
         "staggering arrivals.",
         "10:00 am – 11:00 pm, two coaches"),
        ("Fri 28 May",
         "<b>Accommodations → Villa Cini → accommodations.</b> First pickup at 4:15 pm for the ceremony, "
         "last at midnight for the return from the party: the two coaches stay at your disposal for the "
         "whole evening.",
         "4:15 pm – midnight, two coaches"),
        ("Sat 29 May",
         "<b>Accommodations → Bucine train station.</b> A single pickup and drop-off at 11:00 am, the same "
         "station used for arrivals.",
         "11:00 am, two coaches"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Wed 26 May — arrival, Bucine station → accommodations (3:00 pm – 11:00 pm)", "€ 650.00", "+ VAT 10%"),
        ("Thu 27 May — arrivals, Bucine station ↔ accommodations (10:00 am – 11:00 pm)", "€ 2,800.00", "+ VAT 10%"),
        ("Fri 28 May — ceremony at Villa Cini (4:15 pm – midnight)", "€ 1,600.00", "+ VAT 10%"),
        ("Sat 29 May — departure, accommodations → Bucine station (11:00 am)", "€ 1,200.00", "+ VAT 10%"),
        ("Drivers' board and lodging, 3 nights (26, 27 and 28 May)",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 6,250.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 6,875.00.",
    perhead=(
        "That is about € 107.00 per person for the group of roughly 64 guests indicated; the figure will be "
        "updated if the final headcount changes."
    ),
    h_incluso="Included.",
    incluso=(
        "Two vehicles and drivers, fuel, tolls, parking, full insurance. Free waiting time of up to 90 "
        "minutes from the train's actual arrival time on the 26 and 27 May runs, however late the train runs."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The drivers' board and lodging for the nights of 26, 27 and 28 May, at your charge: you book and "
        "pay for them directly. Waiting beyond the times set out here, € 50.00 per hour per vehicle. Any "
        "additional runs, should the accommodations turn out to be more scattered than expected, to be "
        "confirmed once bookings are final. Return after 2:00 am, € 250.00 per vehicle."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 2,000.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 4,875.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The access road to Villa Cini.</b> The final 800 metres are unpaved: that is why we have "
         "planned the two coaches, 25 and 27 seats, instead of the 51-seat coach. Please still have the "
         "venue confirm the exact drop-off point and manoeuvring space, so we can verify it before 26 May."),
        ("<b>Accommodations are not yet final.</b> The price is built on a hub-and-spoke shuttle service "
         "around the Bucine area, between Palazzo Vanneschi and the nine properties you listed. If the final "
         "bookings turn out to be more spread out across the area, additional runs or a price adjustment may "
         "be needed: let us know as soon as your guests have confirmed where they are staying."),
        ("<b>The five runs on 27 May.</b> With around 64 guests expected and 52 seats total across the two "
         "coaches, no single run carries everyone at once: staggering arrivals across the thirteen hours "
         "between 10:00 am and 11:00 pm is normal, and the price already accounts for it. If you send us "
         "the train times we can plan the runs in advance."),
        ("<b>The last pickup on 28 May, at midnight.</b> If the return runs to the accommodations after "
         "the last pickup run past 2:00 am, the night-return surcharge below applies, € 250.00 per vehicle. "
         "Let us know if you expect the party to run later, so we can account for it now."),
        ("<b>The drivers' board and lodging.</b> The nights of 26, 27 and 28 May remain at your charge: you "
         "book and pay for them directly. The easiest solution is to put them up at Palazzo Vanneschi or "
         "another property near Villa Cini."),
        ("<b>To confirm we need</b> the final guest count (or at least an updated estimate), the train "
         "times arriving on 26 and 27 May, the actual finishing time of the party on the 28th to plan the "
         "evening return, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The two vehicles are currently free and we hold them for "
         "you for the whole validity of this quotation; the booking becomes firm on receipt of the deposit. "
         "Cancellation is free of charge more than 60 days before the service; from 60 to 30 days the "
         "deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. "
         "Quotation valid until 29 September 2026."),
    ],
    closing=("We remain at your disposal for any clarification and look forward to hearing from you.<br/><br/>"
             "Kind regards,<br/>"
             "Giuseppe Munna — GiroMunna NCC, Tuscany · +39 335 587 4744 · info@giromunna.com"),
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

    # --- mezzi
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Jenna Bowman")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Villa_Cini_26-29_maggio_2027_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

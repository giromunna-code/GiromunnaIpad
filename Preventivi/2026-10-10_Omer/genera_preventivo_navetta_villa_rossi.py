#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la navetta ospiti Lucca – Villa Rossi, sabato 10 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_navetta_villa_rossi.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_navetta_villa_rossi.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1010-FO"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Navetta ospiti Lucca – Villa Rossi per il matrimonio  ·  sabato 10 ottobre 2026",
    meta="Preparato per %s  ·  5 ottobre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus con conducente che fa la spola fra il centro di Lucca e Villa Rossi: due corse "
        "all'andata e tre al ritorno, per portare i 40 ospiti alla villa e riportarli in città a fine serata."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "<b>Il minibus ha 26 posti, quindi i 40 ospiti non stanno in un'unica corsa:</b> all'andata servono "
        "due viaggi. Per questo la prima partenza è anticipata alle 12:15, in modo che la seconda resti alle "
        "12:50 come avete chiesto. Con meno di 8 metri di lunghezza, il Beluga entra nel parco della villa e "
        "lascia gli ospiti davanti all'ingresso, senza che debbano camminare in abito da cerimonia."
    ),
    h_servizio="Il servizio",
    svc_head=["Sab 10 ott", "Percorso", "Partenza"],
    svc=[
        ("Andata, 1ª corsa",
         "<b>Lucca centro → Villa Rossi</b> (Via di Villa Altieri 1672). Fino a 26 ospiti. "
         "Circa 5 km, arrivo verso le 12:30.",
         "12:15"),
        ("Andata, 2ª corsa",
         "<b>Lucca centro → Villa Rossi.</b> Gli ospiti restanti, 14 su 40. Arrivo verso le 13:05.",
         "12:50"),
        ("Ritorno, 1ª corsa",
         "<b>Villa Rossi → Lucca centro.</b> Fino a 26 ospiti. Arrivo verso le 21:15.",
         "21:00"),
        ("Ritorno, 2ª corsa",
         "<b>Villa Rossi → Lucca centro.</b> Fino a 26 ospiti. Arrivo verso le 21:45.",
         "21:30"),
        ("Ritorno, 3ª corsa",
         "<b>Villa Rossi → Lucca centro.</b> Gli ultimi ospiti. Arrivo verso le 22:15.",
         "22:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Beluga con conducente — navetta Lucca – Villa Rossi, 2 corse di andata e 3 di ritorno",
         "€ 900,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 900,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 990,00.",
    perhead="Sono € 24,75 a ospite per andata e ritorno, IVA inclusa, su 40 ospiti.",
    h_incluso="Incluso.",
    incluso=(
        "Il minibus con conducente, carburante, pedaggi, parcheggi e assicurazione completa. Tutte e cinque "
        "le corse indicate. Fra l'andata e il ritorno il mezzo rientra alla base: il conducente non resta in "
        "attesa alla villa e non ci sono pasti o pernottamenti a vostro carico."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre gli orari qui indicati, € 50,00 all'ora. Corse aggiuntive, per esempio un ritorno "
        "dopo le 22:00, quotate su richiesta."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 297,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 693,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Perché 12:15 e non 12:30.</b> Fra Lucca e Villa Rossi ci vogliono circa 15 minuti a tratta, "
         "più il tempo per far salire e scendere gli ospiti: con un solo mezzo un giro completo richiede "
         "circa 35 minuti. Partendo alle 12:30 la seconda corsa non potrebbe lasciare Lucca prima delle "
         "13:05. Anticipando la prima alle 12:15 la seconda parte puntuale alle 12:50."),
        ("<b>Chi sale su quale corsa.</b> Il conducente non può sapere chi deve aspettare. Vi chiediamo di "
         "dividere gli ospiti in anticipo: per esempio, sulla prima corsa di andata gli ospiti che devono "
         "essere alla villa per primi (famiglia degli sposi, testimoni, chi aiuta con i preparativi), sulla "
         "seconda gli altri. Al ritorno le prime corse sono di solito per le famiglie con bambini e gli "
         "ospiti più anziani. Ogni bambino conta come un passeggero: sul minibus non salgono più di 26 "
         "persone per volta."),
        ("<b>Il punto di partenza a Lucca.</b> Il centro storico dentro le Mura è zona a traffico limitato e "
         "il minibus non può entrarvi. Il ritiro e la discesa si fanno appena fuori dalle Mura, in un punto "
         "comodo da raggiungere a piedi: per esempio Piazzale Verdi, a Porta Sant'Anna. Ci serve sapere dove "
         "alloggiano gli ospiti per indicarvi il punto migliore."),
        ("<b>Le corse di ritorno.</b> Il minibus è pronto alla villa per le 21:00. Tre corse a mezz'ora "
         "l'una dall'altra lasciano poco margine: se gli ospiti non sono pronti a salire, le corse "
         "successive partono in ritardo. Vi chiediamo di indicarci una persona che dia al conducente il via "
         "alla partenza. Se la festa si prolunga oltre le 22:00, l'attesa si conteggia a € 50,00 all'ora; una "
         "corsa in più si può aggiungere, ma va concordata prima."),
        ("<b>Per confermare ci servono</b> il numero definitivo degli ospiti, il punto di ritiro a Lucca, il "
         "nome e il cellulare di un referente per il giorno del matrimonio, un indirizzo email e i dati per "
         "la fattura."),
        ("<b>Disponibilità e cancellazione.</b> Il minibus è al momento libero e lo teniamo a vostra "
         "disposizione fino al 7 ottobre 2026, data di validità del preventivo; la prenotazione diventa "
         "definitiva alla ricezione dell'acconto. Mancando meno di 10 giorni al servizio, una volta "
         "confermata la prenotazione la cancellazione comporta l'addebito dell'intero importo."),
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
    subtitle="Wedding guest shuttle Lucca – Villa Rossi  ·  Saturday 10 October 2026",
    meta="Prepared for %s  ·  5 October 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "One minibus with driver shuttling between Lucca city centre and Villa Rossi: two runs on the way "
        "out and three on the way back, to bring the 40 guests to the villa and take them back to town at "
        "the end of the evening."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, reclining "
        "ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "<b>The minibus seats 26, so the 40 guests will not fit in a single run:</b> the outbound trip takes "
        "two rides. For this reason the first departure is moved earlier, to 12:15, so that the second can "
        "still leave at 12:50 as you asked. At under 8 metres long, the Beluga drives into the villa grounds "
        "and drops guests at the entrance, so nobody has to walk in their wedding clothes."
    ),
    h_servizio="The service",
    svc_head=["Sat 10 Oct", "Route", "Departure"],
    svc=[
        ("Outbound, run 1",
         "<b>Lucca centre → Villa Rossi</b> (Via di Villa Altieri 1672). Up to 26 guests. "
         "About 5 km, arriving around 12:30.",
         "12:15"),
        ("Outbound, run 2",
         "<b>Lucca centre → Villa Rossi.</b> The remaining guests, 14 of 40. Arriving around 13:05.",
         "12:50"),
        ("Return, run 1",
         "<b>Villa Rossi → Lucca centre.</b> Up to 26 guests. Arriving around 21:15.",
         "21:00"),
        ("Return, run 2",
         "<b>Villa Rossi → Lucca centre.</b> Up to 26 guests. Arriving around 21:45.",
         "21:30"),
        ("Return, run 3",
         "<b>Villa Rossi → Lucca centre.</b> The last guests. Arriving around 22:15.",
         "22:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Beluga with driver — Lucca – Villa Rossi shuttle, 2 outbound and 3 return runs",
         "€ 900.00", "+ VAT 10%"),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 900.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 990.00.",
    perhead="That is € 24.75 per guest for the round trip, VAT included, across 40 guests.",
    h_incluso="Included.",
    incluso=(
        "The minibus with driver, fuel, tolls, parking and full insurance. All five runs listed above. "
        "Between the outbound and the return runs the vehicle goes back to base: the driver does not wait "
        "at the villa, and there are no meals or overnight stays at your charge."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the times set out here, € 50.00 per hour. Additional runs, such as a return after "
        "22:00, quoted on request."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 297.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 693.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Why 12:15 and not 12:30.</b> The drive between Lucca and Villa Rossi takes about 15 minutes each "
         "way, plus time for guests to get on and off: with a single vehicle a full loop takes about 35 "
         "minutes. Leaving at 12:30, the second run could not leave Lucca before 13:05. Moving the first run "
         "to 12:15 lets the second leave on time at 12:50."),
        ("<b>Who takes which run.</b> The driver cannot know whom to wait for. Please split the guests in "
         "advance: for example, the first outbound run for those who need to be at the villa first (the "
         "couple's families, witnesses, anyone helping with preparations), the second for everyone else. On "
         "the way back the earlier runs usually suit families with children and older guests. Every child "
         "counts as a passenger: no more than 26 people can board at a time."),
        ("<b>The pick-up point in Lucca.</b> The historic centre inside the city walls is a restricted traffic "
         "zone and the minibus cannot enter it. Pick-up and drop-off are just outside the walls, at a point "
         "within easy walking distance: for example Piazzale Verdi, by Porta Sant'Anna. If you tell us where "
         "the guests are staying, we will suggest the best spot."),
        ("<b>The return runs.</b> The minibus is ready at the villa by 21:00. Three runs half an hour apart "
         "leave little margin: if guests are not ready to board, the following runs leave late. Please give "
         "us the name of one person who can tell the driver when to leave. If the party runs past 22:00, "
         "waiting is charged at € 50.00 per hour; an extra run can be added, but must be agreed in advance."),
        ("<b>To confirm we need</b> the final number of guests, the pick-up point in Lucca, the name and mobile "
         "number of a contact person for the wedding day, an email address and your invoicing details."),
        ("<b>Availability and cancellation.</b> The minibus is currently free and we hold it for you until "
         "7 October 2026, the validity date of this quotation; the booking becomes firm on receipt of the "
         "deposit. With less than 10 days to the service, once the booking is confirmed a cancellation is "
         "charged at the full amount."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Ferdi Omer")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Navetta_Villa_Rossi_10_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

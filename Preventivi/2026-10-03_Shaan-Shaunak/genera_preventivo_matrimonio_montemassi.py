#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il servizio matrimonio del 3 ottobre 2026,
Montemassi - Ribolla - Conti di San Bonifacio Wine Resort (Gavorrano, GR).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_matrimonio_montemassi.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_matrimonio_montemassi.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1003-SS"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Servizio matrimonio · Montemassi – Ribolla – Conti di San Bonifacio Wine Resort (Gavorrano, GR)  ·  sabato 3 ottobre 2026",
    meta="Preparato per %s  ·  15 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo, fino a 25 persone, con lo stesso conducente per l'intera giornata del matrimonio.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 25 ospiti a bordo resta un solo posto libero: il Beluga copre comodamente il gruppo al completo. "
        "Sotto la soglia degli 8 metri, raggiunge senza difficoltà le strade di collina della Maremma e il "
        "piazzale della tenuta, dove un autobus gran turismo troverebbe più difficoltà a manovrare."
    ),
    h_servizio="Il servizio",
    svc_head=["Quando", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Sab 3 ott, ore 14:00",
         "<b>Montemassi → Ribolla → Conti di San Bonifacio Wine Resort (Gavorrano).</b> "
         "Ritrovo alle 14:00 a Montemassi; transfer di andata fino alla struttura via Ribolla, arrivo previsto "
         "verso le 14:30. Mezzo e conducente restano in zona, a vostra disposizione, per tutta la cerimonia e "
         "il ricevimento.",
         "circa 13:30 – 14:30"),
        ("Sab 3 ott, ore 01:00",
         "<b>Conti di San Bonifacio → Ribolla → Montemassi.</b> Rientro notturno: ritrovo all'1:00 alla "
         "struttura, transfer di ritorno via Ribolla fino a Montemassi, arrivo previsto entro le 01:30 se la "
         "partenza rispetta l'orario concordato.",
         "circa 01:00 – 01:30"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 3 ott — Montemassi → Conti di San Bonifacio via Ribolla, transfer di andata e rientro notturno",
         "€ 2.300,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente, 1 notte (3 ottobre)", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.300,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.530,00.",
    perhead="Sono circa € 101,00 a persona, su 25 ospiti.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggi, assicurazione completa. Il "
        "posizionamento del mezzo dalla nostra base fino a Montemassi e ritorno, e l'impegno del mezzo per "
        "l'intera giornata del 3 ottobre, compreso il periodo fra il transfer di andata e il rientro notturno. "
        "Nessun onere di accesso: il percorso non tocca aeroporti né centri storici soggetti a ZTL o a permesso "
        "comunale."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio del conducente per la notte del 3 ottobre, che restano a vostro carico: la "
        "prenotazione e il pagamento li curate voi direttamente. Attesa oltre gli orari concordati, € 50,00 "
        "all'ora per mezzo. Rientro del mezzo a Montemassi dopo le 02:00, € 250,00 per mezzo — vedi la nota "
        "sull'orario del rientro. Addobbi o allestimenti particolari del mezzo, su richiesta."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 759,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.771,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>L'orario dell'una di notte per il rientro.</b> È molto vicino alla soglia delle 02:00 oltre la "
         "quale scatta il supplemento di rientro notturno di € 250,00 per mezzo. Con un transfer di 20-25 minuti "
         "da Conti di San Bonifacio a Montemassi via Ribolla, si rientra entro le 02:00 solo se la partenza reale "
         "rispetta l'orario concordato: ai matrimoni gli sposi e gli ospiti ritardano spesso. Vi chiediamo di "
         "avvisare il conducente per tempo se prevedete uno slittamento, altrimenti il supplemento è dovuto."),
        ("<b>Vitto e alloggio del conducente.</b> La nostra base è a Ponte Buggianese, circa 150 km da "
         "Montemassi. Fra il transfer del pomeriggio e il rientro all'una di notte corrono undici ore: il "
         "conducente deve riposare in zona prima di rimettersi alla guida per il rientro, come previsto dalle "
         "norme sui tempi di guida e di riposo. La notte del 3 ottobre resta a vostro carico e la prenotate e "
         "pagate voi direttamente: basta una camera singola in zona. La soluzione più comoda è sistemarlo nella "
         "stessa struttura del gruppo, se c'è disponibilità."),
        ("<b>Numero esatto degli ospiti.</b> Avete indicato fino a 25 persone: con il Beluga il margine è di un "
         "solo posto. Vi chiediamo il numero definitivo prima della conferma, per essere certi che il mezzo "
         "basti o valutare per tempo un'alternativa."),
        ("<b>Accesso a Conti di San Bonifacio.</b> È una tenuta in collina, in località Casteani. Vi chiediamo "
         "di farvi confermare dalla struttura il punto esatto di discesa e salita degli ospiti e lo spazio di "
         "manovra per un mezzo di 7,64 m, soprattutto per la manovra notturna dell'una di notte: molto meglio "
         "chiarirlo ora che la sera stessa."),
        ("<b>Per confermare ci servono</b> il numero definitivo degli ospiti, un recapito telefonico o WhatsApp "
         "della persona presente il giorno del matrimonio, l'indirizzo esatto del punto di ritrovo a Montemassi "
         "e i vostri dati di fatturazione."),
        ("<b>Disponibilità, validità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione per la validità di questo preventivo; la prenotazione diventa definitiva alla ricezione "
         "dell'acconto. Mancando oggi 18 giorni al servizio, la prenotazione ricade già nella fascia da 30 a 10 "
         "giorni, in cui la cancellazione comporta l'addebito del 50% del prezzo; dal 23 settembre, a 10 giorni "
         "dal servizio, passerà nella fascia del 100%. Vista la vicinanza della data vi consigliamo di "
         "confermare al più presto. Preventivo valido fino al 22 settembre 2026."),
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
    subtitle="Wedding service · Montemassi – Ribolla – Conti di San Bonifacio Wine Resort (Gavorrano, GR)  ·  Saturday 3 October 2026",
    meta="Prepared for %s  ·  15 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group, up to 25 people, with the same driver for the whole wedding day.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 25 guests on board only one seat stays free: the Beluga comfortably covers the full group. "
        "At under 8 metres it easily reaches the hill roads of the Maremma and the estate's courtyard, where a "
        "full-size coach would struggle to manoeuvre."
    ),
    h_servizio="The service",
    svc_head=["When", "Route", "Vehicle engaged"],
    svc=[
        ("Sat 3 Oct, 14:00",
         "<b>Montemassi → Ribolla → Conti di San Bonifacio Wine Resort (Gavorrano).</b> "
         "Meeting point 14:00 at Montemassi; outbound transfer to the venue via Ribolla, arriving around 14:30. "
         "Vehicle and driver stay in the area, at your disposal, throughout the ceremony and reception.",
         "approx. 13:30 – 14:30"),
        ("Sat 3 Oct, 01:00",
         "<b>Conti di San Bonifacio → Ribolla → Montemassi.</b> Night return: pick-up at 1:00 AM at the venue, "
         "return transfer via Ribolla to Montemassi, arriving by around 01:30 provided departure keeps to the "
         "agreed time.",
         "approx. 01:00 – 01:30"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sat 3 Oct — Montemassi → Conti di San Bonifacio via Ribolla, outbound transfer and night return",
         "€ 2,300.00", "+ VAT 10%"),
        ("Driver's board and lodging, 1 night (3 October)", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,300.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,530.00.",
    perhead="That is about € 101.00 per person, for 25 guests.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, parking, full insurance. Positioning the vehicle from our "
        "base to Montemassi and back, and the vehicle's engagement for the whole day of 3 October, including the "
        "period between the outbound transfer and the night return. No other access charges apply: the route "
        "touches no airport and no historic centre subject to a restricted traffic zone or municipal permit."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's board and lodging for the night of 3 October, which remain at your charge: you book and "
        "pay for them directly. Waiting beyond the agreed times, € 50.00 per hour per vehicle. Return of the "
        "vehicle to Montemassi after 02:00, € 250.00 per vehicle — see the note on the return time. Ribbons or "
        "other special arrangements for the vehicle, on request."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 759.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,771.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The 1:00 AM return time.</b> This sits very close to the 02:00 threshold beyond which the € 250.00 "
         "per vehicle night-return surcharge applies. With a 20-25 minute transfer from Conti di San Bonifacio to "
         "Montemassi via Ribolla, you are back within 02:00 only if the actual departure keeps to the agreed "
         "time — at weddings the couple and guests often run late. Please let the driver know in advance if you "
         "expect a delay, otherwise the surcharge is due."),
        ("<b>The driver's board and lodging.</b> Our base is in Ponte Buggianese, about 150 km from Montemassi. "
         "Eleven hours run between the afternoon transfer and the 1:00 AM return: the driver has to rest in the "
         "area before getting back behind the wheel for the return leg, as required by driving and rest-time "
         "rules. The night of 3 October remains at your charge and you book and pay for it directly: a single "
         "room in the area is all that is needed. The easiest arrangement, if there is availability, is to put "
         "him up at the same property as the group."),
        ("<b>Exact guest count.</b> You have indicated up to 25 people: with the Beluga the margin is a single "
         "seat. Please confirm the final number before booking, so we can be certain the vehicle is enough or "
         "look at an alternative in good time."),
        ("<b>Access at Conti di San Bonifacio.</b> It is a hilltop estate, in Località Casteani. Please have the "
         "venue confirm the exact drop-off and pick-up point and the manoeuvring space for a 7.64 m vehicle, "
         "especially for the 1:00 AM night manoeuvre — far better settled now than on the night itself."),
        ("<b>To confirm we need</b> the final guest count, a mobile or WhatsApp contact for the person on site "
         "on the wedding day, the exact meeting point address in Montemassi, and your invoicing details."),
        ("<b>Availability, validity and cancellation.</b> The vehicle is currently free and we hold it for you "
         "for the validity of this quotation; the booking becomes firm on receipt of the deposit. With 18 days "
         "to the service today, this booking already falls in the 30-to-10-day band, where cancellation carries "
         "a 50% charge; from 23 September, 10 days out, it moves into the 100% band. Given how close the date "
         "is, we recommend confirming as soon as possible. Quotation valid until 22 September 2026."),
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
    cols = [26 * mm, usable - 26 * mm - 25 * mm, 25 * mm]
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Shaan Shaunak")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Matrimonio_Montemassi_3_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

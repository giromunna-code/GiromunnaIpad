#!/usr/bin/env python3
"""
Genera la proforma di pagamento GiroMunna per la giornata aggiuntiva sul Monte
Amiata del 22 agosto 2026, per il gruppo di Anette Haavel (Rif. GM-2026-0822-CF),
nello stesso formato della proforma dell'acconto Corte Francigena.

    python3 genera_proforma_monte_amiata.py --lingua it
    python3 genera_proforma_monte_amiata.py --lingua en
"""

import argparse
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

GREEN = colors.HexColor("#1F4636")
GOLD = colors.HexColor("#C9A24B")
INK = colors.HexColor("#2B2B2B")
MUTED = colors.HexColor("#6B6B6B")
RULE = colors.HexColor("#E4E1D8")
CREAM = colors.HexColor("#F5F3EE")

HERE = os.path.dirname(os.path.abspath(__file__))


def _trova_logo():
    for base in (HERE, os.path.dirname(HERE)):
        p = os.path.join(base, "assets", "giromunna_logo.png")
        if os.path.exists(p):
            return p
    return os.path.join(HERE, "assets", "giromunna_logo.png")


LOGO = _trova_logo()

MARGIN = 20 * mm
TOP = 30 * mm
BOTTOM = 24 * mm

RIF = "GM-2026-0822-CF"

IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    date="21 agosto 2026",
    title="Fattura Proforma",
    subtitle="Saldo  ·  Escursione Monte Amiata, 22 agosto 2026  ·  Rif. " + RIF,
    h_bill="Intestatario",
    bill_rows=[
        ("Società", "ID Production OÜ"),
        ("Codice registro", "11546535"),
        ("Partita IVA", "EE101261777"),
        ("Indirizzo", "Harju maakond, Viimsi vald, Haabneeme alevik, Paadi tee 3, 74001, Estonia"),
        ("Referente", "Anette Haavel  ·  anette@idp.ee  ·  +372 5664 1112"),
    ],
    amount_label="IMPORTO DOVUTO",
    amount="€ 1.815,00",
    amount_desc=(
        "Escursione Monte Amiata (due mezzi) e hotel autisti, sabato 22 agosto 2026, "
        "IVA 10% inclusa.<br/>"
        "Da corrispondere entro oggi, 21 agosto 2026.<br/>"
        "Aggiunta al preventivo Corte Francigena, Rif. GM-2026-0819-CF."
    ),
    h_transfer="Bonifico a",
    transfer_rows=[
        ("Intestatario conto", "Munna Girolamo Giuseppe"),
        ("IBAN", "IT59 O053 4137 0700 0000 0034 24"),
        ("BIC / SWIFT", "BAPPIT21S05"),
        ("Banca", "Banco BPM"),
        ("Filiale", "Viale Castracani 12, 55100 Lucca (LU), Italia"),
        ("Valuta", "EUR"),
        ("Causale", "Saldo - " + RIF + " - Monte Amiata 22 ago 2026"),
    ],
    h_note="Note",
    note_html=(
        "Se la vostra banca è fuori dall'area SEPA, disponete il bonifico con spese a carico "
        "\"OUR\", in modo che l'importo arrivi per intero senza trattenute delle banche "
        "intermediarie.<br/><br/>"
        "Questo è un documento proforma per organizzare il pagamento, non una fattura fiscale. "
        "Emettiamo fattura fiscale alla ricezione del pagamento."
    ),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    date="21 August 2026",
    title="Proforma Invoice",
    subtitle="Balance  ·  Monte Amiata excursion, 22 August 2026  ·  Ref. " + RIF,
    h_bill="Bill to",
    bill_rows=[
        ("Company", "ID Production OÜ"),
        ("Registry code", "11546535"),
        ("VAT number", "EE101261777"),
        ("Address", "Harju maakond, Viimsi vald, Haabneeme alevik, Paadi tee 3, 74001, Estonia"),
        ("Contact", "Anette Haavel  ·  anette@idp.ee  ·  +372 5664 1112"),
    ],
    amount_label="AMOUNT DUE",
    amount="€ 1,815.00",
    amount_desc=(
        "Monte Amiata excursion (two vehicles) and drivers' hotel, Saturday 22 August 2026, "
        "VAT 10% included.<br/>"
        "Payable today, 21 August 2026.<br/>"
        "An addition to the Corte Francigena quotation, Ref. GM-2026-0819-CF."
    ),
    h_transfer="Transfer to",
    transfer_rows=[
        ("Account holder", "Munna Girolamo Giuseppe"),
        ("IBAN", "IT59 O053 4137 0700 0000 0034 24"),
        ("BIC / SWIFT", "BAPPIT21S05"),
        ("Bank", "Banco BPM"),
        ("Branch address", "Viale Castracani 12, 55100 Lucca (LU), Italy"),
        ("Currency", "EUR"),
        ("Reference", "Balance - " + RIF + " - Monte Amiata 22 Aug 2026"),
    ],
    h_note="Please note",
    note_html=(
        "If your bank is outside the SEPA area, please instruct the transfer with charges "
        "\"OUR\", so that the full amount is received without deductions by intermediary "
        "banks.<br/><br/>"
        "This is a proforma document to arrange the payment, not a fiscal invoice. We issue "
        "a fiscal invoice on receipt of payment."
    ),
)


def styles():
    base = dict(fontName="Helvetica", textColor=INK, leading=13.2, fontSize=9.2)
    return {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=21,
                                textColor=GREEN, leading=24, spaceAfter=3),
        "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=10.2,
                                   textColor=INK, leading=14, spaceAfter=16),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.5,
                             textColor=GREEN, leading=13, spaceBefore=4, spaceAfter=2),
        "label": ParagraphStyle("label", fontName="Helvetica", fontSize=8.6,
                                textColor=MUTED, leading=12),
        "value": ParagraphStyle("value", fontName="Helvetica-Bold", fontSize=9.4,
                                textColor=INK, leading=13),
        "amount_label": ParagraphStyle("amount_label", fontName="Helvetica-Bold", fontSize=8.4,
                                       textColor=MUTED, leading=11, spaceAfter=4,
                                       tracking=1),
        "amount_fig": ParagraphStyle("amount_fig", fontName="Helvetica-Bold", fontSize=27,
                                     textColor=GREEN, leading=30),
        "amount_desc": ParagraphStyle("amount_desc", fontName="Helvetica", fontSize=8.8,
                                      textColor=INK, leading=12.6),
        "small": ParagraphStyle("small", alignment=TA_JUSTIFY, fontName="Helvetica",
                                fontSize=8.6, textColor=INK, leading=12.4, **{}),
        "foot": ParagraphStyle("foot", alignment=TA_JUSTIFY, spaceBefore=6, spaceAfter=2,
                               fontName="Helvetica", fontSize=8.2,
                               textColor=MUTED, leading=11.4),
    }


def make_chrome(L):
    def chrome(canvas, doc):
        canvas.saveState()
        w, h = A4
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
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.6)
        canvas.line(MARGIN, BOTTOM - 4 * mm, w - MARGIN, BOTTOM - 4 * mm)
        canvas.setFont("Helvetica", 6.8)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, BOTTOM - 8.5 * mm, L["footer1"])
        canvas.drawString(MARGIN, BOTTOM - 12 * mm, L["footer2"])
        canvas.drawRightString(w - MARGIN, BOTTOM - 12 * mm, L["date"])
        canvas.restoreState()
    return chrome


def build(lang, out):
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

    # --- intestatario
    F.append(Paragraph(L["h_bill"], S["h2"]))
    brows = [[Paragraph(k, S["label"]), Paragraph(v, S["value"])] for k, v in L["bill_rows"]]
    bt = Table(brows, colWidths=[32 * mm, usable - 32 * mm])
    bt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
    ]))
    F.append(bt)
    F.append(Spacer(1, 16))

    # --- importo dovuto
    amt = Table(
        [[Paragraph(L["amount_label"], S["amount_label"])],
         [Paragraph(L["amount"], S["amount_fig"])],
         [Spacer(1, 6)],
         [Paragraph(L["amount_desc"], S["amount_desc"])]],
        colWidths=[usable],
    )
    amt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LINEBEFORE", (0, 0), (0, -1), 2.5, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (0, 0), 14),
        ("BOTTOMPADDING", (0, -1), (0, -1), 14),
    ]))
    F.append(amt)
    F.append(Spacer(1, 18))

    # --- bonifico a
    F.append(Paragraph(L["h_transfer"], S["h2"]))
    trows = [[Paragraph(k, S["label"]), Paragraph(v, S["value"])] for k, v in L["transfer_rows"]]
    tt = Table(trows, colWidths=[32 * mm, usable - 32 * mm])
    tt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
    ]))
    F.append(tt)
    F.append(Spacer(1, 16))

    # --- note
    F.append(Paragraph(L["h_note"], S["h2"]))
    F.append(Paragraph(L["note_html"], S["small"]))

    doc.build(F)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Proforma_Saldo_Monte_Amiata_22_agosto_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, name))

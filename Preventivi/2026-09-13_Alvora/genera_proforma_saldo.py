#!/usr/bin/env python3
"""
Genera la proforma per il saldo del wine tour in Toscana 13-18 settembre 2026 (Alvora).

Riproduce l'impaginazione dei documenti GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina). Riferimento preventivo: GM-2026-0913-BI.

    python3 genera_proforma_saldo.py --lingua it --cliente "Nome Cliente"
    python3 genera_proforma_saldo.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0913-BI"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Proforma — Saldo",
    subtitle="Wine tour in Toscana, Valdarno · Chianti · Colline Pisane · Versilia  ·  13-18 settembre 2026",
    meta="Intestata a %s  ·  7 settembre 2026  ·  Rif. preventivo " + RIF,
    intro=(
        "Questa proforma riepiloga il saldo dovuto per il servizio in oggetto, già confermato con il "
        "versamento dell'acconto. Non è una fattura fiscale, ma un documento di riepilogo per il pagamento."
    ),
    h_riepilogo="Riepilogo",
    rows=[
        ("Totale servizio, IVA 10% inclusa", "€ 5.104,00"),
        ("Acconto già versato (30%)", "− € 1.530,00"),
    ],
    saldo_label="Saldo da versare",
    saldo="€ 3.574,00",
    h_pagamento="Pagamento",
    pagamento=(
        "Il saldo è dovuto secondo le condizioni indicate nel preventivo di riferimento: entro 5 giorni "
        "dal servizio."
    ),
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. "
          "Nella causale, indicare il riferimento " + RIF + "."),
    h_note="Note",
    note=(
        "Il vitto e l'alloggio del conducente per le notti del 13, 14 e 15 settembre restano a carico "
        "vostro, prenotati e pagati direttamente: non sono compresi in questo saldo. Per il dettaglio "
        "completo del servizio, i giorni, gli orari e le condizioni si rimanda al preventivo " + RIF + "."
    ),
    closing=("Restiamo a disposizione per qualsiasi chiarimento.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Pro Forma — Balance",
    subtitle="Tuscany wine tour, Valdarno · Chianti · Pisan Hills · Versilia  ·  13-18 September 2026",
    meta="Issued to %s  ·  7 September 2026  ·  Quotation ref. " + RIF,
    intro=(
        "This pro forma summarises the balance due for the service below, already confirmed with the "
        "deposit payment. It is not a tax invoice, but a summary document for payment."
    ),
    h_riepilogo="Summary",
    rows=[
        ("Total service, VAT 10% included", "€ 5,104.00"),
        ("Deposit already paid (30%)", "− € 1,530.00"),
    ],
    saldo_label="Balance due",
    saldo="€ 3,574.00",
    h_pagamento="Payment",
    pagamento=(
        "The balance is due under the terms set out in the reference quotation: within 5 days of the "
        "service."
    ),
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. "
          "Please quote reference " + RIF + " in the transfer description."),
    h_note="Notes",
    note=(
        "The driver's board and lodging for the nights of 13, 14 and 15 September remain at your charge, "
        "booked and paid for directly: they are not included in this balance. For the full service detail, "
        "days, times and conditions, please refer to quotation " + RIF + "."
    ),
    closing=("We remain at your disposal for any clarification.<br/><br/>"
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
        "cellsm": ParagraphStyle("cellsm", fontName="Helvetica", fontSize=9.4,
                                 textColor=INK, leading=13),
        "grand": ParagraphStyle("grand", fontName="Helvetica-Bold", fontSize=14,
                                textColor=GREEN, leading=17, spaceBefore=4),
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
    F.append(Paragraph(L["intro"], S["body"]))

    # --- riepilogo
    cols = [usable - 35 * mm, 35 * mm]
    rdata = [[Paragraph(label, S["cellsm"]), Paragraph(amount, S["cellsm"])]
             for label, amount in L["rows"]]
    rdata.append([Paragraph("<b>%s</b>" % L["saldo_label"], S["grand"]),
                  Paragraph("<b>%s</b>" % L["saldo"], S["grand"])])
    rt = Table(rdata, colWidths=cols)
    rt.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("LINEABOVE", (0, -1), (-1, -1), 0.9, GREEN),
        ("BACKGROUND", (0, -1), (-1, -1), CREAM),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    F.append(KeepTogether([Paragraph(L["h_riepilogo"], S["h2"]), rt]))

    # --- pagamento
    F.append(Paragraph(L["h_pagamento"], S["h2"]))
    F.append(Paragraph(L["pagamento"], S["body"]))
    F.append(Paragraph(L["bank"], S["small"]))

    # --- note
    F.append(Paragraph(L["h_note"], S["h2"]))
    F.append(Paragraph(L["note"], S["body"]))

    F.append(Spacer(1, 10))
    F.append(Paragraph(L["closing"], S["small"]))

    doc.build(F)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--cliente", "--client", dest="cliente", default="Alvora")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Proforma_Saldo_Tuscany_Wine_Tour_13-18_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

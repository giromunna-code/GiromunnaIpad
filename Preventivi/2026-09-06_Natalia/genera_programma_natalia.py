#!/usr/bin/env python3
"""
Genera il programma giornaliero GiroMunna per il gruppo Natalia, 6-12 settembre 2026.

Riproduce l'impaginazione dei documenti GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_programma_natalia.py --lingua it
    python3 genera_programma_natalia.py --lingua en
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

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Programma giornaliero",
    subtitle="Servizio 6–12 settembre 2026 · gruppo Natalia · guida: Katerina",
    meta="Preparato il 29 luglio 2026 · Aggiornato il 29 agosto 2026",
    info_rows=[
        ("Mezzo", "Minibus 26 posti più autista · 7,64 × 2,40 m · 8,2 t"),
        ("Gruppo", "16 passeggeri"),
        ("Alloggio", "Villa privata — Via Sorripa, 50026 San Casciano in Val di Pesa (FI)"),
        ("Guida", "Katerina — ritrovo e riaccompagnamento a Villa Costanza, Scandicci "
                  "(capolinea tram T1, uscita A1 Firenze-Scandicci)"),
        ("Firenze", "Contrassegno bus necessario solo l'11 e il 12 settembre: negli altri giorni "
                    "il ritrovo con la guida è fuori dalla zona a pagamento"),
        ("Contatto", "+7 921 941 29 70 — riferimento del gruppo"),
    ],
    h_days="",
    days=[
        dict(date="Domenica 6 settembre", place="Certaldo", dur="5 ore stimate",
             bullets=[
                 "13:00 — ritrovo con la guida a Villa Costanza, Scandicci",
                 "Trasferimento alla villa, ritrovo con il gruppo alle 14:00",
                 "Sosta a Sant'Andrea in Percussina: Casa del Machiavelli",
                 "Certaldo Alto, salita con la funicolare",
                 "Visita guidata circa 1 ora e 30: Casa del Boccaccio, chiesa dove è sepolto "
                 "Boccaccio, Palazzo Pretorio",
                 "Rientro alla villa",
                 "Riaccompagnamento della guida a Villa Costanza",
             ],
             note="Il pullman resta al parcheggio della città bassa: a Certaldo Alto si sale con la funicolare."),
        dict(date="Lunedì 7 settembre", place="Pisa", dur="7 ore stimate",
             bullets=[
                 "09:00 — ritrovo con la guida a Villa Costanza, Scandicci",
                 "Trasferimento alla villa",
                 "10:00 — partenza dalla villa con il gruppo",
                 "Basilica romanica di San Piero a Grado, circa 15 minuti dal centro di Pisa",
                 "Piazza dei Miracoli: Duomo e Battistero",
                 "A piedi fino a Piazza dei Cavalieri",
                 "Durata delle visite circa 3 ore",
                 "Rientro alla villa: pranzo tardo alla villa",
                 "Riaccompagnamento della guida a Villa Costanza",
             ],
             note="È lunedì: verificare le chiusure dei musei prima di fissare gli orari."),
        dict(date="Martedì 8 settembre", place="Siena", dur="11 ore stimate",
             bullets=[
                 "09:00 — ritrovo con la guida a Villa Costanza, Scandicci",
                 "Trasferimento alla villa",
                 "10:00 — partenza dalla villa con il gruppo",
                 "Duomo, Battistero e Museo dell'Opera del Duomo",
                 "Pranzo",
                 "Nel pomeriggio Palazzo Pubblico",
                 "Durata complessiva circa 7 ore, pranzo incluso",
                 "Rientro alla villa",
                 "Riaccompagnamento della guida a Villa Costanza",
             ],
             note="Giornata più lunga della settimana, undici ore di servizio: pianificare la pausa dell'autista."),
        dict(date="Mercoledì 9 settembre", place="Pistoia e Prato", dur="8 ore stimate",
             bullets=[
                 "09:00 — ritrovo con la guida a Villa Costanza, Scandicci",
                 "Trasferimento alla villa",
                 "10:00 — partenza dalla villa con il gruppo",
                 "Pistoia: Duomo di San Zeno con l'Altare argenteo di San Jacopo, San Giovanni "
                 "Fuorcivitas, Sant'Andrea con il pulpito di Giovanni Pisano, Ospedale del Ceppo",
                 "Prato: Duomo di Santo Stefano e affreschi di Filippo Lippi",
                 "Durata delle visite circa 4 ore",
                 "Rientro alla villa",
                 "Riaccompagnamento della guida a Villa Costanza",
             ],
             note="Nessuna cantina in programma questo giorno, confermato da Natalia. Le chiese "
                  "chiudono per la pausa di mezzogiorno: la giornata va costruita su due blocchi, "
                  "mattina e pomeriggio."),
        dict(date="Giovedì 10 settembre", place="San Gimignano", dur="7 ore stimate",
             bullets=[
                 "09:00 — ritrovo con la guida a Villa Costanza, Scandicci",
                 "Trasferimento alla villa",
                 "Partenza dalla villa con il gruppo",
                 "Collegiata di Santa Maria Assunta",
                 "Casa Campatelli: torre medievale visitabile all'interno",
                 "16:00 — degustazione in cantina, confermata, durata circa 1 ora e 30",
                 "Rientro alla villa: pranzo tardo alla villa",
                 "Riaccompagnamento della guida a Villa Costanza",
             ],
             note="Il centro è pedonale: il pullman sosta nei parcheggi fuori dalle mura."),
        dict(date="Venerdì 11 settembre", place="Firenze", dur="10 ore stimate",
             bullets=[
                 "10:00 — partenza dalla villa verso Firenze",
                 "Discesa del gruppo in Piazza Savonarola",
                 "Ripresa del gruppo verso le 19:15 in Piazza Vittorio Veneto",
                 "Rientro alla villa verso le 20:00",
             ],
             note="Discesa e ripresa in due punti diversi: Savonarola a nordest, Vittorio Veneto a "
                  "ovest all'ingresso delle Cascine. Nove ore tra i due passaggi: da decidere se "
                  "l'autista attende a Firenze o rientra alla villa. Il contrassegno vale 0/24, "
                  "quindi una sola giornaliera copre entrambi."),
        dict(date="Sabato 12 settembre", place="Firenze", dur="5 ore stimate",
             bullets=[
                 "10:00 — partenza dalla villa verso Firenze",
                 "Discesa del gruppo a Piazzale Michelangelo",
                 "Ripresa del gruppo verso le 14:15 in Piazza Vittorio Veneto",
                 "Rientro alla villa verso le 15:00",
             ],
             note="Discesa e ripresa in due punti diversi, agli estremi opposti della città: il "
                  "gruppo attraversa il centro a piedi. Poco più di quattro ore di attesa, "
                  "conviene che l'autista resti in zona. Una sola giornaliera copre entrambi i "
                  "passaggi."),
    ],
    h_open="Punti ancora aperti",
    open_points=[
        "<b>Attesa dell'11 settembre.</b> Da decidere se l'autista resta a Firenze fra le 10:00 e "
        "le 19:15 o rientra alla villa: nel primo caso serve un parcheggio bus in città, nel "
        "secondo sono due viaggi in più.",
        "<b>Contrassegni.</b> Vanno acquistati online due contrassegni giornalieri, per l'11 e il "
        "12 settembre, intestati alla targa del mezzo. Negli altri giorni il pullman non entra in "
        "città.",
        "<b>Riposo dell'autista.</b> Sette giorni consecutivi di servizio: verificare la "
        "collocazione del riposo settimanale secondo il Regolamento CE 561/2006.",
    ],
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Daily programme",
    subtitle="Service 6–12 September 2026 · Natalia's group · guide: Katerina",
    meta="Prepared 29 July 2026 · Updated 29 August 2026",
    info_rows=[
        ("Vehicle", "Minibus, 26 seats plus driver · 7.64 × 2.40 m · 8.2 t"),
        ("Group", "16 passengers"),
        ("Accommodation", "Private villa — Via Sorripa, 50026 San Casciano in Val di Pesa (FI)"),
        ("Guide", "Katerina — pick-up and drop-off at Villa Costanza, Scandicci "
                  "(T1 tram terminus, A1 Firenze-Scandicci exit)"),
        ("Florence", "Bus permit only needed on 11 and 12 September: on other days the meeting "
                     "point with the guide is outside the paid zone"),
        ("Contact", "+7 921 941 29 70 — group reference"),
    ],
    h_days="",
    days=[
        dict(date="Sunday 6 September", place="Certaldo", dur="5 hours estimated",
             bullets=[
                 "13:00 — meeting with the guide at Villa Costanza, Scandicci",
                 "Transfer to the villa, meeting the group at 14:00",
                 "Stop at Sant'Andrea in Percussina: Machiavelli's house",
                 "Certaldo Alto, up by funicular",
                 "Guided visit about 1 hour 30: Boccaccio's house, the church where Boccaccio "
                 "is buried, Palazzo Pretorio",
                 "Return to the villa",
                 "Guide dropped off at Villa Costanza",
             ],
             note="The coach stays in the lower town car park: Certaldo Alto is reached by funicular."),
        dict(date="Monday 7 September", place="Pisa", dur="7 hours estimated",
             bullets=[
                 "09:00 — meeting with the guide at Villa Costanza, Scandicci",
                 "Transfer to the villa",
                 "10:00 — departure from the villa with the group",
                 "Romanesque Basilica of San Piero a Grado, about 15 minutes from central Pisa",
                 "Piazza dei Miracoli: Cathedral and Baptistery",
                 "On foot to Piazza dei Cavalieri",
                 "Visits last about 3 hours",
                 "Return to the villa: late lunch at the villa",
                 "Guide dropped off at Villa Costanza",
             ],
             note="It's a Monday: check museum closures before fixing the times."),
        dict(date="Tuesday 8 September", place="Siena", dur="11 hours estimated",
             bullets=[
                 "09:00 — meeting with the guide at Villa Costanza, Scandicci",
                 "Transfer to the villa",
                 "10:00 — departure from the villa with the group",
                 "Cathedral, Baptistery and Museo dell'Opera del Duomo",
                 "Lunch",
                 "Palazzo Pubblico in the afternoon",
                 "About 7 hours overall, lunch included",
                 "Return to the villa",
                 "Guide dropped off at Villa Costanza",
             ],
             note="The longest day of the week, eleven hours of service: plan the driver's break."),
        dict(date="Wednesday 9 September", place="Pistoia and Prato", dur="8 hours estimated",
             bullets=[
                 "09:00 — meeting with the guide at Villa Costanza, Scandicci",
                 "Transfer to the villa",
                 "10:00 — departure from the villa with the group",
                 "Pistoia: Cathedral of San Zeno with the silver Altar of San Jacopo, San "
                 "Giovanni Fuorcivitas, Sant'Andrea with Giovanni Pisano's pulpit, Ospedale del "
                 "Ceppo",
                 "Prato: Cathedral of Santo Stefano and Filippo Lippi's frescoes",
                 "Visits last about 4 hours",
                 "Return to the villa",
                 "Guide dropped off at Villa Costanza",
             ],
             note="No winery stop on this day, confirmed by Natalia. Churches close for the "
                  "midday break: the day needs to be built around two blocks, morning and "
                  "afternoon."),
        dict(date="Thursday 10 September", place="San Gimignano", dur="7 hours estimated",
             bullets=[
                 "09:00 — meeting with the guide at Villa Costanza, Scandicci",
                 "Transfer to the villa",
                 "Departure from the villa with the group",
                 "Collegiata di Santa Maria Assunta",
                 "Casa Campatelli: medieval tower open to visitors",
                 "16:00 — winery tasting, confirmed, lasting about 1 hour 30",
                 "Return to the villa: late lunch at the villa",
                 "Guide dropped off at Villa Costanza",
             ],
             note="The centre is pedestrian: the coach waits in car parks outside the walls."),
        dict(date="Friday 11 September", place="Florence", dur="10 hours estimated",
             bullets=[
                 "10:00 — departure from the villa towards Florence",
                 "Group dropped off at Piazza Savonarola",
                 "Group picked up around 19:15 at Piazza Vittorio Veneto",
                 "Return to the villa around 20:00",
             ],
             note="Drop-off and pick-up at two different points: Savonarola to the north-east, "
                  "Vittorio Veneto to the west at the entrance to the Cascine. Nine hours between "
                  "the two: decide whether the driver waits in Florence or returns to the villa. "
                  "The permit covers 0/24, so a single day pass covers both."),
        dict(date="Saturday 12 September", place="Florence", dur="5 hours estimated",
             bullets=[
                 "10:00 — departure from the villa towards Florence",
                 "Group dropped off at Piazzale Michelangelo",
                 "Group picked up around 14:15 at Piazza Vittorio Veneto",
                 "Return to the villa around 15:00",
             ],
             note="Drop-off and pick-up at two different points, at opposite ends of the city: "
                  "the group crosses the centre on foot. Just over four hours of waiting, better "
                  "for the driver to stay in the area. A single day pass covers both crossings."),
    ],
    h_open="Points still open",
    open_points=[
        "<b>Waiting on 11 September.</b> Decide whether the driver stays in Florence between "
        "10:00 and 19:15 or returns to the villa: the first option needs a bus car park in the "
        "city, the second means two extra trips.",
        "<b>Permits.</b> Two daily permits need to be bought online, for 11 and 12 September, "
        "registered to the vehicle's plate. On other days the coach does not enter the city.",
        "<b>Driver's rest.</b> Seven consecutive days of service: check how the weekly rest fits "
        "under EC Regulation 561/2006.",
    ],
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
        "daydate": ParagraphStyle("daydate", fontName="Helvetica-Bold", fontSize=10.4,
                                  textColor=INK, leading=13),
        "dayplace": ParagraphStyle("dayplace", fontName="Helvetica-Bold", fontSize=10.4,
                                   textColor=GREEN, leading=13),
        "daydur": ParagraphStyle("daydur", fontName="Helvetica", fontSize=8.6,
                                 textColor=MUTED, leading=13, alignment=2),
        "cellsm": ParagraphStyle("cellsm", **base),
        "cellmut": ParagraphStyle("cellmut", fontName="Helvetica", fontSize=8.6,
                                  textColor=MUTED, leading=12),
        "note": ParagraphStyle("note", alignment=TA_JUSTIFY, spaceAfter=10,
                               leftIndent=9, fontName="Helvetica", fontSize=8.6,
                               textColor=MUTED, leading=12, spaceBefore=2),
        "small": ParagraphStyle("small", alignment=TA_JUSTIFY, spaceAfter=5,
                                fontName="Helvetica", fontSize=8.8,
                                textColor=INK, leading=12.4),
        "openitem": ParagraphStyle("openitem", alignment=TA_JUSTIFY, spaceAfter=7,
                                   leftIndent=9, fontName="Helvetica", fontSize=8.8,
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


def build(lang, out):
    L = IT if lang == "it" else EN
    S = styles()
    w, _ = A4
    usable = w - 2 * MARGIN

    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=TOP, bottomMargin=BOTTOM,
                          title="GiroMunna %s" % L["title"],
                          author="GiroMunna")
    frame = Frame(MARGIN, BOTTOM, usable, A4[1] - TOP - BOTTOM, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=make_chrome(L))])

    F = []
    F.append(Paragraph(L["title"], S["title"]))
    F.append(Paragraph(L["subtitle"], S["subtitle"]))
    F.append(Paragraph(L["meta"], S["meta"]))

    # --- tabella informazioni
    icols = [30 * mm, usable - 30 * mm]
    idata = [[Paragraph("<b>%s</b>" % k, S["cellsm"]), Paragraph(v, S["cellsm"])]
             for k, v in L["info_rows"]]
    it_ = Table(idata, colWidths=icols)
    it_.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    F.append(it_)
    F.append(Spacer(1, 10))

    # --- giornate
    dcols = [usable - 27 * mm - 27 * mm, 27 * mm, 27 * mm]
    for d in L["days"]:
        head = Table([[Paragraph(d["date"], S["daydate"]),
                        Paragraph(d["place"], S["dayplace"]),
                        Paragraph(d["dur"], S["daydur"])]], colWidths=dcols)
        head.setStyle(TableStyle([
            ("LINEBELOW", (0, 0), (-1, -1), 0.8, GOLD),
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        bullets_html = "<br/>· ".join(d["bullets"])
        block = [head, Spacer(1, 4), Paragraph("· " + bullets_html, S["small"])]
        if d.get("note"):
            block.append(Paragraph(d["note"], S["note"]))
        else:
            block.append(Spacer(1, 6))
        F.append(KeepTogether(block))

    # --- punti ancora aperti
    F.append(Paragraph(L["h_open"], S["h2"]))
    for p in L["open_points"]:
        F.append(Paragraph("·  " + p, S["openitem"]))

    doc.build(F)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Programma_Natalia_6-12_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, name))

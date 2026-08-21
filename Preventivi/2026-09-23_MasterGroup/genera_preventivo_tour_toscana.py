#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il tour della Toscana in giornata, 12 passeggeri,
quattro itinerari a scelta, carico e scarico all'Hotel Adamas di Firenze.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_tour_toscana.py --cliente "Nome Cliente"

Solo in italiano, per decisione di Girolamo: Master Group e' un tour operator italiano
e ha scritto in italiano. Se dovesse servire anche la versione inglese, il dizionario EN
sta nella storia del repository, nel commit che ha aggiunto questa cartella.
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

RIF = "GM-2026-0923-MG"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Tour della Toscana in giornata, quattro itinerari a scelta  ·  mercoledì 23 settembre 2026  ·  12 passeggeri  ·  partenza e rientro a Firenze",
    meta="Preparato per %s  ·  21 agosto 2026  ·  Rif. " + RIF,

    h_mezzo="Il mezzo",
    mezzo_intro=("Un minibus con conducente per il vostro gruppo di 12 persone, a vostra disposizione per "
                 "l'intera giornata di mercoledì 23 settembre, con lo stesso autista dalla partenza al rientro."),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Ci avete chiesto uno sprinter di capienza sufficiente oppure un minibus: il nostro è un minibus da 26 posti, "
        "quindi con 12 ospiti a bordo ognuno viaggia con il sedile accanto libero e le borse restano nel vano bagagli "
        "invece che fra i piedi. Su una giornata da dieci ore, con tre o quattro tappe e il caldo dell'estate toscana, "
        "è una differenza che si sente. I 7,64 metri sono poi la misura giusta per questa regione: entrano nei piazzali "
        "di San Gimignano, Monteriggioni e Montepulciano dove un gran turismo da 13 metri non passa, e a Firenze "
        "rientrano nella fascia di permesso sotto gli 8 metri, che costa meno."
    ),

    h_carico="Il punto di carico",
    carico_intro=(
        "L'Hotel Adamas è in Via Ricasoli 9, a un passo da Piazza del Duomo. Vi rispondiamo subito e senza giri di "
        "parole: <b>in Via Ricasoli il minibus non ci può entrare, e non esiste permesso che lo consenta.</b> "
        "Il civico 9 si affaccia praticamente sulla piazza del Duomo, che è <b>area pedonale</b>: lì l'accesso dei "
        "veicoli è vietato sempre, non soltanto negli orari della ZTL, e i varchi sono protetti da pilomat che con i "
        "permessi ordinari non si aprono. A monte c'è poi la ZTL bus, che copre tutto il centro abitato ventiquattro "
        "ore su ventiquattro, tutti i giorni dell'anno, e riguarda ogni veicolo per trasporto passeggeri con più di "
        "nove posti: il nostro minibus da 26 esattamente come uno sprinter da 12 o da 16. E il contrassegno che si "
        "paga per portare un bus in città <b>non autorizza a circolare ovunque</b>: i mezzi devono attenersi a "
        "percorsi prestabiliti e possono fermarsi soltanto nei punti autorizzati. Non è un limite del mezzo che vi "
        "proponiamo, è il regime di Firenze. Ecco come si risolve."
    ),
    carico_head=["Soluzione", "Come funziona", "Costo"],
    carico=[
        ("Navetta van<br/><b>la consigliamo</b>",
         "Due van fino a nove posti — che nella ZTL entrano regolarmente — vi prendono davanti all'hotel e vi portano "
         "al minibus in Piazza Vittorio Veneto: dieci minuti di percorso. Lo stesso a fine giornata, per riportarvi "
         "all'ingresso dell'hotel. Non sono mezzi nostri: se volete ce ne occupiamo noi e vi giriamo la tariffa, "
         "oppure la prenotate voi.",
         "su richiesta"),
        ("Taxi dal ricevimento",
         "Tre taxi per dodici persone, stesso percorso: anche i taxi in ZTL entrano. Li prenota il ricevimento "
         "dell'Adamas la sera prima e li pagate voi direttamente sul posto.",
         "circa € 20,00<br/>a taxi, a tratta"),
        ("A piedi, solo la sera",
         "Al rientro il minibus vi lascia in Piazza Savonarola, il punto autorizzato più vicino all'hotel: 1,4 km, "
         "una ventina di minuti a piedi. È autorizzato alla sola discesa e solo fra le 08:00 e le 20:00, quindi "
         "serve per il ritorno, mai per la partenza.",
         "senza costi"),
    ],
    carico_close=(
        "Il ritrovo del mattino è in <b>Piazza Vittorio Veneto</b>, all'altezza del Ponte della Vittoria: è autorizzato "
        "al carico e allo scarico ventiquattro ore su ventiquattro, senza le limitazioni di orario o di tipo di "
        "servizio che gravano sugli altri punti vicini al centro. L'autista vi aspetta lì con il cartello GiroMunna."
    ),

    h_servizio="Il servizio",
    svc_head=["Itinerario", "Percorso e programma", "Impegno del mezzo"],
    svc=[
        ("A<br/>Pisa e Lucca",
         "<b>Firenze → Pisa → Lucca → Firenze.</b> Ritrovo alle 08:30 in Piazza Vittorio Veneto. Novanta chilometri "
         "fino a Pisa con arrivo verso le 09:45; il mezzo sosta al terminal bus di Via Pietrasantina, dieci minuti a "
         "piedi da Piazza dei Miracoli. Ripartenza alle 12:30 e 25 km fino a Lucca, dove si sosta fuori dalle mura e "
         "si entra in centro a piedi. Rientro alle 17:30, 80 km di autostrada, a Firenze verso le 18:45. "
         "<b>In tutto circa 320 km per il mezzo.</b>",
         "circa<br/>08:30 – 19:00"),
        ("B<br/>Pisa, Siena e<br/>San Gimignano",
         "<b>Firenze → Pisa → Siena → San Gimignano → Firenze.</b> Partenza alle 07:30: novanta chilometri fino a "
         "Pisa, poi 125 km attraversando la Toscana fino a Siena, 45 km a San Gimignano e 55 km di rientro. Quattro "
         "tappe e oltre cinque ore di sola guida, cui vanno aggiunte le soste. È di gran lunga la giornata più lunga "
         "delle quattro: nelle note vi spieghiamo perché vi conviene alleggerirla. <b>In tutto circa 470 km per il mezzo.</b>",
         "circa<br/>07:30 – 20:00"),
        ("C<br/>Siena, San Gimignano<br/>e Monteriggioni",
         "<b>Firenze → Siena → San Gimignano → Monteriggioni → Firenze.</b> Partenza alle 08:30 e 75 km fino a Siena; "
         "poi 45 km a San Gimignano, 30 km a Monteriggioni e 55 km di rientro, in città verso le 19:00. Vi proponiamo "
         "di girare l'ordine delle tappe, mettendo Monteriggioni per primo: nelle note trovate il perché. "
         "<b>In tutto circa 330 km per il mezzo, che scendono a 295 nell'ordine che consigliamo.</b>",
         "circa<br/>08:30 – 19:00"),
        ("D<br/>Montalcino, Pienza<br/>e Montepulciano",
         "<b>Firenze → Montalcino → Pienza → Montepulciano → Firenze.</b> Partenza alle 08:00 e 110 km fino a "
         "Montalcino, arrivo verso le 09:45. Venticinque chilometri a Pienza e altri 15 a Montepulciano, nel cuore "
         "della Val d'Orcia; rientro dall'autostrada della Valdichiana, 120 km, a Firenze verso le 19:45. La giornata "
         "più bella delle quattro e la più impegnativa a piedi: tre borghi in collina. <b>In tutto circa 400 km per il mezzo.</b>",
         "circa<br/>08:00 – 20:00"),
    ],
    svc_note=("I chilometri di ogni giornata sono quelli percorsi dal mezzo per intero, dalla nostra rimessa di "
              "Ponte Buggianese al rientro, e comprendono anche gli spostamenti ai parcheggi bus autorizzati durante "
              "le soste: il percorso che farete voi è naturalmente più corto, ed è quello indicato tappa per tappa "
              "qui sopra. I tempi di percorrenza sono stime stradali, traffico escluso, e gli orari sono la nostra "
              "proposta: li ricalcoliamo volentieri sull'ora di partenza che preferite."),

    h_prezzo="Il prezzo",
    price_head=["Itinerario — una giornata intera, tutto compreso", "Al netto", "IVA 10% inclusa"],
    price_rows=[
        ("<b>A</b> · Firenze → Pisa → Lucca → Firenze — circa 320 km", "€ 1.590,91", "€ 1.750,00"),
        ("<b>B</b> · Firenze → Pisa → Siena → San Gimignano → Firenze — circa 470 km", "€ 1.954,55", "€ 2.150,00"),
        ("<b>C</b> · Firenze → Siena → San Gimignano → Monteriggioni → Firenze — circa 330 km", "€ 1.590,91", "€ 1.750,00"),
        ("<b>D</b> · Firenze → Montalcino → Pienza → Montepulciano → Firenze — circa 400 km", "€ 1.272,73", "€ 1.400,00"),
        ("Navetta van fra l'hotel e il punto di carico, andata e ritorno — <i>opzionale</i>",
         "<i>su richiesta</i>", "—"),
        ("Vitto del conducente", "<i>a carico vostro</i>", "—"),
    ],
    grand=("Gli importi sono per l'intera giornata e per tutto il gruppo, non a persona: in dodici, "
           "da €&nbsp;116,67 a €&nbsp;179,17 a testa secondo l'itinerario."),
    perhead=("Si conferma un itinerario solo, quello che sceglierete. Il prezzo comprende tutti gli oneri di accesso, "
             "compreso il permesso ZTL bus di Firenze e, negli itinerari che toccano Siena, il permesso comunale per "
             "i bus turistici: il giorno del servizio non vi verrà chiesto nulla di aggiuntivo."),

    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi autostradali, assicurazione completa e "
        "movimentazione bagagli. Sono compresi anche tutti gli oneri di accesso, che su questi itinerari non sono una "
        "voce secondaria: il checkpoint di Firenze, che il nostro mezzo paga nella fascia sotto gli 8 metri, e poi, "
        "secondo l'itinerario che sceglierete, la sosta bus di Pisa e quella di Lucca, il permesso comunale per i bus "
        "turistici di Siena, le soste autorizzate di San Gimignano e Monteriggioni e i parcheggi di Montalcino, Pienza e "
        "Montepulciano."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il vitto del conducente, che resta a vostro carico. Ingressi ai monumenti, guide, degustazioni, pasti e "
        "mance. La navetta van da e per l'hotel, che vi quotiamo a parte se ci chiedete di occuparcene. Attesa oltre gli orari "
        "concordati, € 50,00 all'ora. Soste aggiuntive o modifiche all'itinerario decise in corso di giornata, "
        "quotate a parte. Rientro dopo le 02:00, € 250,00."
    ),

    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 420,00 – € 645,00", "secondo l'itinerario scelto"),
        ("Saldo, entro 5 giorni dal servizio", "il restante 70%", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),

    h_note="Note",
    note=[
        ("<b>In Via Ricasoli non entra nessun autobus, e non è una questione del nostro mezzo.</b> Lo mettiamo per "
         "iscritto perché è esattamente quello che ci avete chiesto: il divieto non dipende dalla misura del minibus "
         "e non si compra con un permesso. Si sommano tre cose. L'area del Duomo è pedonale e sbarrata da pilomat. "
         "La ZTL bus copre tutto il centro abitato e vale per qualsiasi veicolo oltre i nove posti, sprinter "
         "compresi. Il contrassegno bus, infine, consente di circolare solo sui percorsi prestabiliti e di fermarsi "
         "solo nei punti autorizzati dal Comune. Fra questi, il più vicino all'Adamas che consenta anche la salita è "
         "Piazza Vittorio Veneto, verso le Cascine, a circa 2,5 km. Piazza Savonarola è più vicina — 1,4 km, una "
         "ventina di minuti a piedi — ma è autorizzata alla sola discesa e solo dalle 08:00 alle 20:00: va bene per "
         "il rientro serale, non per la partenza."),
        ("<b>La navetta van: ce ne occupiamo noi oppure ve la fate voi, come preferite.</b> È la risposta alla "
         "vostra domanda ed è la soluzione che vi consigliamo, soprattutto la mattina presto e alla fine di una "
         "giornata lunga. I veicoli fino a nove posti non ricadono nella ZTL bus e arrivano davanti all'hotel: per "
         "dodici persone servono due van, che vi portano al minibus in dieci minuti. Non sono mezzi nostri, e "
         "preferiamo non metterveli a preventivo con una cifra che poi dovremmo correggere: <b>se ci dite di "
         "procedere sentiamo un collega di Firenze e vi giriamo la tariffa</b>, senza impegno da parte vostra. Se "
         "invece preferite organizzarla voi, o farla prenotare direttamente dall'Adamas che quei van li chiama tutti "
         "i giorni, per noi va benissimo lo stesso. L'importante è che qualcuno la prenoti: da Via Ricasoli a Piazza "
         "Vittorio Veneto a piedi sono 2,5 km, e la mattina presto con la famiglia non è la partenza che vi augurate."),
        ("<b>L'itinerario B chiede troppo a una giornata sola.</b> Pisa sta a ovest, Siena e San Gimignano a sud: "
         "metterli insieme significa 470 chilometri per il mezzo e oltre cinque ore di sola guida, cui vanno "
         "aggiunte le soste. "
         "Partendo alle 07:30 si rientra verso le 20:00, e in mezzo restano due ore a Pisa, tre a Siena — pranzo "
         "compreso — e due a San Gimignano: il minimo per tre luoghi di quel calibro. Dodici ore e mezza fuori, per "
         "una famiglia, sono tante. Ve lo quotiamo lo stesso perché ce lo avete "
         "chiesto, ma se volete il nostro parere: togliete Pisa e avete l'itinerario C, oppure tenete Pisa e "
         "abbinatela a Lucca, che è l'itinerario A. Sono due giornate belle invece di una corsa."),
        ("<b>L'itinerario C conviene girarlo.</b> Monteriggioni si trova sulla superstrada Firenze-Siena, "
         "praticamente sulla strada dell'andata, mentre nell'ordine che ci avete indicato ci si arriva tornando "
         "indietro da San Gimignano. Facendo Firenze → Monteriggioni → Siena → San Gimignano → Firenze si scende a "
         "circa 295 km invece di 330 e si guadagna quasi un'ora, che sul posto vale molto più che in autostrada. "
         "Il prezzo non cambia: € 1.750,00 IVA inclusa in entrambi i casi."),
        ("<b>I borghi si guadagnano a piedi.</b> Siena, San Gimignano, Monteriggioni, Montalcino, Pienza e "
         "Montepulciano hanno tutti il centro storico chiuso ai bus: si scende ai parcheggi autorizzati appena fuori "
         "dalle mura e si sale a piedi. A Montepulciano la salita dal parcheggio a Piazza Grande è ripida e dura una "
         "ventina di minuti. Se nella famiglia ci sono persone anziane, bambini piccoli o qualcuno con difficoltà a "
         "camminare, ditecelo prima di confermare: cambiano i punti di discesa che chiediamo e, in qualche caso, "
         "l'ordine delle tappe."),
        ("<b>Vitto del conducente, e nessun pernottamento.</b> Si parte e si torna a Firenze in giornata, quindi il "
         "conducente rientra alla base e non c'è nessuna notte da prenotare. Resta il pranzo, che come da nostre "
         "condizioni è a vostro carico: la via più semplice è che mangi dove si ferma il gruppo, altrimenti "
         "concordiamo in anticipo una cifra fissa. Non lo mettiamo a preventivo perché non lo organizziamo noi."),
        ("<b>Gli orari li fissiamo insieme.</b> Quelli indicati sono la nostra proposta, costruita su una giornata "
         "piena e sul traffico normale della stagione: confermateci l'ora di partenza che preferite e ricalcoliamo "
         "il resto. L'attesa oltre gli orari concordati si conteggia a € 50,00 all'ora. Per gli itinerari B e D la "
         "partenza di buon'ora non è un dettaglio, è la condizione perché la giornata funzioni."),
        ("<b>Il 23 settembre è una buona data.</b> È un mercoledì di fine stagione: i prezzi qui sopra sono "
         "quelli di media stagione e restano fermi, senza maggiorazioni da fine settimana o da alta stagione. "
         "Siena e San Gimignano di mercoledì sono molto più vivibili che nel fine settimana, e in Val d'Orcia si "
         "è in piena vendemmia, il che rende l'itinerario D particolarmente bello — con qualche trattore in più "
         "sulle strade e i piazzali delle cantine più affollati. Due cose da tenere presenti: a fine settembre la "
         "luce va via verso le 19:20, quindi negli itinerari B e D l'ultimo tratto di rientro si fa al buio, e i "
         "borghi in collina chiudono musei e botteghe prima che d'estate. Se contate di vedere qualcosa di "
         "preciso, ditecelo e costruiamo gli orari su quello."),
        ("<b>Per confermare ci servono</b> l'itinerario scelto, l'ora di partenza, il numero definitivo di "
         "passeggeri, se volete la navetta van dall'hotel, un recapito telefonico o WhatsApp di chi viaggia con la "
         "famiglia e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo per il 23 settembre è libero e ve lo teniamo a "
         "disposizione per tutta la validità di questo preventivo; la prenotazione diventa definitiva alla "
         "ricezione dell'acconto. "
         "La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene trattenuto "
         "l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. "
         "Mancando oggi 33 giorni al servizio, questa prenotazione ricade nella fascia da 60 a 30 giorni, e dal "
         "24 agosto passerà in quella da 30 a 10: se contate di confermare, farlo entro quella data vi lascia "
         "condizioni migliori. Preventivo valido fino al 4 settembre 2026."),
    ],
    closing=("Restiamo a disposizione per qualsiasi chiarimento e in attesa di un vostro riscontro.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
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


def _grid(extra=()):
    """Bordi e spaziature comuni a tutte le tabelle del preventivo."""
    return TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ] + list(extra))


def build(cliente, out):
    L = IT
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
    bullet.setStyle(_grid([
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

    # --- punto di carico
    F.append(Paragraph(L["h_carico"], S["h2"]))
    F.append(Paragraph(L["carico_intro"], S["body"]))
    ccols = [32 * mm, usable - 32 * mm - 28 * mm, 28 * mm]
    cdata = [[Paragraph(h, S["th"]) for h in L["carico_head"]]]
    for opt, how, cost in L["carico"]:
        cdata.append([Paragraph("<b>%s</b>" % opt, S["cellsm"]),
                      Paragraph(how, S["cellsm"]),
                      Paragraph(cost, S["cellmut"])])
    ct = Table(cdata, colWidths=ccols, repeatRows=1)
    ct.setStyle(_grid([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, RULE),
    ]))
    F.append(ct)
    F.append(Spacer(1, 7))
    F.append(Paragraph(L["carico_close"], S["body"]))

    # --- servizio
    F.append(Paragraph(L["h_servizio"], S["h2"]))
    cols = [30 * mm, usable - 30 * mm - 24 * mm, 24 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for itin, desc, eng in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % itin, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
            Paragraph(eng, S["cellmut"]),
        ])
    t = Table(data, colWidths=cols, repeatRows=1)
    t.setStyle(_grid([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, RULE),
    ]))
    F.append(t)
    F.append(Spacer(1, 6))
    F.append(Paragraph(L["svc_note"], S["small"]))

    # --- prezzo (intestazione e tabella non si spezzano fra due pagine)
    pcols = [usable - 27 * mm - 27 * mm, 27 * mm, 27 * mm]
    pdata = [[Paragraph(h, S["th"]) for h in L["price_head"]]]
    for label, netto, lordo in L["price_rows"]:
        pdata.append([Paragraph(label, S["cellsm"]),
                      Paragraph(netto, S["cellsm"]),
                      Paragraph("<b>%s</b>" % lordo, S["cellsm"])])
    pt = Table(pdata, colWidths=pcols, repeatRows=1)
    pt.setStyle(_grid([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, RULE),
        ("LINEABOVE", (0, -1), (-1, -1), 0.5, RULE),
        ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
    ]))
    # la lista va costruita prima: KeepTogether non tiene il riferimento
    # a una lista vuota passata alla costruzione.
    F.append(KeepTogether([
        Paragraph(L["h_prezzo"], S["h2"]),
        pt,
        Paragraph(L["grand"], S["grand"]),
    ]))
    F.append(Paragraph(L["perhead"], S["small"]))
    F.append(Spacer(1, 4))
    F.append(Paragraph("<b>%s</b> %s" % (L["h_incluso"], L["incluso"]), S["small"]))
    F.append(Paragraph("<b>%s</b> %s" % (L["h_nonincluso"], L["nonincluso"]), S["small"]))

    # --- pagamento
    F.append(Paragraph(L["h_pagamento"], S["h2"]))
    ydata = [[Paragraph(a, S["cellsm"]), Paragraph("<b>%s</b>" % b, S["cellsm"]),
              Paragraph(c, S["cellmut"])] for a, b, c in L["pay_rows"]]
    yt = Table(ydata, colWidths=[usable - 40 * mm - 40 * mm, 40 * mm, 40 * mm])
    yt.setStyle(_grid([
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Master Group Tour Operator")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Tour_Toscana_23_settembre_2026_IT.pdf")
    print(build(a.cliente, name))

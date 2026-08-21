#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il servizio Lucca - Tenuta di Forci del 7 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_lucca_forci.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_lucca_forci.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1007-RZ"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Lucca · Tenuta di Forci · Lucca, mezzo e conducente a disposizione  ·  mercoledì 7 ottobre 2026",
    meta="Preparato per %s  ·  21 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un solo minibus privato per il vostro gruppo di 24 persone, riservato al vostro gruppo "
        "per l'intera durata del servizio."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 24 ospiti a bordo restano due posti liberi. I 7,64 metri sono la ragione per cui possiamo "
        "confermarvi Forci: sia il percorso alternativo alla frana sia i sette chilometri di salita fino "
        "alla tenuta sono strade di collina strette, dove un autobus gran turismo non passa. "
        "A bordo non sale nessun altro gruppo."
    ),
    h_servizio="Il servizio",
    svc_head=["Orario", "Percorso", "Durata"],
    svc=[
        ("11:45",
         "<b>Ritrovo a Lucca, Piazzale Boccherini</b>, appena dentro Porta Sant'Anna. Il conducente è sul "
         "posto con un quarto d'ora di anticipo, con il cartello GiroMunna.",
         "—"),
        ("12:00",
         "<b>Piazzale Boccherini → Tenuta di Forci</b>, Via della Pieve Santo Stefano. Circa 15 km per il "
         "percorso alternativo alla frana, che sale da Mutigliano; arrivo alla tenuta verso le 12:35.",
         "circa 35 min"),
        ("12:35 – 16:00",
         "<b>Mezzo e conducente restano a Forci</b>, a vostra disposizione per tutto il pranzo e la "
         "degustazione. L'attesa è compresa nel prezzo.",
         "circa 3 h 25"),
        ("16:00",
         "<b>Tenuta di Forci → Lucca, Piazzale Boccherini.</b> Stesso percorso a ritroso, arrivo verso "
         "le 16:40. Se preferite ripartire alle 15:30, il prezzo non cambia.",
         "circa 40 min"),
    ],
    svc_foot="Mezzo impegnato circa 11:45 – 17:00. Distanze e tempi sono stime stradali, traffico escluso.",
    h_prezzo="Il prezzo",
    price_rows=[
        ("Mer 7 ott — Lucca → Tenuta di Forci → Lucca, mezzo e conducente a vostra disposizione "
         "dalle 11:45 alle 17:00, attesa durante il pranzo compresa", "€ 500,00", "+ IVA 10%"),
        ("IVA 10% sul servizio", "€ 50,00", ""),
        ("Permesso comunale di accesso a Lucca per i bus turistici, che anticipiamo noi per "
         "vostro conto", "€ 180,00", "<i>fuori campo IVA</i>"),
        ("Vitto e alloggio del conducente", "<i>non necessario</i>", ""),
    ],
    price_total_label="Totale da corrispondere",
    price_total="€ 730,00",
    vat_note="",
    grand="Totale da corrispondere: € 730,00.",
    perhead=("€ 550,00 di servizio, IVA 10% inclusa, più € 180,00 di permesso comunale senza IVA. "
             "Circa € 30,40 a persona."),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera fascia oraria indicata, con l'attesa a Forci durante il pranzo e "
        "la degustazione. Carburante, pedaggi, parcheggi e assicurazione completa. Il percorso alternativo "
        "alla frana non comporta alcun sovrapprezzo, e l'accesso a Tenuta di Forci non prevede oneri."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il pranzo, la degustazione e le mance alla tenuta. Attesa oltre le 17:00, € 50,00 all'ora per "
        "mezzo. Soste aggiuntive o modifiche al percorso, quotate su richiesta. L'eventuale navetta in "
        "auto fra il B&amp;B e Piazzale Boccherini, che possiamo organizzare e quotare a parte."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto del 30% sul totale, alla conferma", "€ 219,00", ""),
        ("Saldo, entro 5 giorni dal servizio", "€ 511,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>La frana e il percorso per Forci: ve lo confermiamo.</b> La via per Pieve Santo Stefano — la "
         "salita che si prende da Sant'Alessio dopo il ponte sul Serchio, la strada normale per la tenuta — "
         "è interrotta da una frana, e il Comune di Lucca ci ha aperto un cantiere da 780.000 euro fra pali "
         "e tiranti per rimettere in sicurezza il versante. Il collegamento resta però garantito dalle due "
         "strade alternative indicate dal Comune, <b>via Piana e via delle Foreste</b>, che salgono da "
         "Mutigliano: sono aperte e le percorriamo con il Beluga senza alcun sovrapprezzo. Sono strade di "
         "collina strette, ed è esattamente il motivo per cui vi proponiamo un mezzo da 7,64 metri e non un "
         "autobus gran turismo, che lì non passerebbe. Prima del servizio facciamo comunque un sopralluogo "
         "sul percorso e ricontrolliamo le ordinanze del Comune nei giorni precedenti: se il cantiere "
         "cambiasse le carte in tavola ve lo diremmo per tempo, con la soluzione già pronta."),
        ("<b>Dove vi carichiamo a Lucca.</b> Alla porta del B&amp;B La Bohème non possiamo arrivare: via del "
         "Moro è a due passi da piazza San Michele, nel cuore della città murata, e un mezzo di questa "
         "taglia lì non entra. Il punto di carico e scarico autorizzato più vicino è <b>Piazzale "
         "Boccherini</b>, appena dentro Porta Sant'Anna: sono circa 500 metri dal B&amp;B, sei o sette "
         "minuti a piedi in piano lungo via San Paolino, tutto dritto e senza scale. Gli altri punti "
         "autorizzati per i bus — Porta San Pietro, Porta Santa Maria, Porta Elisa — sono più lontani "
         "da via del Moro. Se qualcuno dei vostri ospiti "
         "facesse fatica a camminare, possiamo organizzare una navetta in auto dalla porta del B&amp;B al "
         "piazzale: ditecelo e ve la quotiamo."),
        ("<b>Il permesso di accesso a Lucca.</b> Il Comune di Lucca subordina l'ingresso dei bus turistici "
         "nella zona verde a un permesso da acquistare prima dell'accesso, e Piazzale Boccherini è dentro "
         "quell'area. Ce ne occupiamo noi e lo anticipiamo per vostro conto: lo trovate in preventivo "
         "come voce a parte, € 180,00 senza IVA, perché è un onere del Comune e non un nostro servizio. "
         "Meglio così che nasconderlo nel prezzo. È l'unico onere di accesso del programma: "
         "Tenuta di Forci non ne prevede."),
        ("<b>Un solo mezzo, come chiedevate.</b> Il Beluga ha 26 posti passeggeri: i vostri 24 ci stanno "
         "tutti, con due posti liberi, su un mezzo privato riservato al solo vostro gruppo. È anche la "
         "risposta giusta per quella strada, perché un unico mezzo da 7,64 metri passa dove due mezzi più "
         "grandi creerebbero problemi. Se il numero dovesse crescere oltre i 26 passeggeri avvisateci "
         "subito, perché cambierebbe l'organizzazione e il preventivo."),
        ("<b>L'attesa durante il pranzo è già compresa nel prezzo.</b> Non stiamo quotando due "
         "trasferimenti separati con l'attesa a parte: mezzo e conducente restano a Forci per tutte le ore "
         "del pranzo e della degustazione, e il prezzo le comprende. Abbiamo costruito il preventivo sulla "
         "ripartenza più tarda fra quelle che ci avete indicato, le 16:00, e teniamo il mezzo impegnato "
         "fino alle 17:00: se il pranzo si allunga di mezz'ora non pagate nulla in più."),
        ("<b>Lo spazio di manovra alla tenuta.</b> Gli ultimi sette chilometri fino a Forci sono in salita "
         "e la tenuta è grande, 360 ettari fra bosco, vigne e oliveti. Fatevi confermare dalla tenuta il "
         "punto esatto dove far scendere il gruppo, lo spazio per far girare un mezzo da 7,64 metri e dove "
         "il conducente può lasciare il minibus durante il pranzo. Se preferite li chiamiamo noi, basta il "
         "nome del vostro riferimento a Forci: molto meglio chiarirlo ora che il giorno stesso."),
        ("<b>Nessun pernottamento del conducente.</b> Il servizio si esaurisce in mezza giornata e il "
         "conducente rientra alla base la sera stessa: non c'è vitto né alloggio a vostro carico e su "
         "questa voce non arriverà alcun addebito. Lo scriviamo perché sui programmi di più giorni è una "
         "spesa che resta al cliente: qui non si pone."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, un recapito telefonico o "
         "WhatsApp della persona che viaggia con il gruppo, l'orario di ripartenza da Forci che preferite "
         "fra le 15:30 e le 16:00, la conferma che Piazzale Boccherini vi va bene come punto di ritrovo e "
         "i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il 7 ottobre il mezzo è libero e lo teniamo per voi "
         "per tutta la validità del preventivo; la prenotazione diventa definitiva alla "
         "ricezione dell'acconto. Cancellazione gratuita oltre 60 giorni prima del servizio; da 60 a "
         "30 giorni si trattiene l'acconto; da 30 a 10 giorni il 50%; negli ultimi 10 giorni il 100%. "
         "Mancando oggi 47 giorni al servizio, questa prenotazione ricade nella "
         "fascia da 60 a 30 giorni, e dal 7 settembre passerà in quella da 30 a 10. "
         "Preventivo valido fino al 4 settembre 2026."),
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
    subtitle="Lucca · Tenuta di Forci · Lucca, vehicle and driver at your disposal  ·  Wednesday 7 October 2026",
    meta="Prepared for %s  ·  21 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "One private minibus for your group of 24, reserved for your party for the whole of the service."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 24 guests on board two seats stay free. The 7.64 m is the reason we can confirm Forci for "
        "you: both the diversion around the landslide and the seven-kilometre climb up to the estate are "
        "narrow hill roads that a full-size coach cannot manage. No other group travels with you."
    ),
    h_servizio="The service",
    svc_head=["Time", "Route", "Duration"],
    svc=[
        ("11:45",
         "<b>Meeting point in Lucca, Piazzale Boccherini</b>, just inside Porta Sant'Anna. The driver is "
         "there a quarter of an hour early, with the GiroMunna sign.",
         "—"),
        ("12:00",
         "<b>Piazzale Boccherini → Tenuta di Forci</b>, Via della Pieve Santo Stefano. About 15 km by the "
         "diversion around the landslide, climbing from Mutigliano; arrival at the estate around 12:35.",
         "approx. 35 min"),
        ("12:35 – 16:00",
         "<b>Vehicle and driver stay at Forci</b>, at your disposal throughout the lunch and the tasting. "
         "The waiting time is included in the price.",
         "approx. 3 h 25"),
        ("16:00",
         "<b>Tenuta di Forci → Lucca, Piazzale Boccherini.</b> The same route back, arriving around 16:40. "
         "If you would rather leave at 15:30, the price is unchanged.",
         "approx. 40 min"),
    ],
    svc_foot="Vehicle engaged approx. 11:45 – 17:00. Distances and times are road estimates, excluding traffic.",
    h_prezzo="The price",
    price_rows=[
        ("Wed 7 Oct — Lucca → Tenuta di Forci → Lucca, vehicle and driver at your disposal from 11:45 to "
         "17:00, waiting time during lunch included", "€ 500.00", "+ VAT 10%"),
        ("VAT 10% on the service", "€ 50.00", ""),
        ("City of Lucca access permit for tourist coaches, which we advance on your behalf",
         "€ 180.00", "<i>not subject to VAT</i>"),
        ("Driver's board and lodging", "<i>not required</i>", ""),
    ],
    price_total_label="Total payable",
    price_total="€ 730.00",
    vat_note="",
    grand="Total payable: € 730.00.",
    perhead=("€ 550.00 for the service, VAT 10% included, plus the € 180.00 municipal permit, no VAT. "
             "About € 30.40 per person."),
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole period set out above, with the wait at Forci during the lunch "
        "and the tasting. Fuel, tolls, parking and full insurance. The diversion around the landslide "
        "carries no surcharge, and there is no access fee at Tenuta di Forci."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The lunch, the tasting and gratuities at the estate. Waiting beyond 17:00, € 50.00 per hour per "
        "vehicle. Additional stops or changes to the route, quoted on request. Any car shuttle between the "
        "B&amp;B and Piazzale Boccherini, which we can arrange and quote separately."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit of 30% of the total, on confirmation", "€ 219.00", ""),
        ("Balance, within 5 days of the service", "€ 511.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The landslide and the route to Forci — we confirm it.</b> The via per Pieve Santo Stefano — "
         "the climb taken from Sant'Alessio after the bridge over the Serchio, the normal road to the "
         "estate — is cut by a landslide, and the City of Lucca has a € 780,000 site open there, piling "
         "and tie-backs to stabilise the slope for good. The connection is nonetheless maintained by the "
         "two alternative roads the City indicates, <b>via Piana and via delle Foreste</b>, which climb "
         "from Mutigliano: they are open and we drive them with the Beluga at no surcharge. They are "
         "narrow hill roads, and that is precisely why we are offering you a 7.64 m vehicle rather than a "
         "full-size coach, which would not get through. We will still drive the route ourselves before the "
         "service and re-check the City's traffic orders in the days beforehand: if the works changed the "
         "picture we would tell you in good time, with the alternative already worked out."),
        ("<b>Where we pick you up in Lucca.</b> We cannot reach the door of the B&amp;B La Bohème: via del "
         "Moro is a few steps from piazza San Michele, in the heart of the walled city, and a vehicle of "
         "this size does not go in there. The nearest authorised loading and unloading point is "
         "<b>Piazzale Boccherini</b>, just inside Porta Sant'Anna: about 500 metres from the B&amp;B, six "
         "or seven minutes on the flat along via San Paolino, straight ahead and with no steps. The other "
         "authorised coach points — Porta San Pietro, Porta Santa Maria, Porta Elisa — are further from "
         "via del Moro. If any of your party "
         "finds walking difficult, we can arrange a car shuttle from the door of the B&amp;B to the square: "
         "tell us and we will quote it."),
        ("<b>The access permit for Lucca.</b> The City of Lucca requires tourist coaches entering the green "
         "zone to hold a permit bought before access, and Piazzale Boccherini sits inside that area. We "
         "take care of it and advance it on your behalf: you will find it in the quotation as a line of "
         "its own, € 180.00 with no VAT, because it is a charge of the City's and not a service of ours. "
         "Better that than buried in the price. It is the only access charge on this programme, as "
         "Tenuta di Forci has none."),
        ("<b>One vehicle, as you asked.</b> The Beluga has 26 passenger seats: your 24 all fit, with two "
         "seats to spare, on a private vehicle reserved for your group alone. It is also the right answer "
         "for that road, because a single 7.64 m vehicle gets through where two larger ones would cause "
         "trouble. If the number grows beyond 26 passengers, tell us straight away, as it would change "
         "both the arrangement and the price."),
        ("<b>The waiting time during lunch is already in the price.</b> We are not quoting two separate "
         "transfers with the waiting charged on top: vehicle and driver stay at Forci for the whole of the "
         "lunch and the tasting, and the price covers it. We have built the quotation on the later of the "
         "departure times you gave us, 16:00, and we hold the vehicle until 17:00: if lunch runs half an "
         "hour long, you pay nothing more."),
        ("<b>Manoeuvring space at the estate.</b> The last seven kilometres up to Forci climb, and the "
         "estate is a large one — 360 hectares of woods, vineyards and olive groves. Please have the "
         "estate confirm the exact point where the group can be set down, the space to turn a 7.64 m "
         "vehicle, and where the driver can leave the minibus during lunch. We are happy to call them "
         "ourselves: just give us the name of your contact at Forci. Far better settled now than on the "
         "day."),
        ("<b>No overnight stay for the driver.</b> The service is over within half a day and the driver "
         "returns to base the same evening: there is no board or lodging at your charge and nothing will "
         "be billed on that account. We put it in writing because on multi-day programmes it is a cost "
         "that stays with the client, and here we want it clear that it does not arise."),
        ("<b>To confirm we need</b> the final passenger count, a mobile or WhatsApp contact for the person "
         "travelling with the group, which departure time from Forci you prefer between 15:30 and 16:00, "
         "confirmation that Piazzale Boccherini suits you as the meeting point, and your invoicing "
         "details."),
        ("<b>Availability and cancellation.</b> The vehicle is free on 7 October and we hold it for you "
         "for the whole validity of this quotation; the booking becomes firm on receipt of the deposit. "
         "Cancellation is free of charge more than 60 days before the service; from 60 to 30 days the "
         "deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. "
         "With 47 days to the service today, this booking falls in the 60-to-30-day band, and from "
         "7 September it moves into the 30-to-10 band. Quotation valid until 4 September 2026."),
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
                               textColor=MUTED, leading=12, spaceAfter=11),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5,
                             textColor=GREEN, leading=15, spaceBefore=10, spaceAfter=5),
        "body": ParagraphStyle("body", alignment=TA_JUSTIFY, spaceAfter=5, **base),
        "cell": ParagraphStyle("cell", **base),
        "cellsm": ParagraphStyle("cellsm", fontName="Helvetica", fontSize=8.6,
                                 textColor=INK, leading=12),
        "cellmut": ParagraphStyle("cellmut", fontName="Helvetica", fontSize=8.6,
                                  textColor=MUTED, leading=12),
        "th": ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=7.6,
                             textColor=GREEN, leading=10),
        "grand": ParagraphStyle("grand", fontName="Helvetica-Bold", fontSize=11.5,
                                textColor=GREEN, leading=15, spaceBefore=8),
        "note": ParagraphStyle("note", alignment=TA_JUSTIFY, spaceAfter=3,
                               leftIndent=9, fontName="Helvetica", fontSize=8.8,
                               textColor=INK, leading=11.4),
        "small": ParagraphStyle("small", alignment=TA_JUSTIFY, spaceAfter=3,
                                fontName="Helvetica", fontSize=8.8,
                                textColor=INK, leading=11.8),
        "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=8.2,
                               textColor=MUTED, leading=11.6, spaceBefore=6),
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
    for when, desc, dur in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % when, S["cellsm"]),
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
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    F.append(t)
    F.append(Paragraph(L["svc_foot"], S["foot"]))

    # --- prezzo (intestazione e tabella non si spezzano fra due pagine)
    # terza colonna larga: deve contenere "fuori campo IVA" su una riga sola
    pcols = [usable - 30 * mm - 28 * mm, 30 * mm, 28 * mm]
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
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
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
    # la colonna IVA e' piu' larga di quella del prezzo: "VAT included" non deve andare a capo
    ycols = [usable - 30 * mm - 26 * mm, 30 * mm, 26 * mm]
    ydata = [[Paragraph(a, S["cellsm"]), Paragraph("<b>%s</b>" % b, S["cellsm"]),
              Paragraph(c, S["cellmut"])] for a, b, c in L["pay_rows"]]
    yt = Table(ydata, colWidths=ycols)
    yt.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    F.append(KeepTogether([
        Paragraph(L["h_pagamento"], S["h2"]),
        yt,
        Spacer(1, 6),
        Paragraph(L["bank"], S["small"]),
    ]))

    # --- note
    F.append(Paragraph(L["h_note"], S["h2"]))
    for n in L["note"]:
        F.append(Paragraph("·  " + n, S["note"]))

    F.append(Spacer(1, 3))
    F.append(Paragraph(L["closing"], S["small"]))

    doc.build(F)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--cliente", "--client", dest="cliente", default="Ray Zeoli")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Lucca_Tenuta_di_Forci_7_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

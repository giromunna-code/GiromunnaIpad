#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il tour della Toscana in giornata, 12 passeggeri,
quattro itinerari a scelta, carico e scarico all'Hotel Adamas di Firenze.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_tour_toscana.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_tour_toscana.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0821-MG"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Tour della Toscana in giornata, quattro itinerari a scelta  ·  12 passeggeri  ·  partenza e rientro a Firenze",
    meta="Preparato per %s  ·  21 agosto 2026  ·  Rif. " + RIF,

    h_mezzo="Il mezzo",
    mezzo_intro=("Un minibus con conducente per il vostro gruppo di 12 persone, a vostra disposizione "
                 "per l'intera giornata, con lo stesso autista dalla partenza al rientro."),
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
        "L'Hotel Adamas è in Via Ricasoli 9, a pochi passi dal Duomo, nel cuore della zona a traffico limitato. "
        "Conviene chiarirlo subito, perché è il punto vero della vostra richiesta: <b>la ZTL bus di Firenze copre "
        "tutto il centro abitato, ventiquattro ore su ventiquattro, tutti i giorni dell'anno</b>, e riguarda ogni "
        "veicolo per trasporto passeggeri con più di nove posti. Vale per il nostro minibus da 26 esattamente come "
        "varrebbe per uno sprinter da 12 o da 16: non è un limite del mezzo che vi proponiamo, è il regime della "
        "città. Sotto l'hotel non si carica, e nessun operatore serio vi dirà il contrario. Ecco come si risolve."
    ),
    carico_head=["Soluzione", "Come funziona", "Costo"],
    carico=[
        ("Navetta van<br/><b>la consigliamo</b>",
         "Due van fino a nove posti — che nella ZTL entrano regolarmente — vi prendono davanti all'hotel e vi portano "
         "al minibus in Piazza Vittorio Veneto: dieci minuti di percorso. Lo stesso servizio a fine giornata, "
         "per riportarvi all'ingresso dell'hotel.",
         "€ 320,00 + IVA<br/>andata e ritorno"),
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
         "<b>Circa 195 km.</b>",
         "circa<br/>08:30 – 19:00"),
        ("B<br/>Pisa, Siena e<br/>San Gimignano",
         "<b>Firenze → Pisa → Siena → San Gimignano → Firenze.</b> Partenza alle 07:30: novanta chilometri fino a "
         "Pisa, poi 125 km attraversando la Toscana fino a Siena, 45 km a San Gimignano e 55 km di rientro. Quattro "
         "tappe e oltre cinque ore di sola guida, cui vanno aggiunte le soste. È di gran lunga la giornata più lunga "
         "delle quattro: nelle note vi spieghiamo perché vi conviene alleggerirla. <b>Circa 315 km.</b>",
         "circa<br/>07:30 – 20:00"),
        ("C<br/>Siena, San Gimignano<br/>e Monteriggioni",
         "<b>Firenze → Siena → San Gimignano → Monteriggioni → Firenze.</b> Partenza alle 08:30 e 75 km fino a Siena; "
         "poi 45 km a San Gimignano, 30 km a Monteriggioni e 55 km di rientro, in città verso le 19:00. Vi proponiamo "
         "di girare l'ordine delle tappe, mettendo Monteriggioni per primo: nelle note trovate il perché. "
         "<b>Circa 205 km, che diventano 170 nell'ordine che consigliamo.</b>",
         "circa<br/>08:30 – 19:00"),
        ("D<br/>Montalcino, Pienza<br/>e Montepulciano",
         "<b>Firenze → Montalcino → Pienza → Montepulciano → Firenze.</b> Partenza alle 08:00 e 110 km fino a "
         "Montalcino, arrivo verso le 09:45. Venticinque chilometri a Pienza e altri 15 a Montepulciano, nel cuore "
         "della Val d'Orcia; rientro dall'autostrada della Valdichiana, 120 km, a Firenze verso le 19:45. La giornata "
         "più bella delle quattro e la più impegnativa a piedi: tre borghi in collina. <b>Circa 270 km.</b>",
         "circa<br/>08:00 – 20:00"),
    ],
    svc_note=("Distanze e tempi di percorrenza sono stime stradali, traffico escluso. Gli orari sono la nostra "
              "proposta: li ricalcoliamo volentieri sull'ora di partenza che preferite."),

    h_prezzo="Il prezzo",
    price_head=["Itinerario — una giornata intera, tutto compreso", "Al netto", "IVA 10% inclusa"],
    price_rows=[
        ("<b>A</b> · Firenze → Pisa → Lucca → Firenze — circa 195 km", "€ 1.380,00", "€ 1.518,00"),
        ("<b>B</b> · Firenze → Pisa → Siena → San Gimignano → Firenze — circa 315 km", "€ 1.950,00", "€ 2.145,00"),
        ("<b>C</b> · Firenze → Siena → San Gimignano → Monteriggioni → Firenze — circa 205 km", "€ 1.550,00", "€ 1.705,00"),
        ("<b>D</b> · Firenze → Montalcino → Pienza → Montepulciano → Firenze — circa 270 km", "€ 1.620,00", "€ 1.782,00"),
        ("Navetta van fra l'hotel e il punto di carico, andata e ritorno — <i>opzionale</i>", "€ 320,00", "€ 352,00"),
        ("Vitto del conducente", "<i>a carico vostro</i>", "—"),
    ],
    grand=("Gli importi sono per l'intera giornata e per tutto il gruppo, non a persona: in dodici, "
           "da €&nbsp;126,50 a €&nbsp;178,75 a testa secondo l'itinerario."),
    perhead=("Si conferma un itinerario solo, quello che sceglierete. Il prezzo comprende tutti gli oneri di accesso, "
             "compreso il permesso ZTL bus di Firenze e, negli itinerari che toccano Siena, il permesso comunale per "
             "i bus turistici: il giorno del servizio non vi verrà chiesto nulla di aggiuntivo."),

    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi autostradali, assicurazione completa e "
        "movimentazione bagagli. Sono compresi anche tutti gli oneri di accesso: il permesso ZTL bus di Firenze, che "
        "il nostro mezzo paga nella fascia sotto gli 8 metri; il parcheggio bus di Pisa negli itinerari A e B; il "
        "permesso comunale per i bus turistici di Siena negli itinerari B e C; i parcheggi autorizzati dei borghi "
        "della Val d'Orcia nell'itinerario D."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il vitto del conducente, che resta a vostro carico. Ingressi ai monumenti, guide, degustazioni, pasti e "
        "mance. La navetta van da e per l'hotel, che trovate come voce opzionale nel listino. Attesa oltre gli orari "
        "concordati, € 50,00 all'ora. Soste aggiuntive o modifiche all'itinerario decise in corso di giornata, "
        "quotate a parte. Rientro dopo le 02:00, € 250,00."
    ),

    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 455,40 – € 643,50", "secondo l'itinerario scelto"),
        ("Saldo, entro 5 giorni dal servizio", "il restante 70%", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),

    h_note="Note",
    note=[
        ("<b>Sotto l'hotel non si carica, e non è una questione del nostro mezzo.</b> La ZTL bus di Firenze vale su "
         "tutto il centro abitato, ventiquattro ore su ventiquattro, e comprende qualsiasi veicolo per trasporto "
         "passeggeri oltre i nove posti: il nostro minibus da 26 come uno sprinter da 12 o da 16. Via Ricasoli, poi, "
         "è stretta e a due passi dal Duomo. Il carico e lo scarico si fanno nei punti autorizzati dal Comune, e il "
         "più vicino all'Adamas fra quelli che consentono anche la salita è Piazza Vittorio Veneto, verso le Cascine, "
         "a circa 2,5 km. Piazza Savonarola è più vicina — 1,4 km, una ventina di minuti a piedi — ma è autorizzata "
         "alla sola discesa e solo dalle 08:00 alle 20:00: va bene per il rientro serale, non per la partenza."),
        ("<b>La navetta van: sì, la organizziamo.</b> È la risposta alla vostra domanda ed è la soluzione che vi "
         "consigliamo, soprattutto la mattina presto e alla fine di una giornata lunga. I veicoli fino a nove posti "
         "non ricadono nella ZTL bus e arrivano davanti all'hotel: per dodici persone servono due van, che vi portano "
         "al minibus in dieci minuti. L'abbiamo quotata € 320,00 + IVA andata e ritorno. Una precisazione che "
         "preferiamo farvi subito: i van non sono mezzi nostri, li mettiamo a disposizione tramite un collega di "
         "Firenze, quindi li confermiamo insieme alla prenotazione e non prima."),
        ("<b>L'itinerario B chiede troppo a una giornata sola.</b> Pisa sta a ovest, Siena e San Gimignano a sud: "
         "metterli insieme significa 315 chilometri e oltre cinque ore di sola guida, cui vanno aggiunte le soste. "
         "Partendo alle 07:30 si rientra verso le 20:00, e in mezzo restano due ore a Pisa, tre a Siena — pranzo "
         "compreso — e due a San Gimignano: il minimo per tre luoghi di quel calibro. Dodici ore e mezza fuori, per "
         "una famiglia, sono tante. Ve lo quotiamo lo stesso perché ce lo avete "
         "chiesto, ma se volete il nostro parere: togliete Pisa e avete l'itinerario C, oppure tenete Pisa e "
         "abbinatela a Lucca, che è l'itinerario A. Sono due giornate belle invece di una corsa."),
        ("<b>L'itinerario C conviene girarlo.</b> Monteriggioni si trova sulla superstrada Firenze-Siena, "
         "praticamente sulla strada dell'andata, mentre nell'ordine che ci avete indicato ci si arriva tornando "
         "indietro da San Gimignano. Facendo Firenze → Monteriggioni → Siena → San Gimignano → Firenze si scende a "
         "170 km invece di 205 e si guadagna quasi un'ora, che sul posto vale molto più che in autostrada. "
         "Il prezzo non cambia: € 1.550,00 in entrambi i casi."),
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
        ("<b>Per confermare ci serve prima di tutto la data.</b> Abbiamo un solo minibus e in alta stagione le "
         "giornate si esauriscono con settimane di anticipo: finché non abbiamo il giorno non possiamo bloccare "
         "nulla. I prezzi qui sopra sono riferiti a una giornata di media stagione; per i fine settimana di alta "
         "stagione e i periodi di ponte possono muoversi, e ve lo diremmo subito. Con la data ci servono anche "
         "l'itinerario scelto, l'ora di partenza, il numero definitivo di passeggeri, se volete la navetta van, un "
         "recapito telefonico o WhatsApp di chi viaggia con la famiglia e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> La prenotazione diventa definitiva alla ricezione dell'acconto. "
         "La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene trattenuto "
         "l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. "
         "Preventivo valido fino al 20 settembre 2026."),
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
    subtitle="Full-day tour of Tuscany, four itineraries to choose from  ·  12 passengers  ·  departing and returning in Florence",
    meta="Prepared for %s  ·  21 August 2026  ·  Ref. " + RIF,

    h_mezzo="The vehicle",
    mezzo_intro=("One minibus with driver for your group of 12, at your disposal for the whole day, "
                 "with the same driver from departure to return."),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "You asked for a Sprinter of sufficient capacity or a minibus: ours is a 26-seat minibus, so with 12 guests "
        "on board everyone travels with the seat beside them free and bags stay in the hold rather than around "
        "people's feet. On a ten-hour day, with three or four stops and the Tuscan summer heat, that difference "
        "tells. And 7.64 m is the right size for this region: it reaches the coach bays at San Gimignano, "
        "Monteriggioni and Montepulciano where a 13-metre coach cannot go, and in Florence it falls into the "
        "under-8-metre permit band, which costs less."
    ),

    h_carico="The pick-up point",
    carico_intro=(
        "Hotel Adamas is at Via Ricasoli 9, a few steps from the Duomo, in the heart of the limited traffic zone. "
        "This is worth settling straight away, because it is the real substance of your enquiry: <b>Florence's coach "
        "ZTL covers the entire built-up area, twenty-four hours a day, every day of the year</b>, and it applies to "
        "any passenger vehicle with more than nine seats. It applies to our 26-seat minibus exactly as it would to a "
        "12- or 16-seat Sprinter: this is not a limitation of the vehicle we are offering, it is the city's regime. "
        "There is no picking up at the hotel door, and no serious operator will tell you otherwise. Here is how it "
        "is solved."
    ),
    carico_head=["Option", "How it works", "Cost"],
    carico=[
        ("Van shuttle<br/><b>our recommendation</b>",
         "Two vans of up to nine seats — which are allowed into the ZTL — collect you outside the hotel and take you "
         "to the minibus at Piazza Vittorio Veneto: a ten-minute run. The same service at the end of the day, to "
         "bring you back to the hotel door.",
         "€ 320.00 + VAT<br/>return"),
        ("Taxis, booked by reception",
         "Three taxis for twelve people, same route: taxis are also allowed into the ZTL. Reception at the Adamas "
         "books them the evening before and you pay them directly on the spot.",
         "about € 20.00<br/>per taxi, each way"),
        ("On foot, evening only",
         "On the way back the minibus sets you down at Piazza Savonarola, the authorised point nearest the hotel: "
         "1.4 km, about twenty minutes on foot. It is authorised for setting down only and only between 08:00 and "
         "20:00, so it serves the return, never the departure.",
         "no charge"),
    ],
    carico_close=(
        "The morning meeting point is <b>Piazza Vittorio Veneto</b>, by Ponte della Vittoria: it is authorised for "
        "both picking up and setting down twenty-four hours a day, without the restrictions on hours or type of "
        "service that apply to the other points near the centre. The driver waits for you there with the GiroMunna sign."
    ),

    h_servizio="The service",
    svc_head=["Itinerary", "Route and programme", "Vehicle engaged"],
    svc=[
        ("A<br/>Pisa and Lucca",
         "<b>Florence → Pisa → Lucca → Florence.</b> Meeting point 08:30 at Piazza Vittorio Veneto. Ninety kilometres "
         "to Pisa, arriving around 09:45; the vehicle waits at the Via Pietrasantina coach terminal, ten minutes on "
         "foot from Piazza dei Miracoli. Departure at 12:30 and 25 km to Lucca, where the vehicle stops outside the "
         "walls and you walk into the centre. Return at 17:30, 80 km of motorway, back in Florence around 18:45. "
         "<b>About 195 km.</b>",
         "approx.<br/>08:30 – 19:00"),
        ("B<br/>Pisa, Siena and<br/>San Gimignano",
         "<b>Florence → Pisa → Siena → San Gimignano → Florence.</b> Departure at 07:30: ninety kilometres to Pisa, "
         "then 125 km across Tuscany to Siena, 45 km to San Gimignano and 55 km back. Four stops and over five hours "
         "of driving alone, before the visits themselves. By far the longest of the four days: the notes explain why "
         "it is worth lightening. <b>About 315 km.</b>",
         "approx.<br/>07:30 – 20:00"),
        ("C<br/>Siena, San Gimignano<br/>and Monteriggioni",
         "<b>Florence → Siena → San Gimignano → Monteriggioni → Florence.</b> Departure at 08:30 and 75 km to Siena; "
         "then 45 km to San Gimignano, 30 km to Monteriggioni and 55 km back, into town around 19:00. We suggest "
         "reversing the order of the stops, putting Monteriggioni first: the notes explain why. "
         "<b>About 205 km, which becomes 170 in the order we recommend.</b>",
         "approx.<br/>08:30 – 19:00"),
        ("D<br/>Montalcino, Pienza<br/>and Montepulciano",
         "<b>Florence → Montalcino → Pienza → Montepulciano → Florence.</b> Departure at 08:00 and 110 km to "
         "Montalcino, arriving around 09:45. Twenty-five kilometres to Pienza and another 15 to Montepulciano, in "
         "the heart of the Val d'Orcia; back on the Valdichiana motorway, 120 km, into Florence around 19:45. The "
         "finest of the four days and the most demanding on foot: three hilltop towns. <b>About 270 km.</b>",
         "approx.<br/>08:00 – 20:00"),
    ],
    svc_note=("Distances and journey times are road estimates, traffic excluded. The times shown are our proposal: "
              "we will gladly recalculate around whatever departure time you prefer."),

    h_prezzo="The price",
    price_head=["Itinerary — one full day, everything included", "Excl. VAT", "VAT 10% included"],
    price_rows=[
        ("<b>A</b> · Florence → Pisa → Lucca → Florence — about 195 km", "€ 1,380.00", "€ 1,518.00"),
        ("<b>B</b> · Florence → Pisa → Siena → San Gimignano → Florence — about 315 km", "€ 1,950.00", "€ 2,145.00"),
        ("<b>C</b> · Florence → Siena → San Gimignano → Monteriggioni → Florence — about 205 km", "€ 1,550.00", "€ 1,705.00"),
        ("<b>D</b> · Florence → Montalcino → Pienza → Montepulciano → Florence — about 270 km", "€ 1,620.00", "€ 1,782.00"),
        ("Van shuttle between the hotel and the pick-up point, return — <i>optional</i>", "€ 320.00", "€ 352.00"),
        ("Driver's meals", "<i>at your charge</i>", "—"),
    ],
    grand=("The amounts are for the whole day and the whole group, not per person: split twelve ways, "
           "from €&nbsp;126.50 to €&nbsp;178.75 each depending on the itinerary."),
    perhead=("Only one itinerary is confirmed — whichever you choose. The price covers every access charge, including "
             "the Florence coach ZTL permit and, on the itineraries that take in Siena, the municipal tourist coach "
             "permit: nothing further will be asked of you on the day of service."),

    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, fuel, motorway tolls, full insurance and luggage handling. All access "
        "charges are included too: the Florence coach ZTL permit, which our vehicle pays in the under-8-metre band; "
        "the Pisa coach park on itineraries A and B; the municipal tourist coach permit for Siena on itineraries B "
        "and C; the authorised coach parks of the Val d'Orcia towns on itinerary D."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meals, which remain at your charge. Entrance fees, guides, tastings, meals and gratuities. "
        "The van shuttle to and from the hotel, which appears as an optional line in the price list. Waiting beyond "
        "the agreed times, € 50.00 per hour. Additional stops or changes to the itinerary decided during the day, "
        "quoted separately. Return after 02:00, € 250.00."
    ),

    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 455.40 – € 643.50", "depending on the itinerary"),
        ("Balance, within 5 days of the service", "the remaining 70%", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),

    h_note="Notes",
    note=[
        ("<b>There is no picking up at the hotel door, and it is not a question of our vehicle.</b> Florence's coach "
         "ZTL applies across the whole built-up area, twenty-four hours a day, and covers any passenger vehicle over "
         "nine seats: our 26-seat minibus just as much as a 12- or 16-seat Sprinter. Via Ricasoli, moreover, is "
         "narrow and two steps from the Duomo. Picking up and setting down happen at the points authorised by the "
         "city, and the nearest one to the Adamas that also allows picking up is Piazza Vittorio Veneto, towards the "
         "Cascine, about 2.5 km away. Piazza Savonarola is closer — 1.4 km, about twenty minutes on foot — but it is "
         "authorised for setting down only, and only from 08:00 to 20:00: fine for the evening return, not for the "
         "morning departure."),
        ("<b>The van shuttle: yes, we can arrange it.</b> This is the answer to your question and the solution we "
         "recommend, particularly first thing in the morning and at the end of a long day. Vehicles of up to nine "
         "seats fall outside the coach ZTL and reach the hotel door: for twelve people that means two vans, taking "
         "you to the minibus in ten minutes. We have quoted it at € 320.00 + VAT for the return trip. One point we "
         "would rather make now than later: the vans are not our own vehicles, we provide them through a colleague "
         "in Florence, so we confirm them together with the booking and not before."),
        ("<b>Itinerary B asks too much of a single day.</b> Pisa lies west, Siena and San Gimignano south: putting "
         "them together means 315 kilometres and over five hours of driving alone, before the visits. Leaving at "
         "07:30 you would be back around 20:00, and in between you are left with two hours in Pisa, three in Siena — "
         "lunch included — and two in San Gimignano: the bare minimum for three places of that calibre. Twelve and a "
         "half hours out, for a family, is a great deal. We have quoted it "
         "all the same because you asked, but if you want our view: drop Pisa and you have itinerary C, or keep Pisa "
         "and pair it with Lucca, which is itinerary A. That is two good days rather than one long dash."),
        ("<b>Itinerary C is worth reversing.</b> Monteriggioni sits on the Florence-Siena expressway, essentially on "
         "the outward road, whereas in the order you set out you reach it doubling back from San Gimignano. Running "
         "Florence → Monteriggioni → Siena → San Gimignano → Florence brings the day down to 170 km instead of 205 "
         "and saves almost an hour, which is worth far more on the ground than on the motorway. The price is "
         "unchanged: € 1,550.00 either way."),
        ("<b>The hill towns are earned on foot.</b> Siena, San Gimignano, Monteriggioni, Montalcino, Pienza and "
         "Montepulciano all close their historic centres to coaches: you are set down at the authorised parks just "
         "outside the walls and walk up. At Montepulciano the climb from the coach park to Piazza Grande is steep "
         "and takes about twenty minutes. If the family includes elderly travellers, small children or anyone who "
         "finds walking difficult, tell us before confirming: it changes the set-down points we request and, in some "
         "cases, the order of the stops."),
        ("<b>Driver's meals, and no overnight stay.</b> The day starts and ends in Florence, so the driver returns "
         "to base and there is no night to book. Lunch remains, and under our terms it stays at your charge: the "
         "simplest arrangement is that he eats wherever the group stops, otherwise we agree a fixed amount in "
         "advance. We do not put it in the quotation because we do not arrange it."),
        ("<b>We will set the times together.</b> Those shown are our proposal, built around a full day and normal "
         "seasonal traffic: confirm the departure time you prefer and we will recalculate the rest. Waiting beyond "
         "the agreed times is charged at € 50.00 per hour. On itineraries B and D an early start is not a detail, it "
         "is the condition on which the day works."),
        ("<b>To confirm, what we need first of all is the date.</b> We have one minibus, and in high season the days "
         "go weeks in advance: until we have the date we cannot hold anything. The prices above are for a mid-season "
         "day; for high-season weekends and public holiday periods they may move, and we would tell you at once. "
         "Along with the date we also need the chosen itinerary, the departure time, the final passenger count, "
         "whether you want the van shuttle, a phone or WhatsApp contact for whoever travels with the family, and "
         "your invoicing details."),
        ("<b>Availability and cancellation.</b> The booking becomes firm on receipt of the deposit. Cancellation is "
         "free of charge more than 60 days before the service; from 60 to 30 days the deposit is retained; from 30 "
         "to 10 days 50% of the price is charged; in the last 10 days, 100%. "
         "This quotation is valid until 20 September 2026."),
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


def _grid(extra=()):
    """Bordi e spaziature comuni a tutte le tabelle del preventivo."""
    return TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ] + list(extra))


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
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--cliente", "--client", dest="cliente", default="Master Group Tour Operator")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Tour_Toscana_Giornaliero_12pax_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

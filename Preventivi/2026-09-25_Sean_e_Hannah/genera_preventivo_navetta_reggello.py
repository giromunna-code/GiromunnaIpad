#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la navetta del welcome event a Reggello del 25 settembre 2026.

Programma aggiornato al 9 settembre 2026 sullo schema dei punti di carico del cliente
(«FRIDAY — WELCOME EVENT»): 9 punti di carico, 50 ospiti, arrivo in location entro le 18:00,
rientri dalle 23:00. Il prezzo resta quello del preventivo dell'8 settembre.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_navetta_reggello.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_navetta_reggello.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0925-REGGELLO"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Noleggio con conducente — navetta per il welcome event  ·  Fattoria I Bonsi, Reggello (Firenze)  ·  venerdì 25 settembre 2026",
    meta="Preparato per %s  ·  programma aggiornato al 9 settembre 2026  ·  Rif. " + RIF + "  ·  valido fino al 15 settembre 2026",
    intro=(
        "Abbiamo riportato il programma sul vostro schema dei punti di carico del venerdì: nove indirizzi, "
        "50 ospiti, tutti in location entro le 18:00. <b>Il prezzo resta quello del preventivo dell'8 settembre</b>, "
        "invariato. Rispetto alla prima versione cambia solo il modo in cui i due minibus si dividono il lavoro: "
        "tre corse di raccolta invece di quattro, sui vostri indirizzi definitivi. Vi chiediamo di confermare due "
        "anticipi di orario e l'ordine di una corsa: sono spiegati fra i punti da confermare, in fondo."
    ),
    h_mezzi="I mezzi",
    mezzi=[
        ("Mezzo 1",
         "<b>Minibus Mercedes-Benz — 25+1+1</b> (25 posti passeggeri + capogruppo + autista), aria condizionata, "
         "frigo bar, sedili reclinabili, vano bagagli."),
        ("Mezzo 2",
         "<b>Minibus Mercedes-Benz — 27+1+1</b> (27 posti passeggeri + capogruppo + autista), aria condizionata, "
         "sedili reclinabili, vano bagagli."),
    ],
    mezzi_facts=[
        ("Posti", "50 ospiti distribuiti su tre corse: la più carica ne porta 21, su un mezzo da 25 posti. "
                  "Nessuna corsa va al limite e nessuno viaggia in piedi."),
        ("Tempo a bordo",
         "Dai 10 ai 25 minuti. Ogni corsa copre un gruppo di indirizzi vicini fra loro, così nessuno si fa tutto "
         "il giro di raccolta."),
        ("Conducenti", "Due autisti professionisti, uno per mezzo, in servizio per tutta la serata."),
    ],
    h_servizio="Il servizio — venerdì 25 settembre 2026",
    svc_intro=(
        "Tre corse di raccolta — due con il Mezzo 1 e una con il Mezzo 2 — così che tutti siano in location entro "
        "le 18:00. I mezzi restano poi alla Fattoria I Bonsi per tutta la serata e ripartono alle 23:00 con i "
        "rientri, sempre in tre corse. Gli orari sono i vostri, anticipati di un quarto d'ora sulle due corse dove "
        "non tenevano."
    ),
    svc_head=["Corsa", "Percorso", "Orario"],
    svc=[
        ("Mezzo 1<br/>prima corsa",
         "<b>I Trebbiali, Loc. I Trebbiali 116 (3)</b> → <b>Podere la Romola, Loc. Podere la Romola 78 (14)</b> → "
         "<b>location — Fattoria I Bonsi, Via Bonsi 47.</b> Arrivo verso le 17:15.",
         "dalle 16:50<br/>17 ospiti"),
        ("Mezzo 2<br/>corsa unica",
         "<b>La Terrazza di Reggello, Via di Fano 6 (2)</b> → <b>S. Giovenale, Loc. S. Giovenale 55 (2)</b> → "
         "<b>Podere Giusti, Loc. Giusti 105 (4)</b> → <b>Appartamento Olivella, Via Fornacina 32 (2)</b> → "
         "<b>Via dei Glicini 14, Poggio ai Giubbiani (2)</b> → <b>location, Via Bonsi 47.</b> "
         "Arrivo entro le 18:00.",
         "dalle 17:10<br/>12 ospiti"),
        ("Mezzo 1<br/>seconda corsa",
         "<b>Rovai, Loc. Rovai 26, Pietrapiana (3)</b> → <b>Casalino, Via Ponte di Casalino 66–68 (18)</b> — "
         "l'Hotel Archimede e Podere Casalino distano 120 m sulla stessa strada, quindi li serviamo come un'unica "
         "fermata → <b>location, Via Bonsi 47.</b> Arrivo entro le 18:00.",
         "dalle 17:20<br/>21 ospiti"),
        ("Entrambi i mezzi<br/>in location",
         "I minibus restano parcheggiati alla Fattoria I Bonsi per tutta la serata, a vostra disposizione con i "
         "conducenti.",
         "18:00 – 23:00"),
        ("Rientri<br/>tre corse",
         "Il <b>Mezzo 1</b> parte alle 23:00 con i 21 ospiti di Casalino e Rovai, tutti a casa verso le 23:25; "
         "rientra in location alle 23:35 e fa l'ultima corsa con i 17 di Podere la Romola e I Trebbiali, a casa "
         "verso le 23:55. Il <b>Mezzo 2</b> parte alle 23:00 con i 12 ospiti di Via di Fano, S. Giovenale, Podere "
         "Giusti, Via Fornacina e Via dei Glicini, tutti a casa verso le 23:35.",
         "dalle 23:00<br/>fino alle 23:55 ca."),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("<b>Trasporto — Mezzo 1</b> (minibus, 25+1+1). Due corse di raccolta da quattro punti — I Trebbiali, "
         "Podere la Romola, Rovai e la fermata unica di Casalino — mezzo e conducente a vostra disposizione in "
         "location dalle 18:00 alle 23:00, due corse di rientro agli stessi indirizzi. Carburante, pedaggi "
         "autostradali, parcheggi, assicurazione e movimentazione del mezzo da e per la nostra rimessa sono "
         "compresi.",
         "€ 1.100,00", "+ IVA 10%"),
        ("<b>Trasporto — Mezzo 2</b> (minibus, 27+1+1). Una corsa di raccolta da cinque punti — Via di Fano, "
         "S. Giovenale, Podere Giusti, Via Fornacina e Via dei Glicini — mezzo e conducente a vostra disposizione "
         "in location dalle 18:00 alle 23:00, una corsa di rientro agli stessi indirizzi. Stesse voci comprese "
         "della riga precedente.",
         "€ 1.100,00", "+ IVA 10%"),
        ("Cena dei due conducenti, in servizio dal pomeriggio a notte fonda",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.200,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.420,00.",
    price_note=(
        "Trasporto € 2.200,00 + IVA 10% (€ 220,00). <b>Il prezzo è quello del preventivo dell'8 settembre e non "
        "cambia</b>: le tre corse di raccolta e le tre di rientro sono tutte comprese. Prezzo fisso, nessun "
        "addebito ulteriore oltre a quanto elencato sotto «Non incluso»."
    ),
    permessi=(
        "<b>Nessun onere di accesso è dovuto per questo servizio.</b> Alcune città toscane fanno pagare ai bus un "
        "permesso giornaliero di accesso — Firenze, Siena, Lucca, Pisa — e sono cifre che arrivano a diverse "
        "centinaia di euro. Questo evento si svolge interamente nel Comune di Reggello, che non ha varchi di "
        "questo tipo, quindi nel preventivo non c'è nulla del genere. Se un onere dovesse risultare dovuto in "
        "qualche punto del percorso, ve lo diremmo prima e ve lo gireremmo al costo ufficiale, mai come sorpresa "
        "in fattura."
    ),
    h_incluso="Incluso",
    incluso=[
        "Due minibus e due autisti professionisti per tutta la serata, dal primo ritiro all'ultimo rientro.",
        "Tre corse di raccolta e tre di rientro, così che il tempo a bordo resti fra i 10 e i 25 minuti.",
        "Mezzi e conducenti a vostra disposizione in location dalle 18:00 alle 23:00.",
        "Carburante, pedaggi autostradali, parcheggi e assicurazione.",
        "Movimentazione dei due mezzi da e per la nostra rimessa, prima e dopo il servizio.",
        "Servizio in orario serale: gli ultimi ospiti vengono riaccompagnati intorno alle 23:55.",
        "Tutte le imposte dovute: l'IVA al 10% è esposta a parte qui sopra ed è già conteggiata nel totale da "
        "corrispondere.",
    ],
    h_nonincluso="Non incluso",
    nonincluso=[
        "Qualsiasi trasferimento in più rispetto a quelli descritti — per esempio un rientro anticipato per una "
        "parte del gruppo prima delle 23:00: possiamo organizzarlo, quotato a parte.",
        "Ospiti in più su una singola corsa. La più carica ne porta 21 su 25 posti, quindi un margine c'è, ma "
        "ogni indirizzo aggiunto cambia lo schema degli orari: segnalatecelo prima.",
        "<b>Cena dei due conducenti</b>, che resta a vostro carico: la prenotate e la pagate voi direttamente.",
        "Attesa oltre gli orari concordati: € 50,00 all'ora per mezzo.",
        "Rientro oltre le 02:00: € 250,00 per mezzo. Il programma si chiude verso le 23:55, quindi non è dovuto.",
        "Tutto quanto non espressamente indicato qui sopra.",
    ],
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 726,00", "IVA inclusa"),
        ("Saldo, entro il 20 settembre 2026", "€ 1.694,00", ""),
    ],
    pay_text=(
        "Il saldo è dovuto entro il 20 settembre 2026, cinque giorni prima del servizio. <b>La prenotazione "
        "diventa definitiva quando l'acconto arriva sul nostro conto</b>, non prima. Per l'intero importo viene "
        "emessa regolare fattura."
    ),
    bank=(
        "<b>Coordinate bancarie.</b> Bonifico bancario intestato a Munna Girolamo Giuseppe — "
        "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. Come causale indicate il vostro nome e il "
        "riferimento " + RIF + "."
    ),
    validita=(
        "<b>Validità.</b> Questo preventivo è valido fino al 15 settembre 2026. La data è vicina: fino ad allora "
        "teniamo bloccati per voi i due mezzi, dopo non possiamo garantirli."
    ),
    cancellazione=(
        "<b>Cancellazione.</b> Gratuita oltre 30 giorni prima del servizio. Da 30 a 10 giorni viene trattenuto "
        "l'acconto; da 10 a 3 giorni il 70% dell'importo; nelle ultime 72 ore il 100%. Mancando oggi meno di 30 "
        "giorni all'evento, una conferma ricade direttamente nella seconda fascia: in caso di cancellazione "
        "l'acconto viene trattenuto. Le cause di forza maggiore si valutano caso per caso."
    ),
    h_punti="Punti da confermare",
    punti=[
        "<b>Due corse partono un quarto d'ora prima delle vostre.</b> Nel vostro schema il Mezzo 2 parte alle "
        "17:25 per cinque fermate e deve essere in location per le 18:00: sono sette minuti a fermata, salita "
        "degli ospiti compresa, e su queste strade non tiene. Noi lo facciamo partire <b>alle 17:10</b>. Per lo "
        "stesso motivo la seconda corsa del Mezzo 1 parte <b>alle 17:20</b> invece che alle 17:35: sono 21 persone "
        "da caricare a due fermate. Con un quarto d'ora in più nessuno arriva di corsa.",
        "<b>Abbiamo invertito Rovai e Casalino</b> rispetto al vostro schema: prima Rovai, poi Casalino. Casalino "
        "è a tre minuti dalla location ed è la fermata più numerosa, con 18 ospiti: servendola per ultima quelle "
        "18 persone restano a bordo tre minuti invece di venti. Al rientro l'ordine è quello naturale, prima "
        "Casalino e poi Rovai.",
        "<b>Alle 23:00 non partono tutti.</b> I due mezzi riportano a casa 33 ospiti sui 50: gli ultimi 17, quelli "
        "di Podere la Romola e I Trebbiali, restano alla festa fino alle 23:35 e sono a casa verso le 23:55. "
        "È il punto su cui vale la pena mettersi d'accordo prima, così i vostri ospiti lo sanno.",
        "<b>Se a ogni indirizzo ci arriva un minibus.</b> Diversi punti di ritiro sono case coloniche su strade "
        "strette. Dove un minibus non può girare o passare, concordiamo un punto d'incontro a pochi passi, "
        "piuttosto che rischiare la sera stessa.",
        "<b>La posizione esatta di Loc. Podere la Romola 78 e Loc. Giusti 105</b> — sono 18 ospiti sui 50 e basta "
        "uno spillo sulla mappa o un numero di telefono per ciascuno.",
        "<b>Un numero di cellulare per la serata</b>, da dare a entrambi gli autisti.",
        "<b>I vostri dati di fatturazione.</b>",
    ],
    closing=(
        "Restiamo a disposizione per organizzare il servizio. Le coordinate bancarie per l'acconto sono qui sopra: "
        "appena arriva vi confermiamo la prenotazione, e sotto data vi mandiamo i nomi e i numeri diretti dei due "
        "autisti insieme all'orario definitivo di ritiro per ogni indirizzo.<br/><br/>"
        "Cordiali saluti,<br/>"
        "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"
    ),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Coach hire with driver — welcome event shuttle  ·  Fattoria I Bonsi, Reggello (Florence)  ·  Friday 25 September 2026",
    meta="Prepared for %s  ·  programme updated 9 September 2026  ·  Ref. " + RIF + "  ·  valid until 15 September 2026",
    intro=(
        "We have rebuilt the programme around your Friday loading-points sheet: nine addresses, 50 guests, "
        "everyone at the venue by 18:00. <b>The price is the one quoted on 8 September and does not change.</b> "
        "What changes is only how the two minibuses share the work: three collection runs instead of four, on your "
        "final addresses. We would ask you to confirm two earlier departure times and the order of one run: both "
        "are explained under the points to confirm, at the end."
    ),
    h_mezzi="The vehicles",
    mezzi=[
        ("Vehicle 1",
         "<b>Mercedes-Benz minibus — 25+1+1</b> (25 passenger seats + tour leader + driver), air conditioning, "
         "fridge, reclining seats, luggage compartment."),
        ("Vehicle 2",
         "<b>Mercedes-Benz minibus — 27+1+1</b> (27 passenger seats + tour leader + driver), air conditioning, "
         "reclining seats, luggage compartment."),
    ],
    mezzi_facts=[
        ("Seating", "50 guests spread across three runs: the fullest carries 21, on a vehicle seating 25. "
                    "No run is at its limit and nobody travels standing."),
        ("Time on board",
         "Between 10 and 25 minutes. Each run covers a cluster of addresses close to one another, so no one sits "
         "through the whole collection."),
        ("Drivers", "Two professional drivers, one per vehicle, on duty for the whole evening."),
    ],
    h_servizio="Programme — Friday 25 September 2026",
    svc_intro=(
        "Three collection runs — two by Vehicle 1 and one by Vehicle 2 — so that everyone is at the venue by 18:00. "
        "Both vehicles then stay at Fattoria I Bonsi for the whole evening and set off again at 23:00 with the "
        "return runs, three of them as well. The times are yours, brought forward by a quarter of an hour on the "
        "two runs where they did not hold."
    ),
    svc_head=["Run", "Route", "Timing"],
    svc=[
        ("Vehicle 1<br/>first run",
         "<b>I Trebbiali, Loc. I Trebbiali 116 (3)</b> → <b>Podere la Romola, Loc. Podere la Romola 78 (14)</b> → "
         "<b>venue — Fattoria I Bonsi, Via Bonsi 47.</b> Arrival around 17:15.",
         "from 16:50<br/>17 guests"),
        ("Vehicle 2<br/>single run",
         "<b>La Terrazza di Reggello, Via di Fano 6 (2)</b> → <b>S. Giovenale, Loc. S. Giovenale 55 (2)</b> → "
         "<b>Podere Giusti, Loc. Giusti 105 (4)</b> → <b>Appartamento Olivella, Via Fornacina 32 (2)</b> → "
         "<b>Via dei Glicini 14, Poggio ai Giubbiani (2)</b> → <b>venue, Via Bonsi 47.</b> Arrival by 18:00.",
         "from 17:10<br/>12 guests"),
        ("Vehicle 1<br/>second run",
         "<b>Rovai, Loc. Rovai 26, Pietrapiana (3)</b> → <b>Casalino, Via Ponte di Casalino 66–68 (18)</b> — "
         "Hotel Archimede and Podere Casalino are 120 m apart on the same road, so we serve them as a single stop "
         "→ <b>venue, Via Bonsi 47.</b> Arrival by 18:00.",
         "from 17:20<br/>21 guests"),
        ("Both vehicles<br/>at the venue",
         "The minibuses stay parked at Fattoria I Bonsi for the whole evening, at your disposal together with "
         "their drivers.",
         "18:00 – 23:00"),
        ("Return<br/>three runs",
         "<b>Vehicle 1</b> leaves at 23:00 with the 21 guests at Casalino and Rovai, all home by about 23:25; it "
         "is back at the venue at 23:35 and makes the last run with the 17 at Podere la Romola and I Trebbiali, "
         "home by about 23:55. <b>Vehicle 2</b> leaves at 23:00 with the 12 guests at Via di Fano, S. Giovenale, "
         "Podere Giusti, Via Fornacina and Via dei Glicini, all home by about 23:35.",
         "from 23:00<br/>until about 23:55"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("<b>Transport — Vehicle 1</b> (minibus, 25+1+1). Two collection runs from four points — I Trebbiali, "
         "Podere la Romola, Rovai and the combined Casalino stop — vehicle and driver at your disposal at the "
         "venue from 18:00 to 23:00, two return runs to the same addresses. Fuel, motorway tolls, parking, "
         "insurance and positioning of the vehicle from and to our depot are included.",
         "€ 1,100.00", "+ VAT 10%"),
        ("<b>Transport — Vehicle 2</b> (minibus, 27+1+1). One collection run from five points — Via di Fano, "
         "S. Giovenale, Podere Giusti, Via Fornacina and Via dei Glicini — vehicle and driver at your disposal at "
         "the venue from 18:00 to 23:00, one return run to the same addresses. Same inclusions as the line above.",
         "€ 1,100.00", "+ VAT 10%"),
        ("Dinner for the two drivers, on duty from the afternoon until late at night",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, net of VAT",
    price_total="€ 2,200.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,420.00.",
    price_note=(
        "Transport € 2,200.00 + VAT 10% (€ 220.00). <b>The price is the one quoted on 8 September and does not "
        "change</b>: the three collection runs and three return runs are all included. Fixed price, no further "
        "charges beyond what is listed under “Not included”."
    ),
    permessi=(
        "<b>No city access permits are due for this service.</b> Some Tuscan cities charge coaches a daily access "
        "permit — Florence, Siena, Lucca, Pisa — and those charges can run into hundreds of euros. This event "
        "stays entirely within the municipality of Reggello, which has no such check point, so there is nothing of "
        "the sort in this quotation. If a charge did turn out to apply anywhere on the route, we would tell you "
        "beforehand and pass it on at its official cost, never as a surprise on the final invoice."
    ),
    h_incluso="Included",
    incluso=[
        "Two minibuses and two professional drivers for the whole evening, from the first pick-up to the last "
        "drop-off.",
        "Three collection runs and three return runs, so that time on board stays between 10 and 25 minutes.",
        "Both vehicles and drivers at your disposal at the venue from 18:00 to 23:00.",
        "Fuel, motorway tolls, parking and insurance.",
        "Positioning of both vehicles from and to our depot, before and after the service.",
        "Evening operation: the last guests are taken home at around 23:55.",
        "All applicable taxes: VAT at 10% is shown separately above and is already counted in the total payable.",
    ],
    h_nonincluso="Not included",
    nonincluso=[
        "Any additional journey beyond the ones described above — for example an earlier return for part of the "
        "group before 23:00: we can organise it, quoted separately.",
        "Extra guests on a single run. The fullest carries 21 on 25 seats, so there is some margin, but every "
        "address added changes the timing plan: please tell us in advance.",
        "<b>Dinner for the two drivers</b>, which stays at your charge: you book it and pay for it directly.",
        "Waiting beyond the agreed times: € 50.00 per hour, per vehicle.",
        "A return running past 02:00: € 250.00 per vehicle. The programme closes at around 23:55, so nothing is "
        "due.",
        "Anything not expressly listed above.",
    ],
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit of 30% on confirmation", "€ 726.00", "VAT included"),
        ("Balance, by 20 September 2026", "€ 1,694.00", ""),
    ],
    pay_text=(
        "The balance is due by 20 September 2026, five days before the service. <b>The booking becomes firm when "
        "the deposit reaches our account</b>, not before. A tax invoice is issued for the full amount."
    ),
    bank=(
        "<b>Bank details.</b> Bank transfer to Munna Girolamo Giuseppe — "
        "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05. Please quote your name and reference " +
        RIF + " as the payment reference."
    ),
    validita=(
        "<b>Validity.</b> This quotation is valid until 15 September 2026. The date is close: we hold the two "
        "vehicles for you until then, but we cannot guarantee them afterwards."
    ),
    cancellazione=(
        "<b>Cancellation.</b> Free of charge more than 30 days before the service. From 30 to 10 days the deposit "
        "is retained; from 10 to 3 days, 70% of the amount; in the last 72 hours, 100%. As the event is now less "
        "than 30 days away, a confirmation falls straight into the second band: the deposit is retained in case of "
        "cancellation. Force majeure is assessed case by case."
    ),
    h_punti="Points to confirm",
    punti=[
        "<b>Two runs start a quarter of an hour earlier than in your plan.</b> In your sheet Vehicle 2 leaves at "
        "17:25 for five stops and has to be at the venue by 18:00: that is seven minutes per stop including "
        "boarding, and on these roads it does not hold. We start it <b>at 17:10</b>. For the same reason Vehicle "
        "1's second run leaves <b>at 17:20</b> rather than 17:35: there are 21 people to board at two stops. "
        "A quarter of an hour more and nobody arrives in a rush.",
        "<b>We have swapped Rovai and Casalino</b> compared with your sheet: Rovai first, then Casalino. Casalino "
        "is three minutes from the venue and is the busiest stop, with 18 guests: serving it last keeps those 18 "
        "people on board for three minutes instead of twenty. On the return the order is the natural one, "
        "Casalino first and then Rovai.",
        "<b>Not everyone leaves at 23:00.</b> The two vehicles take 33 guests out of 50 home: the last 17, those "
        "at Podere la Romola and I Trebbiali, stay at the party until 23:35 and are home by about 23:55. This is "
        "the point worth agreeing beforehand, so your guests know.",
        "<b>Whether a minibus can reach each address.</b> Several pick-up points are farm houses on narrow lanes. "
        "Where a minibus cannot turn or pass, we agree a meeting point a short walk away rather than risk it on "
        "the evening.",
        "<b>The exact location of Loc. Podere la Romola 78 and Loc. Giusti 105</b> — that is 18 guests out of 50, "
        "and a map pin or a phone number for each is enough.",
        "<b>A mobile number for the evening</b>, to be given to both drivers.",
        "<b>Your billing details.</b>",
    ],
    closing=(
        "We are at your disposal to organise the service. The bank details for the deposit are above: as soon as "
        "it arrives we will confirm the booking, and closer to the date send the names and direct numbers of the "
        "two drivers together with the final pick-up time for each address.<br/><br/>"
        "Kind regards,<br/>"
        "Girolamo Munna — GiroMunna NCC, Tuscany · +39 335 587 4744 · info@giromunna.com"
    ),
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


def _box(testo, S, usable):
    """Riquadro crema con filetto oro, come nella sezione mezzo dei preventivi."""
    t = Table([[Paragraph(testo, S["cellsm"])]], colWidths=[usable])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


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

    # --- i mezzi
    F.append(Paragraph(L["h_mezzi"], S["h2"]))
    for etichetta, testo in L["mezzi"]:
        F.append(_box("<b>%s.</b>  %s" % (etichetta, testo), S, usable))
        F.append(Spacer(1, 6))
    fcols = [30 * mm, usable - 30 * mm]
    fdata = [[Paragraph("<b>%s</b>" % a, S["cellsm"]), Paragraph(b, S["cellsm"])]
             for a, b in L["mezzi_facts"]]
    ft = Table(fdata, colWidths=fcols)
    ft.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    F.append(ft)

    # --- il servizio
    F.append(Paragraph(L["h_servizio"], S["h2"]))
    F.append(Paragraph(L["svc_intro"], S["body"]))
    cols = [26 * mm, usable - 26 * mm - 26 * mm, 26 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for corsa, desc, orario in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % corsa, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
            Paragraph(orario, S["cellmut"]),
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

    # --- il prezzo
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
    F.append(KeepTogether([
        Paragraph(L["h_prezzo"], S["h2"]),
        pt,
        Paragraph(L["grand"], S["grand"]),
        Paragraph(L["price_note"], S["small"]),
    ]))
    F.append(Spacer(1, 4))
    F.append(Paragraph(L["permessi"], S["small"]))

    # --- incluso / non incluso
    F.append(Paragraph(L["h_incluso"], S["h2"]))
    for voce in L["incluso"]:
        F.append(Paragraph("·  " + voce, S["note"]))
    F.append(Paragraph(L["h_nonincluso"], S["h2"]))
    for voce in L["nonincluso"]:
        F.append(Paragraph("·  " + voce, S["note"]))

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
    F.append(Paragraph(L["pay_text"], S["small"]))
    F.append(Paragraph(L["bank"], S["small"]))
    F.append(Paragraph(L["validita"], S["small"]))
    F.append(Paragraph(L["cancellazione"], S["small"]))

    # --- punti da confermare
    F.append(Paragraph(L["h_punti"], S["h2"]))
    for n in L["punti"]:
        F.append(Paragraph("·  " + n, S["note"]))

    F.append(Spacer(1, 8))
    F.append(Paragraph(L["closing"], S["small"]))

    doc.build(F)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingua", "--lang", dest="lang", default="it", choices=["it", "en"])
    ap.add_argument("--cliente", "--client", dest="cliente", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    cliente = a.cliente or ("Sean e Hannah" if a.lang == "it" else "Sean and Hannah")
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25_settembre_2026_programma_aggiornato_%s.pdf" % a.lang.upper())
    print(build(a.lang, cliente, name))

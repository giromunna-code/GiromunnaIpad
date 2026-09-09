#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la navetta del matrimonio a Reggello del 25 settembre 2026.

Revisione 2 del 9 settembre 2026, sullo schema dei punti di carico mandato dal cliente:
54 ospiti, dieci indirizzi, tutti in location entro le 15:30, rientri dall'01:00.

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
    subtitle="Noleggio con conducente — navetta per matrimonio  ·  Fattoria I Bonsi, Reggello (Firenze)  ·  venerdì 25 settembre 2026",
    meta="Preparato per %s  ·  revisione 2 del 9 settembre 2026  ·  Rif. " + RIF + "  ·  valido fino al 15 settembre 2026",
    intro=(
        "Questa versione sostituisce il preventivo dell'8 settembre e segue lo schema dei punti di carico che ci "
        "avete mandato: 54 ospiti su dieci indirizzi, tutti in location entro le 15:30, rientri dall'01:00. "
        "Rispetto alla prima versione le corse sono meno — tre all'andata e tre al ritorno invece di quattro e "
        "quattro — ma i mezzi sono impegnati <b>dalle 14:25 alle 02:00</b> invece che dalle 16:20 alle 00:25: sono "
        "tre ore e mezza in più per mezzo, con la serata che si chiude alle due del mattino. È questo che cambia "
        "il prezzo, non il numero delle corse."
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
        ("Posti", "54 ospiti distribuiti su tre corse: la più carica ne porta 20, su mezzi da 25 e 27 posti. "
                  "Nessuna corsa va al limite e nessuno viaggia in piedi."),
        ("Tempo a bordo",
         "Dai 10 ai 25 minuti. Ogni corsa copre un gruppo di indirizzi vicini fra loro, così nessuno si fa tutto "
         "il giro di raccolta."),
        ("Conducenti", "Due autisti professionisti, uno per mezzo, in servizio dalle 14:00 alle due passate."),
    ],
    h_servizio="Il servizio — venerdì 25 settembre 2026",
    svc_intro=(
        "Tre corse di raccolta — due con il Mezzo 1 e una con il Mezzo 2 — così che tutti siano in location entro "
        "le 15:30. I mezzi restano poi alla Fattoria I Bonsi per tutto il ricevimento e ripartono all'01:00 con i "
        "rientri, sempre in tre corse. Gli orari sono i vostri, con una sola modifica che vi chiediamo di "
        "confermare: la corsa del Mezzo 2 parte alle 14:25 invece che alle 14:45. Il motivo è nelle note."
    ),
    svc_head=["Corsa", "Percorso", "Orario"],
    svc=[
        ("Mezzo 1<br/>prima corsa",
         "<b>I Trebbiali, Loc. I Trebbiali 116 (3)</b> → <b>Podere la Romola, Loc. Podere la Romola 78 (14)</b> → "
         "<b>location — Fattoria I Bonsi, Via Bonsi 47.</b> Arrivo verso le 14:55.",
         "dalle 14:35<br/>17 ospiti"),
        ("Mezzo 2<br/>corsa unica",
         "<b>Via dei Glicini 14, Poggio ai Giubbiani (2)</b> → <b>Appartamento Olivella, Via Fornacina 32 (2)</b> → "
         "<b>Podere Giusti, Loc. Giusti 105 (5)</b> → <b>S. Giovenale, Loc. S. Giovenale 55 (2)</b> → "
         "<b>La Terrazza di Reggello, Via di Fano 6 (2)</b> → <b>Hotel Archimede, Via Ponte di Casalino 68 (7)</b> → "
         "<b>location, Via Bonsi 47.</b> Arrivo entro le 15:30.",
         "dalle 14:25<br/>20 ospiti"),
        ("Mezzo 1<br/>seconda corsa",
         "<b>Podere Casalino, Via Ponte di Casalino 66 (14)</b> → <b>Rovai, Loc. Rovai 26, Pietrapiana (3)</b> → "
         "<b>location, Via Bonsi 47.</b> Arrivo entro le 15:30.",
         "dalle 15:05<br/>17 ospiti"),
        ("Entrambi i mezzi<br/>in location",
         "I minibus restano parcheggiati alla Fattoria I Bonsi per tutto il ricevimento, a vostra disposizione "
         "con i conducenti. Sono nove ore e mezza.",
         "15:30 – 01:00"),
        ("Rientri<br/>tre corse",
         "Il <b>Mezzo 1</b> parte all'01:00 con i 17 ospiti di Podere Casalino e Rovai, a casa verso le 01:25; "
         "rientra in location alle 01:35 e fa l'ultima corsa con i 17 di Podere la Romola e I Trebbiali, a casa "
         "verso le 01:55. Il <b>Mezzo 2</b> parte all'01:00 con i 20 ospiti di Hotel Archimede, Via di Fano, "
         "S. Giovenale, Podere Giusti, Via Fornacina e Via dei Glicini, tutti a casa verso le 01:40.",
         "dall'01:00<br/>fino alle 02:00 ca."),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("<b>Trasporto — Mezzo 1</b> (minibus, 25+1+1). Due corse di raccolta da cinque indirizzi, mezzo e "
         "conducente a vostra disposizione in location dalle 15:30 all'01:00, due corse di rientro agli stessi "
         "indirizzi. Carburante, pedaggi autostradali, parcheggi, assicurazione e movimentazione del mezzo da e "
         "per la nostra rimessa sono compresi.",
         "€ 1.450,00", "+ IVA 10%"),
        ("<b>Trasporto — Mezzo 2</b> (minibus, 27+1+1). Una corsa di raccolta da sei indirizzi, mezzo e conducente "
         "a vostra disposizione in location dalle 15:30 all'01:00, una corsa di rientro agli stessi indirizzi. "
         "Stesse voci comprese della riga precedente.",
         "€ 1.450,00", "+ IVA 10%"),
        ("Cena dei due conducenti, in servizio dalle 14:00 alle due passate",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.900,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 3.190,00.",
    price_note=(
        "Trasporto € 2.900,00 + IVA 10% (€ 290,00). Le tre corse di raccolta e le tre di rientro sono tutte "
        "comprese in questo prezzo. Prezzo fisso, nessun addebito ulteriore oltre a quanto elencato sotto "
        "«Non incluso»."
    ),
    permessi=(
        "<b>Nessun onere di accesso è dovuto per questo servizio.</b> Alcune città toscane fanno pagare ai bus un "
        "permesso giornaliero di accesso — Firenze, Siena, Lucca, Pisa — e sono cifre che arrivano a diverse "
        "centinaia di euro. Questo matrimonio si svolge interamente nel Comune di Reggello, che non ha varchi di "
        "questo tipo, quindi nel preventivo non c'è nulla del genere. Se un onere dovesse risultare dovuto in "
        "qualche punto del percorso, ve lo diremmo prima e ve lo gireremmo al costo ufficiale, mai come sorpresa "
        "in fattura."
    ),
    h_incluso="Incluso",
    incluso=[
        "Due minibus e due autisti professionisti, dal primo ritiro delle 14:25 all'ultimo rientro delle 01:55.",
        "Tre corse di raccolta e tre di rientro, così che il tempo a bordo resti fra i 10 e i 25 minuti.",
        "Mezzi e conducenti a vostra disposizione in location dalle 15:30 all'01:00: nove ore e mezza.",
        "Carburante, pedaggi autostradali, parcheggi e assicurazione.",
        "Movimentazione dei due mezzi da e per la nostra rimessa, prima e dopo il servizio.",
        "Servizio in orario notturno: gli ultimi ospiti vengono riaccompagnati fra l'01:35 e le 02:00.",
        "Tutte le imposte dovute: l'IVA al 10% è esposta a parte qui sopra ed è già conteggiata nel totale da "
        "corrispondere.",
    ],
    h_nonincluso="Non incluso",
    nonincluso=[
        "Qualsiasi trasferimento in più rispetto a quelli descritti — per esempio un rientro anticipato per una "
        "parte del gruppo prima dell'01:00: possiamo organizzarlo, quotato a parte.",
        "Ospiti in più su una singola corsa. La corsa più carica ne porta 20 su 27 posti, quindi un margine c'è, "
        "ma ogni indirizzo aggiunto cambia lo schema degli orari: segnalatecelo prima.",
        "<b>Cena dei due conducenti</b>, che resta a vostro carico: la prenotate e la pagate voi direttamente.",
        "Attesa oltre gli orari concordati: € 50,00 all'ora per mezzo.",
        "Rientro oltre le 02:00: € 250,00 per mezzo. Il programma si chiude alle 01:55 e quindi non è dovuto, ma "
        "un ritardo sulla partenza dell'01:00 lo fa scattare.",
        "Tutto quanto non espressamente indicato qui sopra.",
    ],
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 957,00", "IVA inclusa"),
        ("Saldo, entro il 20 settembre 2026", "€ 2.233,00", ""),
    ],
    pay_text=(
        "Il saldo è dovuto entro il 20 settembre 2026, cinque giorni prima del servizio. Le coordinate bancarie "
        "vengono inviate con la richiesta di conferma; <b>la prenotazione diventa definitiva quando l'acconto "
        "arriva sul nostro conto</b>, non prima. Per l'intero importo viene emessa regolare fattura."
    ),
    validita=(
        "<b>Validità.</b> Questo preventivo è valido fino al 15 settembre 2026. La data è vicina: fino ad allora "
        "teniamo bloccati per voi i due mezzi, dopo non possiamo garantirli."
    ),
    cancellazione=(
        "<b>Cancellazione.</b> Gratuita oltre 30 giorni prima del servizio. Da 30 a 10 giorni viene trattenuto "
        "l'acconto; da 10 a 3 giorni il 70% dell'importo; nelle ultime 72 ore il 100%. Mancando oggi meno di 30 "
        "giorni al matrimonio, una conferma ricade direttamente nella seconda fascia: in caso di cancellazione "
        "l'acconto viene trattenuto. Le cause di forza maggiore si valutano caso per caso."
    ),
    h_punti="Punti da confermare",
    punti=[
        "<b>I numeri per indirizzo.</b> Il preventivo segue il vostro schema: 54 ospiti su dieci punti di carico. "
        "Confermateci che sono i numeri definitivi, perché sono loro a decidere come si dividono le corse.",
        "<b>La partenza della corsa del Mezzo 2.</b> Nel vostro schema parte alle 14:45, fa sei fermate e deve "
        "essere in location per le 15:30: sono sette minuti a fermata, salita degli ospiti compresa, e su queste "
        "strade non tiene. Noi la facciamo partire <b>alle 14:25</b>. Con venti minuti in più l'orario regge anche "
        "se una fermata va lunga, e nessuno arriva di corsa.",
        "<b>All'01:00 non partono tutti.</b> I due mezzi portano via 37 ospiti sui 54: gli ultimi 17, quelli di "
        "Podere la Romola e I Trebbiali, restano al ricevimento fino alle 01:35 e sono a casa verso le 01:55. "
        "È il punto del programma su cui vale la pena mettersi d'accordo prima. Se preferite che rientrino tutti "
        "insieme all'01:00 serve un terzo mezzo, che quotiamo a parte.",
        "<b>Se a ogni indirizzo ci arriva un minibus.</b> Diversi punti di ritiro sono case coloniche su strade "
        "strette. Dove un minibus non può girare o passare, concordiamo un punto d'incontro a pochi passi, "
        "piuttosto che rischiare il giorno stesso.",
        "<b>La posizione esatta di Loc. Podere la Romola 78 e Loc. Giusti 105</b> — sono 19 ospiti sui 54 e basta "
        "uno spillo sulla mappa o un numero di telefono per ciascuno.",
        "<b>Un numero di cellulare per la serata</b>, da dare a entrambi gli autisti.",
        "<b>I vostri dati di fatturazione.</b>",
    ],
    closing=(
        "Restiamo a disposizione per organizzare il servizio. Alla conferma vi invieremo le coordinate bancarie e, "
        "sotto data, i nomi e i numeri diretti dei due autisti insieme all'orario definitivo di ritiro per ogni "
        "indirizzo.<br/><br/>"
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
    subtitle="Coach hire with driver — wedding shuttle  ·  Fattoria I Bonsi, Reggello (Florence)  ·  Friday 25 September 2026",
    meta="Prepared for %s  ·  revision 2 of 9 September 2026  ·  Ref. " + RIF + "  ·  valid until 15 September 2026",
    intro=(
        "This version replaces the quotation of 8 September and follows the loading-points plan you sent us: "
        "54 guests across ten addresses, everyone at the venue by 15:30, return runs from 01:00. Compared with the "
        "first version there are fewer runs — three out and three back instead of four and four — but the vehicles "
        "are engaged <b>from 14:25 to 02:00</b> instead of 16:20 to 00:25: three and a half hours more per vehicle, "
        "with the evening closing at two in the morning. That is what changes the price, not the number of runs."
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
        ("Seating", "54 guests spread across three runs: the fullest carries 20, on vehicles seating 25 and 27. "
                    "No run is at its limit and nobody travels standing."),
        ("Time on board",
         "Between 10 and 25 minutes. Each run covers a cluster of addresses close to one another, so no one sits "
         "through the whole collection."),
        ("Drivers", "Two professional drivers, one per vehicle, on duty from 14:00 until gone two in the morning."),
    ],
    h_servizio="Programme — Friday 25 September 2026",
    svc_intro=(
        "Three collection runs — two by Vehicle 1 and one by Vehicle 2 — so that everyone is at the venue by 15:30. "
        "Both vehicles then stay at Fattoria I Bonsi for the whole reception and set off again at 01:00 with the "
        "return runs, three of them as well. The times are yours, with one change we would ask you to confirm: "
        "Vehicle 2's run starts at 14:25 rather than 14:45. The reason is in the notes."
    ),
    svc_head=["Run", "Route", "Timing"],
    svc=[
        ("Vehicle 1<br/>first run",
         "<b>I Trebbiali, Loc. I Trebbiali 116 (3)</b> → <b>Podere la Romola, Loc. Podere la Romola 78 (14)</b> → "
         "<b>venue — Fattoria I Bonsi, Via Bonsi 47.</b> Arrival around 14:55.",
         "from 14:35<br/>17 guests"),
        ("Vehicle 2<br/>single run",
         "<b>Via dei Glicini 14, Poggio ai Giubbiani (2)</b> → <b>Appartamento Olivella, Via Fornacina 32 (2)</b> → "
         "<b>Podere Giusti, Loc. Giusti 105 (5)</b> → <b>S. Giovenale, Loc. S. Giovenale 55 (2)</b> → "
         "<b>La Terrazza di Reggello, Via di Fano 6 (2)</b> → <b>Hotel Archimede, Via Ponte di Casalino 68 (7)</b> → "
         "<b>venue, Via Bonsi 47.</b> Arrival by 15:30.",
         "from 14:25<br/>20 guests"),
        ("Vehicle 1<br/>second run",
         "<b>Podere Casalino, Via Ponte di Casalino 66 (14)</b> → <b>Rovai, Loc. Rovai 26, Pietrapiana (3)</b> → "
         "<b>venue, Via Bonsi 47.</b> Arrival by 15:30.",
         "from 15:05<br/>17 guests"),
        ("Both vehicles<br/>at the venue",
         "The minibuses stay parked at Fattoria I Bonsi for the whole reception, at your disposal together with "
         "their drivers. That is nine and a half hours.",
         "15:30 – 01:00"),
        ("Return<br/>three runs",
         "<b>Vehicle 1</b> leaves at 01:00 with the 17 guests at Podere Casalino and Rovai, home by about 01:25; "
         "it is back at the venue at 01:35 and makes the last run with the 17 at Podere la Romola and I Trebbiali, "
         "home by about 01:55. <b>Vehicle 2</b> leaves at 01:00 with the 20 guests at Hotel Archimede, Via di Fano, "
         "S. Giovenale, Podere Giusti, Via Fornacina and Via dei Glicini, all home by about 01:40.",
         "from 01:00<br/>until about 02:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("<b>Transport — Vehicle 1</b> (minibus, 25+1+1). Two collection runs from five addresses, vehicle and "
         "driver at your disposal at the venue from 15:30 to 01:00, two return runs to the same addresses. Fuel, "
         "motorway tolls, parking, insurance and positioning of the vehicle from and to our depot are included.",
         "€ 1,450.00", "+ VAT 10%"),
        ("<b>Transport — Vehicle 2</b> (minibus, 27+1+1). One collection run from six addresses, vehicle and driver "
         "at your disposal at the venue from 15:30 to 01:00, one return run to the same addresses. Same inclusions "
         "as the line above.",
         "€ 1,450.00", "+ VAT 10%"),
        ("Dinner for the two drivers, on duty from 14:00 until gone two in the morning",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, net of VAT",
    price_total="€ 2,900.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 3,190.00.",
    price_note=(
        "Transport € 2,900.00 + VAT 10% (€ 290.00). The three collection runs and three return runs are all "
        "included at this price. Fixed price, no further charges beyond what is listed under “Not included”."
    ),
    permessi=(
        "<b>No city access permits are due for this service.</b> Some Tuscan cities charge coaches a daily access "
        "permit — Florence, Siena, Lucca, Pisa — and those charges can run into hundreds of euros. This wedding "
        "stays entirely within the municipality of Reggello, which has no such check point, so there is nothing of "
        "the sort in this quotation. If a charge did turn out to apply anywhere on the route, we would tell you "
        "beforehand and pass it on at its official cost, never as a surprise on the final invoice."
    ),
    h_incluso="Included",
    incluso=[
        "Two minibuses and two professional drivers, from the first pick-up at 14:25 to the last drop-off at 01:55.",
        "Three collection runs and three return runs, so that time on board stays between 10 and 25 minutes.",
        "Both vehicles and drivers at your disposal at the venue from 15:30 to 01:00: nine and a half hours.",
        "Fuel, motorway tolls, parking and insurance.",
        "Positioning of both vehicles from and to our depot, before and after the service.",
        "Night-time operation: the last guests are taken home between 01:35 and 02:00.",
        "All applicable taxes: VAT at 10% is shown separately above and is already counted in the total payable.",
    ],
    h_nonincluso="Not included",
    nonincluso=[
        "Any additional journey beyond the ones described above — for example an earlier return for part of the "
        "group before 01:00: we can organise it, quoted separately.",
        "Extra guests on a single run. The fullest run carries 20 on 27 seats, so there is some margin, but every "
        "address added changes the timing plan: please tell us in advance.",
        "<b>Dinner for the two drivers</b>, which stays at your charge: you book it and pay for it directly.",
        "Waiting beyond the agreed times: € 50.00 per hour, per vehicle.",
        "A return running past 02:00: € 250.00 per vehicle. The programme closes at 01:55 so nothing is due, but a "
        "delay on the 01:00 departure would trigger it.",
        "Anything not expressly listed above.",
    ],
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit of 30% on confirmation", "€ 957.00", "VAT included"),
        ("Balance, by 20 September 2026", "€ 2,233.00", ""),
    ],
    pay_text=(
        "The balance is due by 20 September 2026, five days before the service. Bank details are sent with the "
        "confirmation request; <b>the booking becomes firm when the deposit reaches our account</b>, not before. "
        "A tax invoice is issued for the full amount."
    ),
    validita=(
        "<b>Validity.</b> This quotation is valid until 15 September 2026. The date is close: we hold the two "
        "vehicles for you until then, but we cannot guarantee them afterwards."
    ),
    cancellazione=(
        "<b>Cancellation.</b> Free of charge more than 30 days before the service. From 30 to 10 days the deposit "
        "is retained; from 10 to 3 days, 70% of the amount; in the last 72 hours, 100%. As the wedding is now less "
        "than 30 days away, a confirmation falls straight into the second band: the deposit is retained in case of "
        "cancellation. Force majeure is assessed case by case."
    ),
    h_punti="Points to confirm",
    punti=[
        "<b>The numbers at each address.</b> This quotation follows your plan: 54 guests across ten loading points. "
        "Please confirm these are the final numbers, as they decide how the runs are split.",
        "<b>The start time of Vehicle 2's run.</b> In your plan it leaves at 14:45, makes six stops and has to be at "
        "the venue by 15:30: that is seven minutes per stop including boarding, and on these roads it does not hold. "
        "We start it <b>at 14:25</b>. Twenty minutes more and the schedule stands even if one stop runs long, and "
        "nobody arrives in a rush.",
        "<b>Not everyone leaves at 01:00.</b> The two vehicles take away 37 guests out of 54: the last 17, those at "
        "Podere la Romola and I Trebbiali, stay at the reception until 01:35 and are home by about 01:55. This is "
        "the point of the programme worth agreeing on beforehand. If you would rather everyone left together at "
        "01:00, that takes a third vehicle, which we would quote separately.",
        "<b>Whether a minibus can reach each address.</b> Several pick-up points are farm houses on narrow lanes. "
        "Where a minibus cannot turn or pass, we agree a meeting point a short walk away rather than risk it on "
        "the day.",
        "<b>The exact location of Loc. Podere la Romola 78 and Loc. Giusti 105</b> — that is 19 guests out of 54, "
        "and a map pin or a phone number for each is enough.",
        "<b>A mobile number for the evening</b>, to be given to both drivers.",
        "<b>Your billing details.</b>",
    ],
    closing=(
        "We are at your disposal to organise the service. On confirmation we will send the bank details and, "
        "closer to the date, the names and direct numbers of the two drivers together with the final pick-up time "
        "for each address.<br/><br/>"
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
        HERE, "GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25_settembre_2026_rev2_%s.pdf" % a.lang.upper())
    print(build(a.lang, cliente, name))

#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la navetta del matrimonio a Reggello del 25 settembre 2026.

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
    meta="Preparato per %s  ·  8 settembre 2026  ·  Rif. " + RIF + "  ·  valido fino al 15 settembre 2026",
    intro=(
        "Grazie della vostra richiesta e dei dettagli sul gruppo. Questo preventivo è costruito sui vostri due "
        "punti fermi: 50 ospiti, tre dei quali all'Hotel Archimede, e due corse brevi per ogni minibus invece di "
        "una sola lunga, così che nessuno resti a bordo più di una mezz'ora scarsa. Entrambi i mezzi sono minibus "
        "compatti e non autobus gran turismo: è quello che chiedono le strade collinari intorno a Pietrapiana, "
        "Donnini e Cascia."
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
        ("Posti", "52 posti passeggeri per 50 ospiti: ci state comodamente, con due posti di margine."),
        ("Tempo a bordo",
         "Al massimo una mezz'ora, dai 10 ai 20 minuti per la maggior parte degli ospiti. È a questo che servono "
         "le due corse per mezzo: ogni corsa copre un piccolo gruppo di indirizzi vicini fra loro, così nessuno "
         "si fa tutto il giro di raccolta."),
        ("Conducenti", "Due autisti professionisti, uno per mezzo, in servizio per tutta la serata."),
    ],
    h_servizio="Il servizio — venerdì 25 settembre 2026",
    svc_intro=(
        "Quattro corse brevi di raccolta, due per mezzo, in parallelo, così che ogni ospite sia in location ben "
        "prima delle 18:00. Gli orari qui sotto sono il nostro piano di lavoro: l'orario esatto di ritiro a ogni "
        "indirizzo lo confermiamo tre o quattro giorni prima del matrimonio, quando ci avrete detto a quali "
        "indirizzi un minibus arriva davvero. I due mezzi restano poi in location e riportano indietro gli stessi "
        "ospiti dalle 23:00, di nuovo in due corse ciascuno."
    ),
    svc_head=["Corsa", "Percorso", "Orario"],
    svc=[
        ("Mezzo 1<br/>prima corsa",
         "<b>Casalino, Via Ponte di Casalino 66–68 (17)</b> — l'Hotel Archimede e Podere Casalino distano 120 m "
         "sulla stessa strada, quindi li serviamo come un'unica fermata → <b>Loc. Rovai 26, Pietrapiana (3)</b> → "
         "<b>location — Fattoria I Bonsi, Via Bonsi 47.</b> Due fermate a pochi minuti l'una dall'altra, con la "
         "location appena tre minuti più avanti; arrivo verso le 17:00.",
         "dalle 16:35<br/>20 ospiti"),
        ("Mezzo 1<br/>seconda corsa",
         "<b>Villa Pitiana Hotel, Via Provinciale per Tosi 7 (1)</b> → <b>Loc. I Trebbiali 116 (2)</b> → "
         "<b>location, Via Bonsi 47.</b> Arrivo in location verso le 17:45.",
         "dalle 17:20<br/>3 ospiti"),
        ("Mezzo 2<br/>prima corsa",
         "<b>Le Siepi, Via Filippo Turati Montanino 16 (1)</b> → <b>Loc. Podere la Romola 78 (14)</b> → "
         "<b>Podere Houston/Giusti, Loc. Giusti 105 (4)</b> → <b>location — Fattoria I Bonsi, Via Bonsi 47.</b> "
         "Arrivo in location verso le 17:00.",
         "dalle 16:20<br/>19 ospiti"),
        ("Mezzo 2<br/>seconda corsa",
         "<b>Loc. S. Giovenale 55 (2)</b> → <b>La Terrazza di Reggello, Via di Fano 6 (2)</b> → "
         "<b>Appartamento Olivella, Via Fornacina 32 (2)</b> → <b>Via dei Glicini 14, Poggio ai Giubbiani (2)</b> → "
         "<b>location — Fattoria I Bonsi, Via Bonsi 47.</b> Arrivo in location verso le 17:50, comodamente prima "
         "del vostro limite delle 18:00.",
         "dalle 17:15<br/>8 ospiti"),
        ("Entrambi i mezzi<br/>in location",
         "I minibus restano parcheggiati alla Fattoria I Bonsi per tutto il ricevimento, a vostra disposizione "
         "con i conducenti.",
         "18:00 – 23:00"),
        ("Rientri<br/>due corse per mezzo",
         "Il <b>Mezzo 1</b> parte alle 23:00 con i venti ospiti di Casalino e Loc. Rovai, tutti a casa verso le "
         "23:20; rientra in location alle 23:30 e riporta gli ultimi tre a I Trebbiali e a Villa Pitiana entro le "
         "23:55 circa. Il <b>Mezzo 2</b> parte alle 23:00 con gli otto ospiti di Poggio ai Giubbiani, Via "
         "Fornacina, Via di Fano e S. Giovenale, a casa verso le 23:30; torna in location alle 23:47 e riporta gli "
         "ultimi diciannove a Loc. Giusti, Podere la Romola e Montanino, con l'ultimo indirizzo raggiunto intorno "
         "alle 00:25.",
         "dalle 23:00<br/>fino alle 00:25 ca."),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("<b>Trasporto — Mezzo 1</b> (minibus, 25+1+1). Raccolta a cinque indirizzi in due corse, trasferimento in "
         "location entro le 18:00, mezzo e conducente a vostra disposizione dalle 18:00 alle 23:00, rientro agli "
         "stessi indirizzi dalle 23:00, di nuovo in due corse. Carburante, pedaggi autostradali, parcheggi, "
         "assicurazione e movimentazione del mezzo da e per la nostra rimessa sono compresi.",
         "€ 1.100,00", "+ IVA 10%"),
        ("<b>Trasporto — Mezzo 2</b> (minibus, 27+1+1). Raccolta a sette indirizzi in due corse, trasferimento in "
         "location entro le 18:00, mezzo e conducente a vostra disposizione dalle 18:00 alle 23:00, rientro agli "
         "stessi indirizzi dalle 23:00, di nuovo in due corse. Stesse voci comprese della riga precedente.",
         "€ 1.100,00", "+ IVA 10%"),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.200,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.420,00.",
    price_note=(
        "Trasporto € 2.200,00 + IVA 10% (€ 220,00). Le quattro corse di raccolta e le quattro di rientro sono "
        "tutte comprese in questo prezzo. Prezzo fisso, nessun addebito ulteriore oltre a quanto elencato sotto "
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
        "Due minibus e due autisti professionisti per tutta la serata, dal primo ritiro all'ultimo rientro.",
        "Quattro corse di raccolta e quattro di rientro, due per mezzo, così che il tempo a bordo resti al massimo "
        "sulla mezz'ora.",
        "Carburante, pedaggi autostradali, parcheggi e assicurazione.",
        "Movimentazione dei due mezzi da e per la nostra rimessa, prima e dopo il servizio.",
        "Mezzi e conducenti a vostra disposizione in location dalle 18:00 alle 23:00.",
        "Servizio in orario notturno: gli ultimi ospiti vengono riaccompagnati dopo la mezzanotte.",
        "Tutte le imposte dovute: l'IVA al 10% è esposta a parte qui sopra ed è già conteggiata nel totale da "
        "corrispondere.",
    ],
    h_nonincluso="Non incluso",
    nonincluso=[
        "Qualsiasi trasferimento in più rispetto a quelli descritti — per esempio un rientro anticipato per una "
        "parte del gruppo prima delle 23:00: possiamo organizzarlo, quotato a parte.",
        "Più di 52 ospiti, che è la capienza complessiva dei due mezzi: un gruppo più numeroso richiederebbe un "
        "terzo mezzo, da quotare a parte.",
        "Attesa oltre gli orari concordati: € 50,00 all'ora per mezzo.",
        "Pasti, mance e spese personali dei conducenti non legate al servizio.",
        "Tutto quanto non espressamente indicato qui sopra.",
    ],
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 726,00", "IVA inclusa"),
        ("Saldo, entro il 20 settembre 2026", "€ 1.694,00", ""),
    ],
    pay_text=(
        "Il saldo è dovuto entro il 20 settembre 2026, cinque giorni prima del servizio. Le coordinate bancarie "
        "vengono inviate con la richiesta di conferma; la prenotazione diventa definitiva quando l'acconto arriva "
        "sul nostro conto. Per l'intero importo viene emessa regolare fattura."
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
        "<b>Il numero definitivo degli ospiti.</b> Questo preventivo è costruito su 50, sugli undici punti di "
        "carico che ci avete indicato. I due mezzi hanno 52 posti, quindi c'è spazio per due persone in più; oltre "
        "servirebbe un terzo mezzo.",
        "<b>Sull'ultimo rientro.</b> Le due corse per mezzo tengono corto il tempo a bordo, che era la vostra "
        "preoccupazione principale: gli ospiti della seconda corsa non aspettano a bordo, restano al ricevimento "
        "fino a mezzanotte circa e poi viaggiano per una ventina di minuti. L'ultimo rientro resta comunque "
        "intorno alle 00:25. Riportare tutti a casa sensibilmente prima richiederebbe un terzo mezzo, non un "
        "orario diverso, perché ogni seconda corsa può partire solo quando la prima è rientrata.",
        "<b>Se a ogni indirizzo ci arriva un minibus.</b> Diversi punti di ritiro sono case coloniche su strade "
        "strette. Dove un minibus non può girare o passare, concordiamo un punto d'incontro a pochi passi, "
        "piuttosto che rischiare la sera stessa.",
        "<b>La posizione esatta di Loc. Podere la Romola 78 e Loc. Giusti 105</b> — basta uno spillo sulla mappa o "
        "un numero di telefono per ciascuno per fissare l'ordine dei ritiri.",
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
    meta="Prepared for %s  ·  8 September 2026  ·  Ref. " + RIF + "  ·  valid until 15 September 2026",
    intro=(
        "Thank you for your enquiry and for the details of your group. This quotation is built around your two "
        "points: 50 guests, with three of them at Hotel Archimede, and each minibus doing two short runs rather "
        "than one long one, so that nobody spends more than about half an hour on board. Both vehicles are compact "
        "minibuses rather than full-size coaches, which is what the hill roads around Pietrapiana, Donnini and "
        "Cascia require."
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
        ("Seating", "52 passenger seats against 50 guests: everyone fits comfortably, with two seats to spare."),
        ("Time on board",
         "Around 30 minutes at most, and 10 to 20 minutes for most guests. This is what the two runs per vehicle "
         "are for: each run covers a small cluster of addresses close to one another, so no one sits through the "
         "whole collection."),
        ("Drivers", "Two professional drivers, one per vehicle, on duty for the whole evening."),
    ],
    h_servizio="Programme — Friday 25 September 2026",
    svc_intro=(
        "Four short collection runs, two per vehicle, running in parallel so that every guest is at the venue well "
        "before 18:00. The times below are our working plan: we confirm the exact pick-up time for each address "
        "three to four days before the wedding, once you have told us which addresses a minibus can actually "
        "reach. Both vehicles then stay at the venue and take the same guests back from 23:00, again in two runs "
        "each."
    ),
    svc_head=["Run", "Route", "Timing"],
    svc=[
        ("Vehicle 1<br/>first run",
         "<b>Casalino, Via Ponte di Casalino 66–68 (17)</b> — Hotel Archimede and Podere Casalino are 120 m apart "
         "on the same road, so we serve them as a single stop → <b>Loc. Rovai 26, Pietrapiana (3)</b> → "
         "<b>venue — Fattoria I Bonsi, Via Bonsi 47.</b> Two stops a few minutes apart, with the venue barely "
         "three minutes further on; arrival around 17:00.",
         "from 16:35<br/>20 guests"),
        ("Vehicle 1<br/>second run",
         "<b>Villa Pitiana Hotel, Via Provinciale per Tosi 7 (1)</b> → <b>Loc. I Trebbiali 116 (2)</b> → "
         "<b>venue, Via Bonsi 47.</b> Arrival at the venue around 17:45.",
         "from 17:20<br/>3 guests"),
        ("Vehicle 2<br/>first run",
         "<b>Le Siepi, Via Filippo Turati Montanino 16 (1)</b> → <b>Loc. Podere la Romola 78 (14)</b> → "
         "<b>Podere Houston/Giusti, Loc. Giusti 105 (4)</b> → <b>venue — Fattoria I Bonsi, Via Bonsi 47.</b> "
         "Arrival at the venue around 17:00.",
         "from 16:20<br/>19 guests"),
        ("Vehicle 2<br/>second run",
         "<b>Loc. S. Giovenale 55 (2)</b> → <b>La Terrazza di Reggello, Via di Fano 6 (2)</b> → "
         "<b>Appartamento Olivella, Via Fornacina 32 (2)</b> → <b>Via dei Glicini 14, Poggio ai Giubbiani (2)</b> → "
         "<b>venue — Fattoria I Bonsi, Via Bonsi 47.</b> Arrival at the venue around 17:50, comfortably before "
         "your 18:00 deadline.",
         "from 17:15<br/>8 guests"),
        ("Both vehicles<br/>at the venue",
         "The minibuses stay parked at Fattoria I Bonsi for the whole reception, at your disposal together with "
         "their drivers.",
         "18:00 – 23:00"),
        ("Return<br/>two runs per vehicle",
         "<b>Vehicle 1</b> leaves at 23:00 with the twenty guests at Casalino and Loc. Rovai, all of whom are home "
         "by about 23:20; it is back at the venue at 23:30 and takes the last three to I Trebbiali and Villa "
         "Pitiana by about 23:55. <b>Vehicle 2</b> leaves at 23:00 with the eight guests at Poggio ai Giubbiani, "
         "Via Fornacina, Via di Fano and S. Giovenale, home by about 23:30; it returns to the venue at 23:47 and "
         "takes the last nineteen to Loc. Giusti, Podere la Romola and Montanino, the final address reached around "
         "00:25.",
         "from 23:00<br/>until about 00:25"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("<b>Transport — Vehicle 1</b> (minibus, 25+1+1). Collection from five addresses in two runs, transfer to "
         "the venue by 18:00, vehicle and driver at your disposal from 18:00 to 23:00, return to the same "
         "addresses from 23:00, again in two runs. Fuel, motorway tolls, parking, insurance and positioning of the "
         "vehicle from and to our depot are included.",
         "€ 1,100.00", "+ VAT 10%"),
        ("<b>Transport — Vehicle 2</b> (minibus, 27+1+1). Collection from seven addresses in two runs, transfer to "
         "the venue by 18:00, vehicle and driver at your disposal from 18:00 to 23:00, return to the same "
         "addresses from 23:00, again in two runs. Same inclusions as the line above.",
         "€ 1,100.00", "+ VAT 10%"),
    ],
    price_total_label="Total, net of VAT",
    price_total="€ 2,200.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,420.00.",
    price_note=(
        "Transport € 2,200.00 + VAT 10% (€ 220.00). The four collection runs and four return runs are all included "
        "at this price. Fixed price, no further charges beyond what is listed under “Not included”."
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
        "Two minibuses and two professional drivers for the whole evening, from the first pick-up to the last "
        "drop-off.",
        "Four collection runs and four return runs, two per vehicle, so that time on board stays around 30 minutes "
        "at most.",
        "Fuel, motorway tolls, parking and insurance.",
        "Positioning of both vehicles from and to our depot, before and after the service.",
        "Both vehicles and drivers at your disposal at the venue from 18:00 to 23:00.",
        "Night-time operation: the last guests are dropped off after midnight.",
        "All applicable taxes: VAT at 10% is shown separately above and is already counted in the total payable.",
    ],
    h_nonincluso="Not included",
    nonincluso=[
        "Any additional journey beyond the ones described above — for example an earlier return for part of the "
        "group before 23:00: we can organise it, quoted separately.",
        "More than 52 guests, which is the total seating of the two vehicles: a larger group would need a third "
        "vehicle, to be quoted separately.",
        "Waiting beyond the agreed times: € 50.00 per hour, per vehicle.",
        "Meals, gratuities and personal expenses of the drivers not related to the service.",
        "Anything not expressly listed above.",
    ],
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit of 30% on confirmation", "€ 726.00", "VAT included"),
        ("Balance, by 20 September 2026", "€ 1,694.00", ""),
    ],
    pay_text=(
        "The balance is due by 20 September 2026, five days before the service. Bank details are sent with the "
        "confirmation request; the booking becomes firm when the deposit reaches our account. A tax invoice is "
        "issued for the full amount."
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
        "<b>The final number of guests.</b> This quotation is built on 50, across the eleven loading points you "
        "sent us. The two vehicles seat 52, so there is room for two more; above that we would need a third "
        "vehicle.",
        "<b>On the last return.</b> The two runs per vehicle keep time on board short, which was your main "
        "concern: the guests on the second run are not waiting on board, they stay at the reception until around "
        "midnight and then travel for about twenty minutes. The final drop-off still lands at around 00:25. "
        "Bringing everyone home substantially earlier than that would take a third vehicle rather than a different "
        "schedule, since each second run can only start once the first one is back.",
        "<b>Whether a minibus can reach each address.</b> Several pick-up points are farm houses on narrow lanes. "
        "Where a minibus cannot turn or pass, we agree a meeting point a short walk away rather than risk it on "
        "the evening.",
        "<b>The exact location of Loc. Podere la Romola 78 and Loc. Giusti 105</b> — a map pin or a phone number "
        "for each is enough to fix the order of the pick-ups.",
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
        HERE, "GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, cliente, name))

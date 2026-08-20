#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il servizio navetta del 9 ottobre 2026.

House of Nine (Firenze) -> Villa Medicea di Lilliano (Grassina) -> Tenuta Bossi
(Pontassieve) -> Firenze. Il servizio e' quotato sui due minibus, Beluga e
Tourengo (25+1+1 e 27+1+1), 52 posti passeggeri in tutto.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_navetta_9_ottobre.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_navetta_9_ottobre.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-1009-HN"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Servizio navetta, Firenze · Grassina · Pontassieve  ·  venerdì 9 ottobre 2026",
    meta="Preparato per %s  ·  20 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="I mezzi",
    mezzo_intro=(
        "Due minibus con conducente, entrambi sotto gli otto metri come ci avete chiesto: è la scelta "
        "giusta per Via Lilliano e Meoli e per Via dello Stracchino, due strade di collina dove un autobus "
        "gran turismo non arriva."
    ),
    mezzo_bullets=[
        "<b>Mercedes-Benz Beluga</b> — <b>25+1+1</b>, cioè 25 posti passeggeri più l'autista e "
        "l'accompagnatore, 7,64 m. Aria condizionata, sedili ultra comfort reclinabili, frigo bar, "
        "impianto audio di bordo, ampio vano bagagli.",
        "<b>Mercedes-Benz Tourengo</b> — <b>27+1+1</b>, cioè 27 posti passeggeri più l'autista e "
        "l'accompagnatore, 7,86 m. Aria condizionata, sedili reclinabili, impianto audio di bordo, "
        "ampio vano bagagli.",
    ],
    mezzo_close=(
        "Mettiamo a disposizione <b>questi due mezzi e nessun altro</b>: in tutto <b>52 posti passeggeri</b>, "
        "ed è a loro che si riferisce il prezzo. Ci avete indicato un gruppo di 80-100 persone, quindi per i "
        "passeggeri oltre i 52 servono altri mezzi, che non sono compresi in questo preventivo: ne parliamo "
        "per esteso fra le note. I due minibus portano il numero 1 e il numero 2 bene in vista, così i "
        "vostri ospiti ritrovano il proprio a ogni tappa."
    ),
    h_servizio="Il servizio",
    svc_head=["Trasferimento", "Percorso", "Impegno dei mezzi"],
    svc=[
        ("1 · 14:30",
         "<b>Firenze, House of Nine (Via dei Conti 9) → Villa Medicea di Lilliano, Via Lilliano e Meoli 82, "
         "Grassina (FI).</b> I due minibus sono in posizione alle 14:00 al punto di carico concordato, "
         "imbarco dalle 14:15 e partenza alle 14:30. Circa 12 km e 35 minuti nel traffico del venerdì "
         "pomeriggio, con arrivo in villa verso le 15:05.",
         "14:00 – 15:15"),
        ("2 · 18:00",
         "<b>Villa Medicea di Lilliano → Tenuta Bossi, Marchesi Gondi, Via dello Stracchino 32, "
         "Pontassieve (FI).</b> Partenza alle 18:00 e circa 25 km per Bagno a Ripoli e Rosano, "
         "45 minuti, con arrivo alla tenuta verso le 18:45.",
         "18:00 – 19:00"),
        ("3 · 23:00",
         "<b>Tenuta Bossi → Firenze, House of Nine.</b> Partenza alle 23:00 e circa 22 km lungo l'Aretina, "
         "35 minuti, con rientro a Firenze verso le 23:40 allo stesso punto del carico.",
         "23:00 – 24:00"),
        ("Fra un trasferimento e l'altro",
         "<b>I mezzi e i conducenti restano con voi.</b> Fra il primo e il secondo trasferimento passano quasi "
         "tre ore, fra il secondo e il terzo più di quattro. La nostra base è a 55 km da Firenze, quindi i mezzi "
         "non rientrano: restano sul posto con i conducenti, a vostra disposizione dalle 14:00 alle 24:00. "
         "Se serve anticipare un orario o fare un giro in più, basta dirlo al conducente sul momento.",
         "tutta la giornata"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Minibus 1 — Mercedes-Benz Beluga, 25+1+1 · i tre trasferimenti, mezzo e conducente a "
         "disposizione dalle 14:00 alle 24:00", "€ 1.150,00", "+ IVA 10%"),
        ("Minibus 2 — Mercedes-Benz Tourengo, 27+1+1 · stesso servizio", "€ 1.150,00", "+ IVA 10%"),
        ("Vitto e alloggio dei conducenti — non necessario con gli orari in programma, dovuto solo se il "
         "rientro slitta ben oltre le 02:00 (vedi note)", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.300,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.530,00.",
    perhead=("Il prezzo è per mezzo e vale per i due minibus qui descritti, 52 posti passeggeri in tutto: "
             "a pieno carico sono circa € 49,00 a persona."),
    h_incluso="Incluso.",
    incluso=(
        "Due mezzi e due conducenti, carburante, pedaggi, parcheggi, assicurazione completa e la "
        "disponibilità dei minibus dalle 14:00 alle 24:00, non solo per i tre trasferimenti in programma. "
        "A Grassina e a Pontassieve non sono dovuti oneri di accesso: né Villa Medicea di Lilliano né "
        "Tenuta Bossi si trovano in zona a traffico limitato."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il trasporto dei passeggeri oltre i 52 posti dei due minibus: mezzi ulteriori non sono compresi "
        "in questo preventivo (vedi note). Il permesso comunale di accesso dei bus turistici al centro di Firenze, necessario soltanto se "
        "carico e scarico avvengono davanti all'albergo in Via dei Conti: circa € 350,00 per mezzo, che vi "
        "addebiteremmo al costo (vedi note). Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. "
        "Trasferimenti aggiuntivi o modifiche al programma, quotati su richiesta. Rientro a Firenze dopo le "
        "02:00, € 250,00 per mezzo. Vitto e alloggio dei conducenti, se il programma dovesse allungarsi al "
        "punto da renderli necessari."
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
        ("<b>Mettiamo a disposizione due minibus: il Beluga e il Tourengo.</b> Sono 52 posti passeggeri in "
         "tutto, e il prezzo di questo preventivo è riferito a loro due. Ci avete indicato un gruppo di "
         "80-100 persone: i passeggeri oltre i 52 hanno bisogno di altri mezzi, che qui non sono compresi. "
         "Potete organizzarli voi direttamente, oppure ditecelo e vediamo se riusciamo a trovarveli — in "
         "quel caso ve li quoteremmo a parte. Quello che non possiamo fare è coprire il gruppo intero "
         "facendo due viaggi con questi due mezzi: fra il primo e l'ultimo trasferimento la giornata dei "
         "conducenti è già di dodici ore, e raddoppiare le corse la porterebbe oltre i limiti di guida "
         "consentiti. Ci serve comunque il numero definitivo dei passeggeri, così vi confermiamo come si "
         "ripartiscono sui due minibus."),
        ("<b>Il punto di carico a Firenze.</b> House of Nine è in Via dei Conti 9, a due passi dal Duomo: "
         "siamo nel cuore della ZTL, in una strada dove un minibus da otto metri non può fermarsi a "
         "caricare. La soluzione che usiamo sempre è caricare e scaricare in <b>Via Valfonda o in Piazza "
         "Adua</b>, dietro la stazione di Santa Maria Novella, dove la sosta dei bus è autorizzata: sono "
         "poco più di 400 metri dall'albergo, cinque minuti a piedi in piano, e non comportano alcun onere. "
         "Se invece volete i mezzi davanti all'ingresso serve il permesso comunale per i bus turistici, "
         "circa € 350,00 a mezzo, da richiedere con qualche giorno di anticipo: lo gestiamo noi e ve lo "
         "addebitiamo al costo. Diteci quale delle due soluzioni preferite, perché cambia il preventivo."),
        ("<b>Le 23:00 da Tenuta Bossi.</b> È il punto su cui vi chiediamo di essere realistici, perché a una "
         "festa l'orario di partenza slitta quasi sempre: l'attesa oltre l'orario concordato costa € 50,00 "
         "all'ora per mezzo, cioè € 100,00 all'ora per i due, e un rientro che si chiude dopo le 02:00 costa "
         "€ 250,00 per mezzo. Molto meglio fissare adesso l'orario vero: <b>possiamo spostare la partenza "
         "fino alle 00:30 senza differenza di prezzo</b>, purché lo decidiate alla conferma e non la sera "
         "stessa. Oltre quell'ora la giornata dei conducenti supera i limiti di guida e servirebbe un "
         "secondo turno."),
        ("<b>Accesso e sosta a Villa Medicea di Lilliano.</b> Via Lilliano e Meoli sale da Grassina per circa "
         "un chilometro ed è stretta: è esattamente il motivo per cui ci avete chiesto mezzi di questa "
         "classe. Ci servono due conferme dalla villa, possibilmente per iscritto: dove scaricano i mezzi e "
         "se possono restare parcheggiati in tenuta dalle 15:00 alle 18:00. Se lo spazio non c'è, i minibus "
         "scendono a Grassina e risalgono alle 18:00 senza costi aggiuntivi — ma è una cosa da sapere prima, "
         "non davanti al cancello."),
        ("<b>Accesso e sosta a Tenuta Bossi.</b> Stesso discorso, e più delicato: qui l'attesa è di oltre "
         "quattro ore e la ripartenza è di notte, su una strada di collina stretta e senza illuminazione. "
         "Chiedete alla tenuta il punto di discesa, lo spazio di manovra e, se possibile, che i minibus "
         "restino dentro fino alla partenza: alle 23:00 e al buio, averli già in posizione fa risparmiare "
         "tempo e parecchia confusione."),
        ("<b>I posti dei due minibus e il limite dei 25.</b> Il Beluga è omologato <b>25+1+1</b>: "
         "venticinque posti passeggeri, più il posto dell'autista e quello dell'accompagnatore. Sta quindi "
         "esattamente dentro il limite che ci avete indicato. Il Tourengo è <b>27+1+1</b>, quindi due "
         "passeggeri in più, ma è lungo 7,86 m: su strada ingombra quanto il Beluga e nelle due salite si "
         "comporta allo stesso modo. Se il limite dei 25 ve lo ha posto una delle due strutture ed è un "
         "limite di persone e non di mezzo, ditecelo: sul Tourengo carichiamo 25 e i posti passeggeri "
         "diventano 50 in tutto."),
        ("<b>Due mezzi si muovono insieme solo se qualcuno li coordina.</b> Il tempo si perde nell'imbarco, "
         "non in strada. Vi proponiamo di assegnare gli ospiti al minibus 1 o al minibus 2 fin dal primo "
         "trasferimento, così a ogni tappa ognuno risale sul suo. Al vostro referente lasciamo i numeri di "
         "cellulare dei due conducenti e teniamo una sola persona di riferimento da parte nostra per tutta "
         "la giornata."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, la scelta del punto di carico "
         "a Firenze, le conferme di accesso e sosta dalle due strutture, l'orario di partenza definitivo da "
         "Tenuta Bossi, un recapito telefonico o WhatsApp della persona che segue il gruppo sul posto e i "
         "vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> I due minibus sono al momento liberi e li teniamo a "
         "vostra disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla "
         "ricezione dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 "
         "giorni viene trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli "
         "ultimi 10 giorni il 100%. Mancando oggi 50 giorni al servizio, questa prenotazione ricade nella "
         "fascia da 60 a 30 giorni, e dal 9 settembre passerà in quella da 30 a 10. "
         "Preventivo valido fino al 3 settembre 2026."),
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
    subtitle="Shuttle service, Florence · Grassina · Pontassieve  ·  Friday 9 October 2026",
    meta="Prepared for %s  ·  20 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicles",
    mezzo_intro=(
        "Two minibuses with drivers, both under eight metres as you asked: the right choice for Via Lilliano "
        "e Meoli and Via dello Stracchino, two hill roads a full-size coach cannot manage."
    ),
    mezzo_bullets=[
        "<b>Mercedes-Benz Beluga</b> — <b>25+1+1</b>: 25 passenger seats plus the driver and the courier, "
        "7.64 m. Air conditioning, reclining ultra-comfort seats, fridge bar, on-board audio system, "
        "large luggage hold.",
        "<b>Mercedes-Benz Tourengo</b> — <b>27+1+1</b>: 27 passenger seats plus the driver and the "
        "courier, 7.86 m. Air conditioning, reclining seats, on-board audio system, large luggage hold.",
    ],
    mezzo_close=(
        "We are putting <b>these two vehicles and no others</b> at your disposal: <b>52 passenger seats</b> in total, "
        "and that is what the price covers. You told us the group is 80-100 people, so the passengers "
        "beyond 52 need further vehicles, which are not part of this quotation: we set this out in full in "
        "the notes below. The two minibuses carry the numbers 1 and 2 clearly displayed, so your guests "
        "find the same one at every stage."
    ),
    h_servizio="The service",
    svc_head=["Transfer", "Route", "Vehicles engaged"],
    svc=[
        ("1 · 14:30",
         "<b>Florence, House of Nine (Via dei Conti 9) → Villa Medicea di Lilliano, Via Lilliano e Meoli 82, "
         "Grassina (FI).</b> The two minibuses are in position at 14:00 at the agreed boarding point, "
         "boarding from 14:15 and departure at 14:30. About 12 km and 35 minutes in Friday afternoon "
         "traffic, reaching the villa around 15:05.",
         "14:00 – 15:15"),
        ("2 · 18:00",
         "<b>Villa Medicea di Lilliano → Tenuta Bossi, Marchesi Gondi, Via dello Stracchino 32, "
         "Pontassieve (FI).</b> Departure at 18:00 and about 25 km via Bagno a Ripoli and Rosano, "
         "45 minutes, reaching the estate around 18:45.",
         "18:00 – 19:00"),
        ("3 · 23:00",
         "<b>Tenuta Bossi → Florence, House of Nine.</b> Departure at 23:00 and about 22 km along the "
         "Aretina, 35 minutes, back in Florence around 23:40 at the same point as the pick-up.",
         "23:00 – 24:00"),
        ("Between transfers",
         "<b>Vehicles and drivers stay with you.</b> Almost three hours pass between the first and second "
         "transfer, more than four between the second and the third. Our base is 55 km from Florence, so the "
         "vehicles do not go back: they stay on site with their drivers, at your disposal from 14:00 to "
         "24:00. If you need to bring a time forward or add a run, just tell the driver on the spot.",
         "all day"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Minibus 1 — Mercedes-Benz Beluga, 25+1+1 · the three transfers, vehicle and driver at your "
         "disposal from 14:00 to 24:00", "€ 1,150.00", "+ VAT 10%"),
        ("Minibus 2 — Mercedes-Benz Tourengo, 27+1+1 · same service", "€ 1,150.00", "+ VAT 10%"),
        ("Drivers' board and lodging — not required with the programme as scheduled, due only if the return "
         "slips well past 02:00 (see notes)", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,300.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,530.00.",
    perhead=("The price is per vehicle and covers the two minibuses described here, 52 passenger seats in total: "
             "at full load that is about € 49.00 per person."),
    h_incluso="Included.",
    incluso=(
        "Two vehicles and two drivers, fuel, tolls, parking, full insurance and the minibuses at your "
        "disposal from 14:00 to 24:00, not only for the three scheduled transfers. No access charges are "
        "due at Grassina or Pontassieve: neither Villa Medicea di Lilliano nor Tenuta Bossi sits inside a "
        "restricted traffic zone."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Transport for passengers beyond the 52 seats on the two minibuses: further vehicles are not part "
        "of this quotation (see notes). The city permit for tourist coaches entering the centre of Florence, needed only if boarding and drop-off happen "
        "outside the hotel in Via dei Conti: about € 350.00 per vehicle, which we would charge you at cost "
        "(see notes). Waiting beyond the times set out here, € 50.00 per hour per vehicle. Additional "
        "transfers or changes to the programme, quoted on request. Return to Florence after 02:00, "
        "€ 250.00 per vehicle. The drivers' board and lodging, should the programme stretch far enough to "
        "make them necessary."
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
        ("<b>We are putting two minibuses at your disposal: the Beluga and the Tourengo.</b> That is 52 "
         "passenger seats in total, and the price in this quotation is for those two. You told us the group is 80-100 "
         "people: the passengers beyond 52 need further vehicles, and those are not included here. You can "
         "arrange them yourselves, or tell us and we will see whether we can find them for you — in that "
         "case we would quote them separately. What we cannot do is cover the whole group by running these "
         "two vehicles twice: between the first and the last transfer the drivers' day is already twelve "
         "hours, and doubling the runs would take it beyond the permitted driving limits. We still need the "
         "final passenger count, so we can confirm how it splits across the two minibuses."),
        ("<b>The boarding point in Florence.</b> House of Nine is at Via dei Conti 9, a few steps from the "
         "Duomo: that is the heart of the restricted traffic zone, on a street where an eight-metre minibus "
         "cannot stop to board passengers. The arrangement we always use is to board and drop off in "
         "<b>Via Valfonda or Piazza Adua</b>, behind Santa Maria Novella station, where coach stops are "
         "authorised: just over 400 metres from the hotel, five minutes on the flat, and no charge at all. "
         "If you would rather have the vehicles at the door, the city permit for tourist coaches is "
         "required, about € 350.00 per vehicle, applied for some days in advance: we handle it and pass it "
         "on at cost. Tell us which of the two you prefer, because it changes the quotation."),
        ("<b>The 23:00 departure from Tenuta Bossi.</b> This is where we ask you to be realistic. At a party "
         "the departure time almost always slips: waiting beyond the agreed time costs € 50.00 per hour per "
         "vehicle, which is € 100.00 an hour for the two, and a return that ends after 02:00 costs € 250.00 "
         "per vehicle. It is far better to fix the real time now: <b>we can move the departure as late as "
         "00:30 with no change in price</b>, as long as you decide it at confirmation and not on the night. "
         "Beyond that hour the drivers' day exceeds the permitted limits and a second shift would be "
         "needed."),
        ("<b>Access and parking at Villa Medicea di Lilliano.</b> Via Lilliano e Meoli climbs from Grassina "
         "for about a kilometre and it is narrow: precisely why you asked for vehicles of this class. We "
         "need two confirmations from the villa, in writing if possible: where the vehicles set down, and "
         "whether they may stay parked on the estate from 15:00 to 18:00. If there is no room, the "
         "minibuses go back down to Grassina and come up again at 18:00 at no extra cost — but it is "
         "something to know beforehand, not at the gate."),
        ("<b>Access and parking at Tenuta Bossi.</b> The same question, and a more delicate one: here the "
         "wait is over four hours and the departure is at night, on a narrow unlit hill road. Please ask the "
         "estate for the set-down point, the manoeuvring space and, if possible, for the minibuses to stay "
         "inside until departure: at 23:00 in the dark, having them already in position saves time and a "
         "good deal of confusion."),
        ("<b>The seats on the two minibuses and the 25 limit.</b> The Beluga is homologated <b>25+1+1</b>: "
         "twenty-five passenger seats, plus the driver's seat and the courier's. It therefore sits exactly "
         "within the limit you gave us. The Tourengo is <b>27+1+1</b>, so two passengers more, but it is "
         "7.86 m long: on the road it takes the same space as the Beluga and it handles both climbs the "
         "same way. If the 25 limit was set by one of the two venues and is a limit on people rather than "
         "on the vehicle, tell us: we will load 25 on the Tourengo and the passenger seats become 50 in "
         "total."),
        ("<b>Two vehicles move together only if someone coordinates them.</b> The time is lost in boarding, "
         "not on the road. We suggest assigning guests to minibus 1 or minibus 2 from the first transfer "
         "onwards, so at every stage each person gets back on the same one. We give your coordinator the "
         "mobile numbers of both drivers and keep a single point of contact on our side for the whole day."),
        ("<b>To confirm we need</b> the final passenger count, your choice of boarding point in Florence, "
         "the access and parking confirmations from both venues, the definitive departure time from Tenuta "
         "Bossi, a mobile or WhatsApp contact for the person looking after the group on site, and your "
         "invoicing details."),
        ("<b>Availability and cancellation.</b> The two minibuses are currently free and we hold them for "
         "you for the whole validity of this quotation; the booking becomes firm on receipt of the deposit. "
         "Cancellation is free of charge more than 60 days before the service; from 60 to 30 days the "
         "deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. "
         "With 50 days to the service today, this booking falls in the 60-to-30-day band, and from "
         "9 September it moves into the 30-to-10 band. Quotation valid until 3 September 2026."),
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

    # --- mezzi
    F.append(Paragraph(L["h_mezzo"], S["h2"]))
    F.append(Paragraph(L["mezzo_intro"], S["body"]))
    for testo in L["mezzo_bullets"]:
        bullet = Table([[Paragraph(testo, S["cellsm"])]], colWidths=[usable])
        bullet.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), CREAM),
            ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]))
        F.append(bullet)
        F.append(Spacer(1, 5))
    F.append(Spacer(1, 2))
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="House of Nine")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Navetta_9_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

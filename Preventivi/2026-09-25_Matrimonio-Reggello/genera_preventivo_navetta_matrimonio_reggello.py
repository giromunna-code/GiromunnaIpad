#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la navetta del matrimonio a Reggello (FI)
del 25-26 settembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_navetta_matrimonio_reggello.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_navetta_matrimonio_reggello.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0925-VB"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    cliente_default="il vostro matrimonio a Reggello",
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Navetta per matrimonio · Reggello (FI), 12 indirizzi di raccolta → Via Bonsi 47  ·  25-26 settembre 2026",
    meta="Preparato per %s  ·  8 settembre 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus con lo stesso conducente per tutte e due le serate, che raccoglie i vostri ospiti "
        "ai dodici indirizzi e li riporta a casa a fine festa."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "I 7,64 metri sono la ragione per cui questo mezzo funziona a Reggello: sta sotto gli 8 metri e arriva "
        "dove un autobus gran turismo non passa, sulle strade strette che salgono ai poderi e nelle vie del paese. "
        "<b>I vostri ospiti però sono 54 e i posti a bordo sono 26:</b> un mezzo solo non li porta in una volta. "
        "Il prezzo qui sotto è riferito a un mezzo e il programma è costruito su tre giri di raccolta; "
        "nella prima nota trovate per esteso che cosa comporta e come cambia con due o tre minibus."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Servizio", "Impegno del mezzo"],
    svc=[
        ("Ven 25 set",
         "<b>Andata — dai dodici indirizzi a Via Bonsi 47.</b> Tre giri di raccolta consecutivi, calcolati a ritroso "
         "dalla vostra scadenza delle 18:00: il primo giro parte verso le 15:05 e arriva in Via Bonsi alle 15:45, "
         "il secondo parte alle 15:55 e arriva alle 16:45, il terzo parte alle 16:55 e arriva alle 17:55.",
         "circa 15:00 – 18:00"),
        ("Ven 25 set",
         "<b>Rientro — da Via Bonsi 47 ai dodici indirizzi.</b> Prima partenza alle 23:00 con il gruppo di "
         "Pietrapiana, rientro in Via Bonsi verso le 23:50; seconda partenza alle 23:55, rientro verso le 00:50; "
         "terza e ultima partenza alle 00:55, ultimo ospite a casa verso le 01:45.",
         "circa 23:00 – 01:45"),
        ("Sab 26 set",
         "<b>Andata — dai dodici indirizzi a Via Bonsi 47.</b> Gli stessi tre giri, calcolati a ritroso dalla "
         "scadenza delle 15:30: primo giro alle 12:45 con arrivo alle 13:25, secondo alle 13:35 con arrivo alle "
         "14:25, terzo alle 14:35 con arrivo alle 15:25.",
         "circa 12:40 – 15:30"),
        ("Dom 27 set",
         "<b>Rientro — da Via Bonsi 47 ai dodici indirizzi.</b> Prima partenza alle 01:00, rientro in Via Bonsi "
         "verso le 01:50; seconda partenza alle 01:55, rientro verso le 02:50; terza e ultima partenza alle 02:55, "
         "ultimo ospite a casa verso le 03:45.",
         "circa 01:00 – 03:45"),
    ],
    h_giri="I tre giri di raccolta",
    giri_intro=(
        "Abbiamo raggruppato i dodici indirizzi per zona, in modo che ogni giro resti compatto e che il gruppo più "
        "numeroso viaggi tutto insieme. Gli ospiti di ciascun giro partono e rientrano insieme, sempre alla stessa ora."
    ),
    giri_head=["Giro", "Indirizzo", "Ospiti"],
    giri=[
        ("<b>1 · Pietrapiana</b><br/><font size=7.4 color='#6B6B6B'>24 ospiti · 3 fermate</font>", [
            ("Via Casalino 66, Loc. Pietrapiana", "14"),
            ("Hotel Archimede, Ponte di Casalino 68", "7"),
            ("Località Rovai 26, Pietrapiana", "3"),
        ]),
        ("<b>2 · La Romola e i poderi</b><br/><font size=7.4 color='#6B6B6B'>22 ospiti · 4 fermate</font>", [
            ("Località Podere la Romola 78", "14"),
            ("Podere Houston / Giusti, Località Giusti 105", "4"),
            ("Loc. I Trebbiali 116", "2"),
            ("Via dei Glicini 14, Poggio ai Giubbiani", "2"),
        ]),
        ("<b>3 · Reggello, Donnini e San Giovenale</b><br/><font size=7.4 color='#6B6B6B'>8 ospiti · 5 fermate</font>", [
            ("La Terrazza di Reggello, Via di Fano 6", "2"),
            ("Appartamento Olivella, Via Fornacina 32", "2"),
            ("Località S. Giovenale 55", "2"),
            ("Le Siepi, Via Filippo Turati, Montanino 16", "1"),
            ("Villa Pitiana Hotel, Donnini", "1"),
        ]),
    ],
    giri_total="Totale ospiti",
    giri_total_n="54",
    giri_close=(
        "Il terzo giro è il più lungo: otto ospiti sparsi su cinque indirizzi, dal centro di Reggello fino a Donnini "
        "e San Giovenale. È quello che pesa di più sugli orari, ed è il primo che conviene affidare a un secondo mezzo."
    ),
    h_prezzo="Il prezzo",
    price_rows=[
        ("Ven 25 set — andata dai dodici indirizzi e rientro notturno, tre giri per verso", "€ 1.480,00", "+ IVA 10%"),
        ("Sab 26 set — andata dai dodici indirizzi e rientro notturno, tre giri per verso", "€ 1.560,00", "+ IVA 10%"),
        ("Supplemento rientro oltre le 02:00, notte fra sabato e domenica", "€ 250,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente, 2 notti (25 e 26 settembre)", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 3.290,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 3.619,00.",
    price_note=(
        "Gli importi si riferiscono a <b>un mezzo</b>, quello che si vede nel programma qui sopra. Il preventivo per "
        "il secondo e l'eventuale terzo minibus ve lo mandiamo appena ci dite come volete procedere: vedete la prima nota."
    ),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per tutte e due le serate, carburante, pedaggi, parcheggi, assicurazione completa e i tre "
        "giri di raccolta e i tre di rientro in ciascuna delle due giornate. Reggello non ha zone a traffico limitato "
        "né permessi comunali per i bus turistici, quindi non ci sono oneri di accesso da aggiungere. Il conducente "
        "resta a disposizione in zona anche durante le ore di attesa fra l'andata e il rientro, senza che vi venga "
        "addebitato nulla per quel tempo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio del conducente per le notti del 25 e del 26 settembre, che restano a vostro carico: la "
        "prenotazione e il pagamento li curate voi direttamente. Il secondo e il terzo minibus, quotati a parte. "
        "Attesa oltre gli orari concordati, € 50,00 all'ora per mezzo. Giri aggiuntivi o modifiche al programma dopo "
        "la conferma, quotati su richiesta. Il supplemento per il rientro dopo le 02:00 della notte fra venerdì e "
        "sabato, che secondo il programma non si verifica e che quindi non abbiamo conteggiato."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 1.090,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 2.529,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Cinquantaquattro ospiti su un mezzo da 26 posti: questo è il punto da decidere.</b> Con un solo minibus "
         "servono tre giri per ogni spostamento, e le conseguenze si leggono negli orari qui sopra: venerdì i primi "
         "ospiti vengono presi alle 15:05, oltre due ore prima degli ultimi, e la notte fra sabato e domenica "
         "l'ultimo gruppo lascia la festa alle 02:55 e arriva a casa verso le 03:45. Con <b>due minibus</b> i primi "
         "due giri viaggiano in parallelo e resta un solo giro di coda: la raccolta dura poco più di un'ora e il "
         "rientro si chiude intorno alle 02:00. Con <b>tre minibus</b> tutti partono e rientrano "
         "insieme, l'ultimo ospite è a casa verso le 01:50 e il supplemento per il rientro oltre le 02:00 non è più "
         "dovuto. La nostra raccomandazione, per 54 persone su due serate, sono tre mezzi il sabato e almeno due il "
         "venerdì; il preventivo per i mezzi in più ve lo mandiamo appena ci dite come volete procedere."),
        ("<b>Dove il minibus può arrivare davvero.</b> Diversi dei vostri indirizzi sono poderi sulle colline di "
         "Reggello, su strade strette, a volte bianche e senza spazio di manovra. Un mezzo di 7,64 metri arriva "
         "molto più in su di un autobus, ma non a ogni cancello. Ci serve il punto esatto sulla mappa di tutti e "
         "dodici: facciamo un sopralluogo e vi diciamo quali fermate reggono il minibus e per quali conviene "
         "concordare un punto di ritrovo sulla strada asfaltata. Meglio saperlo adesso che alle undici di sera, "
         "con gli ospiti in abito lungo."),
        ("<b>Via Bonsi 47.</b> Ci servono due cose dalla struttura: dove scendono e salgono gli ospiti — con lo "
         "spazio per fermare e girare un mezzo di quasi otto metri — e dove il minibus può sostare durante la festa, "
         "cinque ore il venerdì e nove e mezza il sabato. Se non c'è posto il conducente si sposta in un parcheggio "
         "vicino, ma dobbiamo saperlo prima."),
        ("<b>Il rientro della notte fra sabato e domenica.</b> L'orario che ci avete dato è l'01:00. Con un mezzo "
         "solo l'ultimo giro parte alle 02:55 e il supplemento previsto per il rientro oltre le 02:00, € 250,00 per "
         "mezzo, è a preventivo. Con tre mezzi il rientro si chiude prima delle 02:00 e il supplemento sparisce. "
         "La notte fra venerdì e sabato invece si chiude verso l'01:45 e non comporta alcun supplemento."),
        ("<b>Vitto e alloggio del conducente.</b> Le due notti del 25 e del 26 settembre sono a vostro carico e le "
         "prenotate e pagate voi direttamente: basta una camera singola in zona, con la cena. Servono davvero: "
         "Reggello dista circa 90 km dalla nostra base e ogni giornata si chiude fra l'una e le quattro del mattino, "
         "quindi rientrare a casa sforerebbe i tempi di riposo del conducente. Il consiglio che diamo sempre è di "
         "sistemarlo nella stessa struttura dei vostri ospiti."),
        ("<b>Gli ospiti per indirizzo.</b> I numeri che ci avete mandato fanno 54 e li abbiamo presi alla lettera. "
         "Ai matrimoni cambiano sempre: vi chiediamo la lista definitiva, fermata per fermata, dieci giorni prima. "
         "La sera del servizio ci serve un vostro referente con il telefono acceso — non gli sposi — a cui il "
         "conducente possa chiedere di chi manca prima di chiudere le porte."),
        ("<b>Gli orari che ci avete indicato.</b> Abbiamo letto le 18:00 di venerdì e le 15:30 di sabato come l'ora "
         "entro cui gli ospiti devono essere in Via Bonsi, e da lì abbiamo calcolato tutto a ritroso. Se sono invece "
         "l'ora della cerimonia, ditecelo e spostiamo i giri."),
        ("<b>Per confermare ci servono</b> il numero definitivo degli ospiti per ciascun indirizzo, il punto sulla "
         "mappa dei dodici indirizzi e di Via Bonsi 47, un recapito telefonico o WhatsApp del vostro referente sul "
         "posto, i vostri dati di fatturazione e la vostra decisione sul numero di mezzi."),
        ("<b>Disponibilità e cancellazione.</b> Mancano diciassette giorni al primo servizio e siamo nel pieno della "
         "stagione dei matrimoni: il nostro minibus è libero e lo teniamo per tutta la validità del preventivo, ma i "
         "mezzi aggiuntivi vanno bloccati subito. La prenotazione diventa definitiva alla ricezione "
         "dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene "
         "trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il "
         "100%. Alla data di oggi la prenotazione ricade già nella fascia da 30 a 10 giorni, e dal 15 settembre "
         "passa in quella degli ultimi 10 giorni. Preventivo valido fino al 15 settembre 2026."),
    ],
    closing=("Restiamo a disposizione per qualsiasi chiarimento e in attesa di un vostro riscontro.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    cliente_default="your wedding in Reggello",
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="Wedding shuttle · Reggello (FI), 12 pick-up addresses → Via Bonsi 47  ·  25-26 September 2026",
    meta="Prepared for %s  ·  8 September 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "One minibus with the same driver on both evenings, collecting your guests from the twelve addresses "
        "and taking them home again at the end of the night."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "Those 7.64 m are why this vehicle works in Reggello: it stays under eight metres and reaches places a "
        "full-size coach cannot, on the narrow roads climbing to the farmhouses and in the village streets. "
        "<b>Your guests, however, are 54 and the vehicle seats 26:</b> one minibus cannot carry them in a single "
        "movement. The price below is for one vehicle and the programme is built on three collection runs; "
        "the first note sets out in full what that means and how it changes with two or three minibuses."
    ),
    h_servizio="The service",
    svc_head=["Date", "Service", "Vehicle engaged"],
    svc=[
        ("Fri 25 Sep",
         "<b>Outward — from the twelve addresses to Via Bonsi 47.</b> Three consecutive collection runs, worked "
         "backwards from your 18:00 deadline: the first run leaves around 15:05 and reaches Via Bonsi at 15:45, "
         "the second leaves at 15:55 and arrives at 16:45, the third leaves at 16:55 and arrives at 17:55.",
         "approx. 15:00 – 18:00"),
        ("Fri 25 Sep",
         "<b>Return — from Via Bonsi 47 to the twelve addresses.</b> First departure at 23:00 with the Pietrapiana "
         "group, back at Via Bonsi around 23:50; second departure at 23:55, back around 00:50; third and last "
         "departure at 00:55, last guest home around 01:45.",
         "approx. 23:00 – 01:45"),
        ("Sat 26 Sep",
         "<b>Outward — from the twelve addresses to Via Bonsi 47.</b> The same three runs, worked backwards from "
         "the 15:30 deadline: first run at 12:45 arriving 13:25, second at 13:35 arriving 14:25, third at 14:35 "
         "arriving 15:25.",
         "approx. 12:40 – 15:30"),
        ("Sun 27 Sep",
         "<b>Return — from Via Bonsi 47 to the twelve addresses.</b> First departure at 01:00, back at Via Bonsi "
         "around 01:50; second departure at 01:55, back around 02:50; third and last departure at 02:55, "
         "last guest home around 03:45.",
         "approx. 01:00 – 03:45"),
    ],
    h_giri="The three collection runs",
    giri_intro=(
        "We have grouped the twelve addresses by area, so that each run stays compact and the largest party travels "
        "together. The guests on each run leave and return together, always at the same time."
    ),
    giri_head=["Run", "Address", "Guests"],
    giri=[
        ("<b>1 · Pietrapiana</b><br/><font size=7.4 color='#6B6B6B'>24 guests · 3 stops</font>", [
            ("Via Casalino 66, Loc. Pietrapiana", "14"),
            ("Hotel Archimede, Ponte di Casalino 68", "7"),
            ("Località Rovai 26, Pietrapiana", "3"),
        ]),
        ("<b>2 · La Romola and the farmhouses</b><br/><font size=7.4 color='#6B6B6B'>22 guests · 4 stops</font>", [
            ("Località Podere la Romola 78", "14"),
            ("Podere Houston / Giusti, Località Giusti 105", "4"),
            ("Loc. I Trebbiali 116", "2"),
            ("Via dei Glicini 14, Poggio ai Giubbiani", "2"),
        ]),
        ("<b>3 · Reggello, Donnini and San Giovenale</b><br/><font size=7.4 color='#6B6B6B'>8 guests · 5 stops</font>", [
            ("La Terrazza di Reggello, Via di Fano 6", "2"),
            ("Appartamento Olivella, Via Fornacina 32", "2"),
            ("Località S. Giovenale 55", "2"),
            ("Le Siepi, Via Filippo Turati, Montanino 16", "1"),
            ("Villa Pitiana Hotel, Donnini", "1"),
        ]),
    ],
    giri_total="Total guests",
    giri_total_n="54",
    giri_close=(
        "The third run is the longest: eight guests scattered over five addresses, from the centre of Reggello out "
        "to Donnini and San Giovenale. It is the one that weighs most on the timings, and the first that is worth "
        "handing to a second vehicle."
    ),
    h_prezzo="The price",
    price_rows=[
        ("Fri 25 Sep — outward from the twelve addresses and night return, three runs each way", "€ 1,480.00", "+ VAT 10%"),
        ("Sat 26 Sep — outward from the twelve addresses and night return, three runs each way", "€ 1,560.00", "+ VAT 10%"),
        ("Supplement for the return beyond 02:00, night of Saturday to Sunday", "€ 250.00", "+ VAT 10%"),
        ("Driver's board and lodging, 2 nights (25 and 26 September)", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 3,290.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 3,619.00.",
    price_note=(
        "These amounts are for <b>one vehicle</b>, the one shown in the programme above. We will send you the "
        "quotation for a second and, if you wish, a third minibus as soon as you tell us how you would like to "
        "proceed: please see the first note."
    ),
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver on both evenings, fuel, tolls, parking, full insurance, and the three collection runs "
        "and three return runs on each of the two days. Reggello has no restricted traffic zone and no municipal "
        "coach permit, so there are no access charges to add. The driver also stays available in the area during "
        "the waiting hours between the outward and the return runs, at no charge to you for that time."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's board and lodging for the nights of 25 and 26 September, which remain at your charge: you "
        "book and pay for them directly. The second and third minibus, quoted separately. Waiting beyond the agreed "
        "times, € 50.00 per hour per vehicle. Additional runs or changes to the programme after confirmation, quoted "
        "on request. The supplement for a return after 02:00 on the night of Friday to Saturday, which on this "
        "programme does not arise and which we have therefore not charged."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 1,090.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 2,529.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Fifty-four guests in a 26-seat vehicle: this is the decision to take.</b> With a single minibus every "
         "movement needs three runs, and the consequences are there to read in the timings above: on Friday the "
         "first guests are collected at 15:05, more than two hours before the last ones, and on Saturday night the "
         "last group leaves the party at 02:55 and reaches home around 03:45. With <b>two minibuses</b> the first "
         "two runs travel in parallel and only one trailing run is left: collection is concentrated into little "
         "more than an hour and the return closes around 02:00. With <b>three minibuses</b> everyone leaves and "
         "returns together, the last guest is home around 01:50 and the supplement for the return beyond 02:00 no "
         "longer applies. Our recommendation, for 54 people over two evenings, is three vehicles on the Saturday "
         "and at least two on the Friday; we will quote the extra vehicles as soon as you tell us how to proceed."),
        ("<b>Where the minibus can actually reach.</b> Several of your addresses are farmhouses in the Reggello "
         "hills, on narrow roads, sometimes unmade and with no room to turn. A 7.64 m vehicle gets far higher up "
         "than a coach, but not to every gate. We need the exact map location of all twelve: we will drive the "
         "roads and tell you which stops the minibus can take and where a meeting point on the surfaced road works "
         "better. Far better to know now than at eleven at night, with guests in long dresses."),
        ("<b>Via Bonsi 47.</b> We need two things from the venue: where guests get on and off — with the room to "
         "stop and turn a vehicle of nearly eight metres — and where the minibus can wait during the party, five "
         "hours on the Friday and nine and a half on the Saturday. If there is no space the driver moves to a "
         "nearby car park, but we need to know beforehand."),
        ("<b>The return on Saturday night.</b> The time you gave us is 01:00. With one vehicle the last run leaves "
         "at 02:55 and the supplement for a return beyond 02:00, € 250.00 per vehicle, is included in this "
         "quotation. With three vehicles the return closes before 02:00 and the supplement disappears. The Friday "
         "night, by contrast, closes around 01:45 and carries no supplement at all."),
        ("<b>The driver's board and lodging.</b> The two nights of 25 and 26 September are at your charge and you "
         "book and pay for them directly: a single room in the area, with dinner, is all that is needed. They are "
         "genuinely necessary: Reggello is about 90 km from our base and each day closes between one and four in the "
         "morning, so driving home would breach the driver's rest periods. Our usual advice is to put him up at "
         "the same property as your guests."),
        ("<b>Guests per address.</b> The numbers you sent us add up to 54 and we have taken them at face value. "
         "At weddings they always change: we ask for the final list, stop by stop, ten days beforehand. On the night "
         "we also need a contact of yours with their phone on — not the couple — whom the driver can ask about "
         "anyone missing before closing the doors."),
        ("<b>The times you gave us.</b> We have read the 18:00 on Friday and the 15:30 on Saturday as the time by "
         "which guests must be at Via Bonsi, and worked everything backwards from there. If they are instead the "
         "time of the ceremony or of the reception drinks, tell us and we will shift the runs accordingly."),
        ("<b>To confirm we need</b> the map locations, the final guest numbers per address, a mobile or WhatsApp "
         "contact for your person on the ground, your invoicing details and your decision on the number of vehicles."),
        ("<b>Availability and cancellation.</b> There are seventeen days to the first service and we are in the "
         "middle of the wedding season: our minibus is free today and we hold it for the validity of this quotation, "
         "but additional vehicles need securing as soon as possible. The booking becomes firm on receipt of the "
         "deposit. Cancellation is free of charge more than 60 days before the service; from 60 "
         "to 30 days the deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, "
         "100%. As of today the booking already falls in the 30-to-10-day band, and from 15 September it moves "
         "into the last-10-days band. Quotation valid until 15 September 2026."),
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
        "note": ParagraphStyle("note", alignment=TA_JUSTIFY, spaceAfter=5,
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


def tabella_giri(L, S, usable):
    """I tre giri di raccolta: l'etichetta del giro copre le sue fermate."""
    cols = [52 * mm, usable - 52 * mm - 18 * mm, 18 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["giri_head"]]]
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), CREAM),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (2, 0), (2, -1), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    r = 1
    for label, fermate in L["giri"]:
        primo = r
        for i, (indirizzo, pax) in enumerate(fermate):
            data.append([
                Paragraph(label, S["cellsm"]) if i == 0 else Paragraph("", S["cellsm"]),
                Paragraph(indirizzo, S["cellsm"]),
                Paragraph(pax, S["cellsm"]),
            ])
            r += 1
        cmds.append(("SPAN", (0, primo), (0, r - 1)))
        cmds.append(("LINEBELOW", (0, r - 1), (-1, r - 1), 0.5, RULE))
        cmds.append(("TOPPADDING", (0, primo), (-1, primo), 8))
        cmds.append(("BOTTOMPADDING", (0, r - 1), (-1, r - 1), 8))
    data.append([Paragraph("<b>%s</b>" % L["giri_total"], S["cellsm"]),
                 Paragraph("", S["cellsm"]),
                 Paragraph("<b>%s</b>" % L["giri_total_n"], S["cellsm"])])
    cmds.append(("SPAN", (0, r), (1, r)))
    cmds.append(("LINEABOVE", (0, r), (-1, r), 0.9, GREEN))
    cmds.append(("BACKGROUND", (0, r), (-1, r), CREAM))
    t = Table(data, colWidths=cols, repeatRows=1)
    t.setStyle(TableStyle(cmds))
    return t


def build(lang, cliente, out):
    L = IT if lang == "it" else EN
    S = styles()
    cliente = cliente or L["cliente_default"]
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
    cols = [23 * mm, usable - 23 * mm - 27 * mm, 27 * mm]
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

    # --- giri di raccolta
    F.append(Paragraph(L["h_giri"], S["h2"]))
    F.append(Paragraph(L["giri_intro"], S["body"]))
    F.append(tabella_giri(L, S, usable))
    F.append(Spacer(1, 7))
    F.append(Paragraph(L["giri_close"], S["body"]))

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
        Paragraph(L["price_note"], S["small"]),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE,
        "GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25-26_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

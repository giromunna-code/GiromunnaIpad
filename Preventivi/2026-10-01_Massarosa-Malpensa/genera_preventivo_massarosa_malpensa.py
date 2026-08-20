#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il trasferimento Massarosa (LU) -> Milano Malpensa
del 1 ottobre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_massarosa_malpensa.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_massarosa_malpensa.py --lingua en --cliente "Client Name"

Senza --cliente il preventivo esce senza intestatario: la richiesta e' arrivata
senza nome, quindi va rigenerato appena si conosce.
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

RIF = "GM-2026-1001-MM"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Trasferimento privato Massarosa (LU) → Aeroporto di Milano Malpensa  ·  giovedì 1° ottobre 2026, partenza ore 02:00  ·  16 passeggeri",
    meta="Preparato per %s  ·  20 agosto 2026  ·  Rif. " + RIF,
    meta_nocliente="Preparato il 20 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo di 16 persone, con un solo conducente per l'intero trasferimento.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 16 passeggeri a bordo restano dieci posti liberi, e su un viaggio notturno di oltre tre ore "
        "questo conta: ciascuno ha la propria fila e i sedili reclinabili si usano davvero, così si arriva "
        "a Malpensa avendo dormito qualcosa. I dieci posti liberi sono anche appoggio per i bagagli a mano, "
        "oltre al vano bagagli che accoglie senza forzare sedici valigie da stiva. I 7,64 metri del mezzo, "
        "infine, entrano dove un autobus gran turismo non passa: un punto non scontato se il ritrovo a "
        "Massarosa è in una via stretta o in collina."
    ),
    h_servizio="Il servizio",
    svc_head=["Orario", "Percorso", "Distanza"],
    svc=[
        ("01:45",
         "<b>L'autista è sul posto a Massarosa (LU).</b> Arriva con quindici minuti di anticipo sull'orario "
         "concordato, così il carico dei bagagli non mangia tempo alla partenza. Attende a motore spento nel "
         "punto di ritrovo che avremo stabilito insieme.",
         "—"),
        ("02:00",
         "<b>Partenza da Massarosa (LU) → Aeroporto di Milano Malpensa.</b> Itinerario A11 da Massarosa, "
         "A12 in direzione Genova, quindi A26 dei Trafori verso Gravellona Toce e uscita diretta per "
         "l'aeroporto. A quest'ora la strada è libera e questo percorso evita del tutto il nodo di Milano.",
         "circa 330 km<br/>3 h 30"),
        ("03:45",
         "<b>Sosta di ristoro facoltativa</b>, una ventina di minuti in area di servizio sulla A26. "
         "La facciamo solo se il gruppo la desidera: senza sosta si arriva prima.",
         "—"),
        ("05:30",
         "<b>Arrivo a Malpensa</b>, direttamente al terminal della vostra partenza. Verso le 05:50 se avete "
         "fatto la sosta. Il conducente scarica i bagagli e vi accompagna fino all'ingresso dell'aerostazione.",
         "—"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Gio 1 ott — Massarosa (LU) → Aeroporto di Milano Malpensa, circa 330 km", "€ 1.550,00", "+ IVA 10%"),
        ("Maggiorazione per la partenza notturna delle 02:00", "€ 250,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente — nessun pernottamento necessario",
         "<i>nessun onere</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.800,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.980,00.",
    perhead="Sono circa € 124,00 a persona, pedaggi e bagagli compresi.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, oneri di accesso e di sosta all'aeroporto di "
        "Malpensa per lo scarico dei passeggeri, assicurazione completa, movimentazione dei bagagli e la sosta "
        "di ristoro lungo il percorso. Controlliamo il vostro volo la sera prima della partenza: se la compagnia "
        "ne anticipa l'orario, ve lo segnaliamo e spostiamo la partenza di conseguenza, senza costi aggiuntivi. "
        "Sull'orario di partenza da Massarosa vi lasciamo una tolleranza di 30 minuti."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Attesa oltre gli orari qui concordati e oltre la tolleranza dei 30 minuti, € 50,00 all'ora per mezzo. "
        "Soste aggiuntive, punti di carico ulteriori o modifiche all'itinerario, quotati su richiesta. "
        "Il viaggio di ritorno da Malpensa, che quotiamo volentieri a parte. Pasti, bevande e consumazioni. "
        "Vitto e alloggio del conducente: su questo servizio non serve alcun pernottamento e non vi addebitiamo "
        "nulla a questo titolo — su programmi di più giorni resterebbe invece a vostro carico."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 594,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.386,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>L'orario del volo, che è la domanda vera.</b> Partendo alle 02:00 siete al terminal verso le 05:30: "
         "è l'orario giusto per un volo dalle 07:30 in poi, con i banchi appena aperti e le code ancora corte. "
         "Se però il vostro volo parte più tardi — mettiamo dalle 10:00 — con la partenza alle 02:00 il gruppo "
         "si troverebbe a passare quattro o cinque ore in aerostazione dopo una notte in bianco. In quel caso "
         "conviene partire da Massarosa verso le 05:00 ed essere a Malpensa verso le 08:45, traffico del mattino "
         "compreso: tutti dormono nel proprio letto e, non essendoci più la partenza notturna, "
         "<b>il prezzo scende a € 1.550,00 + IVA, cioè € 1.705,00</b>. Se invece il volo parte prima delle 07:00, "
         "anticipiamo la partenza all'01:30. Mandateci numero e orario del volo e vi confermiamo l'orario giusto: "
         "l'abbiamo quotato alle 02:00 perché così ce lo avete chiesto, ma su questo vale la pena ragionare."),
        ("<b>Quale terminal di Malpensa.</b> Il Terminal 1 e il Terminal 2 distano circa quattro chilometri e si "
         "raggiungono da svincoli diversi: sbagliarlo alle cinque del mattino significa mezz'ora persa e un "
         "gruppo che corre. La quasi totalità delle compagnie parte dal Terminal 1, mentre il Terminal 2 ne serve "
         "poche, tutte low cost. Ci basta il numero del volo e lo verifichiamo noi."),
        ("<b>Il punto esatto di carico a Massarosa.</b> Il CAP 55054 copre l'intero comune, e sono due mondi "
         "diversi: la piana — Bozzano, Quiesa, Stiava, Piano di Conca, Piano del Quercione — dove si arriva "
         "ovunque senza problemi, e i paesi in collina come Corsanico, Pieve a Elici, Montigiano e Gualdo, dove "
         "le strade si stringono e i punti in cui girare sono pochi. Il nostro mezzo da 7,64 metri ci arriva dove "
         "un gran turismo si ferma, ma alle due di notte e al buio è meglio saperlo prima: mandateci l'indirizzo "
         "esatto, o ancora meglio una posizione WhatsApp, e verifichiamo per tempo il punto di salita e lo spazio "
         "di manovra. Se il posto è scomodo vi proponiamo noi un ritrovo a poche centinaia di metri, comodo per "
         "tutti. A quell'ora l'autista attende a motore spento e non suona il clacson: il gruppo si trova al "
         "punto concordato, e i vicini continuano a dormire."),
        ("<b>I bagagli.</b> Sedici persone in partenza per un volo vogliono dire, verosimilmente, sedici valigie "
         "da stiva più i bagagli a mano: il vano del Beluga le prende senza forzare e i dieci posti liberi in "
         "cabina fanno da appoggio per il resto. Segnalateci in anticipo sci, sacche da golf, passeggini, "
         "strumenti musicali o altri colli fuori misura. Si caricano lo stesso, ma è molto meglio saperlo prima "
         "che scoprirlo al buio con l'orario che stringe."),
        ("<b>Il conducente, e perché non vi costa alcun pernottamento.</b> Su questo servizio non serve che "
         "l'autista dorma fuori e non vi addebitiamo nulla per il suo vitto e alloggio. Parte dalla nostra base "
         "verso l'01:00 avendo osservato il riposo previsto, vi accompagna a Malpensa, effettua a destinazione la "
         "pausa obbligatoria di 45 minuti e rientra in Toscana. Tutto il servizio sta dentro i limiti di guida e "
         "riposo di legge con un solo conducente: nessun secondo autista, nessuna notte a vostro carico."),
        ("<b>La maggiorazione notturna.</b> I € 250,00 sono la nostra tariffa per il lavoro nelle ore notturne, "
         "la stessa che applichiamo ai rientri dopo le due: qui la giornata del conducente comincia all'01:00. "
         "Non è un supplemento sull'aeroporto né sui chilometri, che sono già compresi nel prezzo del "
         "trasferimento. Come detto sopra, spostando la partenza alle 05:00 o più tardi non è dovuta."),
        ("<b>Che cosa copre il prezzo, e il ritorno.</b> Il prezzo copre il viaggio del mezzo per intero: circa "
         "660 chilometri fra l'andata con voi a bordo e il rientro a vuoto in Toscana. È la ragione per cui un "
         "trasferimento di sola andata costa più di quanto suggerirebbero i chilometri che percorrete voi. "
         "Se vi serve anche il ritorno da Malpensa, ditecelo: quotati insieme, andata e ritorno costano meno di "
         "due sole andate. Lo stesso vale se il gruppo rientra su Pisa o su Firenze."),
        ("<b>Per confermare ci servono</b> l'indirizzo esatto del punto di carico a Massarosa, numero e orario "
         "del volo con il terminal di partenza, il numero definitivo dei passeggeri, un recapito telefonico o "
         "WhatsApp della persona che viaggia con il gruppo e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero per la notte fra il 30 settembre e "
         "il 1° ottobre e lo teniamo a vostra disposizione per tutta la validità di questo preventivo; la "
         "prenotazione diventa definitiva alla ricezione dell'acconto. La cancellazione è gratuita oltre 60 "
         "giorni prima del servizio; da 60 a 30 giorni viene trattenuto l'acconto; da 30 a 10 giorni viene "
         "addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. Mancando oggi 42 giorni al servizio, "
         "questa prenotazione ricade nella fascia da 60 a 30 giorni, e dal 1° settembre passerà in quella da 30 "
         "a 10. Preventivo valido fino al 3 settembre 2026."),
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
    subtitle="Private transfer Massarosa (LU) → Milan Malpensa Airport  ·  Thursday 1 October 2026, departure 02:00  ·  16 passengers",
    meta="Prepared for %s  ·  20 August 2026  ·  Ref. " + RIF,
    meta_nocliente="Prepared on 20 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of 16, with a single driver for the whole transfer.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 16 passengers on board ten seats stay free, and on a night run of more than three hours that "
        "matters: everyone gets a row to themselves and the reclining seats actually get used, so you reach "
        "Malpensa having had some sleep. Those ten free seats also take the overflow of hand luggage, on top of "
        "a hold that swallows sixteen checked suitcases without a squeeze. And at 7.64 m the minibus goes where "
        "a full-size coach cannot — no small thing if the pick-up point in Massarosa is on a narrow street or up "
        "in the hills."
    ),
    h_servizio="The service",
    svc_head=["Time", "Route", "Distance"],
    svc=[
        ("01:45",
         "<b>The driver is on site in Massarosa (LU).</b> He arrives fifteen minutes ahead of the agreed time, so "
         "loading the luggage does not eat into the departure. He waits with the engine off at the meeting point "
         "we will have agreed together.",
         "—"),
        ("02:00",
         "<b>Departure from Massarosa (LU) → Milan Malpensa Airport.</b> Routing: A11 from Massarosa, A12 towards "
         "Genoa, then the A26 towards Gravellona Toce and the direct airport exit. At this hour the road is clear, "
         "and this route avoids the Milan ring entirely.",
         "approx. 330 km<br/>3 h 30"),
        ("03:45",
         "<b>Optional comfort stop</b>, around twenty minutes at a service area on the A26. "
         "We make it only if the group wants it: without the stop you arrive earlier.",
         "—"),
        ("05:30",
         "<b>Arrival at Malpensa</b>, directly at your departure terminal — around 05:50 if you took the stop. "
         "The driver unloads the luggage and walks you to the terminal entrance.",
         "—"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Thu 1 Oct — Massarosa (LU) → Milan Malpensa Airport, about 330 km", "€ 1,550.00", "+ VAT 10%"),
        ("Night departure supplement, 02:00 start", "€ 250.00", "+ VAT 10%"),
        ("Driver's board and lodging — no overnight stay required",
         "<i>no charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,800.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,980.00.",
    perhead="That is about € 124.00 per person, tolls and luggage included.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, Malpensa airport access and set-down charges, full insurance, "
        "luggage handling and the comfort stop along the way. We check your flight the evening before departure: "
        "if the airline brings the time forward we tell you and move the pick-up accordingly, at no extra cost. "
        "On the departure time from Massarosa we allow you 30 minutes of grace."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "Waiting beyond the times agreed here and beyond the 30-minute grace, € 50.00 per hour per vehicle. "
        "Additional stops, further pick-up points or changes to the itinerary, quoted on request. The return "
        "journey from Malpensa, which we are glad to quote separately. Meals, drinks and refreshments. "
        "The driver's board and lodging: this service requires no overnight stay and we charge you nothing on "
        "that count — on a multi-day programme it would instead remain at your charge."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 594.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,386.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Your flight time, which is the real question.</b> Leaving at 02:00 puts you at the terminal around "
         "05:30: the right time for a flight from 07:30 onwards, with the desks just open and the queues still "
         "short. If your flight leaves later, though — say from 10:00 — a 02:00 departure would leave the group "
         "with four or five hours in the terminal after a sleepless night. In that case it is better to leave "
         "Massarosa around 05:00 and reach Malpensa around 08:45, morning traffic included: everyone sleeps in "
         "their own bed and, with no night departure, <b>the price drops to € 1,550.00 + VAT, that is "
         "€ 1,705.00</b>. If instead the flight leaves before 07:00, we bring the departure forward to 01:30. "
         "Send us the flight number and time and we will confirm the right schedule: we have quoted 02:00 "
         "because that is what you asked for, but it is worth a thought."),
        ("<b>Which Malpensa terminal.</b> Terminal 1 and Terminal 2 are about four kilometres apart and are "
         "reached from different exits: getting it wrong at five in the morning means half an hour lost and a "
         "group at a run. Almost every airline departs from Terminal 1, while Terminal 2 serves only a handful, "
         "all low cost. Just send us the flight number and we will check it."),
        ("<b>The exact pick-up point in Massarosa.</b> Postcode 55054 covers the whole municipality, and it is "
         "two different worlds: the plain — Bozzano, Quiesa, Stiava, Piano di Conca, Piano del Quercione — where "
         "we reach anywhere without difficulty, and the hill villages such as Corsanico, Pieve a Elici, "
         "Montigiano and Gualdo, where the roads narrow and there are few places to turn. Our 7.64 m vehicle gets "
         "where a full-size coach stops, but at two in the morning and in the dark it is better known in advance: "
         "send us the exact address, or better still a WhatsApp location, and we will check the boarding point "
         "and the manoeuvring space in good time. If the spot is awkward we will suggest a meeting point a few "
         "hundred metres away that suits everyone. At that hour the driver waits with the engine off and does not "
         "sound the horn: the group gathers at the agreed point, and the neighbours sleep on."),
        ("<b>Luggage.</b> Sixteen people leaving on a flight most likely means sixteen checked suitcases plus "
         "hand luggage: the Beluga's hold takes them without a squeeze and the ten free seats in the cabin absorb "
         "the rest. Do tell us in advance about skis, golf bags, pushchairs, musical instruments or other "
         "oversized items. They travel all the same, but far better known beforehand than discovered in the dark "
         "with the clock running."),
        ("<b>The driver, and why no overnight stay costs you anything.</b> This service does not require the "
         "driver to stay away, and we charge you nothing for his board and lodging. He leaves our base around "
         "01:00 having taken the required rest, takes you to Malpensa, makes his compulsory 45-minute break on "
         "arrival and drives back to Tuscany. The whole service stays inside the statutory driving and rest "
         "limits with a single driver: no second driver, no nights at your charge."),
        ("<b>The night supplement.</b> The € 250.00 is our rate for work in the night hours, the same one we "
         "apply to returns after two in the morning: here the driver's day begins at 01:00. It is not an airport "
         "surcharge nor a mileage one — those are already inside the transfer price. As noted above, moving the "
         "departure to 05:00 or later means it is not due."),
        ("<b>What the price covers, and the return.</b> The price covers the vehicle's whole journey: about 660 "
         "kilometres between the run with you on board and the empty return to Tuscany. That is why a one-way "
         "transfer costs more than the kilometres you yourselves travel would suggest. If you also need the "
         "return from Malpensa, tell us: quoted together, out and back cost less than two separate one-ways. "
         "The same applies if the group flies back into Pisa or Florence."),
        ("<b>To confirm we need</b> the exact pick-up address in Massarosa, the flight number and time with the "
         "departure terminal, the final passenger count, a mobile or WhatsApp contact for the person travelling "
         "with the group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free for the night of 30 September to "
         "1 October and we hold it for you for the whole validity of this quotation; the booking becomes firm on "
         "receipt of the deposit. Cancellation is free of charge more than 60 days before the service; from 60 to "
         "30 days the deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, "
         "100%. With 42 days to the service today, this booking falls in the 60-to-30-day band, and from "
         "1 September it moves into the 30-to-10 band. Quotation valid until 3 September 2026."),
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
    # la richiesta e' arrivata senza nome: senza --cliente l'intestatario si omette
    meta = (L["meta"] % cliente) if cliente else L["meta_nocliente"]
    F.append(Paragraph(meta, S["meta"]))

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
    cols = [17 * mm, usable - 17 * mm - 30 * mm, 30 * mm]
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Transfer_Massarosa_Malpensa_1_ottobre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

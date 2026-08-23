#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per Firenze e i trasferimenti da e per l'aeroporto
del 29 maggio 2028.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_firenze.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_firenze.py --lingua en --cliente "Client Name"
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

RIF = "GM-2028-0529-TW"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Firenze e trasferimenti da e per l'aeroporto  ·  lunedì 29 maggio 2028  ·  fino a 26 passeggeri",
    meta="Preparato per %s  ·  23 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo, fino a 26 persone, con lo stesso conducente per tutti i servizi.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Il gruppo ci sta: 26 posti passeggeri sono esattamente le vostre 26 persone. Proprio perché il conto "
        "torna al posto esatto, due cose vanno guardate insieme prima di confermare — il numero definitivo dei "
        "passeggeri e la quantità di bagagli. Le trovate come prima nota, in fondo. I 7,64 metri del mezzo sono "
        "invece un vantaggio da sfruttare: entrano dove un autobus gran turismo non arriva, dai piazzali delle "
        "ville fuori Firenze alle strade strette delle colline."
    ),
    h_servizio="Il servizio",
    servizio_intro=(
        "La vostra richiesta è arrivata senza il dettaglio del programma: Firenze, fino a 26 persone, prelievi "
        "in aeroporto. Qui sotto abbiamo messo l'ipotesi più probabile, così avete subito un prezzo di "
        "riferimento su cui ragionare. Ogni voce è quotata per conto suo: appena ci dite il programma vero "
        "rifacciamo il preventivo su misura, e quello che non vi serve esce semplicemente dal conto."
    ),
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Lun 29 mag 2028",
         "<b>Aeroporto di Pisa (PSA) → Firenze.</b> Accoglienza in sala arrivi con il cartello GiroMunna, "
         "carico dei bagagli e trasferimento fino al vostro indirizzo di Firenze. Circa 85 km, un'ora e un "
         "quarto di percorrenza. Il volo lo seguiamo noi e l'autista si regola sull'atterraggio effettivo.",
         "circa 3 ore"),
        ("Data da definire",
         "<b>Giornata a disposizione, Firenze e dintorni.</b> Mezzo e conducente a vostra disposizione per otto "
         "ore e fino a 120 km: le ville e i borghi intorno a Firenze, una cantina del Chianti, il mare, oppure "
         "semplicemente gli spostamenti del gruppo in città e nell'immediata periferia. L'itinerario lo fissiamo "
         "insieme a voi.",
         "8 ore, max 120 km"),
        ("Data da definire",
         "<b>Firenze → Aeroporto di Pisa (PSA).</b> Trasferimento di ritorno alla ripartenza del gruppo, con "
         "l'orario calcolato sul vostro volo: in alta stagione partiamo da Firenze tre ore e mezza prima "
         "del decollo.",
         "circa 3 ore"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Trasferimento aeroporto di Pisa → Firenze, all'arrivo", "€ 700,00", "+ IVA 10%"),
        ("Giornata a disposizione a Firenze e dintorni, 8 ore fino a 120 km", "€ 990,00", "+ IVA 10%"),
        ("Trasferimento Firenze → aeroporto di Pisa, alla ripartenza", "€ 700,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente, se il programma richiederà pernottamenti",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 2.390,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 2.629,00.",
    perhead=("Sono circa € 101,00 a persona con il mezzo pieno. Le tre voci vivono ognuna per conto suo: "
             "se ne serve solo una parte, il totale scende di conseguenza."),
    h_extra="Altre voci, se servono",
    extra_rows=[
        ("Mezza giornata a disposizione, 4 ore fino a 60 km", "€ 620,00", "+ IVA 10%"),
        ("Trasferimento fra l'aeroporto di Firenze (FLR) e Firenze, per tratta", "€ 420,00", "+ IVA 10%"),
        ("Giornata nel Chianti con partenza da Firenze, 10 ore fino a 200 km", "€ 1.250,00", "+ IVA 10%"),
        ("Prelievo aggiuntivo a Pisa, per un secondo volo in arrivo", "€ 700,00", "+ IVA 10%"),
        ("Attesa oltre gli orari concordati, all'ora e per mezzo", "€ 50,00", "+ IVA 10%"),
        ("Rientro dopo le 02:00, per mezzo", "€ 250,00", "+ IVA 10%"),
        ("Permesso di accesso di un bus turistico al centro di Firenze, se necessario",
         "circa € 350,00", "al costo"),
    ],
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggi — compreso il parcheggio bus "
        "dell'aeroporto di Pisa —, assicurazione completa, movimentazione dei bagagli, monitoraggio del volo e "
        "accoglienza in sala arrivi con il cartello GiroMunna. All'arrivo l'autista attende senza costi "
        "aggiuntivi fino a 90 minuti dall'orario di atterraggio effettivo, per quanto il volo arrivi in ritardo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio del conducente, se il programma dovesse richiedere pernottamenti: restano a vostro "
        "carico e li prenotate e pagate voi direttamente. Ingressi, pasti, guide e mance. Attesa oltre gli orari "
        "concordati, € 50,00 all'ora per mezzo. Soste aggiuntive o modifiche all'itinerario, quotate su "
        "richiesta. Rientro dopo le 02:00, € 250,00. L'eventuale permesso di accesso di un bus turistico al "
        "centro storico di Firenze, circa € 350,00, e il permesso comunale di Siena per i bus turistici, circa "
        "€ 160,00, se il programma dovesse toccare Siena."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 790,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 1.839,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>I bagagli sono il punto da guardare per primo.</b> Il Beluga ha 26 posti passeggeri: il vostro "
         "gruppo ci sta, ma esatto esatto, senza un posto libero. Ne discendono due cose pratiche. La prima: se "
         "con voi viaggiano un accompagnatore, una guida o un ventisettesimo passeggero, il mezzo non basta più "
         "e serve un secondo minibus, da organizzare per tempo. La seconda: 26 persone in arrivo dal Regno "
         "Unito significano fino a 26 valigie da stiva più i bagagli a mano, e il vano di un mezzo da 7,64 m "
         "porta comodamente una ventina di valigie grandi, non trenta. Diteci quante valigie grandi ci sono "
         "davvero e se ci sono passeggini, sacche da golf o attrezzatura: se i numeri sono al limite mettiamo "
         "in conto un mezzo di appoggio per i soli bagagli. È una cosa che si risolve in due minuti adesso e "
         "che in aeroporto, con il gruppo che aspetta, non si risolve affatto."),
        ("<b>Firenze, la zona a traffico limitato e il punto di discesa.</b> Il centro storico di Firenze è a "
         "traffico limitato e l'ingresso di un bus turistico richiede un permesso a parte, circa € 350,00. "
         "Nella maggior parte dei casi non serve: si carica e si scarica nei punti autorizzati — l'area della "
         "Fortezza da Basso e Piazzale Montelungo per gli hotel della zona stazione, i lungarni, Piazza della "
         "Libertà — e da lì l'albergo è a pochi minuti a piedi. Con 26 valigie al seguito, però, quei pochi "
         "minuti a piedi pesano. Mandateci l'indirizzo esatto dove alloggiate: vi diciamo dove si ferma il "
         "mezzo e, se il caso lo merita, mettiamo a preventivo il permesso e vi portiamo davanti alla porta."),
        ("<b>Da quale aeroporto arrivate.</b> Abbiamo quotato Pisa (PSA), lo scalo più usato dai voli dal Regno "
         "Unito: 85 km da Firenze, un'ora e un quarto. Se invece atterrate a Firenze (FLR) il trasferimento "
         "costa € 420,00 netti a tratta invece di € 700,00, e il totale scende di conseguenza. Da Bologna o da "
         "Roma il prezzo sale: ditecelo e vi mandiamo la cifra esatta."),
        ("<b>«Airport pickups too»: quanti prelievi servono.</b> Un gruppo di 26 persone raramente arriva su un "
         "unico volo. Se siete tutti sullo stesso, il trasferimento qui quotato basta. Se invece arrivate "
         "spezzati su due o tre voli, ogni corsa è un servizio a sé: mandateci gli orari e vi diciamo se "
         "conviene tenere il mezzo in attesa in aeroporto fra un volo e l'altro (€ 50,00 all'ora) oppure fare "
         "due viaggi separati. Con i numeri davanti la scelta è immediata."),
        ("<b>Se il volo ritarda.</b> Il volo lo monitoriamo noi e l'autista si regola sull'atterraggio "
         "effettivo: l'attesa è gratuita fino a 90 minuti da quando l'aereo tocca terra, senza che dobbiate "
         "avvisarci di niente. Ci serve solo il numero del volo. Per la ripartenza, in alta stagione partiamo "
         "da Firenze tre ore e mezza prima del decollo; se avete in mente un orario diverso, ne parliamo."),
        ("<b>La data.</b> Abbiamo preso alla lettera lunedì 29 maggio 2028, che è il lunedì di festa di fine "
         "maggio nel Regno Unito e cade in piena alta stagione fiorentina. Se l'anno o il giorno fossero "
         "diversi da quello che ci avete scritto, ditecelo e rifacciamo il preventivo in giornata. Se invece "
         "sono giusti, muoversi con questo anticipo è un vantaggio vero: su quelle date i mezzi di questa "
         "dimensione si esauriscono con largo anticipo."),
        ("<b>Il prezzo a due anni di distanza.</b> Gli importi qui sopra sono costruiti sulle nostre tariffe di "
         "oggi e mancano circa venti mesi al servizio. Alla conferma definitiva li riconfermiamo e ci "
         "riserviamo il solo adeguamento dei costi vivi — carburante, pedaggi, contratto degli autisti — che "
         "comunichiamo con largo anticipo e che negli anni è sempre stato contenuto. Se per voi è importante "
         "avere un prezzo bloccato fin d'ora, chiedetecelo in fase di conferma e ne parliamo."),
        ("<b>Vitto e alloggio del conducente.</b> Con il programma qui ipotizzato non serve alcun pernottamento: "
         "dalla nostra base a Firenze ci sono una cinquantina di chilometri e il conducente rientra ogni sera. "
         "Se il programma diventasse di più giorni con base lontana, o con rientri sistematici a notte fonda, "
         "il pernottamento diventerebbe necessario: in quel caso resta a vostro carico e lo prenotate e pagate "
         "voi direttamente — basta una camera singola con la cena, e la soluzione più comoda per tutti è "
         "sistemare il conducente nella stessa struttura del gruppo. Ve lo segnaliamo prima, mai a cose fatte."),
        ("<b>Per farvi un preventivo su misura ci servono</b> il numero definitivo dei passeggeri e delle "
         "valigie, quanti giorni di servizio e in quali date, le tappe o almeno l'idea di massima del "
         "programma, l'indirizzo di Firenze dove alloggiate, l'aeroporto con numero e orario dei voli in arrivo "
         "e in partenza, e un recapito WhatsApp della persona che viaggia con il gruppo. Rispondete anche solo "
         "per punti: rifacciamo il preventivo e ve lo rimandiamo."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero per quelle date e lo teniamo a "
         "vostra disposizione per tutta la validità di questo preventivo; la prenotazione diventa definitiva "
         "alla ricezione dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio, quindi "
         "fino al 30 marzo 2028, e in quel caso l'acconto vi viene restituito per intero; da 60 a 30 giorni "
         "viene trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 "
         "giorni il 100%. Preventivo valido fino al 22 settembre 2026."),
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
    subtitle="Florence and airport transfers  ·  Monday 29 May 2028  ·  up to 26 passengers",
    meta="Prepared for %s  ·  23 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of up to 26, with the same driver across every service.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "The group fits: 26 passenger seats are exactly your 26 people. Precisely because the count comes out "
        "to the last seat, two things are worth settling together before you confirm — the final passenger "
        "number and how much luggage there is. They are the first note at the end of this quotation. "
        "The 7.64 m length, on the other hand, is an advantage worth using: the minibus reaches places a "
        "full-size coach cannot, from the courtyards of the villas outside Florence to the narrow hill roads."
    ),
    h_servizio="The service",
    servizio_intro=(
        "Your enquiry reached us without the detail of the programme: Florence, up to 26 people, airport "
        "pickups. Below is the most likely shape of it, so that you have a reference price to work from "
        "straight away. Each item is priced on its own: as soon as you tell us the real programme we rebuild "
        "the quotation around it, and whatever you do not need simply drops out of the total."
    ),
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Mon 29 May 2028",
         "<b>Pisa Airport (PSA) → Florence.</b> The driver welcomes you in the arrivals hall with the GiroMunna "
         "sign, loads the luggage and takes you to your address in Florence. About 85 km, an hour and a quarter "
         "on the road. We track the flight ourselves and the driver works to the actual landing time.",
         "approx. 3 hours"),
        ("Date to be set",
         "<b>Day at disposal, Florence and surroundings.</b> Vehicle and driver at your disposal for eight hours "
         "and up to 120 km: the villas and villages around Florence, a Chianti winery, the coast, or simply "
         "moving the group around the city and its outskirts. We set the itinerary together with you.",
         "8 hours, max 120 km"),
        ("Date to be set",
         "<b>Florence → Pisa Airport (PSA).</b> Return transfer when the group flies home, timed against your "
         "flight: in high season we leave Florence three and a half hours before departure.",
         "approx. 3 hours"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Transfer Pisa airport → Florence, on arrival", "€ 700.00", "+ VAT 10%"),
        ("Day at disposal in Florence and surroundings, 8 hours up to 120 km", "€ 990.00", "+ VAT 10%"),
        ("Transfer Florence → Pisa airport, on departure", "€ 700.00", "+ VAT 10%"),
        ("Driver's board and lodging, should the programme require overnight stays",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 2,390.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 2,629.00.",
    perhead=("That is about € 101.00 per person with the minibus full. Each of the three items stands on its "
             "own: if you only need part of them, the total comes down accordingly."),
    h_extra="Other items, should you need them",
    extra_rows=[
        ("Half day at disposal, 4 hours up to 60 km", "€ 620.00", "+ VAT 10%"),
        ("Transfer between Florence airport (FLR) and Florence, each way", "€ 420.00", "+ VAT 10%"),
        ("Day in Chianti starting from Florence, 10 hours up to 200 km", "€ 1,250.00", "+ VAT 10%"),
        ("Additional pickup at Pisa, for a second arriving flight", "€ 700.00", "+ VAT 10%"),
        ("Waiting beyond the agreed times, per hour per vehicle", "€ 50.00", "+ VAT 10%"),
        ("Return after 02:00, per vehicle", "€ 250.00", "+ VAT 10%"),
        ("Tourist coach access permit for the centre of Florence, if needed", "approx. € 350.00", "at cost"),
    ],
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, parking — including the coach parking fee at Pisa airport —, "
        "full insurance, luggage handling, flight monitoring and the welcome in the arrivals hall with the "
        "GiroMunna sign. On arrival the driver waits at no extra cost for up to 90 minutes from the actual "
        "landing time, however late the flight comes in."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's board and lodging, should the programme require overnight stays: they remain at your "
        "charge and you book and pay for them directly. Entrance fees, meals, guides and gratuities. Waiting "
        "beyond the agreed times, € 50.00 per hour per vehicle. Additional stops or changes to the itinerary, "
        "quoted on request. Return after 02:00, € 250.00. Any tourist coach access permit for the historic "
        "centre of Florence, about € 350.00, and the Siena municipal coach permit, about € 160.00, should the "
        "programme take in Siena."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 790.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 1,839.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>Luggage is the first thing to look at.</b> The Beluga has 26 passenger seats: your group fits, but "
         "exactly, with no seat to spare. Two practical consequences follow. First: if a tour leader, a guide "
         "or a twenty-seventh passenger travels with you, one minibus is no longer enough and a second one has "
         "to be arranged in good time. Second: 26 people arriving from the UK means up to 26 hold suitcases "
         "plus hand luggage, and the hold of a 7.64 m vehicle comfortably takes around twenty large cases, not "
         "thirty. Tell us how many large cases there really are, and whether there are pushchairs, golf bags or "
         "equipment: if the numbers are tight we will plan a support vehicle for the luggage alone. It is a "
         "thing that takes two minutes to settle now and cannot be settled at all at the airport, with the "
         "group standing there waiting."),
        ("<b>Florence, the restricted traffic zone and the drop-off point.</b> The historic centre of Florence "
         "is a restricted traffic zone, and taking a tourist coach into it requires a separate permit, about "
         "€ 350.00. In most cases it is not needed: we load and unload at the authorised points — the Fortezza "
         "da Basso and Piazzale Montelungo area for hotels near the station, the Lungarni, Piazza della Libertà "
         "— and the hotel is a few minutes' walk from there. With 26 suitcases in tow, though, those few "
         "minutes count. Send us the exact address where you are staying: we will tell you where the vehicle "
         "stops and, if the case warrants it, we will put the permit in the quotation and bring you to the "
         "door."),
        ("<b>Which airport you fly into.</b> We have quoted Pisa (PSA), the airport most used by flights from "
         "the UK: 85 km from Florence, an hour and a quarter. If you land at Florence (FLR) instead, the "
         "transfer costs € 420.00 net each way rather than € 700.00, and the total comes down accordingly. "
         "From Bologna or Rome the price goes up: tell us and we will send you the exact figure."),
        ("<b>&ldquo;Airport pickups too&rdquo;: how many pickups.</b> A group of 26 rarely arrives on a single flight. If "
         "you are all on the same one, the transfer quoted here covers it. If you arrive split across two or "
         "three flights, each run is a service in its own right: send us the times and we will tell you whether "
         "it works out cheaper to hold the vehicle at the airport between flights (€ 50.00 per hour) or to make "
         "two separate journeys. With the numbers in front of us the choice is immediate."),
        ("<b>If the flight is delayed.</b> We monitor the flight ourselves and the driver works to the actual "
         "landing time: waiting is free for up to 90 minutes from the moment the aircraft touches down, with no "
         "need for you to let us know anything. All we need is the flight number. For the return, in high "
         "season we leave Florence three and a half hours before departure; if you have a different time in "
         "mind, let us talk it through."),
        ("<b>The date.</b> We have taken Monday 29 May 2028 at face value — the late May bank holiday Monday in "
         "the UK, falling in the middle of the Florentine high season. If the year or the day are not what you "
         "meant, tell us and we will redo the quotation the same day. If they are right, moving this far ahead "
         "is a genuine advantage: vehicles of this size sell out well in advance for those dates."),
        ("<b>The price two years out.</b> The amounts above are built on our current tariffs, and the service "
         "is some twenty months away. At final confirmation we reconfirm them, reserving only the adjustment "
         "of direct costs — fuel, tolls, drivers' pay agreement — which we communicate well in advance and "
         "which over the years has always been modest. If a price fixed from today matters to you, ask us at "
         "confirmation and we will discuss it."),
        ("<b>The driver's board and lodging.</b> The programme as set out here requires no overnight stay: "
         "Florence is about fifty kilometres from our base and the driver goes home each evening. Should the "
         "programme grow into several days with a distant base, or with returns regularly in the small hours, "
         "an overnight stay would become necessary: it then remains at your charge and you book and pay for it "
         "directly — a single room with dinner is all that is needed, and the easiest arrangement for everyone "
         "is to put the driver up at the same property as the group. We flag it beforehand, never after the "
         "fact."),
        ("<b>To build you a tailored quotation we need</b> the final number of passengers and suitcases, how "
         "many days of service and on which dates, the stops or at least the broad idea of the programme, the "
         "address in Florence where you are staying, the airport with the number and time of the arriving and "
         "departing flights, and a WhatsApp contact for the person travelling with the group. Bullet points are "
         "fine: we will redo the quotation and send it back to you."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free for those dates and we hold it "
         "for you for the whole validity of this quotation; the booking becomes firm on receipt of the deposit. "
         "Cancellation is free of charge more than 60 days before the service, so up to 30 March 2028, and the "
         "deposit is refunded in full; from 60 to 30 days the deposit is retained; from 30 to 10 days 50% of "
         "the price is charged; in the last 10 days, 100%. Quotation valid until 22 September 2026."),
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
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=9.6,
                             textColor=GREEN, leading=12.5, spaceBefore=10, spaceAfter=5),
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


def _importi(rows, cols, S, totale=None, vat_note=""):
    """Tabella a tre colonne: voce, importo, nota IVA. Con o senza riga di totale."""
    data = [[Paragraph(label, S["cellsm"]),
             Paragraph(amount, S["cellsm"]),
             Paragraph(vat, S["cellmut"])] for label, amount, vat in rows]
    style = [
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    if totale is not None:
        label, amount = totale
        data.append([Paragraph("<b>%s</b>" % label, S["cellsm"]),
                     Paragraph("<b>%s</b>" % amount, S["cellsm"]),
                     Paragraph(vat_note, S["cellmut"])])
        style += [
            ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
            ("LINEABOVE", (0, -1), (-1, -1), 0.9, GREEN),
            ("BACKGROUND", (0, -1), (-1, -1), CREAM),
        ]
    t = Table(data, colWidths=cols)
    t.setStyle(TableStyle(style))
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
    F.append(Paragraph(L["servizio_intro"], S["body"]))
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

    # --- prezzo (intestazione e tabella non si spezzano fra due pagine)
    pcols = [usable - 30 * mm - 20 * mm, 30 * mm, 20 * mm]
    pt = _importi(L["price_rows"], pcols, S,
                  totale=(L["price_total_label"], L["price_total"]), vat_note=L["vat_note"])
    # la lista va costruita prima: KeepTogether non tiene il riferimento
    # a una lista vuota passata alla costruzione.
    F.append(KeepTogether([
        Paragraph(L["h_prezzo"], S["h2"]),
        pt,
        Paragraph(L["grand"], S["grand"]),
        Paragraph(L["perhead"], S["small"]),
    ]))

    # --- altre voci a listino
    F.append(KeepTogether([
        Paragraph(L["h_extra"], S["h3"]),
        _importi(L["extra_rows"], pcols, S),
    ]))
    F.append(Spacer(1, 8))

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Tracey Williams")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Firenze_29_maggio_2028_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

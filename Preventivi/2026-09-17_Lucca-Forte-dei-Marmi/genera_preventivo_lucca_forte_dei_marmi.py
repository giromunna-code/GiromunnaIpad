#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la giornata Lucca - Forte dei Marmi - cantina - Lucca.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_lucca_forte_dei_marmi.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_lucca_forte_dei_marmi.py --lingua en --cliente "Client Name"

Senza --cliente il preventivo esce senza intestatario, che e' la forma giusta
finche' il cliente non ci dice come si chiama. Con --rif si aggiorna il
riferimento quando la data del servizio e' fissata.
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

# Provvisorio: la data del servizio non e' ancora fissata, quindi le quattro cifre
# sono quelle di emissione e le iniziali stanno per Lucca-Versilia. Quando arrivano
# data e nome del cliente si rigenera con --rif.
RIF = "GM-2026-0917-LV"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Giornata a disposizione  ·  Lucca · Forte dei Marmi · cantina · Lucca  ·  16-20 passeggeri",
    meta_con="Preparato per %s  ·  17 settembre 2026  ·  Rif. %s",
    meta_senza="Preparato il 17 settembre 2026  ·  Rif. %s",
    h_mezzo="Il mezzo",
    mezzo_intro=("Un minibus con conducente per il vostro gruppo, a vostra disposizione dal ritrovo "
                 "a Lucca fino al rientro della sera."),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 16 o 20 persone a bordo restano dai sei ai dieci posti liberi, che su una giornata intera "
        "si sentono. I 7,64 metri contano più della capienza su questo itinerario: il Beluga sta sotto gli "
        "otto metri e arriva ai piazzali della Versilia e alle strade di collina delle cantine dove un "
        "autobus gran turismo non entra."
    ),
    h_servizio="Il servizio",
    svc_head=["Orario", "Percorso", "Distanza"],
    svc=[
        ("09:00",
         "<b>Lucca → Forte dei Marmi.</b> Ritrovo al punto che ci indicate — se l'albergo è dentro le mura "
         "concordiamo il punto accessibile più vicino. Arrivo in Versilia verso le 09:45.",
         "38 km · 45 min"),
        ("09:45 – 13:00",
         "<b>Mattinata a Forte dei Marmi.</b> Mezzo e conducente restano a vostra disposizione: il pontile, "
         "il centro, il mercato del mercoledì, il lungomare. Gli spostamenti brevi in paese sono compresi.",
         "—"),
        ("13:00",
         "<b>Forte dei Marmi → il ristorante.</b> Vi portiamo dove avete prenotato: dentro Forte dei Marmi "
         "oppure a Pietrasanta, che è a un quarto d'ora ed è la scelta che facciamo più spesso.",
         "0 – 8 km · 15 min"),
        ("15:30",
         "<b>Ristorante → cantina.</b> Due direzioni possibili, entrambe comprese nel prezzo: le colline di "
         "Candia dei Colli Apuani sopra Massa, oppure le Colline Lucchesi e Montecarlo sulla via del rientro.",
         "25 – 45 km · 40 min"),
        ("16:15 – 18:30",
         "<b>Visita e degustazione.</b> Mezzo e conducente vi aspettano in cantina per tutta la durata "
         "della visita.",
         "—"),
        ("18:30",
         "<b>Cantina → Lucca.</b> Rientro al punto di partenza o all'albergo, con arrivo intorno alle 19:30.",
         "15 – 45 km · 30-50 min"),
    ],
    svc_close=("Il mezzo è impegnato per l'intera giornata, circa dalle 09:00 alle 19:30, sempre con lo "
               "stesso conducente. Orari e distanze sono stime stradali: li fissiamo sul programma "
               "definitivo appena ci date data, ristorante e cantina."),
    h_prezzo="Il prezzo",
    price_rows=[
        ("Giornata intera, 09:00 – 19:30 — Lucca → Forte dei Marmi → cantina → Lucca",
         "€ 1.050,00", "+ IVA 10%"),
        ("Vitto del conducente, il pranzo della giornata", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.050,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.155,00.",
    perhead=("Il prezzo è del mezzo, non a testa: € 57,75 a persona in venti, € 72,19 in sedici."),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi autostradali, parcheggi ordinari, "
        "assicurazione completa e tutti gli spostamenti brevi all'interno di Forte dei Marmi. "
        "Su questo itinerario non sono dovuti oneri di accesso: non si tocca l'aeroporto di Pisa, "
        "né il centro di Firenze, né Siena, quindi non c'è alcun permesso da pagare."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto del conducente, che resta a vostro carico. Pranzo del gruppo, visite, degustazioni, "
        "ingressi e mance in cantina. Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. "
        "Soste aggiuntive o modifiche all'itinerario, quotate su richiesta. Rientro dopo le 02:00, € 250,00."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 346,50", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 808,50", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>La data.</b> Nella vostra richiesta non c'è e senza data non possiamo tenere il mezzo: "
         "il Beluga è uno solo e va a prenotazioni. Il prezzo qui indicato vale per qualunque giorno "
         "dell'anno, quindi appena ci dite la data confermiamo la disponibilità e blocchiamo la giornata. "
         "Un'avvertenza sul periodo: nei fine settimana di luglio e agosto il traffico sulla costa "
         "versiliese è pesante e gli spostamenti si allungano di parecchio. Se avete margine di scelta, "
         "un giorno infrasettimanale è un'altra giornata."),
        ("<b>Sedici o venti, il prezzo non cambia.</b> Quello che vedete è il prezzo del mezzo, non "
         "una quota a testa: su 26 posti il vostro gruppo ci sta comodo in entrambi i casi e l'importo "
         "resta lo stesso. Il numero esatto serve comunque, perché ce lo chiede l'assicurazione e "
         "perché con venti persone i tempi di salita e discesa a ogni tappa si allungano un po'."),
        ("<b>Ristorante e cantina sono ancora da scegliere.</b> Li abbiamo tenuti aperti perché la vostra "
         "richiesta parla di «un posto lì vicino» senza nominarli. Per il pranzo: dentro Forte dei Marmi "
         "restate sul mare, mentre Pietrasanta è a un quarto d'ora e ha il centro storico più bello della "
         "zona. Per la cantina ci sono due strade. La prima è <b>Candia dei Colli Apuani</b>, sulle colline "
         "sopra Massa, a venti minuti dal mare: è la denominazione più vicina a Forte dei Marmi, con le "
         "Apuane alle spalle e il mare davanti — per esempio Podere Scurtarola o Aurelio Cima. La seconda "
         "sono le <b>Colline Lucchesi e Montecarlo</b>, che stanno sulla via del rientro verso Lucca — per "
         "esempio Fattoria Sardi, Tenuta di Valgiano o Fattoria del Buonamico a Montecarlo. Sono solo "
         "indicazioni nostre da verificare, non prenotazioni: la visita la fissate voi. In entrambi i casi "
         "il chilometraggio della giornata è simile e <b>il prezzo non cambia</b>."),
        ("<b>Se la cantina è a Candia, la strada è stretta.</b> L'ultimo tratto verso le colline di Massa è "
         "in salita, con tornanti e passaggi fra i muri: il nostro minibus da 7,64 m ci arriva, un autobus "
         "gran turismo no. Vi chiediamo comunque di farvi confermare dalla cantina il punto di discesa e lo "
         "spazio di manovra per un mezzo di questa lunghezza. Meglio chiarirlo adesso che davanti al cancello."),
        ("<b>Il punto di ritrovo a Lucca.</b> Il centro dentro le mura è zona a traffico limitato. "
         "Diteci l'indirizzo esatto dell'albergo o del punto di ritrovo: se è raggiungibile vi prendiamo "
         "lì, altrimenti vi indichiamo il punto accessibile più vicino, che a Lucca significa quasi sempre "
         "due minuti a piedi e non di più."),
        ("<b>Forte dei Marmi in alta stagione.</b> Da giugno a settembre l'accesso al centro e al lungomare "
         "è regolato e i pullman hanno stalli dedicati fuori dal paese. Restando sotto gli otto metri ci "
         "muoviamo con molta più libertà di un gran turismo, ma il piano traffico cambia di anno in anno: "
         "alla data confermata verifichiamo quello in vigore e vi diciamo esattamente dove scendete e dove "
         "vi riprendiamo."),
        ("<b>Quanto dura la giornata.</b> Così com'è, dal ritrovo delle 09:00 al rientro delle 19:30, il "
         "programma sta dentro i limiti di guida e di servizio del conducente con circa un'ora di margine, "
         "contando anche il viaggio del mezzo dalla nostra base e ritorno. Se volete rientrare a Lucca più "
         "tardi delle 20:30 — una cena in Versilia, per dire — si può fare, ma va deciso prima: si sposta "
         "avanti la partenza del mattino oppure si organizza il cambio del conducente. Improvvisarlo la "
         "sera stessa non è possibile."),
        ("<b>Il pranzo del conducente.</b> Resta a vostro carico e non lo mettiamo a preventivo. "
         "Non serve invece alcun pernottamento: la giornata finisce a Lucca e il conducente rientra alla "
         "base in serata. La soluzione più semplice, ed è quella che scelgono quasi tutti i nostri clienti, "
         "è aggiungere un coperto al vostro tavolo."),
        ("<b>Un'alternativa che vale la pena considerare.</b> Diverse cantine della zona servono il pranzo "
         "insieme alla degustazione. Accorpando le due tappe si toglie uno spostamento di mezzogiorno, si "
         "arriva in collina con più calma e resta tutto il pomeriggio libero sul mare. Se vi interessa "
         "ditecelo: il prezzo è lo stesso e vi rifacciamo il programma della giornata."),
        ("<b>Per confermare ci servono</b> la data, il numero definitivo dei passeggeri, l'indirizzo e "
         "l'orario del ritrovo a Lucca, il nome e l'indirizzo del ristorante e della cantina, un recapito "
         "telefonico o WhatsApp della persona che viaggia con il gruppo e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo si blocca alla ricezione dell'acconto, non prima. "
         "La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene trattenuto "
         "l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. "
         "Non essendo ancora fissata la data del servizio, la fascia applicabile la calcoliamo insieme "
         "appena la scegliete. Preventivo valido fino al 17 ottobre 2026."),
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
    subtitle="Full day at disposal  ·  Lucca · Forte dei Marmi · winery · Lucca  ·  16-20 passengers",
    meta_con="Prepared for %s  ·  17 September 2026  ·  Ref. %s",
    meta_senza="Prepared on 17 September 2026  ·  Ref. %s",
    h_mezzo="The vehicle",
    mezzo_intro=("One minibus with driver for your group, at your disposal from the pick-up in Lucca "
                 "to the evening return."),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 16 or 20 people on board, six to ten seats stay free — something you notice over a full day. "
        "On this itinerary the 7.64 m matter more than the capacity: the Beluga is under eight metres and "
        "reaches the Versilia seafront and the hill roads up to the wineries, where a full-size coach "
        "cannot go."
    ),
    h_servizio="The service",
    svc_head=["Time", "Route", "Distance"],
    svc=[
        ("09:00",
         "<b>Lucca → Forte dei Marmi.</b> Pick-up wherever you tell us — if your hotel is inside the walls "
         "we agree the nearest accessible point. Arrival in Versilia around 09:45.",
         "38 km · 45 min"),
        ("09:45 – 13:00",
         "<b>Morning in Forte dei Marmi.</b> Vehicle and driver stay at your disposal: the pier, the town "
         "centre, the Wednesday market, the seafront. Short hops within the town are included.",
         "—"),
        ("13:00",
         "<b>Forte dei Marmi → the restaurant.</b> We take you wherever you have booked: within Forte dei "
         "Marmi, or in Pietrasanta, fifteen minutes away and the choice we most often suggest.",
         "0 – 8 km · 15 min"),
        ("15:30",
         "<b>Restaurant → winery.</b> Two possible directions, both covered by this price: the Candia dei "
         "Colli Apuani hills above Massa, or the Colline Lucchesi and Montecarlo on the way back.",
         "25 – 45 km · 40 min"),
        ("16:15 – 18:30",
         "<b>Visit and tasting.</b> Vehicle and driver wait for you at the winery for the whole visit.",
         "—"),
        ("18:30",
         "<b>Winery → Lucca.</b> Back to your starting point or your hotel, arriving around 19:30.",
         "15 – 45 km · 30-50 min"),
    ],
    svc_close=("The vehicle is engaged for the whole day, roughly 09:00 to 19:30, with the same driver "
               "throughout. Times and distances are road estimates: we set them against your final "
               "programme once you give us the date, restaurant and winery."),
    h_prezzo="The price",
    price_rows=[
        ("Full day, 09:00 – 19:30 — Lucca → Forte dei Marmi → winery → Lucca",
         "€ 1,050.00", "+ VAT 10%"),
        ("Driver's meal, lunch on the day", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,050.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,155.00.",
    perhead=("The price is for the vehicle, not per head: € 57.75 each at twenty, € 72.19 at sixteen."),
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, fuel, motorway tolls, ordinary parking, full insurance and "
        "every short transfer within Forte dei Marmi. No access charges apply on this itinerary: it touches "
        "neither Pisa airport, nor the centre of Florence, nor Siena, so there is no permit to pay for."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meal, which remains at your charge. The group's lunch, winery visits, tastings, "
        "entrance fees and gratuities. Waiting beyond the times set out here, € 50.00 per hour per vehicle. "
        "Additional stops or changes to the itinerary, quoted on request. Return after 02:00, € 250.00."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 346.50", "VAT included"),
        ("Balance, within 5 days of the service", "€ 808.50", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The date.</b> Your enquiry does not give one, and without a date we cannot hold the vehicle: "
         "there is only one Beluga and it goes by booking order. The price quoted here applies to any day "
         "of the year, so as soon as you tell us the date we confirm availability and block the day. "
         "One word about timing: on July and August weekends the traffic along the Versilia coast is heavy "
         "and every transfer stretches considerably. If you have any choice in the matter, a weekday is a "
         "different day altogether."),
        ("<b>Sixteen or twenty, the price is the same.</b> What you see is the price of the vehicle, "
         "not a per-head share: on 26 seats your group travels comfortably either way and the amount "
         "does not move. We still need the exact number, because our insurance asks for it and because "
         "with twenty people boarding and alighting at each stop takes a little longer."),
        ("<b>Restaurant and winery are still open.</b> We have left them so because your enquiry speaks of "
         "\"a nearby spot\" without naming either. For lunch: staying inside Forte dei Marmi keeps you by "
         "the sea, while Pietrasanta is fifteen minutes away and has the finest historic centre in the "
         "area. For the winery there are two directions. The first is <b>Candia dei Colli Apuani</b>, on "
         "the hills above Massa, twenty minutes from the coast: the closest denomination to Forte dei "
         "Marmi, with the Apuan Alps behind and the sea in front — Podere Scurtarola or Aurelio Cima, for "
         "instance. The second is the <b>Colline Lucchesi and Montecarlo</b>, which sit on the way back to "
         "Lucca — Fattoria Sardi, Tenuta di Valgiano or Fattoria del Buonamico at Montecarlo, for instance. "
         "These are our suggestions to look into, not bookings: the visit is yours to arrange. Either way "
         "the day's mileage is similar and <b>the price does not change</b>."),
        ("<b>If the winery is at Candia, the road is narrow.</b> The final stretch up the Massa hills "
         "climbs through hairpins and between stone walls: our 7.64 m minibus gets there, a full-size "
         "coach does not. Even so, please have the winery confirm the drop-off point and the manoeuvring "
         "space for a vehicle of this length. Far better settled now than at the gate."),
        ("<b>The pick-up point in Lucca.</b> The centre inside the walls is a restricted traffic zone. "
         "Send us the exact address of your hotel or meeting point: if we can reach it we collect you "
         "there, otherwise we will name the nearest accessible point, which in Lucca almost always means "
         "a two-minute walk and no more."),
        ("<b>Forte dei Marmi in high season.</b> From June to September access to the centre and the "
         "seafront is regulated and coaches have designated bays outside the town. Being under eight "
         "metres we move far more freely than a full-size coach, but the traffic scheme changes from year "
         "to year: once the date is fixed we check the one in force and tell you exactly where you get off "
         "and where we pick you up."),
        ("<b>How long the day runs.</b> As it stands, from the 09:00 pick-up to the 19:30 return, the "
         "programme sits inside the driver's legal driving and duty limits with about an hour to spare, "
         "counting the vehicle's run from our base and back. If you want to return to Lucca later than "
         "20:30 — dinner in Versilia, say — it can be done, but it has to be decided beforehand: either "
         "the morning start moves later, or we arrange a change of driver. It cannot be improvised on "
         "the evening itself."),
        ("<b>The driver's lunch.</b> It remains at your charge and we do not put a figure on it. "
         "No overnight stay is needed: the day ends in Lucca and the driver returns to base that evening. "
         "The simplest arrangement, and the one nearly all our clients choose, is one more place at your "
         "table."),
        ("<b>An alternative worth considering.</b> Several wineries in the area serve lunch alongside the "
         "tasting. Merging the two stops removes a midday transfer, gets you up into the hills at an "
         "easier pace and leaves the whole afternoon free by the sea. Tell us if it appeals: the price is "
         "the same and we will redraw the day for you."),
        ("<b>To confirm we need</b> the date, the final passenger count, the address and time of the "
         "pick-up in Lucca, the name and address of the restaurant and the winery, a mobile or WhatsApp "
         "contact for the person travelling with the group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is blocked on receipt of the deposit, not "
         "before. Cancellation is free of charge more than 60 days before the service; from 60 to 30 days "
         "the deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, "
         "100%. As the service date is not yet fixed, we will work out the applicable band together as "
         "soon as you choose it. Quotation valid until 17 October 2026."),
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


def build(lang, cliente, out, rif=RIF):
    L = IT if lang == "it" else EN
    S = styles()
    w, _ = A4
    usable = w - 2 * MARGIN

    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=TOP, bottomMargin=BOTTOM,
                          title="GiroMunna %s %s" % (L["title"], rif),
                          author="GiroMunna")
    frame = Frame(MARGIN, BOTTOM, usable, A4[1] - TOP - BOTTOM, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=make_chrome(L))])

    F = []
    F.append(Paragraph(L["title"], S["title"]))
    F.append(Paragraph(L["subtitle"], S["subtitle"]))
    # Finche' non sappiamo come si chiama il cliente, il preventivo esce senza
    # intestatario invece che con un segnaposto.
    meta = (L["meta_con"] % (cliente, rif)) if cliente else (L["meta_senza"] % rif)
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
    cols = [25 * mm, usable - 25 * mm - 27 * mm, 27 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for orario, desc, dist in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % orario, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
            Paragraph(dist, S["cellmut"]),
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
    F.append(Spacer(1, 5))
    F.append(Paragraph(L["svc_close"], S["body"]))

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="",
                    help="Intestatario del preventivo. Vuoto finche' non lo sappiamo.")
    ap.add_argument("--rif", dest="rif", default=RIF,
                    help="Riferimento GM-AAAA-MMGG-XX, da aggiornare con la data del servizio.")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Lucca_Forte_dei_Marmi_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name, a.rif))

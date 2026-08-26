#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il wine tour in Toscana del 13-18 settembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_tuscany_wine_tour.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_tuscany_wine_tour.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0913-BI"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Wine tour in Toscana, Valdarno · Chianti · Colline Pisane · Versilia  ·  13-18 settembre 2026",
    meta="Preparato per %s  ·  8 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro="Un minibus per il vostro gruppo di 21 persone, con lo stesso conducente per tutta la durata del programma.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 21 ospiti a bordo restano cinque posti liberi: un margine reale di comodità su un tour di più giorni. "
        "I 7,64 metri del mezzo raggiungono i piazzali di tutte le cantine in programma, comprese le strade strette "
        "del Chianti dove un autobus gran turismo non arriva."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Dom 13 set",
         "<b>Aeroporto di Firenze (FLR) → Ruffino, Tenuta Poggio Casciano (Bagno a Ripoli) → Borgo Iesolana (Bucine).</b> "
         "Ritrovo alle 10:15 in aeroporto, l'autista vi accoglie in sala arrivi con il cartello GiroMunna. "
         "Circa 28 km fino alla cantina, arrivo verso le 11:00. Mezzo e conducente restano a vostra disposizione per "
         "tutta la visita; ripartenza alle 16:30 e arrivo a Borgo Iesolana verso le 17:30, 55 km.",
         "circa 10:00 – 17:30"),
        ("Lun 14 set",
         "<b>Borgo Iesolana → Baldetti (Loc. Pietraia, Cortona) → Il Borro (San Giustino Valdarno) → Borgo Iesolana.</b> "
         "Partenza alle 10:00, 60 km fino a Baldetti. Alle 14:00 si prosegue verso Il Borro, 55 km attraverso il Valdarno. "
         "Rientro alle 17:30, arrivo alla struttura verso le 18:00. Giornata intera a disposizione.",
         "circa 10:00 – 18:00"),
        ("Mar 15 set",
         "<b>Borgo Iesolana → Badia a Coltibuono (Gaiole in Chianti) → Borgo Iesolana.</b> "
         "Partenza alle 16:00 sui 40 km di strade del Chianti, arrivo verso le 17:00. Mezzo e conducente a vostra "
         "disposizione per tutta la serata; rientro alle 21:00, alla struttura verso le 22:00.",
         "circa 16:00 – 22:00"),
        ("Mer 16 set",
         "<b>Borgo Iesolana → Tenuta di Montefoscoli (Palaia) → Badia di Morrona (Terricciola) → hotel a Forte dei Marmi.</b> "
         "Partenza alle 10:15, 135 km verso le colline pisane con arrivo intorno alle 12:05. Alle 15:00 il breve "
         "trasferimento di 12 km fino a Badia di Morrona; alle 17:00 si prosegue per la Versilia, 90 km, con arrivo "
         "in hotel verso le 18:20. La giornata più lunga del programma, circa 250 km.",
         "circa 10:00 – 18:30"),
        ("Gio 17 set",
         "<b>Nessun servizio richiesto.</b> Il mezzo rientra alla base e non viene tenuto in stand-by: "
         "questa giornata non comporta alcun addebito.",
         "—"),
        ("Ven 18 set",
         "<b>Hotel a Forte dei Marmi → Aeroporto di Firenze (FLR).</b> "
         "Partenza alle 12:30, circa 110 km, arrivo alle partenze di Firenze verso le 13:50.",
         "circa 12:15 – 14:00"),
    ],
    h_prezzo="Il prezzo",
    price_rows=[
        ("Dom 13 set — aeroporto di Firenze → Ruffino → Borgo Iesolana", "€ 950,00", "+ IVA 10%"),
        ("Lun 14 set — giornata a disposizione: Baldetti, Il Borro, rientro", "€ 980,00", "+ IVA 10%"),
        ("Mar 15 set — serata a disposizione: Badia a Coltibuono, rientro", "€ 680,00", "+ IVA 10%"),
        ("Mer 16 set — Borgo Iesolana → Montefoscoli → Badia di Morrona → Forte dei Marmi", "€ 1.250,00", "+ IVA 10%"),
        ("Ven 18 set — Forte dei Marmi → aeroporto di Firenze", "€ 780,00", "+ IVA 10%"),
        ("Vitto e alloggio del conducente, 3 notti (13, 14 e 15 settembre)",
         "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 4.640,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 5.104,00.",
    perhead="Sono circa € 243,00 a persona per l'intero programma.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente, carburante, pedaggi autostradali, parcheggi, assicurazione completa, movimentazione "
        "bagagli e monitoraggio del volo del 13 settembre. Non sono dovuti altri oneri di accesso: l'aeroporto di "
        "Firenze non comporta alcun onere e nessuna delle cantine in programma si trova in zona a traffico "
        "limitato. Il 13 settembre l'autista attende senza costi aggiuntivi fino a 90 minuti dall'orario di "
        "atterraggio effettivo, per quanto il volo arrivi in ritardo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Vitto e alloggio del conducente per le notti del 13, 14 e 15 settembre, che restano a vostro carico: la "
        "prenotazione e il pagamento li curate voi direttamente. Ingressi, degustazioni, pasti, guide e mance in "
        "cantina. Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. Soste aggiuntive o modifiche "
        "all'itinerario, quotate su richiesta. Rientro alla struttura dopo le 02:00, € 250,00. L'eventuale ingresso "
        "di un bus turistico nel centro di Firenze, che comporterebbe un permesso a parte."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 1.530,00", "IVA inclusa"),
        ("Saldo, entro 5 giorni dal servizio", "€ 3.574,00", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Vitto e alloggio del conducente.</b> Il programma richiede che il conducente pernotti in zona nelle "
         "notti del 13, 14 e 15 settembre: Borgo Iesolana dista circa 120 km dalla nostra base e il rientro "
         "giornaliero porterebbe la giornata di guida oltre i limiti consentiti. Le tre notti sono a vostro carico "
         "e le prenotate e pagate voi direttamente: basta una camera singola vicino alla struttura, con la cena. "
         "Molti dei nostri clienti sistemano il conducente nella stessa struttura del gruppo, che è la soluzione "
         "più comoda per tutti. Fateci sapere dove alloggerà prima della partenza."),
        ("<b>Bagagli del 16 settembre.</b> È il punto da guardare con più attenzione: si lascia Borgo Iesolana "
         "con tutti i bagagli a bordo, si visitano due cantine e si arriva in hotel a Forte dei Marmi solo la sera. "
         "Il vano del Beluga porta senza problemi una ventina di valigie normali per 21 ospiti, ma segnalateci in "
         "anticipo eventuali colli fuori misura, sacche da golf o scatole di vino acquistate lungo il percorso, "
         "così organizziamo il carico o aggiungiamo un mezzo di supporto."),
        ("<b>Accessibilità di Badia a Coltibuono.</b> L'ultimo tratto di strada è stretto e tortuoso. "
         "Il nostro minibus da 7,64 m ci arriva, mentre un autobus gran turismo no. Vi chiediamo comunque di farvi "
         "confermare dalla cantina il punto di discesa e lo spazio di manovra per un mezzo di questa lunghezza: "
         "molto meglio chiarirlo ora che la sera stessa."),
        ("<b>Il volo in partenza del 18 settembre.</b> Partendo alle 12:30 da Forte dei Marmi si arriva alle "
         "partenze di Firenze verso le 13:50. Va bene per un volo dalle 16:00 in poi; se il vostro parte prima, "
         "conviene anticipare la partenza dall'hotel e ce lo potete chiedere senza costi aggiuntivi. "
         "Mandateci numero e orario del volo e confermiamo gli orari su quello."),
        ("<b>Il volo in arrivo del 13 settembre.</b> Ci servono numero del volo e orario di atterraggio. "
         "Il ritrovo indicato alle 10:15 lo abbiamo preso alla lettera come orario di incontro in sala arrivi: "
         "se invece è l'orario di atterraggio, spostiamo tutto di circa un'ora e vi aggiorniamo il programma."),
        ("<b>Quale tenuta Ruffino.</b> Abbiamo quotato la Tenuta Poggio Casciano di Bagno a Ripoli, la sede "
         "dell'ospitalità Ruffino. Ruffino riceve anche in altre proprietà: confermateci quale, perché "
         "cambierebbe il percorso e il prezzo del 13 settembre."),
        ("<b>Il 17 settembre.</b> Non è previsto alcun servizio e non addebitiamo nulla. Se i vostri ospiti "
         "volessero il mezzo a disposizione in Versilia, possiamo tenerlo: mezza giornata € 450,00 + IVA, "
         "giornata intera € 700,00 + IVA. Ditecelo entro la conferma, così teniamo libero il conducente."),
        ("<b>Per confermare ci servono</b> il numero definitivo dei passeggeri, l'indirizzo esatto dell'hotel a "
         "Forte dei Marmi, gli orari dei due voli, un recapito telefonico o WhatsApp della persona che viaggia con "
         "il gruppo e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> Il mezzo è al momento libero e lo teniamo a vostra "
         "disposizione per tutta la validità del preventivo; la prenotazione diventa definitiva alla ricezione "
         "dell'acconto. La cancellazione è gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene "
         "trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni il 100%. "
         "Mancando oggi 36 giorni al primo servizio, questa prenotazione ricade nella fascia da 60 a 30 giorni, "
         "e dal 14 agosto passerà in quella da 30 a 10. Preventivo valido fino al 22 agosto 2026."),
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
    subtitle="Tuscany wine tour, Valdarno · Chianti · Pisan Hills · Versilia  ·  13-18 September 2026",
    meta="Prepared for %s  ·  8 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro="One minibus for your group of 21, with the same driver throughout the programme.",
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 21 guests on board five seats stay free — real breathing room on a multi-day tour. "
        "At 7.64 m the minibus reaches the courtyard of every winery on the programme, including the narrow "
        "Chianti lanes a full-size coach cannot manage."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sun 13 Sep",
         "<b>Florence Airport (FLR) → Ruffino, Tenuta Poggio Casciano (Bagno a Ripoli) → Borgo Iesolana (Bucine).</b> "
         "Meeting point 10:15 at the airport, where the driver welcomes you in the arrivals hall with the GiroMunna sign. "
         "About 28 km to the winery, arriving around 11:00. Vehicle and driver stay at your disposal throughout the visit; "
         "departure at 16:30 and arrival at Borgo Iesolana around 17:30, 55 km.",
         "approx. 10:00 – 17:30"),
        ("Mon 14 Sep",
         "<b>Borgo Iesolana → Baldetti (Loc. Pietraia, Cortona) → Il Borro (San Giustino Valdarno) → Borgo Iesolana.</b> "
         "Departure at 10:00, 60 km to Baldetti. At 14:00 on to Il Borro, 55 km across the Valdarno. "
         "Return at 17:30, back at the property around 18:00. Full day at disposal.",
         "approx. 10:00 – 18:00"),
        ("Tue 15 Sep",
         "<b>Borgo Iesolana → Badia a Coltibuono (Gaiole in Chianti) → Borgo Iesolana.</b> "
         "Departure at 16:00 along 40 km of Chianti roads, arriving around 17:00. Vehicle and driver at your disposal "
         "for the whole evening; return at 21:00, back at the property around 22:00.",
         "approx. 16:00 – 22:00"),
        ("Wed 16 Sep",
         "<b>Borgo Iesolana → Tenuta di Montefoscoli (Palaia) → Badia di Morrona (Terricciola) → hotel in Forte dei Marmi.</b> "
         "Departure at 10:15, 135 km to the Pisan hills arriving around 12:05. At 15:00 the short 12 km hop to "
         "Badia di Morrona; at 17:00 on to Versilia, 90 km, reaching the hotel around 18:20. "
         "The longest day of the programme, about 250 km.",
         "approx. 10:00 – 18:30"),
        ("Thu 17 Sep",
         "<b>No service requested.</b> The vehicle returns to base and is not held on stand-by: "
         "nothing is charged for this day.",
         "—"),
        ("Fri 18 Sep",
         "<b>Hotel in Forte dei Marmi → Florence Airport (FLR).</b> "
         "Departure at 12:30, about 110 km, reaching Florence departures around 13:50.",
         "approx. 12:15 – 14:00"),
    ],
    h_prezzo="The price",
    price_rows=[
        ("Sun 13 Sep — Florence airport → Ruffino → Borgo Iesolana", "€ 950.00", "+ VAT 10%"),
        ("Mon 14 Sep — full day at disposal: Baldetti, Il Borro, return", "€ 980.00", "+ VAT 10%"),
        ("Tue 15 Sep — evening at disposal: Badia a Coltibuono, return", "€ 680.00", "+ VAT 10%"),
        ("Wed 16 Sep — Borgo Iesolana → Montefoscoli → Badia di Morrona → Forte dei Marmi", "€ 1,250.00", "+ VAT 10%"),
        ("Fri 18 Sep — Forte dei Marmi → Florence airport", "€ 780.00", "+ VAT 10%"),
        ("Driver's board and lodging, 3 nights (13, 14 and 15 September)",
         "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 4,640.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 5,104.00.",
    perhead="That is about € 243.00 per person for the complete programme.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver, fuel, motorway tolls, parking, full insurance, luggage handling and flight monitoring "
        "on 13 September. No other access charges apply: Florence Airport carries no fee and none of the wineries "
        "on the programme sits inside a restricted traffic zone. On 13 September the driver waits at no extra cost "
        "for up to 90 minutes from the actual landing time, however late the flight arrives."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's board and lodging for the nights of 13, 14 and 15 September, which remain at your charge: "
        "you book and pay for them directly. Winery entrance fees, tastings, meals, guides and gratuities. "
        "Waiting beyond the times set out here, € 50.00 per hour per vehicle. Additional stops or changes to the "
        "itinerary, quoted on request. Return to the property after 02:00, € 250.00. Any entry of a tourist coach "
        "into the centre of Florence, which would require a separate permit."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 1,530.00", "VAT included"),
        ("Balance, within 5 days of the service", "€ 3,574.00", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O050 3413 7070 0000 0003 424 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The driver's board and lodging.</b> The programme requires the driver to stay in the area on the nights "
         "of 13, 14 and 15 September: Borgo Iesolana is about 120 km from our base, and a daily return would push "
         "the driving day beyond the permitted limits. The three nights are at your charge and you book and pay for "
         "them directly: a single room near the property, with dinner, is all that is needed. Many of our clients "
         "put the driver up at the same property as the group, which is the easiest arrangement for everyone. "
         "Please let us know where he will be staying before departure."),
        ("<b>Luggage on 16 September.</b> This is the point worth the closest look: you leave Borgo Iesolana with all "
         "the luggage on board, visit two wineries, and only reach the hotel in Forte dei Marmi in the evening. "
         "The Beluga's hold takes around twenty normal suitcases for 21 guests without difficulty, but do tell us in "
         "advance about oversized items, golf bags or cases of wine bought along the way, so we can plan the loading "
         "or add a support vehicle."),
        ("<b>Access at Badia a Coltibuono.</b> The final stretch of road is narrow and winding. Our 7.64 m minibus "
         "gets there; a full-size coach does not. Please still have the winery confirm the drop-off point and the "
         "manoeuvring space for a vehicle of this length — far better settled now than on the evening itself."),
        ("<b>The departing flight on 18 September.</b> Leaving Forte dei Marmi at 12:30 brings you to Florence "
         "departures around 13:50. That works for a flight from 16:00 onwards; if yours leaves earlier, it is worth "
         "bringing the hotel departure forward, and you can ask us at no extra cost. Send us the flight number and "
         "time and we will confirm the schedule against it."),
        ("<b>The arriving flight on 13 September.</b> We need the flight number and landing time. We have read the "
         "10:15 as the meeting time in the arrivals hall; if it is instead the landing time, everything shifts by "
         "about an hour and we will send you an updated programme."),
        ("<b>Which Ruffino estate.</b> We have quoted Tenuta Poggio Casciano at Bagno a Ripoli, Ruffino's hospitality "
         "estate. Ruffino also receives guests at other properties: please confirm which one, as it would change both "
         "the routing and the price for 13 September."),
        ("<b>17 September.</b> No service is scheduled and nothing is charged. Should your guests want the vehicle at "
         "their disposal in Versilia, we can hold it: half day € 450.00 + VAT, full day € 700.00 + VAT. "
         "Let us know by confirmation so we can keep the driver free."),
        ("<b>To confirm we need</b> the final passenger count, the exact hotel address in Forte dei Marmi, both flight "
         "times, a mobile or WhatsApp contact for the person travelling with the group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> The vehicle is currently free and we hold it for you for the whole "
         "validity of this quotation; the booking becomes firm on receipt of the deposit. Cancellation is free of "
         "charge more than 60 days before the service; from 60 to 30 days the deposit is retained; from 30 to 10 days "
         "50% of the price is charged; in the last 10 days, 100%. With 36 days to the first service today, this "
         "booking falls in the 60-to-30-day band, and from 14 August it moves into the 30-to-10 band. "
         "Quotation valid until 22 August 2026."),
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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Alvora")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Tuscany_Wine_Tour_13-18_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per la giornata sul Monte Amiata del 22 agosto 2026
e il trasferimento da e per l'ospedale a Castel del Piano (GR).

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e piè di pagina su ogni pagina).

    python3 genera_preventivo_monte_amiata.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_monte_amiata.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0822-GI"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Giornata sul Monte Amiata e trasferimento da e per l'ospedale  ·  Castel del Piano (GR)  ·  sabato 22 agosto 2026",
    meta="Preparato per %s  ·  21 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=(
        "Un minibus con conducente a vostra disposizione per l'intera giornata di sabato 22 agosto, "
        "a Castel del Piano e sul Monte Amiata."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con i suoi 7,64 metri il Beluga sale alla Vetta Amiata e arriva ai piazzali dei borghi del monte, "
        "dove un autobus gran turismo non passa: su queste strade è il mezzo giusto. "
        "Il prezzo indicato più avanti è riferito a <b>un mezzo</b>: ci serve il numero esatto dei passeggeri "
        "per confermare che il gruppo entri nei 26 posti."
    ),
    h_servizio="Il servizio",
    svc_head=["Orario", "Percorso", "Percorrenza"],
    svc=[
        ("08:00 – 08:25",
         "<b>Corte Francigena, Castelnuovo dell'Abate (SI) → Castel del Piano (GR).</b> "
         "Il minibus è già in zona: parte da un altro nostro servizio in corso vicino a Montalcino per "
         "raggiungere il vostro hotel. Nessun passeggero a bordo, breve trasferimento.",
         "≈ 17 km · 25 min"),
        ("09:00 – 10:15",
         "<b>Grand Hotel Impero → ospedale → Grand Hotel Impero.</b> "
         "Trasferimento riservato per riaccompagnare in hotel la vostra ospite dimessa, con l'autista che "
         "attende sul posto per tutto il tempo delle formalità di dimissione. "
         "Orari e percorrenza si fissano quando ci direte di quale ospedale si tratta.",
         "da confermare"),
        ("a seguire",
         "<b>Giornata sul Monte Amiata.</b> Grand Hotel Impero → Vetta Amiata, Prato delle Macinaie → "
         "Abbadia San Salvatore → Santa Fiora → Arcidosso → rientro in hotel. Partenza subito dopo il "
         "rientro dall'ospedale, orario esatto da confermare insieme. Mezzo e conducente restano a vostra "
         "disposizione per tutta la giornata. Il giro qui sopra è una <b>proposta</b>: lo adattiamo a "
         "quello che volete vedere e a quanto tempo volete fermarvi in ogni tappa.",
         "≈ 80 km · 6 h 45"),
        ("a fine giornata",
         "<b>Castel del Piano → Corte Francigena, Castelnuovo dell'Abate.</b> Il mezzo rientra a fine "
         "servizio dove era già impegnato, non alla base di Ponte Buggianese.",
         "≈ 17 km · 25 min"),
    ],
    svc_foot=(
        "Distanze e tempi sono stime stradali, traffico escluso. L'orario di partenza per il monte si "
        "conferma insieme a voi in base a come si chiude il servizio del mattino: quello che conta è che "
        "mezzo e conducente restano vostri, con continuità, dal ritiro in ospedale fino a sera."
    ),
    h_prezzo="Il prezzo",
    price_rows=[
        ("Sab 22 ago — mezzo e conducente a disposizione a Castel del Piano e sul Monte Amiata, "
         "circa 8 ore e mezza dal ritiro in ospedale a sera, compreso il trasferimento del mattino "
         "da e per l'ospedale",
         "€ 1.050,00", "+ IVA 10%"),
        ("Trasferimento del mezzo da e per Corte Francigena, Castelnuovo dell'Abate (SI), circa 34 km",
         "€ 150,00", "+ IVA 10%"),
        ("Vitto del conducente", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 1.200,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 1.320,00.",
    perhead=(
        "Il prezzo è per il mezzo e non a persona: non cambia che a bordo siate in dieci o in venticinque. "
        "Il mezzo è già in zona per un altro servizio, quindi il trasferimento è breve — "
        "leggete la nota <i>Il viaggio del mezzo da Corte Francigena</i>."
    ),
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per l'intera giornata, carburante, pedaggi autostradali, parcheggi, assicurazione "
        "completa e l'attesa all'ospedale durante le formalità di dimissione. Sull'itinerario proposto sul Monte "
        "Amiata non risultano oneri di accesso o permessi a pagamento; se una tappa che ci chiederete dovesse "
        "richiedere un parcheggio bus a pagamento, ve lo segnaliamo prima e non dopo."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il vitto del conducente, che resta a vostro carico. Pranzi, ingressi, guide e mance. "
        "Attesa oltre gli orari qui indicati, € 50,00 all'ora per mezzo. Soste aggiuntive o modifiche di percorso "
        "fuori dall'Amiata, quotate su richiesta. Rientro dopo le 02:00, € 250,00. L'eventuale pernottamento del "
        "conducente a Castel del Piano, se il programma si prolunga la sera: anche quello è a vostro carico."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Alla conferma — nessun acconto, il servizio è a meno di 24 ore", "€ 0,00", ""),
        ("Saldo unico, entro il 26 agosto 2026", "€ 1.320,00", "IVA inclusa"),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Prima di tutto: la conferma a voce.</b> Il servizio è per domani mattina e GiroMunna ha un solo "
         "minibus. Girolamo vi richiama a breve per confermarvi che mezzo e conducente sono liberi sabato: "
         "fino a quella telefonata questo preventivo è un prezzo, non una prenotazione."),
        ("<b>Come sta la vostra ospite.</b> È il punto che ci preme di più e vi chiediamo di rispondere con "
         "franchezza. Il Beluga è un minibus turistico: ha i gradini all'ingresso, sedili normali e nessuna "
         "attrezzatura sanitaria a bordo. Va benissimo se la signora cammina da sola o appoggiandosi a un "
         "accompagnatore. Se invece esce dall'ospedale in carrozzina, o se salire tre gradini è un problema, "
         "il mezzo giusto non è il nostro: serve un'auto attrezzata o un trasporto sanitario privato. "
         "Ditecelo subito, perché è una cosa che si scopre male domani mattina davanti all'ospedale."),
        ("<b>Quale ospedale.</b> Non ci avete detto dove si trova. Se è il presidio di Castel del Piano siamo "
         "a pochi minuti dall'hotel e il programma sopra regge così com'è. Se è Abbadia San Salvatore si "
         "aggiunge circa un'ora fra andata e ritorno. Se invece è l'ospedale di Grosseto siamo sui 55 km a "
         "tratta, il mattino si allunga di un paio d'ore e la partenza per il monte slitta verso mezzogiorno: "
         "in quel caso vi rifacciamo gli orari. Ci serve il nome dell'ospedale oggi."),
        ("<b>Due servizi, un mezzo solo.</b> Il programma tiene insieme l'ospedale e la gita, con la partenza "
         "per il monte subito dopo il rientro in hotel. Se il gruppo preferisse fare le due cose in momenti "
         "lontani della giornata, con un mezzo solo non si fa: o si sposta il rientro dall'ospedale al "
         "pomeriggio, oppure serve un secondo minibus, che possiamo cercare ma va deciso oggi e ha un costo "
         "a parte."),
        ("<b>Il viaggio del mezzo da Corte Francigena.</b> Il minibus è già impegnato vicino a Montalcino e "
         "raggiunge Castel del Piano con un salto breve, circa 17 km, invece che dalla nostra base a oltre "
         "170 km di distanza: è il motivo per cui il trasferimento in tabella pesa così poco sul totale. Se a "
         "fine giornata il mezzo dovesse invece rientrare alla base di Ponte Buggianese anziché tornare a Corte "
         "Francigena, il trasferimento si allunga e il prezzo va rivisto: ve lo confermiamo appena sappiamo "
         "come si chiude la giornata."),
        ("<b>Quanti siete.</b> Il Beluga porta 26 passeggeri più l'autista, e il prezzo qui sopra è per un mezzo. "
         "Mandateci il numero esatto: se il gruppo supera i 26, serve un secondo minibus e il preventivo cambia."),
        ("<b>Le strade del monte.</b> La salita alla Vetta Amiata è tutta tornanti e i centri storici di Santa "
         "Fiora e Arcidosso sono stretti: si scende ai piazzali all'ingresso dei borghi e si prosegue a piedi per "
         "pochi minuti. Il nostro minibus da 7,64 m ci arriva, un autobus gran turismo no — è esattamente il "
         "motivo per cui su questo giro conviene il mezzo piccolo. Se avete in mente una tappa precisa, diteci "
         "quale e verifichiamo il punto di discesa prima di partire."),
        ("<b>La giornata del conducente e il suo vitto.</b> Fra il viaggio di andata, il servizio e il rientro "
         "sono quasi quattordici ore: è il massimo che si può fare tornando alla base in giornata. Se volete "
         "tenere il mezzo la sera — una cena sul monte, un rientro dopo le 20:00 — il conducente deve pernottare "
         "a Castel del Piano, e il pernottamento è a vostro carico. Vale lo stesso per il pranzo di sabato: il "
         "vitto del conducente è sempre a carico del cliente, non lo mettiamo a preventivo e non lo organizziamo "
         "noi. La soluzione più comoda, e quella che scelgono quasi tutti i nostri clienti, è farlo mangiare "
         "e dormire nella stessa struttura del gruppo."),
        ("<b>Per confermare ci servono</b> il nome dell'ospedale, due righe sulle "
         "condizioni della vostra ospite, il numero dei passeggeri, l'ora di partenza che preferite per il monte, "
         "un recapito WhatsApp di chi viaggia con il gruppo e i vostri dati di fatturazione."),
        ("<b>Disponibilità e cancellazione.</b> La cancellazione è gratuita oltre 60 giorni prima del servizio; "
         "da 60 a 30 giorni viene trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; "
         "negli ultimi 10 giorni il 100%. Mancando meno di ventiquattr'ore al servizio, questa prenotazione "
         "ricade per intero nell'ultima fascia. Preventivo valido fino alle 20:00 del 21 agosto 2026, "
         "che è il momento oltre il quale il mezzo non fa più in tempo a organizzarsi per domani mattina."),
    ],
    closing=("Ci dispiace per la vostra ospite e speriamo si rimetta presto. Chiamateci o scriveteci il vostro "
             "numero e ci organizziamo per domani.<br/><br/>"
             "Cordiali saluti,<br/>"
             "Girolamo Munna — GiroMunna NCC, Toscana · +39 335 587 4744 · info@giromunna.com"),
)

EN = dict(
    tagline="Coach Hire with Driver  ·  Tuscany, Italy",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Tuscany, Italy  ·  VAT IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="page %d",
    title="Quotation",
    subtitle="A day on Monte Amiata and a transfer to and from the hospital  ·  Castel del Piano (GR)  ·  Saturday 22 August 2026",
    meta="Prepared for %s  ·  21 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=(
        "One minibus with driver at your disposal for the whole day of Saturday 22 August, "
        "in Castel del Piano and on Monte Amiata."
    ),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "At 7.64 m the Beluga climbs to the summit of Monte Amiata and reaches the parking areas of the "
        "mountain villages, where a full-size coach cannot go: on these roads it is the right vehicle. "
        "The price set out below is for <b>one vehicle</b>: we need the exact number of passengers to confirm "
        "the group fits within the 26 seats."
    ),
    h_servizio="The service",
    svc_head=["Time", "Route", "Distance"],
    svc=[
        ("08:00 – 08:25",
         "<b>Corte Francigena, Castelnuovo dell'Abate (SI) → Castel del Piano (GR).</b> "
         "The minibus is already in the area on another of our services near Montalcino and comes across "
         "to reach your hotel. No passengers on board, a short hop.",
         "≈ 17 km · 25 min"),
        ("09:00 – 10:15",
         "<b>Grand Hotel Impero → hospital → Grand Hotel Impero.</b> "
         "Private transfer to bring your discharged guest back to the hotel, with the driver waiting on site "
         "throughout the discharge formalities. "
         "Timings and distance will be fixed once you tell us which hospital it is.",
         "to be confirmed"),
        ("following on",
         "<b>A day on Monte Amiata.</b> Grand Hotel Impero → Vetta Amiata, Prato delle Macinaie → "
         "Abbadia San Salvatore → Santa Fiora → Arcidosso → back to the hotel. Departure straight after "
         "the hospital run, exact time to be confirmed together. Vehicle and driver stay at your disposal "
         "for the whole day. The round above is a <b>proposal</b>: we adapt it to what you want to see and "
         "how long you want to stop at each place.",
         "≈ 80 km · 6 h 45"),
        ("end of day",
         "<b>Castel del Piano → Corte Francigena, Castelnuovo dell'Abate.</b> The vehicle returns at the end "
         "of the service to where it was already engaged, not to the Ponte Buggianese base.",
         "≈ 17 km · 25 min"),
    ],
    svc_foot=(
        "Distances and times are road estimates, traffic excluded. The departure time for the mountain will "
        "be confirmed with you once we know how the morning service wraps up: what matters is that vehicle "
        "and driver stay yours, without a break, from the hospital pickup through the evening."
    ),
    h_prezzo="The price",
    price_rows=[
        ("Sat 22 Aug — vehicle and driver at your disposal in Castel del Piano and on Monte Amiata, "
         "about eight and a half hours from the hospital pickup through the evening, including the "
         "morning transfer to and from the hospital",
         "€ 1,050.00", "+ VAT 10%"),
        ("Vehicle travel to and from Corte Francigena, Castelnuovo dell'Abate (SI), about 34 km",
         "€ 150.00", "+ VAT 10%"),
        ("Driver's meals", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 1,200.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 1,320.00.",
    perhead=(
        "The price is per vehicle, not per person: it does not change whether ten or twenty-five of you are on "
        "board. The vehicle is already in the area on another job, so the transfer is short — please read the "
        "note <i>The vehicle's journey from Corte Francigena</i>."
    ),
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for the whole day, fuel, motorway tolls, parking, full insurance, and the driver's "
        "waiting time at the hospital during the discharge formalities. The proposed Monte Amiata itinerary "
        "carries no known access charges or paid permits; should a stop you ask for require a paid coach car "
        "park, we will tell you beforehand rather than afterwards."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meals, which remain at your charge. Lunches, entrance fees, guides and gratuities. "
        "Waiting beyond the times set out here, € 50.00 per hour per vehicle. Additional stops or route changes "
        "outside the Amiata, quoted on request. Return after 02:00, € 250.00. Any overnight stay for the driver "
        "in Castel del Piano, should the programme run into the evening: that too is at your charge."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("On confirmation — no deposit, the service is less than 24 hours away", "€ 0.00", ""),
        ("Single payment, by 26 August 2026", "€ 1,320.00", "VAT included"),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>First of all: confirmation by phone.</b> The service is for tomorrow morning and GiroMunna has one "
         "minibus. Girolamo will call you shortly to confirm that vehicle and driver are free on Saturday: "
         "until that call, this quotation is a price, not a booking."),
        ("<b>How your guest is.</b> This is the point that concerns us most and we ask you to answer frankly. "
         "The Beluga is a touring minibus: it has steps at the door, ordinary seats and no medical equipment on "
         "board. It is perfectly fine if the lady walks unaided or leaning on a companion. If instead she leaves "
         "hospital in a wheelchair, or if climbing three steps is a problem, ours is not the right vehicle: she "
         "needs an adapted car or a private medical transport. Please tell us straight away — it is a bad thing "
         "to discover tomorrow morning outside the hospital."),
        ("<b>Which hospital.</b> You have not told us where she is. If it is the Castel del Piano hospital we are "
         "a few minutes from the hotel and the programme above holds as it stands. If it is Abbadia San Salvatore, "
         "add roughly an hour there and back. If it is the hospital in Grosseto we are looking at some 55 km each "
         "way, the morning grows by a couple of hours and the departure for the mountain slips towards midday: in "
         "that case we will redo the timings for you. We need the name of the hospital today."),
        ("<b>Two services, one vehicle.</b> The programme holds the hospital run and the excursion together, "
         "with departure for the mountain straight after the return to the hotel. Should the group prefer the "
         "two set well apart in the day, one vehicle cannot do both: either the hospital run moves to the "
         "afternoon, or a second minibus is needed — we can look for one, but it has to be decided today and "
         "carries a separate cost."),
        ("<b>The vehicle's journey from Corte Francigena.</b> The minibus is already engaged near Montalcino "
         "and reaches Castel del Piano with a short hop, about 17 km, rather than from our base over 170 km "
         "away: that is why the transfer line weighs so little on the total. Should the vehicle need to return "
         "to the Ponte Buggianese base at the end of the day instead of going back to Corte Francigena, the "
         "transfer grows and the price needs revising: we will confirm as soon as we know how the day closes."),
        ("<b>How many of you there are.</b> The Beluga carries 26 passengers plus the driver, and the price above "
         "is for one vehicle. Send us the exact number: if the group exceeds 26, a second minibus is needed and "
         "the quotation changes."),
        ("<b>The mountain roads.</b> The climb to the summit of the Amiata is one hairpin after another, and the "
         "old centres of Santa Fiora and Arcidosso are narrow: you get off at the car parks at the entrance to "
         "the villages and walk the last few minutes. Our 7.64 m minibus gets there, a full-size coach does not — "
         "which is exactly why the small vehicle is the one to have on this round. If you have a particular stop "
         "in mind, tell us which and we will check the drop-off point before we set off."),
        ("<b>The driver's day, and his meals.</b> Between the outward journey, the service and the return it comes "
         "to almost fourteen hours: that is the most that can be done while returning to base the same day. If you "
         "want to keep the vehicle in the evening — dinner on the mountain, a return after 20:00 — the driver has "
         "to stay overnight in Castel del Piano, and that overnight is at your charge. The same goes for Saturday "
         "lunch: the driver's board is always at the client's charge, we do not put it in the quotation and we do "
         "not arrange it. The easiest arrangement, and the one almost all our clients choose, is to have him eat "
         "and sleep at the same property as the group."),
        ("<b>To confirm we need</b> the name of the hospital, a couple of lines on your "
         "guest's condition, the number of passengers, your preferred departure time for the mountain, a WhatsApp "
         "contact for the person travelling with the group, and your invoicing details."),
        ("<b>Availability and cancellation.</b> Cancellation is free of charge more than 60 days before the "
         "service; from 60 to 30 days the deposit is retained; from 30 to 10 days 50% of the price is charged; in "
         "the last 10 days, 100%. With less than twenty-four hours to the service, this booking falls entirely "
         "within the last band. Quotation valid until 20:00 on 21 August 2026, the point beyond which the vehicle "
         "can no longer be organised in time for tomorrow morning."),
    ],
    closing=("We are sorry about your guest and hope she recovers quickly. Call us, or send us your number, and "
             "we will get organised for tomorrow.<br/><br/>"
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
        "foot": ParagraphStyle("foot", alignment=TA_JUSTIFY, spaceBefore=6, spaceAfter=2,
                               fontName="Helvetica", fontSize=8.2,
                               textColor=MUTED, leading=11.4),
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
    cols = [26 * mm, usable - 26 * mm - 27 * mm, 27 * mm]
    data = [[Paragraph(h, S["th"]) for h in L["svc_head"]]]
    for orario, desc, km in L["svc"]:
        data.append([
            Paragraph("<b>%s</b>" % orario, S["cellsm"]),
            Paragraph(desc, S["cellsm"]),
            Paragraph(km, S["cellmut"]),
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
    F.append(Paragraph(L["svc_foot"], S["foot"]))

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Grand Hotel Impero, Castel del Piano")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Monte_Amiata_22_agosto_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

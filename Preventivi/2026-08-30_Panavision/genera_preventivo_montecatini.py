#!/usr/bin/env python3
"""
Genera il preventivo GiroMunna per il gruppo Panavision Tours,
Montecatini Terme, 30 agosto - 3 settembre 2026.

Riproduce l'impaginazione dei preventivi GiroMunna (logo, verde bottiglia e oro,
intestazione e pie' di pagina su ogni pagina).

    python3 genera_preventivo_montecatini.py --lingua it --cliente "Nome Cliente"
    python3 genera_preventivo_montecatini.py --lingua en --cliente "Client Name"
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

RIF = "GM-2026-0830-PT"

# --- contenuto ------------------------------------------------------------------
IT = dict(
    tagline="Noleggio Autobus con Conducente  ·  Toscana, Italia",
    footer1="GiroMunna — Munna Girolamo Giuseppe  ·  Ponte Buggianese (PT), Toscana, Italia  ·  P. IVA IT 02124530474",
    footer2="+39 335 587 4744  ·  info@giromunna.com  ·  giromunna.com",
    page="pag. %d",
    title="Preventivo",
    subtitle="Soggiorno a Montecatini Terme · Cinque Terre · Siena e San Gimignano · Lucca e Pisa · Firenze  ·  30 agosto - 3 settembre 2026",
    meta="Preparato per %s  ·  19 agosto 2026  ·  Rif. " + RIF,
    h_mezzo="Il mezzo",
    mezzo_intro=("Un minibus per il vostro gruppo di 17 persone — 16 partecipanti e il capo gruppo — "
                 "con lo stesso conducente per tutti e cinque i giorni."),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata, "
        "sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli."
    ),
    mezzo_close=(
        "Con 17 ospiti a bordo restano nove posti liberi: su tre giornate da undici ore e mezza è un margine "
        "di comodità che si sente. I 7,64 metri contano anche in manovra: il mezzo entra nei terminal bus di "
        "Siena, Lucca e Pisa e trova sosta a Firenze dove un autobus gran turismo da dodici metri fatica. "
        "La nostra base è a un quarto d'ora da Montecatini Terme: il conducente rientra a "
        "casa ogni sera e non vi costa alcun pernottamento."
    ),
    h_servizio="Il servizio",
    svc_head=["Data", "Percorso", "Impegno del mezzo"],
    svc=[
        ("Dom 30 ago",
         "<b>Aeroporto di Firenze (FLR) → Montecatini Terme, Hotel Minerva.</b> "
         "Volo IB689 da Madrid, atterraggio previsto alle 19:30. L'autista vi accoglie in sala arrivi con il "
         "cartello GiroMunna e attende senza costi aggiuntivi fino a 90 minuti dall'atterraggio effettivo, "
         "per quanto il volo ritardi. Poco meno di un'ora sulla A11, arrivo in hotel intorno alle 21:00.",
         "circa 19:15 – 21:15"),
        ("Lun 31 ago",
         "<b>Montecatini Terme → La Spezia → Cinque Terre → Montecatini Terme.</b> "
         "Partenza alle 08:00 e arrivo a La Spezia verso le 09:30. Da lì si prosegue in treno "
         "con il Cinque Terre Express per Manarola, Vernazza e Monterosso: i borghi non sono raggiungibili in "
         "pullman e la soluzione è spiegata nelle Note. Ritrovo a La Spezia alle 17:30 e rientro in hotel "
         "verso le 19:30. Mezzo e conducente a vostra disposizione per l'intera giornata.",
         "circa 07:45 – 19:45"),
        ("Mar 1 set",
         "<b>Montecatini Terme → Siena → San Gimignano → Montecatini Terme.</b> "
         "Partenza alle 08:00 e arrivo a Siena verso le 09:45; discesa al terminal bus di via "
         "Tozzi, sotto San Domenico, a pochi minuti a piedi dal Duomo. Nel primo pomeriggio si prosegue per San "
         "Gimignano, con sosta al parcheggio bus fuori Porta San Giovanni. Rientro in hotel verso le 19:30. "
         "La giornata più lunga su strada del programma.",
         "circa 07:45 – 19:45"),
        ("Mer 2 set",
         "<b>Montecatini Terme → Lucca → Pisa → Montecatini Terme.</b> "
         "Partenza alle 08:00 e arrivo a Lucca verso le 08:40, discesa al terminal bus fuori le "
         "mura. Nel pomeriggio mezz'ora di strada fino a Pisa, con discesa al terminal di via Pietrasantina e "
         "navetta fino a Piazza dei Miracoli. Rientro in hotel verso le 19:30. La giornata più leggera del "
         "programma: c'è tempo in abbondanza.",
         "circa 07:45 – 19:45"),
        ("Gio 3 set",
         "<b>Montecatini Terme → Firenze → Aeroporto di Firenze (FLR).</b> "
         "Check-out e partenza alle 09:00 con tutti i bagagli a bordo, arrivo a Firenze verso le 10:00. "
         "Tempo libero fino alle 17:30: il mezzo resta a Firenze in area di sosta autorizzata, con i vostri "
         "bagagli sorvegliati a bordo, e vi riprende nel punto concordato. Trasferimento all'aeroporto, con "
         "arrivo alle partenze verso le 18:00 per il volo IB690 delle 20:20.",
         "circa 08:45 – 18:15"),
    ],
    h_ztl="Permessi ZTL e accessi",
    ztl_intro=("Avete chiesto espressamente i permessi ZTL: eccoli tutti, giornata per giornata. "
               "Li anticipiamo noi e sono già compresi nel prezzo alla riga <i>Permessi ZTL, terminal e "
               "parcheggi bus</i>. Gli importi sono quelli delle tariffe in vigore: vi riaddebitiamo il costo "
               "effettivo con le ricevute e conguagliamo in fattura, in più o in meno."),
    ztl_head=["Giornata e località", "Cosa serve", "Importo"],
    ztl=[
        ("30 ago e 3 set — Aeroporto di Firenze",
         "Nessun onere di accesso: l'aeroporto di Firenze non applica tariffe ai bus.", "—"),
        ("30 ago – 3 set — Montecatini Terme",
         "Nessun permesso. La sosta davanti all'hotel per carico e scarico è consentita e il mezzo non "
         "resta parcheggiato in centro.", "—"),
        ("31 ago — La Spezia",
         "Sosta del minibus all'area bus per l'intera giornata. Nelle Cinque Terre non esistono permessi "
         "acquistabili per Manarola e Vernazza: sono borghi pedonali senza accesso ai pullman.", "€ 40,00"),
        ("1 set — Siena",
         "Permesso comunale bus turistici e terminal di via Tozzi.", "€ 160,00"),
        ("1 set — San Gimignano",
         "Parcheggio bus fuori le mura, presso Porta San Giovanni.", "€ 40,00"),
        ("2 set — Lucca",
         "Terminal bus fuori le mura. Dentro le mura i pullman non entrano, ma le porte sono a pochi passi.",
         "€ 50,00"),
        ("2 set — Pisa",
         "Terminal bus di via Pietrasantina, con navetta per Piazza dei Miracoli. In Piazza dei Miracoli i bus "
         "non accedono.", "€ 80,00"),
        ("3 set — Firenze",
         "Permesso comunale bus turistici per l'ingresso in città e sosta giornaliera in area autorizzata. "
         "È la voce più pesante e nelle Note trovate come evitarla.", "€ 350,00"),
    ],
    ztl_total_label="Totale permessi e accessi, al netto di IVA",
    ztl_total="€ 720,00",
    h_prezzo="Il prezzo",
    price_rows=[
        ("Dom 30 ago — aeroporto di Firenze → Montecatini Terme", "€ 550,00", "+ IVA 10%"),
        ("Lun 31 ago — giornata intera alle Cinque Terre, via La Spezia", "€ 1.500,00", "+ IVA 10%"),
        ("Mar 1 set — giornata intera a Siena e San Gimignano", "€ 1.400,00", "+ IVA 10%"),
        ("Mer 2 set — giornata intera a Lucca e Pisa", "€ 1.100,00", "+ IVA 10%"),
        ("Gio 3 set — giornata a Firenze e trasferimento all'aeroporto", "€ 1.050,00", "+ IVA 10%"),
        ("Permessi ZTL, terminal e parcheggi bus — dettaglio nella tabella sopra", "€ 720,00", "+ IVA 10%"),
        ("Pernottamento del conducente — non necessario, la base è a un quarto d'ora",
         "<i>nessun costo</i>", ""),
        ("Vitto del conducente, 4 giornate", "<i>a carico vostro</i>", ""),
    ],
    price_total_label="Totale, al netto di IVA",
    price_total="€ 6.320,00",
    vat_note="+ IVA 10%",
    grand="Totale da corrispondere, IVA 10% inclusa: € 6.952,00.",
    perhead="Sono circa € 409,00 a persona su 17 partecipanti, per l'intero programma di cinque giorni.",
    h_incluso="Incluso.",
    incluso=(
        "Mezzo e conducente per cinque giornate, carburante, pedaggi autostradali, assicurazione completa, "
        "movimentazione bagagli e monitoraggio del volo IB689 del 30 agosto. Sono compresi tutti i permessi ZTL, "
        "i terminal e i parcheggi bus elencati nella tabella qui sopra, Firenze inclusa. Il 30 agosto l'autista "
        "attende senza costi aggiuntivi fino a 90 minuti dall'orario di atterraggio effettivo, per quanto il volo "
        "arrivi in ritardo. Il 3 settembre i bagagli restano a bordo e sorvegliati per tutta la giornata."
    ),
    h_nonincluso="Non incluso.",
    nonincluso=(
        "Il vitto del conducente nelle quattro giornate di escursione, che resta a vostro carico. I biglietti del "
        "Cinque Terre Express e la Cinque Terre Card del 31 agosto, che si acquistano in stazione e sono a vostro "
        "carico. Ingressi, musei, pasti, guide e mance. Attesa oltre gli orari qui indicati, € 50,00 all'ora "
        "per mezzo. Soste aggiuntive o modifiche all'itinerario, quotate su richiesta. Rientro in hotel dopo le "
        "02:00, € 250,00."
    ),
    h_pagamento="Pagamento",
    pay_rows=[
        ("Acconto 30% alla conferma", "€ 2.085,60", "IVA inclusa"),
        ("Saldo, entro il 27 agosto 2026", "€ 4.866,40", ""),
    ],
    bank=("Bonifico bancario intestato a Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Note",
    note=[
        ("<b>Le Cinque Terre non si raggiungono in pullman, e non è una questione di permessi.</b> "
         "Manarola e Vernazza sono borghi pedonali: le strade che scendono al mare sono strette, a tornanti e "
         "chiuse ai bus, e non esiste alcun permesso acquistabile che le apra. Monterosso ha una strada di "
         "accesso, ma la sosta è contingentata e comunque non risolve le altre due. La soluzione che "
         "funziona, ed è quella che usano tutti gli operatori seri, è il treno: minibus fino a La "
         "Spezia Centrale, poi il Cinque Terre Express, che collega i borghi ogni quindici o venti minuti in "
         "pochi minuti di viaggio. Vi lasciamo a La Spezia alle 09:30 e vi riprendiamo lì alle 17:30. "
         "I biglietti o la Cinque Terre Card si comprano in stazione o meglio online in anticipo, sono a vostro "
         "carico e in alta stagione costano indicativamente € 20-30 a persona per la giornata. "
         "In alternativa, con mare calmo, il battello da La Spezia tocca Monterosso e Vernazza ed è il modo "
         "più bello di vederle: a Manarola l'attracco dipende dalle condizioni del mare. Ditecelo e "
         "organizziamo la giornata sul battello all'andata e sul treno al ritorno."),
        ("<b>Firenze del 3 settembre: come risparmiare i 350 euro del permesso.</b> "
         "Il permesso comunale per far entrare un bus turistico in città è la voce più cara di "
         "tutto il preventivo, e l'abbiamo messa perché con i bagagli a bordo e otto ore e mezza di tempo "
         "libero è la soluzione più comoda. Esiste però un'alternativa che usiamo spesso: "
         "il minibus vi lascia al parcheggio scambiatore di Villa Costanza, a Scandicci, dove la tramvia T1 "
         "parte ogni pochi minuti e in venti minuti è in Piazza della Stazione, in pieno centro. "
         "Il biglietto costa poco più di un euro e mezzo a persona, il mezzo sosta gratuitamente con i "
         "vostri bagagli e il permesso non serve. Sono circa € 350,00 in meno sul totale. "
         "Fateci sapere quale delle due preferite: il prezzo si adegua di conseguenza."),
        ("<b>Il permesso di Firenze e la lunghezza del mezzo.</b> Le tariffe del Comune di Firenze sono "
         "graduate per lunghezza del veicolo e il Beluga sta sotto gli otto metri, quindi potrebbe rientrare in "
         "una fascia più bassa dei € 350,00 che abbiamo prudenzialmente indicato. Verifichiamo al "
         "momento del rilascio e quello che risparmiamo ve lo scaliamo in fattura."),
        ("<b>Siena e San Gimignano: conviene invertire l'ordine.</b> Così come lo avete scritto il "
         "programma funziona, ma partendo da San Gimignano, che è parecchio più vicino di Siena, si arriva "
         "in piazza verso le 09:15 e si guadagnano circa 45 minuti buoni da spendere a Siena nel pomeriggio, "
         "quando il Campo è al suo meglio. Il prezzo non cambia. Se preferite l'ordine originale va "
         "benissimo lo stesso: ci regoliamo su quello che decidete."),
        ("<b>La giornata del 2 settembre è mezza vuota.</b> Lucca e Pisa distano fra loro 25 minuti e "
         "ed è di gran lunga la giornata più corta del programma: dalle 08:00 alle 19:30 vi "
         "avanza parecchio tempo. Senza alcun costo aggiuntivo possiamo aggiungere una sosta sulla via del "
         "rientro — Pietrasanta e il suo centro di marmi e gallerie, oppure Forte dei Marmi e il mare, "
         "che d'estate un gruppo spagnolo apprezza — oppure semplicemente farvi partire più tardi al "
         "mattino. Ditecelo in fase di conferma."),
        ("<b>Tre giornate da undici ore e mezza di fila.</b> Dal 31 agosto al 2 settembre il programma "
         "prevede 08:00 – 19:30 per tre giorni consecutivi. È fattibile e lo facciamo regolarmente, "
         "ma sta al limite dei tempi di guida e riposo previsti dal regolamento europeo: vi chiediamo di "
         "rispettare gli orari di rientro concordati, perché un ritardo importante di sera si trascina "
         "sulla partenza del mattino dopo. Se un giorno servisse più tempo, avvisateci il giorno prima e "
         "riorganizziamo, non all'ultimo momento."),
        ("<b>Il conducente non pernotta e questo vi fa risparmiare.</b> La nostra base è a Ponte "
         "Buggianese, un quarto d'ora dal vostro hotel: il conducente rientra a casa ogni sera e non c'è "
         "alcun pernottamento da prenotare né da pagare, a differenza di quanto succede quando il gruppo "
         "alloggia lontano. Resta a vostro carico soltanto il vitto nelle quattro giornate di escursione: la "
         "cosa più semplice è aggiungerlo dove pranza il gruppo, altrimenti si arrangia lui e ce lo "
         "dite subito."),
        ("<b>Il volo IB689 del 30 agosto.</b> Con atterraggio alle 19:30 e poco meno di un'ora di autostrada "
         "arrivate all'Hotel Minerva intorno alle 21:00. Verificate con l'hotel il check-in a quell'ora e "
         "soprattutto la cena: molte strutture di Montecatini chiudono la sala alle 21:00 e con diciassette "
         "persone conviene averlo concordato prima, non scoprirlo all'arrivo. Se il volo ritarda l'autista "
         "aspetta comunque fino a 90 minuti dall'atterraggio effettivo, senza addebiti."),
        ("<b>Il volo IB690 del 3 settembre.</b> Ripartendo da Firenze alle 17:30 siete alle partenze verso le "
         "18:00, due ore e venti prima del decollo delle 20:20: per un volo Schengen è giusto. Se "
         "preferite più margine anticipiamo il ritrovo alle 17:00 senza costi aggiuntivi. Confermateci "
         "voi quale orario tenere."),
        ("<b>Disponibilità: qui il tempo stringe davvero.</b> Mancano undici giorni al primo servizio e "
         "siamo nel periodo più pieno dell'anno. Il mezzo oggi è libero e ve lo teniamo per tutta la "
         "validità di questo preventivo, ma non possiamo garantirlo oltre: se il gruppo è confermato, "
         "una vostra conferma anche solo di massima ci permette di bloccare subito il calendario. "
         "Preventivo valido fino al 22 agosto 2026."),
        ("<b>Cancellazione.</b> Gratuita oltre 60 giorni prima del servizio; da 60 a 30 giorni viene "
         "trattenuto l'acconto; da 30 a 10 giorni viene addebitato il 50% del prezzo; negli ultimi 10 giorni "
         "il 100%. Mancando oggi undici giorni al primo servizio, questa prenotazione ricade nella fascia da "
         "30 a 10 giorni, e dal 20 agosto passa in quella degli ultimi 10 giorni: è giusto che lo sappiate "
         "prima di confermare."),
        ("<b>Per confermare ci servono</b> l'indirizzo esatto dell'Hotel Minerva a Montecatini Terme, il "
         "numero definitivo dei passeggeri, un recapito telefonico o WhatsApp del capo gruppo, la vostra "
         "scelta fra permesso di Firenze e tramvia da Villa Costanza, e i vostri dati di fatturazione."),
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
    subtitle="Stay in Montecatini Terme · Cinque Terre · Siena and San Gimignano · Lucca and Pisa · Florence  ·  30 August - 3 September 2026",
    meta="Prepared for %s  ·  19 August 2026  ·  Ref. " + RIF,
    h_mezzo="The vehicle",
    mezzo_intro=("One minibus for your group of 17 — 16 participants and the tour leader — "
                 "with the same driver for all five days."),
    mezzo_bullet=(
        "<b>Mercedes-Benz Beluga</b> — 26 passenger seats plus driver, 7.64 m. Air conditioning, "
        "reclining ultra-comfort seats, fridge bar, on-board audio system, large luggage hold."
    ),
    mezzo_close=(
        "With 17 guests on board nine seats stay free — breathing room you notice across three "
        "eleven-and-a-half-hour days. The 7.64 m matter for manoeuvring too: the vehicle fits the coach "
        "terminals of Siena, Lucca and Pisa and finds parking in Florence where a twelve-metre coach struggles. "
        "Our base is a quarter of an hour from Montecatini Terme: the driver goes home every "
        "night and costs you nothing in accommodation."
    ),
    h_servizio="The service",
    svc_head=["Date", "Route", "Vehicle engaged"],
    svc=[
        ("Sun 30 Aug",
         "<b>Florence Airport (FLR) → Montecatini Terme, Hotel Minerva.</b> "
         "Flight IB689 from Madrid, scheduled landing 19:30. The driver welcomes you in the arrivals hall with "
         "the GiroMunna sign and waits at no extra cost for up to 90 minutes from the actual landing time, "
         "however late the flight arrives. A little under an hour on the A11, reaching the hotel around 21:00.",
         "approx. 19:15 – 21:15"),
        ("Mon 31 Aug",
         "<b>Montecatini Terme → La Spezia → Cinque Terre → Montecatini Terme.</b> "
         "Departure at 08:00, reaching La Spezia around 09:30. From there onward by train on the "
         "Cinque Terre Express to Manarola, Vernazza and Monterosso: the villages cannot be reached by coach "
         "and the solution is set out in the Notes. Meeting point back at La Spezia at 17:30, hotel around "
         "19:30. Vehicle and driver at your disposal for the whole day.",
         "approx. 07:45 – 19:45"),
        ("Tue 1 Sep",
         "<b>Montecatini Terme → Siena → San Gimignano → Montecatini Terme.</b> "
         "Departure at 08:00, reaching Siena around 09:45; drop-off at the via Tozzi coach terminal "
         "below San Domenico, a few minutes on foot from the Duomo. Early afternoon, on to San Gimignano, "
         "with the coach park just outside Porta San Giovanni. Back at the hotel around 19:30. "
         "The longest day on the road of the programme.",
         "approx. 07:45 – 19:45"),
        ("Wed 2 Sep",
         "<b>Montecatini Terme → Lucca → Pisa → Montecatini Terme.</b> "
         "Departure at 08:00, reaching Lucca around 08:40, drop-off at the coach terminal outside the "
         "walls. In the afternoon half an hour on to Pisa, drop-off at the via Pietrasantina terminal with the "
         "shuttle to Piazza dei Miracoli. Back at the hotel around 19:30. The lightest day of the programme: "
         "there is time to spare.",
         "approx. 07:45 – 19:45"),
        ("Thu 3 Sep",
         "<b>Montecatini Terme → Florence → Florence Airport (FLR).</b> "
         "Check-out and departure at 09:00 with all the luggage on board, reaching Florence around 10:00. "
         "Free time until 17:30: the vehicle stays in Florence in an authorised parking area, with your luggage "
         "watched on board, and collects you at the agreed point. Transfer to the airport, reaching "
         "departures around 18:00 for flight IB690 at 20:20.",
         "approx. 08:45 – 18:15"),
    ],
    h_ztl="ZTL permits and access",
    ztl_intro=("You asked specifically about ZTL permits: here they all are, day by day. We advance them and "
               "they are already included in the price under the line <i>ZTL permits, terminals and coach "
               "parking</i>. The amounts are at the tariffs currently in force: we recharge you the actual cost "
               "with the receipts and settle the difference on the invoice, up or down."),
    ztl_head=["Day and place", "What is required", "Amount"],
    ztl=[
        ("30 Aug and 3 Sep — Florence Airport",
         "No access charge: Florence Airport applies no coach fee.", "—"),
        ("30 Aug – 3 Sep — Montecatini Terme",
         "No permit. Stopping in front of the hotel to load and unload is allowed and the vehicle is not "
         "parked in the centre.", "—"),
        ("31 Aug — La Spezia",
         "Minibus parking at the coach area for the full day. In the Cinque Terre there is no permit that can "
         "be bought for Manarola and Vernazza: they are pedestrian villages with no coach access.",
         "€ 40.00"),
        ("1 Sep — Siena",
         "Municipal tourist coach permit and the via Tozzi terminal.", "€ 160.00"),
        ("1 Sep — San Gimignano",
         "Coach park outside the walls, by Porta San Giovanni.", "€ 40.00"),
        ("2 Sep — Lucca",
         "Coach terminal outside the walls. Coaches do not enter the walled town, but the gates are a few "
         "steps away.", "€ 50.00"),
        ("2 Sep — Pisa",
         "Via Pietrasantina coach terminal, with the shuttle to Piazza dei Miracoli. Coaches have no access to "
         "Piazza dei Miracoli itself.", "€ 80.00"),
        ("3 Sep — Florence",
         "Municipal tourist coach permit for entry into the city and full-day parking in an authorised area. "
         "It is the heaviest item and the Notes explain how to avoid it.", "€ 350.00"),
    ],
    ztl_total_label="Total permits and access, excluding VAT",
    ztl_total="€ 720.00",
    h_prezzo="The price",
    price_rows=[
        ("Sun 30 Aug — Florence airport → Montecatini Terme", "€ 550.00", "+ VAT 10%"),
        ("Mon 31 Aug — full day to the Cinque Terre, via La Spezia", "€ 1,500.00", "+ VAT 10%"),
        ("Tue 1 Sep — full day to Siena and San Gimignano", "€ 1,400.00", "+ VAT 10%"),
        ("Wed 2 Sep — full day to Lucca and Pisa", "€ 1,100.00", "+ VAT 10%"),
        ("Thu 3 Sep — day in Florence and transfer to the airport", "€ 1,050.00", "+ VAT 10%"),
        ("ZTL permits, terminals and coach parking — itemised in the table above", "€ 720.00", "+ VAT 10%"),
        ("Driver's accommodation — not required, our base is a quarter of an hour away",
         "<i>no charge</i>", ""),
        ("Driver's meals, 4 days", "<i>at your charge</i>", ""),
    ],
    price_total_label="Total, excluding VAT",
    price_total="€ 6,320.00",
    vat_note="+ VAT 10%",
    grand="Total payable, VAT 10% included: € 6,952.00.",
    perhead="That is about € 409.00 per person across 17 travellers, for the complete five-day programme.",
    h_incluso="Included.",
    incluso=(
        "Vehicle and driver for five days, fuel, motorway tolls, full insurance, luggage handling and monitoring "
        "of flight IB689 on 30 August. All the ZTL permits, terminals and coach parking listed in the table "
        "above are included, Florence among them. On 30 August the driver waits at no extra cost for up to 90 "
        "minutes from the actual landing time, however late the flight arrives. On 3 September the luggage stays "
        "on board and watched all day."
    ),
    h_nonincluso="Not included.",
    nonincluso=(
        "The driver's meals on the four excursion days, which remain at your charge. Cinque Terre Express "
        "tickets and the Cinque Terre Card on 31 August, bought at the station and at your charge. Entrance "
        "fees, museums, meals, guides and gratuities. Waiting beyond the times set out here, € 50.00 per "
        "hour per vehicle. Additional stops or changes to the itinerary, quoted on request. Return to the hotel "
        "after 02:00, € 250.00."
    ),
    h_pagamento="Payment",
    pay_rows=[
        ("Deposit 30% on confirmation", "€ 2,085.60", "VAT included"),
        ("Balance, by 27 August 2026", "€ 4,866.40", ""),
    ],
    bank=("Bank transfer to Munna Girolamo Giuseppe — "
          "IBAN IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05."),
    h_note="Notes",
    note=[
        ("<b>The Cinque Terre cannot be reached by coach, and it is not a matter of permits.</b> "
         "Manarola and Vernazza are pedestrian villages: the roads down to the sea are narrow, full of "
         "hairpins and closed to coaches, and there is no permit on sale that opens them. Monterosso does have "
         "an access road, but stopping is rationed and it does not solve the other two anyway. The solution "
         "that works, and the one every serious operator uses, is the train: minibus to La Spezia Centrale, "
         "then the Cinque Terre Express, which links the villages every fifteen to twenty minutes in a few "
         "minutes' ride. We drop you at La Spezia at 09:30 and collect you there at 17:30. Tickets or the "
         "Cinque Terre Card are bought at the station, or better online in advance; they are at your charge and "
         "in high season cost roughly € 20-30 per person for the day. Alternatively, in calm weather, the "
         "ferry from La Spezia calls at Monterosso and Vernazza and is the finest way to see them: at Manarola "
         "landing depends on the sea. Tell us and we will build the day around the boat outbound and the train "
         "back."),
        ("<b>Florence on 3 September: how to save the € 350 permit.</b> "
         "The municipal permit that lets a tourist coach into the city is the most expensive single item in "
         "this quotation, and we have included it because with the luggage on board and eight and a half hours "
         "of free time it is the most comfortable arrangement. There is an alternative we use often, though: "
         "the minibus drops you at the Villa Costanza park-and-ride in Scandicci, where the T1 tramway leaves "
         "every few minutes and reaches Piazza della Stazione, right in the centre, in twenty minutes. The "
         "ticket costs little more than one and a half euro per person, the vehicle parks free of charge with "
         "your luggage, and no permit is needed. That is about € 350.00 off the total. Let us know which "
         "of the two you prefer and the price follows."),
        ("<b>The Florence permit and the length of the vehicle.</b> The City of Florence tariffs are graduated "
         "by vehicle length and the Beluga is under eight metres, so it may fall into a band below the "
         "€ 350.00 we have prudently quoted. We will check when the permit is issued and credit you "
         "whatever we save."),
        ("<b>Siena and San Gimignano: worth reversing the order.</b> The programme works as you wrote it, but "
         "starting from San Gimignano, a good deal closer than Siena, puts you in the square around 09:15 and "
         "gains a good 45 minutes to spend in Siena in the afternoon, when the Campo is at its best. The price "
         "is unchanged. If you prefer the original order that is perfectly fine too: we follow whatever you "
         "decide."),
        ("<b>2 September is a half-empty day.</b> Lucca and Pisa are 25 minutes apart and the whole day comes "
         "much the shortest of the programme: from 08:00 to 19:30 you have time left over. At no extra "
         "cost we can add a stop on the way back — Pietrasanta, with its marble workshops and galleries, "
         "or Forte dei Marmi and the sea, which a Spanish group tends to enjoy in summer — or simply have "
         "you start later in the morning. Tell us when you confirm."),
        ("<b>Three consecutive eleven-and-a-half-hour days.</b> From 31 August to 2 September the programme "
         "runs 08:00 – 19:30 for three days in a row. It is workable and we do it regularly, but it sits "
         "at the limit of the driving and rest times set by the European regulation: we ask you to keep to the "
         "agreed return times, because a serious delay in the evening carries over into the next morning's "
         "departure. If one day needs more time, tell us the day before and we will reorganise — not at "
         "the last minute."),
        ("<b>The driver does not stay overnight, and that saves you money.</b> Our base is at Ponte "
         "Buggianese, a quarter of an hour from your hotel: the driver goes home every night and there is no "
         "accommodation to book or pay for, unlike the usual case where the group stays further away. Only the "
         "meals on the four excursion days remain at your charge: the simplest arrangement is to add him "
         "wherever the group has lunch, otherwise he sorts himself out — just tell us straight away."),
        ("<b>Flight IB689 on 30 August.</b> Landing at 19:30, with a little under an hour of motorway, brings you to "
         "the Hotel Minerva around 21:00. Do check with the hotel that check-in at that hour is fine and, above "
         "all, dinner: many Montecatini properties close the dining room at 21:00, and with seventeen people it "
         "is far better agreed in advance than discovered on arrival. If the flight is late the driver waits "
         "regardless, up to 90 minutes from the actual landing, at no charge."),
        ("<b>Flight IB690 on 3 September.</b> Leaving Florence at 17:30 puts you at departures around 18:00, "
         "two hours and twenty before the 20:20 take-off: right for a Schengen flight. If you would rather have "
         "more margin we can bring the pick-up forward to 17:00 at no extra cost. Confirm which time you want "
         "us to hold."),
        ("<b>Availability: time really is short here.</b> There are eleven days to the first service and this "
         "is the busiest stretch of the year. The vehicle is free today and we hold it for you for the whole "
         "validity of this quotation, but we cannot guarantee it beyond that: if the group is confirmed, even "
         "an indicative go-ahead from you lets us block the calendar straight away. Quotation valid until "
         "22 August 2026."),
        ("<b>Cancellation.</b> Free of charge more than 60 days before the service; from 60 to 30 days the "
         "deposit is retained; from 30 to 10 days 50% of the price is charged; in the last 10 days, 100%. With "
         "eleven days to the first service today, this booking falls in the 30-to-10-day band, and from "
         "20 August it moves into the last-10-days band: you should know that before confirming."),
        ("<b>To confirm we need</b> the exact address of the Hotel Minerva in Montecatini Terme, the final "
         "passenger count, a mobile or WhatsApp contact for the tour leader, your choice between the Florence "
         "permit and the tramway from Villa Costanza, and your invoicing details."),
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

    # --- permessi ZTL: il cliente li ha chiesti espressamente.
    # Titolo e presentazione restano insieme, altrimenti il titolo resta
    # orfano in fondo alla pagina del servizio.
    F.append(KeepTogether([
        Paragraph(L["h_ztl"], S["h2"]),
        Paragraph(L["ztl_intro"], S["body"]),
    ]))
    zcols = [40 * mm, usable - 40 * mm - 24 * mm, 24 * mm]
    zdata = [[Paragraph(h, S["th"]) for h in L["ztl_head"]]]
    for place, what, amount in L["ztl"]:
        zdata.append([
            Paragraph("<b>%s</b>" % place, S["cellsm"]),
            Paragraph(what, S["cellsm"]),
            Paragraph(amount, S["cellsm"]),
        ])
    zdata.append([
        Paragraph("<b>%s</b>" % L["ztl_total_label"], S["cellsm"]),
        Paragraph("", S["cellsm"]),
        Paragraph("<b>%s</b>" % L["ztl_total"], S["cellsm"]),
    ])
    zt = Table(zdata, colWidths=zcols, repeatRows=1)
    zt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, RULE),
        ("LINEABOVE", (0, -1), (-1, -1), 0.9, GREEN),
        ("BACKGROUND", (0, -1), (-1, -1), CREAM),
        ("SPAN", (0, -1), (1, -1)),
        ("ALIGN", (2, 0), (2, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    F.append(zt)

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
    ap.add_argument("--cliente", "--client", dest="cliente", default="Panavision Tours")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    name = a.out or os.path.join(
        HERE, "GiroMunna_Preventivo_Montecatini_30_agosto-3_settembre_2026_%s.pdf" % a.lang.upper())
    print(build(a.lang, a.cliente, name))

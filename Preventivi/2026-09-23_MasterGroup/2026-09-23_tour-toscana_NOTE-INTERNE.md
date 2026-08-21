# Note interne — Tour della Toscana, mercoledì 23 settembre 2026, 12 pax

**Cliente:** Master Group Tour Operator · **Rif. preventivo:** GM-2026-0923-MG ·
**Servizio:** mercoledì 23 settembre 2026 · **Preparato:** 21 agosto 2026 · **Validità:** 4 settembre 2026

**Questo preventivo è solo in italiano, per decisione di Girolamo.** Master Group è un tour
operator italiano e ha scritto in italiano, quindi la versione inglese non serve. È l'unico
preventivo che fa eccezione alla regola delle due lingue: se dovesse servire l'inglese, il
dizionario `EN` sta nella storia del repository, nel commit che ha aggiunto questa cartella.

File generati:

- `GiroMunna_Preventivo_Tour_Toscana_23_settembre_2026_IT.pdf`
- `genera_preventivo_tour_toscana.py` — rigenera il PDF
- `preventivo_tour_toscana_23_settembre_2026.html` — la pagina web
- `mail_per_master_group.txt` — il testo della mail, da copiare e inviare a mano

Tutto dentro `Preventivi/2026-09-23_MasterGroup/`.

Il cliente è già il valore predefinito dello script. Per rigenerare il PDF:

```bash
python3 genera_preventivo_tour_toscana.py
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## La richiesta

Master Group chiede la quotazione di **una giornata sola** per una famiglia di **12 persone**,
con quattro itinerari alternativi fra cui scegliere. Chiedono uno sprinter o un minibus.
Carico e scarico all'**Hotel Adamas, Via Ricasoli 9, Firenze** — verificato, è un tre stelle
di 23 camere a due passi dal Duomo — e domandano espressamente quale sia il punto di carico
più vicino e se si possa organizzare una navetta in van dall'hotel.

La richiesta era arrivata **senza data**. Girolamo l'ha poi avuta: **mercoledì 23 settembre
2026**. Il preventivo, il riferimento, i nomi dei file e la cartella sono stati rifatti su
quel giorno; la prima stesura, intestata `GM-2026-0821-MG`, sta nella storia del repository.

**Il 23 settembre gioca a favore.** È infrasettimanale e di fine stagione, quindi i prezzi di
media stagione reggono senza maggiorazioni e non c'è da rivederli. Siena e San Gimignano di
mercoledì sono molto più vivibili, e in Val d'Orcia si è in piena vendemmia: l'itinerario D
ne guadagna parecchio come giornata da vendere. Due cose dette al cliente: a fine settembre
la luce va via verso le 19:20, quindi su B e D l'ultimo tratto si fa al buio, e i borghi in
collina chiudono prima che d'estate.

## Prezzi

| Itinerario | Km mezzo | Netto | IVA inclusa | A persona |
|---|---|---|---|---|
| A · Firenze → Pisa → Lucca → Firenze | 320 | € 1.590,91 | € 1.750,00 | € 145,83 |
| B · Firenze → Pisa → Siena → San Gimignano → Firenze | 470 | € 1.954,55 | € 2.150,00 | € 179,17 |
| C · Firenze → Siena → San Gimignano → Monteriggioni → Firenze | 330 | € 1.590,91 | € 1.750,00 | € 145,83 |
| D · Firenze → Montalcino → Pienza → Montepulciano → Firenze | 400 | € 1.272,73 | € 1.400,00 | € 116,67 |
| Navetta van A/R (opzionale) | — | *su richiesta* | — | — |
| Vitto del conducente | — | a carico del cliente | — | — |

Acconto 30%: da € 420,00 (itinerario D) a € 645,00 (itinerario B).

⚠️ **I prezzi che Girolamo ha dato — 1.750, 2.150, 1.750, 1.400 — sono IVA INCLUSA**, non
al netto: lo ha precisato dopo averli mandati. I netti qui sopra sono ricavati all'indietro
dividendo per 1,10, e per questo hanno i centesimi. Nel preventivo il cliente vede il netto
nella colonna di sinistra e la cifra tonda in quella dell'IVA inclusa, che è quella che
Girolamo ha in testa. **Da tenere a mente in fattura e in trattativa: la cifra tonda è il
lordo, non l'imponibile.**

**I prezzi li ha fissati Girolamo**, non il modello qui sotto. Il modello resta utile come
riferimento per i preventivi futuri, ma per questo lavoro il listino è quello deciso da lui
e il conto sotto serve solo a documentare da dove si era partiti.

## Come erano stati costruiti i prezzi, e dove sono finiti

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come
questo. Riportato al netto: trasferimento di ~50 km € 500,00; giornata a disposizione di
~80 km e 5 ore € 809,00.

Da lì, e dalla scala già usata per Alvora (140 km e 8 ore → € 980; 250 km e tre tappe →
€ 1.250), viene una regola pratica che tiene su tutti e tre i preventivi:

> **circa € 600 di base più € 2,60 al chilometro**, poi si aggiungono gli oneri di accesso
> e si arrotonda al rialzo se la giornata è lunga.

Verifica sui riferimenti esistenti: 80 km → € 808; 140 km → € 964; 250 km → € 1.250.
Torna.

### Attenzione: due misure diverse di chilometri

Girolamo ha corretto i chilometri: **320, 470, 330 e 400**, che sono quelli veri del mezzo
da rimessa a rimessa — il percorso del cliente più il vuoto Ponte Buggianese-Firenze e
ritorno (un centinaio di km) più gli spostamenti ai parcheggi bus durante le soste. Le mie
stime — 195, 315, 205, 270 — erano il solo percorso del cliente, e come tali reggono: da
Firenze a Pisa sono novanta chilometri, non c'è discussione.

Nel preventivo e nella pagina web compaiono adesso **le cifre di Girolamo, dichiarate per
quello che sono** ("chilometri percorsi dal mezzo, dalla rimessa al rientro"). Serviva
dirlo: Master Group è un tour operator e se cerca Firenze-Pisa-Lucca-Firenze su una mappa
trova 195 km, non 320. Dichiarata così, la cifra non è contestabile e anzi giustifica meglio
il prezzo.

**Il modello dei prezzi resta però ancorato ai chilometri di percorso, non a quelli di
rimessa, ed è corretto così.** Il motivo: i preventivi di riferimento sono costruiti allo
stesso modo. Le Filigare quota € 809,00 per una "giornata da ~80 km", ma San Donato in
Poggio dista ~75 km dalla base, quindi quel prezzo si porta già dentro ~150 km di vuoto.
Applicare € 2,60 ai chilometri da rimessa significherebbe **contare due volte** il vuoto,
che sta già dentro i € 600 di base e dentro i prezzi di riferimento. Il conto qui sotto è
quindi rimasto sui chilometri di percorso e **i prezzi non cambiano**.

### Gli oneri di accesso, cifre vere di Girolamo

Queste sono le tariffe reali, non più le mie stime:

| Voce | Costo |
|---|---|
| Checkpoint di Firenze | **€ 421,00** |
| Sosta bus Pisa | **€ 270,00** |
| Sosta bus Lucca | **€ 180,00** |
| Permesso comunale Siena | **€ 160,00** |
| Sosta bus San Gimignano | **€ 240,00** |
| Parcheggio Pienza | **€ 22,00** |

Mancano ancora **Monteriggioni** (itinerario C) e **Montalcino e Montepulciano** (itinerario
D): nei conti qui sotto sono lasciati fuori, quindi i residui di C e D sono un filo
ottimistici.

Sommati per itinerario, sul netto:

| | Netto | Oneri dentro | % del netto | Resta | Resta al km |
|---|---|---|---|---|---|
| A · Pisa e Lucca | € 1.590,91 | € 871,00 | **55%** | € 719,91 | € 2,25 |
| B · Pisa, Siena, San Gimignano | € 1.954,55 | € 1.091,00 | **56%** | € 863,55 | € 1,84 |
| C · Siena, San Gim., Monteriggioni | € 1.590,91 | € 821,00 + Monteriggioni | 52% | € 769,91 | € 2,33 |
| D · Montalcino, Pienza, Montepulciano | € 1.272,73 | € 443,00 + due parcheggi | 35% | € 829,73 | € 2,07 |

### Il listino di Girolamo è coerente, il rilievo su D era sbagliato

Tolti gli oneri, quello che resta per il trasporto sta fra **€ 1,84 e € 2,33 al chilometro**
su tutti e quattro gli itinerari: una banda stretta, con i valori che calano man mano che la
giornata si allunga. È esattamente come si prezza il trasporto.

E l'ordine si ribalta: **D non è il più povero dei quattro, è quello che lascia di più in
assoluto** (€ 829,73), perché porta dentro € 443 di oneri contro gli € 871 di A. Il rilievo
scritto in precedenza — «D è fuori scala, va alzato» — **era sbagliato e va considerato
chiuso.** Nasceva dal confrontare quattro prezzi lordi di oneri come se fossero omogenei,
quando A ne contiene il doppio di D.

⚠️ **Il dato che conta davvero, però, è un altro: gli oneri di accesso valgono dal 35% al
56% del prezzo netto.** Su B sono € 1.091 su € 1.954,55. Più della metà di quello che il
cliente paga, su tre itinerari su quattro, non è ricavo: è denaro che esce comunque. Ha due
conseguenze pratiche, ed è la cosa più importante di tutte queste note:

1. **Lo spazio di trattativa è molto più stretto di quanto sembri.** Se Master Group chiede
   il 10% su A, sono € 175 su € 719,91 di residuo: un quarto di quello che resta.
2. **Vale la pena dire al cliente quanto pesano.** Vedi il punto in fondo, "Da valutare".

**Non sono stati usati come base i prezzi del Corte Francigena divisi per due**, come vuole
la regola: quello è un lavoro a due mezzi con importi già scontati per volume.

## Margine

Preventivo costruito sul **mezzo di proprietà** (Beluga).

I chilometri corretti da Girolamo obbligano a rifare anche questo conto: **la stima di
€ 250-350 di costo diretto a giornata era ottimistica.** Su 320-470 km reali il solo gasolio
vale € 140-240, cui si aggiungono i pedaggi (la A11 su A, la A1 della Valdichiana su D) e la
giornata dell'autista, che su B e D è di dodici-tredici ore. Realisticamente si sta sui
**€ 400-500 a giornata**, più gli oneri di accesso che qui sono compresi nel prezzo e che,
con le tariffe vere, valgono € 443-1.091 secondo l'itinerario.

Con il listino deciso da Girolamo, tolti gli oneri di accesso che sono compresi nel prezzo,
resta questo per coprire costi e margine:

| | Netto | − accessi | Resta | Margine stimato |
|---|---|---|---|---|
| A · Pisa e Lucca | € 1.590,91 | € 295 | € 1.296 | ~€ 850 |
| B · Pisa, Siena, San Gimignano | € 1.954,55 | € 455 | € 1.500 | ~€ 1.000 |
| C · Siena, San Gimignano, Monteriggioni | € 1.590,91 | € 395 | € 1.196 | ~€ 750 |
| D · Montalcino, Pienza, Montepulciano | € 1.272,73 | € 275 | € 998 | ~€ 530 |

Con le tariffe vere degli oneri il conto è questo:

| | Netto | − oneri | Resta | − gasolio e pedaggi | Per la giornata e il margine |
|---|---|---|---|---|---|
| A · Pisa e Lucca | € 1.590,91 | € 871 | € 720 | ~€ 180 | **~€ 540** |
| B · Pisa, Siena, San Gimignano | € 1.954,55 | € 1.091 | € 864 | ~€ 260 | **~€ 605** |
| C · Siena, San Gim., Monteriggioni | € 1.590,91 | € 821+ | € 770 | ~€ 185 | **~€ 585** |
| D · Montalcino, Pienza, Montepulciano | € 1.272,73 | € 443+ | € 830 | ~€ 225 | **~€ 605** |

Quei € 540-605 sono la giornata dell'autista più il margine. Se guida Girolamo è la sua
giornata più quello che avanza; se guida un dipendente, di margine vero ne resta poco.

**Rispetto al conto precedente il quadro si è stretto di parecchio**, perché le mie stime
degli oneri erano basse di circa € 500 a itinerario. Nessuno dei quattro è in perdita e la
banda è omogenea, ma non c'è il cuscinetto che sembrava esserci: **in trattativa non si
scende, e se proprio si deve, si scende su D, che è quello che lascia di più.**

Nessun pernottamento del conducente: si parte e si torna a Firenze in giornata e la base di
Ponte Buggianese è a ~50 km dal punto di carico. Sull'itinerario D, però, la giornata del
conducente sfiora le tredici ore fra partenza dalla base e rientro: sta nei limiti ma è da
tenere presente quando si sceglie l'autista.

**Se si subappalta a Francesco**, il costo si colloca sui € 600-700 al giorno e il margine
si assottiglia: in quel caso conviene rivedere al rialzo del 20-25% prima di rispondere.

## Il punto di carico — il lavoro vero di questo preventivo

Via Ricasoli 9 è dentro la ZTL, a due passi dal Duomo. Verificato sulle fonti del Comune e
di Servizi alla Strada:

- La **ZTL bus di Firenze copre tutto il centro abitato, 24 ore su 24, tutti i giorni**, e
  riguarda ogni veicolo per trasporto passeggeri **oltre i nove posti**. Quindi vale per il
  Beluga *e* varrebbe per uno sprinter da 12 o 16 posti: cambiare mezzo non risolve niente,
  ed è l'argomento da usare se insistono sullo sprinter.
- Serve il **contrassegno**, che si compra solo online e previa registrazione del veicolo
  sul portale di Servizi alla Strada, con tariffa a seconda di lunghezza e classe
  ambientale. **Il costo vero per noi, dato da Girolamo, è € 421,00.** Le tariffe pubblicate
  che avevo trovato — € 235 fino a 8 metri, € 315 oltre, per un diesel Euro VI con permesso
  giornaliero ordinario — non corrispondono: fa fede la cifra di Girolamo, che è quella che
  paga davvero. Resta vero che sotto gli 8 metri si sta nella fascia più bassa, e questo il
  preventivo lo dice al cliente senza citare importi.
- I punti di salita/discesa attivi sono: **Piazza Vittorio Veneto** (2 stalli, 24 h, salita
  e discesa, max 10 min), **Piazzale Michelangelo** (8 stalli, 24 h, max 20 min),
  **Viale Ariosto** (1 stallo, 24 h, max 10 min), **Piazza Savonarola** (2 stalli, solo
  discesa, 08:00-20:00, max 5 min), **Largo Vincenzo Giudice** (8 stalli, 24 h, ma
  riservato ai servizi da e per la stazione di Santa Maria Novella).
- Distanze a piedi dall'Adamas: Savonarola ~1,4 km, Largo Giudice ~1,1 km, Piazza Vittorio
  Veneto ~2,5 km, Piazzale Michelangelo ~2,5 km più la salita.

Su richiesta di Girolamo il preventivo dice **esplicitamente e in grassetto, in prima pagina,
che in Via Ricasoli il minibus non entra e che non esiste permesso che lo consenta**. Serviva:
scritto come prima, un tour operator poteva pensare che bastasse pagare il contrassegno per
avere il mezzo davanti alla porta. Le tre ragioni, tutte verificate, sono cumulative:

1. **L'area del Duomo è area pedonale**, non semplicemente ZTL: lì l'accesso dei veicoli è
   vietato sempre, non solo negli orari della ZTL, e i varchi sono protetti da **pilomat**
   che con i permessi ordinari, compresi quelli alberghieri, non si aprono. Il civico 9 si
   affaccia praticamente sulla piazza.
2. **La ZTL bus** vale per ogni veicolo oltre i nove posti, quindi anche per lo sprinter che
   il cliente proponeva in alternativa.
3. **Il contrassegno bus non è un lasciapassare**: autorizza a circolare solo sui percorsi
   prestabiliti e a fermarsi solo nei punti autorizzati. Anche pagandolo, in Via Ricasoli
   non ci si arriva.

Quindi: **nessun punto che consenta la salita è a distanza pedonale ragionevole**. Da lì la
proposta della navetta van, che è esattamente quello che il cliente aveva intuito
chiedendola. Nel preventivo è indicato Piazza Vittorio Veneto come ritrovo del mattino
perché è l'unico vicino al centro senza limiti di orario né di tipo di servizio.

⚠️ **Nel CLAUDE.md il permesso di Firenze è indicato in ~€ 350: la cifra vera è € 421,00.**
Vale la pena aggiornare la regola, perché è un numero che tornerà su ogni preventivo che
tocca Firenze. Stessa cosa per Pisa: nel CLAUDE.md il parcheggio bus dell'aeroporto è dato a
~€ 61, mentre la sosta bus in città costa € 270. Sono due voci diverse, ma conviene
scriverle entrambe. Se vuoi che aggiorni il CLAUDE.md con tutto il listino degli oneri —
Firenze € 421, Pisa € 270, Lucca € 180, Siena € 160, San Gimignano € 240, Pienza € 22 —
dimmelo e lo faccio.

## Altre verifiche di accesso

- **Pisa:** sosta bus al terminal di Via Pietrasantina, ~€ 60, compresa nel prezzo di A e B.
- **Siena:** permesso comunale bus turistici ~€ 160, compreso in B e C. Il centro storico è
  chiuso ai bus, si scende ai punti autorizzati fuori dalle mura.
- **Val d'Orcia:** Montalcino, Pienza e Montepulciano hanno parcheggi bus a pagamento sotto
  le mura, stimati ~€ 40 in tutto, compresi in D.
- **Lucca e San Gimignano:** sosta fuori dalle mura, nessun onere significativo.
- **Regolamento UNESCO di Firenze:** ne esiste uno nuovo sul trasporto turistico dentro
  l'area del centro storico, che vieta caddy e risciò e ammette solo navette elettriche
  contingentate su due itinerari. **Non ci riguarda**, in nessuna delle due direzioni: il
  Beluga non fa trasporto turistico dentro l'area UNESCO, e il TAR ha confermato la
  distinzione fra quel servizio e il trasporto pubblico non di linea. Quindi **i van NCC
  della navetta restano fuori dal regolamento** e la soluzione che abbiamo quotato regge.

Tutti gli oneri sono **compresi nel prezzo** invece di essere ribaltati a parte: per un tour
operator è più pulito e toglie argomenti di discussione il giorno del servizio.

## Da chiarire prima di rispondere

1. ✅ **Disponibilità del mezzo: confermata da Girolamo, il Beluga del 23 settembre è
   libero.** Il preventivo lo dice al cliente a chiare lettere. Resta solo da bloccarlo
   appena arriva la conferma — il mezzo è uno solo e non ci sono alternative.
2. ✅ **I van sono passati a "su richiesta", come hai deciso.** Nel preventivo non c'è più
   nessuna cifra: si offre di sentire il collega di Firenze e girare la tariffa, oppure si
   lascia che se ne occupi il cliente o l'Adamas. Così non ti impegni su un prezzo prima di
   averlo verificato e la risposta alla loro domanda resta comunque un sì.
   Per tua memoria, la stima di partenza era **€ 320,00 netti andata e ritorno** per due van
   fino a nove posti: quattro corse in tutto, su un costo presunto di € 60-70 a corsa. Se il
   collega ti dà una tariffa molto diversa, il margine sta lì.
3. **Master Group è un tour operator**, non il cliente finale: rivende con il suo ricarico e
   quasi certamente tratterà. I prezzi sono tenuti alti apposta, c'è margine per scendere.
4. **Il numero dei passeggeri.** Dodici è comodissimo sul Beluga. Se la famiglia cresce fino
   a 26 il mezzo regge lo stesso e il prezzo non cambia — vale la pena dirglielo, è un
   argomento di vendita.
5. **Composizione della famiglia.** Su D e C ci sono salite vere, quella di Montepulciano
   soprattutto. Se ci sono anziani o bambini piccoli conviene saperlo prima.
6. **L'itinerario B.** Nel preventivo è quotato ma sconsigliato apertamente, con due
   alternative concrete. Se lo confermano, l'autista fa una giornata di dodici ore e mezza:
   va scelto chi la regge.
7. **Le scadenze della cancellazione.** Oggi mancano 33 giorni al servizio, quindi si è
   nella fascia da 60 a 30 giorni (si trattiene l'acconto). **Dal 24 agosto** si passa alla
   fascia da 30 a 10, dove si addebita il 50%: nel preventivo il cliente è avvisato, e per
   noi è la leva per farlo decidere in fretta. La validità è fissata al 4 settembre.
8. **Bloccare il mezzo sul 23 settembre** appena arriva la conferma.
9. **Mancano tre tariffe:** Monteriggioni per l'itinerario C, Montalcino e Montepulciano
   per il D. Non cambiano il quadro, ma i residui di C e D sono un filo ottimistici finché
   non si hanno.

## Da valutare: dire al cliente quanto pesano gli oneri

Oggi il preventivo dice che gli oneri di accesso sono compresi, ma non quanto valgono. Con
le cifre vere in mano la scelta merita un ripensamento: su A sono € 871 su € 1.590,91 di
netto, il 55%. Scrivere nel preventivo *"il prezzo comprende € 871,00 di oneri di accesso —
checkpoint di Firenze, sosta bus di Pisa e di Lucca — che versiamo per vostro conto"*
avrebbe due effetti:

- **Toglie il terreno sotto la trattativa.** Un tour operator che vede che più della metà
  del prezzo non è nostro ricavo non chiede lo sconto sull'intero importo.
- **Fa capire il valore del tutto compreso**, che oggi passa come una formula e diventerebbe
  una cifra.

Il contro: si mostra la propria struttura di costo, e se un concorrente quota "trasporto
€ 800 + oneri a parte" il confronto diventa possibile. Personalmente lo farei — con questi
numeri il rischio di sembrare cari senza motivo è più grande. **Decidi tu: se dici di sì,
lo aggiungo al preventivo in due minuti.**

**Il preventivo è chiuso e si può mandare così com'è.** Non resta niente da verificare
prima dell'invio: la data c'è, il mezzo è libero, il punto di carico è documentato e i van
non impegnano nessuno. L'unica cosa che potrebbe tornare indietro è la richiesta della
tariffa dei van — e a quel punto basta una telefonata al collega di Firenze.

## Cosa è già stato detto al cliente e cosa no

Nel preventivo c'è tutto: la faccenda della ZTL spiegata per esteso, le tre soluzioni per il
carico, il consiglio di girare l'itinerario C, il parere contrario su B e le scadenze della
cancellazione. Non c'è nessun riferimento a Francesco né ai costi all'ingrosso, e i van sono
presentati come "tramite un collega di Firenze".

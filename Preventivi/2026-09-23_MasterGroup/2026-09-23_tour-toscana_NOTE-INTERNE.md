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

| Itinerario | Km | Netto | IVA inclusa | A persona |
|---|---|---|---|---|
| A · Firenze → Pisa → Lucca → Firenze | ~195 | € 1.380,00 | € 1.518,00 | € 126,50 |
| B · Firenze → Pisa → Siena → San Gimignano → Firenze | ~315 | € 1.950,00 | € 2.145,00 | € 178,75 |
| C · Firenze → Siena → San Gimignano → Monteriggioni → Firenze | ~205 | € 1.550,00 | € 1.705,00 | € 142,08 |
| D · Firenze → Montalcino → Pienza → Montepulciano → Firenze | ~270 | € 1.620,00 | € 1.782,00 | € 148,50 |
| Navetta van A/R (opzionale) | — | € 320,00 | € 352,00 | — |
| Vitto del conducente | — | a carico del cliente | — | — |

Acconto 30%: da € 455,40 (itinerario A) a € 643,50 (itinerario B).

## Come sono stati costruiti i prezzi

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come
questo. Riportato al netto: trasferimento di ~50 km € 500,00; giornata a disposizione di
~80 km e 5 ore € 809,00.

Da lì, e dalla scala già usata per Alvora (140 km e 8 ore → € 980; 250 km e tre tappe →
€ 1.250), viene una regola pratica che tiene su tutti e tre i preventivi:

> **circa € 600 di base più € 2,60 al chilometro**, poi si aggiungono gli oneri di accesso
> e si arrotonda al rialzo se la giornata è lunga.

Verifica sui riferimenti esistenti: 80 km → € 808; 140 km → € 964; 250 km → € 1.250.
Torna.

Applicata qui, più i permessi:

| | Base + km | Accessi | Totale grezzo | Quotato |
|---|---|---|---|---|
| A · 195 km | € 1.107 | Pisa € 60 + Firenze € 235 | € 1.402 | € 1.380 |
| B · 315 km | € 1.419 | Pisa € 60 + Siena € 160 + Firenze € 235 | € 1.874 | € 1.950 |
| C · 205 km | € 1.133 | Siena € 160 + Firenze € 235 | € 1.528 | € 1.550 |
| D · 270 km | € 1.302 | parcheggi Val d'Orcia ~€ 40 + Firenze € 235 | € 1.577 | € 1.620 |

B è tirato un po' sopra il calcolo perché è una giornata di dodici ore e mezza: le ore
extra vanno pagate. A è tenuto appena sotto perché è la giornata più corta ed è quella che
fa da prezzo civetta fra le quattro.

**Non sono stati usati come base i prezzi del Corte Francigena divisi per due**, come vuole
la regola: quello è un lavoro a due mezzi con importi già scontati per volume.

## Margine

Preventivo costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato € 250-350
per giornata di servizio, cui vanno aggiunti gli oneri di accesso che qui sono compresi nel
prezzo (€ 235-455 secondo l'itinerario). Il margine resta buono su tutti e quattro, ottimo
su A e C.

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
  sul portale di Servizi alla Strada. Tariffa a seconda di lunghezza e classe ambientale:
  per un diesel Euro VI il permesso giornaliero ordinario è **€ 235 fino a 8 metri** e
  **€ 315 oltre**. Il Beluga sta a 7,64 m, quindi paga la fascia bassa: **sono € 80 al
  giorno di vantaggio** rispetto a un gran turismo, ed è un argomento di vendita.
- I punti di salita/discesa attivi sono: **Piazza Vittorio Veneto** (2 stalli, 24 h, salita
  e discesa, max 10 min), **Piazzale Michelangelo** (8 stalli, 24 h, max 20 min),
  **Viale Ariosto** (1 stallo, 24 h, max 10 min), **Piazza Savonarola** (2 stalli, solo
  discesa, 08:00-20:00, max 5 min), **Largo Vincenzo Giudice** (8 stalli, 24 h, ma
  riservato ai servizi da e per la stazione di Santa Maria Novella).
- Distanze a piedi dall'Adamas: Savonarola ~1,4 km, Largo Giudice ~1,1 km, Piazza Vittorio
  Veneto ~2,5 km, Piazzale Michelangelo ~2,5 km più la salita.

Quindi: **nessun punto che consenta la salita è a distanza pedonale ragionevole**. Da lì la
proposta della navetta van, che è esattamente quello che il cliente aveva intuito
chiedendola. Nel preventivo è indicato Piazza Vittorio Veneto come ritrovo del mattino
perché è l'unico vicino al centro senza limiti di orario né di tipo di servizio.

⚠️ **Nel CLAUDE.md il permesso di Firenze è indicato in ~€ 350.** La cifra verificata oggi è
€ 235 per la fascia sotto gli 8 metri. Il preventivo usa € 235. Se la regola in CLAUDE.md
va aggiornata, decidi tu.

## Altre verifiche di accesso

- **Pisa:** sosta bus al terminal di Via Pietrasantina, ~€ 60, compresa nel prezzo di A e B.
- **Siena:** permesso comunale bus turistici ~€ 160, compreso in B e C. Il centro storico è
  chiuso ai bus, si scende ai punti autorizzati fuori dalle mura.
- **Val d'Orcia:** Montalcino, Pienza e Montepulciano hanno parcheggi bus a pagamento sotto
  le mura, stimati ~€ 40 in tutto, compresi in D.
- **Lucca e San Gimignano:** sosta fuori dalle mura, nessun onere significativo.

Tutti gli oneri sono **compresi nel prezzo** invece di essere ribaltati a parte: per un tour
operator è più pulito e toglie argomenti di discussione il giorno del servizio.

## Da chiarire prima di rispondere

1. ⚠️ **Verifica il calendario del 23 settembre prima di mandare.** Il preventivo dice al
   cliente che il mezzo per quel giorno è a sua disposizione. Il lavoro Alvora del 13-18
   settembre non confligge, ma il Beluga è uno solo: se quel mercoledì fosse già impegnato,
   quella riga va cambiata prima che il preventivo esca.
2. **I van non sono nostri.** I € 320,00 andata e ritorno coprono due van fino a nove posti
   con un collega di Firenze, e vanno concordati **prima** di impegnarsi. Nel preventivo la
   cosa è dichiarata al cliente ("si confermano insieme alla prenotazione"). Se preferisci
   non impegnarti affatto, togli la riga della navetta dal listino e la seconda nota: resta
   la soluzione taxi, che il cliente organizza da sé.
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

## Cosa è già stato detto al cliente e cosa no

Nel preventivo c'è tutto: la faccenda della ZTL spiegata per esteso, le tre soluzioni per il
carico, il consiglio di girare l'itinerario C, il parere contrario su B e le scadenze della
cancellazione. Non c'è nessun riferimento a Francesco né ai costi all'ingrosso, e i van sono
presentati come "tramite un collega di Firenze".

# Note interne — Montecatini Terme 30.08-03.09.2026, 17 pax

**Cliente:** Panavision Tours (Fernando Ibáñez, Madrid — fernando@panavision-tours.es,
tel. 0034 676196351) · **Rif. preventivo:** GM-2026-0830-PT · **Preparato:** 19 agosto 2026 ·
**Validità:** 22 agosto 2026

File generati:
- `GiroMunna_Preventivo_Montecatini_30_agosto-3_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Montecatini_30_agosto-3_settembre_2026_EN.pdf`
- `genera_preventivo_montecatini.py` — rigenera entrambi i PDF
- `preventivo_montecatini_30_agosto-3_settembre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-08-30_Panavision/`.

Il cliente (Panavision Tours) è già il valore predefinito dello script. Per rigenerare i PDF:

```bash
python3 genera_preventivo_montecatini.py --lingua it
python3 genera_preventivo_montecatini.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## URGENTE — da fare prima di rispondere

**Mancano undici giorni al primo servizio ed è alta stagione.** La prima cosa non è il
prezzo, è il calendario: **controlla che il Beluga sia libero dal 30 agosto al 3 settembre**,
tutti e cinque i giorni. Se non lo è, il preventivo non parte così com'è e va deciso subito
se coinvolgere Francesco.

Attenzione anche alla fascia di cancellazione: oggi, 19 agosto, siamo a 11 giorni, quindi
nella fascia **da 30 a 10 giorni (50%)**. **Da domani, 20 agosto, si passa negli ultimi 10
giorni (100%).** Nel preventivo è scritto chiaro, così il cliente lo sa prima di confermare.

## Il gruppo e il programma

17 persone paganti (16 partecipanti più il capo gruppo) più l'autista: sul Beluga da 26
posti ci stanno larghi, restano nove posti liberi. Nessun problema di capienza, nessun
secondo mezzo da valutare.

| Data | Servizio | Km | Ore | Netto |
|---|---|---|---|---|
| Dom 30 ago | FLR (volo IB689, atterraggio 19:30) → Montecatini, Hotel Minerva | 50 | 2 | € 550,00 |
| Lun 31 ago | Cinque Terre via La Spezia, giornata a disposizione | 220 | 11,5 | € 1.500,00 |
| Mar 1 set | Siena e San Gimignano, giornata a disposizione | 250 | 11,5 | € 1.400,00 |
| Mer 2 set | Lucca e Pisa, giornata a disposizione | 105 | 11,5 | € 1.100,00 |
| Gio 3 set | Firenze a disposizione + transfer FLR (volo IB690 delle 20:20) | 110 | 9 | € 1.050,00 |
| — | Permessi ZTL e parcheggi bus, riaddebito al costo | | | € 720,00 |
| — | Pernottamento del conducente | | | non necessario |
| — | Vitto del conducente, 4 giornate | | | a carico del cliente |

**Totale netto € 6.320,00 · IVA 10% € 632,00 · Totale € 6.952,00** (circa € 409,00 a persona)

Acconto 30% € 2.085,60 — saldo € 4.866,40 entro il 27 agosto, **prima** del servizio: con un
operatore estero nuovo e undici giorni di preavviso è la scelta giusta.

## Come sono stati costruiti i prezzi

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come
questo. Riportato al netto:

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Gli € 809 per 5 ore implicano circa **€ 162 all'ora**. Su questo lavoro tutte le giornate
sono state quotate **sotto** la pura proporzione oraria, perché cinque servizi consecutivi
giustificano un minimo di scala: 11,5 ore × 162 farebbero € 1.863, e il 31 agosto è quotato
€ 1.500. Il transfer del 30 agosto segue direttamente i € 500 di Le Filigare, con € 50 in
più per l'arrivo serale e il monitoraggio del volo.

**Non è stato usato il Corte Francigena** (GM-2026-0819-CF): quel preventivo ha due mezzi e
importi già scontati per volume, e usarli qui schiaccerebbe il prezzo sotto mercato.

C'è quindi **margine di trattativa verso il basso** se Panavision tira sul prezzo — sono
operatori spagnoli che rivendono — ma il preventivo non nasce basso ed è giusto così.

## Margine

Costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato € 250-350 a giornata di
servizio e **nessun pernottamento**, perché Montecatini Terme dista dodici chilometri dalla
base: il conducente rientra a casa ogni sera. Il margine sulle cinque giornate è buono.

I € 720 di permessi sono **partita di giro** e non producono margine: nel preventivo è
scritto che si riaddebita il costo effettivo con le ricevute e si conguaglia in fattura.

**Se si subappalta a Francesco**, il costo si colloca sui € 600-700 al giorno e il margine
si assottiglia parecchio: in quel caso i prezzi vanno rivisti al rialzo del 20-25% prima
di inviare.

## Il punto vero: le Cinque Terre

Il cliente ha chiesto **Manarola, Vernazza e Monterosso in pullman. Non è possibile**, e non
è una questione di permessi da comprare: Manarola e Vernazza sono borghi pedonali, le strade
che scendono al mare sono strette, a tornanti e chiuse ai bus. Monterosso ha una strada di
accesso ma la sosta è contingentata, e comunque non risolve le altre due.

Quotata la soluzione che funziona: **minibus fino a La Spezia Centrale (110 km, 1h30), poi
Cinque Terre Express fra i borghi**. Scarico alle 09:30, ripresa alle 17:30. I biglietti o
la Cinque Terre Card sono a carico del cliente, indicativamente € 20-30 a persona.

Nel preventivo è offerta anche l'alternativa del **battello** da La Spezia con mare calmo
(tocca Monterosso e Vernazza; a Manarola l'attracco dipende dal mare), andata in battello e
ritorno in treno.

Se Panavision insiste per arrivare a Monterosso in bus, va verificata la sosta prima di
promettere qualsiasi cosa.

## Permessi ZTL: quello che è certo e quello che è stimato

Il cliente li ha chiesti espressamente, quindi nel preventivo c'è una **sezione dedicata**
con il dettaglio giornata per giornata.

| Giornata | Voce | Importo | Fonte |
|---|---|---|---|
| 30 ago e 3 set | Aeroporto di Firenze | nessun onere | dato di casa |
| 30 ago – 3 set | Montecatini Terme, carico/scarico in hotel | nessun onere | — |
| 31 ago | La Spezia, sosta area bus | € 40,00 | **stima** |
| 1 set | Siena, permesso comunale bus turistici | € 160,00 | dato di casa |
| 1 set | San Gimignano, parcheggio bus | € 40,00 | **stima** |
| 2 set | Lucca, terminal bus fuori le mura | € 50,00 | **stima** |
| 2 set | Pisa, terminal di via Pietrasantina | € 80,00 | **stima** |
| 3 set | Firenze, permesso bus turistici + sosta giornaliera | € 350,00 | dato di casa |
| | **Totale** | **€ 720,00** | |

Certi solo Siena e Firenze, che vengono dai dati di casa. Gli altri quattro sono stime, ma
**non c'è esposizione**: nel preventivo è scritto che si riaddebita il costo effettivo con
le ricevute e si conguaglia in fattura, in più o in meno. Le tariffe vanno comunque
verificate prima della partenza.

## La leva sul prezzo: Firenze del 3 settembre

I € 350 del permesso di Firenze sono la voce più cara del preventivo. Nelle Note è offerta
l'alternativa: **scarico a Villa Costanza (Scandicci) e tramvia T1 fino in centro**, venti
minuti, poco più di un euro e mezzo a persona, sosta gratuita del mezzo con i bagagli a
bordo, nessun permesso.

Se il cliente sceglie la tramvia il totale scende a **€ 5.970,00 netti, € 6.567,00 IVA
inclusa**. È una carta buona da giocare se tirano sul prezzo: sono € 385 in meno per loro
senza toccare il nostro margine.

C'è anche un secondo margine: le tariffe di Firenze sono graduate per lunghezza del veicolo
e il Beluga sta sotto gli otto metri, quindi potrebbe rientrare in una fascia più bassa dei
€ 350. Nel preventivo è promesso di scalare in fattura quello che si risparmia.

## Altre cose segnalate al cliente

- **Tre giornate da 11,5 ore consecutive** (31 ago – 2 set, 08:00-19:30). Fattibile, ma al
  limite dei tempi di guida e riposo: nel preventivo è chiesto di rispettare gli orari di
  rientro, perché un ritardo di sera si trascina sulla partenza del mattino dopo. Serve
  anche a coprirci.
- **Siena e San Gimignano conviene invertirli**: partendo da San Gimignano (85 km contro i
  120 di Siena) si guadagnano circa 45 minuti. Proposto senza cambiare il prezzo.
- **Il 2 settembre è mezzo vuoto**: Lucca e Pisa sono 105 km in 11,5 ore. Offerta una sosta
  in più senza costi (Pietrasanta o Forte dei Marmi) oppure partenza più tarda. È un regalo
  che non costa nulla e fa buona impressione.
- **Cena del 30 agosto**: arrivo in hotel verso le 21:00. Segnalato di verificare con
  l'Hotel Minerva il check-in a quell'ora e soprattutto la cena, che molte strutture di
  Montecatini chiudono alle 21:00.
- **Volo del 3 settembre**: ripresa alle 17:30, alle partenze verso le 18:00, due ore e venti
  prima del decollo. Per uno Schengen va bene; offerto di anticipare alle 17:00 senza costi.

## Da chiarire prima di confermare

1. **Disponibilità del Beluga**, 30 agosto - 3 settembre. Prima di tutto il resto.
2. **Indirizzo esatto dell'Hotel Minerva** a Montecatini Terme, per il transfer del 30.
3. **Numero definitivo dei passeggeri** e recapito telefonico o WhatsApp del capo gruppo.
4. **Scelta fra permesso di Firenze e tramvia da Villa Costanza**, che cambia il totale.
5. **Ordine di Siena e San Gimignano**, se accettano l'inversione.
6. **Dati di fatturazione** di Panavision Tours.

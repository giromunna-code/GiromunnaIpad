# Note interne — Montecatini Terme 30.08-03.09.2026, 17 pax

**Cliente:** Panavision Tours (Fernando Ibáñez, Madrid — fernando@panavision-tours.es,
tel. 0034 676196351) · **Rif. preventivo:** GM-2026-0830-PT · **Preparato:** 19 agosto 2026 ·
**Validità:** 22 agosto 2026

File generati:
- `GiroMunna_Preventivo_Montecatini_30_agosto-3_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Montecatini_30_agosto-3_settembre_2026_EN.pdf`
- `genera_preventivo_montecatini.py` — rigenera entrambi i PDF
- `preventivo_montecatini_30_agosto-3_settembre_2026.html` — la pagina web bilingue
- `2026-08-30_montecatini_TESTO-MAIL_IT.txt` — testo della mail, da copiare
- `2026-08-30_montecatini_TESTO-MAIL_EN.txt` — lo stesso in inglese

I due testi mail sono in testo semplice, senza formattazione, così si incollano in Gmail
puliti. **Non è stata creata nessuna bozza e non è stato inviato nulla:** la mail la scrive
e la manda Girolamo. Prima di mandarla vanno ricontrollati la disponibilità del mezzo e il
fatto che il testo dice «il mezzo oggi è libero».

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
| Dom 30 ago | FLR (volo IB689, atterraggio 19:30) → Montecatini, Hotel Minerva | 50 | 2 | € 400,00 |
| Lun 31 ago | Cinque Terre via La Spezia, giornata a disposizione | 220 | 11,5 | € 1.050,00 |
| Mar 1 set | Siena e San Gimignano, giornata a disposizione | 250 | 11,5 | € 950,00 |
| Mer 2 set | Lucca e Pisa, giornata a disposizione | 105 | 11,5 | € 780,00 |
| Gio 3 set | Firenze a disposizione + transfer FLR (volo IB690 delle 20:20) | 110 | 9 | € 780,00 |
| — | Check point e sosta bus, riaddebito al costo, **fuori campo IVA** | | | € 1.371,00 |
| — | Pernottamento del conducente | | | non necessario |
| — | Vitto del conducente, 4 giornate | | | a carico del cliente |

**Servizi € 3.960,00 + IVA 10% € 396,00 = € 4.356,00 · Check point € 1.371,00 senza IVA ·
Totale € 5.727,00** (circa € 337,00 a persona)

L'IVA si applica **solo ai servizi**: i check point sono tassa comunale e restano fuori
dall'imponibile, quindi entrano nel totale tali e quali.

I chilometri qui sopra servono solo a ricostruire il prezzo: **nel preventivo consegnato al
cliente non compaiono**, né nella tabella del servizio né nelle note. Lì ci sono soltanto gli
orari e i tempi di percorrenza.

Acconto 30% arrotondato a € 1.710,00 — saldo € 4.017,00 entro il 27 agosto, **prima** del
servizio: con un operatore estero nuovo e undici giorni di preavviso è la scelta giusta.

## Come sono stati costruiti i prezzi

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come
questo. Riportato al netto:

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

### La prima stesura era troppo alta: perché

La prima versione partiva dai **€ 162 all'ora** impliciti in Le Filigare (€ 809 per 5 ore) e
li scalava sulle giornate da 11,5 ore. Totale: € 6.952,00. Sbagliato, e l'errore è nel metodo.

**Una giornata da 11,5 ore non vale il doppio di una da 5.** Le cinque ore di Le Filigare
pagano soprattutto un minimo di giornata: uscire il mezzo, impegnare il conducente, coprire
il fisso. Le ore in più di questo programma sono ore in cui il gruppo è a Siena o alle Cinque
Terre e il mezzo è fermo in parcheggio: sono ore di attesa, e costano poco. Scalare
linearmente le trattava come se fossero tutte ore di guida.

**E sono cinque giornate consecutive per un tour operator.** Stesso mezzo, stesso conducente,
nessun riposizionamento, nessun pernottamento, un unico contratto: è il lavoro più economico
che ci sia da erogare. Non si prezza come cinque lavori singoli messi in fila. Vale la stessa
logica per cui il Corte Francigena, a due mezzi, ha importi per mezzo più bassi — con la
differenza che lì lo sconto è per volume di mezzi, qui per continuità di giornate.

### Come sono costruiti i prezzi adesso

Base: una **tariffa di giornata piena**, con un aumento contenuto per le giornate lunghe e
per la strada, non una moltiplicazione delle ore.

| Giornata | Netto | Perché |
|---|---|---|
| 31 ago — Cinque Terre | € 1.050,00 | la più cara: 220 km e la giornata più lunga |
| 1 set — Siena e San Gimignano | € 950,00 | 250 km ma due tappe vicine fra loro |
| 2 set — Lucca e Pisa | € 780,00 | 105 km, giornata corta di strada |
| 3 set — Firenze e transfer | € 780,00 | 9 ore, mezzo fermo in città quasi tutto il giorno |
| 30 ago — transfer serale FLR | € 400,00 | sotto i € 500 di Le Filigare perché è dentro un pacchetto |

Le Filigare resta il riferimento buono per **il trasferimento singolo**, non per le giornate
lunghe: quello è il pezzo di quel preventivo che si può ancora usare tale e quale.

## Margine

Costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato € 250-350 a giornata di
servizio e **nessun pernottamento**, perché Montecatini Terme dista dodici chilometri dalla
base: il conducente rientra a casa ogni sera. Sono circa **€ 1.600 di costo vivo su cinque
giornate**, contro € 3.960 di servizi: il margine resta buono anche dopo il taglio.

I € 1.371 di check point sono **partita di giro** e non producono margine: si riaddebita il
costo effettivo con le ricevute e si conguaglia in fattura. **Quelli non si toccano** se
serve scendere ancora: è cassa che esce davvero. Valgono quasi un quarto del totale, quindi
conviene spiegarli bene invece di nasconderli dentro il prezzo — è il motivo per cui la
tabella dedicata resta la scelta giusta.

Il margine vero sta tutto sui **€ 3.960 di servizi**, contro circa € 1.600 di costo vivo su
cinque giornate.

**Se si subappalta a Francesco**, il costo si colloca sui € 600-700 al giorno e a questi
prezzi il margine si assottiglia parecchio: in quel caso il lavoro va rifatto sui numeri,
non inviato così com'è.

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

| Giornata | Voce | Importo |
|---|---|---|
| 30 ago e 3 set | Aeroporto di Firenze | nessun onere |
| 30 ago – 3 set | Montecatini Terme, carico/scarico in hotel | nessun onere |
| 31 ago | La Spezia, check point bus turistici e sosta | € 100,00 |
| 1 set | Siena, check point bus turistici | € 160,00 |
| 1 set | San Gimignano, check point bus turistici | € 240,00 |
| 2 set | Lucca, check point bus turistici | € 180,00 |
| 2 set | Pisa, check point di via Pietrasantina | € 270,00 |
| 3 set | Firenze, check point + sosta giornaliera, tariffa da settembre | € 421,00 |
| | **Totale, fuori campo IVA** | **€ 1.371,00** |

**Sono tutti dati di Girolamo: nessuna stima.** Le mie stime iniziali erano lontanissime —
avevo messo San Gimignano a € 40 contro € 240 reali, Pisa a € 80 contro € 270, Lucca a € 50
contro € 180, La Spezia a € 40 contro € 100. In totale avevo stimato € 720 dove ne servono
€ 1.371: quasi il doppio.

**Firenze: € 421 è la tariffa in vigore da settembre**, e il terzo giorno del gruppo ci
ricade dentro per tre giorni. Se il programma slittasse ad agosto varrebbe l'importo più
basso.

**Sono tassa comunale, quindi senza IVA.** Non vanno mai messi nell'imponibile insieme ai
servizi: si anticipano, si riaddebitano al costo e restano fuori campo. Nel preventivo la
tabella del prezzo lo mostra a parte — totale servizi, IVA sui servizi, poi i check point —
così il cliente vede subito su cosa può recuperare l'IVA e su cosa no. A un tour operator
questa distinzione interessa parecchio.

Nota per i prossimi lavori: in Toscana **ogni città d'arte ha il suo check point per i bus
turistici e costano parecchio.** Non vanno mai stimati a occhio come parcheggi: sono la voce
che può sballare un preventivo. Le tariffe sono ora in `CLAUDE.md`, e vanno comunque
riverificate perché i Comuni le ritoccano.

## La leva sul prezzo: Firenze del 3 settembre

I € 350 del permesso di Firenze sono la voce più cara del preventivo. Nelle Note è offerta
l'alternativa: **scarico a Villa Costanza (Scandicci) e tramvia T1 fino in centro**, venti
minuti, poco più di un euro e mezzo a persona, sosta gratuita del mezzo con i bagagli a
bordo, nessun permesso.

Se il cliente sceglie la tramvia il totale scende a **€ 5.306,00**. È la carta da giocare se
tirano ancora sul prezzo: sono **€ 421,00 esatti in meno** per loro — esatti perché il check
point non sconta IVA — **senza toccare il nostro margine**, perché è un costo che
semplicemente non si sostiene.

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

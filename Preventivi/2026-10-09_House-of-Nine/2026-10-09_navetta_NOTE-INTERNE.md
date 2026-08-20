# Note interne — Navetta 9 ottobre 2026, due minibus

**Cliente:** House of Nine (Firenze) · **Rif. preventivo:** GM-2026-1009-HN
**Preparato:** 20 agosto 2026 · **Validità:** 3 settembre 2026

File generati:
- `GiroMunna_Preventivo_Navetta_9_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Navetta_9_ottobre_2026_EN.pdf`
- `genera_preventivo_navetta_9_ottobre.py` — rigenera entrambi i PDF
- `preventivo_navetta_9_ottobre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-10-09_House-of-Nine/`.

Il cliente («House of Nine») è già il valore predefinito dello script. Per rigenerare i PDF:

```bash
python3 genera_preventivo_navetta_9_ottobre.py --lingua it
python3 genera_preventivo_navetta_9_ottobre.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

> **Versione a due mezzi.** Su decisione di Girolamo il servizio è quotato **solo sui due
> minibus**, Beluga e Tourengo. La prima stesura era su quattro mezzi (€ 4.600 netti) ed è
> nella storia git, commit `7a69229`, se dovesse servire riprenderla.

---

## Il programma

Venerdì 9 ottobre 2026, tre trasferimenti nella stessa giornata.

| | Ora | Percorso | Stima |
|---|---|---|---|
| 1 | 14:30 | Firenze, House of Nine (Via dei Conti 9) → Villa Medicea di Lilliano, Grassina | 12 km · 35 min |
| 2 | 18:00 | Villa Medicea di Lilliano → Tenuta Bossi, Marchesi Gondi, Pontassieve | 25 km · 45 min |
| 3 | 23:00 | Tenuta Bossi → Firenze, House of Nine | 22 km · 35 min |

## Prezzi

| Voce | Netto |
|---|---|
| Minibus 1 — Beluga, 26 posti, i tre trasferimenti, a disposizione 14:00-24:00 | € 1.150,00 |
| Minibus 2 — Tourengo, 28 posti, stesso servizio | € 1.150,00 |
| Vitto e alloggio conducenti | non necessario |

**Totale netto € 2.300,00 · IVA 10% € 230,00 · Totale € 2.530,00**
(a pieno carico sui 54 posti, ≈ € 47,00 a persona)

Acconto 30% € 759,00 — saldo € 1.771,00.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo, e la scala di Alvora.
**Non** il Corte Francigena diviso per due: quegli importi sono già scontati per volume.

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento ~50 km | € 500,00 |
| Le Filigare — giornata a disposizione, ~80 km, 5 h | € 809,00 |
| Alvora — giornata a disposizione, 140 km, 8 h | € 980,00 |
| **9 ottobre — giornata a disposizione, ~190 km, 10 h con chiusura a mezzanotte** | **€ 1.150,00** |

**Il punto chiave: non sono tre corse, è una giornata a disposizione.** Fra il primo e il
secondo trasferimento passano quasi tre ore, fra il secondo e il terzo più di quattro, e la
base è a 55 km da Firenze: i mezzi non rientrano, restano fermi tutto il pomeriggio e tutta
la sera con i conducenti. Da qui i ~190 km per mezzo contando i vuoti da e per la base, e le
dieci ore di impegno, 14:00-24:00. La giornata del conducente va dalle 13:00 (partenza dalla
base) all'01:00 circa: dodici ore, dentro i limiti ma senza margine.

Quotare i tre trasferimenti come corse separate avrebbe portato il prezzo intorno ai € 550
a mezzo, cioè sotto il costo reale della giornata. È l'errore da non fare.

## Margine

- **Beluga:** costo diretto € 250-350. Su € 1.150 il margine è pieno.
- **Tourengo:** non è di GiroMunna, il costo va concordato con Francesco. Se resta entro gli
  € 700-800 per una giornata di questo profilo, il margine sul secondo mezzo è € 350-450.
  **Se sfora gli € 800, il prezzo di vendita del secondo mezzo va portato a € 1.250** e i PDF
  vanno rigenerati.

## La capienza: GiroMunna mette due mezzi e basta

Il cliente ha indicato **80-100 persone**. I due mezzi fanno **54 posti** (26 + 28), e con un
limite stretto di 25 a mezzo scendono a 50.

Il preventivo lo dice in chiaro, senza giri di parole: **mettiamo a disposizione il Beluga e
il Tourengo, e nient'altro.** Per i passeggeri oltre i 54 il cliente ha due strade, ed è lui
a scegliere:

1. **Se li organizza da solo.** È la strada che il preventivo mette per prima.
2. **Ce lo fa sapere e vediamo se riusciamo a trovarli.** In quel caso è un preventivo a
   parte, da costruire dopo aver sentito Francesco: qui non c'è nessun impegno e nessun
   prezzo, giusto la disponibilità a guardarci.

**L'ipotesi dei due turni con i soli Beluga e Tourengo è stata esclusa** e nel preventivo si
spiega perché: fra il primo e l'ultimo trasferimento la giornata dei conducenti è già di
dodici ore e raddoppiare le corse la porterebbe oltre i limiti di guida. Meglio dirlo subito
che trovarselo addosso la sera del 9 ottobre.

Il numero definitivo dei passeggeri serve comunque, per confermare come si ripartiscono sui
due minibus.

## Verifiche di accesso

- **Firenze, Via dei Conti 9 — il problema più grosso dopo la capienza.** House of Nine sta a
  due passi dal Duomo, in piena ZTL, su una strada dove un minibus da otto metri non può
  fermarsi a caricare. Nel preventivo è proposto il carico in **Via Valfonda o Piazza Adua**,
  dietro Santa Maria Novella, dove la sosta bus è autorizzata: 400 m dall'albergo, cinque
  minuti a piedi, nessun onere. Se il cliente insiste sull'ingresso in centro serve il
  permesso comunale bus turistici, ~€ 350 a mezzo: **non è nel totale**, va richiesto e
  addebitato al costo.
- **Villa Medicea di Lilliano (Grassina):** fuori ZTL, nessun onere. Via Lilliano e Meoli
  sale da Grassina per circa un chilometro ed è stretta. Da confermare: punto di discesa e
  sosta dalle 15:00 alle 18:00.
- **Tenuta Bossi (Pontassieve):** fuori ZTL, nessun onere. Via dello Stracchino sale da
  Pontassieve. Da confermare: punto di discesa, spazio di manovra e sosta dalle 18:45 alle
  23:00, con ripartenza al buio.
- Nessun permesso di Siena e nessun parcheggio aeroportuale: non sono toccati.

## Da chiarire prima di inviare

1. **La capienza.** 80-100 persone contro 54 posti. Il preventivo dice che mettiamo due mezzi
   e basta: gli altri se li organizza il cliente, oppure ce lo fa sapere e si vede. Se chiede
   a noi, il preventivo per i mezzi in più si fa a parte, dopo aver sentito Francesco.
2. **Francesco.** Costo del Tourengo per il 9 ottobre, giornata 14:00-24:00 con chiusura a
   mezzanotte. Il preventivo dice al cliente che i due mezzi sono liberi: va confermato
   **prima** di inviare, non dopo.
3. **Dotazione del Tourengo.** Nel PDF è descritto con aria condizionata, sedili reclinabili,
   impianto audio e vano bagagli. Il frigo bar non è indicato perché non confermato: se c'è,
   si aggiunge e si rigenerano i PDF.
4. **Punto di carico a Firenze.** Da far scegliere al cliente: Via Valfonda / Piazza Adua
   (nessun costo) oppure Via dei Conti con il permesso bus a ~€ 350 a mezzo.
5. **Nome esatto dell'intestatario.** Quotato «House of Nine»: se la richiesta arriva da una
   wedding planner o da un'agenzia, rigenerare i PDF con `--cliente`.
6. **Orario di partenza da Tenuta Bossi.** Le 23:00 di una festa slittano quasi sempre. Nel
   preventivo la partenza si può spostare fino alle 00:30 senza sovrapprezzo, ma solo se
   deciso alla conferma. Attesa oltre l'orario € 50/h a mezzo (€ 100/h per i due), rientro
   dopo le 02:00 € 250 a mezzo (€ 500 per i due).
7. **Bloccare la disponibilità** del Beluga per il 9 ottobre.

## Nel preventivo non si specifica di chi sono i mezzi

Il cliente vede due minibus GiroMunna, Beluga e Tourengo, descritti allo stesso modo: non
c'è nessun accenno a quale sia di proprietà e quale venga da fuori. La provenienza e i costi
di acquisto restano in queste note.

## Vitto e alloggio dei conducenti

Con gli orari in programma **non servono**: il servizio si chiude a Firenze verso le 23:40 e
i conducenti rientrano alla base intorno all'01:00. Nel preventivo la voce è comunque
indicata, sia nella tabella del prezzo sia fra il non incluso, perché diventa dovuta — e a
carico del cliente — se il rientro slitta ben oltre le 02:00.

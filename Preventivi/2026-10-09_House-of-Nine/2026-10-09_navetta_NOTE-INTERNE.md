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
| Minibus 1 — Beluga, 25+1+1, i tre trasferimenti, a disposizione 14:00-24:00 | € 900,00 |
| Minibus 2 — Tourengo, 27+1+1, stesso servizio | € 900,00 |
| Permesso di accesso al centro di Firenze, giornata del 9 ottobre, entrambi i mezzi | € 421,00 |
| Vitto e alloggio conducenti | non necessario |

**Totale netto € 2.221,00 · IVA 10% € 222,10 · Totale € 2.443,10**
(a pieno carico sui 52 posti, ≈ € 47,00 a persona)

Acconto 30% € 732,93 — saldo € 1.710,17.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo, e la scala di Alvora.
**Non** il Corte Francigena diviso per due: quegli importi sono già scontati per volume.

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento ~50 km | € 500,00 |
| Le Filigare — giornata a disposizione, ~80 km, 5 h | € 809,00 |
| Alvora — giornata a disposizione, 140 km, 8 h | € 980,00 |
| 9 ottobre — quanto varrebbe secondo la scala: ~190 km, 10 h, chiusura a mezzanotte | € 1.150,00 |
| **Prezzo deciso da Girolamo, per mezzo** | **€ 900,00** |
| **Permesso di accesso a Firenze, ribaltato al cliente** | **€ 421,00** |

**Il punto chiave: non sono tre corse, è una giornata a disposizione.** Fra il primo e il
secondo trasferimento passano quasi tre ore, fra il secondo e il terzo più di quattro, e la
base è a 55 km da Firenze: i mezzi non rientrano, restano fermi tutto il pomeriggio e tutta
la sera con i conducenti. Da qui i ~190 km per mezzo contando i vuoti da e per la base, e le
dieci ore di impegno, 14:00-24:00. La giornata del conducente va dalle 13:00 (partenza dalla
base) all'01:00 circa: dodici ore, dentro i limiti ma senza margine.

Quotare i tre trasferimenti come corse separate avrebbe portato il prezzo intorno ai € 550
a mezzo, cioè sotto il costo reale della giornata. È l'errore da non fare.

## Margine

Il prezzo di **€ 900 a mezzo è una decisione di Girolamo**. Sta sotto la scala di riferimento
(Le Filigare: € 809 per 80 km e 5 ore, mentre qui la giornata è di dieci ore e ~190 km).
Registrato qui perché resti agli atti, non per rimetterlo in discussione.

- **Beluga:** costo diretto € 250-350. Su € 900 il margine resta buono, € 550-650.
- **Tourengo:** non è di GiroMunna, il costo va concordato con Francesco. A € 600-800 di
  acquisto il margine sul secondo mezzo scende a **€ 100-300**: sottile.
  **Se Francesco chiede più di € 800, il secondo mezzo va in pari o sotto.** In quel caso o si
  rinegozia con lui, o si rivede il prezzo con Girolamo.
- **Permesso Firenze € 421:** ribaltato al cliente in fattura, con IVA 10% come il resto del
  servizio. Non è un margine, è una partita di giro: va verificato che l'importo effettivo
  del permesso sia davvero quello, altrimenti la differenza la paghiamo noi.

## Il permesso di Firenze e le 23:00

Il permesso di accesso al centro vale per **la giornata del 9 ottobre**. Partendo da Tenuta
Bossi alle 23:00 si rientra a Firenze verso le 23:40, dentro la giornata: un solo permesso.
Se la partenza slitta si entra in città dopo la mezzanotte, quindi il 10 ottobre, e **serve
un secondo permesso da € 421**.

Per questo nel preventivo **le 23:00 sono un orario tassativo** e non più spostabile: la
versione precedente concedeva lo slittamento fino alle 00:30 senza sovrapprezzo, ed è stata
tolta. Al cliente il motivo è scritto per esteso, con la cifra: è l'argomento più efficace per
far rispettare l'orario a una festa.

## La capienza: GiroMunna mette due mezzi e basta

Il cliente ha indicato **80-100 persone**. I due mezzi fanno **52 posti passeggeri**: il Beluga è
omologato **25+1+1** e il Tourengo **27+1+1**, quindi 25 + 27. Se una delle due strutture
impone un limite di 25 persone a mezzo, si scende a 50.

Il preventivo lo dice in chiaro, senza giri di parole: **mettiamo a disposizione il Beluga e
il Tourengo, e nient'altro.** Per i passeggeri oltre i 52 il cliente ha due strade, ed è lui
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

- **Firenze, Via dei Conti 9.** House of Nine sta a due passi dal Duomo, in piena ZTL. Il
  permesso comunale di accesso è **compreso nel preventivo a € 421** e lo richiediamo noi.
  Resta da concordare con il cliente il punto esatto della fermata, perché Via dei Conti è
  stretta e il carico di un gruppo numeroso vuole qualche minuto di sosta. Se non c'è modo di
  fermarsi davanti all'ingresso, l'alternativa indicata nel preventivo è **Via Valfonda o
  Piazza Adua**, dietro Santa Maria Novella, 400 m a piedi.
- **Villa Medicea di Lilliano (Grassina):** fuori ZTL, nessun onere. Via Lilliano e Meoli
  sale da Grassina per circa un chilometro ed è stretta. Da confermare: punto di discesa e
  sosta dalle 15:00 alle 18:00.
- **Tenuta Bossi (Pontassieve):** fuori ZTL, nessun onere. Via dello Stracchino sale da
  Pontassieve. Da confermare: punto di discesa, spazio di manovra e sosta dalle 18:45 alle
  23:00, con ripartenza al buio.
- Nessun permesso di Siena e nessun parcheggio aeroportuale: non sono toccati.

## Da chiarire prima di inviare

1. **La capienza.** 80-100 persone contro 52 posti. Il preventivo dice che mettiamo due mezzi
   e basta: gli altri se li organizza il cliente, oppure ce lo fa sapere e si vede. Se chiede
   a noi, il preventivo per i mezzi in più si fa a parte, dopo aver sentito Francesco.
2. **Francesco.** Costo del Tourengo per il 9 ottobre, giornata 14:00-24:00 con chiusura a
   mezzanotte. Il preventivo dice al cliente che i due mezzi sono liberi: va confermato
   **prima** di inviare, non dopo.
3. **Dotazione del Tourengo.** Nel PDF è descritto con aria condizionata, sedili reclinabili,
   impianto audio e vano bagagli. Il frigo bar non è indicato perché non confermato: se c'è,
   si aggiunge e si rigenerano i PDF.
4. **Punto di carico a Firenze.** Il permesso è già nel prezzo: resta da concordare con il
   cliente il punto esatto della fermata in Via dei Conti, o in alternativa Via Valfonda /
   Piazza Adua. **Verificare l'importo effettivo del permesso**: a preventivo sono € 421 e
   la differenza, se c'è, la paghiamo noi.
5. **Nome esatto dell'intestatario.** Quotato «House of Nine»: se la richiesta arriva da una
   wedding planner o da un'agenzia, rigenerare i PDF con `--cliente`.
6. **Orario di partenza da Tenuta Bossi.** Le 23:00 sono tassative e nel preventivo è scritto
   perché: oltre quell'ora serve il secondo permesso da € 421. Attesa oltre l'orario € 50/h a
   mezzo (€ 100/h per i due), rientro dopo le 02:00 € 250 a mezzo (€ 500 per i due).
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

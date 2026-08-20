# Note interne — Navetta 9 ottobre 2026, 80-100 pax, quattro minibus

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

---

## Il programma

Venerdì 9 ottobre 2026, tre trasferimenti nella stessa giornata.

| | Ora | Percorso | Stima |
|---|---|---|---|
| 1 | 14:30 | Firenze, House of Nine (Via dei Conti 9) → Villa Medicea di Lilliano, Grassina | 12 km · 35 min |
| 2 | 18:00 | Villa Medicea di Lilliano → Tenuta Bossi, Marchesi Gondi, Pontassieve | 25 km · 45 min |
| 3 | 23:00 | Tenuta Bossi → Firenze, House of Nine | 22 km · 35 min |

Richiesta del cliente: mezzi da **massimo 20-25 posti** su tutti e tre i trasferimenti.
Con 80-100 persone servono **quattro minibus**, e il numero non è una nostra iniziativa:
è la richiesta stessa a imporlo.

## Prezzi

| Voce | Netto |
|---|---|
| Minibus 1 — Beluga, i tre trasferimenti, a disposizione 14:00-24:00 | € 1.150,00 |
| Minibus 2 — stesso servizio | € 1.150,00 |
| Minibus 3 — stesso servizio | € 1.150,00 |
| Minibus 4 — stesso servizio | € 1.150,00 |
| Vitto e alloggio conducenti | non necessario |

**Totale netto € 4.600,00 · IVA 10% € 460,00 · Totale € 5.060,00**
(≈ € 51,00 a persona su 100 ospiti, ≈ € 63,00 su 80)

Acconto 30% € 1.518,00 — saldo € 3.542,00.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo, e la scala di Alvora.
**Non** il Corte Francigena diviso per due: quegli importi sono già scontati per volume e qui
tre mezzi su quattro si comprano da Francesco, quindi hanno un costo vero da coprire.

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
a mezzo, cioè **sotto il costo dei tre mezzi comprati da Francesco**. È l'errore da non fare.

## Margine

- **Beluga (mezzo di proprietà):** costo diretto € 250-350. Su € 1.150 il margine è pieno.
- **Gli altri tre:** acquisto da Francesco stimato € 600-800 per una giornata di questo
  profilo, con chiusura a mezzanotte. A € 1.150 di vendita restano € 350-550 a mezzo.
- Margine complessivo stimato: € 1.850-2.450 su € 4.600.

**Se Francesco sfora gli € 800 a mezzo, il prezzo di vendita va portato a € 1.250** (totale
netto € 5.000, totale IVA inclusa € 5.500), rigenerando i PDF.

## Verifiche di accesso

- **Firenze, Via dei Conti 9 — il problema più grosso.** House of Nine sta a due passi dal
  Duomo, in piena ZTL, su una strada dove un minibus da otto metri non può fermarsi a
  caricare: figurarsi quattro con cento persone. Nel preventivo è proposto il carico in
  **Via Valfonda o Piazza Adua**, dietro Santa Maria Novella, dove la sosta bus è
  autorizzata: 400 m dall'albergo, cinque minuti a piedi, nessun onere. Se il cliente
  insiste sull'ingresso in centro serve il permesso comunale bus turistici, ~€ 350 a mezzo
  (quindi ~€ 1.400 per quattro): **non è nel totale**, va richiesto e addebitato al costo.
- **Villa Medicea di Lilliano (Grassina):** fuori ZTL, nessun onere. Via Lilliano e Meoli
  sale da Grassina per circa un chilometro ed è stretta — è il motivo del limite dei 25
  posti. Da confermare: punto di discesa e sosta di quattro mezzi dalle 15:00 alle 18:00.
- **Tenuta Bossi (Pontassieve):** fuori ZTL, nessun onere. Via dello Stracchino sale da
  Pontassieve. Da confermare: punto di discesa, spazio di manovra e sosta dalle 18:45 alle
  23:00, con ripartenza al buio.
- Nessun permesso di Siena e nessun parcheggio aeroportuale: non sono toccati.

## Da chiarire prima di inviare

1. **Francesco.** Disponibilità di tre minibus 24-25 posti per il 9 ottobre e prezzo
   all'ingrosso. Il preventivo dice al cliente che i mezzi sono liberi: va confermato
   **prima** di inviare, non dopo.
2. **Il secondo minibus di famiglia.** Se il Tourengo entra come mezzo 2, il costo va
   concordato con Francesco. La decisione è di Girolamo: nel PDF non è nominato.

   **Nel preventivo non si specifica di chi sono i mezzi.** Il cliente vede quattro minibus
   GiroMunna, tutti della stessa classe: non c'è nessun accenno a quale sia di proprietà e
   quali vengano da fuori. La provenienza e i costi di acquisto restano in queste note.
3. **Punto di carico a Firenze.** Da far scegliere al cliente: Via Valfonda / Piazza Adua
   (nessun costo) oppure Via dei Conti con il permesso bus a ~€ 350 a mezzo.
4. **Nome esatto dell'intestatario.** Quotato «House of Nine»: se la richiesta arriva da una
   wedding planner o da un'agenzia, rigenerare i PDF con `--cliente`.
5. **Numero passeggeri.** 80-100 è una forbice da venti persone. Quattro mezzi fanno circa
   cento posti: a cento ospiti sono pieni, senza un posto per l'ospite dell'ultimo minuto o
   per chi organizza. Sopra i 96 serve il quinto minibus, € 1.150 + IVA. Numero definitivo
   chiesto entro il 24 settembre.
6. **Orario di partenza da Tenuta Bossi.** Le 23:00 di una festa slittano quasi sempre. Nel
   preventivo la partenza si può spostare fino alle 00:30 senza sovrapprezzo, ma solo se
   deciso alla conferma: oltre quell'ora la giornata dei conducenti sfora e servirebbe un
   secondo turno. Attesa oltre l'orario € 50/h a mezzo (€ 200/h per la flotta), rientro dopo
   le 02:00 € 250 a mezzo (€ 1.000 per la flotta). È il rischio economico principale della
   giornata: meglio fissare l'orario vero adesso.
7. **Due turni di rientro.** Offerti nel preventivo: due mezzi alle 23:00 e tutti e quattro
   alle 00:30, con € 350 + IVA per ciascuno dei due mezzi che fanno il doppio viaggio.
   Da concordare con i conducenti se il cliente lo chiede.
8. **Bloccare la disponibilità** del Beluga per il 9 ottobre.

## Vitto e alloggio dei conducenti

Con gli orari in programma **non servono**: il servizio si chiude a Firenze verso le 23:40 e
i conducenti rientrano alla base intorno all'01:00. Nel preventivo la voce è comunque
indicata, sia nella tabella del prezzo sia fra il non incluso, perché diventa dovuta — e a
carico del cliente — se il rientro slitta ben oltre le 02:00. In quel caso servono quattro
camere a Firenze, che il cliente prenota e paga direttamente.

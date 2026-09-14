# Note interne — Serata di compleanno 19.09.2026, 10 ragazzi

**Cliente:** Girolamo Munna (per il figlio) · **Rif. preventivo:** GM-2026-0919-PM ·
**Preparato:** 14 settembre 2026

File generati:
- `GiroMunna_Preventivo_Compleanno_19_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Compleanno_19_settembre_2026_EN.pdf`
- `genera_preventivo_compleanno.py` — rigenera entrambi i PDF
- `preventivo_compleanno_19_settembre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-19_Munna/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_compleanno.py --lingua it --cliente "Nome"
python3 genera_preventivo_compleanno.py --lingua en --cliente "Name"
```

---

## La richiesta

Sabato 19 settembre, compleanno di 16 anni del figlio di Girolamo. Gruppo di 10 ragazzi.
Partenza da Prato verso le 23:00, destinazione Piazzale Michelangelo a Firenze, rientro a
Prato verso le 03:00 di notte.

Nessun nome del festeggiato è stato indicato nella richiesta ("mio figlio"): il preventivo
è intestato a Girolamo Munna come referente. Da correggere se serve un altro nominativo
prima di consegnarlo.

## Prezzi

| Servizio | Netto |
|---|---|
| Serata a disposizione: Prato → Piazzale Michelangelo → Prato, ore 23:00-03:00 circa | € 480,00 |
| Supplemento rientro dopo le 02:00 (per mezzo) | € 250,00 |
| Permesso ZTL Bus per la sosta a Piazzale Michelangelo — confermato da Girolamo | € 415,00 |

**Totale netto € 1.145,00 · IVA 10% € 114,50 · Totale € 1.259,50** (≈ € 125,95 a persona)

Acconto 30% € 377,85 — saldo € 881,65, richiesto entro il 18 settembre invece dei soliti
termini più lunghi, vista la vicinanza della data.

## Come è stato costruito il prezzo

Riferimento: il preventivo **Le Filigare** (GM-2026-0821-LF), a mezzo singolo come questo:

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Le Filigare — giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |
| Alvora — serata a disposizione Chianti, ~80 km andata/ritorno, 6 ore | € 680,00 |

Questo lavoro è più vicino a una "serata a disposizione" corta che a una giornata piena:
partenza alle 23:00, ~20 km fino a Piazzale Michelangelo, attesa sul posto, rientro verso
le 03:00. Scalando la serata di Alvora (80 km, 6 ore, € 680) sulla distanza e sui tempi di
questo lavoro (~40-50 km andata/ritorno, 4 ore) si ottiene una base fra € 400 e € 460.
Tenendo il prezzo alto, come da regola quando c'è incertezza, la base è stata fissata a
€ 480,00.

A questa si aggiunge il supplemento fisso di **€ 250,00 per il rientro dopo le 02:00**,
una delle condizioni ricorrenti indicate in CLAUDE.md: qui non è una contingenza da
segnalare come possibile, è già il programma richiesto (rientro a Prato verso le 03:00),
quindi va messo a preventivo come importo effettivo, non solo citato fra le condizioni.
Da non confondere con l'attesa oraria di € 50,00/ora: non c'è ritardo, è l'orario stesso
concordato con il cliente.

## Margine

Lavoro sul mezzo di proprietà (Beluga), nessun pernottamento del conducente da coprire,
percorso breve e noto (Prato-Firenze, ~20 km): costo diretto stimato contenuto, margine
buono sui € 1.145,00 netti.

## Verifiche di accesso — corrette dopo la prima stesura

**Nella prima versione avevo sbagliato**: avevo scritto che Piazzale Michelangelo, non
essendo nel centro storico, non richiedesse alcun permesso. Girolamo ha segnalato che a
Firenze "si paga il check point" e aveva ragione. Verificato:

- La **ZTL Bus** del Comune di Firenze copre l'intero centro abitato (non solo il centro
  storico, anche il quartiere di Galluzzo), attiva 24 ore su 24, tutti i giorni.
- La sosta per salita/discesa a Piazzale Michelangelo rientra nella zona regolamentata:
  serve il permesso online (il "check point", ora gestito solo via portale, non più ai
  varchi fisici).
- Fonti: [Servizi alla Strada — autorizzazioni circolazione e sosta autobus](https://www.serviziallastrada.it/servizi-al-turista/autorizzazioni-circolazione-e-sosta-autobus),
  [Feel Florence — bus turistici](https://www.feelflorence.it/en/editorial-staff/tourist-coaches-arriving-florence-ztl-bus),
  [Servizi alla Strada — Parcheggi salite/discese](https://www.serviziallastrada.it/servizi-al-turista/autorizzazioni-circolazione-e-sosta-autobus/parcheggi-salitediscese)
  (a Piazzale Michelangelo salita/discesa 24/24, sosta max 20 minuti, accesso da Viale
  Galileo/Viale Michelangelo).
- **Tariffa confermata da Girolamo: € 415,00** per il nostro minibus. Più alta della stima
  iniziale trovata online (€ 235,00, per un generico mezzo Euro VI ≤ 8 m, "tipo G
  ordinario") — verosimilmente la nostra categoria di permesso o classe emissioni reale
  porta a una fascia diversa; la forbice ufficiale delle tariffe (€ 110-760) è comunque
  ampia. Il preventivo ora riporta i € 415,00 come importo definitivo, non più stimato.

## Da chiarire prima di consegnare

1. **Nome del festeggiato/cliente** — arrivato solo come "mio figlio". Il preventivo è
   intestato a Girolamo Munna: correggere se serve un nome diverso.
2. **Indirizzo esatto di partenza a Prato.**
3. **Punto di sosta preciso del mezzo** a Piazzale Michelangelo durante l'attesa.
4. **Recapito di un genitore/accompagnatore di riferimento per la serata**, trattandosi di
   un gruppo di soli minorenni.
5. **Tempi stretti** — mancano solo 5 giorni al servizio (oggi 14, servizio il 19): la
   prenotazione ricade già nella fascia di cancellazione più stretta (ultimi 10 giorni,
   100% in caso di disdetta). Conviene bloccare la disponibilità del mezzo e acquistare il
   permesso ZTL Bus appena possibile.

## Promemoria

Per istruzione di lavoro (CLAUDE.md): il documento consegnato è il PDF in italiano e
inglese dentro questa cartella. Non è stata preparata né inviata alcuna mail — a quello
pensa Girolamo con i suoi tempi.

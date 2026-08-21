# Note interne — Cinque Terre 11.10.2026, 10 pax

**Cliente:** Viaggi Tigullio Marcone (Fabio Marcone) · **Rif. preventivo:** GM-2026-1011-VT ·
**Preparato:** 21 agosto 2026 · **Validità:** 4 settembre 2026

File generati:
- `GiroMunna_Preventivo_Cinque_Terre_11_ottobre_2026_IT.pdf`
- `2026-10-11_mail-risposta-a-Marcone.md` — il testo della mail, da copiare e inviare
- `genera_preventivo_cinque_terre.py` — rigenera il PDF
- `preventivo_cinque_terre_11_ottobre_2026.html` — la pagina web di lavoro

**Solo italiano: Viaggi Tigullio Marcone è un'agenzia italiana e scrive in italiano.** La
versione inglese del PDF non serve ed è stata tolta; se un domani servisse, la rigenera lo
script con `--lingua en`.

Tutto dentro `Preventivi/2026-10-11_Viaggi-Tigullio-Marcone/`.

Il cliente è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_cinque_terre.py --lingua it
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## La richiesta

Domenica 11 ottobre 2026, 10 passeggeri americani senza bagagli, escursione di una giornata
alle Cinque Terre. Da Nievole — Villa Ginevra alla stazione della Spezia Migliarina, dove la
guida dell'agenzia attende il gruppo. Partenza ore 8:00, ritorno ore 18:00 circa.
Chiesto un 20-22 posti gran turismo. **Budget indicato dal cliente: € 700 + IVA 10%.**

## Prezzo

| Data | Servizio | Netto |
|---|---|---|
| Dom 11 ott | Nievole → La Spezia Migliarina, giornata a disposizione e rientro (~220 km, 8:00-19:45) | € 800,00 |
| — | Vitto del conducente durante la sosta | a carico del cliente |

**Totale netto € 800,00 · IVA 10% € 80,00 · Totale € 880,00** (€ 88,00 a persona)

Acconto 30% € 264,00 — saldo € 616,00.

Prezzo **deciso da Girolamo il 21 agosto**. La prima stesura era a € 1.250,00 netti, cioè quanto
la giornata vale sulla scala della casa: il confronto è più sotto e va tenuto, perché serve la
prossima volta. I chilometri di questa scheda restano qui e non escono: al cliente non si danno.

Nessun pernottamento: il servizio si apre e si chiude in giornata. Resta a carico del cliente
il solo pasto del conducente durante le ore di sosta alla Spezia, indicato a preventivo ma non
conteggiato, come da regola della casa.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come questo. Il Corte
Francigena non si usa: i suoi importi sono per mezzo su un lavoro a due mezzi, già scontati per
volume.

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento ~50 km | € 500,00 |
| Le Filigare — giornata a disposizione, ~80 km, 5 h | € 809,00 |
| Alvora — giornata a disposizione, 115 km, 8 h | € 980,00 |
| Alvora — giornata lunga, 237 km, 8 h 30 | € 1.250,00 |
| **Cinque Terre — 220 km, 11 h 45** | **€ 1.250,00** |

È la giornata più lunga come impegno del conducente di tutte quelle quotate finora — quasi
dodici ore, dalle 8:00 alle 19:45 — e la seconda per chilometri. Però è una tratta autostradale
semplice con una lunga sosta in mezzo, senza tappe da girare: per questo si allinea alla
giornata lunga di Alvora invece di stare sopra.

## Margine

Costo diretto stimato **€ 450-500**: gasolio e pedaggi per 220 km, ticket di accesso e sosta bus
alla Spezia, giornata del conducente. A **€ 800 netti restano € 300-350** per una domenica intera
con il mezzo bloccato, che non può fare altro.

Il pavimento calcolato sulla scala della casa era € 900 netti e la giornata ne varrebbe € 1.250:
Girolamo è sceso a € 800 per restare vicino al budget dell'agenzia. **Questo prezzo non è un
riferimento da ripetere**: se Viaggi Tigullio Marcone torna con richieste simili, si riparte
dalla scala, non da € 800.

**La giornata va fatta con il mezzo di proprietà.** Subappaltandola a Francesco il costo si
colloca sui € 600-700 e a € 800 non resta praticamente niente.

## Verifiche fatte

- **Percorso.** Nievole → La Spezia Migliarina circa 110 km per A11 e A12; in auto sono ~1 h 10,
  con un bus e l'ingresso in città si sta su 1 h 40. Andata e ritorno circa 220 km.
- **Migliarina.** Dal 2025 è l'hub del Cinque Terre Express: binario dedicato (1 Nord) e 35
  collegamenti al giorno verso Levanto e le Cinque Terre, più il piazzale rifatto. La scelta
  della guida è quella giusta e il piazzale è più comodo della Spezia Centrale per un mezzo
  turistico.
- **Sosta alla Spezia.** Il Comune applica un ticket per la salita e discesa dei passeggeri e
  tariffe di sosta per i bus turistici (aree di Piazza Pozzoli al Canaletto e dell'ex area IP).
  Costo modesto, già compreso nel prezzo: al cliente non si fa pagare niente sul posto.
- **Permessi.** Né Villa Ginevra né Migliarina comportano permessi ulteriori. Il centro storico
  della Spezia non viene toccato.
- **Cancellazione.** Mancano 51 giorni al servizio: si è già nella fascia 60-30 giorni (acconto
  trattenuto), e dall'11 settembre si passa alla fascia 30-10 giorni (50%).

## Da chiarire prima di inviare

1. **Le «ore 18 circa».** Ripartenza da La Spezia o rientro a Nievole? È quotata la prima
   lettura, la più impegnativa; se sono le 18:00 a Nievole il ritrovo si sposta alle 16:15 e il
   prezzo resta lo stesso. Nel preventivo la domanda è posta esplicitamente.
2. **Indirizzo esatto di Villa Ginevra** e punto di carico del gruppo: con 7,64 m si arriva quasi
   ovunque, ma meglio saperlo prima.
3. **Recapito telefonico della guida** che attende a Migliarina, per il coordinamento diretto con
   il conducente sia all'arrivo sia al ritorno.
4. **Bloccare la disponibilità del mezzo** per domenica 11 ottobre.

## Aggiornamento 21 agosto — decisione sul prezzo e mail al cliente

Girolamo ha fissato il prezzo a **€ 800,00 + IVA** (€ 880,00 IVA inclusa) e ha chiesto il testo
della mail che lo comunica al cliente: `2026-10-11_mail-risposta-a-Marcone_IT-EN.md`, italiano e
inglese. Nessuna bozza creata in Gmail, niente inviato: la mail la manda lui.

**Il PDF e la pagina web sono stati rigenerati a € 800**, quindi mail e preventivo ora dicono
la stessa cifra e si possono mandare insieme. Nel preventivo la nota sul budget è stata riscritta:
non parla più di metà giornata, dice che € 800 + IVA è il minimo al quale la giornata si può
fare, non un prezzo di partenza.

**Tolti i chilometri da tutto il materiale che va al cliente** — PDF, pagina web e testo della
mail. Restano solo in questa scheda e nei blocchi interni della pagina web. La regola è ora
scritta nel CLAUDE.md.

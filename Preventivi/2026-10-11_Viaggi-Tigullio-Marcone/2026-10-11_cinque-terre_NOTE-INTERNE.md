# Note interne — Cinque Terre 11.10.2026, 10 pax

**Cliente:** Viaggi Tigullio Marcone (Fabio Marcone) · **Rif. preventivo:** GM-2026-1011-VT ·
**Preparato:** 21 agosto 2026 · **Validità:** 4 settembre 2026

File generati:
- `GiroMunna_Preventivo_Cinque_Terre_11_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Cinque_Terre_11_ottobre_2026_EN.pdf`
- `genera_preventivo_cinque_terre.py` — rigenera entrambi i PDF
- `preventivo_cinque_terre_11_ottobre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-10-11_Viaggi-Tigullio-Marcone/`.

Il cliente è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_cinque_terre.py --lingua it
python3 genera_preventivo_cinque_terre.py --lingua en
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
| Dom 11 ott | Nievole → La Spezia Migliarina, giornata a disposizione e rientro (~220 km, 8:00-19:45) | € 1.250,00 |
| — | Vitto del conducente durante la sosta | a carico del cliente |

**Totale netto € 1.250,00 · IVA 10% € 125,00 · Totale € 1.375,00** (€ 137,50 a persona)

Acconto 30% € 412,50 — saldo € 962,50.

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

## Margine e pavimento

Costo diretto stimato **€ 450-500**: gasolio e pedaggi per 220 km, ticket di accesso e sosta bus
alla Spezia, giornata del conducente. Con il mezzo di proprietà, a € 1.250 il margine è buono.

**Il pavimento è € 900 netti.** Sotto quella cifra una domenica intera bloccata — con il mezzo
che non può fare altro — non vale la pena. Il budget del cliente, € 700, è sotto il pavimento:
coprirebbe poco più della metà della giornata.

**Se il cliente insiste sul budget**, meglio non fare lo sconto secco: Viaggi Tigullio Marcone è
un'agenzia che lavora in continuità, quindi conviene rispondere con il pacchetto — altri
trasferimenti o escursioni nello stesso periodo — e tenere il prezzo di questa giornata.
Se proprio si deve scendere, non oltre € 900 netti.

Se invece la giornata si subappalta a Francesco, il costo si colloca sui € 600-700 e a € 1.250
il margine resta accettabile ma non brillante: in quel caso il pavimento sale a € 1.000.

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

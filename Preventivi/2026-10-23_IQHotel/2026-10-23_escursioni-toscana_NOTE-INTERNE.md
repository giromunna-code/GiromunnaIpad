# Note interne — Escursioni da Firenze (iQ Hotel), 23 e 24.10.2026, 10 pax

**Cliente:** gruppo di circa 10 donne ospiti all'iQ Hotel Firenze (Via Lorenzo il Magnifico 2)
dal 22 al 25 ottobre — nome, mail e telefono da completare.
**Rif. preventivo:** GM-2026-1023-IQ · **Preparato:** 15 ottobre 2026 · **Validità:** 17 ottobre 2026

File generati:
- `GiroMunna_Preventivo_Escursioni_Toscana_23-24_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Escursioni_Toscana_23-24_ottobre_2026_EN.pdf`
- `genera_preventivo_escursioni_toscana.py` — rigenera entrambi i PDF
- `MAIL.md` — testo del messaggio (WhatsApp o mail), italiano e inglese

Quando si sa il nome della cliente, rigenerare con:

```bash
python3 genera_preventivo_escursioni_toscana.py --lingua it --cliente "Nome Cognome"
python3 genera_preventivo_escursioni_toscana.py --lingua en --cliente "Nome Cognome"
```

## Richiesta

Prima richiesta: due preventivi, solo minibus e minibus più cantina prenotata da noi, con
veicolo da 10 posti. Girolamo ha risposto su WhatsApp, senza prezzi: il mezzo più piccolo è
da 25 posti, **GiroMunna non prenota le cantine**, le consiglia soltanto. La cliente ha
accettato e chiede un preventivo per le due giornate, partenza e rientro all'iQ Hotel,
tutto compreso. Il preventivo è quindi **solo minibus**; nelle note ci sono tre cantine
consigliate (Antinori Bargino, Badia a Passignano, Castello di Verrazzano), scelta e
prenotazione a loro.

## Prezzi

| Voce | Netto |
|---|---|
| Ven 23/10 Firenze – Pisa – Lucca – Firenze, 9 ore, ~190 km | € 1.150,00 |
| Sab 24/10 Firenze – Siena – San Gimignano – Chianti – Firenze, 10 ore, ~180 km | € 1.250,00 |
| Permessi bus (vedi sotto) | € 1.320,00 |
| Pranzo conducente | a carico del cliente |
| **Totale netto** | **€ 3.720,00** |

IVA 10% € 372,00 · **Totale € 4.092,00** — acconto € 1.227,60, saldo € 2.864,40.

Come sono costruiti: base Le Filigare (giornata 80 km / 5 ore € 809). Qui le giornate sono
di 9 e 10 ore, ~190 e ~180 km di servizio più ~110 km di vuoto da e per Ponte Buggianese ogni
giorno (12 ore circa di impegno del conducente). Alvora aveva € 980 per 8 ore senza vuoto.
€ 1.150 e € 1.250 stanno nella fascia alta, come da regola.

## Permessi bus — stime da verificare

Online non ho trovato le tariffe aggiornate di Pisa, Lucca e San Gimignano (i siti dei comuni
e l'elenco ANAV non erano raggiungibili). Ho messo:

| Città | Stima | Fonte |
|---|---|---|
| Firenze, check point, 2 giornate | € 842 | dato di Girolamo, € 421/giorno |
| Pisa, parcheggio bus via Pietrasantina | € 100 | stima |
| Lucca, check point bus (pagamento online LuccaPlus) | € 100 | stima |
| Siena, permesso bus | € 160 | CLAUDE.md |
| San Gimignano, parcheggio bus Montemaggio | € 120 | La Nazione: € 120 online, € 190 sul posto (alta stagione) |
| **Totale** | **€ 1.322 → arrotondato € 1.320** | |

Se Girolamo conosce le tariffe vere, correggere la riga e i totali.

**Margine di trattativa sul check point di Firenze (€ 842):** è il costo più pesante. Se la
cliente chiede uno sconto, si può proporre il ritrovo fuori dall'area bus (per esempio Villa
Costanza, raggiungibile con la tramvia T1 dalla fermata Fortezza, a pochi passi dall'hotel):
si risparmiano € 926 IVA inclusa. Per un gruppo così però il ritiro in hotel è il punto del
servizio: l'ho lasciato compreso.

## Da verificare

1. **Disponibilità del Beluga 23–24 ottobre.** Nel PDF e nella mail ho scritto che è libero:
   nei preventivi del repository non risultano lavori in quelle date, ma va confermato.
2. **Tariffe dei permessi** di Pisa, Lucca e San Gimignano.
3. **Tempi stretti.** Il servizio è fra 8 giorni: siamo negli ultimi 10 giorni, quindi dopo
   la conferma la cancellazione è al 100%. Validità messa al 17 ottobre e saldo entro il 22.
4. **Ore del conducente.** Sabato: partenza dalla base verso le 7:30, rientro verso le 19:30,
   circa 12 ore di impegno e 5 di guida. Nei limiti.
5. Nome, mail e telefono della cliente, per l'intestazione del PDF.

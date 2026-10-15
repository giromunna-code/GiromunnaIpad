# Note interne — Alexandra Lange, escursione Firenze ↔ Santuario della Verna, 27.4.2027

**Cliente:** Alexandra Lange — richiesta via mail, 25 persone, alloggiate in zona Santo Spirito
**Rif. preventivo:** GM-2027-0427-AL · **Preparato:** 15 ottobre 2026 · **Validità:** 30 ottobre 2026

File generati:
- `GiroMunna_Preventivo_Firenze_La_Verna_27_aprile_2027_IT.pdf`
- `GiroMunna_Preventivo_Firenze_La_Verna_27_aprile_2027_EN.pdf`
- `genera_preventivo_verna.py` — rigenera entrambi i PDF
- `MAIL.md` — testo della mail, italiano e inglese

```bash
python3 genera_preventivo_verna.py --lingua it
python3 genera_preventivo_verna.py --lingua en
```

## Prezzo

| Voce | Netto |
|---|---|
| Giornata a disposizione Firenze – La Verna – Firenze, 7:45–19:00 | € 1.300,00 |
| Pranzo del conducente | a carico del cliente |

IVA 10% € 130,00 · **Totale € 1.430,00** (≈ € 57 a persona) — acconto € 429,00, saldo € 1.001,00.

Come è costruito: base Le Filigare (giornata a disposizione ~80 km e 5 ore = € 809). Qui il
cliente ha il mezzo per oltre 11 ore e ~190 km di servizio, più ~100 km di trasferimenti
vuoti dalla sede a Firenze e ritorno. Confronto con Alvora: 140 km / 8 ore a € 980, 237 km a
€ 1.250. La Verna sta sopra entrambi per ore, quindi € 1.300. Margine di trattativa: si può
scendere a € 1.200 + IVA se la cliente chiede uno sconto.

## Da verificare / decidere

1. **Porta Romana e il check point bus.** Ho proposto Piazzale di Porta Romana come ritrovo
   fuori ZTL (10–12 minuti a piedi da Santo Spirito). Girolamo, verifica che la sosta per
   carico/scarico lì non ricada nella zona del check point da € 421: se ricade, l'alternativa
   è spostare il ritrovo più in là sui viali (per esempio Viale Petrarca / Piazza Tasso? da
   controllare) o mettere il check point a preventivo.
2. **Orario del conducente.** Partenza dalla sede verso le 6:30, rientro verso le 20:00: circa
   13 ore e mezza di impegno, con poco più di 5 ore di guida. Si sta nelle regole usando il
   riposo giornaliero ridotto (9 ore); se l'autista ha altri servizi il 26 sera o il 28
   mattina, va controllato.
3. **Capienza.** 25 persone = Beluga pieno; resta il posto dell'accompagnatore. Se il gruppo
   supera i 26 serve il secondo minibus: decide Girolamo, e il costo va concordato con
   Francesco.
4. **Parcheggio alla Verna.** Non ho trovato informazioni ufficiali sulla sosta dei pullman al
   santuario; il Beluga sale ai parcheggi del santuario. Se c'è un ticket bus, è compreso nel
   prezzo.
5. **Processione delle 15.** Nel preventivo è scritto "nel primo pomeriggio" con invito a
   verificare l'orario col santuario, per non impegnarsi su un'ora precisa.

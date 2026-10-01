# Note interne — Matrimonio Tenuta di Artimino, 11.10.2026

**Cliente:** Aries Weddings Tuscany (Chiara Detti & Silvia Chiti, info@ariesweddingstuscany.com)
**Rif. preventivo:** GM-2026-1011-AW · **Preparato:** 1 ottobre 2026 · **Validità:** 3 ottobre 2026

File generati:
- `GiroMunna_Preventivo_Matrimonio_Artimino_11_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Matrimonio_Artimino_11_ottobre_2026_EN.pdf`
- `genera_preventivo_matrimonio_artimino.py` — rigenera entrambi i PDF

```bash
python3 genera_preventivo_matrimonio_artimino.py --lingua it
python3 genera_preventivo_matrimonio_artimino.py --lingua en
```

## Cosa copre

Su decisione di Girolamo, solo due gruppi:

| Struttura | Ospiti | Mezzo | Andata | Ritorno |
|---|---|---|---|---|
| Villa la Malva, Carmignano | 26 | Beluga (26 posti, pieno) | 14:45 | 03:00 |
| Borgo di Villa Castelletti, Signa | 18 | Tourengo (28 posti) | 14:30 | 03:00 |

**Esclusi:** Airbnb Via Livornese 395, Lastra a Signa (7) e Villa le Farnette, Comeano (3).
Nel preventivo è detto che per loro non c'è disponibilità.

## Prezzi

| Voce | Netto |
|---|---|
| Beluga, andata e ritorno | € 1.000,00 |
| Tourengo, andata e ritorno | € 1.000,00 |
| Supplemento rientro dopo le 02:00, 2 × € 250 | € 500,00 |

**Totale netto € 2.500,00 · IVA 10% € 250,00 · Totale € 2.750,00** — acconto € 825,00, saldo € 1.925,00.

Ogni andata e ogni ritorno è un trasferimento breve (6–15 km), ma i mezzi partono e rientrano da
Ponte Buggianese (~40 km da Artimino), quindi sono quattro uscite in tutto, una di notte.
Riferimento Le Filigare: € 500 netti per un trasferimento di ~50 km.

## Da decidere / verificare

1. **Commissione.** L'agenzia chiede il prezzo "incluso di commissione" senza indicare la
   percentuale. I prezzi sono stati tenuti alti per assorbirla: con una commissione del 10%
   (€ 250 sul netto) a GiroMunna restano € 2.250. Il PDF non nomina la commissione, così
   l'agenzia può girarlo agli sposi; la percentuale va detta nella mail.
2. **Costo del Tourengo con Francesco** — da concordare prima di inviare.
3. Il Beluga è pieno a 26: se cresce anche di una persona non basta.
4. Il Tourengo con 18 ospiti ha 10 posti liberi: 7 (Lastra a Signa) + 3 (Comeano) = 10.
   Volendo, potrebbe prendere anche loro, ma l'andata di Castelletti e dell'Airbnb è alla
   stessa ora (14:30): bisognerebbe spostare un ritiro.

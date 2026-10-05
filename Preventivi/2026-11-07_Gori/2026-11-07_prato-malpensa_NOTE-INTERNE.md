# Note interne — Trasferimento Prato ↔ Milano Malpensa, 7 e 14.11.2026

**Cliente:** Francesca Gori (francescagori@yahoo.it, +39 340 313 4154)
**Rif. preventivo:** GM-2026-1107-FG · **Preparato:** 5 ottobre 2026 · **Validità:** 19 ottobre 2026

File generati:
- `GiroMunna_Preventivo_Prato_Malpensa_7-14_novembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Prato_Malpensa_7-14_novembre_2026_EN.pdf`
- `genera_preventivo_malpensa.py` — rigenera entrambi i PDF
- `MAIL.md` — testo della mail, italiano e inglese

```bash
python3 genera_preventivo_malpensa.py --lingua it --cliente "Francesca Gori"
python3 genera_preventivo_malpensa.py --lingua en --cliente "Francesca Gori"
```

## Richiesta

Fino a 25 persone, Beluga. Sab 7/11 partenza da Prato alle 5:00 per Malpensa; sab 14/11
ritorno Malpensa → Prato "alle ore 23 circa" (letto come orario di atterraggio: da confermare).

## Prezzi

| Voce | Netto |
|---|---|
| 7/11 Prato → Malpensa | € 1.650,00 |
| 14/11 Malpensa → Prato | € 1.650,00 |
| Supplemento rientro dopo le 02:00 | € 250,00 |
| **Totale netto** | **€ 3.550,00** |

IVA 10% € 355,00 · **Totale € 3.905,00** — acconto € 1.171,50, saldo € 2.733,50.

Come è costruito: ogni trasferimento è in realtà una giornata intera per il mezzo, perché
c'è il vuoto. Base → Prato → Malpensa → base sono circa 700 km e 8–9 ore. Le Filigare
(€ 500 per ~50 km) e il Corte Francigena (€ 1.300 per 208 km, ma già scontato per due mezzi)
portano, a mezzo singolo e su 320 km, a € 1.600–1.800: tenuto € 1.650, nella fascia alta
come da regola. Costi vivi stimati per trasferimento: gasolio ~€ 250, pedaggi ~€ 80.

Il supplemento notturno è messo a preventivo perché, con atterraggio alle 23:00, si arriva
a Prato verso le 2:30–3:00. Nel preventivo è detto che si toglie se il volo arriva prima.

## Da verificare

1. **Ore di guida del 14/11.** Il conducente parte dalla base verso le 18:00 e rientra
   verso le 3:30: circa 700 km, 8 ore di guida effettive. Entro le 9 ore giornaliere ma
   senza margine: con ritardi forti del volo si sfora. Valutare se serve un secondo autista
   o se accettare il rischio.
2. **Bagagli.** 25 persone per una settimana: 25 valigie grandi più bagagli a mano possono
   non entrare nel vano del Beluga. Chiesto al cliente il numero esatto. Se non entrano,
   valutare il carrello o il Tourengo (decisione di Girolamo).
3. **Orario del volo di andata.** Arrivo a Malpensa verso le 8:45: va bene per voli dalle
   11:30 in poi.
4. **Prato ZTL.** Se il ritiro è dentro le mura, punto di ritrovo esterno.

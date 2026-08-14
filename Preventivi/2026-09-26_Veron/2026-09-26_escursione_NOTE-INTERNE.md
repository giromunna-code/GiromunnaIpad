# Note interne — Escursione Siena, San Gimignano e Pisa, 26.09.2026

**Cliente:** Maria Juliana Veron · **Rif. preventivo:** GM-2026-0926-MJV · **Preparato:** 14 agosto 2026 · **Validità:** 28 agosto 2026

**Contatti cliente:** juliveron97@gmail.com · +54 3624759805 (Argentina)

Richiesta originale: escursione culturale il 26 settembre 2026, da Firenze verso Siena, San
Gimignano e Pisa, fino a 26 persone (Beluga). Nessuna nota aggiuntiva dalla cliente.

File generati:
- `GiroMunna_Preventivo_Escursione_Siena_San_Gimignano_Pisa_26_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Escursione_Siena_San_Gimignano_Pisa_26_settembre_2026_EN.pdf`
- `genera_preventivo_escursione.py` — rigenera entrambi i PDF

Per rigenerare:

```bash
python3 genera_preventivo_escursione.py --lingua it --cliente "Maria Juliana Veron"
python3 genera_preventivo_escursione.py --lingua en --cliente "Maria Juliana Veron"
```

---

## Come è stato costruito il prezzo

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, mezzo singolo:

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento ~50 km | € 500,00 |
| Giornata a disposizione ~80 km, 5 ore | € 809,00 |

Questa escursione è una giornata intera a disposizione su ~254 km e ~11 ore e mezza
(ritrovo 07:30, rientro 18:55): sia i km sia le ore sono molto sopra la giornata di
riferimento (circa 3x i km, circa 2,3x le ore). Prezzo netto fissato a **€ 2.450,00**,
tenuto sul lato alto della proporzione perché nel dubbio il prezzo va tenuto alto.

**Non è stato usato il Corte Francigena come base**, essendo un lavoro a due mezzi con
importi per mezzo già scontati per volume.

Nel netto sono già compresi i parcheggi bus a Siena, San Gimignano e Pisa e il permesso
comunale di Siena (~€ 160): non compaiono come voce separata per non appesantire il
preventivo, ma vanno tenuti a mente nel margine.

Totale netto € 2.450,00 · IVA 10% € 245,00 · **Totale € 2.695,00** (≈ € 103,65 a persona
sul gruppo pieno di 26). Acconto 30% € 808,50 — saldo € 1.886,50.

## Itinerario e km — come sono stati stimati

Nessun indirizzo di ritrovo a Firenze è stato fornito: orari e km sono costruiti su una
partenza generica dal centro di Firenze.

| Tratta | Km stimati | Durata |
|---|---|---|
| Firenze → Siena | ~70 km | ~1h15 |
| Siena → San Gimignano | ~42 km | ~50 min |
| San Gimignano → Pisa | ~62 km | ~1h05 |
| Pisa → Firenze | ~80 km | ~1h10 |

Totale ~254 km, ~4h20 di guida effettiva su una giornata di ~11h25 (il resto sono le soste
nelle tre località). Tempi di sosta: Siena 2h15, San Gimignano 2h40 (con pranzo libero),
Pisa 2h10. Tutto compatibile con le ore di guida di un solo conducente, senza pernottamento
fuori sede.

## Punti da chiarire prima di confermare

1. **Indirizzo esatto di ritrovo/rientro a Firenze** — se dentro la ZTL del centro storico
   serve il permesso bus separato (~€ 350), non compreso nel prezzo. È il punto più
   importante da chiudere prima di dare conferma definitiva del prezzo.
2. **Numero definitivo dei passeggeri** — "hasta 26" è un tetto, non un numero confermato;
   il Beluga è già alla capienza massima con 26, quindi utile saperlo presto.
3. Nessuna mail di richiesta di preventivo da inviare: il documento si consegna così com'è,
   a Girolamo pensa lui a rispondere alla cliente.

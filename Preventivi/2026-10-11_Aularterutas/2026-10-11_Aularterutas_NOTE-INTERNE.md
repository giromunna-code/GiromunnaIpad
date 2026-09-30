# Note interne — Siena · Monteriggioni · San Gimignano · Firenze, 11.10.2026, fino a 25 pax

**Cliente:** Aularterutas — Lorena (+34 685 111 559, info@aularterutas.com) · **Rif. preventivo:**
GM-2026-1011-LA · **Preparato:** 30 settembre 2026 · **Validità:** 3 ottobre 2026

File generati, tutti in `Preventivi/2026-10-11_Aularterutas/`:
- `GiroMunna_Preventivo_Siena_San_Gimignano_Firenze_11_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Siena_San_Gimignano_Firenze_11_ottobre_2026_EN.pdf`
- `genera_preventivo_aularterutas.py` — rigenera entrambi i PDF
- `preventivo_siena_san_gimignano_firenze_11_ottobre_2026.html` — la pagina web bilingue

```bash
python3 genera_preventivo_aularterutas.py --lingua it
python3 genera_preventivo_aularterutas.py --lingua en
```

Il cliente predefinito è "Aularterutas"; con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Richiesta

Domenica 11 ottobre 2026, giornata a disposizione, fino a 25 persone, Beluga:
08:30 NH Siena (Via La Lizza 1) → Monteriggioni · 11:00 Monteriggioni → San Gimignano ·
16:00 San Gimignano → Grand Hotel Adriatico (Via Maso Finiguerra 9, Firenze).

## Prezzi

| Voce | Netto |
|---|---|
| Giornata a disposizione Siena → Monteriggioni → San Gimignano → Firenze | € 1.250,00 |
| Permesso bus Comune di Siena | € 160,00 |
| Permesso accesso bus centro di Firenze | € 350,00 |
| Vitto conducente (pranzo), nessun pernottamento | a carico del cliente |

**Totale netto € 1.760,00 · IVA 10% € 176,00 · Totale € 1.936,00** (≈ € 77,00 a persona su 25)

Acconto 30% € 580,00 — saldo € 1.356,00.

## Come è stato costruito il prezzo

Riferimento a mezzo singolo: **Le Filigare** (GM-2026-0821-LF), giornata a disposizione di
~80 km e 5 ore a € 809,00 netti. Qui:

- servizio circa 08:15-17:30, 9 ore;
- ~105 km con il gruppo (20 + 30 + 55);
- avvicinamento a vuoto Ponte Buggianese → Siena ~115 km, rientro Firenze → base ~50 km;
- in tutto ~270 km e una giornata del conducente di circa 12 ore (partenza ~06:45, rientro ~18:30).

Da qui € 1.250,00 per la giornata, tenuto alto. I permessi sono righe a parte: se il cliente
rinuncia all'ingresso nel centro di Firenze si tolgono € 350,00 senza rifare il resto.
Nessun importo del Corte Francigena usato come base.

## Margine

Mezzo di proprietà, nessun pernottamento. Costo diretto stimato € 300-400 per la giornata:
margine buono. Se per qualche motivo si dovesse subappaltare a Francesco, rivedere il prezzo.

## Da chiarire prima di inviare

1. **Disponibilità del Beluga domenica 11 ottobre.** Il preventivo non dice che il mezzo è
   libero: va verificato.
2. **Importi dei permessi.** Siena ~€ 160 e Firenze ~€ 350 sono le cifre di riferimento:
   controllare le tariffe attuali per un 26 posti e la procedura per la domenica.
3. **Bagagli.** Cambio hotel Siena → Firenze con 25 persone: il vano porta una ventina di
   valigie normali, non 25 grandi. Nel preventivo si propongono una valigia media a testa o un
   furgone bagagli separato (da quotare se lo chiedono).
4. **Orari.** Le 11:00 e le 16:00 sono lette come partenze. Se le 11:00 sono l'arrivo a
   Monteriggioni, si parte da Siena alle 10:30, stesso prezzo.
5. **Tempi stretti.** Oggi mancano 11 giorni; dal 1° ottobre il servizio è negli ultimi 10
   giorni (cancellazione 100%). Acconto da incassare subito alla conferma.
6. **Lingua.** La cliente è spagnola; il preventivo è in italiano e inglese come da regola.

# Note interne — Massarosa → Malpensa, 01.10.2026, 16 pax

**Rif.** GM-2026-1001-MM · **Preparato** 20 agosto 2026 · **Validità** 3 settembre 2026
**Cliente:** non ancora noto — la richiesta è arrivata senza nome.

## Il lavoro

Massarosa (LU) → Aeroporto di Milano Malpensa, sola andata, giovedì 1 ottobre 2026,
partenza ore 02:00, 16 passeggeri. Circa 330 km via A11 / A12 / A26.

Un mezzo solo, il Beluga. Nessun bisogno di Francesco.

## Prezzo

| Voce | Netto |
|---|---|
| Trasferimento, circa 330 km | € 1.550,00 |
| Maggiorazione notturna 02:00 | € 250,00 |
| Parcheggio bus Malpensa, prima ora | € 35,00 |

**Netto € 1.835,00 · IVA 10% € 183,50 · Totale € 2.018,50** — circa € 126,00 a persona.
Acconto 30% € 605,00 (arrotondato da 605,55), saldo € 1.413,50.

Base di riferimento: **Le Filigare**, che è a mezzo singolo. Il Corte Francigena non è stato
usato, ha due mezzi e prezzi già scontati per volume.

## Margine

Il mezzo fa circa 660 km fra andata carica e rientro a vuoto. Gasolio e pedaggi sui
€ 350-400, più il parcheggio. Restano indicativamente € 1.100-1.200 prima del costo del
conducente: buono.

## Vitto e alloggio del conducente

Non serve nessun pernottamento: parte dalla base all'01:00, scarica a Malpensa alle 05:30,
pausa obbligatoria di 45 minuti, rientra verso le 09:45. Circa 8 ore di guida, un solo
conducente, dentro i limiti di legge.

Nel preventivo la voce è comunque indicata — riga di prezzo, non incluso — ma con la dicitura
« nessun pernottamento necessario » invece di « a carico vostro », che per zero notti avrebbe
confuso.

## Da chiarire col cliente

1. Numero e orario del volo, e il terminal di Malpensa.
2. Indirizzo esatto del punto di carico (il CAP 55054 comprende anche i paesi in collina).
3. Numero definitivo dei passeggeri.
4. Nome, recapito e dati di fatturazione.
5. Chiedere se serve anche il ritorno: rende di più e al cliente costa meno di due andate.
6. Bloccare il mezzo per la notte fra il 30 settembre e il 1° ottobre.

## Rigenerare i PDF

```bash
python3 genera_preventivo_massarosa_malpensa.py --lingua it --cliente "Nome"
python3 genera_preventivo_massarosa_malpensa.py --lingua en --cliente "Nome"
```

Senza `--cliente` esce senza intestatario, com'è ora. Le `MM` del riferimento stanno per
Massarosa–Malpensa: se il nome del cliente cambia le iniziali, si aggiorna `RIF` in cima allo
script e nella pagina HTML.

La pagina web `preventivo_transfer_massarosa_malpensa_1_ottobre_2026.html` è bilingue e sta
su iPhone senza scorrimento laterale. Non contiene note interne: si può mostrare al cliente
così com'è.

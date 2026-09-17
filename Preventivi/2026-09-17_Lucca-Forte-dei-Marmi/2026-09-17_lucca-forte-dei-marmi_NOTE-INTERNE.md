# Note interne — Lucca · Forte dei Marmi · cantina, giornata a disposizione, 16-20 pax

**Cliente:** non ancora noto · **Rif. preventivo:** GM-2026-0917-LV (provvisorio) ·
**Preparato:** 17 settembre 2026 · **Validità:** 17 ottobre 2026

File generati:

- `GiroMunna_Preventivo_Lucca_Forte_dei_Marmi_IT.pdf`
- `GiroMunna_Preventivo_Lucca_Forte_dei_Marmi_EN.pdf`
- `genera_preventivo_lucca_forte_dei_marmi.py` — rigenera entrambi i PDF
- `preventivo_lucca_forte_dei_marmi.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-17_Lucca-Forte-dei-Marmi/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_lucca_forte_dei_marmi.py --lingua it
python3 genera_preventivo_lucca_forte_dei_marmi.py --lingua en
```

Senza `--cliente` il preventivo esce **senza intestatario** — la richiesta è arrivata anonima
e un segnaposto in cima a un preventivo fa peggio del niente. Quando arriva il nome:

```bash
python3 genera_preventivo_lucca_forte_dei_marmi.py --lingua it --cliente "Nome" --rif GM-2026-MMGG-XX
python3 genera_preventivo_lucca_forte_dei_marmi.py --lingua en --cliente "Nome" --rif GM-2026-MMGG-XX
```

---

## La richiesta

Arrivata in inglese, senza nome, senza data e senza recapito. Testo: un bus per 16-20 persone,
partenza da Lucca la mattina per Forte dei Marmi, da lì un posto lì vicino per il pranzo, nel
pomeriggio una cantina nei dintorni, rientro a Lucca la sera.

## Il programma quotato

| Orario | Percorso | km |
|---|---|---|
| 09:00 | Lucca → Forte dei Marmi | 38 |
| 09:45 – 13:00 | Mattinata a Forte dei Marmi, mezzo a disposizione | — |
| 13:00 | Forte dei Marmi → ristorante (in paese o Pietrasanta) | 0-8 |
| 15:30 | Ristorante → cantina | 25-45 |
| 16:15 – 18:30 | Visita e degustazione, mezzo a disposizione | — |
| 18:30 | Cantina → Lucca, arrivo verso le 19:30 | 15-45 |

Percorso completo **circa 120 km**, mezzo impegnato **circa 10 ore e mezza**, più le due
trasferte dalla base di Ponte Buggianese (circa 40 km per parte).

Il gruppo sta comodamente sul **Beluga**: 26 posti contro 16-20 passeggeri. Nessun motivo di
tirare in ballo il secondo minibus.

## Prezzo

| Voce | Netto |
|---|---|
| Giornata intera a disposizione, 09:00 – 19:30, ~120 km | € 1.050,00 |
| Vitto del conducente (pranzo) | a carico del cliente |

**Totale netto € 1.050,00 · IVA 10% € 105,00 · Totale € 1.155,00**
(€ 57,75 a persona in venti, € 72,19 in sedici)

Acconto 30% € 346,50 — saldo € 808,50.

## Come è stato costruito

Riferimento: **Le Filigare** (GM-2026-0821-LF), a mezzo singolo come questo — giornata a
disposizione di ~80 km e 5 ore a € 809 netti. Secondo termine di paragone la giornata piena
del preventivo Alvora, 140 km e 8 ore a € 980 netti.

Qui i chilometri sono meno di quelli di Alvora ma le ore sono di più: **10 ore e mezza di
mezzo impegnato contro 8**. Con le trasferte dalla base la giornata del conducente arriva a
circa 12 ore, vicino al limite. Su una giornata a disposizione pesano le ore, non la distanza:
da qui i € 1.050.

**Non si usano i prezzi del Corte Francigena.** Quel preventivo ha due mezzi e i suoi importi
per mezzo sono già scontati per volume: applicarli qui porterebbe il prezzo sotto mercato.

## Margine

Lavoro sul mezzo di proprietà, costo diretto stimato **€ 250-350** sulla giornata, senza
pernottamento perché la giornata finisce a Lucca e il conducente rientra alla base. Margine
buono.

Se per qualunque motivo il lavoro dovesse passare a **Francesco** (€ 600-700 al giorno), il
prezzo va rivisto al rialzo del 20-25% prima di inviare.

## Verifiche di accesso

- Nessun onere: l'itinerario non tocca l'aeroporto di Pisa, né il centro di Firenze, né Siena.
- **Lucca**: il centro dentro le mura è ZTL. Il punto di ritrovo va verificato sull'indirizzo
  esatto dell'albergo.
- **Forte dei Marmi**: in alta stagione l'accesso a centro e lungomare è regolato e i pullman
  hanno stalli dedicati. Sotto gli otto metri ci si muove molto meglio, ma il piano traffico
  va verificato alla data scelta.
- **Candia dei Colli Apuani**: se la cantina è lassù, strada stretta e in salita. Il Beluga ci
  arriva, un gran turismo no. Farsi confermare dalla cantina il punto di discesa.

## Da chiarire prima di inviare

1. **La data del servizio.** Manca del tutto. Senza data non si blocca il mezzo, non si
   calcola la fascia di cancellazione e il riferimento resta provvisorio: `GM-2026-0917-LV`
   usa le cifre di emissione e le iniziali dell'itinerario, non quelle del primo servizio.
   Quando la data arriva, rigenerare con `--rif` e rinominare la cartella
   `Preventivi/AAAA-MM-GG_Cliente/`.
2. **Nome, mail e recapito del cliente.** La richiesta è anonima: i PDF escono senza
   intestatario finché non sappiamo a chi sono indirizzati.
3. **Ristorante e cantina.** Quotate entrambe le direzioni — Candia dei Colli Apuani sopra
   Massa, oppure Colline Lucchesi e Montecarlo sulla via del rientro — perché il chilometraggio
   si equivale e il prezzo non cambia. Se la scelta cade più lontano, per esempio Bolgheri, il
   preventivo va rifatto.
4. **Punto di ritrovo a Lucca**, con indirizzo esatto e orario.
5. **Numero definitivo dei passeggeri.** Non cambia il prezzo, serve per l'assicurazione.
6. **Durata della giornata.** 09:00 – 19:30 sta nei limiti con circa un'ora di margine. Se
   chiedono la cena in Versilia serve il cambio del conducente o una partenza più tardi: va
   deciso in fase di conferma, non la sera stessa.
7. **Bloccare la disponibilità del mezzo** appena la data è fissata.

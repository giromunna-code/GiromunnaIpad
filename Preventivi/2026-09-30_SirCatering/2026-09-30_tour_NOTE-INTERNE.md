# Note interne — Tour Toscana 30.09-02.10.2026, 24 pax

**Cliente:** Sir Catering (contatto: Tim, zaakvoerder, tim@sircatering.be, +32 486 33 77 12)
**Rif. preventivo:** GM-2026-0930-SC · **Preparato:** 26 agosto 2026 · **Validità:** 9 settembre 2026

File generati:
- `GiroMunna_Preventivo_Tuscany_Tour_30_settembre-2_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Tuscany_Tour_30_settembre-2_ottobre_2026_EN.pdf`
- `genera_preventivo_tuscany_tour.py` — rigenera entrambi i PDF
- `preventivo_tour_30_settembre-2_ottobre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-30_SirCatering/`.

Il cliente (Sir Catering) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_tuscany_tour.py --lingua it
python3 genera_preventivo_tuscany_tour.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Il gruppo e il mezzo

24 passeggeri: stanno comodamente sul **Beluga** (26 posti + autista), con due posti liberi.
Non serve il secondo minibus di Francesco: nessuna decisione da chiedere a Girolamo su questo
punto, il lavoro è a mezzo singolo.

## Prezzi

| Data | Servizio | Netto |
|---|---|---|
| Mer 30 set | Aeroporto di Pisa → sosta pranzo → Le Ragnaie (Montalcino), ~170 km, 5 h 30 | € 990,00 |
| Gio 1 ott | Giornata intera: Vineria Aperta, Antinori, cena da Saloni, ~168 km, **11 h 55** | € 1.480,00 |
| Ven 2 ott | Siena (Le Logge) → Querciabella → aeroporto di Pisa, ~190 km, 9 h 30, permesso Siena incluso | € 1.230,00 |
| — | Vitto e alloggio conducente, 1 notte (1 ottobre) | a carico del cliente |

**Totale netto € 3.700,00 · IVA 10% € 370,00 · Totale € 4.070,00** (≈ € 170,00 a persona)

Acconto 30% € 1.221,00 — saldo € 2.849,00.

## Come sono stati costruiti i prezzi

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, a mezzo singolo come questo lavoro.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Da qui la scala: il trasferimento di mercoledì (~170 km, 5 h 30, con una sosta pranzo di 2 ore
inclusa) vale più del trasferimento-tipo di Le Filigare per il chilometraggio quasi triplo, ma
con un tasso a km più basso, coerente con lo sconto sulla distanza già visto nel preventivo
Alvora (giornate più lunghe = costo/km più basso). Giovedì è la giornata più pesante: quasi 12
ore di impegno, meno km ma molto più tempo di attesa (visita, degustazione, cena), prezzata più
alta delle altre a parità di distanza. Venerdì è una giornata piena "normale" con l'aggiunta del
permesso di Siena.

**Non si è usato il Corte Francigena come base**, per lo stesso motivo spiegato nel preventivo
Alvora: quei prezzi sono per mezzo su un lavoro a due mezzi, già scontati per volume.

## La giornata critica: giovedì 1 ottobre

Pick-up alle 11:45, ultimo rientro alle 23:40: **11 ore e 55 minuti di impegno del mezzo**, la
giornata più lunga vista finora in un preventivo GiroMunna (più lunga anche del giorno più pesante
di Alvora, che arrivava a 8 h 15 ma su più chilometri). La guida effettiva è limitata (circa 3 h
35 min), il resto è attesa durante pranzo, visita/degustazione e cena.

**Il problema vero non è la giornata in sé, ma la cerniera con venerdì.** Fra il rientro delle
23:40 di giovedì e la partenza delle 09:30 di venerdì restano **9 ore e 50 minuti**: sotto le 11
ore di riposo giornaliero previste per un autista professionista (Regolamento UE 561/2006). Non
va silenziato: è stato segnalato al cliente come prima nota del preventivo, con una soluzione
proposta a costo zero (spostare di un'ora l'uno o l'altro orario). Se il cliente non risponde
prima della conferma, il programma non si può eseguire così com'è — va bloccato in fase di
definizione, non lasciato per il giorno del servizio.

## Le notti del conducente

**Una sola notte a carico del cliente (1 ottobre)**, non tre come nel preventivo Alvora. La sera
di mercoledì il conducente ha margine ampio — quasi 20 ore fra le 16:00 e le 11:45 del giorno
dopo — per rientrare alla base di Ponte Buggianese (~130 km da Montalcino) e tornare. Fra giovedì
e venerdì no: il conducente pernotta in zona, verosimilmente nella stessa struttura del gruppo.

## Margine

Preventivo costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato € 250-350 a
giornata di servizio, più il rientro a vuoto di mercoledì sera (~260 km andata e ritorno) che
resta a carico di GiroMunna, più il pernottamento del conducente di giovedì che paga il cliente.
Il margine sui tre servizi resta buono, un po' eroso dal chilometraggio a vuoto di mercoledì
rispetto a un'ipotesi di conducente che pernotta comunque in zona per tutta la durata (da valutare
con Girolamo se preferibile in pratica, anche se più caro per il cliente).

**Se si subappalta a Francesco**, il costo si colloca sui € 600-700 al giorno e il margine si
assottiglia parecchio: in quel caso vanno rivisti i prezzi al rialzo di circa il 20-25% prima di
inviare.

## Verifiche di accesso

- Aeroporto di Pisa: parcheggio bus, circa € 61,00 complessivi per i due transiti (pick-up del 30
  settembre e drop-off del 2 ottobre) — incluso nel prezzo.
- Siena: il centro storico dove si trova il ristorante Le Logge è area pedonale, serve il permesso
  comunale per i bus turistici (circa € 160,00) — incluso nel prezzo di venerdì. Da confermare il
  punto esatto del parcheggio bus autorizzato più vicino a Le Logge.
- Nessuna delle altre tappe (Vineria Aperta, Antinori, Querciabella, ristorante Saloni) risulta in
  zona a traffico limitato, ma le indirizzi esatti vanno confermati assieme al cliente.

## Da chiarire prima di inviare

1. **Il riposo del conducente fra giovedì e venerdì** — il punto più delicato, richiede una
   decisione del cliente prima di dare il programma per definitivo.
2. **Le Ragnaie e l'hotel del giovedì** — stessa struttura o due diverse? Cambia i punti di
   ritrovo e dove alloggia il conducente.
3. **Località della sosta pranzo di mercoledì 30 settembre**, non ancora nota — il prezzo è
   stimato sulla direttrice Siena-Grosseto (San Gimignano/Colle di Val d'Elsa).
4. **Quale sede Antinori** — quotata Antinori nel Chianti Classico, San Casciano in Val di Pesa.
5. **Orari dei due voli** (arrivo 30 settembre, partenza 2 ottobre).
6. **Numero definitivo dei passeggeri** e dati di fatturazione.
7. **Bloccare la disponibilità del mezzo** per il 30 settembre - 2 ottobre.

Nessuna bozza di mail è stata preparata: la richiesta arrivata (da Tim, Sir Catering) resta senza
risposta scritta da parte nostra, come da regola — ci pensa Girolamo.

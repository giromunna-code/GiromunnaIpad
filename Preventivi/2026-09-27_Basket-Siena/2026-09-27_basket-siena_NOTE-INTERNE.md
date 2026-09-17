# Note interne — Trasferta basket a Siena, domenica 27 settembre 2026

**Cliente:** da definire · **Rif. preventivo:** GM-2026-0927-BS · **Preparato:** 17 settembre 2026 · **Validità:** 21 settembre 2026

File generati:
- `GiroMunna_Preventivo_Trasferta_Basket_Siena_27_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Trasferta_Basket_Siena_27_settembre_2026_EN.pdf`
- `genera_preventivo_basket_siena.py` — rigenera entrambi i PDF
- `preventivo_basket_siena_27_settembre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-27_Basket-Siena/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_basket_siena.py --lingua it
python3 genera_preventivo_basket_siena.py --lingua en
```

Con `--cliente "Nome"` si cambia l'intestatario e con `--rif GM-2026-0927-XX` il riferimento:
appena si sa chi intesta la trasferta vanno cambiati tutti e due, perché adesso il PDF esce
con l'intestazione generica *Gruppo trasferta basket* e le iniziali provvisorie **BS**
(basket Siena). Anche il nome della cartella va poi rifatto con il nome del cliente.

---

## Il servizio quotato

Dal **palazzetto dello sport di Montecatini Terme** al **palazzetto dello sport di Siena**,
attesa per tutta la partita, rientro al palazzetto di Montecatini. Un mezzo, il Beluga, fino
a 26 passeggeri. Circa 110 km per tratta, 220 in tutto, per l'A11 e il raccordo Firenze-Siena.

Orari costruiti sulla **palla a due delle 20:30** (Girolamo ha detto che si gioca in serata,
l'orario esatto non c'è ancora):

| | |
|---|---|
| Ritrovo al palazzetto di Montecatini | 17:15, partenza 17:30 |
| Arrivo al palazzetto di Siena | verso le 19:10 |
| Attesa durante la partita | circa 19:15 – 23:00 |
| Ripartenza da Siena | 23:00 |
| Rientro a Montecatini | verso le 00:40 |

Mezzo impegnato circa nove ore, rientro **prima delle 02:00**: nessun supplemento notturno.

## Prezzi

| Servizio | Netto |
|---|---|
| Dom 27 set — palazzetto di Montecatini → palazzetto di Siena, attesa, rientro (220 km, fino a 9 h) | € 900,00 |
| Vitto del conducente | a carico del cliente |

**Totale netto € 900,00 · IVA 10% € 90,00 · Totale € 990,00** (≈ € 38,00 a persona in 26)

Acconto 30% € 297,00 — saldo € 693,00 entro il 25 settembre.

## Come è stato costruito il prezzo

Riferimento **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come questo, e le due
giornate del preventivo Alvora:

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento ~50 km | € 500,00 |
| Le Filigare — giornata a disposizione Siena, ~80 km, 5 h | € 809,00 |
| Alvora — giornata a disposizione, 115 km, 8 h | € 980,00 |
| Alvora — giornata piena con tre tappe, 250 km, 8 h 30 | € 1.250,00 |
| Questa trasferta secondo la scala — 220 km, fino a 9 h, di sera e di domenica | € 1.200,00 |
| **Prezzo messo a preventivo** | **€ 900,00** |

Per chilometri e ore il lavoro sta fra le due giornate Alvora, e in più è serale e domenicale
con il conducente impegnato fino all'una di notte: la scala lo porterebbe sui € 1.200,00 netti,
che è la cifra della prima stesura.

**Il prezzo è stato abbassato a € 900,00 su indicazione di Girolamo**, che lo ha ritenuto
troppo alto per una trasferta sportiva di una sera sola. Sono € 990,00 IVA inclusa, cioè sotto
i mille euro, che su una trasferta di squadra o di tifosi è la soglia che conta. Sotto questa
cifra non si scende a preventivo: si tratta semmai a voce, altrimenti il servizio si svaluta.

**Non sono stati usati i prezzi del Corte Francigena divisi per due**: quelli sono per mezzo
su un lavoro a due mezzi e sono già scontati per volume.

## Margine

Mezzo di proprietà: costo diretto stimato € 250-350 fra carburante, pedaggi e conducente, più
la serata di lavoro. Nessuna notte da pagare, perché si rientra in nottata e la base di Ponte
Buggianese è a quindici chilometri da Montecatini. Anche a € 900,00 netti il margine resta
ampio.

**Se il Beluga fosse impegnato altrove** e il lavoro andasse a Francesco, il costo salirebbe
sui € 600-700 e a questo prezzo non ci starebbe quasi più niente: in quel caso il preventivo
va rifatto prima di inviarlo.

## Verifiche di accesso

- Il palazzetto di Siena è **fuori dalle mura**: nessun permesso comunale, nessun onere.
- Il permesso per i bus turistici nel centro storico di Siena (circa € 160,00) serve solo se
  il gruppo vuole una sosta dentro le mura prima della partita. Va chiesto in anticipo.
- Nessun altro onere di accesso sul percorso.

## Da chiarire prima di inviare

1. **Chi è il cliente** — società sportiva, gruppo di tifosi o privato. Servono nome esatto,
   dati di fatturazione e un recapito.
2. **L'orario della partita** — quotata la palla a due delle 20:30. Con le 18:00 cambiano
   tutti gli orari (partenza alle 15:00, rientro verso le 22:15) ma non il prezzo.
3. **Quale palazzetto a Siena e dove si può fermare il mezzo** — per le partite serali con un
   gruppo organizzato capita che venga indicata un'area di sosta obbligata per il pullman.
4. **Numero esatto dei passeggeri** — fino a 26 sta sul Beluga. Oltre, serve il secondo
   minibus di Francesco e la decisione è di Girolamo.
5. **Sosta per mangiare dopo la partita** — se la vogliono, va rifatto il conto del rientro
   e va guardato il limite delle 02:00 (€ 250,00 di supplemento).
6. **Bloccare la disponibilità del mezzo** per la sera del 27 settembre: mancano dieci
   giorni e da domani si entra nella fascia di cancellazione al 100%.

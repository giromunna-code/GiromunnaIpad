# Note interne — Navetta matrimonio a Reggello (FI), 25-26.09.2026, 54 ospiti

**Cliente:** da confermare · **Rif. preventivo:** GM-2026-0925-VB · **Preparato:** 8 settembre 2026 · **Validità:** 15 settembre 2026

File generati:
- `GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25-26_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25-26_settembre_2026_EN.pdf`
- `genera_preventivo_navetta_matrimonio_reggello.py` — rigenera entrambi i PDF
- `preventivo_navetta_matrimonio_25-26_settembre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-25_Matrimonio-Reggello/`.

La richiesta è arrivata senza intestatario, quindi lo script non ha un cliente predefinito:
in mancanza di `--cliente` scrive *«Preparato per il vostro matrimonio a Reggello»*. Appena
si sa il nome, i due PDF vanno rigenerati:

```bash
python3 genera_preventivo_navetta_matrimonio_reggello.py --lingua it --cliente "Nome"
python3 genera_preventivo_navetta_matrimonio_reggello.py --lingua en --cliente "Nome"
```

---

## Che cosa ha chiesto il cliente

| | |
|---|---|
| Venerdì 25 settembre | andata entro le 18:00, rientro alle 23:00 |
| Sabato 26 settembre | andata entro le 15:30, rientro all'01:00 |
| Destinazione | Via Bonsi 47, Reggello (FI) |
| Ospiti | 54, distribuiti su 12 indirizzi |

Tutti e dodici gli indirizzi sono nel comune di Reggello: distanze corte, ma dodici punti
di raccolta e due rientri notturni.

## Prezzi

| Voce | Netto |
|---|---|
| Ven 25 set — andata e rientro notturno, tre giri per verso | € 1.480,00 |
| Sab 26 set — andata e rientro notturno, tre giri per verso | € 1.560,00 |
| Supplemento rientro oltre le 02:00, notte fra sabato e domenica | € 250,00 |
| Vitto e alloggio conducente, 2 notti | a carico del cliente |

**Totale netto € 3.290,00 · IVA 10% € 329,00 · Totale € 3.619,00** — **riferito a un mezzo.**

Acconto 30% € 1.090,00 — saldo € 2.529,00.

## Come sono stati costruiti i prezzi

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come
questo. Riportato al netto:

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Le Filigare vale € 809 per 80 km e 5 ore. Qui il mezzo è impegnato circa 11 ore il venerdì
e 12 il sabato, con sei attraversamenti di Reggello per giornata, lavoro fra mezzanotte e
le quattro del mattino e nessun rientro in base fra un servizio e l'altro. Più del doppio
della giornata Le Filigare in ore, quindi un prezzo poco sopra il doppio. Il sabato costa
€ 80 in più del venerdì perché l'attesa fra andata e rientro è di nove ore e mezza contro
cinque e la giornata si chiude alle 03:45.

**Non sono stati usati i prezzi del Corte Francigena** (GM-2026-0819-CF): sono importi per
mezzo su un lavoro a due mezzi, già scontati per volume, e su un lavoro singolo
schiaccerebbero il prezzo sotto mercato.

Nel dubbio il prezzo è stato tenuto alto, come da regola: Girolamo lo abbassa se serve.

## Il punto vero: 54 ospiti e 26 posti

Il Beluga porta 26 passeggeri. Gli ospiti sono 54. Con un mezzo solo servono **tre giri per
ogni spostamento**, e le conseguenze sono pesanti:

- **Andata di venerdì.** I primi ospiti vengono presi alle 15:05 e sono in Via Bonsi alle
  15:45, oltre due ore prima degli ultimi.
- **Rientro della notte fra sabato e domenica.** L'ultimo gruppo lascia la festa alle 02:55,
  quasi due ore dopo l'orario chiesto dal cliente, e arriva a casa verso le 03:45.

Come da regola, **il preventivo quota comunque un solo Beluga**, spiega la capienza reale,
segnala il problema al cliente e chiede la decisione. Nel preventivo il punto è la prima
cosa che si legge dopo la descrizione del mezzo, ed è la prima delle note.

**Che cosa cambia con più mezzi:**

| Mezzi | Andata | Rientro |
|---|---|---|
| 1 | tre giri, oltre due ore fra il primo e l'ultimo ospite | ultimo a casa alle 03:45 (sabato) |
| 2 | due giri in parallelo più un giro di coda, poco più di un'ora | chiusura verso le 02:00 |
| 3 | un giro solo, quaranta minuti | ultimo a casa verso l'01:50, niente supplemento |

**La raccomandazione messa nel preventivo è tre mezzi il sabato e almeno due il venerdì.**

## I mezzi aggiuntivi — decisione di Girolamo

Il preventivo **non quota** il secondo e il terzo minibus e **non anticipa nessuna cifra**:
dice solo che il preventivo per i mezzi in più arriva appena il cliente risponde.

Il Tourengo è di Francesco, non di GiroMunna: il costo va concordato con lui
(Tuscany T.O. & Munna Bus Operator, Montecatini Terme, `infomunnabus@gmail.com`) prima di
mettere qualsiasi numero per iscritto, e le sue tariffe sono all'ingrosso, quindi vanno
ricaricate. Per il terzo mezzo vale lo stesso.

Mancano diciassette giorni: se si va a due o tre mezzi, la telefonata a Francesco è la prima
cosa da fare.

## I tre giri di raccolta

Il raggruppamento è fatto a tavolino sulla toponomastica di Reggello, per zona:

| Giro | Indirizzi | Ospiti |
|---|---|---|
| 1 · Pietrapiana | Via Casalino 66 (14), Hotel Archimede, Ponte di Casalino 68 (7), Loc. Rovai 26 (3) | 24 |
| 2 · La Romola e i poderi | Podere la Romola 78 (14), Podere Houston/Giusti, Loc. Giusti 105 (4), I Trebbiali 116 (2), Via dei Glicini 14, Poggio ai Giubbiani (2) | 22 |
| 3 · Reggello, Donnini e San Giovenale | La Terrazza, Via di Fano 6 (2), Appartamento Olivella, Via Fornacina 32 (2), Loc. S. Giovenale 55 (2), Le Siepi, Montanino 16 (1), Villa Pitiana, Donnini (1) | 8 |

Il primo giro è il più fortunato: 24 ospiti su tre fermate vicine, quasi un mezzo pieno in
una volta. Il terzo è il peggiore: otto ospiti su cinque fermate sparse fra il centro,
Donnini e San Giovenale. È quello da togliere per primo se arriva un secondo mezzo.

**Il raggruppamento va verificato su strada prima della conferma.** Sulla carta funziona,
ma i tempi di percorrenza sono stime.

## Le due notti del conducente

Servono davvero. Reggello dista circa 90 km da Ponte Buggianese, il venerdì si finisce
all'01:45 e la domenica alle 03:45, e il sabato si riparte alle 12:40: il rientro in base
fra un servizio e l'altro sforerebbe i tempi di riposo.

A preventivo sono **indicate ma non conteggiate**, con la dicitura *a carico vostro* al
posto della cifra, la voce fra il non incluso e la nota che spiega perché servono. Il
suggerimento dato al cliente è di sistemare il conducente nella stessa struttura degli
ospiti.

## Margine

Preventivo costruito sul **mezzo di proprietà**. Costo diretto stimato € 300-400 a giornata
— sono giornate lunghe e notturne, non giornate normali — senza l'alloggio che paga il
cliente: il margine sulle due giornate è buono.

**Se si subappalta a Francesco** anche il primo mezzo, il costo sale sui € 700-800 al giorno
per giornate di questo tipo e il margine si assottiglia parecchio: in quel caso i prezzi
vanno rivisti al rialzo del 20-25% prima di inviare.

## Verifiche di accesso

- Reggello non ha ZTL né permesso comunale per i bus turistici: nessun onere di accesso.
- Non si tocca né Firenze centro né Siena, quindi niente permessi a parte.
- **Via Bonsi 47 è da verificare**: è una via del paese e serve sapere dove ferma e gira un
  mezzo di 7,64 m, e dove sosta durante la festa (cinque ore il venerdì, nove e mezza il
  sabato).

## Da chiarire prima di inviare

1. **Nome e indirizzo del cliente.** La richiesta è arrivata senza intestatario: i PDF vanno
   rigenerati con `--cliente "Nome"`.
2. **Quanti mezzi.** Decisione di Girolamo, previo accordo con Francesco sul costo del
   secondo e del terzo minibus.
3. **Il punto esatto sulla mappa dei dodici indirizzi.** Diversi sono poderi su strade
   strette, a volte bianche e senza spazio di manovra: da verificare soprattutto La Romola,
   I Trebbiali, Poggio ai Giubbiani e Località Giusti. Dove il mezzo non arriva, si concorda
   un punto di ritrovo sulla strada asfaltata.
4. **Via Bonsi 47**: punto di salita e discesa, spazio di manovra, sosta durante la festa.
5. **Gli orari delle 18:00 e delle 15:30.** Letti come l'ora entro cui gli ospiti devono
   essere in Via Bonsi. Se sono l'ora della cerimonia, i giri si spostano.
6. **Il supplemento oltre le 02:00** è a preventivo per la notte fra sabato e domenica.
   Se si va a tre mezzi va tolto.
7. **Bloccare il mezzo** per il 25-27 settembre e le due notti del conducente in zona.

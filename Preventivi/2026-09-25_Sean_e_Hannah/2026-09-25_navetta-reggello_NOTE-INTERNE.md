# Note interne — Navetta matrimonio Reggello 25.09.2026, 50 ospiti

**Cliente:** Sean e Hannah · **Rif. preventivo:** GM-2026-0925-REGGELLO · **Preparato:** 8 settembre 2026 · **Validità:** 15 settembre 2026

Location: Fattoria I Bonsi, Via Bonsi 47, Reggello (FI). Due minibus, quattro corse di
raccolta e quattro di rientro, undici punti di carico.

File generati:

- `GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25_settembre_2026_EN.pdf`
- `genera_preventivo_navetta_reggello.py` — rigenera entrambi i PDF
- `preventivo_navetta_matrimonio_reggello_25_settembre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-25_Sean_e_Hannah/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_navetta_reggello.py --lingua it
python3 genera_preventivo_navetta_reggello.py --lingua en
```

Il cliente predefinito è «Sean e Hannah» in italiano e «Sean and Hannah» in inglese;
con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Da dove viene questo preventivo

Il preventivo inglese era già stato preparato ed è arrivato in chat come PDF. Qui è stato
**ripreso alla lettera** — stessi orari, stessi prezzi, stessi testi — e portato nel formato
della casa (logo, verde e oro, intestazione e piè di pagina su ogni pagina), più la versione
italiana che mancava. Nessun importo e nessuna condizione sono stati cambiati di iniziativa:
i punti che si discostano dalle regole della casa sono elencati qui sotto, così la decisione
resta a Girolamo.

## Prezzi

| Voce | Netto |
|---|---|
| Mezzo 1 (minibus 25+1+1) — 2 corse di raccolta, a disposizione 18:00-23:00, 2 corse di rientro | € 1.100,00 |
| Mezzo 2 (minibus 27+1+1) — 2 corse di raccolta, a disposizione 18:00-23:00, 2 corse di rientro | € 1.100,00 |

**Totale netto € 2.200,00 · IVA 10% € 220,00 · Totale € 2.420,00**

Acconto 30% € 726,00 — saldo € 1.694,00 entro il 20 settembre 2026.

## Impegno reale dei mezzi

Partenza dalla rimessa verso le 15:15 (Ponte Buggianese → Reggello, ~70 km, un'ora scarsa),
primo ritiro alle 16:20, ultimo rientro intorno alle 00:25, ritorno in rimessa verso l'01:30.
Sono **circa dieci ore di impegno per conducente** e **200-230 km per mezzo** compresa la
movimentazione, con lavoro in orario notturno.

## Il prezzo rispetto ai riferimenti

- **Le Filigare (GM-2026-0821-LF)**, mezzo singolo: € 809 netti per una giornata a
  disposizione di ~80 km e 5 ore; € 500 netti per un trasferimento di ~50 km.
- **Corte Francigena (GM-2026-0819-CF)**, due mezzi: € 550 per mezzo per una giornata a
  disposizione, € 1.300 per mezzo per un trasferimento da 208 km — importi già scontati per
  volume, validi solo per lavori a due mezzi come questo.

Sulla scala Le Filigare, dieci ore e ~215 km con rientri notturni starebbero fra € 1.400 e
€ 1.600 netti a mezzo. Gli € 1.100 attuali sono uno **sconto volume di circa il 25%** sul
mezzo singolo: coerente con la logica del Corte Francigena, ma è il limite basso. Se il
secondo mezzo viene preso da Francesco a € 600-700, sul Mezzo 2 restano € 400-500 di
margine, che per una serata che finisce all'01:30 è poco.

**Se il preventivo non è ancora partito**, portare le due righe a € 1.250 (totale netto
€ 2.500, totale € 2.750) resta dentro mercato per due minibus con conducente su una serata
di matrimonio con rientri dopo la mezzanotte.

## Punti che si discostano dalle regole della casa

1. **Il secondo mezzo va concordato con Francesco.** Il Mezzo 2 (27+1+1) è il Tourengo di
   Francesco Munna: GiroMunna ha in proprietà solo il Beluga. Il costo del secondo minibus
   va concordato con lui **prima** che il preventivo diventi impegnativo.
2. **Fasce di cancellazione diverse dallo standard.** Qui: gratuita oltre 30 giorni, da 30 a
   10 giorni acconto trattenuto, da 10 a 3 giorni 70%, ultime 72 ore 100%. Lo standard della
   casa è 60/30/10 con 50% nella fascia intermedia. La scelta ha senso vista la data vicina
   (16 giorni al servizio), ma è una deroga: va tenuta a mente se il cliente confronta con
   altri nostri preventivi.
3. **Il riferimento non segue lo schema.** `GM-2026-0925-REGGELLO` invece di
   `GM-2026-0925-SH` (o `-IB` per I Bonsi). È stato lasciato com'è perché il documento
   inglese è già stato preparato con questo numero: cambiarlo ora creerebbe confusione se
   il cliente lo ha già ricevuto.
4. **Vitto del conducente.** La regola della casa vuole una riga nella tabella del prezzo con
   *a carico vostro*. Qui non c'è pernottamento (si rientra in rimessa la notte stessa) e la
   cena dei due autisti compare solo fra le voci non incluse. Se si rifà il documento, meglio
   esplicitarla: due cene per una serata che va dalle 15:15 all'01:30.
5. **I mezzi non sono nominati.** Nel documento sono «minibus Mercedes-Benz 25+1+1 e
   27+1+1». La casa vuole il **Beluga** nominato e descritto (26 posti passeggeri più
   l'autista, 7,64 m): la compattezza sotto gli 8 metri è un argomento di vendita, e su
   queste strade collinari è proprio il punto. Le cifre 25+1+1 e 27+1+1 tengono un posto per
   il capogruppo su ciascun mezzo, quindi la capienza dichiarata è 52 invece di 54.
6. **Il PDF ricevuto era senza logo** e senza l'intestazione della casa. Le due versioni
   generate qui lo hanno.

## Da verificare

1. **Costo del secondo mezzo con Francesco** — è la voce che decide il margine.
2. **Accessibilità degli undici punti di carico.** Case coloniche su strade strette a
   Pietrapiana, Donnini e Cascia: dove il minibus non gira, serve un punto d'incontro.
3. **Posizione esatta di Loc. Podere la Romola 78 e Loc. Giusti 105** — 18 ospiti su 50
   stanno su questi due indirizzi.
4. **Numero definitivo degli ospiti.** 50 su 52 posti: due di margine, non uno di più.
5. **Bloccare i due mezzi per la sera del 25 settembre**, se non è già stato fatto.
6. **Validità al 15 settembre**: sono sei giorni da oggi. Oltre quella data il preventivo va
   riemesso, e con meno di dieci giorni al servizio la fascia di cancellazione cambia ancora.

---

# Il piano del sabato mandato dal cliente (9 settembre)

Documento del cliente: `cliente_Loading_Points_Saturday.pdf` — «Guest Pickup — Loading Points
& Timings · SATURDAY — WEDDING DAY». Arrivato con la domanda se conosciamo qualcuno
disponibile **il sabato**.

## Cosa chiede

**10 punti di carico · 54 ospiti · arrivo in location entro le 15:30 · partenza dalla
location all'01:00.**

| # | Punto di carico | Ospiti |
|---|---|---|
| 1 | Hotel Archimede, Via Ponte di Casalino 68 | 7 |
| 2 | Podere Casalino, Via Ponte di Casalino 66 | 14 |
| 3 | Podere Giusti, Loc. Giusti 105 | 5 |
| 4 | Podere la Romola, Loc. Podere la Romola 78 | 14 |
| 5 | Rovai, Loc. Rovai 26, Pietrapiana | 3 |
| 6 | La Terrazza di Reggello, Via di Fano 6 | 2 |
| 7 | Appartamento Olivella, Via Fornacina 32 | 2 |
| 8 | Via dei Glicini 14, Poggio ai Giubbiani | 2 |
| 9 | I Trebbiali, Loc. I Trebbiali 116 | 3 |
| 10 | San Giovenale, Loc. S. Giovenale 55 | 2 |
| | **Totale** | **54** |

**Andata, arrivo previsto 15:30**

| Mezzo | Corsa | Percorso | Ospiti | Partenza | Arrivo |
|---|---|---|---|---|---|
| Bus 1 | B | I Trebbiali → Podere la Romola | 17 | ~14:35 | 14:55 |
| Bus 2 | C | Via dei Glicini → Via Fornacina → Podere Giusti → S. Giovenale → Via di Fano → Hotel Archimede | 20 | ~14:45 | 15:30 |
| Bus 1 | A | Podere Casalino → Rovai | 17 | ~15:05 | 15:30 |

**Rientro, partenza dalla location all'01:00**

| Mezzo | Corsa | Percorso | Ospiti | Partenza | A casa |
|---|---|---|---|---|---|
| Bus 1 | A | Podere Casalino → Rovai | 17 | 01:00 | ~01:25 |
| Bus 2 | C | Hotel Archimede → Via di Fano → S. Giovenale → Podere Giusti → Via Fornacina → Via dei Glicini | 20 | 01:00 | ~01:40 |
| Bus 1 | B | I Trebbiali → Podere la Romola | 17 | ~01:35 | ~01:55 |

## Compatibilità con il servizio

**Sui mezzi il piano regge.** Le corse sono sfalsate e la punta massima è di 20 passeggeri
su una corsa: 17 e 17 sul Bus 1, 20 sul Bus 2. I due minibus del preventivo (25 e 27 posti)
bastano, i 54 ospiti non sono un problema perché non viaggiano mai tutti insieme. Il limite
dei 52 posti scritto fra le voci non incluse riguarda il trasporto in un'unica soluzione,
non questo schema a tre corse.

**Ma non è il servizio del preventivo. È un secondo servizio, su un altro giorno.**

1. **Giorno diverso.** Il preventivo GM-2026-0925-REGGELLO è per **venerdì 25 settembre**.
   Questo documento è intestato «SATURDAY — WEDDING DAY», quindi **sabato 26**. Da chiarire
   subito: il venerdì è un evento a parte e ne vogliono due, oppure il giorno del matrimonio
   è il sabato e la richiesta di partenza era sbagliata? Cambia tutto, compreso a quale
   giorno si riferisce l'acconto.
2. **Ospiti 54 invece di 50**, su 10 punti di carico invece di 11.
3. **Orari molto più lunghi.** Il venerdì: raccolta dalle 16:20, mezzi in location dalle
   18:00 alle 23:00, ultimo rientro alle 00:25. Il sabato: raccolta dalle 14:35, mezzi fermi
   in location **dalle 15:30 all'01:00, nove ore e mezza**, ultimo rientro all'01:55.
4. **Impegno reale del sabato:** partenza dalla rimessa verso le 13:30, ritorno in rimessa
   intorno alle **03:00**. Sono circa **13,5 ore per conducente**, contro le 10 del venerdì.
5. **Rientro dopo le 02:00.** I mezzi lasciano l'ultimo indirizzo verso le 01:55 e rientrano
   in rimessa dopo le 02:00: scatta la condizione dei **€ 250,00 per mezzo**.
6. **All'01:00 non partono tutti.** I due mezzi portano via 37 ospiti su 54: gli ultimi 17
   restano in location fino alle 01:35 circa. Va detto, perché è l'unico punto del piano che
   il cliente potrebbe non aver messo in conto.
7. **Due giorni di fila.** Se vogliono venerdì *e* sabato, fra il rientro del venerdì
   (~01:30) e la partenza del sabato (~13:30) restano dodici ore di riposo: si può fare, ma
   sono due notti consecutive per gli stessi due autisti.

**Il sabato non si può quotare al prezzo del venerdì.** Sono 3,5 ore in più di impegno per
mezzo, con rientro oltre le 02:00. Partendo dagli € 1.100 del venerdì, il sabato non sta
sotto i € 1.400-1.500 netti a mezzo, più i € 250 per mezzo del rientro notturno.

## Stato

Girolamo risponde che **la disponibilità è solo quella del preventivo** e che la conferma la
dà l'acconto. Il piano del sabato resta qui archiviato: se lo vorrà quotare, i numeri sopra
sono già pronti.

# Note interne — Navetta matrimonio Reggello 25.09.2026, 50 ospiti

**Cliente:** Sean e Hannah · **Rif. preventivo:** GM-2026-0925-REGGELLO · **Preparato:** 8 settembre 2026 · **Validità:** 15 settembre 2026

Location: Fattoria I Bonsi, Via Bonsi 47, Reggello (FI). Due minibus, quattro corse di
raccolta e quattro di rientro, undici punti di carico.

File nella cartella:

- `..._programma_aggiornato_IT.pdf` e `..._programma_aggiornato_EN.pdf` — **la versione da
  mandare**: programma rifatto sullo schema del venerdì del cliente, **stesso prezzo**
  € 2.420 IVA inclusa, acconto € 726.
- `GiroMunna_Preventivo_Navetta_Matrimonio_Reggello_25_settembre_2026_IT.pdf` e `..._EN.pdf` —
  la versione mandata l'8 settembre, tenuta per memoria di cosa ha ricevuto il cliente.
- `cliente_Loading_Points_Friday.pdf` — lo schema del cliente per il **venerdì 25, welcome
  event**: 9 punti di carico, 50 ospiti, arrivo 18:00, partenza 23:00. È il nostro servizio.
- `cliente_Loading_Points_Saturday.pdf` — lo schema del **sabato 26, giorno del matrimonio**:
  10 punti, 54 ospiti, 15:30-01:00. Non lo facciamo.
- `genera_preventivo_navetta_reggello.py` — rigenera i due PDF in vigore.
- `preventivo_navetta_matrimonio_reggello_25_settembre_2026.html` — la pagina web bilingue.

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

## Prezzi della prima versione (revisione 1, mandata l'8 settembre)

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

# I due schemi mandati dal cliente (9 settembre)

Il cliente ha mandato due fogli di punti di carico, e sono **due eventi diversi in due giorni
diversi**:

| | `cliente_Loading_Points_Friday.pdf` | `cliente_Loading_Points_Saturday.pdf` |
|---|---|---|
| Intestazione | FRIDAY — WELCOME EVENT | SATURDAY — WEDDING DAY |
| Giorno | venerdì 25 settembre | sabato 26 settembre |
| Punti di carico | 9 | 10 |
| Ospiti | 50 | 54 |
| Orari | arrivo 18:00, partenza 23:00 | arrivo 15:30, partenza 01:00 |
| Ultimo rientro | ~23:55 | ~01:55 |
| | **è il nostro servizio** | non lo facciamo |

Girolamo ha risposto che è disponibile **solo il 25**, quindi il sabato resta fuori.

## Il venerdì 25: il preventivo mandato regge

| | Preventivo mandato | Schema vero del venerdì |
|---|---|---|
| Ospiti | 50 | 50 |
| Punti di carico | 11 | **9** |
| Arrivo in location | entro le 18:00 | entro le 18:00 |
| Mezzi in location | 18:00-23:00 | 18:00-23:00 |
| Primo ritiro | 16:20 | **17:05** |
| Corse | 4 andata + 4 rientro | **3 andata + 3 rientro** |
| Ultimo ospite a casa | 00:25 | **~23:55** |

**Il servizio vero è più leggero di quello quotato**: due punti di carico in meno, due corse
in meno, si parte 45 minuti più tardi e si finisce mezz'ora prima. Gli orari a preventivo —
18:00-23:00 — sono esattamente quelli richiesti. Il preventivo non va toccato, e non c'è
nessuna attesa fuori orario da addebitare: quella questione riguardava lo schema del sabato,
che non facciamo.

**Punti di carico del venerdì:** Casalino, fermata unica per Hotel Archimede (3) e Podere
Casalino, Via Ponte di Casalino 66 (15) = 18 · Podere Giusti (4) · Podere la Romola (14) ·
Rovai (3) · La Terrazza di Reggello (2) · Appartamento Olivella (2) · Via dei Glicini (2) ·
I Trebbiali (3) · S. Giovenale (2). Totale 50.

Rispetto al preventivo spariscono **Villa Pitiana** e **Le Siepi/Montanino**: quei due ospiti
sono adesso a Casalino e a I Trebbiali. Il totale resta 50.

**Le corse:** Bus 1 corsa B, I Trebbiali → Podere la Romola, 17 ospiti, 17:05 → 17:25 · Bus 2
corsa C, Via di Fano → S. Giovenale → Podere Giusti → Via Fornacina → Via dei Glicini, 12
ospiti, 17:25 → 18:00 · Bus 1 corsa A, Casalino → Rovai, 21 ospiti, 17:35 → 18:00. Rientri
dalle 23:00 con lo stesso schema: gli ultimi 17 di Podere la Romola e I Trebbiali partono
alle 23:35 e sono a casa verso le 23:55.

**Sui posti nessun problema:** la corsa più carica è quella del Bus 1 con 21 ospiti su 25
posti.

## Due orari da sistemare con il cliente

Non cambiano il prezzo, ma sul campo contano:

- **Corsa C del Bus 2**: cinque fermate fra le 17:25 e le 18:00. Sono 35 minuti per Via di
  Fano, S. Giovenale, Podere Giusti, Via Fornacina e Via dei Glicini, più il tratto fino in
  location. Conviene partire alle 17:10.
- **Corsa A del Bus 1**: parte dalla location alle 17:35 e deve caricare 18 persone a Casalino
  e 3 a Rovai ed essere di ritorno per le 18:00. Venticinque minuti per 21 persone a due
  fermate sono pochi: meglio partire alle 17:20.
- **Al rientro delle 23:00 non partono tutti**: 33 ospiti sui 50; gli ultimi 17 restano in
  location fino alle 23:35. Va detto prima, non la sera stessa.

## La revisione 2 è stata tolta

Era stata costruita sullo schema del sabato credendo fosse lo stesso servizio del 25: orari
15:30-01:00, 54 ospiti, € 1.450 netti a mezzo. Adesso che i due giorni sono distinti quel
documento non ha più senso — e intestato al venerdì sarebbe pericoloso, perché qualcuno
potrebbe mandarlo per sbaglio. Rimosso dalla cartella.

**Restano validi i suoi numeri se un domani si dovesse quotare il sabato:** € 1.450-1.500
netti a mezzo per 13,5 ore di impegno con rientro alle due, cioè € 3.190-3.300 IVA inclusa
per i due mezzi, più la cena dei conducenti a carico del cliente e i € 250 per mezzo se si
sfora l'02:00.

## Stato — 9 settembre

**Vale il prezzo del preventivo mandato l'8 settembre: € 2.420 IVA inclusa, acconto € 726.**
Su richiesta di Girolamo è stato rifatto il programma, allineato allo schema del venerdì del
cliente, e adesso il documento include anche **l'IBAN e i dati bancari completi**, così il
cliente può pagare l'acconto senza aspettare un secondo messaggio.

Cosa dice il documento in vigore, oltre al programma allineato (vedi sotto):

- **Coordinate bancarie in chiaro** nella sezione Pagamento: bonifico intestato a Munna
  Girolamo Giuseppe, IBAN IT59 O053 4137 0700 0000 0034 24, BIC/SWIFT BAPPIT21S05, causale
  con nome cliente e riferimento GM-2026-0925-REGGELLO. Prima diceva solo «le coordinate
  bancarie vengono inviate con la richiesta di conferma»: adesso non serve un secondo giro.
- Il testo di chiusura non promette più di mandare l'IBAN in un secondo momento: dice che è
  già sopra e che la conferma arriva appena l'acconto risulta accreditato.

Cosa cambia rispetto alla versione mandata l'8 settembre, a parità di prezzo:

- **nove punti di carico invece di undici**: spariscono Villa Pitiana e Le Siepi/Montanino,
  quei due ospiti sono a Casalino (18) e a I Trebbiali (3);
- **tre corse di raccolta e tre di rientro** invece di quattro e quattro;
- gli orari del cliente, con **due partenze anticipate di un quarto d'ora**: il Mezzo 2 alle
  17:10 invece che alle 17:25, perché cinque fermate in 35 minuti non tengono, e la seconda
  corsa del Mezzo 1 alle 17:20 invece che alle 17:35, perché sono 21 persone a due fermate;
- **Rovai e Casalino invertiti** all'andata: Casalino è a tre minuti dalla location ed è la
  fermata da 18 ospiti, servirla per ultima tiene quelle 18 persone a bordo tre minuti invece
  di venti. Al rientro l'ordine resta quello naturale;
- la **cena dei due conducenti** in tabella con la dicitura *a carico vostro*, come vuole la
  regola della casa;
- la riga dei «più di 52 ospiti» riscritta sulla capienza della singola corsa;
- scritto che **alle 23:00 partono 33 ospiti sui 50** e gli ultimi 17 restano alla festa fino
  alle 23:35.

Il servizio è più leggero di quello quotato l'8 settembre — due punti e due corse in meno, si
parte più tardi e si finisce prima — quindi a € 2.420 il lavoro sta in piedi bene.

### Sulla wedding planner (9 settembre)

Ha contattato Girolamo offrendo di girare i contatti; risentiti per telefono, lei ha detto che
non può aggiungere una sua percentuale visto che il preventivo era già stato fatto
direttamente con Sean e Hannah. **Girolamo ha deciso di non riconoscerle nulla di tasca sua**:
nessun impatto sul prezzo del cliente. Da valutare solo se in futuro porta altri lavori, nel
qual caso la commissione andrebbe messa a preventivo fin dall'inizio.

Resta da fare:

1. **Riconcordare con Francesco** il costo del secondo mezzo.
2. **Farsi confermare la posizione** di Podere la Romola e Loc. Giusti: 18 ospiti sui 50.
3. **Bloccare i due mezzi** per la sera del 25.
4. La validità resta il **15 settembre**: dopo va riemesso, e sotto i dieci giorni la
   cancellazione passa al 70%.

# Note interne — Giornata sul Monte Amiata, sab 22.08.2026, Castel del Piano (GR)

**Cliente:** da identificare (gruppo al Grand Hotel Impero, Castel del Piano) · **Rif. preventivo:**
GM-2026-0822-GI · **Preparato:** 21 agosto 2026 · **Validità:** 21 agosto 2026, ore 20:00

File generati:
- `GiroMunna_Preventivo_Monte_Amiata_22_agosto_2026_IT.pdf`
- `GiroMunna_Preventivo_Monte_Amiata_22_agosto_2026_EN.pdf`
- `genera_preventivo_monte_amiata.py` — rigenera entrambi i PDF
- `preventivo_monte_amiata_22_agosto_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-08-22_Grand-Hotel-Impero/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_monte_amiata.py --lingua it
python3 genera_preventivo_monte_amiata.py --lingua en
```

Il cliente predefinito è `Grand Hotel Impero, Castel del Piano`, che è un ripiego: appena si sa
chi è davvero, si rigenera con `--cliente "Nome vero"`.

---

## Regole ferme per ogni preventivo (Girolamo, ripetuto più volte)

1. **Solo a nome GiroMunna.** Il cliente non deve mai sapere di chi sono i mezzi. Il Tourengo si
   presenta come un secondo minibus, punto — niente Francesco, niente Tuscany T.O., niente
   spiegazioni sull'accordo fra fratelli. Tolto ovunque dal documento cliente.
2. **Niente km, tempi o logistica di dettaglio.** Il preventivo cliente dice solo: mezzi,
   giornata, prezzo. Niente tabella tappe, niente itinerari inventati, niente spiegazioni del
   perché di un prezzo (trasferimenti, provenienza dei mezzi, logistica). Quel ragionamento
   resta solo qui e nella sezione "Interno" della pagina web.
3. **Niente trasferimenti a parte in fattura.** Tolta la riga da € 150 per mezzo: il prezzo per
   la giornata è unico, il trasferimento non si vede.

Valgono sempre, anche per i prossimi preventivi.

## Il programma vero (Girolamo, 21 agosto sera)

Le stesure precedenti di questo preventivo avevano il programma sbagliato più di una volta:
prima si pensava che il ritiro dall'ospedale fosse per sabato mattina insieme alla gita; poi,
corretto quel punto, mancavano ancora i dettagli veri di oggi. Il programma completo, spiegato
da Girolamo:

- **Oggi, venerdì 21 agosto**
  - **09:00 – 11:00 circa** — ritiro della signora dimessa dall'ospedale, che si trova al Grand
    Hotel Impero di Castel del Piano: andata e ritorno da Corte Francigena. **Già fatto
    stamattina**, non è più un servizio da fare domani.
  - **17:00 – 23:00/23:30 circa** — partenza per **Podere Le Ripi e Serendipity** (serata),
    per il cliente di Corte Francigena. Rientro previsto fra le 23:00 e le 23:30.
- **Domani, sabato 22 agosto** — **due minibus**, Beluga e Tourengo, con partenza da Corte
  Francigena in direzione Monte Amiata e rientro a Corte Francigena. Orario di partenza ancora
  da decidere, lasciato apposta aperto nel preventivo (vedi sotto).

**Conseguenza pratica:** questo preventivo riguarda **solo la gita di domani sull'Amiata**, con
i due mezzi. Il servizio dell'ospedale e la serata di stasera sono lavoro di oggi, per lo più già
fatto o in corso: non c'entrano con questo documento, restano solo qui come programma interno
per calcolare correttamente il riposo del conducente prima di domani.

## Come si presenta la giornata di sabato al cliente

Girolamo ha detto esplicitamente di lasciare da decidere l'orario di partenza per l'Amiata, e di
non mettere km/tempi nel documento cliente. Il preventivo ora è molto più semplice: una sola voce
di servizio ("due mezzi da Corte Francigena verso il Monte Amiata, giornata a disposizione,
orario e tappe da concordare") e una di rientro. Niente tabella con tappe, orari intermedi o
chilometri — quelli restano solo qui.

Anche l'itinerario col dettaglio dei borghi (Vetta Amiata, Abbadia San Salvatore, Santa Fiora,
Arcidosso) è stato tolto dal documento cliente: era una proposta inventata da Claude come esempio
di possibile giro, ma non è mai stata confermata né da Girolamo né dal cliente. Meglio non
scriverla come se fosse già decisa. Se Girolamo ha in mente un giro preciso, va aggiunto lui
stesso o va detto esplicitamente a voce, non lasciato scritto a preventivo come fosse già deciso.

Il prezzo non cambia: resta legato alla giornata intera a disposizione, non a un orario di
inizio o a un itinerario specifico.

## Prezzi

| Voce | Netto |
|---|---|
| Sab 22 ago — Beluga: mezzo e conducente a disposizione sul Monte Amiata | € 900,00 |
| Sab 22 ago — Tourengo: mezzo e conducente a disposizione sul Monte Amiata | € 900,00 |
| Vitto dei due conducenti | a carico del cliente |

**Totale netto € 1.800,00 · IVA 10% € 180,00 · Totale € 1.980,00**

Nessuna riga di trasferimento: tolta su istruzione di Girolamo (regola 3 sopra). Nessun acconto,
saldo unico entro il 26 agosto.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**. La giornata sull'Amiata (6h45, montagna) sta
circa il 15% sopra i suoi € 809 per una giornata a disposizione (5h, Siena) — da qui gli € 900,
prezzo unico per mezzo, senza trasferimento in fattura: entrambi i mezzi sono già a Corte
Francigena, il salto è breve e il costo lo assorbe GiroMunna.

## Margine

Beluga: costo diretto stimato € 300-370 su € 900 di ricavo — margine buono, mezzo già in zona.

Tourengo: quotato al cliente allo stesso prezzo del Beluga (decisione di Girolamo), non sulla
tariffa reale di Francesco. **Resta da regolare con Francesco**, separatamente: la tariffa vera
che chiede per il mezzo (da cui dipende il margine di GiroMunna su questa parte) e la
disponibilità sua e del conducente per sabato.

## Se i mezzi devono rientrare alla base

Il prezzo sopra vale se entrambi i mezzi restano in zona (Corte Francigena) anche dopo sabato.
Se uno dei due dovesse invece rientrare alla base di Ponte Buggianese, va riquotato a parte —
non è compreso nei € 1.980,00.

## Ore di guida e di riposo — risolto con l'orario vero

Con la prima versione del programma (fine servizio stasera all'01:00-01:30) il riposo prima di
domani era sotto il minimo di legge, anche nell'ipotesi migliore. **Con l'orario vero le cose
cambiano parecchio.** Fine servizio di stasera (Podere Le Ripi e Serendipity) prevista fra le
**23:00 e le 23:30**:

| Partenza domani | Riposo (fine stasera 23:00) | Riposo (fine stasera 23:30) | In regola? |
|---|---|---|---|
| 08:00 | 9h00 | 8h30 | Al limite o sotto il minimo ridotto (9h) — troppo risicato |
| 09:00 | 10h00 | 9h30 | Sì, con margine |
| 10:00 | 11h00 | 10h30 | Sì, comodo |
| 11:00 e oltre | 12h00+ | 11h30+ | Sì, riposo pieno |

Per stare tranquilli anche se stasera si va per le lunghe, **conviene non far partire il mezzo
domani prima delle 9:30-10:00**: così il riposo è in regola in entrambi gli scenari, senza
bisogno di sapere in anticipo l'ora esatta di rientro di stasera. È anche per questo che ha senso
lasciare la partenza aperta come chiesto da Girolamo, invece di fissarla subito. **Non serve più
il secondo conducente** con questi orari — resta un'opzione solo se stasera si dovesse
prolungare oltre mezzanotte.

## Da chiarire prima di mandare

1. **Tariffa reale del Tourengo da Francesco.** Il cliente è già stato quotato allo stesso
   prezzo del Beluga (decisione di Girolamo); resta da regolare con Francesco il costo vero,
   separatamente e senza impatto sul cliente — condiziona solo il margine di GiroMunna.
2. **Disponibilità del Tourengo e del suo conducente per sabato**, da confermare con Francesco.
3. **Orario di partenza per il monte.** Lasciato apposta senza orario fisso nel documento; va
   comunicato al cliente appena deciso, non prima delle 9:30-10:00 per il riposo del conducente.
4. **I due mezzi a fine giornata tornano a Corte Francigena o alla base?** Se uno resta in zona
   il prezzo sopra regge; se deve rientrare a Ponte Buggianese va riquotato a parte.
5. **Nome e dati del cliente.** La richiesta è arrivata senza intestazione: il PDF va rigenerato
   con `--cliente` quando si sa chi è.
6. **Numero di telefono del cliente: +372 5664 1112.** Recuperato — prefisso estone, probabile
   cellulare/WhatsApp. Da usare solo per la telefonata di conferma di Girolamo.
7. **Distanza Corte Francigena → Castel del Piano.** Stimata in 17 km/25 min da fonti stradali
   generiche su Castelnuovo dell'Abate; da confermare con la percorrenza reale, visto che i
   mezzi sono già lì.
8. **Acconto.** Qui è stato azzerato perché il servizio è a meno di 24 ore. Se si preferisce
   incassare prima, si cambia la tabella del pagamento.

## Storico delle correzioni su questo preventivo

Per tenere traccia di come è cambiato, dato quante volte è stato rifatto in poche ore:

1. **Prima stesura:** ospedale + Amiata come un unico servizio sabato mattina, mezzo dalla base
   di Ponte Buggianese (350 km di riposizionamento). Totale € 1.870,00 IVA inclusa.
2. **Seconda stesura:** corretto il punto di partenza del mezzo, da Ponte Buggianese a Corte
   Francigena (17 km invece di 175). Totale sceso a € 1.320,00.
3. **Terza correzione:** numero di telefono del cliente recuperato (+372 5664 1112), tolto dal
   preventivo l'invito a mandarlo.
4. **Quarta correzione:** su richiesta di Girolamo, la partenza per il monte è stata resa
   flessibile ("a seguire" invece di un orario fisso), perché ancora da decidere.
5. **Quinta correzione, quella buona:** il programma era ancora sbagliato — l'ospedale non è
   sabato mattina, è **già avvenuto oggi** alle 9:00. Rifatto il preventivo per essere solo la
   gita di domani sull'Amiata: tolto il servizio ospedale, ricalcolato il prezzo (€ 1.155,00
   IVA inclusa) e il riposo del conducente, che con l'orario vero (fine stasera verso le 23:00
   invece dell'1:00-1:30) torna comodamente in regola per qualunque orario di partenza
   ragionevole di domani.
6. **Sesta correzione:** aggiunto il Tourengo di Francesco come secondo mezzo, su richiesta
   esplicita di Girolamo. Il suo prezzo non è stato inventato: manca la tariffa all'ingrosso di
   Francesco, quindi in preventivo compare come "a seguire" e il totale ufficiale resta quello
   del solo Beluga (€ 1.155,00 IVA inclusa), in attesa di quel numero.
7. **Settima correzione:** tolti dal documento cliente tutti i km e tempi di dettaglio (tabella
   delle tappe con minuti e chilometri), che non ci dovevano mai essere — vanno solo nei
   programmi interni. Tolto anche l'itinerario inventato con i borghi specifici, mai confermato.
   Corretto anche il programma di oggi con gli orari e i nomi veri (ritiro ospedale 9:00-11:00,
   serata a Podere Le Ripi e Serendipity 17:00-23:00/23:30), da cui il calcolo del riposo del
   conducente per domani è stato rifatto con un margine di sicurezza (partenza consigliata non
   prima delle 9:30-10:00).
8. **Ottava correzione:** confermato che anche il Tourengo è già a Corte Francigena come il
   Beluga. Girolamo ha chiesto di completare subito il preventivo per due mezzi: il Tourengo è
   stato quotato al cliente allo stesso prezzo del Beluga (€ 900 + € 150 trasferimento), per
   decisione di Girolamo, non calcolato sulla tariffa reale di Francesco — quella resta da
   regolare fra loro due separatamente. Totale: € 2.310,00 IVA inclusa per due mezzi.
9. **Nona correzione, sui toni forti:** il documento dava ancora troppi dettagli al cliente.
   Tolto ovunque chi possiede i mezzi (mai più il nome di Francesco o di Tuscany T.O.: il
   preventivo è solo a nome GiroMunna) e tolte le righe di trasferimento da € 150 a mezzo, che
   non vanno in fattura. Il servizio ora è una riga sola per mezzo, un prezzo, nessuna
   spiegazione del perché. **Totale finale: € 1.980,00 IVA inclusa** per due mezzi. Le regole
   in cima a questo file valgono per tutti i prossimi preventivi, non solo per questo.

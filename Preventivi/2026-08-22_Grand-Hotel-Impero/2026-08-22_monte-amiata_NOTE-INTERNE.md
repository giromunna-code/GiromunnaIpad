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

## Regola: km e orari di dettaglio solo nei programmi interni

Girolamo l'ha ripetuto più volte: **le voci di km e tempi non vanno mai nel documento per il
cliente.** Vanno solo qui, nei programmi interni (questo file e la sezione "Interno" della
pagina web), che sono gli strumenti di lavoro di Girolamo — non nel preventivo che legge il
cliente. Il preventivo cliente descrive il servizio (mezzi, giornata, prezzo); il programma
interno descrive il lavoro vero, con orari, tappe e chilometri. Da questa versione in poi vale
sempre così, anche per i prossimi preventivi.

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
| Sab 22 ago — Beluga: mezzo e conducente a disposizione sul Monte Amiata, circa 6h45 | € 900,00 |
| Trasferimento del Beluga da e per Corte Francigena, Castelnuovo dell'Abate, ~34 km a vuoto | € 150,00 |
| Sab 22 ago — Tourengo: mezzo e conducente a disposizione sul Monte Amiata, circa 6h45 | € 900,00 |
| Trasferimento del Tourengo da e per Corte Francigena, Castelnuovo dell'Abate, ~34 km a vuoto | € 150,00 |
| Vitto dei due conducenti | a carico del cliente |

**Totale netto € 2.100,00 · IVA 10% € 210,00 · Totale € 2.310,00**

Nessun acconto: il servizio è a meno di 24 ore, si è messo saldo unico entro il 26 agosto.

## Il secondo minibus: il Tourengo di Francesco — prezzo allineato al Beluga

Girolamo ha confermato che **entrambi i mezzi sono già a Corte Francigena** — non solo il
Beluga — e ha chiesto di completare il preventivo per due minibus senza aspettare oltre la
tariffa di Francesco. Il Tourengo è stato quindi quotato al cliente **allo stesso prezzo del
Beluga** (€ 900 giornata + € 150 trasferimento): è una scelta di Girolamo, non un numero
calcolato sulla tariffa reale di Francesco.

**Resta comunque da regolare con Francesco**, separatamente e senza impatto sul cliente:
1. **La tariffa reale** che Francesco chiede a GiroMunna per il Tourengo — da cui dipende il
   margine sulla parte Tourengo di questo lavoro.
2. **La disponibilità sua e del conducente** per sabato.

Il preventivo Corte Francigena (a due mezzi) resta utile come controllo, una volta nota la
tariffa vera di Francesco, per verificare che il margine complessivo sia in linea con gli altri
lavori a due mezzi.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**, a mezzo singolo come questo.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Con l'ospedale fuori dal conto, la giornata sull'Amiata (6h45, tutta su strade di montagna) sta
circa il **15% sopra** gli € 809 di Le Filigare — un'ora e 45 in più di disposizione, con il
premio "strade di montagna" che ora si applica a tutta la durata e non solo a una parte. Da qui
gli **€ 900**.

Il **trasferimento** da Corte Francigena resta a **€ 150** per i ~34 km andata e ritorno: è
un salto breve (17 km a tratta), il mezzo è già in zona per l'altro cliente. Non ha senso la
tariffa del riposizionamento lungo (~€ 1,86/km usata per i 350 km dalla base): si è tenuta una
cifra minima che copre più il tempo del conducente che il gasolio.

**Non è stato usato il Corte Francigena (GM-2026-0819-CF) come base di prezzo.** Quel preventivo
è a due mezzi e i suoi importi per mezzo sono già scontati per volume — è però il luogo fisico
da cui parte il Beluga per questo servizio.

## Margine

Preventivo costruito sul **mezzo di proprietà**, già mobilitato per un altro lavoro: il costo
aggiuntivo per il Beluga è quasi solo il trasferimento breve più la giornata sull'Amiata. Costo
diretto stimato **€ 300-370** su € 1.050 netti, per il solo Beluga: margine ottimo, proprio
perché il mezzo è già sul posto.

**Se il Beluga non fosse in zona** e dovesse riposizionarsi dalla base, il costo diretto
salirebbe (vedi variante 2 sotto) e il margine si assottiglierebbe in proporzione.

Sul **Tourengo** il margine dipende dalla tariffa reale di Francesco, non ancora nota: quotato
al cliente allo stesso prezzo del Beluga (decisione di Girolamo), il margine di GiroMunna su
questa parte è la differenza fra quei € 1.050 e quanto chiede Francesco.

## Varianti di prezzo già calcolate

1. **Base, come nel preventivo inviato** — due mezzi da/per Corte Francigena:
   € 2.100,00 netti, **€ 2.310,00** IVA inclusa.
2. **Se a fine giornata i mezzi devono rientrare alla base di Ponte Buggianese** anziché tornare
   a Corte Francigena — il rientro serale non è più breve ma un centinaio di km in più a testa:
   ogni trasferimento sale da € 150 a circa € 350-400, portando il totale sui **€ 2.750-2.850**
   IVA inclusa. Cifra da verificare con la percorrenza esatta prima di quotarla al cliente.

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
4. **I due mezzi a fine giornata tornano a Corte Francigena o alla base?** Cambia il prezzo di
   alcune centinaia di euro (variante 2 sopra) e va confermato appena chiaro come prosegue il
   lavoro dell'altro cliente.
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
   regolare fra loro due separatamente. Totale finale: **€ 2.310,00 IVA inclusa** per due mezzi.

# Note interne — Monte Amiata e rientro dall'ospedale, sab 22.08.2026, Castel del Piano (GR)

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

## Che cosa ha chiesto il cliente

Una mail sola, in inglese, con dentro tre cose diverse:

1. **Una richiesta urgente.** Una loro ospite è finita in ospedale il 20 agosto e vogliono un
   conducente che la riaccompagni domani mattina, sabato 22, alle 9 o alle 10, al Grand Hotel
   Impero di Castel del Piano.
2. **Una richiesta di essere richiamati subito.** Senza però lasciare il numero di telefono.
3. **Un preventivo.** Il gruppo vuole andare sul Monte Amiata il 22, e chiede se è possibile e
   quanto costa.

I punti 1 e 3 sono **lo stesso giorno**, e GiroMunna ha **un mezzo solo**. È il nodo di tutta
questa richiesta, ed è per quello che il preventivo li tiene insieme in una giornata sola invece
di quotarli separati.

## Prezzi

| Voce | Netto |
|---|---|
| Sab 22 ago — mezzo e conducente a disposizione, ~09:00-17:30, compreso il trasferimento ospedale | € 1.050,00 |
| Riposizionamento del mezzo da e per Ponte Buggianese, ~350 km a vuoto | € 650,00 |
| Vitto del conducente | a carico del cliente |

**Totale netto € 1.700,00 · IVA 10% € 170,00 · Totale € 1.870,00**

Nessun acconto: il servizio è a meno di 24 ore, si è messo saldo unico entro il 26 agosto. Se si
preferisce incassare prima, si cambia `pay_rows` nello script.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come questo.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

La giornata qui sta il **30% sopra** gli € 809 di Le Filigare: sono 8 ore e mezzo di disposizione
invece di 5, gli 80 km sono tutti di montagna (tornanti, seconda e terza, tempi doppi a parità di
chilometri) e dentro la giornata ci sta anche il servizio dell'ospedale. Da lì i € 1.050.

Il **riposizionamento** è una voce a parte e va pensata diversamente: non è una giornata di
servizio e non si paga come tale, ma sono comunque 350 km a vuoto e quasi cinque ore di conducente.
€ 650 fanno circa € 1,86/km, che è la tariffa giusta per un trasferimento senza passeggeri —
tenerla al livello di un servizio con gente a bordo avrebbe portato il totale fuori mercato.

**Non è stato usato il Corte Francigena (GM-2026-0819-CF).** Quello è a due mezzi e i suoi importi
per mezzo sono già scontati per volume: qui il mezzo è uno.

## Margine

Preventivo costruito sul **mezzo di proprietà**. In tutto circa 460 km (350 di riposizionamento,
80 sul monte, il resto fra hotel e ospedale): gasolio sui € 220-230, pedaggi contenuti passando
da Siena invece che dall'A1, conducente su una giornata da quattordici ore. Costo diretto stimato
**€ 450-550** su € 1.700 netti: margine buono.

**Se il Beluga non è libero e si passa da Francesco**, una giornata così con questo
riposizionamento si colloca sui € 700-900 all'ingrosso. In quel caso i prezzi vanno rivisti al
rialzo del 20-25% prima di mandare.

## Le due varianti già calcolate

1. **Mezzo già in zona con il gruppo** — cade la riga del riposizionamento:
   € 1.050,00 netti, **€ 1.155,00** IVA inclusa. Differenza di € 715,00.
2. **Solo il rientro dall'ospedale, niente gita** — riposizionamento € 650 + trasferimento € 300 =
   € 950,00 netti, **€ 1.045,00** IVA inclusa. Per accompagnare una persona sola è sproporzionato,
   e nel preventivo è detto chiaramente al cliente, consigliando un'auto NCC della zona di Grosseto.

Entrambe sono scritte nel preventivo, così il cliente non ha sorprese in nessuno dei due casi.

## La giornata del conducente

Partenza dalla base 06:15, rientro verso le 20:00: **quasi quattordici ore**. Ci si sta, ma è il
massimo che si può fare rientrando in giornata. La guida effettiva è sulle 7 ore (2h30 + ~2h + 2h30),
quindi larga rispetto ai limiti; il problema è la durata complessiva della giornata, non i chilometri.

Se il gruppo vuole tenere il mezzo la sera — una cena sul monte, un rientro dopo le 20:00 — **serve
il pernottamento a Castel del Piano**, a carico del cliente come sempre. Nel preventivo è scritto,
insieme al suggerimento di sistemare il conducente nella stessa struttura del gruppo.

## Da chiarire prima di mandare

1. **Il Beluga è libero sabato 22?** È la prima domanda di tutte, prima ancora di rispondere al
   cliente. Il 21 c'è il servizio Le Filigare (GM-2026-0821-LF).
2. **Il mezzo è già a Castel del Piano con questo gruppo?** Il cliente scrive «uno dei conducenti»,
   che lascia pensare che GiroMunna stia già seguendo questo gruppo. Cambia il totale di € 715,00 e
   va verificato prima di mandare qualsiasi cifra.
3. **Come sta la signora.** È il punto più serio. Il Beluga è un minibus turistico: gradini
   all'ingresso, nessuna attrezzatura sanitaria. Se esce dall'ospedale in carrozzina o non riesce a
   salire i gradini, **il lavoro non è nostro** e va detto subito, non domani mattina davanti
   all'ospedale. Nel preventivo la domanda è posta esplicitamente.
4. **Quale ospedale.** Non è detto nella richiesta. Castel del Piano è a pochi minuti dall'hotel;
   Abbadia San Salvatore aggiunge circa un'ora fra andata e ritorno; Grosseto sono ~55 km a tratta
   e sposta la partenza per il monte verso mezzogiorno.
5. **Quanti passeggeri.** Il Beluga porta 26 più l'autista. Sopra i 26 serve un secondo minibus, e
   quello lo decide Girolamo con Francesco: non è stato messo a preventivo di iniziativa.
6. **Nome e dati del cliente**, per rigenerare i PDF con `--cliente`.
7. **Il numero di telefono del cliente non c'è nella richiesta**, anche se chiede di essere
   richiamato subito. Va cercato nella corrispondenza precedente.

## Cancellazione

Mancando meno di ventiquattr'ore, la prenotazione ricade per intero nella fascia degli ultimi
10 giorni, cioè il 100%. Nel preventivo la scala è riportata per intero e la cosa è detta senza
giri di parole.

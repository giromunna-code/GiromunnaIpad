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

## ATTENZIONE — riposo del conducente, da risolvere prima di confermare l'orario

Orario reale di oggi (ven 21 ago), da Girolamo: partenza 09:00, sosta verso le 11:30, ripartenza
alle 17:00, rientro stimato verso l'01:00. **La pausa di mezzogiorno (11:30-17:00, 5h30) non
conta come riposo**: per essere un riposo giornaliero valido servono almeno 9 ore consecutive
(ridotto) o 11 (pieno), quindi ai fini del calcolo il turno di oggi è uno solo, continuo dalle
9:00 di stamattina fino a circa l'1:00 di stanotte — quasi 16 ore di giornata, con dentro
2h30 + 8h di impegno effettivo.

Quello che conta per domani è il riposo da quando finisce il turno di stanotte (01:00) a quando
riparte quello di domani:

| Partenza domani | Riposo | In regola? |
|---|---|---|
| 08:00 | 7h00 | No — mancano 2h anche al minimo ridotto (9h) |
| 09:00 | 8h00 | No — manca 1h anche al minimo ridotto |
| 10:00 | 9h00 | Al limite esatto del ridotto — zero margine |
| 11:00 | 10h00 | Sì, sopra il ridotto |
| 12:00 | 11h00 | Sì, riposo pieno, comodo |

Il riposo ridotto (9h) è concesso solo 3 volte a settimana: da verificare se è già stato usato
in questi giorni. Anche nel caso migliore (partenza alle 10:00) il margine è zero: qualunque
ritardo stasera (si chiude all'1:10 invece che all'1:00) fa scendere sotto il minimo.

**Per essere in regola con lo stesso conducente**, una delle due:
- il servizio di stasera finisce prima (sposta indietro il rientro dell'1:00);
- la partenza di domani slitta ad almeno le 10:00 (ridotto, senza margine) o meglio le 11:00-12:00
  (con un margine vero) — ma vuol dire spostare anche il ritiro in ospedale, che il cliente ha
  chiesto per le 9 o le 10.

**L'alternativa più semplice, se stasera non si può accorciare**: un secondo conducente prende
il mezzo domattina, mentre chi ha lavorato stasera riposa. Il limite è per persona, non per
mezzo, quindi questo risolve tutto senza toccare gli orari già promessi al cliente
dell'ospedale. Va deciso prima di confermare qualunque orario.

**Ancora non deciso da Girolamo** (21 ago, sera): quale delle strade sopra si segue. Il
preventivo qui sotto ha ancora l'arrivo del mezzo alle 08:00 e il ritiro in ospedale alle 09:00
come punti fissi (chiesti dal cliente), ma la **ripartenza per il Monte Amiata è stata
lasciata volutamente aperta** ("a seguire", non un orario fisso) — vedi sezione successiva.
Se la questione del riposo sposta anche l'orario dell'ospedale, quella parte del documento va
rifatta prima di mandarlo.

## La ripartenza per il Monte Amiata è aperta, di proposito

Girolamo ha chiesto di lasciare da decidere l'orario di ripartenza per la gita sul monte, dopo
il rientro dall'ospedale. Il documento (PDF e pagina web) è stato aggiornato di conseguenza:

- la tabella del servizio non ha più orari fissi per la giornata sull'Amiata (era "10:30 –
  17:15"), ma "a seguire" con le tappe successive indicate come tempo trascorso dalla partenza
  (+2h30, +4h30, +5h45), così restano valide qualunque sia l'ora reale di partenza;
- il rientro del mezzo a Corte Francigena è diventato "a fine giornata" invece di un orario fisso
  (era 17:30-17:55);
- il prezzo **non cambia**: resta legato alla durata (circa 6h45 di giro sul monte, circa 8h30
  di impegno totale dal ritiro in ospedale a sera), non a un orario di inizio preciso.

Questo dà un margine reale per assorbire la questione del riposo qui sopra, ma **solo per la
parte della gita**: il ritiro in ospedale resta l'unico punto dell'orario di domani già promesso
al cliente ("9 or 10 o'clock"), quindi è quello che deve rispettare per forza il minimo di
riposo — non la partenza per il monte, che segue comunque a ruota.

## Cosa cambia: il mezzo parte da Corte Francigena, non dalla base

Il 21-22 agosto il Beluga è impegnato a Corte Francigena, Castelnuovo dell'Abate (SI), vicino a
Montalcino — non a Ponte Buggianese. Il preventivo va quindi calcolato con quel punto di
partenza: **Corte Francigena → Castel del Piano è stimata in circa 17 km, 25 minuti** (fonti
stradali generiche su Castelnuovo dell'Abate; da confermare con la percorrenza reale, visto che
il mezzo è già lì e Girolamo può verificarla sul posto).

Questo abbatte il costo di riposizionamento rispetto a un'ipotesi di partenza dalla base
(che sarebbe stata di 350 km/€ 650, come nella prima stesura di questo preventivo).

## Che cosa ha chiesto il cliente

Una mail sola, in inglese, con dentro tre cose diverse:

1. **Una richiesta urgente.** Una loro ospite è finita in ospedale il 20 agosto e vogliono un
   conducente che la riaccompagni domani mattina, sabato 22, alle 9 o alle 10, al Grand Hotel
   Impero di Castel del Piano.
2. **Una richiesta di essere richiamati subito.** Il numero non era nella mail, ma Girolamo lo ha
   recuperato: **+372 5664 1112**.
3. **Un preventivo.** Il gruppo vuole andare sul Monte Amiata il 22, e chiede se è possibile e
   quanto costa.

I punti 1 e 3 sono **lo stesso giorno**, e GiroMunna ha **un mezzo solo**. È il nodo di tutta
questa richiesta, ed è per quello che il preventivo li tiene insieme in una giornata sola invece
di quotarli separati.

## Prezzi

| Voce | Netto |
|---|---|
| Sab 22 ago — mezzo e conducente a disposizione, ~09:00-17:30, compreso il trasferimento ospedale | € 1.050,00 |
| Trasferimento del mezzo da e per Corte Francigena, Castelnuovo dell'Abate, ~34 km a vuoto | € 150,00 |
| Vitto del conducente | a carico del cliente |

**Totale netto € 1.200,00 · IVA 10% € 120,00 · Totale € 1.320,00**

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
chilometri) e dentro la giornata ci sta anche il servizio dell'ospedale. Da lì i € 1.050 —
questa parte non cambia rispetto alla prima stesura, perché non dipende da dove parte il mezzo.

Il **trasferimento** da Corte Francigena è minimo: 17 km a tratta, il mezzo è già in zona per
l'altro cliente. Applicare la tariffa del riposizionamento lungo (~€ 1,86/km, usata nella prima
stesura per i 350 km dalla base) non avrebbe senso su un salto così corto: si è tenuta una cifra
minima, € 150, che copre più il tempo del conducente che il gasolio.

**Non è stato usato il Corte Francigena (GM-2026-0819-CF) come base di prezzo.** Quel preventivo
è a due mezzi e i suoi importi per mezzo sono già scontati per volume — è però il luogo fisico da
cui parte il Beluga per questo servizio.

## Margine

Preventivo costruito sul **mezzo di proprietà**, già mobilitato per un altro lavoro: il costo
aggiuntivo per questo servizio è quasi solo il breve trasferimento e la giornata sull'Amiata, non
un riposizionamento lungo. Costo diretto stimato **€ 350-420** su € 1.200 netti: margine ottimo,
proprio perché il mezzo è già sul posto.

**Se il Beluga non fosse in zona** e dovesse riposizionarsi dalla base, il costo diretto
salirebbe (vedi variante 2 sotto) e il margine si assottiglierebbe in proporzione. **Se invece si
passasse a Francesco**, i prezzi andrebbero rivisti al rialzo del 20-25%.

## Varianti di prezzo già calcolate

1. **Base, come nel preventivo inviato** — mezzo da/per Corte Francigena, ~34 km:
   € 1.200,00 netti, **€ 1.320,00** IVA inclusa.
2. **Se a fine giornata il mezzo deve rientrare alla base di Ponte Buggianese** anziché tornare a
   Corte Francigena — il rientro serale non è più 17 km ma un centinaio in più: il trasferimento
   sale da € 150 a circa € 350-400, portando il totale sui **€ 1.500-1.550** IVA inclusa. Cifra
   da verificare con la percorrenza esatta prima di quotarla al cliente.
3. **Solo il rientro dall'ospedale, niente gita sull'Amiata** — trasferimento € 150 + servizio
   ospedale isolato € 300 = € 450,00 netti, **€ 495,00** IVA inclusa. Con il mezzo già vicino,
   accompagnare la sola signora torna proporzionato: non serve più il distinguo sull'auto NCC di
   Grosseto che si sarebbe dovuto fare partendo dalla base.

Le varianti 1 e 3 sono scritte anche nel preventivo inviato al cliente; la 2 resta interna finché
non si sa dove il mezzo deve essere a fine giornata.

## La giornata del conducente

Partenza da Corte Francigena alle 08:00, rientro previsto verso le 17:55: la parte di domani è
sulle nove ore e mezza. Sommata alle 8h30 di stasera, col riposo insufficiente in mezzo, è
l'intero motivo dell'avviso in cima a questa pagina — vedere quella sezione prima di tutto.

Se il gruppo vuole tenere il mezzo la sera — una cena sul monte, un rientro dopo le 20:00 —
**serve il pernottamento a Castel del Piano**, a carico del cliente come sempre. Nel preventivo è
scritto, insieme al suggerimento di sistemare il conducente nella stessa struttura del gruppo.

## Da chiarire prima di mandare

1. **Come si risolve il riposo del conducente.** Vedi l'avviso in cima. Condiziona l'orario di
   partenza reale di domani, che potrebbe non essere le 08:00 se resta lo stesso conducente.
2. **Il mezzo a fine giornata torna a Corte Francigena o alla base?** Cambia il prezzo di alcune
   centinaia di euro (variante 2 sopra) e va confermato appena chiaro come prosegue il lavoro
   dell'altro cliente.
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
7. ~~Il numero di telefono del cliente~~ — **recuperato: +372 5664 1112.** Girolamo chiama da lì
   per la conferma a voce.
8. **Distanza Corte Francigena → Castel del Piano.** Stimata in 17 km/25 min da fonti generiche;
   da confermare con la percorrenza reale.

## Cancellazione

Mancando meno di ventiquattr'ore, la prenotazione ricade per intero nella fascia degli ultimi
10 giorni, cioè il 100%. Nel preventivo la scala è riportata per intero e la cosa è detta senza
giri di parole.

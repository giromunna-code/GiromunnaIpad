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

Il mezzo stasera (ven 21 ago) lavora a Corte Francigena dalle 17:00 fino all'01:30 di notte:
8 ore e mezzo di servizio. Con partenza domani alle 08:00 per Castel del Piano, il riposo fra i
due turni è di **sole 6 ore e mezza** (01:30-08:00).

Il riposo giornaliero minimo per un conducente professionale è di **11 ore consecutive**, o
**9 ore ridotte** (ammesse al massimo 3 volte a settimana). 6h30 sta sotto **anche** il minimo
ridotto, di 2 ore e mezza. Non è un tecnicismo: è la sicurezza del conducente, oltre che la legge
(Reg. CE 561/2006), e in caso di controllo è una sanzione pesante.

**Per essere in regola con lo stesso conducente**, una delle due:
- il servizio di stasera finisce entro le 23:00 (riposo ridotto di 9h) o meglio entro le 21:00
  (riposo pieno di 11h);
- la partenza di domani slitta ad almeno le 10:30 (ridotto) o le 12:30 (pieno) — ma vuol dire
  spostare anche il ritiro in ospedale, che il cliente ha chiesto per le 9 o le 10.

**L'alternativa più semplice, se stasera non si può accorciare**: un secondo conducente prende
il mezzo domattina, mentre chi ha lavorato stasera riposa. Il limite è per persona, non per
mezzo, quindi questo risolve tutto senza toccare gli orari già promessi al cliente
dell'ospedale. Va deciso stasera stessa, prima di confermare qualunque orario.

Il preventivo sotto è scritto con partenza alle 08:00 perché è quello che è stato chiesto, ma
resta condizionato a questa decisione.

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
7. **Il numero di telefono del cliente non c'è nella richiesta**, anche se chiede di essere
   richiamato subito. Va cercato nella corrispondenza precedente.
8. **Distanza Corte Francigena → Castel del Piano.** Stimata in 17 km/25 min da fonti generiche;
   da confermare con la percorrenza reale.

## Cancellazione

Mancando meno di ventiquattr'ore, la prenotazione ricade per intero nella fascia degli ultimi
10 giorni, cioè il 100%. Nel preventivo la scala è riportata per intero e la cosa è detta senza
giri di parole.

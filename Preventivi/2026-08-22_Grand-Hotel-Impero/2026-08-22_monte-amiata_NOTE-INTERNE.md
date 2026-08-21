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

## Il programma corretto (Girolamo, 21 agosto sera)

Le prime due stesure di questo preventivo avevano il programma sbagliato: pensavano che il
ritiro dall'ospedale fosse per **sabato mattina**, insieme alla gita. Non è così. Il programma
vero, spiegato da Girolamo, è:

- **Oggi, venerdì 21 agosto** — partenza alle 09:00 per andare a riprendere la cliente dimessa
  dall'ospedale, che si trova al Grand Hotel Impero di Castel del Piano: il ritiro è **già
  avvenuto stamattina**, non è più un servizio da fare domani. Il mezzo poi torna a Corte
  Francigena. Alle 17:00 riparte per il servizio serale dell'altro cliente (quello a cui il
  Beluga è destinato in questi giorni vicino a Montalcino), con fine prevista verso le **23:00**
  — non l'01:00-01:30 come si era capito nelle versioni precedenti.
- **Domani, sabato 22 agosto** — resta solo, eventualmente, la **gita sul Monte Amiata**.
  L'orario di partenza per il monte è ancora da decidere, ed è stato lasciato apposta aperto nel
  preventivo (vedi sotto).

**Conseguenza pratica:** questo preventivo ora riguarda **solo la gita sull'Amiata di domani**.
Il servizio dell'ospedale di oggi non ci è più dentro — è già stato fatto, il cliente non lo
aveva chiesto a preventivo (solo di essere richiamato con urgenza), e non risulta bisogno di un
documento separato per quello, a meno che Girolamo non lo richieda.

## Perché l'orario di partenza per il monte è lasciato aperto

Girolamo ha detto esplicitamente di lasciare da decidere l'orario di ripartenza per l'Amiata. Il
documento è coerente con questo: niente orario fisso ("10:30" era nella prima stesura), ma "a
seguire", con le tappe indicate come tempo trascorso dalla partenza (+2h30, +4h30, +5h45) così
restano valide qualunque sia l'ora reale. Il prezzo non cambia, è legato alla durata (6h45), non
all'orario di inizio.

## Prezzi

| Voce | Netto |
|---|---|
| Sab 22 ago — mezzo e conducente a disposizione sul Monte Amiata, circa 6h45 | € 900,00 |
| Trasferimento del mezzo da e per Corte Francigena, Castelnuovo dell'Abate, ~34 km a vuoto | € 150,00 |
| Vitto del conducente | a carico del cliente |

**Totale netto € 1.050,00 · IVA 10% € 105,00 · Totale € 1.155,00**

Nessun acconto: il servizio è a meno di 24 ore, si è messo saldo unico entro il 26 agosto.

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
aggiuntivo per questo servizio è quasi solo il trasferimento breve più la giornata sull'Amiata.
Costo diretto stimato **€ 300-370** su € 1.050 netti: margine ottimo, proprio perché il mezzo è
già sul posto.

**Se il Beluga non fosse in zona** e dovesse riposizionarsi dalla base, il costo diretto
salirebbe (vedi variante 2 sotto) e il margine si assottiglierebbe in proporzione. **Se invece si
passasse a Francesco**, i prezzi andrebbero rivisti al rialzo del 20-25%.

## Varianti di prezzo già calcolate

1. **Base, come nel preventivo inviato** — mezzo da/per Corte Francigena, ~34 km:
   € 1.050,00 netti, **€ 1.155,00** IVA inclusa.
2. **Se a fine giornata il mezzo deve rientrare alla base di Ponte Buggianese** anziché tornare
   a Corte Francigena — il rientro serale non è più 17 km ma un centinaio in più: il
   trasferimento sale da € 150 a circa € 350-400, portando il totale sui **€ 1.400-1.450** IVA
   inclusa. Cifra da verificare con la percorrenza esatta prima di quotarla al cliente.

## Ore di guida e di riposo — risolto con l'orario corretto

Con la prima versione del programma (fine servizio stasera all'01:00-01:30) il riposo prima di
domani era sotto il minimo di legge, anche nell'ipotesi migliore. **Con l'orario vero le cose
cambiano parecchio.** Fine servizio di stasera prevista verso le **23:00**:

| Partenza domani | Riposo | In regola? |
|---|---|---|
| 08:00 | 9h00 | Tocca il minimo ridotto — ancora risicato |
| 09:00 | 10h00 | Sì, comodo |
| 10:00 | 11h00 | Sì, riposo pieno |

Con qualunque orario ragionevole per la partenza di domani il riposo torna in regola. È proprio
per questo che ha senso lasciare la partenza aperta come chiesto da Girolamo, invece di fissarla
subito: dà il margine per rispettare il minimo comodamente, cosa che con l'ipotesi precedente
(fine all'1:30) non sarebbe stata possibile senza un secondo conducente. **Non serve più, con
questo orario, ricorrere al secondo conducente** — resta un'opzione se per qualche motivo il
servizio di stasera dovesse prolungarsi oltre le 23:00.

## Da chiarire prima di mandare

1. **Orario di partenza per il monte.** Lasciato apposta senza orario fisso nel documento; va
   comunicato al cliente appena deciso.
2. **Il mezzo a fine giornata torna a Corte Francigena o alla base?** Cambia il prezzo di alcune
   centinaia di euro (variante 2 sopra) e va confermato appena chiaro come prosegue il lavoro
   dell'altro cliente.
3. **Nome e dati del cliente.** La richiesta è arrivata senza intestazione: il PDF va rigenerato
   con `--cliente` quando si sa chi è.
4. **Numero di telefono del cliente: +372 5664 1112.** Recuperato — prefisso estone, probabile
   cellulare/WhatsApp. Da usare solo per la telefonata di conferma di Girolamo.
5. **Distanza Corte Francigena → Castel del Piano.** Stimata in 17 km/25 min da fonti stradali
   generiche su Castelnuovo dell'Abate; da confermare con la percorrenza reale, visto che il
   mezzo è già lì.
6. **Acconto.** Qui è stato azzerato perché il servizio è a meno di 24 ore. Se si preferisce
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

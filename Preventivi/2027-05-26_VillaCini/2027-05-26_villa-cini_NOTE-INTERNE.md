# Note interne — Servizio navetta Villa Cini, 26-29 maggio 2027

**Cliente:** Jenna Bowman · **Struttura:** Villa Cini, Bucine (AR) · **Rif. preventivo:** GM-2027-0526-VC ·
**Preparato:** 15 settembre 2026 · **Validità:** 29 settembre 2026 ·
**Canale:** richiesta arrivata sia su WhatsApp che via mail

File generati:
- `GiroMunna_Preventivo_Villa_Cini_26-29_maggio_2027_IT.pdf`
- `GiroMunna_Preventivo_Villa_Cini_26-29_maggio_2027_EN.pdf`
- `genera_preventivo_villa_cini.py` — rigenera entrambi i PDF
- `preventivo_villa_cini_26-29_maggio_2027.html` — la pagina web bilingue

Tutto dentro `Preventivi/2027-05-26_VillaCini/`.

Il cliente (Jenna Bowman) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_villa_cini.py --lingua it
python3 genera_preventivo_villa_cini.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Il lavoro, in breve

Non è un lavoro sul Beluga: il gruppo (circa 64 persone) non ci sta, e il cliente aveva già concordato
via mail due minibus con più passaggi (51 posti in origine, scartato perché l'ultimo tratto di accesso
a Villa Cini, 800 m, non è asfaltato). **Attenzione, principio generale confermato da Girolamo:** al
cliente i mezzi si presentano sempre come GiroMunna, punto — anche quando solo uno dei due è
effettivamente suo (l'altro può essere il Tourengo del fratello Francesco o un mezzo di Francesco stesso).
Chi possiede davvero ciascun mezzo è un dettaglio interno che alla gente non interessa e nel preventivo
non va scritto. Non significa che i costi reali siano quelli di Girolamo per entrambi i mezzi: significa
solo non nominare mai un fornitore esterno nel documento che va al cliente. Ho tolto ogni riferimento a
Tuscany T.O. & Munna Bus Operator dal PDF e dalla pagina web per questo motivo.

Ritrovo e riconsegna sempre alla stazione di Bucine. Orari comunicati dalla cliente (WhatsApp, 15
settembre 2026) — non sono corse singole ma vere finestre di disponibilità, con primo e ultimo ritiro:

| Data | Primo ritiro | Ultimo ritiro | Mezzi |
|---|---|---|---|
| Mer 26 mag | 15:00 | 23:00 | 2 |
| Gio 27 mag | 10:00 | 23:00 | 2 |
| Ven 28 mag | 16:15 | 24:00 (mezzanotte) | 2 |
| Sab 29 mag | 11:00 (unica corsa, ritiro e riconsegna) | — | 2 |

Tutti e quattro i giorni sono a due mezzi: decisione di Girolamo (15 settembre 2026), per avere sempre
la capienza necessaria fin dai primi arrivi del 26, non solo dal 27 in poi.

## Prezzi

| Data | Servizio | Netto |
|---|---|---|
| Mer 26 mag | Arrivo, 15:00–23:00 (8h) | € 1.200,00 |
| Gio 27 mag | Arrivi, 10:00–23:00 (13h) | € 2.600,00 |
| Ven 28 mag | Cerimonia, 16:15–00:00 (~7h45) | € 1.600,00 |
| Sab 29 mag | Partenza (ore 11:00) | € 1.200,00 |
| — | Vitto e alloggio dei due conducenti, 3 notti | a carico del cliente |

**Totale netto € 6.600,00 · IVA 10% € 660,00 · Totale € 7.260,00** (≈ € 113,00 a persona su ~64 ospiti)

Acconto 30% € 2.178,00 — saldo € 5.082,00.

**Aggiornamento 15 settembre 2026 (due passaggi).** Prima Girolamo ha segnalato che la stima iniziale
(netto € 4.250,00, totale € 4.675,00) sembrava troppo bassa: ho rialzato ogni giornata di circa il 33%
(netto € 5.700,00, totale € 6.270,00). Poi la cliente ha mandato via WhatsApp gli orari reali di primo e
ultimo ritiro per ogni giornata, che si sono rivelati finestre molto più lunghe di quanto ipotizzato
(13 ore il 27, fino a mezzanotte il 28): ho rifatto i prezzi su queste basi, arrivando ai valori sopra.
Il rialzo ora è motivato sia dal riscontro di Girolamo sia dall'impegno effettivo di mezzi e conducenti,
non solo dalla sua richiesta. Non sostituisce comunque i costi reali di Girolamo per i suoi due mezzi.

**Aggiornamento ulteriore.** Girolamo ha corretto: al cliente i due mezzi si presentano come GiroMunna,
punto — non si nomina Tuscany T.O. & Munna Bus Operator né alcun fornitore esterno. Ha anche precisato
che, in realtà, solo uno dei due mezzi potrebbe essere davvero suo (l'altro magari del fratello
Francesco): un dettaglio interno che alla gente non interessa e che nel documento al cliente non va
scritto in nessun caso. Ho tolto dal PDF e dalla pagina web ogni riferimento a un fornitore esterno.
Per il costo diretto stimato sotto, resta il punto di prima: non ho cifre reali, quindi la stima va
verificata con Girolamo (che conosce i costi, comunque siano ripartiti tra i due mezzi).

**Aggiornamento 15 settembre 2026 (terzo passaggio).** Girolamo ha deciso di mettere due mezzi anche il
26 maggio, non uno solo come ipotizzato all'inizio: vuole garantire la capienza fin dai primi arrivi,
non solo dal 27 in poi. Prezzo del 26 raddoppiato da € 650,00 a € 1.200,00 (2 mezzi × 8h invece di 1);
totale netto € 6.800,00, totale IVA inclusa € 7.480,00.

**Aggiornamento 15 settembre 2026 (quarto passaggio).** Per bilanciare l'aumento del 26, Girolamo ha
scelto di abbassare di € 200 il 27 maggio (da € 2.800,00 a € 2.600,00): è il giorno con più margine
(~50% prima del taglio), quindi assorbe meglio la riduzione. Totale netto ora € 6.600,00, IVA 10%
€ 660,00, totale € 7.260,00 (≈ € 113,00 a persona). Acconto e saldo aggiornati di conseguenza.

## Come sono stati costruiti i prezzi — È una stima, non un costo reale

**Non ho i costi diretti reali di Girolamo per questi due mezzi.** Ha scelto di procedere con una stima
(piuttosto che bloccare il preventivo in attesa dei numeri) quindi i costi diretti sotto sono ipotizzati.

Base usata: il preventivo Alvora (GM-2026-0913-BI) osserva che, se il servizio sul mezzo di proprietà
venisse subappaltato a Francesco, il costo si collocherebbe sui € 600-700 al giorno per un mezzo di
classe Beluga (26 posti). Ho preso quell'intervallo come proxy per un mezzo di classe analoga (25-27
posti), pur sapendo che qui non si tratta di subappalto: è solo l'unico punto di riferimento numerico
disponibile in assenza dei costi reali di Girolamo. Adattato alle finestre orarie reali (non più corse
brevi, ma giornate/serate lunghe a disposizione):

| Giorno | Mezzi impiegati | Costo diretto stimato | Prezzo netto |
|---|---|---|---|
| 26 maggio (15:00–23:00, 8h) | 2 | ~€ 600 | € 1.200,00 |
| 27 maggio (10:00–23:00, 13h) | 2 | ~€ 1.400 | € 2.600,00 |
| 28 maggio (16:15–00:00, ~7h45) | 2 | ~€ 900 | € 1.600,00 |
| 29 maggio (partenza) | 2 | ~€ 650 | € 1.200,00 |

Costo diretto stimato complessivo ~€ 3.550 contro un netto di € 6.600,00: margine lordo stimato attorno
al 46%, ancora tenuto alto come da regola ("nel dubbio il prezzo va tenuto alto"), pur essendo sceso
leggermente rispetto al 48% di prima per via del taglio di € 200 sul 27 maggio.

**Prima di inviare il preventivo, verificare con Girolamo i costi reali dei due mezzi su queste date e su
queste finestre orarie, e correggere le cifre se risultano diverse dalla stima.** Se il costo reale è più
alto di quanto stimato qui, il margine si assottiglia e i prezzi vanno rivisti al rialzo.

## Rischio rientro dopo le 02:00 il 28 maggio

L'ultimo ritiro è fissato a mezzanotte, ma non è garantito che tutte le corse di rientro agli alloggi si
concludano prima delle 02:00 — specie se ci sono più giri in sequenza per riportare tutti a casa dalla
festa. Se il rientro supera le 02:00 si applica il supplemento standard di € 250,00 per mezzo (già nelle
condizioni del preventivo): da monitorare, non necessariamente da anticipare nel prezzo base. Ne vale la
pena chiedere alla cliente l'orario effettivo previsto di fine festa.

## Distanza Bucine → Villa Cini

Da una ricerca pubblica (Villa Cini è una nota location per matrimoni in Toscana): la villa si trova
nel comune di Bucine stesso, non a Siena o Arezzo città — è quindi un transfer breve, coerente con
l'impostare il prezzo a giornata/corsa piuttosto che a chilometraggio lungo come nel modello Le Filigare.
Non ho verificato la distanza esatta né il tipo di strada oltre al fatto, riferito dal cliente, che
l'ultimo tratto di 800 m non è asfaltato.

## Il numero di ospiti

Il cliente ha indicato:
- 22 persone a Palazzo Vanneschi (confermato)
- circa 42 persone su nove alloggi diversi (Il Bosso Di Toscana, Fra L Mesi, A Casa Di Rafa, Isalicia
  Agriturismo, Vecchia Fornace Appartments, Agriturismo Tontenano, Fattoria Casa Bianca, Agri Le Mura,
  Toscana Verde) — **non ancora prenotati**, la cliente stessa non saprà il numero esatto finché tutti
  non avranno prenotato.

Ho usato 64 come totale di lavoro (22+42). È una stima della cliente, non un numero definitivo: il
prezzo per persona nel preventivo lo segnala esplicitamente ("si aggiorna se il numero finale cambia").

## Perché cinque corse il 27 maggio

52 posti sui due mezzi contro ~64 ospiti attesi quel giorno: nessuna corsa porta tutti insieme, quindi
ci vogliono più giri nell'arco delle tredici ore (10:00–23:00). Non è un problema, ma va spiegato al
cliente (fatto, nelle Note del preventivo) perché altrimenti "5 corse" può sembrare un costo aggiuntivo
ingiustificato.

## Prezzi confermati da Girolamo

**Aggiornamento 15 settembre 2026 (quinto passaggio).** Girolamo ha confermato che i prezzi finali
(netto € 6.600,00, totale € 7.260,00, dettaglio sopra) vanno bene. Il punto 1 sotto — verificare i
costi reali — è quindi da considerarsi risolto per l'invio: il preventivo può partire con questi numeri.
Gli altri punti (2-7) restano aperti perché riguardano informazioni che deve dare la cliente, non prezzi.

## Da chiarire prima di inviare

1. ~~**I costi reali di Girolamo** per i due mezzi da 25 e 27 posti — confermati il 15 settembre 2026,
   i prezzi finali vanno bene.~~
2. **Il numero definitivo degli ospiti**, o almeno una stima più aggiornata quando le prenotazioni
   avanzano.
3. **Orari dei treni del 26 e del 27 maggio**, per organizzare le corse dentro le finestre indicate.
4. **Orario effettivo di fine della festa del 28 maggio**, per capire se il rientro rischia di superare
   le 02:00 (vedi sopra).
5. **Indirizzi definitivi degli alloggi**, per verificare che il servizio a raggiera nella zona di Bucine
   basti, o se qualche struttura tra le nove indicate è più lontana del previsto (in tal caso andrebbero
   aggiunte corse o rivisto il prezzo).
6. **Dati di fatturazione della cliente.**
7. **Punto di discesa a Villa Cini** — farsi confermare dalla struttura dove esattamente i due mezzi si
   fermano sugli ultimi 800 m non asfaltati, e lo spazio di manovra disponibile.

## Nessuna mail preparata

Come da regola: questo lavoro si ferma al documento. Nessuna bozza né invio: la mail alla cliente la
scrive Girolamo con i suoi tempi.

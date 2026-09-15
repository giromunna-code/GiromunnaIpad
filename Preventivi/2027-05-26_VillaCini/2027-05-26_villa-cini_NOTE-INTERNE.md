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
via mail due pullman a noleggio da 25 e 27 posti (51 in origine, scartato perché l'ultimo tratto di
accesso a Villa Cini, 800 m, non è asfaltato). Questo va quindi **subappaltato a Tuscany T.O. & Munna Bus
Operator** (Francesco), che fornisce mezzi e tariffe all'ingrosso — come previsto da CLAUDE.md per i
gruppi che non stanno sul Beluga.

Ritrovo e riconsegna sempre alla stazione di Bucine. Programma:

| Data | Servizio | Mezzi |
|---|---|---|
| Mer 26 mag, 15:00 | Arrivo, stazione → alloggi | 1 |
| Gio 27 mag | Arrivo principale, 5 corse | 2 |
| Ven 28 mag | Cerimonia a Villa Cini, andata e ritorno | 2 |
| Sab 29 mag, 11:00 | Partenza, alloggi → stazione | 2 |

## Prezzi

| Data | Servizio | Netto |
|---|---|---|
| Mer 26 mag | Arrivo (ore 15:00) | € 450,00 |
| Gio 27 mag | Arrivi, 5 corse | € 1.800,00 |
| Ven 28 mag | Cerimonia, andata e ritorno | € 1.100,00 |
| Sab 29 mag | Partenza (ore 11:00) | € 900,00 |
| — | Vitto e alloggio dei due conducenti, 3 notti | a carico del cliente |

**Totale netto € 4.250,00 · IVA 10% € 425,00 · Totale € 4.675,00** (≈ € 73,00 a persona su ~64 ospiti)

Acconto 30% € 1.400,00 — saldo € 3.275,00.

## Come sono stati costruiti i prezzi — È una stima, non una tariffa reale

**Non ho le tariffe di Francesco per questo lavoro.** Girolamo ha scelto di procedere con una stima
(piuttosto che bloccare il preventivo in attesa dei numeri) quindi i costi diretti sotto sono ipotizzati,
non concordati con Francesco.

Base usata: il preventivo Alvora (GM-2026-0913-BI) osserva che, se il servizio sul mezzo di proprietà
venisse subappaltato a Francesco, il costo si collocherebbe sui € 600-700 al giorno per un mezzo di
classe Beluga (26 posti). I due mezzi di questo lavoro (25 e 27 posti) sono della stessa classe
dimensionale, quindi ho preso quell'intervallo come riferimento, adattandolo a corse brevi ripetute
invece che a una giornata intera a disposizione:

| Giorno | Mezzi impiegati | Costo diretto stimato | Prezzo netto |
|---|---|---|---|
| 26 maggio (1 corsa) | 1 | ~€ 250 | € 450,00 |
| 27 maggio (5 corse) | 2 | ~€ 1.100 | € 1.800,00 |
| 28 maggio (cerimonia A/R) | 2 | ~€ 750 | € 1.100,00 |
| 29 maggio (partenza) | 2 | ~€ 650 | € 900,00 |

Costo diretto stimato complessivo ~€ 2.750 contro un netto di € 4.250,00: margine lordo stimato attorno
al 35%, tenuto alto come da regola ("nel dubbio il prezzo va tenuto alto").

**Prima di inviare il preventivo, verificare con Francesco le tariffe reali dei due mezzi su queste date
e correggere le cifre se risultano diverse dalla stima.** Se Francesco costa più di quanto stimato qui,
il margine si assottiglia e i prezzi vanno rivisti al rialzo.

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
ci vogliono più giri. Non è un problema, ma va spiegato al cliente (fatto, nelle Note del preventivo)
perché altrimenti "5 corse" può sembrare un costo aggiuntivo ingiustificato.

## Da chiarire prima di inviare

1. **Le tariffe di Francesco** per i due mezzi da 25 e 27 posti su queste date — priorità più alta,
   cambia tutti i prezzi di questo preventivo.
2. **Il numero definitivo degli ospiti**, o almeno una stima più aggiornata quando le prenotazioni
   avanzano.
3. **Orari dei treni del 26 e del 27 maggio**, per organizzare in anticipo le corse (soprattutto le
   cinque del 27).
4. **Orario di fine della cerimonia del 28 maggio**, per organizzare il rientro serale agli alloggi.
5. **Indirizzi definitivi degli alloggi**, per verificare che il servizio a raggiera nella zona di Bucine
   basti, o se qualche struttura tra le nove indicate è più lontana del previsto (in tal caso andrebbero
   aggiunte corse o rivisto il prezzo).
6. **Dati di fatturazione della cliente.**
7. **Punto di discesa a Villa Cini** — farsi confermare dalla struttura dove esattamente i due mezzi si
   fermano sugli ultimi 800 m non asfaltati, e lo spazio di manovra disponibile.

## Nessuna mail preparata

Come da regola: questo lavoro si ferma al documento. Nessuna bozza né invio: la mail alla cliente la
scrive Girolamo con i suoi tempi.

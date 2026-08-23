# Note interne — Firenze e trasferimenti aeroporto, 29.05.2028, fino a 26 pax

**Cliente:** Tracey Williams · **Rif. preventivo:** GM-2028-0529-TW · **Preparato:** 23 agosto 2026 · **Validità:** 22 settembre 2026

**Contatti del cliente:** +44 7447 544660 · tjacbaby@gmail.com (Regno Unito)

File generati:
- `GiroMunna_Preventivo_Firenze_29_maggio_2028_IT.pdf`
- `GiroMunna_Preventivo_Firenze_29_maggio_2028_EN.pdf`
- `genera_preventivo_firenze.py` — rigenera entrambi i PDF
- `preventivo_firenze_29_maggio_2028.html` — la pagina web bilingue

Tutto dentro `Preventivi/2028-05-29_Williams/`.

Il cliente (Tracey Williams) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_firenze.py --lingua it
python3 genera_preventivo_firenze.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Cosa è arrivato davvero

Il modulo dal sito dice pochissimo:

| Campo | Valore |
|---|---|
| Nome | Tracey Williams |
| Servizio | Other |
| Data | 2028-05-29 |
| Passeggeri | Up to 26 people (Beluga minibus) |
| Tratta | Florence |
| Note | Airport pickups too |

Niente programma, niente aeroporto, niente numero di giorni, niente orari. **Il preventivo è
dichiaratamente un'ipotesi**: lo dice il sottotitolo, lo dice l'apertura de *Il servizio* e lo
ripetono le note. Serve a dare al cliente un ordine di grandezza e a farsi rispondere con i
dati che mancano.

## Prezzi

| Voce | Netto |
|---|---|
| Trasferimento aeroporto di Pisa → Firenze, all'arrivo | € 700,00 |
| Giornata a disposizione a Firenze e dintorni, 8 ore fino a 120 km | € 990,00 |
| Trasferimento Firenze → aeroporto di Pisa, alla ripartenza | € 700,00 |
| Vitto e alloggio conducente | non necessario, comunque a carico del cliente |

**Totale netto € 2.390,00 · IVA 10% € 239,00 · Totale € 2.629,00** (≈ € 101,00 a persona con 26 pax)

Acconto 30% € 790,00 — saldo € 1.839,00.

Voci a listino aggiunte in fondo alla sezione prezzo, così il cliente può ricomporsi il
preventivo da sé senza risentirci: mezza giornata € 620, trasferimento FLR ↔ Firenze € 420 a
tratta, giornata nel Chianti € 1.250, prelievo aggiuntivo a Pisa € 700, attesa € 50/ora,
rientro dopo le 02:00 € 250, permesso ZTL Firenze ~€ 350 al costo.

## Come sono stati costruiti i prezzi

Riferimenti, entrambi a mezzo singolo come questo:

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Le Filigare — giornata a disposizione a Siena, ~80 km, 5 h | € 809,00 |
| Alvora — giornata a disposizione, ~115 km, 8 h | € 980,00 |
| Alvora — trasferimento da FLR con sosta in cantina, ~83 km | € 950,00 |

**Pisa → Firenze € 700.** 85 km contro i 50 km da € 500 delle Filigare, più il parcheggio bus
di Pisa (~€ 61) che qui è dentro il prezzo e dichiarato come incluso. Con andata e ritorno
dalla base sono circa 220 km di giornata.

**FLR → Firenze € 420.** La corsa è di 12 km, ma dalla base all'aeroporto di Firenze sono
50 km: il mezzo ne fa comunque 120. È un pavimento, non una proporzione sui chilometri di
corsa — sotto non si scende.

**Giornata a disposizione € 990.** Allineata alla giornata Alvora del 14 settembre (8 h,
~115 km, € 980). Mezza giornata € 620 e giornata nel Chianti € 1.250 stanno sulla stessa scala.

**Il Corte Francigena non è stato usato**, come da regola: quel preventivo ha due mezzi e i
suoi importi per mezzo sono già scontati per volume.

## Il secondo minibus

Non inserito, e non va inserito d'iniziativa. 26 passeggeri stanno sul Beluga al posto
esatto, quindi per ora un mezzo basta. Se il numero sale (un accompagnatore, una guida, un
ventisettesimo passeggero) o se i bagagli non ci stanno, serve il Tourengo di Francesco:
**la decisione è di Girolamo**, e il costo va concordato con Francesco prima di metterlo a
preventivo. Al cliente la questione è segnalata come punto da chiarire, in prima nota.

## Margine

Preventivo costruito sul mezzo di proprietà. Costo diretto stimato € 250-350 a giornata di
servizio e **nessun pernottamento del conducente** (Firenze dista una cinquantina di km dalla
base, si rientra ogni sera): il margine è buono su tutte e tre le voci.

Se il lavoro venisse subappaltato a Francesco — € 600-700 al giorno — i prezzi vanno rivisti
al rialzo del 20-25% prima di inviare.

## Verifiche di accesso

- **Aeroporto di Pisa:** parcheggio bus circa € 61, incluso nel prezzo del trasferimento.
- **Aeroporto di Firenze:** nessun onere di accesso.
- **Centro storico di Firenze:** l'ingresso di un bus turistico richiede un permesso a parte,
  circa € 350. Nella maggior parte dei casi si evita scaricando nei punti autorizzati
  (Fortezza da Basso / Piazzale Montelungo, lungarni, Piazza della Libertà). Con 26 valigie
  al seguito, però, va valutato caso per caso: serve l'indirizzo dell'hotel.
- **Siena:** non toccata dal programma ipotizzato. Se dovesse entrarci, permesso comunale
  bus circa € 160.

## Da chiarire prima di inviare

1. **La data.** 29 maggio 2028 è a 21 mesi di distanza, il che è insolito. Però è il *late May
   bank holiday* del Regno Unito, e cade di lunedì: la data è plausibile e va **confermata,
   non corretta d'ufficio**. Nel preventivo la richiesta di conferma c'è, formulata senza dare
   del distratto al cliente.
2. **Il programma.** «Other» e «Florence» non bastano. La giornata a disposizione è
   un'ipotesi nostra e va sostituita appena arriva il programma vero.
3. **Quanti giorni di servizio.** Il modulo dà una data sola, ma «airport pickups too» al
   plurale fa pensare a un soggiorno con arrivo e ripartenza, forse su più voli.
4. **L'aeroporto.** Quotato Pisa, che è lo scalo più probabile per un gruppo britannico.
   Firenze costerebbe € 420 a tratta, Bologna di più.
5. **Bagagli e numero esatto.** È il punto tecnico vero di questo lavoro: 26 valigie da stiva
   sono al limite del vano del Beluga. Se il gruppo è davvero di 26 con bagaglio pieno, va
   messo in conto un mezzo di appoggio per le sole valigie.
6. **L'indirizzo a Firenze**, per capire se scatta il permesso ZTL.
7. **Bloccare la disponibilità** del mezzo per il 29 maggio 2028 se la richiesta si consolida.

## Nota sul prezzo a due anni di distanza

Gli importi sono sulle tariffe di oggi. Nel preventivo è scritto che alla conferma definitiva
si riconfermano, con il solo adeguamento dei costi vivi comunicato in anticipo, e che se il
cliente vuole un prezzo bloccato se ne parla in fase di conferma. Vale la pena ricordarsene:
un impegno a prezzo fisso su un servizio del 2028 è una scelta che spetta a Girolamo, non una
concessione automatica.

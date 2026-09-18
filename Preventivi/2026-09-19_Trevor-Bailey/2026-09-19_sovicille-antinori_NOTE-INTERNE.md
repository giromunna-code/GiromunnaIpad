# Note interne — Sovicille ⇄ Antinori nel Chianti Classico, 19.09.2026, 18-20 pax

**Cliente:** Trevor Bailey (richiesta arrivata da Duckbill Concierge, +1 617-644-4351) ·
**Rif. preventivo:** GM-2026-0919-TB · **Preparato:** 18 settembre 2026 ·
**Validità:** 18 settembre 2026 — il servizio è domani.

File generati, tutti dentro `Preventivi/2026-09-19_Trevor-Bailey/`:

- `GiroMunna_Preventivo_Sovicille_Antinori_19_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Sovicille_Antinori_19_settembre_2026_EN.pdf`
- `genera_preventivo_sovicille_antinori.py` — rigenera entrambi i PDF
- `preventivo_sovicille_antinori_19_settembre_2026.html` — la pagina web bilingue

Il cliente (Trevor Bailey) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_sovicille_antinori.py --lingua it
python3 genera_preventivo_sovicille_antinori.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario — per esempio `--cliente "Duckbill Concierge"`
se si preferisce intestarlo all'agenzia invece che all'ospite.

---

## La richiesta

Sabato 19 settembre 2026, andata e ritorno in giornata:

| | |
|---|---|
| Partenza | Residenza d'Epoca Borgo Il Poggiaccio, Strada Provinciale Maremmana 541, 53018 Sovicille (SI) |
| Destinazione | Antinori nel Chianti Classico / Rinuccio 1180, Via Cassia per Siena 133, 50026 Bargino (FI) |
| Passeggeri | 18-20 |
| Ritrovo | 10:45 – 11:00 al Poggiaccio |
| Rientro | partenza da Antinori fra le 15:00 e le 16:00 |
| Budget dichiarato | € 250-300 per l'andata e ritorno |

## Prezzo

| Voce | Netto |
|---|---|
| Giornata a disposizione, Poggiaccio → Antinori → Poggiaccio, 10:45-16:00, viaggio del mezzo da e per la sede compreso | € 1.200,00 |
| Vitto del conducente (pranzo durante l'attesa) | a carico del cliente |

**Totale netto € 1.200,00 · IVA 10% € 120,00 · Totale € 1.320,00**
(da € 66,00 a € 73,33 a persona secondo il numero definitivo)

Acconto 30% € 396,00 — saldo € 924,00.

Nessun pernottamento: la giornata si apre e si chiude in serata, quindi al cliente non resta
alcun costo di alloggio. Resta il pranzo del conducente durante le circa quattro ore di attesa
a Bargino, che per prassi è a carico del cliente: a preventivo è indicato ma non conteggiato,
con il suggerimento di aggiungere un coperto per lui alla prenotazione da Rinuccio 1180.

## Il posizionamento non si fattura a parte — errore da non ripetere

In una stesura precedente il viaggio da e per Ponte Buggianese era stato messo come **riga a
sé** in tabella (€ 850 di giornata + € 350 di posizionamento), sopra una giornata a disposizione
calcolata sulla scala Le Filigare.

**Sbagliato.** Da Ponte Buggianese si parte *sempre*, in ogni lavoro: quel viaggio è già dentro
gli € 809 delle Filigare e dentro tutti gli altri prezzi di riferimento della casa. Esporlo come
voce aggiuntiva lo faceva pagare **due volte**. Il prezzo qui è uno solo e comprende tutto, come
in ogni altro preventivo GiroMunna.

Il posizionamento resta però **l'argomento migliore da spendere nelle note**: spiega al cliente
perché una tratta di 55 km costa quanto costa, senza comparire come voce di prezzo.
*Spiegazione, non fattura.* La nota lo dice esplicitamente — «ve lo spieghiamo perché il conto
torni, non per addebitarvelo a parte» — e i due tratti a vuoto restano visibili nel programma
della giornata, alle 09:00 e alle 17:00, marcati come compresi nel prezzo.

## Come è stato costruito il prezzo

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come questo.

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento ~50 km | € 500,00 |
| Le Filigare — giornata a disposizione ~80 km, 5 ore | € 809,00 |
| **Questa giornata** — ~300 km totali, 9 ore di conducente, tutto compreso | **€ 1.200,00** |

Gli € 1.200 stanno **sopra** gli € 809 della giornata a disposizione delle Filigare perché lì
erano 80 km di servizio e 5 ore, qui la giornata del mezzo è di ~300 km e nove ore: una volta e
mezza il prezzo, per una giornata che pesa parecchio di più. Entrambe le cifre sono **tutto
compreso**, posizionamento incluso, quindi il confronto è omogeneo.

**Non sono stati usati i prezzi del Corte Francigena**, che sono per mezzo su un lavoro a due
mezzi e quindi già scontati per volume.

## Il conto della giornata

| Tratta | km |
|---|---|
| Ponte Buggianese → Sovicille (a vuoto) | ~115 |
| Sovicille → Bargino | 55 |
| Bargino → Sovicille | 55 |
| Sovicille → Ponte Buggianese (a vuoto) | ~80 |
| **Totale** | **~300** |

Conducente fuori dalle **09:00 alle 18:00**: nove ore, per 110 km di trasporto passeggeri e
circa quattro ore di attesa ferma a Bargino.

## Margine e spazio di trattativa

Mezzo di proprietà (Beluga), nessun pernottamento, nessun onere di accesso. Costo diretto
stimato € 250-350 fra carburante, pedaggi e conducente.

A € 1.200 netti il margine è ottimo. Se Girolamo volesse trattare, **regge fino a € 900 netti**
senza toccare la struttura del preventivo: si cambia una cifra sola. **Sotto i € 700 netti non si va**: è la fascia Corte Francigena
applicata a un mezzo singolo, l'errore già fatto una volta.

## Il divario di budget

Loro chiedono **€ 250-300**, il preventivo è a **€ 1.320** IVA inclusa. Il confronto che chiude
la discussione è quello a persona: **€ 12-15 a testa contro € 66**, per una giornata intera di
un mezzo da 26 posti con conducente. Nelle note del preventivo è detto senza giri di parole,
compreso il paragone con la corsa urbana in taxi.

Il preventivo affronta in anticipo anche la controproposta prevedibile — *«e se ci lasciaste lì
e tornaste a prenderci?»* — spiegando che sarebbero quattro trasferimenti a vuoto invece di due,
circa 160 km in più di quelli già in tabella, quindi più caro e non più economico.

Il tono delle note è stato reso **asciutto**: niente inviti a chiudere, niente «se potete
arrivare alla cifra», niente aperture alla trattativa. Un prezzo, il motivo, e la porta.
Se vanno via, vanno via sapendo perché.

## Verifiche di accesso

- Né Sovicille né Bargino sono in zona a traffico limitato.
- Il percorso aggira Siena sul raccordo Firenze-Siena senza entrare in città: **non serve** il
  permesso comunale per i bus turistici (~€ 160).
- Antinori nel Chianti Classico ha un proprio piazzale, è una cantina attrezzata per ricevere
  gruppi in pullman.
- Nessun ingresso nel centro di Firenze, quindi nessun permesso da € 350.

## Da verificare prima di rispondere

1. **La disponibilità del Beluga e del conducente per sabato 19.** È la prima cosa da guardare:
   il preventivo è scritto come se il mezzo fosse libero, ma con un giorno di preavviso non si
   può darlo per scontato. Nelle note al cliente è indicato di telefonare prima di tutto il resto.
2. **Le distanze sono stime stradali**, non un calcolo su mappa: ~115 km base-Sovicille,
   55 km Sovicille-Bargino, ~80 km Bargino-base. Reggono l'ordine di grandezza e non compaiono
   come voce di prezzo, ma sono citati nelle note: se qualcuno li mette in discussione conviene
   averli ricontrollati.
3. **Il gruppo sta sul Beluga.** 18-20 ospiti su 26 posti, restano da sei a otto posti liberi:
   non serve il secondo minibus e non c'è motivo di tirare in ballo Francesco.
4. **L'orario della prenotazione in cantina.** Antinori e Rinuccio 1180 ricevono solo su
   prenotazione. Il ritrovo alle 10:45 è tarato su una visita che comincia verso mezzogiorno:
   se l'orario vero è un altro, la partenza si sposta senza cambiare il prezzo.
5. **Il punto di salita al Poggiaccio** e lo spazio di manovra, da farsi confermare dalla
   struttura.
6. **L'acconto a ventiquattr'ore.** Il bonifico non fa in tempo a incassarsi: nel preventivo è
   scritto che la contabile vale come conferma e il saldo si regola il giorno stesso. Se
   Girolamo preferisce diversamente, è una riga da cambiare.
7. **La penale al 100%.** Mancando un giorno al servizio, la cancellazione dopo la conferma
   costa l'intero importo. Nel preventivo è detto chiaramente prima che dicano di sì.

## Chi risponde

La richiesta è arrivata in inglese da un'agenzia americana. Il preventivo è pronto nelle due
lingue: l'italiano per Girolamo, l'inglese per loro. **Alla risposta ci pensa Girolamo**, e
visti i tempi conviene una telefonata più di una mail.

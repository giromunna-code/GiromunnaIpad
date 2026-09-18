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

| Data | Servizio | Netto |
|---|---|---|
| Sab 19 set | Poggiaccio → Antinori → Poggiaccio, mezzo a disposizione 10:45-16:00 | € 900,00 |
| — | Vitto del conducente (pranzo durante l'attesa) | a carico del cliente |

**Totale netto € 900,00 · IVA 10% € 90,00 · Totale € 990,00**
(da € 49,50 a € 55,00 a persona secondo il numero definitivo)

Acconto 30% € 297,00 — saldo € 693,00.

Nessun pernottamento: la giornata si apre e si chiude in serata, quindi al cliente non resta
alcun costo di alloggio. Resta il pranzo del conducente durante le circa quattro ore di attesa
a Bargino, che per prassi è a carico del cliente: a preventivo è indicato ma non conteggiato,
con il suggerimento di aggiungere un coperto per lui alla prenotazione da Rinuccio 1180.

## Come è stato costruito il prezzo

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come questo.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento ~50 km | € 500,00 |
| Giornata a disposizione ~80 km, 5 ore | € 809,00 |

Il conto della giornata, mezzo incluso il viaggio da e per la base:

| Tratta | km |
|---|---|
| Ponte Buggianese → Sovicille (a vuoto) | ~115 |
| Sovicille → Bargino | 55 |
| Bargino → Sovicille | 55 |
| Sovicille → Ponte Buggianese (a vuoto) | ~80 |
| **Totale** | **~300** |

Il conducente esce dalla base verso le 09:00 e rientra verso le 17:45: **nove ore**, per
110 km di trasporto passeggeri e circa quattro ore di attesa ferma a Bargino.

Da qui gli € 900: **sopra** gli € 809 della giornata a disposizione delle Filigare, perché lì
erano 80 km e 5 ore e qui i chilometri sono quasi quattro volte tanti; **sotto** gli € 980
della giornata piena di Alvora, perché l'impegno con il cliente è più corto e il mezzo sta
fermo mezza giornata. Nel dubbio si è tenuto alto, come da regola: Girolamo lo abbassa se
vuole, il contrario non si recupera.

**Non sono stati usati i prezzi del Corte Francigena**, che sono per mezzo su un lavoro a due
mezzi e quindi già scontati per volume.

## Margine

Mezzo di proprietà (Beluga), nessun pernottamento, nessun onere di accesso. Costo diretto
stimato € 250-350 fra carburante, pedaggi e conducente. Il margine è buono e regge anche a
€ 700-750 netti, se Girolamo vuole scendere per chiudere. **Sotto i € 700 netti non conviene
andare**: si finisce nella fascia del Corte Francigena applicata a un mezzo singolo, che è
l'errore già fatto una volta.

## Il divario di budget

È il punto della trattativa. Loro chiedono **€ 250-300**, il preventivo è a **€ 990** IVA
inclusa: più del triplo. Nelle note del preventivo il divario è affrontato apertamente, senza
giri di parole, spiegando che il costo non è la tratta ma la giornata intera del mezzo e del
conducente, e invitandoli a dirlo subito se il budget non è spostabile, così hanno ancora un
giorno per cercare altro.

Una nota risponde in anticipo alla controproposta prevedibile — *«e se ci lasciaste lì e
tornaste a prenderci?»* — spiegando che costerebbe di più, perché sono circa 160 km di viaggi
a vuoto in più.

## Verifiche di accesso

- Né Sovicille né Bargino sono in zona a traffico limitato.
- Il percorso aggira Siena sul raccordo Firenze-Siena senza entrare in città: **non serve** il
  permesso comunale per i bus turistici (~€ 160).
- Antinori nel Chianti Classico ha un proprio piazzale, è una cantina attrezzata per ricevere
  gruppi in pullman.
- Nessun ingresso nel centro di Firenze, quindi nessun permesso da € 350.

Il preventivo lo dice esplicitamente fra le voci incluse: è un argomento di vendita, perché
significa nessun costo a sorpresa il giorno stesso.

## Da verificare prima di rispondere

1. **La disponibilità del Beluga e del conducente per sabato 19.** È la prima cosa da guardare:
   il preventivo è scritto come se il mezzo fosse libero, ma con un giorno di preavviso non si
   può darlo per scontato. Nelle note al cliente è indicato di telefonare prima di tutto il resto.
2. **Le distanze sono stime stradali**, non un calcolo su mappa: ~115 km base-Sovicille,
   55 km Sovicille-Bargino, ~80 km Bargino-base. Se si vuole essere precisi al chilometro vanno
   ricontrollate, ma l'ordine di grandezza regge il prezzo.
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
   costa l'intero importo. Nel preventivo è detto chiaramente prima che dicano di sì: meglio
   perderli adesso che litigarci domani.

## Chi risponde

La richiesta è arrivata in inglese da un'agenzia americana. Il preventivo è pronto nelle due
lingue: l'italiano per Girolamo, l'inglese per loro. **Alla risposta ci pensa Girolamo**, e
visti i tempi conviene una telefonata più di una mail.

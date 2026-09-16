# Note interne — Trasferimento Artimino ↔ Capezzana, 4 ottobre 2026

**Cliente:** Chiara Buonamici (azienda non specificata nella richiesta) · **Rif. preventivo:**
GM-2026-1004-CB · **Preparato:** 16 settembre 2026 · **Validità:** 30 settembre 2026

File generati:
- `GiroMunna_Preventivo_Carmignano_4_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Carmignano_4_ottobre_2026_EN.pdf`
- `genera_preventivo_carmignano.py` — rigenera entrambi i PDF
- `preventivo_carmignano_4_ottobre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-10-04_Buonamici/`.

Il cliente (Chiara Buonamici) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_carmignano.py --lingua it
python3 genera_preventivo_carmignano.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## La richiesta del cliente

Trasferimento per un gruppo di circa 30 persone, il 4 ottobre 2026, dalle 10:00 alle 12:00
indicativamente, tra Tenuta di Artimino e Tenuta di Capezzana, nel comune di Carmignano (PO).
Distanza indicativa circa 10 km. La cliente ha chiesto anche le modalità di prenotazione.

## Prezzo

| Data | Servizio | Netto |
|---|---|---|
| Dom 4 ott | Trasferimento Tenuta di Artimino → Tenuta di Capezzana (~10 km), mezzo a disposizione 10:00–12:00 circa | € 550,00 |

**Totale netto € 550,00 · IVA 10% € 55,00 · Totale € 605,00** (≈ € 20,15 a persona su 30
partecipanti)

Acconto 30% € 181,50 — saldo € 423,50 (il giorno del servizio, non essendoci notti di mezzo
tra acconto e servizio come nei lavori pluri-giornalieri).

## Come è stato costruito il prezzo

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, a mezzo singolo come questo:
trasferimento di ~50 km a € 500,00 netti.

Questo lavoro copre solo ~10 km pagati fra le due tenute, molto meno dei 50 km di Le
Filigare. Ma il Beluga parte dalla base di Ponte Buggianese e vi rientra: sono circa 25-30 km
per tratta, quindi ~50-60 km di trasferimento a vuoto, per un impegno complessivo di circa 2
ore sul posto più il viaggio di andata e ritorno del mezzo.

**Prima stesura (16 settembre): € 450,00.** Girolamo ha fatto notare che avevo sottostimato
il peso del tragitto andata/ritorno dalla base — la prima stima usava ~30 km a tratta ma non
l'avevo tradotta in un aumento di prezzo adeguato rispetto ai soli 10 km pagati. Ho provato a
verificare la distanza reale online (siti di calcolo percorsi irraggiungibili dalla rete di
questa sessione); l'unico dato indiretto trovato — Prato-Ponte Buggianese ~35 km, Prato-
Carmignano ~13 km — colloca Ponte Buggianese-Carmignano tra 22 e 30 km a tratta.

**Prezzo rivisto: € 550,00 netti.** Tiene conto per intero del giro a vuoto dalla base
(~50-60 km) oltre ai 10 km di servizio pagato: resta sotto i € 500,00 di Le Filigare
scalati e ben sotto la fascia della giornata a disposizione (€ 809,00 per ~80 km e 5 ore),
ma non è più tarato solo sul tratto Artimino-Capezzana. **Girolamo conosce la strada meglio
di qualunque stima online: se il tragitto reale è più corto, può abbassarlo.**

**Attenzione:** non ho usato come base i prezzi del preventivo Corte Francigena, che sono per
un lavoro a due mezzi e già scontati per volume.

## Il problema dei posti

La richiesta è per **circa 30 persone**. Girolamo ha confermato (16 settembre) che per questo
servizio il Beluga ha **25 posti disponibili per il gruppo, più uno riservato
all'accompagnatore** — non i 26 posti passeggeri nominali del mezzo. Preventivo e pagina web
sono stati aggiornati di conseguenza (sezione *Il mezzo*, nota sui partecipanti, sezione
*Incluso e non incluso*).

Ho seguito lo stesso approccio del preventivo Le Filigare, citato come riferimento nelle
istruzioni:

- il preventivo quota comunque **un solo Beluga**;
- si spiega la capienza reale e si segnala il problema al cliente, nel corpo del preventivo
  (sezione *Il mezzo* e nota dedicata);
- si chiede il **numero esatto dei partecipanti**;
- si precisa che il prezzo è riferito a un mezzo.

**Non ho inserito il secondo minibus (Tourengo di Francesco Munna).** Non è di GiroMunna ed
è una decisione che spetta solo a Girolamo: va aggiunto soltanto se lo decide lui, dopo aver
sentito Francesco per il costo. Nel preventivo ho scritto che, saputo il numero esatto,
"valutiamo insieme se e come inserire un secondo mezzo di supporto" — non è una promessa,
resta aperta.

## Margine

Preventivo costruito sul mezzo di proprietà (Beluga). Servizio breve e locale: nessuna notte
del conducente da conteggiare, nessun pernottamento da organizzare. A € 550,00 netti, con un
giro a vuoto di ~50-60 km compreso, il margine dovrebbe restare sano.

## Verifiche di accesso

- Non risultano oneri di accesso noti per Tenuta di Artimino o Tenuta di Capezzana (non sono
  zone a traffico limitato di un centro storico). Da confermare comunque con le due strutture.
- Le strade interne di molte tenute vinicole toscane sono strette: non ho dati specifici su
  Artimino e Capezzana, quindi ho messo una nota che chiede alla cliente di far confermare il
  punto di carico/scarico e lo spazio di manovra per un mezzo di 7,64 m.

## Da chiarire prima di inviare

1. **Numero esatto dei passeggeri** — decide se serve il secondo mezzo.
2. **Nome dell'azienda e un recapito diretto** — la richiesta è firmata solo "Chiara
   Buonamici", senza ragione sociale, telefono o indirizzo email di risposta indicati nel
   testo che mi è stato girato.
3. **Orario di rientro** — Girolamo l'ha segnalato come punto specifico da chiedere (16
   settembre): la richiesta dà solo l'orario del trasferimento (10:00–12:00), non l'orario
   né la destinazione del rientro del gruppo. Cambia la durata dell'impegno del mezzo e, se
   il rientro è nel pomeriggio o in serata, va quotato a parte rispetto a questo preventivo.
4. **Accesso del mezzo alle due tenute** — da far confermare dalle strutture.
5. **Bloccare la disponibilità del mezzo** per il 4 ottobre.

Il preventivo (i due PDF) segnala già alla cliente i punti 1, 3 e 4 come richieste di
chiarimento; il punto 2 serve solo per intestare correttamente il documento prima
dell'invio.

# Note interne — Keshav Menon, Castel Monastero · Castelfalfi · Lago di Garda

**Cliente:** Keshav Menon · **Rif. preventivo:** GM-2026-MENON · **Preparato:** 9 settembre 2026 ·
**Aggiornato:** 14 settembre 2026 · **Validità:** 29 settembre 2026 · **Servizi:** 20 e 23 ottobre 2026

File generati:
- `GiroMunna_Preventivo_Keshav_Menon_Castel_Monastero_Castelfalfi_Lago_di_Garda_IT.pdf`
- `GiroMunna_Preventivo_Keshav_Menon_Castel_Monastero_Castelfalfi_Lago_di_Garda_EN.pdf`
- `genera_preventivo_menon.py` — rigenera entrambi i PDF
- `preventivo_keshav_menon.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-10-20_Menon/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_menon.py --lingua it
python3 genera_preventivo_menon.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Cronologia degli aggiornamenti

**14 settembre 2026, primo aggiornamento — bagagli.** Il cliente ha risposto alla prima versione
del preventivo (arrivata come PDF, non generata da questo repository) precisando i bagagli:
**23 valigie da stiva e 15 bagagli a mano.**

La prima versione segnalava 32 colli complessivi contro una capienza del vano di circa 23
valigie — 9 pezzi oltre il limite, punto lasciato aperto in attesa di chiarimento. Con la
scomposizione fornita:

- Le **23 valigie da stiva** riempiono esattamente il vano bagagliaio, al limite della sua
  capienza comoda: **nessun margine per altro**, ma dentro la soglia.
- I **15 bagagli a mano** viaggiano nell'abitacolo con i passeggeri. Il gruppo è di 16 persone
  su 26 posti: restano 10 sedili liberi, più che sufficienti per sistemarli.

Il problema segnalato nella prima versione è quindi risolto: **non serve un secondo mezzo**, il
prezzo resta invariato (€ 2.600,00 netti · € 2.860,00 IVA inclusa).

In questo stesso passaggio ho anche **corretto le condizioni di cancellazione**, diverse dallo
standard GiroMunna nella prima versione (libera oltre 30 giorni; 30-10 giorni acconto trattenuto;
10-3 giorni 70%; ultime 72h 100%). Standard GiroMunna applicato: **gratuita oltre 60 giorni; da 60
a 30 giorni si trattiene l'acconto; da 30 a 10 giorni il 50%; negli ultimi 10 giorni il 100%.**

**14 settembre 2026, secondo aggiornamento — mese confermato.** Il cliente ha indicato il mese di
viaggio: **ottobre 2026.** I due trasferimenti confermabili sono quindi il **20 e il 23 ottobre
2026** (il 17 e il 26 ottobre restano i due tratti da/per Milano che GiroMunna non copre).

Di conseguenza:
- **Cartella rinominata** da `Preventivi/2026-09-20_Menon/` a `Preventivi/2026-10-20_Menon/`
  (idem il file delle note interne), secondo lo schema `AAAA-MM-GG_Cliente` con la data del primo
  servizio confermato.
- **Validità del preventivo spostata dal 24 al 29 settembre 2026** (15 giorni da oggi, 14
  settembre): la data precedente era antecedente ai servizi di ottobre e avrebbe fatto scadere il
  preventivo prima ancora che il cliente potesse confermarlo.
- **Saldo**: la scadenza "5 giorni prima del primo trasferimento" ora ha una data precisa,
  **15 ottobre 2026**, al posto del generico "da fissare col mese".
- Rimossa la nota "il mese e l'anno" dall'elenco dei punti da confermare, ormai risolta.
- Tutti i riferimenti a "20" e "23" nel testo sono stati esplicitati in "20 ottobre" e
  "23 ottobre" (idem "17" e "26").

## Punti ancora aperti

1. **Riferimento preventivo** lasciato invariato, `GM-2026-MENON`, per continuità con la prima
   versione già inviata al cliente — non segue lo schema standard `GM-AAAA-MMGG-XX` (che darebbe
   `GM-2026-1020-KM`). Valutare con Girolamo se vale la pena allinearlo ora che il mese è noto,
   oppure mantenerlo per non confondere la corrispondenza già in corso col cliente.
2. **Il 17 e il 26 ottobre non sono coperti** (i due tratti da/per Milano): resta da vedere se
   Girolamo vuole proporre una soluzione tramite Francesco (Tuscany T.O. & Munna Bus Operator)
   per quei due trasferimenti, oppure lasciare che il cliente si organizzi altrimenti.
3. **Orari e punti di carico esatti**, per entrambi i trasferimenti — non solo l'orario di
   partenza, ma anche il punto di carico preciso (ingresso o punto di ritrovo indicato dalla
   struttura) a Castel Monastero il 20 ottobre e a Castelfalfi il 23 ottobre. Segnalato
   esplicitamente da Girolamo come mancante nella nota; prima si parlava solo di orari.
4. Accesso stradale al Cape of Senses Hideaway, numero di cellulare del gruppo — ancora da
   confermare, come nelle versioni precedenti.

## Nota sul processo

Questo preventivo non era stato generato da questo repository (è arrivato come PDF caricato in
chat, con un riferimento fuori schema). Dal primo aggiornamento l'ho portato dentro
`Preventivi/`, nel formato standard con script Python, PDF bilingue e pagina web, così che i
prossimi aggiornamenti si possano rigenerare da qui.

**Promemoria:** nessuna bozza di mail è stata preparata né inviata — alle comunicazioni con il
cliente ci pensa Girolamo.

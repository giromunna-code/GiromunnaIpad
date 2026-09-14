# Note interne — Keshav Menon, Castel Monastero · Castelfalfi · Lago di Garda

**Cliente:** Keshav Menon · **Rif. preventivo:** GM-2026-MENON · **Preparato:** 9 settembre 2026 ·
**Aggiornato:** 14 settembre 2026 · **Validità:** 24 settembre 2026

File generati:
- `GiroMunna_Preventivo_Keshav_Menon_Castel_Monastero_Castelfalfi_Lago_di_Garda_IT.pdf`
- `GiroMunna_Preventivo_Keshav_Menon_Castel_Monastero_Castelfalfi_Lago_di_Garda_EN.pdf`
- `genera_preventivo_menon.py` — rigenera entrambi i PDF
- `preventivo_keshav_menon.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-20_Menon/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_menon.py --lingua it
python3 genera_preventivo_menon.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Cosa è cambiato con questo aggiornamento

Il cliente ha risposto alla prima versione del preventivo (arrivata come PDF, non generata da
questo repository) precisando i bagagli: **23 valigie da stiva e 15 bagagli a mano.**

La prima versione segnalava 32 colli complessivi contro una capienza del vano di circa 23
valigie — 9 pezzi oltre il limite, punto lasciato aperto in attesa di chiarimento. Con la
scomposizione ora fornita:

- Le **23 valigie da stiva** riempiono esattamente il vano bagagliaio, al limite della sua
  capienza comoda: **nessun margine per altro**, ma dentro la soglia.
- I **15 bagagli a mano** viaggiano nell'abitacolo con i passeggeri. Il gruppo è di 16 persone
  su 26 posti: restano 10 sedili liberi, più che sufficienti per sistemarli.

Il problema segnalato nella prima versione è quindi risolto: **non serve un secondo mezzo**, il
prezzo resta invariato (€ 2.600,00 netti · € 2.860,00 IVA inclusa). Ho aggiornato la sezione
bagagli, il riquadro sotto il prezzo, la voce "Incluso" e il punto "da confermare" corrispondente
nella lista note, oltre a segnare la data di aggiornamento nell'intestazione.

## Correzione applicata: condizioni di cancellazione

La prima versione del preventivo riportava condizioni di cancellazione diverse dallo standard
GiroMunna (libera oltre 30 giorni; 30-10 giorni acconto trattenuto; 10-3 giorni 70%; ultime 72h
100%). Le condizioni ricorrenti GiroMunna sono invece: **gratuita oltre 60 giorni; da 60 a 30
giorni si trattiene l'acconto; da 30 a 10 giorni il 50%; negli ultimi 10 giorni il 100%.**
Ho corretto il testo per allinearlo allo standard, dato che stavo comunque rigenerando il
documento nel formato della casa.

## Punti ancora aperti (invariati rispetto alla prima versione)

1. **Il mese del viaggio** non è confermato — la richiesta del cliente indica solo i giorni 17,
   20, 23 e 26. Ho usato **settembre 2026** come ipotesi di lavoro per la cartella e il nome
   file, basandomi sul fatto che la validità del preventivo (fino al 24 settembre) è coerente
   con servizi nello stesso mese. **Se il cliente conferma un mese diverso, la cartella va
   rinominata** secondo lo schema `AAAA-MM-GG_Cliente`.
2. **Riferimento preventivo** lasciato invariato, `GM-2026-MENON`, per continuità con la prima
   versione già inviata al cliente — non segue lo schema standard `GM-AAAA-MMGG-XX` (che
   richiederebbe il mese, non ancora noto).
3. **Il 17 e il 26 settembre non sono coperti** (i due tratti da/per Milano): resta da vedere se
   Girolamo vuole proporre una soluzione tramite Francesco (Tuscany T.O. & Munna Bus Operator)
   per quei due trasferimenti, oppure lasciare che il cliente si organizzi altrimenti.
4. Orari di partenza, accesso stradale al Cape of Senses Hideaway, numero di cellulare del
   gruppo — tutti ancora da confermare, come nella prima versione.

## Nota sul processo

Questo preventivo non era stato generato da questo repository (è arrivato come PDF caricato in
chat, con un riferimento fuori schema). Con questo aggiornamento l'ho portato dentro
`Preventivi/`, nel formato standard con script Python, PDF bilingue e pagina web, così che i
prossimi aggiornamenti (mese confermato, orari, ecc.) si possano rigenerare da qui.

**Promemoria:** nessuna bozza di mail è stata preparata né inviata — alle comunicazioni con il
cliente ci pensa Girolamo.

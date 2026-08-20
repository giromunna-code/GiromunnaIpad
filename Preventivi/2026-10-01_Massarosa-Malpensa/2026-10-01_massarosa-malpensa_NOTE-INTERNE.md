# Note interne — Trasferimento Massarosa → Malpensa, 01.10.2026, 16 pax

**Cliente:** non ancora noto · **Rif. preventivo:** GM-2026-1001-MM · **Preparato:** 20 agosto 2026 · **Validità:** 3 settembre 2026

File generati, tutti dentro `Preventivi/2026-10-01_Massarosa-Malpensa/`:

- `GiroMunna_Preventivo_Transfer_Massarosa_Malpensa_1_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Transfer_Massarosa_Malpensa_1_ottobre_2026_EN.pdf`
- `genera_preventivo_massarosa_malpensa.py` — rigenera entrambi i PDF
- `preventivo_transfer_massarosa_malpensa_1_ottobre_2026.html` — la pagina web bilingue

```bash
python3 genera_preventivo_massarosa_malpensa.py --lingua it
python3 genera_preventivo_massarosa_malpensa.py --lingua en
```

**La richiesta è arrivata senza nome**, quindi lo script non ha un intestatario predefinito e i
PDF attuali escono senza la riga "Preparato per …". Appena si sa chi è, va rigenerato con
`--cliente "Nome"`. Anche il riferimento va rivisto: le `MM` finali stanno per
Massarosa–Malpensa, non per le iniziali del cliente. Se il nome cambia le iniziali, si
aggiorna `RIF` in cima allo script e nella pagina HTML.

---

## La richiesta

| | |
|---|---|
| Partenza | 55054 Massarosa (LU) — indirizzo esatto non indicato |
| Arrivo | Aeroporto di Milano Malpensa — terminal non indicato |
| Data | giovedì 1 ottobre 2026 |
| Orario | 02:00 |
| Passeggeri | 16 |

Sedici passeggeri stanno comodamente sul Beluga (26 posti): **un mezzo solo, nessun bisogno
di coinvolgere Francesco.**

## Prezzi

| Voce | Netto |
|---|---|
| Massarosa → Malpensa, circa 330 km | € 1.550,00 |
| Maggiorazione partenza notturna 02:00 | € 250,00 |
| Vitto e alloggio conducente | non necessario, nessun onere |

**Totale netto € 1.800,00 · IVA 10% € 180,00 · Totale € 1.980,00** (€ 123,75 a persona,
arrotondato a « circa € 124,00 » nel documento)

Acconto 30% € 594,00 — saldo € 1.386,00.

## Come è stato costruito il prezzo

Riferimento **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come questo:

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento ~50 km | € 500,00 |
| Giornata a disposizione ~80 km, 5 ore | € 809,00 |

E la scala dei trasferimenti già usata per Alvora: € 500 per 50 km, € 780 per 110 km, cioè
circa € 4,70 al km oltre i primi 50. Estesa a 330 km darebbe € 500 + (280 × 4,70) ≈ € 1.816
netti. Ho tenuto € 1.550 per il trasferimento **più** € 250 di maggiorazione notturna, che
fa € 1.800: praticamente lo stesso numero, ma con la parte notturna esposta a parte, così è
difendibile e si può togliere se l'orario si sposta.

**Non ho usato il Corte Francigena.** Quel preventivo ha due mezzi e i suoi importi per mezzo
sono già scontati per volume.

## Margine

Il mezzo percorre **circa 660 km** fra andata carica e rientro a vuoto. Costi diretti stimati:

| Voce | Stima |
|---|---|
| Gasolio, ~660 km | € 250-280 |
| Pedaggi A11/A12/A26 andata e ritorno | € 90-110 |
| Sosta/accesso a Malpensa per lo scarico | € 20-40 |
| Conducente, turno notturno di circa 9 ore | secondo accordo |

Restano indicativamente **€ 1.100-1.200 lordi di margine** prima del costo del conducente:
buono per un servizio che occupa il mezzo mezza giornata scarsa. Se per qualsiasi ragione il
lavoro dovesse passare a Francesco, il suo costo su una tratta del genere si colloca ben oltre
i € 700 e il margine si assottiglia: in quel caso conviene rivedere al rialzo prima di inviare.

## Due scelte che vanno confermate da te

1. **La maggiorazione notturna di € 250.** L'ho applicata perché la giornata del conducente
   comincia all'01:00, ed è la stessa cifra della nostra tariffa per i rientri dopo le due.
   Nel preventivo ho scritto che **non è dovuta se la partenza si sposta alle 05:00 o più
   tardi**. Se preferisci tenerla anche in quel caso, o spostare la soglia più avanti, si
   cambia la nota e la riga di prezzo.

2. **L'alternativa delle 05:00 messa nero su bianco.** Il preventivo dice apertamente che, se
   il volo parte tardi, conviene partire alle 05:00 e il prezzo scende a € 1.705,00 IVA
   inclusa. È un'informazione che ci fa fare bella figura e che quasi nessuno dà, ma è anche
   un prezzo più basso già scritto: se non ti va, quella parte della nota si toglie in un
   minuto e si tiene solo la proposta di spostare l'orario.

## Il vitto e alloggio del conducente

Su questo lavoro **non serve alcun pernottamento** e nel preventivo è scritto così, sia nella
riga della tabella (« nessun pernottamento necessario — nessun onere ») sia fra il non incluso
sia in una nota. Il conto torna: partenza dalla base verso l'01:00, scarico a Malpensa alle
05:30, pausa obbligatoria di 45 minuti a destinazione, rientro in Toscana verso le 09:45.
Circa 8 ore di guida su un solo conducente, dentro i limiti di legge, senza secondo autista.

La regola di casa dice di indicare *sempre* vitto e alloggio: l'ho fatto, ma dicendo che qui
non si applica invece di mettere « a carico vostro » per zero notti, che avrebbe confuso il
cliente. La riga resta visibile, così nessuno se lo ritrova come sorpresa dopo.

## Verifiche di accesso e percorso

- Itinerario quotato: A11 da Massarosa → A12 direzione Genova → A26 dei Trafori → uscita
  aeroporto. Evita il nodo di Milano, che di mattina presto sarebbe il rischio maggiore.
- Nessuna ZTL, nessun permesso comunale: né Massarosa né Malpensa ne richiedono.
- Gli oneri di accesso e sosta a Malpensa per il solo scarico passeggeri li ho messi
  **dentro** il prezzo e dichiarati fra l'incluso, senza esporre la cifra. Vanno verificati
  alla conferma, quando sapremo il terminal.

## Da chiarire con il cliente prima di confermare

1. **Numero e orario del volo, e il terminal.** È la cosa più importante: T1 e T2 si
   raggiungono da svincoli diversi, e soprattutto l'orario del volo dice se le 02:00 sono
   davvero l'orario giusto.
2. **Indirizzo esatto del punto di carico.** Il CAP 55054 comprende sia la piana sia i paesi
   in collina (Corsanico, Pieve a Elici, Montigiano, Gualdo), dove alle due di notte serve
   sapere prima dove ci si mette e dove si gira.
3. **Bagagli fuori misura** — sci, golf, passeggini, strumenti.
4. **Numero definitivo dei passeggeri** (16 sta largo sul Beluga, ma sopra i 26 cambierebbe
   tutto).
5. **Il ritorno.** Vale la pena chiederlo: andata e ritorno quotati insieme rendono di più e
   il cliente spende meno di due sole andate.
6. **Nome, recapito e dati di fatturazione**, che al momento non abbiamo.
7. **Bloccare il mezzo** per la notte fra il 30 settembre e il 1° ottobre.

## Nota sulla pagina web

A differenza del preventivo Alvora, la pagina HTML di questo lavoro **non contiene il blocco
interno** con margini e ragionamenti sui prezzi: quelle cose stanno solo in questo file. La
pagina si può quindi mandare o mostrare al cliente così com'è, senza doverci pensare.

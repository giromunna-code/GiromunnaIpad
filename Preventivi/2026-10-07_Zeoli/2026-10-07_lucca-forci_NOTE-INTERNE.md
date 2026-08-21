# Note interne — Lucca → Tenuta di Forci → Lucca, 7 ottobre 2026, 24 pax

**Cliente:** Ray Zeoli (riunione di famiglia) · **Rif. preventivo:** GM-2026-1007-RZ
**Preparato:** 21 agosto 2026 · **Validità:** 4 settembre 2026

File generati, tutti dentro `Preventivi/2026-10-07_Zeoli/`:

- `GiroMunna_Preventivo_Lucca_Tenuta_di_Forci_7_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Lucca_Tenuta_di_Forci_7_ottobre_2026_EN.pdf`
- `genera_preventivo_lucca_forci.py` — rigenera entrambi i PDF
- `preventivo_lucca_forci_7_ottobre_2026.html` — la pagina web bilingue

Il cliente (Ray Zeoli) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_lucca_forci.py --lingua it
python3 genera_preventivo_lucca_forci.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## Il servizio

Mercoledì 7 ottobre 2026, mezza giornata a disposizione con un solo mezzo.

| Orario | |
|---|---|
| 11:45 | Ritrovo a Lucca, Piazzale Boccherini |
| 12:00 | Partenza per Tenuta di Forci, ~15 km per il percorso alternativo alla frana |
| 12:35 | Arrivo alla tenuta; mezzo e conducente restano lì per pranzo e degustazione |
| 16:00 | Ripartenza (o 15:30, a scelta del cliente, stesso prezzo) |
| 16:40 | Rientro a Piazzale Boccherini |

Mezzo impegnato circa 11:45 – 17:00. Con il posizionamento da Ponte Buggianese, la giornata
del conducente è circa 11:00 – 17:30.

## Prezzo

| Voce | Importo | IVA |
|---|---|---|
| Lucca → Tenuta di Forci → Lucca, mezzo a disposizione, attesa compresa | € 500,00 | 10% |
| IVA 10% sul servizio | € 50,00 | — |
| Permesso comunale di accesso a Lucca | € 180,00 | fuori campo |
| Vitto e alloggio conducente | non necessario | — |

**Servizio € 550,00 IVA inclusa + permesso € 180,00 = totale € 730,00**
(circa € 30,40 a persona)

Acconto 30% del totale € 219,00 — saldo € 511,00.

Il permesso di Lucca è addebitato **a parte** e **fuori campo IVA**: è un onere del Comune
che GiroMunna anticipa per conto del cliente e riaddebita al costo, quindi non sconta il
10%. L'IVA resta solo sui € 500,00 di servizio. **Stesso trattamento va applicato al
permesso comunale di Siena e a quello per il centro di Firenze** negli altri preventivi.

## Come è stato costruito il prezzo

Riferimento: **Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come questo.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Qui le ore sono le stesse della giornata a disposizione di Le Filigare (5 h 15 di mezzo
impegnato), i chilometri di servizio molti meno (~30 km contro ~80).

**Gli € 500 sono una decisione di Girolamo su questo lavoro, non un nuovo riferimento.**
La prima stesura era a € 820, sopra gli € 809 di Le Filigare, per tre motivi che restano
veri: la strada è di collina e passa dalla deviazione della frana; ai ~30 km di servizio si
sommano ~60 km di posizionamento da Ponte Buggianese; il mezzo e il conducente sono fuori
dalle 11:00 alle 17:30 circa, quindi il 7 ottobre non si vende due volte e non è una mezza
giornata da prezzare come marginale. Girolamo ha abbassato a € 500, che è il livello del
**trasferimento** da ~50 km di Le Filigare, non quello di una giornata a disposizione.

Chi rifà un preventivo a mezzo singolo deve ripartire da **Le Filigare**, non da questo:
gli € 500 su cinque ore a disposizione non sono la tariffa di casa.

**Non usare come base neanche i € 450 di mezza giornata offerti nel preventivo Alvora per il
17 settembre.** Quelli erano per un mezzo già posizionato in Versilia dentro un tour di più
giorni, cioè un prezzo marginale su un mezzo già pagato dal resto del programma. Qui il
lavoro è isolato e si porta dietro tutto il posizionamento.

## Margine

Preventivo costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato € 250-300
sulla giornata, senza il permesso che ora è ribaltato al cliente. Con € 500 di servizio il
margine sulla giornata è **sottile**, contando i ~60 km di posizionamento e le sei ore e
mezza di impegno del conducente. Nessuna notte da coprire, quindi niente vitto e alloggio
in gioco.

## Nessun secondo mezzo

24 passeggeri stanno sul Beluga (26 posti, due liberi). Il Tourengo di Francesco **non
serve e non è stato inserito**. Nelle note al cliente è scritto che oltre i 26 passeggeri
cambierebbero organizzazione e prezzo: se il gruppo dovesse crescere, la decisione sul
secondo mezzo è di Girolamo e va concordata prima con Francesco.

## La frana — il punto centrale della richiesta

Il cliente ha chiesto **esplicitamente** di confermare che il mezzo arriva a Forci con la
strada principale chiusa. Verificato:

- La **via per Pieve Santo Stefano** (la salita da Sant'Alessio dopo il ponte sul Serchio,
  cioè la strada normale indicata dalla tenuta stessa) è interrotta da una frana.
- Il Comune di Lucca ha in corso un intervento da **€ 780.000** fra pali e tiranti per
  consolidare il versante, cantiere aperto da marzo 2026. A giugno 2026 i lavori erano
  ancora in corso e non risulta una data di riapertura.
- Il Comune indica come viabilità alternativa **via Piana** e **via delle Foreste**, che
  salgono da Mutigliano. Sono aperte: la zona non è isolata.

Nel preventivo la cosa è girata a favore: sono strade strette, ed è esattamente il motivo
per cui si quota il Beluga da 7,64 m e non un gran turismo. Argomento di vendita, non
problema.

## Da fare prima di inviare

1. **Verificare che i € 180 del permesso di Lucca coprano il costo vero.** L'importo è
   quello indicato da Girolamo ed è addebitato a parte, fuori campo IVA, ma la tariffa 2026
   non è confermata: le tariffe sono cambiate dal 1° gennaio 2026 e il permesso si compra
   **solo online**, sul portale LuccaPlus, sezione Bus Turistici, **prima** dell'ingresso
   nella zona verde. Info: `checkpointbus@metrosrl.it`, ufficio al parcheggio Palatucci,
   viale Carlo del Prete. Se il costo effettivo fosse più alto, va corretta la riga prima di
   inviare. Conservare la ricevuta del permesso: è la giustificazione dell'anticipazione.
2. **Fare davvero il sopralluogo sul percorso alternativo.** Nelle note al cliente è
   promesso: via Piana e via delle Foreste da Mutigliano, con il mezzo o almeno in auto,
   guardando i punti stretti e i tornanti. E ricontrollare le ordinanze del Comune nei
   giorni prima del servizio, perché il cantiere è ancora aperto.
3. **Contattare Tenuta di Forci** per il punto esatto di discesa del gruppo, lo spazio di
   manovra per un mezzo da 7,64 m e dove il conducente lascia il minibus durante il pranzo.
   Sono 360 ettari e gli ultimi 7 km sono in salita.

   **Attenzione al numero: il fisso 0583 349001 risulta inesistente** (provato da Girolamo
   il 21 agosto 2026). È il numero che tutti gli elenchi online continuano a riportare —
   PagineGialle, PagineBianche, i portali di cantine — ma sono schede vecchie che si copiano
   fra loro. Segnale che il recapito è cambiato: la tenuta è passata dal dominio
   `tenutadiforci.it` a `tenutadiforci.com`.

   In ordine, i canali da provare:
   - **Mail `info@tenutadiforci.com`** — è il canale che la tenuta stessa indica per le
     prenotazioni, con almeno 48 ore di preavviso. Il più affidabile.
   - **Mobile 370 3709667**, indicato anche come numero WhatsApp.
   - **Chiedere il recapito buono al cliente.** Ray Zeoli ha già prenotato il pranzo e ha un
     suo riferimento alla tenuta: è la strada più corta e nel preventivo gli abbiamo già
     chiesto quel nome.

   Nota utile: la tenuta riceve i piccoli gruppi su prenotazione **il mercoledì**, e il
   7 ottobre 2026 è un mercoledì. La data del cliente combacia con il giorno delle visite.
4. **Confermare Piazzale Boccherini** come punto di ritrovo. È il punto di carico e scarico
   autorizzato per i bus più vicino al B&B La Bohème (via del Moro 2, accanto a piazza San
   Michele): circa 500 m, sei o sette minuti a piedi in piano lungo via San Paolino. Gli
   altri autorizzati — Porta San Pietro, Porta Santa Maria, Porta Elisa — sono più lontani.
5. **Bloccare il mezzo** per il 7 ottobre.
6. **Se il cliente chiede la navetta** dal B&B al piazzale per chi fa fatica a camminare, va
   quotata a parte: nel preventivo è offerta ma non compresa.

## Cancellazione

Mancano 47 giorni al servizio: siamo nella fascia **60-30 giorni** (si trattiene l'acconto).
Dal **7 settembre** si passa alla fascia 30-10 giorni (50%). Dal **27 settembre**, 100%.

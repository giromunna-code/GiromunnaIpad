# GiromunnaIpad

Spazio di lavoro di **GiroMunna** — Munna Girolamo Giuseppe, noleggio autobus e minibus
con conducente (NCC), Ponte Buggianese (PT), Toscana.

## Regole di lavoro

- **Parlare sempre in italiano.** Girolamo non parla inglese: ogni risposta, spiegazione o
  messaggio va scritto in italiano.
- **Ogni documento va prodotto in due versioni, italiana e inglese.** Vale per i preventivi,
  le mail ai clienti e qualsiasi altro materiale destinato all'esterno: i clienti scrivono
  spesso in inglese, ma la versione che Girolamo deve poter leggere è quella italiana.
  Nessuna delle due sostituisce l'altra.

## Dati aziendali

| | |
|---|---|
| Ragione sociale | GiroMunna — Munna Girolamo Giuseppe |
| Sede | Ponte Buggianese (PT), Toscana, Italia |
| P. IVA | IT 02124530474 |
| Telefono | +39 335 587 4744 |
| Email | info@giromunna.com |
| Sito | giromunna.com |
| IBAN | IT59 O053 4137 0700 0000 0034 24 — BIC/SWIFT BAPPIT21S05 |

## Mezzi

- **Mercedes-Benz Beluga** — 26 posti passeggeri più l'autista, 7,64 m. Aria condizionata,
  sedili ultra comfort reclinabili, frigo bar, impianto audio di bordo, ampio vano bagagli.
- **Mercedes-Benz Tourengo** — 28 posti passeggeri più l'autista, 7,86 m. Aria condizionata,
  sedili reclinabili, vano bagagli.

Entrambi stanno sotto gli 8 metri e raggiungono strade e piazzali dove un autobus gran
turismo non arriva. È un argomento di vendita, non un dettaglio tecnico.

Per i gruppi che non stanno sui mezzi di proprietà si lavora con **Tuscany T.O. & Munna Bus
Operator** (Francesco Munna, Montecatini Terme, `infomunnabus@gmail.com`), che fornisce
tariffe all'ingrosso. Le sue tariffe **non** sono i prezzi di vendita: vanno ricaricate.

## Preventivi

I preventivi si generano come PDF nel formato della casa: logo circolare, verde bottiglia
`#1F4636` e oro `#C9A24B`, intestazione e piè di pagina su ogni pagina, Helvetica.

Struttura: titolo e riferimento, *Il mezzo*, *Il servizio* (tabella per data), *Il prezzo*
(importi al netto con `+ IVA 10%` e totale IVA inclusa), *Incluso* / *Non incluso*,
*Pagamento* (acconto 30% alla conferma, saldo), *Note*.

Il riferimento segue lo schema `GM-AAAA-MMGG-XX`, dove `MMGG` è la data del primo servizio
e `XX` sono le iniziali del cliente o della struttura.

Le *Note* sono la parte che distingue questi preventivi: non ripetono le condizioni, ma
segnalano al cliente i problemi veri del programma — bagagli, strade strette, orari dei
voli troppo stretti — e propongono la soluzione. Vanno scritte, non riempite.

### Condizioni ricorrenti

- IVA sui servizi di trasporto passeggeri: **10%**.
- Attesa oltre gli orari concordati: **€ 50,00 all'ora per mezzo**.
- Rientro dopo le 02:00: **€ 250,00 per mezzo**.
- Attesa gratuita fino a **90 minuti** dall'atterraggio effettivo, per quanto il volo ritardi.
- Vitto e alloggio del conducente, quando serve: circa **€ 140,00 a notte**.
- Cancellazione: gratuita oltre 60 giorni; da 60 a 30 giorni si trattiene l'acconto;
  da 30 a 10 giorni il 50%; negli ultimi 10 giorni il 100%.
- L'aeroporto di Firenze non comporta oneri di accesso; quello di Pisa ha il parcheggio bus
  (circa € 61). L'ingresso di un bus turistico nel centro di Firenze richiede un permesso a
  parte (circa € 350). Siena ha il permesso comunale per i bus turistici (circa € 160).

## Struttura del repository

- `quotes/` — preventivi, uno script di generazione per ciascuno, note interne.
- `quotes/assets/giromunna_logo.png` — logo per i PDF.

Lo script di un preventivo accetta `--lingua it|en` e `--cliente "Nome"` e produce il PDF
corrispondente. Va eseguito per entrambe le lingue.

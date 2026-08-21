# Note interne — Giornata aggiuntiva Monte Amiata, 22 agosto 2026

**Cliente:** Anette Haavel · **Rif. addendum:** GM-2026-0822-CF · **Preparato:** 21 agosto 2026

Questo è un giorno in più aggiunto al preventivo già in corso **Corte Francigena
(Rif. GM-2026-0819-CF)**, 19-23 agosto, € 10.670,00 totale. Il PDF originale di
quel preventivo è salvato qui accanto:
`RIFERIMENTO_GiroMunna_Quotation_Corte_Francigena_19-23_agosto_2026_EN.pdf`
— è il riferimento di stile, prezzo e contenuto per questo documento.

File in questa cartella:
- `GiroMunna_Preventivo_Monte_Amiata_22_agosto_2026_IT.pdf` / `_EN.pdf`
- `GiroMunna_Proforma_Saldo_Monte_Amiata_22_agosto_2026_IT.pdf` / `_EN.pdf`
- `genera_preventivo_monte_amiata.py` — rigenera i due PDF del preventivo
- `genera_proforma_monte_amiata.py` — rigenera i due PDF della proforma
- `preventivo_monte_amiata_22_agosto_2026.html` — pagina web bilingue, con sezione interna

```bash
python3 genera_preventivo_monte_amiata.py --lingua it
python3 genera_preventivo_monte_amiata.py --lingua en
python3 genera_proforma_monte_amiata.py --lingua it
python3 genera_proforma_monte_amiata.py --lingua en
```

Il cliente (Anette Haavel) è già il valore predefinito dello script.

---

## Il prezzo

| | |
|---|---|
| Sab 22 ago — Mercedes-Benz Beluga, mezzo e conducente | € 750,00 + IVA 10% |
| Sab 22 ago — Mercedes-Benz Tourengo, mezzo e conducente | € 750,00 + IVA 10% |
| Hotel autisti | € 150,00 + IVA 10% |
| **Totale IVA inclusa** | **€ 1.815,00** |

Prezzo fissato da Girolamo in due passaggi il 21 agosto: prima il trasporto a
€ 1.500,00 netti (€ 750,00 per mezzo, con le due voci specificate
separatamente invece di una riga unica "due mezzi"), poi aggiunti € 150,00 di
hotel autisti — totale netto € 1.650,00, **€ 1.815,00 IVA inclusa**. Questo
hotel è specifico di questa giornata: non contraddice il fatto che vitto e
alloggio dei conducenti per il resto del periodo 19-23 agosto restino coperti
dal preventivo Corte Francigena — è un costo aggiuntivo legato solo
all'escursione di sabato, che Girolamo ha scelto di far pagare al cliente
invece di assorbirlo. Punto di
partenza per il confronto: la giornata di **giovedì 20 agosto** dello stesso
preventivo Corte Francigena, anch'essa a due mezzi e giornata intera (Pienza +
cena) — € 1.100,00 netti; Girolamo ha deciso di andare sopra quella cifra. Le
Filigare non è stato usato come riferimento perché è un lavoro a mezzo singolo;
qui i mezzi sono due, e Corte Francigena è la base corretta per un lavoro a due
mezzi (per un lavoro a **un solo mezzo**, il riferimento resta invece Le Filigare,
GM-2026-0821-LF — vedi CLAUDE.md).

## La proforma del saldo

Generata su richiesta di Girolamo, nello stesso formato della proforma
dell'acconto Corte Francigena (`RIFERIMENTO_GiroMunna_Proforma_Invoice_Corte_
Francigena_Deposit.pdf`, salvata qui accanto): intestatario, importo dovuto in
evidenza, dati bancari, note. A differenza di quella — che era un acconto 30%
— questa è per l'**intero importo** di questa giornata (€ 1.815,00), pagamento
unico entro 5 giorni dal servizio, come già indicato nel preventivo. Dati di
fatturazione (ID Production OÜ) e dati bancari (Banco BPM, filiale di Lucca)
ripresi identici dalla proforma dell'acconto.

## Regole ferme per ogni preventivo (valgono sempre, non solo qui)

1. **Solo a nome GiroMunna.** Il cliente non deve mai sapere di chi sono i
   mezzi. Il Tourengo si presenta con nome e caratteristiche del mezzo, mai con
   Francesco, Tuscany T.O. o l'accordo fra fratelli.
2. **Km e orari sì, ma dentro il racconto del percorso — mai come
   giustificazione del prezzo.** Il preventivo Corte Francigena vero li usa
   così: "circa 208 km, arrivo verso le 14:15", non come colonna a parte né
   come spiegazione del perché costa quella cifra.
3. **Niente trasferimenti a parte.** Nessuna riga di trasferimento o
   riposizionamento addebitata al cliente.

## Programma reale di oggi, 21 agosto (per contesto, non per il cliente)

- **09:00–11:00 circa** — ritiro della signora dimessa dall'ospedale (Grand
  Hotel Impero, Castel del Piano), andata e ritorno da Corte Francigena. Fatto.
- **17:00–23:00/23:30 circa** — Podere Le Ripi e Serendipity (serata), per il
  gruppo di Corte Francigena.
- **Domani, sabato** — due minibus, Corte Francigena → Monte Amiata → Corte
  Francigena. Orario ancora da decidere: non prima delle 9:30-10:00, per
  lasciare almeno 9h30 di riposo al conducente dopo la fine del servizio di
  stasera (fra le 23:00 e le 23:30).

## Servizio ad hoc — trasferimento ospedale → Corte Francigena

Girolamo ha chiesto se e quanto far pagare all'agenzia per il trasferimento di
stamattina (fuori da questo preventivo). Indicazione data a voce: **€ 200,00 +
IVA (€ 220,00)**, o € 150,00 + IVA (€ 165,00) come minimo. Nessun documento
richiesto finora.

## Da chiarire prima di mandare

1. Conferma di disponibilità di entrambi i mezzi per sabato — telefonata di
   Girolamo al cliente.
2. Orario di partenza per il monte e tappe (non prima delle 9:30-10:00).
3. Numero passeggeri per sabato, se cambia rispetto al resto del programma.
4. Trasferimento ospedale → Corte Francigena: se e quanto addebitare
   all'agenzia — Girolamo decide prima di documentarlo, se vuole un documento.

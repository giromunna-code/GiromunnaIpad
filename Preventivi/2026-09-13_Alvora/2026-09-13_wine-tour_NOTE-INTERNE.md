# Note interne — Wine tour Toscana 13-18.09.2026, 21 pax

**Cliente:** Alvora (Viaggi Alvora – Edgars Kolodnickis) · **Rif. preventivo realmente
inviato:** GM-2026-0913-WT21 · **Data:** 29 luglio 2026 · **Validità:** 29 agosto 2026

> ⚠️ Il 7 settembre 2026 Girolamo ha caricato il PDF realmente inviato ad Alvora
> (`b2181fc6-GiroMunnaquotationwinetour1318September2026.pdf`). Il preventivo generato in
> questa cartella (`GiroMunna_Preventivo_Tuscany_Wine_Tour..._IT/EN.pdf`, rif.
> GM-2026-0913-BI) **non è quello usato**: importi, riferimento, date e alcune condizioni
> sono diversi. Vedi "Cosa dice il preventivo realmente inviato" più sotto — è la fonte di
> verità per qualsiasi documento futuro su questo lavoro, non la tabella prezzi in fondo a
> questo file, che resta come archivio della prima stesura.

File generati:
- `GiroMunna_Preventivo_Tuscany_Wine_Tour_13-18_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Tuscany_Wine_Tour_13-18_settembre_2026_EN.pdf`
- `genera_preventivo_tuscany_wine_tour.py` — rigenera entrambi i PDF
- `preventivo_wine_tour_13-18_settembre_2026.html` — la pagina web bilingue
- `GiroMunna_Proforma_Saldo_Tuscany_Wine_Tour_13-18_settembre_2026_IT.pdf`
- `GiroMunna_Proforma_Saldo_Tuscany_Wine_Tour_13-18_settembre_2026_EN.pdf`
- `genera_proforma_saldo.py` — rigenera i due PDF della proforma a saldo

Tutto dentro `Preventivi/2026-09-13_Alvora/`.

Il cliente (Alvora) è già il valore predefinito dello script. Per rigenerare i due PDF del preventivo:

```bash
python3 genera_preventivo_tuscany_wine_tour.py --lingua it
python3 genera_preventivo_tuscany_wine_tour.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

### Cosa dice il preventivo realmente inviato (GM-2026-0913-WT21, 29 luglio 2026)

- **Totale € 4.800,00 IVA inclusa** (imponibile € 4.363,64 + IVA 10% € 436,36).
- **Acconto 30% € 1.440,00** alla conferma, **saldo entro 5 giorni prima dell'inizio del
  servizio** — cioè entro l'**8 settembre 2026**, non dopo il servizio.
- **Vitto e alloggio del conducente per tutto il tour sono INCLUSI nel prezzo**, alla voce
  "Included" del PDF. Non vanno indicati come a carico del cliente: è l'opposto di quanto
  scritto nella prima stesura di questo repository e nelle versioni precedenti della
  fattura proforma.
- Attesa oltre gli orari: € 50/ora (invariato). Partenza da una tenuta dopo le 23:00: € 250
  (non "rientro dopo le 02:00" come nelle condizioni ricorrenti generali).
- Cancellazione: gratuita oltre 30gg; da 29 a 10gg trattenuto l'acconto; negli ultimi 9gg
  50% del totale. Diversa dallo schema 60/30/10gg con 100% finale usato di default.
- IBAN corretto: **IT59 O050 3413 7070 0000 0003 424**. Quello che avevamo in CLAUDE.md e
  in tutti i documenti di questa cartella (`IT59 O053 4137 0700 0000 0034 24`) era
  **sbagliato di una cifra** (26 caratteri invece di 27, IBAN italiano non valido) — corretto
  ovunque il 7 settembre 2026, compreso CLAUDE.md.

### Fattura proforma a saldo

Generata il 7 settembre 2026, aggiornata lo stesso giorno con i dati sopra (rif. corretto
GM-2026-0913-WT21, vitto/alloggio tolto dal "non incluso", scadenza saldo con data precisa
8 settembre, IBAN corretto). Da inviare ad Alvora, stesso schema visivo del preventivo:

```bash
python3 genera_proforma_saldo.py --lingua it
python3 genera_proforma_saldo.py --lingua en
```

Riepiloga: totale € 4.800,00 IVA inclusa, acconto già versato € 1.440,00, **saldo da
versare € 3.360,00**.

**Non ha valore fiscale.** È una richiesta di pagamento, non la fattura vera emessa
dall'Agenzia delle Entrate: quella, se dovuta, va emessa da Girolamo tramite il proprio
sistema di fatturazione elettronica o il commercialista, con numerazione progressiva e dati
fiscali che questo repository non ha.

**Il preventivo PDF archiviato in questa cartella (rif. GM-2026-0913-BI) resta quello della
prima stesura e non corrisponde a quanto realmente inviato.** Se serve, va rifatto da capo
sul contenuto del PDF reale (orari, condizioni e importi sopra), non solo sui prezzi.

---

## Prezzi

| Data | Servizio | Netto |
|---|---|---|
| Dom 13 set | Aeroporto Firenze → Ruffino → Borgo Iesolana | € 950,00 |
| Lun 14 set | Giornata a disposizione: Baldetti, Il Borro, rientro | € 980,00 |
| Mar 15 set | Serata a disposizione: Badia a Coltibuono, rientro | € 680,00 |
| Mer 16 set | Borgo Iesolana → Montefoscoli → Badia di Morrona → Forte dei Marmi | € 1.250,00 |
| Ven 18 set | Forte dei Marmi → aeroporto di Firenze | € 780,00 |
| — | Vitto e alloggio conducente, 3 notti | a carico del cliente |

**Totale netto € 4.640,00 · IVA 10% € 464,00 · Totale € 5.104,00** (≈ € 243,00 a persona)

Acconto 30% € 1.530,00 — saldo € 3.574,00.

Il vitto e alloggio del conducente per le notti del 13, 14 e 15 settembre resta a carico di
Alvora, che prenota e paga direttamente. A preventivo è indicato ma non conteggiato.

## Come sono stati costruiti i prezzi

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, che è a mezzo singolo come
questo. Riportato al netto:

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Da qui la scala usata per Alvora: una giornata piena a disposizione su 140 km e 8 ore vale
più degli € 809 di una da 80 km e 5 ore; il 16 settembre, con 237 km, tre tappe e arrivo in
Versilia, è la giornata più pesante e sta sopra i mille; i trasferimenti seguono la
proporzione degli € 500 per 50 km.

**Attenzione a non ripetere l'errore della prima stesura.** Il preventivo Corte Francigena
(GM-2026-0819-CF) riporta € 550 per una giornata a disposizione e € 1.300 per un
trasferimento da 208 km, ma sono importi **per mezzo su un lavoro con due mezzi**, quindi
già scontati per volume. Usarli come base per un lavoro a mezzo singolo aveva schiacciato i
prezzi sotto mercato: il totale era uscito a € 4.015,00 contro i € 5.104,00 attuali.

## Margine

Il preventivo è costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato
€ 250-350 a giornata di servizio, senza l'alloggio del conducente che paga il cliente:
il margine sui cinque servizi è buono.

Le notti del 13, 14 e 15 servono davvero, anche se non si fatturano: Bucine dista circa
120 km dalla base e il rientro giornaliero porterebbe la giornata del conducente oltre le
12 ore. Il 16 il servizio finisce a Forte dei Marmi, a ~55 km dalla base, quindi il
conducente rientra e il 17 non si addebita nulla.

**Se invece si subappalta a Francesco**, il costo si colloca sui € 600-700 al giorno e il
margine si assottiglia parecchio. In quel caso conviene rivedere i prezzi al rialzo
di circa il 20-25% prima di inviare.

## Verifiche di accesso

- Aeroporto di Firenze: nessun onere (confermato dal preventivo Le Filigare).
- Nessuna delle cantine in programma è in ZTL. Baldetti è in loc. Pietraia, nella piana
  sotto Cortona, quindi fuori dalle limitazioni del centro storico.
- Non serve il permesso bus del Comune di Siena: Siena non è toccata.
- Se il programma dovesse includere il centro di Firenze, va aggiunto il permesso a parte.

## Da chiarire prima di inviare

1. **Indirizzo mail del cliente** — la richiesta è arrivata senza mail di accompagnamento.
2. **Bagagli del 16 settembre** — check-out da Iesolana con tutti i bagagli, due cantine e
   arrivo in hotel solo la sera. È il punto più delicato del programma.
3. **Quale tenuta Ruffino** — quotata Poggio Casciano (Bagno a Ripoli).
4. **Indirizzo dell'hotel a Forte dei Marmi** — serve per il 16 e il 18.
5. **Orari dei due voli.** Il 18 si arriva a Firenze verso le 13:50: va bene per un volo
   dalle 16:00 in poi, altrimenti conviene anticipare la partenza dall'hotel.
   Il 13, chiarire se le 10:15 sono l'orario di ritrovo o quello di atterraggio.
6. **Bloccare la disponibilità del mezzo** per il 13-18 settembre.

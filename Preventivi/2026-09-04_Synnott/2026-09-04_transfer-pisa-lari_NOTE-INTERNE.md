# Note interne — Trasferimento Pisa → Lari, 4.09.2026, 20 pax

**Cliente:** Michelle Synnott · **Rif. preventivo:** GM-2026-0904-MS · **Preparato:** 14 agosto 2026 · **Validità:** 25 agosto 2026

File generati:
- `GiroMunna_Preventivo_Transfer_Pisa_Lari_4_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Transfer_Pisa_Lari_4_settembre_2026_EN.pdf`
- `genera_preventivo_transfer_pisa_lari.py` — rigenera entrambi i PDF
- `preventivo_transfer_pisa_lari_4_settembre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-04_Synnott/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_transfer_pisa_lari.py --lingua it --cliente "Michelle Synnott"
python3 genera_preventivo_transfer_pisa_lari.py --lingua en --cliente "Michelle Synnott"
```

---

## La richiesta

Mail arrivata senza indirizzo di risposta (solo firma "Michelle Synnott"), niente da rispondere
finché non si recupera il contatto. Chiede un trasferimento **di sola andata**:

- Ven 4 settembre 2026, aeroporto di Pisa (PSA) → Castello di San Ruffino, Via di San Ruffino 2,
  56035 Lari (PI).
- 20 adulti, bagaglio standard (~1 valigia + 1 bagaglio a mano a testa).
- Volo in arrivo verso le 13:45 (orario approssimativo, da confermare con numero di volo).
- Chiede in alternativa un midibus 26-30 posti **oppure** due minivan da 8-9 posti.
- Chiede conferma esplicita su: parcheggio aeroportuale, movimentazione bagagli, pedaggi, tasse
  incluse nel prezzo, e la politica sui ritardi del volo.

Il Castello di San Ruffino risulta una location per matrimoni ed eventi a Lari (Pisa) — verificato
via ricerca web. Coerente con un gruppo di 20 persone che arriva di venerdì all'inizio di settembre.

## Perché un mezzo solo, non due minivan

GiroMunna ha un solo mezzo di proprietà, il **Beluga (26 posti + autista)**. 20 passeggeri ci
stanno comodamente, con sei posti liberi anche per i bagagli — non serve dividere il gruppo su due
minivan, che GiroMunna non ha comunque in flotta. Non è stato quindi il caso di considerare il
Tourengo del fratello Francesco: 20 persone stanno tranquillamente sul Beluga da solo, quindi la
decisione di aggiungere un secondo mezzo (che spetta comunque a Girolamo) qui non si pone nemmeno.

## Come è stato costruito il prezzo

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, a mezzo singolo come questo:
trasferimento di ~50 km per **€ 500,00 netti**.

| Riferimento | Netto |
|---|---|
| Le Filigare — trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Distanza Pisa (aeroporto) → Lari, stimata via ricerca web | ~30 km |
| **Prezzo quotato — Pisa (PSA) → Castello di San Ruffino** | **€ 480,00** |

**Non è una proporzione diretta sui km.** 500 € / 50 km = 10 €/km, che sui 30 km del percorso
cliente darebbe circa € 300 — troppo basso. Il prezzo è stato tenuto più alto per due motivi:

1. **Il chilometraggio reale del mezzo è maggiore dei 30 km fatturati.** Il Beluga parte dalla base
   di Ponte Buggianese (PT), raggiunge l'aeroporto di Pisa, fa la corsa con i passeggeri fino a
   Lari, poi rientra vuoto alla base. Le due tratte a vuoto (base→aeroporto e Lari→base) sommano
   probabilmente altri 70-90 km, quindi il costo operativo reale è ben oltre i 30 km "percepiti"
   dal cliente.
2. **Stagione alta.** Venerdì 4 settembre, location che sembra una struttura per matrimoni: giorno
   e periodo di alta domanda.

Per queste ragioni si è tenuto il prezzo vicino alla fascia alta, coerente con l'istruzione di non
scendere sotto mercato nel dubbio.

## Margine

Costruito sul mezzo di proprietà, senza pernottamento del conducente da coprire (trasferimento in
giornata, sola andata). Tra i costi diretti da coprire c'è il **parcheggio bus dell'aeroporto di
Pisa, circa € 61,00** — a differenza di Firenze, che non ha oneri di accesso, Pisa sì. Aggiungendo
questo ai 70-90 km a vuoto da e per la base (carburante, usura), il costo diretto stimato per il
servizio si aggira sui € 150-200; sui € 480,00 netti il margine resta comunque buono. **Se si
subappalta a Francesco**, va rivalutato: il costo di un mezzo esterno per una corsa così breve
rischia di assottigliare parecchio il margine.

## Da chiarire prima di inviare

1. **Indirizzo mail del cliente** — la richiesta non ha un mittente a cui rispondere.
2. **Numero e orario esatto del volo** — nella richiesta solo un orario approssimativo (13:45).
3. **Conferma definitiva dei 20 passeggeri.**
4. **Serve anche il rientro?** La richiesta menziona solo l'andata; se serve un rientro (verso
   l'aeroporto o un'altra destinazione) va quotato a parte.
5. **Accesso al Castello di San Ruffino** — verificare con la location il punto di discesa per un
   mezzo di 7,64 m, essendo una tenuta di campagna con probabile accesso su strade strette.
6. **Bloccare la disponibilità del mezzo** per il 4 settembre.

## Scadenze di cancellazione

Oggi (14 agosto) mancano **21 giorni** al servizio del 4 settembre: la prenotazione ricade già
nella fascia da 30 a 10 giorni (50% trattenuto in caso di cancellazione). Dal **25 agosto** (10
giorni prima del servizio) passerebbe alla fascia degli ultimi 10 giorni (100%). Per questo la
validità del preventivo è stata fissata al 25 agosto 2026.

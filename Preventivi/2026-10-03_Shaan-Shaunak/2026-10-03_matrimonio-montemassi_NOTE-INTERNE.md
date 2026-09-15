# Note interne — Servizio matrimonio, Montemassi 3 ottobre 2026

**Cliente:** Shaan Shaunak · **Email:** shaan.shaunak@gmail.com · **Tel.:** +44 7963 432273
**Rif. preventivo:** GM-2026-1003-SS · **Preparato:** 15 settembre 2026 · **Validità:** 22 settembre 2026

File generati:
- `GiroMunna_Preventivo_Matrimonio_Montemassi_3_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Matrimonio_Montemassi_3_ottobre_2026_EN.pdf`
- `genera_preventivo_matrimonio_montemassi.py` — rigenera entrambi i PDF
- `preventivo_matrimonio_3_ottobre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-10-03_Shaan-Shaunak/`.

Il cliente (Shaan Shaunak) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_matrimonio_montemassi.py --lingua it
python3 genera_preventivo_matrimonio_montemassi.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## La richiesta

- Servizio: matrimonio/evento, sabato 3 ottobre 2026.
- Fino a 25 passeggeri (il Beluga ne porta 26 + autista: margine di un solo posto).
- Percorso: Montemassi → Ribolla → Conti di San Bonifacio Wine Resort (Gavorrano, GR),
  con ritrovo alle 14:00 a Montemassi; rientro degli ospiti all'1:00 di notte, stesso
  percorso al contrario.
- Verificato via web: Conti di San Bonifacio è un resort/tenuta reale in Località Casteani,
  Gavorrano (GR), a circa 5 km dal Castello di Montemassi — quindi il tratto "locale" del
  lavoro (Montemassi-Ribolla-resort) è breve, pochi chilometri.

## Prezzi

| Voce | Netto |
|---|---|
| Sab 3 ott — transfer di andata (14:00) e rientro notturno (01:00), Montemassi ⇄ Conti di San Bonifacio via Ribolla | € 2.300,00 |
| Vitto e alloggio conducente, 1 notte (3 ottobre) | a carico del cliente |

**Totale netto € 2.300,00 · IVA 10% € 230,00 · Totale € 2.530,00** (≈ € 101,00 a persona, su 25 ospiti)

Acconto 30% € 759,00 — saldo € 1.771,00.

## Come è stato costruito il prezzo

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, a mezzo singolo.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Il tratto locale (Montemassi-Ribolla-resort) è breve: pochi chilometri, poco più di un
normale transfer di paese. Il vero costo di questo lavoro è il **posizionamento**: la base
GiroMunna a Ponte Buggianese dista circa 150 km da Montemassi, quindi il mezzo percorre
circa 300 km solo per arrivare e tornare. Fra il transfer delle 14:00 e il rientro
dell'1:00 corrono undici ore — troppe per un rientro alla base e una ripartenza in giornata,
troppo poche per non contare come giornata intera impegnata. Il conducente deve pernottare
in zona prima di rimettersi alla guida per il rientro (norme sui tempi di guida e riposo).

Prezzo costruito come blend fra chilometraggio (~300 km di posizionamento, scalato dagli
€ 500/50 km di Le Filigare con una tariffa a km decrescente sulla lunga distanza) e ore di
impegno (undici ore, ben oltre le 5 ore del riferimento "giornata a disposizione"). Il
risultato, € 2.300,00 netti, è tenuto sul lato alto come da prassi: Girolamo lo abbassa se
lo ritiene opportuno.

**Il punto critico è l'orario di rientro.** Partenza dalla struttura fissata per l'1:00,
con soli 20-25 minuti di transfer fino a Montemassi: si rientra entro le 02:00 (soglia del
supplemento di € 250,00 per mezzo) solo se non ci sono ritardi. Ai matrimoni è
un'ipotesi ottimistica — segnalato chiaramente al cliente nelle note del preventivo.

## Margine

Il preventivo è costruito sul **mezzo di proprietà** (Beluga). Il costo diretto — carburante
e pedaggi per ~300 km — resta contenuto, e la notte del conducente è a carico del cliente
(costo zero per GiroMunna): il margine sul prezzo pieno è ampio.

**Se si subappalta a Francesco** (base a Montecatini Terme), la distanza dalla sua base fino
a Montemassi è comunque rilevante e il costo di giornata sale: da ricalcolare prima di
confermare la disponibilità del mezzo con lui.

## Da chiarire prima di inviare

1. **Numero esatto degli ospiti** — indicato "fino a 25": con il Beluga il margine è di un
   solo posto. Chiedere conferma definitiva.
2. **Accesso a Conti di San Bonifacio** — tenuta in collina, Località Casteani. Far
   confermare dalla struttura il punto di discesa/salita e lo spazio di manovra per un mezzo
   di 7,64 m, soprattutto per la manovra notturna dell'una di notte.
3. **Orario reale del rientro** — l'1:00 indicato dal cliente: chiarire se è l'orario di
   partenza effettiva dalla struttura o quello in cui si comincia a radunare gli ospiti.
   Da questo dipende se scatta il supplemento di rientro dopo le 02:00.
4. **Prenotazione ravvicinata** — mancano solo 18 giorni al servizio (oggi 15/09, evento
   03/10): la prenotazione ricade già nella fascia di cancellazione al 50% (da 30 a 10
   giorni), e dal 23 settembre passerà al 100%. Tenere il mezzo libero finché non arriva
   una risposta e sollecitare una conferma rapida.
5. **Recapito telefonico/WhatsApp** della persona presente il giorno del matrimonio e dati
   di fatturazione, per la conferma.

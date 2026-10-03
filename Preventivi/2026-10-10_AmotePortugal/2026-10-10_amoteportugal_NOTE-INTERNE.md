# Note interne — AMOTEPORTUGAL, 10-11 ottobre 2026

**Cliente:** AMOTEPORTUGAL s.r.o. (agenzia viaggi ceca, contatto Lucie) · **Rif. preventivo:**
GM-2026-1010-AP · **Preparato:** 3 ottobre 2026 · **Validità:** 9 ottobre 2026

File generati:
- `GiroMunna_Preventivo_AmotePortugal_10-11_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_AmotePortugal_10-11_ottobre_2026_EN.pdf`
- `genera_preventivo_amoteportugal.py` — rigenera entrambi i PDF
- `preventivo_amoteportugal_10-11_ottobre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-10-10_AmotePortugal/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_amoteportugal.py --lingua it
python3 genera_preventivo_amoteportugal.py --lingua en
```

---

## Il lavoro, in breve

Lucie (AMOTEPORTUGAL, agenzia ceca) ha mandato via mail il programma completo di un tour in
Toscana di **8 giornate** (7-14 ottobre 2026) per un gruppo di **22 persone** (21 ospiti + 1
accompagnatore), chiedendo il preventivo per l'intero trasporto.

**Girolamo ha disponibilità del Beluga solo per il 10 e l'11 ottobre.** Questo preventivo quota
solo quelle due giornate (le uniche due del programma di Lucie che riguardano Pienza/Montepulciano
e Saturnia/Pitigliano/Montalcino), con una nota esplicita che per il resto del programma (7-9 e
12-14 ottobre) serve un altro fornitore di trasporto. Non ho provato a coprire le altre giornate
tramite Francesco o un mezzo a noleggio: Girolamo non lo ha chiesto, l'ha detto esplicitamente
("fai il preventivo calcolando che ho disponibilità solo per i giorni 10 e 11 ottobre").

Il gruppo di 22 persone sta comodamente sul Beluga (26 posti): nessun secondo mezzo necessario,
nessun coinvolgimento di Tuscany T.O. & Munna Bus Operator.

## Il programma dei due giorni

| Data | Percorso | Km stimati | Impegno |
|---|---|---|---|
| Sab 10 ott | Borgo Elissa (Certaldo) → Pienza → La Boutique del Pastore → Montepulciano → Hotel Dei Capitani (Montalcino) | ~145 km | 9:30–19:00 |
| Dom 11 ott | Hotel Dei Capitani → Saturnia → Pitigliano → Piombaia → Hotel Dei Capitani | ~195 km | 8:30–19:00 |

**Borgo Elissa** è un agriturismo/relais a Certaldo (FI), confermato via ricerca pubblica
(borgoelissa.com) — nelle colline fra Firenze e Siena, vista su San Gimignano. Le altre distanze
(Pienza, Montepulciano, Montalcino, Saturnia, Pitigliano) sono stime basate sulla geografia nota
della zona, non verificate km per km: sono tutte località della Toscana meridionale ben note,
raggruppate in un'area relativamente compatta (Val d'Orcia / Maremma), quindi le proporzioni
dovrebbero essere ragionevoli, ma vanno controllate se Girolamo ha dati più precisi.

## Come sono stati costruiti i prezzi

Riferimento: **Le Filigare** (GM-2026-0821-LF) — mezzo singolo, stesso schema.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 h | € 809,00 |

- **10 ottobre** (~145 km, 9,5h, trasferimento con cambio struttura e bagagli a bordo): quotato
  **€ 1.050,00**. Via di mezzo fra il tasso del trasferimento e quello della giornata a disposizione,
  con un margine in più per le tre tappe e il trasloco bagagli.
- **11 ottobre** (~195 km, 10,5h, la giornata più lunga, zona Maremma più distante): quotato
  **€ 1.250,00**. Leggermente sopra la proporzione lineare, per il margine di sicurezza su una
  giornata lunga e remota.

**Totale netto € 2.300,00 · IVA 10% € 230,00 · Totale € 2.530,00** (≈ € 115,00 a persona su 22)

Acconto 30% € 760,00 — saldo € 1.770,00.

### Margine

Mezzo di proprietà (Beluga): costo diretto stimato € 250-350 a giornata di servizio, senza il
vitto/alloggio del conducente che paga il cliente. Margine buono sulle due giornate, in linea con
Le Filigare — non è un lavoro subappaltato, quindi non si applicano le cautele sul margine viste
per Villa Cini.

### Vitto e alloggio del conducente

Una sola notte, quella del 10 ottobre a Montalcino: la base di Ponte Buggianese è troppo lontana
da Certaldo/Montalcino per un rientro giornaliero comodo prima della ripartenza delle 8:30
dell'11. Dopo l'11 ottobre il conducente può rientrare alla base in serata (Montalcino-base
~110 km): non serve una seconda notte. A carico del cliente come sempre, suggerito lo stesso
Hotel Dei Capitani.

## Perché solo due giorni e non tutti gli otto

Punto centrale di questo preventivo, va spiegato bene al cliente (fatto, nelle Note): il
programma di Lucie copre 7-14 ottobre, ma Girolamo quota solo 10-11. Rischio reale: se l'agenzia
non capisce bene questo limite, potrebbe aspettarsi un preventivo per l'intero tour e restare
confusa. La nota nel preventivo è esplicita su questo fin dal primo punto.

## Tempistica — urgente

La richiesta è arrivata il 3 ottobre per un servizio che comincia il 10: **7 giorni di margine**,
pochissimo per gli standard di questi preventivi. Di conseguenza:
- La prenotazione cade già nella fascia di cancellazione più severa (ultimi 10 giorni = 100% in
  caso di cancellazione dopo la conferma) fin dal momento dell'invio. Segnalato esplicitamente nel
  preventivo.
- Validità impostata al 9 ottobre (il giorno prima del servizio) invece delle consuete 2
  settimane, perché non avrebbe senso altrimenti.
- Il cliente ha scritto che gli serve una risposta rapida per chiudere il programma con i suoi
  clienti: vale la pena che Girolamo risponda il prima possibile.

## Da chiarire prima di inviare

1. **Il numero definitivo dei passeggeri** — qui si è usato 22 (21 ospiti + 1 accompagnatore),
   come indicato dalla cliente.
2. **Punto di discesa a Montepulciano e Pitigliano** — entrambi centri storici con strade
   stretto; da confermare con le guide locali se serve un permesso comunale per il bus.
3. **Recapito telefonico/WhatsApp** di chi viaggia con il gruppo.
4. **Dati di fatturazione** di AMOTEPORTUGAL s.r.o.
5. **Le distanze non sono verificate km per km** — solo stime geografiche ragionevoli; se
   Girolamo conosce meglio la zona (Pienza, Montepulciano, Montalcino, Saturnia, Pitigliano) può
   correggere prima di inviare.

## Nessuna mail preparata

Come da regola aggiornata in CLAUDE.md: il testo per il cliente si scrive solo su richiesta
esplicita di Girolamo, pronto da copiare — non si manda nulla in autonomia e non si crea alcuna
bozza in Gmail. Per ora consegno solo il preventivo.

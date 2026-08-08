# Note interne — Wine tour Toscana 13-18.09.2026, 21 pax

**Cliente:** Alvora · **Rif. preventivo:** GM-2026-0913-BI · **Preparato:** 8 agosto 2026 · **Validità:** 22 agosto 2026

File generati:
- `GiroMunna_Preventivo_Tuscany_Wine_Tour_13-18_settembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Tuscany_Wine_Tour_13-18_settembre_2026_EN.pdf`
- `genera_preventivo_tuscany_wine_tour.py` — rigenera entrambi i PDF
- `preventivo_wine_tour_13-18_settembre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-09-13_Alvora/`.

Il cliente (Alvora) è già il valore predefinito dello script. Per rigenerare i due PDF:

```bash
python3 genera_preventivo_tuscany_wine_tour.py --lingua it
python3 genera_preventivo_tuscany_wine_tour.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

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

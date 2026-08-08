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
| Dom 13 set | Aeroporto Firenze → Ruffino → Borgo Iesolana | € 750,00 |
| Lun 14 set | Giornata a disposizione: Baldetti, Il Borro, rientro | € 780,00 |
| Mar 15 set | Serata a disposizione: Badia a Coltibuono, rientro | € 520,00 |
| Mer 16 set | Borgo Iesolana → Montefoscoli → Badia di Morrona → Forte dei Marmi | € 950,00 |
| Ven 18 set | Forte dei Marmi → aeroporto di Firenze | € 650,00 |
| — | Vitto e alloggio conducente, 3 notti | € 420,00 |

**Totale netto € 4.070,00 · IVA 10% € 407,00 · Totale € 4.477,00** (≈ € 213,00 a persona)

Acconto 30% € 1.350,00 — saldo € 3.127,00.

## Come sono stati costruiti i prezzi

Base di riferimento: i preventivi Le Filigare (GM-2026-0821-LF) e Corte Francigena
(GM-2026-0819-CF), riportati a un solo mezzo.

| Riferimento | Ricavato |
|---|---|
| Le Filigare — trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 netti |
| Le Filigare — giornata a disposizione Siena, ~80 km, 5 h | € 809,00 netti |
| Corte Francigena — trasferimento FCO → Montalcino, 208 km | € 1.300,00 netti/mezzo |
| Corte Francigena — Montalcino → Roma centro → FCO, 211 km + 2 h in città | € 1.650,00 netti/mezzo |
| Corte Francigena — giornata a disposizione, corto raggio | € 550,00 netti/mezzo |
| Corte Francigena — serata a disposizione, 3 km | € 400,00 netti/mezzo |
| Corte Francigena — vitto e alloggio conducenti | € 137,50 a notte |

Il vitto e alloggio è stato arrotondato a € 140,00 × 3 notti. Le notti del 13, 14 e 15
servono davvero: Bucine dista circa 120 km dalla base e il rientro giornaliero porterebbe
la giornata del conducente oltre le 12 ore. Il 16 il servizio finisce a Forte dei Marmi,
a ~55 km dalla base, quindi il conducente rientra e il 17 non si addebita nulla.

## Margine

Il preventivo è costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato
€ 250-350 a giornata di servizio più € 140 a notte di alloggio: il margine sui cinque
servizi è buono.

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

# Note interne — Trasporto privato a Capannori, 20-24 aprile 2027

**Cliente:** Lisa Parks · **Rif. preventivo:** GM-2027-0420-LP · **Preparato:** 13 settembre 2026 · **Validità:** 13 ottobre 2026

File generati:
- `GiroMunna_Preventivo_Villa_Capannori_20-24_aprile_2027_IT.pdf`
- `GiroMunna_Preventivo_Villa_Capannori_20-24_aprile_2027_EN.pdf`
- `genera_preventivo_villa_capannori.py` — rigenera entrambi i PDF
- `preventivo_villa_capannori_20-24_aprile_2027.html` — la pagina web bilingue

Tutto dentro `Preventivi/2027-04-20_Parks/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_villa_capannori.py --lingua it
python3 genera_preventivo_villa_capannori.py --lingua en
```

Con `--cliente "Altro Nome"` si cambia l'intestatario.

---

## La richiesta del cliente

Lisa Parks (Stati Uniti) scrive direttamente, senza agenzia, per un gruppo di 12-14 adulti
in villa a Capannori dal 20 al 24 aprile 2027. Chiede conducenti di lingua inglese e un
programma su 5 giornate: arrivo alla stazione di Firenze S.M.N. con sosta supermercato e
cena serale (20), Firenze mattina e pomeriggio (21), cantina/pranzo e cena a Lucca (22),
trasporti locali orario da definire (23), trasferimento aeroporto di Firenze (24). Ha
lasciato telefono/WhatsApp +1 203 326 0918 e più indirizzi email, spiegando che l'account
USA potrebbe avere problemi a ricevere risposte — utile saperlo se Girolamo dovesse
scriverle.

Ha chiesto di quotare **due opzioni**: un solo minibus per tutto il gruppo, oppure due
furgoni da 6-7 posti ciascuno.

## Perché è stato quotato solo il Beluga

Il gruppo (12-14 persone) sta comodamente nel Beluga (26 posti): non serve un secondo mezzo
e quindi il tema Tourengo/Francesco non si pone qui. La richiesta dei due furgoni da 6-7
posti è un'altra cosa: GiroMunna non possiede né gestisce furgoni di quella taglia, non è
il Tourengo (che è un minibus da 28 posti, non un furgone) e non rientra nello schema
Beluga/secondo minibus del CLAUDE.md. Non avendo una tariffa reale su cui basarsi, **non è
stato messo a preventivo un prezzo per i furgoni**: è stato segnalato al cliente come nota,
lasciando aperta la possibilità di approfondire con un fornitore esterno se lo richiede
davvero. Decisione da confermare con Girolamo se la cliente insiste.

## Come sono stati costruiti i prezzi

Riferimento: il preventivo **Le Filigare (GM-2026-0821-LF)**, a mezzo singolo come questo
lavoro.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento, ~50 km | € 500,00 |
| Giornata a disposizione, ~80 km, 5 ore | € 809,00 |

| Data | Servizio | Netto |
|---|---|---|
| Mar 20 apr | Stazione Firenze S.M.N. → villa (~80 km) + cena in serata (~16 km) | € 680,00 |
| Mer 21 apr | Due trasferimenti separati Capannori↔Firenze (~80 km ciascuno), nessuna attesa prolungata | € 800,00 |
| Gio 22 apr | Giornata più pesante: ~7 ore a disposizione di giorno (cantine, pranzo) + serata a Lucca, ~11 ore su due turni | € 1.430,00 |
| Ven 23 apr | Programma da confermare, prezzata come giornata piena a disposizione locale — **provvisoria** | € 880,00 |
| Sab 24 apr | Villa → aeroporto di Firenze (~80 km) | € 680,00 |

**Totale netto € 4.470,00 · IVA 10% € 447,00 · Totale € 4.917,00** (tra € 351,00 e € 410,00
a persona secondo il numero definitivo tra 12 e 14).

Acconto 30% € 1.475,10 — saldo € 3.441,90.

Nel dubbio i prezzi sono stati tenuti alti, come da indicazione: il 23 aprile in particolare
è una stima prudente in attesa del programma reale.

## Nessuna notte del conducente

Ponte Buggianese dista da Capannori circa 25-30 km: il conducente rientra alla base ogni
sera, quindi qui **non serve** vitto e alloggio a carico del cliente (diversamente dal
preventivo Alvora, dove Borgo Iesolana era a 120 km). Da tenere d'occhio il cambio turno fra
il 22 e il 23: la cena a Lucca finisce verso mezzanotte, quindi nel preventivo si chiede di
non far partire i trasporti del 23 prima delle 10:00 circa, per i tempi di riposo.

## Margine

Costruito sul mezzo di proprietà (Beluga), senza notti del conducente da coprire: il
margine sui cinque servizi è buono, in linea con un lavoro locale a corto raggio.

## Da verificare prima di procedere

1. **Numero definitivo dei partecipanti** (12-14) e indirizzo esatto della villa a
   Capannori.
2. **Orario del treno** in arrivo il 20 aprile a Firenze S.M.N. e **orario del volo** in
   partenza il 24 aprile dall'aeroporto di Firenze.
3. **Programma del 23 aprile**, ancora da definire lato cliente: il prezzo potrà cambiare
   una volta noto.
4. **Decisione sui furgoni**: se la cliente insiste per due mezzi più piccoli invece del
   Beluga, va sentito un fornitore esterno (o Francesco, se pertinente) per un preventivo
   dedicato — non è una decisione da prendere di iniziativa.
5. **Cantine del 22 aprile**: proporre un paio di indirizzi nelle Colline Lucchesi se la
   cliente non ne indica.
6. **Bloccare la disponibilità del mezzo** per il 20-24 aprile 2027.

Nessuna bozza di mail è stata preparata: alla risposta a Lisa Parks ci pensa Girolamo, con i
suoi tempi e le sue parole.

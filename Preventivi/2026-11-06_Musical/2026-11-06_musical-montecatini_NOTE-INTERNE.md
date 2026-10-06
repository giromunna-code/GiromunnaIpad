# Note interne — Compagnia di musical, Firenze ↔ Teatro Verdi di Montecatini, 6.11.2026

**Cliente:** Gianna, compagnia di musical di Firenze — richiesta arrivata su WhatsApp, +39 328 927 3339 (nome della compagnia ed email da completare)
**Rif. preventivo:** GM-2026-1106-MF · **Preparato:** 6 ottobre 2026 · **Validità:** 13 ottobre 2026

File generati:
- `GiroMunna_Preventivo_Firenze_Montecatini_6_novembre_2026_IT.pdf`
- `GiroMunna_Preventivo_Firenze_Montecatini_6_novembre_2026_EN.pdf`
- `genera_preventivo_musical_montecatini.py` — rigenera entrambi i PDF
- `MAIL.md` — testo della mail, italiano e inglese

Quando si sa il nome della compagnia, rigenerare con:

```bash
python3 genera_preventivo_musical_montecatini.py --lingua it --cliente "Gianna, compagnia di musical di Firenze"
python3 genera_preventivo_musical_montecatini.py --lingua en --cliente "Gianna, compagnia di musical di Firenze"
```

## Prezzi

| Voce | Netto |
|---|---|
| Ven 6/11 Firenze → Montecatini, arrivo entro le 10:00 | € 500,00 |
| Notte 6–7/11 Montecatini → Firenze, partenza 2:00 | € 500,00 |
| Supplemento rientro dopo le 02:00 | € 250,00 |
| **Totale netto** | **€ 1.250,00** |

IVA 10% € 125,00 · **Totale € 1.375,00** — acconto € 412,50, saldo € 962,50.

Base Le Filigare: € 500 per un trasferimento di ~50 km. Fra le due corse il mezzo sta in sede
(Ponte Buggianese è a ~10 km da Montecatini): niente attesa, niente vitto del conducente.

## Da decidere

1. **Sovrapposizione con Gori (GM-2026-1107-FG).** Il Beluga rientra in sede verso le 3:45
   del 7/11 e per Gori deve ripartire verso le 4:15 (Prato alle 5:00). Stesso autista
   impossibile per il riposo obbligatorio. Se si confermano entrambi: secondo autista o
   Tourengo di Francesco per uno dei due. Decide Girolamo.
2. **Risposte di Gianna (6 ottobre):** partenza e rientro all'Off Musical, Via di San Giusto,
   davanti all'ospedale di Torregalli (fuori ZTL, niente check point); solo borsoni personali,
   il materiale va sul loro furgone; sperano di finire prima delle 2:00. Nel preventivo: se
   partono da Montecatini entro l'1:10 il supplemento notturno si toglie (totale € 1.100 IVA
   inclusa). Anche così il Beluga rientra in sede verso le 2:45: la sovrapposizione con Gori resta.
3. **Prezzo deciso da Girolamo (6 ottobre): € 1.000,00 IVA inclusa in tutto** (€ 909,09 + IVA
   € 90,91), rientro notturno compreso. Acconto € 300, saldo € 700. Sostituisce i € 1.375 iniziali.

# Note interne — Transfer Pescia → Mantova, 25.10.2026, 14 pax

**Cliente:** non firmato — messaggio arrivato senza nome né recapito · **Rif. preventivo:** GM-2026-1025-MN ·
**Preparato:** 16 settembre 2026 · **Validità:** 30 settembre 2026

File generati:
- `GiroMunna_Preventivo_Pescia_Mantova_25_ottobre_2026_IT.pdf`
- `GiroMunna_Preventivo_Pescia_Mantova_25_ottobre_2026_EN.pdf`
- `genera_preventivo_mantova.py` — rigenera entrambi i PDF
- `preventivo_pescia_mantova_25_ottobre_2026.html` — la pagina web bilingue

Tutto dentro `Preventivi/2026-10-25_Mantova-Mascara/`.

Per rigenerare i due PDF:

```bash
python3 genera_preventivo_mantova.py --lingua it
python3 genera_preventivo_mantova.py --lingua en
```

Con `--cliente "Nome Cliente"` si sostituisce il segnaposto "il gruppo di 14 persone" nell'intestazione.
**Appena si conosce il nome del cliente**, conviene anche aggiornare a mano il suffisso del riferimento
(`RIF = "GM-2026-1025-MN"`, riga 51 dello script) con le sue iniziali, e rinominare la cartella.

---

## La richiesta

> Avrei bisogno di un preventivo per un pulmino per 14 persone con autista per domenica 25 ottobre,
> partenza ore 15 circa da via della stazione, 76 Pescia per Mantova, Discoteca Mascara viale della
> Favorita, 17 e partenza da lì verso mezzanotte circa.

Nessuna firma, nessun recapito. Il messaggio da solo non basta per intestare il preventivo o per
richiamare il cliente in caso di dubbi.

## Prezzi

| Voce | Netto |
|---|---|
| Trasferimento Pescia → Mantova → Pescia, mezzo e conducente a disposizione dalle 15:00 a fine servizio (~480 km) | € 1.750,00 |
| Supplemento rientro dopo le 02:00 (arrivo a Pescia previsto verso le 03:15) | € 250,00 |

**Totale netto € 2.000,00 · IVA 10% € 200,00 · Totale € 2.200,00** (≈ € 157,00 a persona)

Acconto 30% € 660,00 — saldo € 1.540,00.

Niente vitto/alloggio conducente: è un trasferimento in giornata, il conducente rientra la notte stessa.

## Come è stato costruito il prezzo

Riferimento: **il preventivo Le Filigare (GM-2026-0821-LF)**, a mezzo singolo come questo lavoro.

| Riferimento Le Filigare | Netto |
|---|---|
| Trasferimento FLR → San Donato in Poggio, ~50 km | € 500,00 |
| Giornata a disposizione Siena, ~80 km, 5 ore | € 809,00 |

Questo lavoro è molto più grande su entrambi gli assi: ~480 km complessivi contro gli 80 km della
giornata di riferimento, e un impegno del mezzo di circa 12 ore (15:00–03:15) contro le 5 ore. Non
esiste un preventivo a due mezzi comparabile da usare come base: Corte Francigena è fuori scala per
un lavoro di questo tipo, quindi non l'ho toccato.

Il prezzo di € 2.000 netti è stato tenuto **volutamente alto**, come da prassi GiroMunna: Girolamo lo
abbassa se vuole, ma non è recuperabile un preventivo uscito sotto mercato.

Il supplemento di € 250,00 per il rientro dopo le 02:00 non è una clausola contingente qui: con
partenza da Mantova a mezzanotte e ~3h15 di rientro, l'arrivo a Pescia oltre le 02:00 è già previsto
dal programma. Per questo è stato messo a preventivo come riga esplicita, non lasciato tra le condizioni
generiche del "non incluso".

## Perché non serve il pernottamento del conducente

A differenza di Alvora (più notti fuori base), qui si parte e si torna nella stessa nottata. Le quasi
sei ore di attesa a Mantova (18:15 – mezzanotte circa) coprono il riposo del conducente prima del
viaggio di ritorno, che è lungo quanto quello di andata. Il quadro orario resta comunque pesante:
un'unica giornata di servizio da 12 ore circa, con ~6 ore di guida effettiva — sotto ai limiti di
guida giornalieri, ma è comunque una serata lunga per chi è al volante.

## Margine

Costruito sul **mezzo di proprietà** (Beluga). Costo diretto stimato: carburante e pedaggi per ~480 km
più l'ora extra di conducente per il rientro notturno — il margine sul netto di € 2.000 è ampio.

**Se si subappalta a Francesco**, il costo di un lavoro così lungo si avvicina ai € 900-1.100 e il
margine si assottiglia parecchio. In quel caso conviene rivedere i prezzi al rialzo prima di inviare.

## Punti verificati solo in parte

- **Distanza e tempi Pescia–Mantova**: stimati (~240 km, ~3h15 a tratta) da ricerche stradali generiche
  (il dato puntuale Pescia→Mantova non è emerso nelle ricerche fatte; ho usato come riferimento
  Pisa–Mantova, ~271 km / 2h59, scalato per la posizione di Pescia rispetto a Pisa). Da confermare con
  un calcolo percorso preciso prima di comunicare gli orari come definitivi.
- **ZTL di Mantova**: non è fra le condizioni note del preventivario (solo Firenze, Pisa, Siena sono
  documentate). Non ho trovato conferma se Viale della Favorita rientri in una zona a traffico limitato:
  nel preventivo è rimasta una condizione generica ("se necessario"), da non prendere come dato certo.
- **Punto di carico/scarico alla discoteca**: nessuna informazione diretta su dove un pullman può
  fermarsi o sostare in Viale della Favorita 17. Segnalato al cliente come nota, ma andrebbe verificato
  anche da parte nostra se si conosce qualcuno che lavora già con quel locale.

## Da chiarire prima di inviare

1. **Nome e recapito del cliente** — il messaggio non ha firma, telefono o email.
2. **Orario di rientro reale** — mezzanotte è presto per uscire da una discoteca: probabile che sia una
   stima di massima. Ogni ora oltre l'orario indicato si paga a parte (€ 50,00/ora per mezzo).
3. **Indirizzo di rientro** — quotato fino allo stesso punto di partenza (via della Stazione 76); se il
   gruppo va lasciato in più punti, va chiarito ma non cambia il prezzo.
4. **Numero definitivo dei passeggeri** — quotato per 14, come richiesto.
5. **Bloccare la disponibilità del mezzo** per la notte del 25-26 ottobre.

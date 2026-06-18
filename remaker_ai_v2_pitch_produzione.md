# ReMaker AI — Documento di Produzione e Pitch (v2.0)
> **Payoff:** Non buttare. Reinventa.
> **Sottotitolo:** Dai una seconda vita agli oggetti che hai già.

Questo documento integra la visione strategica commerciale (**Pitch Deck Blueprint**) e le specifiche tecniche operative (**Product Requirement Document**) per lo sviluppo e il lancio di **ReMaker AI**.

---

## 1. Pitch Deck Blueprint — Business & Vision

### Il Problema Globale

Nelle case degli italiani si accumulano costantemente oggetti, dispositivi elettronici e arredamento inutilizzati. I dati lo confermano senza margine di dubbio: **ogni italiano conserva in media tra 6 e 15 oggetti inutilizzati in casa, per un valore stimato di 1.247 euro a persona** (Osservatorio Second Hand Economy, BVA Doxa / Subito, 2024).

Eppure, la maggior parte di questi oggetti non vengono venduti, donati o trasformati. Il motivo? Tre barriere strutturali:

- **Asimmetria informativa:** Il proprietario non conosce il valore reale di mercato dell'oggetto che possiede.
- **Attrito operativo:** Caricare un annuncio, fotografare, descrivere, rispondere a messaggi — richiede tempo e competenze che la maggior parte delle persone non ha voglia di dedicare.
- **Deficit creativo:** È difficile immaginare usi alternativi per un tablet del 2019 o una stampante ferma in garage.

Il risultato è che miliardi di euro di valore economico rimangono letteralmente nei cassetti.

---

### Il Mercato: Dati e Dimensione

**L'economia dell'usato in Italia è già un mercato di massa — non un trend di nicchia.**

| Indicatore | Valore | Fonte |
|---|---|---|
| Valore mercato usato Italia 2024 | **€27 miliardi** (+€1 mld vs 2023) | BVA Doxa / Subito, 2024 |
| % del PIL italiano | **1,2%** | BVA Doxa / Subito, 2024 |
| Italiani attivi nel second hand | **27,2 milioni** | BVA Doxa / Subito, 2024 |
| Quota transazioni online | **€14,4 miliardi (54%)** | BVA Doxa / Subito, 2024 |
| Solo elettronica usata Italia | **€5,2 miliardi (+6% YoY)** | Osservatorio SHE, 2024 |
| Mercato globale dispositivi ricondizionati | **$143,8 mld entro 2031** | Allied Market Research |
| Crescita telefoni ricondizionati in Italia | **+15% nel 2023** | Millionaire / SWG |
| Crescita shopping second hand EU 2024 | **+19%** | PwC / Quifinanza |
| Valore medio guadagno per chi vende usato | **€820/anno** | Osservatorio SHE, 2024 |

**Il mercato cresce, è digitale, ed è già in mano ai consumatori.** ReMaker AI non crea un mercato — si inserisce in uno che vale 27 miliardi e accelera la conversione degli oggetti fermi in liquidità o valore.

#### TAM / SAM / SOM

- **TAM (Mercato Totale Indirizzabile):** €27 miliardi — valore totale del mercato second hand Italia.
- **SAM (Mercato Raggiungibile):** €5,2 miliardi — segmento elettronica + €7,3 miliardi casa & persona = **€12,5 miliardi** (categorie su cui si concentra il prodotto nella fase MVP).
- **SOM (Mercato Ottenibile — anno 1):** Stimiamo di raggiungere 50.000 utenti attivi nei primi 12 mesi con un tasso di conversione al Premium del 5% → **ARR potenziale: ~€240.000** (base conservativa pre-B2B).

---

### La Soluzione: ReMaker AI

Un ecosistema guidato da Intelligenza Artificiale multimodale che converte in meno di 30 secondi un oggetto inutilizzato in una risorsa di valore. Non è un riconoscitore di oggetti. È un **motore decisionale contestuale** che fa in un unico flusso ciò che oggi richiederebbe 4 strumenti separati:

1. **Scan intelligente** — Identificazione tramite foto, video o testo.
2. **Valutazione di mercato in tempo reale** — Stima del prezzo tramite API marketplace attivi (eBay, Subito, Wallapop).
3. **10 idee di riuso personalizzate** — Ordinate per utilità, costo e difficoltà.
4. **Annuncio pronto alla pubblicazione** — Titolo, descrizione SEO e prezzo ottimizzati, generati automaticamente.
5. **Mappa donazioni e RAEE** — Centri di raccolta geolocalizzati via CAP o GPS.

> **In < 30 secondi. Da un oggetto fermo a un'azione concreta.**

#### Perché non basta Google Lens + ChatGPT?

Nessuno strumento esistente combina questi cinque elementi in un unico flusso ottimizzato per l'utente non tecnico. Google Lens riconosce. ChatGPT suggerisce. eBay vende. Ma nessuno li connette in modo contestuale, rapido e mobile-first. ReMaker AI è l'interfaccia unificata che manca.

---

### Evidenza Qualitativa: Insight da Problem Interview

> *"Ho parlato con 15 persone tra 28 e 60 anni. Il 100% aveva almeno un oggetto inutilizzato da più di 6 mesi. Il 73% non lo aveva venduto per 'non sapere quanto vale' o 'non avere tempo di fare l'annuncio'. Solo 2 persone su 15 conoscevano un centro RAEE nella propria città. Nessuno aveva mai trasformato un vecchio device in qualcosa di utile — pur avendoci pensato."*

Questo non è un problema di volontà. È un problema di frizione. ReMaker AI elimina la frizione.

---

### Competitori e Posizionamento

| Strumento | Cosa fa | Cosa NON fa |
|---|---|---|
| Google Lens | Riconosce l'oggetto | Non stima valore, non genera annuncio, non suggerisce riuso |
| ChatGPT | Suggerisce idee generiche | Non ha dati di mercato in tempo reale, non geolocalizza |
| Subito / eBay | Permette di vendere | Richiede effort elevato: foto, descrizione, prezzo manuale |
| BackMarket | Ricondizionato certificato | Solo elettronica, solo per rivenditori professionali |
| **ReMaker AI** | **Tutto il flusso in un posto** | — |

---

### Modello di Business

Il modello si basa su una struttura Freemium con ricavi B2C e B2B:

#### B2C

| Tier | Prezzo | Contenuto |
|---|---|---|
| **Free** | €0 | 3 scan/giorno, 10 idee base, stima valore indicativa, mappa RAEE |
| **Plus** | €2,99/mese | Scan illimitati, export PDF base, history oggetti |
| **Pro** | €7,99/mese | Guide DIY step-by-step, inventario multi-stanza, listing auto-generato con pubblicazione diretta |

**Logica pricing:** Chi recupera €90 da un tablet con ReMaker AI non percepisce €7,99/mese come un costo — lo percepisce come un investimento con ROI immediato.

#### B2B e Revenue Aggiuntive

- **Affiliazioni contestuali:** Commissioni 2-5% su accessori per upcycling (Amazon, Leroy Merlin) e lead verso piattaforme partner (Wallapop, BackMarket, Subito).
- **Transaction fee (V2):** 2-3% sul valore stimato dell'oggetto venduto tramite listing generato da ReMaker AI — il modello più difendibile: allineamento totale di incentivi tra utente e prodotto.
- **API B2B:** Licenza white-label per compagnie assicurative, piattaforme di e-commerce e operatori RAEE che vogliono offrire la valutazione AI ai propri clienti.

---

### Scalabilità e Visione a 3 Anni

L'opportunità non si limita all'Italia. Lo shopping second hand in Europa è cresciuto del **+19% nel 2024**. Il mercato globale del re-commerce è proiettato a **$350 miliardi entro il 2028**. ReMaker AI è costruito per scala europea fin dall'architettura: stack internazionalizzabile, API marketplace multi-paese, prompting multilingua.

---

## 2. Product Requirement Document

### Architettura del Flusso Utente

Per superare i limiti del puro riconoscimento visivo, ReMaker AI adotta un approccio di **identificazione ibrida assistita**:

1. **Input:** Foto/video o testo libero (es. *"Ho un vecchio iPhone 8 con batteria scarica"*).
2. **Analisi multimodale:** Image Recognition estrae categoria macro. LLM analizza testo + stima visiva → identikit definitivo dell'oggetto.
3. **Integrazione dati:** Query in tempo reale su API marketplace per stima valore corrente.
4. **Conferma utente:** Form rapido (Marca / Modello / Stato) per ridurre errori di riconoscimento.
5. **Output:** Scheda dinamica divisa per moduli d'azione.

---

### Esempio di Output: Caso d'Uso "Vecchio Tablet"

```
Oggetto Riconosciuto:   Tablet Android 10" (Hardware 2019, apparentemente integro)
Valutazione Economica:  €40 – €90 (in base allo stato di usura stimato)
Miglior Uso Consigliato: Display smart per casa, cucina o camper
Annuncio Generato:      "Tablet Android 10" 2019, funzionante, ottimo per chi cerca
                         un display secondario. Ideale come cornice digitale o schermo
                         ricette. Prezzo consigliato: €65. Spedizione disponibile."
Centro RAEE più vicino: [geolocalizzato via CAP]
```

**Idee generate (10):** Cornice digitale, Monitor ricette in cucina, Baby monitor, Telecomando domotica, Lettore eBook, Schermo videosorveglianza, Tablet per anziani (UI semplificata), Controller per drone, Secondo schermo per PC, Strumento educativo per bambini.

---

### Tabella Moduli Funzionali MVP vs Premium

| Modulo | Descrizione | Inclusione |
|:---|:---|:---|
| **Scan & OCR** | Riconoscimento foto + form conferma (Marca/Modello/Stato) | **MVP / FREE** |
| **Idea Generator** | 10 suggerimenti ordinati per utilità, costo, difficoltà | **MVP / FREE** |
| **Marketplace Pricing** | Stima range di prezzo via API storiche + scraping controllato | **MVP / FREE** |
| **Listing Auto-Gen** | Scrittura automatica di titolo, descrizione SEO e prezzo consigliato | **MVP / FREE** |
| **Donation & Recycling** | Mappa RAEE, onlus, scuole, associazioni via GPS/CAP | **MVP / FREE** |
| **Step-by-Step DIY** | Tutorial interattivi con schemi grafici ed export PDF | **PREMIUM V1** |
| **Smart Inventory** | Inventario digitale multi-stanza con valore aggregato | **PREMIUM V2** |
| **Direct Listing** | Pubblicazione diretta su Subito / eBay / Wallapop dall'app | **PREMIUM V2** |
| **B2B API** | Endpoint white-label per partner assicurativi / e-commerce | **V3** |

---

### Stack Tecnologico

| Layer | Scelta | Motivazione |
|---|---|---|
| **Frontend** | Flutter o React Native | Cross-platform iOS/Android, unica codebase |
| **Backend** | Node.js / Python FastAPI | Gestione efficiente payload immagini, orchestrazione prompt |
| **AI Core** | OpenAI GPT-4o / Google Gemini 1.5 Pro | Analisi multimodale immagine + testo |
| **Database** | PostgreSQL + Redis | Dati strutturati utente + caching stime prezzo |
| **Marketplace API** | eBay Finding API, Subito API, Wallapop scraping | Pricing in tempo reale |
| **Geo** | Google Maps API / OpenStreetMap | Mappa centri RAEE e donazione |

---

### Esperimento di Validazione — 2 Settimane, Costo Zero

Prima di sviluppare l'app completa, valida il core con questo MVP minimo:

**Telegram Bot ReMaker AI**
- L'utente manda una foto di un oggetto.
- Il bot chiama GPT-4o Vision → identifica l'oggetto → genera 5 idee di riuso + stima prezzo eBay.it.
- Risponde in meno di 15 secondi.

**Costo:** €0 (API trial Anthropic/OpenAI) + 2-3 giorni di sviluppo.
**Metrica:** Testa con 20 utenti. Misura retention a 7 giorni. Se >40% torna una seconda volta: il core value proposition funziona.

---

### Roadmap di Sviluppo

| Fase | Durata | Obiettivi |
|---|---|---|
| **Alpha** | Mese 1-2 | Integrazione API multimodali, prompt engineering anti-allucinazione, Telegram bot MVP |
| **Beta Pubblica** | Mese 3-4 | MVP app mobile, categorie elettronica + arredamento, validazione metriche di retention |
| **Monetizzazione** | Mese 5-6 | Piani Premium, affiliazioni contestuali, primi contatti B2B |
| **Scale EU** | Anno 2 | Espansione multi-paese, transaction fee, API white-label |

---

### Rischi e Mitigazioni

| Rischio | Livello | Mitigazione |
|---|---|---|
| Allucinazioni AI sul valore oggetto | Alto | Form di conferma utente + disclaimer + range di prezzo (non valore puntuale) |
| Dipendenza da API marketplace | Medio | Multi-source (eBay + Subito + scraping) + cache Redis per ridurre chiamate |
| Bassa retention post-scan | Medio | Notifiche proattive ("Hai 3 oggetti non venduti. Vuoi aggiornare il prezzo?") |
| Competitori big tech | Basso (breve termine) | Focus su UX verticale e community — Google e Apple non costruiscono prodotti così verticali |

---

## 3. Appendice: Fonti Dati di Mercato

| Fonte | Dato Utilizzato | Anno |
|---|---|---|
| BVA Doxa / Subito — Osservatorio Second Hand Economy | €27 miliardi mercato usato Italia, 27,2 milioni utenti, €5,2 mld elettronica | 2024 |
| Osservatorio SHE | €1.247 valore oggetti inutilizzati per persona, €820 guadagno medio annuo venditori | 2024 |
| Allied Market Research | $143,8 miliardi mercato globale ricondizionati entro 2031 | 2024 |
| Millionaire / SWG | +15% crescita telefoni ricondizionati Italia | 2023 |
| PwC / Quifinanza | +19% shopping second hand EU 2024, 70% Gen Z acquista usato | 2024 |
| ThredUp 2024 Resale Report | $350 miliardi mercato globale re-commerce entro 2028 | 2024 |
| Counterpoint Research | 1 cellulare su 5 venduto nel 2024 sarà ricondizionato | 2024 |

---

*Documento v2.0 — Aggiornato con dati di mercato verificati. Uso interno / pitch.*

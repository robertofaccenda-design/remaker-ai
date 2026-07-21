# ReMaker AI 🌱

> **Non buttare. Reinventa.** / **Don't throw away. Reinvent.**

---

## 🇮🇹 Italiano

### Cos'è ReMaker AI

ReMaker AI è una web app che trasforma oggetti inutilizzati in opportunità concrete in meno di 30 secondi.

Carica una foto o descrivi un oggetto che non usi più: l'intelligenza artificiale lo identifica, stima il suo valore di mercato, genera idee di riuso personalizzate e scrive un annuncio pronto da pubblicare.

### Funzionalità

- 📷 **Scan da foto o testo** — carica un'immagine, descrivi l'oggetto, o usa entrambi insieme
- 💰 **Stima di mercato** — range di prezzo basato su Subito.it / eBay.it
- ♻️ **Idee di riuso** — 6 suggerimenti categorizzati: Vendi, Dona, Trasforma, Ripara
- 📝 **Annuncio pronto** — titolo SEO, descrizione persuasiva e hashtag copiabili in un click
- 👗 **Integrazione Vinted** — per abbigliamento, scarpe e accessori: brand, taglia, colore, materiale, categoria e condizione già compilati
- 🔧 **Ricambi e accessori** — suggerimenti specifici su dove trovare pezzi di ricambio
- 🤖 **Telegram Bot** — disponibile su [@ReMakerAI_bot](https://t.me/ReMakerAI_bot)

### Come usarla

1. Apri l'app su [remaker-ai.roberto-faccenda.workers.dev/remaker-test](https://remaker-ai.roberto-faccenda.workers.dev/remaker-test)
2. Carica una foto o scrivi una descrizione (o entrambe)
3. Clicca **Analizza oggetto**

Nessuna API key richiesta — tutto gestito lato server.

### Architettura

```
Browser → Cloudflare Worker (/analyze) → Gemini 3.5 Flash API
              ↓
        File statici (index.html, remaker-test.html)
```

- **Frontend**: HTML/CSS/JS vanilla — zero dipendenze, zero build
- **Backend**: Cloudflare Worker — proxy sicuro verso Gemini, API key nascosta lato server
- **AI**: [Gemini 3.5 Flash](https://deepmind.google/technologies/gemini/) — visione multimodale
- **Deploy**: Cloudflare Workers (CI/CD via GitHub)

### Roadmap

| Fase | Stato | Focus |
|---|---|---|
| Alpha web | ✅ Live | Test con utenti beta |
| Telegram Bot | ✅ Live | @ReMakerAI_bot |
| Integrazione Vinted | ✅ Live | Moda e abbigliamento |
| App mobile | 🔜 | Flutter / React Native |
| Monetizzazione | 🔜 | Freemium, affiliazioni |

### Contatti

Progetto di [Roberto Faccenda](mailto:roberto.faccenda@istitutopantheon.it) — CEO INCAS Film srl

---

## 🇬🇧 English

### What is ReMaker AI

ReMaker AI is a web app that turns unused objects into concrete opportunities in under 30 seconds.

Upload a photo or describe an item you no longer use: the AI identifies it, estimates its market value, generates personalised reuse ideas, and writes a ready-to-post listing.

### Features

- 📷 **Photo or text scan** — upload an image, describe the object, or use both together
- 💰 **Market estimate** — price range based on Italian second-hand marketplaces
- ♻️ **Reuse ideas** — 6 categorised suggestions: Sell, Donate, Transform, Repair
- 📝 **Ready listing** — SEO title, persuasive description and hashtags, copyable in one click
- 👗 **Vinted integration** — for clothing, shoes and accessories: brand, size, colour, material, category and condition pre-filled
- 🔧 **Spare parts & accessories** — specific suggestions on where to find replacement parts
- 🤖 **Telegram Bot** — available at [@ReMakerAI_bot](https://t.me/ReMakerAI_bot)

### How to use

1. Open the app at [remaker-ai.roberto-faccenda.workers.dev/remaker-test](https://remaker-ai.roberto-faccenda.workers.dev/remaker-test)
2. Upload a photo or type a description (or both)
3. Click **Analizza oggetto** (Analyse object)

No API key required — everything is handled server-side.

### Architecture

```
Browser → Cloudflare Worker (/analyze) → Gemini 3.5 Flash API
              ↓
        Static files (index.html, remaker-test.html)
```

- **Frontend**: Vanilla HTML/CSS/JS — zero dependencies, zero build step
- **Backend**: Cloudflare Worker — secure proxy to Gemini, API key hidden server-side
- **AI**: [Gemini 3.5 Flash](https://deepmind.google/technologies/gemini/) — multimodal vision
- **Deploy**: Cloudflare Workers (CI/CD via GitHub)

### Roadmap

| Phase | Status | Focus |
|---|---|---|
| Alpha web | ✅ Live | Beta user testing |
| Telegram Bot | ✅ Live | @ReMakerAI_bot |
| Vinted integration | ✅ Live | Fashion & clothing |
| Mobile app | 🔜 | Flutter / React Native |
| Monetisation | 🔜 | Freemium, affiliate links |

### Contact

Project by [Roberto Faccenda](mailto:roberto.faccenda@istitutopantheon.it) — CEO INCAS Film srl

---

*ReMaker AI — Beta. Powered by Gemini 3.5 Flash · Cloudflare Workers.*

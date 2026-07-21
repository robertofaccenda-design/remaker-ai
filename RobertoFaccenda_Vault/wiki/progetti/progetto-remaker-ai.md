---
tipo: entità
categoria: progetto
stato: attivo
aggiornato: 2026-06-26
---

# ReMaker AI

## Panoramica
App mobile freemium + Telegram Bot che dà una seconda vita agli oggetti inutilizzati tramite AI multimodale (foto → analisi GPT-4o → valore stimato, idee riuso, annuncio pronto, mappa donazioni). Posizionamento v3: **welfare tech / infrastruttura per il benessere collettivo**.

## Dati chiave

| Campo | Valore |
|-------|--------|
| Payoff | "Non buttare. Reinventa." |
| Stato | Bot MVP live. Beta test in avvio. |
| Bot Telegram | @ReMakerAI_bot |
| URL servizio | https://remakerbot.onrender.com |
| Repo GitHub | remakerBOT |
| Deploy | Render free tier (auto-deploy da GitHub) |
| Keepalive | UptimeRobot → https://remakerbot.onrender.com ogni 5 min |
| Stack bot | Python 3.14 · python-telegram-bot 21.6 · AsyncOpenAI · aiohttp |
| Versione codice | v1.4 |
| AI | GPT-4o Vision (OpenAI) |
| TAM | €27 miliardi (mercato usato Italia 2024) |
| ARR target anno 1 | €240.000 (50k utenti, 5% conversione Premium) |
| Metrica go/no-go | Retention 7 giorni > 40% su 20 utenti test |

## Modello di Business

**B2C Freemium:**
- Free: 3 scan/giorno
- Plus €2,99/mese: scan illimitati, export PDF, history
- Pro €7,99/mese: DIY step-by-step, inventario, listing diretto

**B2B:**
- Affiliazioni contestuali (2–5%)
- Transaction fee V2 (2–3%)
- API white-label (assicurazioni, RAEE, e-commerce)
- Licenze flat terzo settore (Caritas, cooperative, comuni)

## Partner Istituzionali Target

Priorità ALTA: Caritas Italiana, Emmaus Italia, Rete Comuni Virtuosi, Fondazione Con il Sud
Priorità MEDIA: Legacoop, Humana PPP, Remida, ANCI, CNA, Zero Waste Italy

## Funding Alternativo

- Bandi EU social innovation (Horizon Europe, EIC Pathfinder)
- MiC / SIAE per componente culturale economia circolare
- Fondazioni bancarie (Cariplo, Con il Sud)
- Impact investing (B Corp, Fondazione Italiana Accenture)

## Roadmap

| Fase | Durata | Focus | Stato |
|------|--------|-------|-------|
| Alpha | Mese 1-2 | Telegram Bot MVP | ✅ Live |
| Beta Pubblica | Mese 3-4 | App mobile MVP | 🔄 Prossimo |
| Monetizzazione | Mese 5-6 | Premium, affiliazioni, B2B | ⏳ |
| Funding & Partnership | Mese 6-9 | Bandi EU, partner istituzionali | ⏳ |
| Scale EU | Anno 2 | Multi-paese, API white-label | ⏳ |

## Cronologia

- **Giugno 2026 (early):** Pitch v2.0, prototipo web HTML su Netlify con Gemini API
- **Giugno 2026 (mid):** Feedback tester → pivot narrativo welfare-tech → Pitch v3.0
- **Giugno 2026 (26):** Telegram Bot MVP live su Render. Debug quota OpenAI. Bot funzionante.

## Documenti

- `remaker_ai_v3_pitch_produzione.md` — pitch completo v3.0
- `remaker_partner_istituzionali.docx` — 10 schede partner + email template
- `remaker-bot/main.py` — codice bot v1.4
- Pitch deck Gamma: generato da pitch v3.0
- One-pager Gamma: per beta tester

## Note Tecniche Critiche

- **OpenAI credits:** ricaricare su platform.openai.com/settings/billing — senza crediti il bot ritorna errore 429
- **Polling silenzioso:** dopo errori 429, il polling Telegram si può bloccare senza crash visibile → fix: Manual Deploy su Render
- **Non committare .env:** il token Telegram è nei log Render — non condividere log pubblicamente
- **openai>=1.58.0:** versione minima richiesta (1.51.0 incompatibile con httpx su Python 3.14)

## Note aperte

- Avviare beta test formale con 20 utenti, raccogliere metriche retention
- Valutare primo contatto partner istituzionali (priorità: Caritas, Emmaus)
- Esplorare bandi EU social innovation per funding

## Fonti

- [[sessione-2026-06-26-remaker-bot]] — sessione di sviluppo e deploy bot

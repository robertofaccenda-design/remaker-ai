---
tipo: fonte
dominio: progetti
data_ingest: 2026-06-26
source: sessione Claude — sviluppo e deploy Telegram Bot ReMaker AI
tags: [remaker-ai, telegram-bot, deploy, render, openai, debug]
---

# Sessione 2026-06-26 — Deploy e Debug Telegram Bot ReMaker AI

## Sintesi
Sessione di sviluppo completo del Telegram Bot MVP di ReMaker AI: dal codice al deploy live su Render, incluso il debug di tre errori critici (event loop Python 3.14, versione OpenAI incompatibile, quota esaurita) e la configurazione keepalive con UptimeRobot. Bot ora funzionante.

## Azioni completate

1. **Pitch v3.0 aggiornato** con frame welfare-tech / infrastruttura per il benessere collettivo, basato su feedback di un tester
2. **Pitch deck Gamma** generato (14 slide) da pitch v3.0
3. **Lista partner istituzionali** — DOCX con 10 schede (Caritas, Emmaus, Legacoop, ecc.) + email template
4. **One-pager Gamma** per beta tester
5. **Telegram Bot MVP** sviluppato e deployato su Render free tier
6. **Debug e fix** di tre errori critici (vedi sotto)
7. **UptimeRobot** configurato per keepalive ogni 5 minuti

## Decisioni chiave

| Decisione | Motivazione |
|-----------|-------------|
| Polling mode (non webhook) | Più semplice su Render free tier, nessuna configurazione webhook |
| AsyncOpenAI (non sync + executor) | Più stabile in contesto async Python 3.14 |
| aiohttp per health endpoint | Coesiste con il bot sullo stesso event loop |
| asyncio.run(main()) come entry point | Unico modo corretto con Python 3.14 (no get_event_loop deprecato) |
| Render free tier | Railway è a pagamento; Render ha piano free con auto-deploy da GitHub |
| UptimeRobot su URL root (non /health) | /health dava "down" su UptimeRobot; / funziona ugualmente |

## Bug risolti

### 1. RuntimeError: no current event loop (Python 3.14)
- **Causa:** Threading HTTPServer + asyncio incompatibili in Python 3.14
- **Fix:** Riscrittura completa architettura async: `asyncio.run(main())`, aiohttp per health, bot in polling

### 2. TypeError: unexpected keyword argument 'proxies'
- **Causa:** `openai==1.51.0` incompatibile con `httpx==0.28.1` installato automaticamente su Python 3.14
- **Fix:** `requirements.txt` → `openai>=1.58.0`

### 3. Error 429 insufficient_quota
- **Causa:** Account OpenAI senza crediti attivi
- **Diagnosi:** Trovata nei log Render: `openai.RateLimitError: insufficient_quota`
- **Fix:** Ricaricare crediti su platform.openai.com/settings/billing
- **Effetto collaterale:** Dopo 429, il polling Telegram si blocca silenziosamente → fix: Manual Deploy Render

### 4. git index.lock / unrelated histories / secret detected
- Vari problemi Git risolti con comandi manuali da Terminal
- File `remaker-test.html` eliminato da GitHub perché conteneva una GCP API Key a riga 1552

## Stack tecnico finale

```
python-telegram-bot==21.6
openai>=1.58.0
python-dotenv==1.0.1
aiohttp==3.10.5
```

## File creati/modificati

| File | Percorso | Note |
|------|----------|------|
| main.py v1.4 | remakerBOT/main.py | Bot completo con AsyncOpenAI, /test command, traceback logging |
| requirements.txt | remakerBOT/requirements.txt | openai>=1.58.0 fondamentale |
| .env.example | remakerBOT/.env.example | Template variabili d'ambiente |
| .gitignore | remaker/.gitignore | Esclude .env, __pycache__, .docx |
| pitch v3.0 | remaker/remaker_ai_v3_pitch_produzione.md | Welfare-tech frame |
| partner DOCX | remaker/remaker_partner_istituzionali.docx | 10 partner + email template |

## Variabili d'ambiente Render

| Chiave | Note |
|--------|------|
| OPENAI_API_KEY | Service account OpenAI — verificare crediti periodicamente |
| TELEGRAM_BOT_TOKEN | Da @BotFather — non esporre nei log pubblici |

## Stato bot al termine della sessione

- ✅ `/start` funziona
- ✅ Foto → analisi GPT-4o → risposta strutturata
- ✅ Testo → analisi → risposta
- ✅ `/test` → diagnosi OpenAI in tempo reale
- ✅ Health endpoint su https://remakerbot.onrender.com
- ✅ UptimeRobot keepalive attivo

## Connessioni

- [[progetto-remaker-ai]] — entità principale del progetto

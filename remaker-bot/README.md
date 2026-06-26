# ReMaker AI — Telegram Bot MVP

Bot Telegram che analizza foto di oggetti inutilizzati e restituisce: valore stimato, 5 idee di riuso, annuncio pronto, consigli RAEE.

**Stack:** Python 3.11 · python-telegram-bot v21 · GPT-4o Vision · Deploy: Render (gratuito)

---

## Setup completo — 4 passi

---

### Passo 1 — Crea il bot su Telegram (5 minuti)

1. Apri Telegram → cerca **@BotFather**
2. Scrivi `/newbot`
3. Nome del bot: `ReMaker AI`
4. Username: `ReMakerAI_bot` (deve finire in `_bot`)
5. BotFather ti manda un **token** tipo `123456789:ABC-xyz...` → copialo

---

### Passo 2 — Metti il codice su GitHub (3 minuti)

1. Vai su [github.com](https://github.com) → crea account gratuito se non l'hai
2. Clicca **New repository** → nome: `remaker-bot` → **Private** → Create
3. Carica tutti i file di questa cartella nel repository
   (trascina i file nella pagina GitHub, oppure usa GitHub Desktop)
4. **Non caricare il file `.env`** — contiene le tue chiavi segrete

---

### Passo 3 — Deploy su Render (gratuito, 5 minuti)

1. Vai su [render.com](https://render.com) → crea account (login con GitHub)
2. Clicca **New → Web Service**
3. Collega il repository `remaker-bot`
4. Configura il servizio:
   - **Name:** `remaker-bot`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Instance Type:** Free
5. Clicca **Advanced → Add Environment Variable** e aggiungi:

   | Chiave | Valore |
   |---|---|
   | `OPENAI_API_KEY` | la tua chiave OpenAI |
   | `TELEGRAM_BOT_TOKEN` | il token di BotFather |
   | `WEBHOOK_URL` | `https://remaker-bot.onrender.com` *(vedi nota)* |

   > **Nota WEBHOOK_URL:** Render ti assegna un URL quando crei il servizio (tipo `https://remaker-bot.onrender.com`). Puoi vederlo in alto nella pagina del servizio. Copialo qui **senza** lo slash finale.

6. Clicca **Create Web Service** → Render fa il deploy automatico

---

### Passo 4 — Impedisci al bot di "dormire" (2 minuti)

Render free tier spegne il servizio dopo 15 min senza richieste HTTP.
Per tenerlo sempre attivo, usa **UptimeRobot** (gratuito):

1. Vai su [uptimerobot.com](https://uptimerobot.com) → crea account gratuito
2. Clicca **Add New Monitor**
3. Tipo: **HTTP(s)**
4. URL: `https://remaker-bot.onrender.com/health`
5. Intervallo: **5 minuti**
6. Salva

Il bot rimane sempre attivo e risponde senza delay.

---

## Test in locale (prima del deploy, opzionale)

```bash
# Nella cartella remaker-bot/
pip install -r requirements.txt
cp .env.example .env
# Modifica .env: aggiungi OPENAI_API_KEY e TELEGRAM_BOT_TOKEN
# Lascia WEBHOOK_URL vuoto per usare il polling locale
python main.py
```

---

## Variabili d'ambiente

| Variabile | Obbligatoria | Descrizione |
|---|---|---|
| `OPENAI_API_KEY` | ✅ | Chiave API OpenAI (da platform.openai.com) |
| `TELEGRAM_BOT_TOKEN` | ✅ | Token del bot (da @BotFather) |
| `WEBHOOK_URL` | Solo su Render | URL pubblico del servizio (es. `https://remaker-bot.onrender.com`) |

---

## Comandi del bot

| Comando | Funzione |
|---|---|
| `/start` | Messaggio di benvenuto |
| `/help` | Istruzioni d'uso |
| [foto] | Analisi oggetto tramite immagine |
| [testo] | Analisi oggetto tramite descrizione testuale |

---

## Metriche go/no-go

Testa con **20 utenti** nei primi 7 giorni.

**Metrica chiave:** retention a 7 giorni > 40%
(= almeno 8 utenti su 20 tornano a mandare una seconda foto)

Dati da raccogliere:
- Numero di scan totali
- Tasso di ritorno
- Feedback qualitativo: identificazione corretta? Valore realistico? Annuncio pubblicabile?

---

*ReMaker AI — Non buttare. Reinventa.*

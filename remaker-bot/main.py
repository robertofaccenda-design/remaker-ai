"""
ReMaker AI — Telegram Bot MVP
Versione: 1.1
Autore: Roberto Faccenda

Flusso:
  1. Utente manda foto (o testo) di un oggetto
  2. GPT-4o Vision identifica l'oggetto
  3. Bot risponde con: valore stimato, 5 idee di riuso, annuncio pronto, consigli RAEE
  4. Tempo medio di risposta: < 15 secondi

Deploy:
  - Locale: usa polling (WEBHOOK_URL non impostato)
  - Render/cloud: usa webhook (imposta WEBHOOK_URL nelle variabili d'ambiente)
"""

import os
import logging
import base64
from io import BytesIO

from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)
from telegram.constants import ParseMode, ChatAction

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

load_dotenv()

# URL pubblico del servizio su Render (es. https://remaker-bot.onrender.com)
# Se non impostato, il bot usa il polling (modalità locale)
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")
PORT = int(os.environ.get("PORT", 8443))


# ── Health check server (per UptimeRobot) ─────────────────────────────────────
# Risponde a GET /health con 200 OK — mantiene Render sveglio

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Silenzia i log HTTP per non sporcare l'output


def avvia_health_server(porta: int = 8080):
    server = HTTPServer(("0.0.0.0", porta), HealthHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    logger.info(f"Health check server attivo su porta {porta} → GET /health")

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ── Clients ───────────────────────────────────────────────────────────────────
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

# ── Prompt di sistema ─────────────────────────────────────────────────────────
SYSTEM_PROMPT = """Sei ReMaker AI, un assistente italiano esperto nel dare una seconda vita agli oggetti inutilizzati.

Quando ricevi una foto (o una descrizione testuale) di un oggetto, rispondi SEMPRE con questo formato esatto, in italiano:

🔍 *Oggetto identificato:*
[Descrizione precisa: marca, modello, anno stimato, condizioni visibili]

💰 *Valore stimato sul mercato usato italiano:*
€[min] – €[max]
_(Prezzi di riferimento: eBay.it, Subito, Wallapop)_

♻️ *5 idee di riuso:*
1. [Idea concreta e realizzabile]
2. [Idea concreta e realizzabile]
3. [Idea concreta e realizzabile]
4. [Idea concreta e realizzabile]
5. [Idea concreta e realizzabile]

📢 *Annuncio pronto da pubblicare:*
_"[Titolo SEO ottimizzato, max 60 caratteri]_
[Descrizione di 3-4 righe: stato, caratteristiche, uso ideale, prezzo consigliato. Tono professionale ma umano.]"_

🗺️ *Dona o smaltisci correttamente:*
[Consiglio specifico per quell'oggetto: dove donarlo (Caritas, scuole, biblioteche, ecc.) o come smaltirlo (RAEE, isola ecologica, ecc.)]

---
_ReMaker AI — Non buttare. Reinventa._

REGOLE:
- Sii sempre preciso sul valore: dai un range realistico basato sul mercato italiano 2024-2025
- Le idee di riuso devono essere pratiche e ordinate dalla più facile alla più creativa
- L'annuncio deve essere pronto da incollare su Subito o eBay senza modifiche
- Se l'oggetto non è identificabile dalla foto, chiedi educatamente più dettagli
- Usa sempre il Markdown di Telegram (*grassetto*, _corsivo_)
"""

# ── Helper: analisi oggetto ───────────────────────────────────────────────────

async def analizza_oggetto(testo: str = None, immagine_bytes: bytes = None) -> str:
    """Chiama GPT-4o con testo e/o immagine e restituisce la risposta formattata."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if immagine_bytes:
        # Encode immagine in base64
        b64_image = base64.b64encode(immagine_bytes).decode("utf-8")
        content = [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{b64_image}",
                    "detail": "high",
                },
            }
        ]
        if testo:
            content.append({"type": "text", "text": testo})
        else:
            content.append({"type": "text", "text": "Analizza questo oggetto."})
        messages.append({"role": "user", "content": content})
    else:
        messages.append({"role": "user", "content": testo or "Analizza questo oggetto."})

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
        temperature=0.4,
    )
    return response.choices[0].message.content


# ── Handler: /start ───────────────────────────────────────────────────────────

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    testo = (
        "👋 Benvenuto su *ReMaker AI*\\!\n\n"
        "Mandami una *foto* di un oggetto che non usi più\\.\n"
        "In pochi secondi ti dico:\n\n"
        "🔍 Cosa è e quanto vale\n"
        "♻️ 5 idee per riusarlo\n"
        "📢 Un annuncio pronto da pubblicare\n"
        "🗺️ Dove donarlo o smaltirlo\n\n"
        "_Non buttare\\. Reinventa\\._"
    )
    keyboard = [[InlineKeyboardButton("ℹ️ Come funziona", callback_data="help")]]
    await update.message.reply_text(
        testo,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ── Handler: /help ────────────────────────────────────────────────────────────

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    testo = (
        "*Come usare ReMaker AI:*\n\n"
        "1\\. Scatta una foto di un oggetto che non usi più\n"
        "2\\. Mandala qui in chat\n"
        "3\\. Aspetta circa 10\\-15 secondi\n"
        "4\\. Ricevi: valore stimato, idee di riuso, annuncio pronto\n\n"
        "*Funziona con:*\n"
        "📱 Smartphone e tablet\n"
        "🖥️ Elettrodomestici\n"
        "🪑 Mobili e arredamento\n"
        "👗 Abbigliamento\n"
        "🎸 Strumenti musicali\n"
        "📚 Libri, giochi, sport\n\n"
        "Puoi anche scrivere una *descrizione testuale* se non hai la foto\\.\n\n"
        "Contatto: roberto\\.faccenda@istitutopantheon\\.it"
    )
    await update.message.reply_text(testo, parse_mode=ParseMode.MARKDOWN_V2)


# ── Handler: callback bottoni ─────────────────────────────────────────────────

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == "help":
        await cmd_help(update, context)


# ── Handler: foto ─────────────────────────────────────────────────────────────

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.chat.send_action(ChatAction.TYPING)

    # Scarica la foto in alta risoluzione
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    buf = BytesIO()
    await file.download_to_memory(buf)
    image_bytes = buf.getvalue()

    caption = update.message.caption or None

    msg = await update.message.reply_text(
        "⏳ Sto analizzando l'oggetto... (~10 secondi)"
    )

    try:
        risposta = await analizza_oggetto(testo=caption, immagine_bytes=image_bytes)
        await msg.delete()
        keyboard = [
            [InlineKeyboardButton("📸 Analizza un altro oggetto", callback_data="altro")]
        ]
        await update.message.reply_text(
            risposta,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        logger.info(f"Analisi completata per utente {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Errore analisi: {e}")
        await msg.edit_text(
            "❌ Si è verificato un errore. Prova a inviare di nuovo la foto, "
            "oppure scrivimi una descrizione testuale dell'oggetto."
        )


# ── Handler: testo ────────────────────────────────────────────────────────────

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    testo = update.message.text.strip()

    # Ignora comandi non riconosciuti
    if testo.startswith("/"):
        await update.message.reply_text(
            "Comando non riconosciuto. Usa /help per vedere come funziona."
        )
        return

    await update.message.chat.send_action(ChatAction.TYPING)
    msg = await update.message.reply_text("⏳ Sto analizzando l'oggetto...")

    try:
        risposta = await analizza_oggetto(testo=testo)
        await msg.delete()
        keyboard = [
            [InlineKeyboardButton("📸 Analizza un altro oggetto", callback_data="altro")]
        ]
        await update.message.reply_text(
            risposta,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
    except Exception as e:
        logger.error(f"Errore analisi testo: {e}")
        await msg.edit_text(
            "❌ Si è verificato un errore. Riprova tra qualche secondo."
        )


# ── Handler: callback "altro" ─────────────────────────────────────────────────

async def callback_altro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "📸 Manda la foto del prossimo oggetto, oppure descrivimelo con parole!"
    )


# ── Avvio applicazione ────────────────────────────────────────────────────────

def main() -> None:
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Comandi
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))

    # Foto
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Testo libero
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Callback bottoni
    app.add_handler(CallbackQueryHandler(callback_altro, pattern="^altro$"))
    app.add_handler(CallbackQueryHandler(callback_handler))

    # Avvia health check server in background (solo in produzione)
    if WEBHOOK_URL:
        avvia_health_server(porta=8080)

    if WEBHOOK_URL:
        # ── Modalità WEBHOOK (Render / cloud) ────────────────────────────────
        # Render assegna la porta tramite la variabile PORT
        webhook_path = f"/webhook/{TELEGRAM_TOKEN}"
        full_url = f"{WEBHOOK_URL}{webhook_path}"
        logger.info(f"ReMaker AI Bot avviato in modalità WEBHOOK → {full_url}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=webhook_path,
            webhook_url=full_url,
            allowed_updates=Update.ALL_TYPES,
        )
    else:
        # ── Modalità POLLING (locale / sviluppo) ─────────────────────────────
        logger.info("ReMaker AI Bot avviato in modalità POLLING (locale)...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

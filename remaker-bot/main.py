"""
ReMaker AI — Telegram Bot MVP
Versione: 1.3
Autore: Roberto Faccenda

Flusso:
  1. Utente manda foto (o testo) di un oggetto
  2. GPT-4o Vision identifica l'oggetto
  3. Bot risponde con: valore stimato, 5 idee di riuso, annuncio pronto, consigli RAEE
  4. Tempo medio di risposta: < 15 secondi

Deploy:
  - Locale e Render: usa polling + health server aiohttp sullo stesso event loop
"""

import os
import asyncio
import logging
import base64
import traceback
from io import BytesIO

from aiohttp import web as aiohttp_web
from dotenv import load_dotenv
from openai import AsyncOpenAI
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

load_dotenv()

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ── Config ────────────────────────────────────────────────────────────────────
openai_client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
PORT = int(os.environ.get("PORT", 8080))

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
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if immagine_bytes:
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
        content.append({"type": "text", "text": testo or "Analizza questo oggetto."})
        messages.append({"role": "user", "content": content})
    else:
        messages.append({"role": "user", "content": testo or "Analizza questo oggetto."})

    response = await openai_client.chat.completions.create(
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

    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    buf = BytesIO()
    await file.download_to_memory(buf)
    image_bytes = buf.getvalue()
    caption = update.message.caption or None

    msg = await update.message.reply_text("⏳ Sto analizzando l'oggetto... (~10 secondi)")

    try:
        risposta = await analizza_oggetto(testo=caption, immagine_bytes=image_bytes)
        await msg.delete()
        keyboard = [[InlineKeyboardButton("📸 Analizza un altro oggetto", callback_data="altro")]]
        await update.message.reply_text(
            risposta,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        logger.info(f"Analisi completata per utente {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Errore analisi foto: {e}\n{traceback.format_exc()}")
        await msg.edit_text(
            "❌ Si è verificato un errore. Prova a inviare di nuovo la foto, "
            "oppure scrivimi una descrizione testuale dell'oggetto."
        )


# ── Handler: testo ────────────────────────────────────────────────────────────

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    testo = update.message.text.strip()

    if testo.startswith("/"):
        await update.message.reply_text("Comando non riconosciuto. Usa /help per vedere come funziona.")
        return

    await update.message.chat.send_action(ChatAction.TYPING)
    msg = await update.message.reply_text("⏳ Sto analizzando l'oggetto...")

    try:
        risposta = await analizza_oggetto(testo=testo)
        await msg.delete()
        keyboard = [[InlineKeyboardButton("📸 Analizza un altro oggetto", callback_data="altro")]]
        await update.message.reply_text(
            risposta,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
    except Exception as e:
        logger.error(f"Errore analisi testo: {e}\n{traceback.format_exc()}")
        await msg.edit_text("❌ Si è verificato un errore. Riprova tra qualche secondo.")


# ── Handler: callback "altro" ─────────────────────────────────────────────────

async def callback_altro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("📸 Manda la foto del prossimo oggetto, oppure descrivimelo con parole!")


# ── Health check server (aiohttp, per UptimeRobot) ───────────────────────────

async def health(request):
    return aiohttp_web.Response(text="OK")

async def avvia_health_server():
    app = aiohttp_web.Application()
    app.router.add_get("/health", health)
    app.router.add_get("/", health)
    runner = aiohttp_web.AppRunner(app)
    await runner.setup()
    site = aiohttp_web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    logger.info(f"Health server attivo su porta {PORT} → GET /health")


# ── Avvio applicazione ────────────────────────────────────────────────────────

async def main():
    # Health server (mantiene Render sveglio)
    await avvia_health_server()

    # Bot Telegram in polling
    bot = Application.builder().token(TELEGRAM_TOKEN).build()

    bot.add_handler(CommandHandler("start", cmd_start))
    bot.add_handler(CommandHandler("help", cmd_help))
    bot.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    bot.add_handler(CallbackQueryHandler(callback_altro, pattern="^altro$"))
    bot.add_handler(CallbackQueryHandler(callback_handler))

    logger.info("ReMaker AI Bot avviato in modalità POLLING...")

    async with bot:
        await bot.start()
        await bot.updater.start_polling(allowed_updates=Update.ALL_TYPES)
        # Gira per sempre finché non viene interrotto
        await asyncio.Event().wait()
        await bot.updater.stop()
        await bot.stop()


if __name__ == "__main__":
    asyncio.run(main())

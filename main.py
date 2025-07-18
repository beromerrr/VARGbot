import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from flask import Flask, request

TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL")
PORT = int(os.environ.get("PORT", 10000))

app = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Бот жив и работает!")

bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = bot_app.bot._extract_update(request.get_json(force=True))
    bot_app.create_task(bot_app.process_update(update))
    return "ok"

@app.route("/", methods=["GET"])
def root():
    return "Бот работает!"

if __name__ == "__main__":
    bot_app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{APP_URL}/{TOKEN}"
    )

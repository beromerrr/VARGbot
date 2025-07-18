import os
import random
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Логирование
logging.basicConfig(level=logging.INFO)

# Получаем токен и URL из переменных окружения
TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL")
PORT = int(os.environ.get("PORT", 10000))

# Пути к видео (обрати внимание на расширения и регистр)
videos = [
    "videos/ВАРГ.mp4",
    "videos/ВАРГ2.mp4",
    "videos/ВАРГ3.mp4",
    "videos/ВАРГ4.mp4"
]

# Flask приложение
app = Flask(__name__)

# Телеграм-приложение
telegram_app = ApplicationBuilder().token(TOKEN).build()

# Обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Получено сообщение: {update.message.text}")
    if update.message and 'варг' in update.message.text.lower():
        video_path = random.choice(videos)
        logging.info(f"Выбрано видео: {video_path}")
        try:
            with open(video_path, 'rb') as video_file:
                await context.bot.send_video(
                    chat_id=update.effective_chat.id,
                    video=video_file,
                    reply_to_message_id=update.message.message_id
                )
            logging.info("Видео отправлено")
        except Exception as e:
            logging.error(f"Ошибка при отправке видео: {e}")

# Добавляем обработчик в приложение
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Вебхук от Telegram — принимает POST запросы
@app.route(f"/{TOKEN}", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        update = telegram_app.bot._extract_update(request.get_json(force=True))
        telegram_app.create_task(telegram_app.process_update(update))
    return "ok"

# Проверка что бот живой — GET запрос на корень
@app.route("/", methods=["GET"])
def root():
    return "Bot is alive!"

# Запуск вебхука
if __name__ == "__main__":
    telegram_app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{APP_URL}/{TOKEN}"
    )

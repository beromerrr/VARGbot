import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from flask import Flask, request

# Получаем токен и адрес сайта из переменных окружения
TOKEN = os.environ.get("8198057099:AAEhMiejp6XQj0s5NnEiPXoy2HQp3deYM_w")
APP_URL = os.environ.get("https://vargbot.onrender.com")

# Список видео (пути к файлам)
videos = [
    "videos/ВАРГ.mp4",
    "videos/ВАРГ2.mp4",
    "videos/ВАРГ3.mp4",
    "videos/ВАРГ4.mp4"
]

# Запускаем Flask-приложение и Telegram бота
app = Flask(__name__)
telegram_app = ApplicationBuilder().token(TOKEN).build()

# Обработка входящих сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and 'варг' in update.message.text.lower():
        video_path = random.choice(videos)
        with open(video_path, 'rb') as video_file:
            await context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video_file,
                reply_to_message_id=update.message.message_id  # отправка в ответ
            )

# Подключаем обработчик сообщений
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Вебхук: бот принимает обновления с Telegram через POST
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram_app.bot._extract_update(request.get_json(force=True))
    telegram_app.create_task(telegram_app.process_update(update))
    return "ok"

# Корень сайта — проверка, жив ли бот
@app.route("/", methods=["GET"])
def root():
    return "Bot is alive!"

# Запуск вебхука
if __name__ == "__main__":
    telegram_app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url=f"{APP_URL}/{TOKEN}"
    )

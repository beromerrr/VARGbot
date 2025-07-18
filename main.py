import os
import random
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

videos = [
    "videos/ВАРГ.mp4",
    "videos/ВАРГ2.mp4",
    "videos/ВАРГ3.mp4",
    "videos/ВАРГ4.mp4"
]

# Flask сервер для UptimeRobot
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Bot is alive!"

# Бот
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and 'варг' in update.message.text.lower():
        video_path = random.choice(videos)
        with open(video_path, 'rb') as video_file:
            await context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video_file,
                reply_to_message_id=update.message.message_id
            )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен через polling...")
    await app.run_polling()

if __name__ == '__main__':
    # Запускаем Flask в отдельном потоке
    import threading
    threading.Thread(target=lambda: flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))).start()

    # Запускаем asyncio-бота в главном потоке
    asyncio.run(main())

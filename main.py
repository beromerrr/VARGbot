import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL")

videos = [
    "videos/ВАРГ.mp4",
    "videos/ВАРГ2.mp4",
    "videos/ВАРГ3.mp4",
    "videos/ВАРГ4.mp4"
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and 'варг' in update.message.text.lower():
        video_path = random.choice(videos)
        with open(video_path, 'rb') as video_file:
            await context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video_file,
                reply_to_message_id=update.message.message_id
            )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == '__main__':
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url=f"{APP_URL}/{TOKEN}"
    )

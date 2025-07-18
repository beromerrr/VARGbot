from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import random

TOKEN = "8198057099:AAEhMiejp6XQj0s5NnEiPXoy2HQp3deYM_w"

trigger_word = "Варг"  # слово, на которое бот реагирует

video_files = [
    "videos/ВАРГ1.mp4",
    "videos/ВАРГ2.mp4",
    "videos/ВАРГ3.mp4",
    "videos/ВАРГ4.mp4"
]

async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if trigger_word.lower() in text:
        video_path = random.choice(video_files)
        await context.bot.send_video(chat_id=update.effective_chat.id, video=open(video_path, "rb"))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), send_video))
    print("Бот запущен...")
    app.run_polling()

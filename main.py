import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7936838791:AAGIjstY4TbmIu4SbTsAW_DCSehfXmEolyc"

trigger_word = "Варг"

video_files = ["videos/video1.mp4", "videos/video2.mp4"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if trigger_word in text:
        video = random.choice(video_files)
        await context.bot.send_video(chat_id=update.effective_chat.id, video=open(video, 'rb'))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()

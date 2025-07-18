import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

videos = [
    "videos/VARG.mp4",
    "videos/VARG2.mp4",
    "videos/VARG3.mp4",
    "videos/VARG4.mp4"
]

TRIGGER_WORD = "варг"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if TRIGGER_WORD in text:
        video_path = random.choice(videos)
        with open(video_path, 'rb') as video_file:
            await context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video_file,
                reply_to_message_id=update.message.message_id
            )

def main():
    TOKEN = "8198057099:AAEhMiejp6XQj0s5NnEiPXoy2HQp3deYM_w"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен")
    app.run_polling()

if __name__ == '__main__':
    main()

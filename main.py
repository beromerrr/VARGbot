import random
from telegram.ext import Updater, MessageHandler, Filters

videos = [
    "videos/VARG1.mp4",
    "videos/VARG2.mp4",
    "videos/VARG3.mp4",
    "videos/VARG4.mp4"
]

TRIGGER_WORD = "Варг"

def handle_message(update, context):
    text = update.message.text.lower()
    if TRIGGER_WORD in text:
        video_path = random.choice(videos)
        with open(video_path, 'rb') as video_file:
            context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video_file,
                reply_to_message_id=update.message.message_id
            )

def main():
    TOKEN = "8198057099:AAEhMiejp6XQj0s5NnEiPXoy2HQp3deYM_w"
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Бот запущен")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

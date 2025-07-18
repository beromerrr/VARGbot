import os

print("Текущая рабочая директория:", os.getcwd())
print("Содержимое текущей папки:", os.listdir())
try:
    print("Содержимое папки videos:", os.listdir('videos'))
except Exception as e:
    print("Ошибка при чтении папки videos:", e)

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "Bot is alive!"

@app.route(f"/{os.environ.get('BOT_TOKEN')}", methods=["POST"])
def webhook():
    print("Webhook received!")
    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

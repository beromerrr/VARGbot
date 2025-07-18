import os
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

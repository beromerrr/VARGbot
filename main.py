from flask import Flask, request

app = Flask(__name__)

@app.route(f"/{os.environ.get('BOT_TOKEN')}", methods=["POST"])
def webhook():
    print("Webhook received!")
    return "OK"

@app.route("/", methods=["GET"])
def root():
    return "Bot is alive!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

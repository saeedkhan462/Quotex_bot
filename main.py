import os
import threading
import time
from flask import Flask
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")

app = Flask(__name__)

@app.route('/')
def home():
    return "Quotex Major Pairs Bot is LIVE on Render!"

@app.route('/health')
def health():
    return "OK", 200

def send_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        return
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": text})
    except:
        pass

def bot_loop():
    send_telegram("✅ Bot Started on Render!")
    while True:
        print("Checking Major Pairs: EURUSD, GBPUSD, USDJPY...")
        # Yahan aapka Quotex ka signal logic ayega
        time.sleep(60)

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    threading.Thread(target=run_web, daemon=True).start()
    bot_loop()

import os
import time
import requests
import pandas as pd
from telegram import Bot

# === Настройки ===
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

TICKERS = ["NVOS", "GMBL", "SNTG", "HUBC", "CYN"]
VOLUME_MIN = 200_000
PERCENT_CHANGE = 5
PRICE_MIN = 2
PRICE_MAX = 40

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def get_data(ticker):
    now = int(time.time())
    past = now - 600
    url = "https://finnhub.io/api/v1/stock/candle"
    params = {
        "symbol": ticker,
        "resolution": "1",
        "from": past,
        "to": now,
        "token": FINNHUB_API_KEY
    }
    r = requests.get(url, params=params).json()
    if r.get("s") != "ok":
        return None
    df = pd.DataFrame({"t": r["t"], "c": r["c"], "v": r["v"]})
    return df

def check_ticker(ticker):
    df = get_data(ticker)
    if df is None or len(df) < 2:
        return
    start, end = df["c"].iloc[0], df["c"].iloc[-1]
    change = ((end - start) / start) * 100
    if change < PERCENT_CHANGE:
        return
    volume = df["v"].sum()
    if volume < VOLUME_MIN:
        return
    msg = f"📈 {ticker} вырос на {change:.2f}% за 10 минут"
Цена: ${end:.2f}, Объём: {int(volume):,}"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)

if __name__ == "__main__":
    while True:
        for ticker in TICKERS:
            try:
                check_ticker(ticker)
            except Exception as e:
                print(f"Ошибка: {e}")
        time.sleep(120)

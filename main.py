from trading_engine.data_fetcher.data_loader import DataLoader
from trading_engine.indicators.indicators import Indicators
from trading_engine.signal_engine.signal_generator import SignalGenerator
from trading_engine.charting.chart_generator import ChartGenerator
from trading_engine.telegram_bot.bot import TelegramBot
from dotenv import load_dotenv
import os
import time

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

TIMEFRAME = "M15"

if __name__ == "__main__":
    loader = DataLoader()
    generator = SignalGenerator(min_score=4)
    chart = ChartGenerator()
    bot = TelegramBot(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)

    # Initial load
    df = loader.load_candles("EURUSD", TIMEFRAME, 500)
    last_time = df["time"].iloc[-1]  # letzte Kerze merken

    while True:
        print("🔄 Prüfe auf neue Kerzen...")

        df_new = loader.load_candles("EURUSD", TIMEFRAME, 500)
        new_time = df_new["time"].iloc[-1]

        if new_time != last_time:
            print("🟢 Neue Kerze erkannt — aktualisiere Chart!")

            last_time = new_time
            df = Indicators.add_all(df_new)
            signals = generator.generate(df)

            chart.plot(df, signals)
            bot.send_photo("chart_EURUSD M15 Chart.png")

            print("✔ Chart aktualisiert.\n")
        else:
            print("⚪ Keine neue Kerze — warte 30 Sekunden.\n")

        time.sleep(30)

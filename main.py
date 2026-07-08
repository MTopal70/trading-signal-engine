from trading_engine.data_fetcher.data_loader import DataLoader
from trading_engine.indicators.indicators import Indicators
from trading_engine.signal_engine.signal_generator import SignalGenerator

if __name__ == "__main__":
    loader = DataLoader()
    df = loader.load_candles("EURUSD", "M15", 500)

    df = Indicators.add_all(df)

    generator = SignalGenerator(min_score=4)
    signals = generator.generate(df)

    print("Gefundene Signale:")
    for s in signals[-10:]:  # letzte 10 Signale
        print(s)

    print("Letzten 10 Kerzen:")
    print(df.tail(10)) # letzte 10 Signale



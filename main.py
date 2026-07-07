from trading_engine.data_fetcher.data_loader import DataLoader
from trading_engine.indicators.indicators import Indicators

if __name__ == "__main__":
    loader = DataLoader()
    df = loader.load_candles("EURUSD", "M15", 200)

    df = Indicators.add_all(df)
    print(df.tail())


from trading_engine.data_fetcher.data_loader import DataLoader

if __name__ == "__main__":
    loader = DataLoader()
    df = loader.load_candles("EURUSD", "M15", 200)
    print(df.head())

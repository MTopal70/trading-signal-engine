import pandas as pd
import ta


class Indicators:
    """
    Berechnet alle relevanten technischen Indikatoren für die Signal-Engine.
    """

    @staticmethod
    def add_bollinger(df: pd.DataFrame) -> pd.DataFrame:
        bb = ta.volatility.BollingerBands(close=df["close"], window=20, window_dev=2)
        df["bb_high"] = bb.bollinger_hband()
        df["bb_low"] = bb.bollinger_lband()
        df["bb_mid"] = bb.bollinger_mavg()
        return df

    @staticmethod
    def add_macd(df: pd.DataFrame) -> pd.DataFrame:
        macd = ta.trend.MACD(close=df["close"])
        df["macd"] = macd.macd()
        df["macd_signal"] = macd.macd_signal()
        df["macd_hist"] = macd.macd_diff()
        return df

    @staticmethod
    def add_rsi(df: pd.DataFrame) -> pd.DataFrame:
        df["rsi"] = ta.momentum.RSIIndicator(close=df["close"]).rsi()
        return df

    @staticmethod
    def add_ema(df: pd.DataFrame) -> pd.DataFrame:
        df["ema9"] = ta.trend.EMAIndicator(close=df["close"], window=9).ema_indicator()
        df["ema21"] = ta.trend.EMAIndicator(close=df["close"], window=21).ema_indicator()
        return df

    @staticmethod
    def add_atr(df: pd.DataFrame) -> pd.DataFrame:
        atr = ta.volatility.AverageTrueRange(
            high=df["high"], low=df["low"], close=df["close"], window=14
        )
        df["atr"] = atr.average_true_range()
        return df

    @staticmethod
    def add_volume_spike(df: pd.DataFrame) -> pd.DataFrame:
        df["vol_avg20"] = df["tick_volume"].rolling(20).mean()
        df["vol_spike"] = df["tick_volume"] > df["vol_avg20"] * 1.2
        return df

    @staticmethod
    def add_all(df: pd.DataFrame) -> pd.DataFrame:
        df = Indicators.add_bollinger(df)
        df = Indicators.add_macd(df)
        df = Indicators.add_rsi(df)
        df = Indicators.add_ema(df)
        df = Indicators.add_atr(df)
        df = Indicators.add_volume_spike(df)
        return df

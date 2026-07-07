import pandas as pd


class SignalRules:
    """
    Enthält die einzelnen Regelprüfungen für Long- und Short-Signale.
    Jede Regel gibt True/False zurück.
    """

    @staticmethod
    def bollinger_reversal(df: pd.DataFrame, index: int) -> bool:
        """Preis berührt oder unterschreitet das untere Bollinger Band."""
        return df.loc[index, "close"] <= df.loc[index, "bb_low"]

    @staticmethod
    def macd_cross_up(df: pd.DataFrame, index: int) -> bool:
        """MACD-Linie kreuzt das Signal nach oben."""
        if index == 0:
            return False
        prev = df.loc[index - 1]
        curr = df.loc[index]
        return prev["macd"] < prev["macd_signal"] and curr["macd"] > curr["macd_signal"]

    @staticmethod
    def rsi_oversold(df: pd.DataFrame, index: int) -> bool:
        """RSI unter 30."""
        return df.loc[index, "rsi"] < 30

    @staticmethod
    def ema_trend(df: pd.DataFrame, index: int) -> bool:
        """Preis über EMA9 (Trend-Reclaim)."""
        return df.loc[index, "close"] > df.loc[index, "ema9"]

    @staticmethod
    def volume_confirmation(df: pd.DataFrame, index: int) -> bool:
        """Volumen-Spike."""
        return df.loc[index, "vol_spike"]

    @staticmethod
    def atr_valid(df: pd.DataFrame, index: int) -> bool:
        """ATR muss > 0 sein."""
        return df.loc[index, "atr"] > 0

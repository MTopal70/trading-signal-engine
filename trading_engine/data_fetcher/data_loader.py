import pandas as pd
from trading_engine.data_fetcher.mt5_connector import MT5Connector
from trading_engine.markets import MARKETS, TIMEFRAMES


class DataLoader:
    """
    DataLoader ist die zentrale Schnittstelle für das Abrufen von Marktdaten.
    Er nutzt den MT5Connector, um Kerzen aus MetaTrader 5 zu laden.
    """

    def __init__(self):
        self.mt5 = MT5Connector()

    def validate_symbol(self, symbol: str) -> bool:
        """Prüft, ob das Symbol in den unterstützten Märkten existiert."""
        return any(symbol in pairs for pairs in MARKETS.values())

    def validate_timeframe(self, timeframe: str) -> bool:
        """Prüft, ob der Timeframe gültig ist."""
        return timeframe in TIMEFRAMES

    def load_candles(self, symbol: str, timeframe: str, count: int = 500) -> pd.DataFrame:
        """
        Lädt Kerzen aus MT5 und gibt sie als DataFrame zurück.
        """

        if not self.validate_symbol(symbol):
            raise ValueError(f"Symbol '{symbol}' wird nicht unterstützt.")

        if not self.validate_timeframe(timeframe):
            raise ValueError(f"Timeframe '{timeframe}' ist ungültig.")

        df = self.mt5.get_candles(symbol, timeframe, count)

        if df is None or df.empty:
            raise RuntimeError(f"Keine Daten für {symbol} ({timeframe}) erhalten.")

        return df

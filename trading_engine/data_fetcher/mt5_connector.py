import MetaTrader5 as mt5
import pandas as pd

class MT5Connector:
    def __init__(self):
        if not mt5.initialize():
            raise Exception("MT5 konnte nicht initialisiert werden")

    def get_candles(self, symbol, timeframe, count=500):
        timeframe_map = {
            "M1": mt5.TIMEFRAME_M1,
            "M5": mt5.TIMEFRAME_M5,
            "M15": mt5.TIMEFRAME_M15,
            "M30": mt5.TIMEFRAME_M30,
            "H1": mt5.TIMEFRAME_H1,
            "H4": mt5.TIMEFRAME_H4,
            "D1": mt5.TIMEFRAME_D1,
        }

        rates = mt5.copy_rates_from_pos(symbol, timeframe_map[timeframe], 0, count)
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        return df

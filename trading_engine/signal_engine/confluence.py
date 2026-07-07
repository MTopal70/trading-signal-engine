from trading_engine.signal_engine.rules import SignalRules


class ConfluenceCalculator:
    """
    Berechnet die Confluence-Punkte eines Signals.
    """

    @staticmethod
    def calculate(df, index):
        score = 0

        if SignalRules.bollinger_reversal(df, index):
            score += 1
        if SignalRules.macd_cross_up(df, index):
            score += 1
        if SignalRules.rsi_oversold(df, index):
            score += 1
        if SignalRules.ema_trend(df, index):
            score += 1
        if SignalRules.volume_confirmation(df, index):
            score += 1
        if SignalRules.atr_valid(df, index):
            score += 1

        return score

from trading_engine.signal_engine.confluence import ConfluenceCalculator


class SignalGenerator:
    """
    Erzeugt Long- und Short-Signale basierend auf Confluence.
    """

    def __init__(self, min_score=4):
        self.min_score = min_score

    def generate(self, df):
        signals = []

        for i in range(len(df)):
            score = ConfluenceCalculator.calculate(df, i)

            if score >= self.min_score:
                signals.append({
                    "index": i,
                    "time": df.loc[i, "time"],
                    "score": score,
                    "direction": "long",  # später erweitern für short
                    "price": df.loc[i, "close"]
                })

        return signals

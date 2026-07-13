import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ChartGenerator:
    def __init__(self):
        pass

    def plot(self, df, signals=None, title="EURUSD M15 Chart"):
        df = df.copy()
        df["time"] = df["time"].dt.strftime("%Y-%m-%d %H:%M:%S")

        fig = make_subplots(
            rows=5, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.02,
            row_heights=[0.45, 0.15, 0.15, 0.15, 0.10]
        )
        """fig.write_image(f"chart_{title}.png")"""

        # --- Candlestick Chart ---
        fig.add_trace(
            go.Candlestick(
                x=df["time"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"],
                name="Price"
            ),
            row=1, col=1
        )

        # --- Bollinger Bands ---
        fig.add_trace(go.Scatter(x=df["time"], y=df["bb_high"], line=dict(color="blue"), name="BB High"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["bb_mid"], line=dict(color="gray"), name="BB Mid"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["bb_low"], line=dict(color="blue"), name="BB Low"), row=1, col=1)

        # --- EMA ---
        fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], line=dict(color="orange"), name="EMA20"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], line=dict(color="purple"), name="EMA50"), row=1, col=1)

        # --- MACD ---
        fig.add_trace(go.Scatter(x=df["time"], y=df["macd"], line=dict(color="green"), name="MACD"), row=2, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["macd_signal"], line=dict(color="red"), name="Signal"), row=2, col=1)
        fig.add_trace(go.Bar(x=df["time"], y=df["macd_hist"], name="Histogram"), row=2, col=1)

        # --- RSI ---
        fig.add_trace(go.Scatter(x=df["time"], y=df["rsi"], line=dict(color="yellow"), name="RSI"), row=3, col=1)
        fig.add_hline(y=70, line=dict(color="red", dash="dash"), row=3, col=1)
        fig.add_hline(y=30, line=dict(color="green", dash="dash"), row=3, col=1)

        # --- ATR ---
        fig.add_trace(go.Scatter(x=df["time"], y=df["atr"], line=dict(color="cyan"), name="ATR"), row=4, col=1)

        # --- Volume ---
        fig.add_trace(go.Bar(x=df["time"], y=df["tick_volume"], name="Volume"), row=5, col=1)

        # --- Signal Markers ---
        if signals:
            for sig in signals:
                sig["time"] = str(sig["time"])
                if sig["direction"] == "long":
                    fig.add_annotation(
                        x=sig["time"],
                        y=sig["price"],
                        text="▲",
                        showarrow=False,
                        font=dict(color="lime", size=18)
                    )
                else:
                    fig.add_annotation(
                        x=sig["time"],
                        y=sig["price"],
                        text="▼",
                        showarrow=False,
                        font=dict(color="red", size=18)
                    )

        fig.update_layout(
            title=title,
            xaxis_rangeslider_visible=False,
            height=1200,
            template="plotly_dark"
        )

        fig.write_image(f"chart_{title}.png")
        """fig.show()"""

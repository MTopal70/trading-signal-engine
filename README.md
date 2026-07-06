# Trading Signal Engine (Python)

Dieses Projekt implementiert eine modulare Signal-Engine für Daytrading:

- Unterstützte Märkte: Forex, Indizes, Rohstoffe, Krypto
- Datenquelle: MetaTrader 5 (Roboforex)
- Indikatoren: Bollinger Bands, MACD, RSI, EMA, ATR, Volumen
- Konservative Signal-Logik mit Confluence-Filter
- Saubere Architektur (Python-Engine, später C#-Dashboard)
- Ziel: Vorzeigbares, erweiterbares Projekt für professionelle Nutzung

## Projektstruktur

- `trading_engine/` – Kernlogik
- `tests/` – Unit-Tests
- `requirements.txt` – Abhängigkeiten

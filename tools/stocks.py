import yfinance as yf

COUNTRY_INDEX_MAP = {
    "India": {"exchange": "NSE/BSE", "symbol": "^NSEI"},
    "United States": {"exchange": "NYSE/NASDAQ", "symbol": "^GSPC"},
    "Japan": {"exchange": "TSE", "symbol": "^N225"},
    "United Kingdom": {"exchange": "LSE", "symbol": "^FTSE"},
    "Germany": {"exchange": "Frankfurt", "symbol": "^GDAXI"},
    "France": {"exchange": "Euronext Paris", "symbol": "^FCHI"},
    "China": {"exchange": "SSE/SZSE", "symbol": "000300.SS"},
    "Hong Kong": {"exchange": "HKEX", "symbol": "^HSI"},
}

def get_exchange_and_index(country: str):
    if country not in COUNTRY_INDEX_MAP:
        return {"error": "Country not supported"}

    cfg = COUNTRY_INDEX_MAP[country]

    try:
        ticker = yf.Ticker(cfg["symbol"])
        data = ticker.history(period="1d")

        if data.empty:
            raise ValueError("No data")

        return {
            "exchange": cfg["exchange"],
            "index": cfg["symbol"],
            "current_value": round(data["Close"].iloc[-1], 2),
        }

    except Exception:
        return {
            "exchange": cfg["exchange"],
            "index": cfg["symbol"],
            "current_value": "Data not available",
        }

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
    cfg = COUNTRY_INDEX_MAP.get(country)
    if not cfg:
        return {"error": "Index not supported"}

    try:
        ticker = yf.Ticker(cfg["symbol"])
        data = ticker.history(period="1d")

        if data.empty:
            return {"error": "Market data not available"}

        return {
            "exchange": cfg["exchange"],
            "index": cfg["symbol"],
            "current_value": round(data["Close"].iloc[-1], 2)
        }

    except Exception:
        return {"error": "Market data not available"}


def get_top_stocks(country: str, limit=5):
    cfg = COUNTRY_INDEX_MAP.get(country)
    if not cfg:
        return {"error": "Index not supported"}

    try:
        index = yf.Ticker(cfg["symbol"])
        funds = index.funds_data

        if not funds or funds.top_holdings is None:
            return {"error": "Top stocks not available for this index"}

        top = funds.top_holdings.head(limit)

        return [
            {
                "symbol": row["symbol"],
                "name": row["holdingName"],
                "weight_percent": round(row["holdingPercent"] * 100, 2)
            }
            for _, row in top.iterrows()
        ]

    except Exception:
        return {"error": "Top stocks not available"}

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
    symbol = COUNTRY_INDEX.get(country)
    if not symbol:
        return {"error": "Index not supported"}

    try:
        ticker = yf.Ticker(symbol)
        price = ticker.history(period="1d")["Close"].iloc[-1]

        return {
            "exchange": symbol,
            "current_value": round(price, 2)
        }
    except Exception:
        return {"error": "Market data not available"}


def get_top_stocks(country: str, limit=5):
    symbol = COUNTRY_INDEX.get(country)
    if not symbol:
        return {"error": "Index not supported"}

    try:
        index = yf.Ticker(symbol)
        holdings = index.funds_data.top_holdings

        top = holdings.head(limit)

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

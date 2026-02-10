def get_exchange_and_index(country: str):
    data = {
        "India": {"exchange": "NSE/BSE", "index": "NIFTY 50"},
        "Japan": {"exchange": "TSE", "index": "Nikkei 225"},
        "United Kingdom": {"exchange": "LSE", "index": "FTSE 100"},
    }

    return data.get(country, {"error": "Country not supported"})
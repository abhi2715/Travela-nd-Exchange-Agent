def get_currency_and_rates(country: str):
    data = {
        "India": {"currency": "INR", "usd_rate": 83.0},
        "Japan": {"currency": "JPY", "usd_rate": 148.0},
        "United Kingdom": {"currency": "GBP", "usd_rate": 0.78},
    }

    return data.get(country, {"error": "Country not supported"})
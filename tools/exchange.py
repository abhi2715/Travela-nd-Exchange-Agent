import os
import requests

API_KEY = os.getenv("EXCHANGERATE_API_KEY")

def get_currency_and_rates(country: str):
    if not API_KEY:
        return {"error": "Exchange API key missing"}

    try:
        country_res = requests.get(
            f"https://restcountries.com/v3.1/name/{country}",
            timeout=10
        )
        country_data = country_res.json()[0]
        currency_code = list(country_data["currencies"].keys())[0]
    except Exception:
        return {"error": "Invalid country name"}

    try:
        rate_res = requests.get(
            f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD",
            timeout=10
        ).json()

        rate = rate_res["conversion_rates"].get(currency_code)
        if rate is None:
            return {"error": "Rate not available"}

        return {
            "currency": currency_code,
            "usd_rate": rate
        }
    except Exception:
        return {"error": "Failed to fetch exchange rate"}

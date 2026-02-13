import os
import requests

API_KEY = os.getenv("EXCHANGERATE_API_KEY")

def get_currency_and_rates(country: str):
    if not API_KEY:
        return {"error": "Exchange API key missing"}

    try:
        # 1️⃣ Get country info from REST Countries API
        country_res = requests.get(
            f"https://restcountries.com/v3.1/name/{country}",
            timeout=10
        )

        if country_res.status_code != 200:
            return {"error": "Invalid country name"}

        country_data = country_res.json()[0]

        # Extract currency code (ISO 4217)
        currencies = country_data.get("currencies")
        if not currencies:
            return {"error": "Currency not found"}

        currency_code = list(currencies.keys())[0]

    except Exception:
        return {"error": "Failed to fetch country data"}

    try:
        # 2️⃣ Fetch live exchange rates
        rate_res = requests.get(
            f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD",
            timeout=10
        )

        if rate_res.status_code != 200:
            return {"error": "Exchange API request failed"}

        rate_data = rate_res.json()

        if rate_data.get("result") != "success":
            return {"error": "Exchange API returned error"}

        rate = rate_data["conversion_rates"].get(currency_code)

        if rate is None:
            return {"error": "Rate not available"}

        return {
            "currency": currency_code,
            "usd_rate": rate,
        }

    except Exception:
        return {"error": "Failed to fetch exchange rate"}

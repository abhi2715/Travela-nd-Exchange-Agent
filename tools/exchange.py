import os
import requests
import pycountry

API_KEY = os.getenv("EXCHANGERATE_API_KEY")

def get_currency_and_rates(country: str):
    if not API_KEY:
        return {"error": "Exchange API key missing"}

    try:
        # Find country
        country_obj = pycountry.countries.search_fuzzy(country)[0]

        # Find currency
        currency = pycountry.currencies.get(numeric=country_obj.numeric)
        if not currency:
            return {"error": "Currency not found"}

        currency_code = currency.alpha_3 if len(currency.alpha_3) == 3 else currency.alpha_3

    except Exception:
        return {"error": "Invalid country name"}

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {"error": "Exchange API request failed"}

        data = response.json()

        if data.get("result") != "success":
            return {"error": "Exchange API returned error"}

        rate = data["conversion_rates"].get(currency_code)

        if rate is None:
            return {"error": "Rate not available"}

        return {
            "currency": currency_code,
            "usd_rate": rate,
        }

    except Exception:
        return {"error": "Failed to fetch exchange rate"}

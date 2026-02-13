import os
import requests

API_KEY = os.getenv("EXCHANGERATE_API_KEY")

def get_currency_and_rates(country: str):
    if not API_KEY:
        return {"error": "Exchange API key missing"}

    # Map country → currency code
    COUNTRY_CURRENCY = {
        "India": "INR",
        "United States": "USD",
        "Japan": "JPY",
        "United Kingdom": "GBP",
        "Germany": "EUR",
        "France": "EUR",
    }

    if country not in COUNTRY_CURRENCY:
        return {"error": "Country not supported"}

    base = "USD"
    target = COUNTRY_CURRENCY[country]

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {"error": "Exchange API request failed"}

        data = response.json()

        # API-level error (very common)
        if data.get("result") != "success":
            return {"error": "Exchange API returned error"}

        rate = data["conversion_rates"].get(target)

        if rate is None:
            return {"error": "Rate not available"}

        return {
            "base": base,
            "currency": target,
            "rate": rate,
        }

    except Exception as e:
        return {"error": "Failed to fetch exchange rate"}

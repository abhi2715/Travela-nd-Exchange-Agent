import os
import requests

API_KEY = os.getenv("EXCHANGERATE_API_KEY")

def get_currency_and_rates(base="USD"):
    if not API_KEY:
        return {"error": "Exchange API key missing"}

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
    return requests.get(url).json()

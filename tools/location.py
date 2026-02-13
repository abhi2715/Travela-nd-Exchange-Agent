import requests

def get_country_location(country: str):
    try:
        url = f"https://restcountries.com/v3.1/name/{country}"
        res = requests.get(url, timeout=10).json()[0]

        lat, lon = res["latlng"]

        return {
            "country": res["name"]["common"],
            "latitude": lat,
            "longitude": lon,
            "region": res["region"],
            "subregion": res.get("subregion", "N/A"),
        }
    except Exception:
        return {"error": "Location data not available"}


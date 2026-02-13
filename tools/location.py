import requests

def get_country_location(country: str):
    try:
        res = requests.get(
            f"https://restcountries.com/v3.1/name/{country}",
            timeout=10
        ).json()[0]

        lat, lon = res["latlng"]

        return {
            "country": res["name"]["common"],
            "lat": lat,
            "lon": lon,
            "region": res["region"]
        }
    except Exception:
        return {"error": "Location not available"}

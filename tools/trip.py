from groq import Groq
import json

client = Groq()

def get_mock_flights(city: str, month="May", days=3):
    prompt = f"""
    Generate a JSON array of 3 flight options to {city} in {month}.
    Each item must include airline, price_usd, and stops.
    Return ONLY JSON.
    """

    try:
        res = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        return json.loads(res.choices[0].message.content)

    except Exception:
        return [
            {"airline": "Fallback Air", "price_usd": 500, "stops": 1}
        ]


def get_mock_hotels(city: str, nights=3):
    prompt = f"""
    Generate a JSON array of 3 hotels in {city}.
    Each must include name, price_per_night_usd, rating.
    Return ONLY JSON.
    """

    try:
        res = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return json.loads(res.choices[0].message.content)

    except Exception:
        return [
            {"name": "Fallback Hotel", "price_per_night_usd": 100, "rating": 4.0}
        ]

from groq import Groq
import json

client = Groq()

def get_mock_flights(city: str, month: str = "May", days: int = 3):
    mock_data = {
        "Tokyo": [
            {"airline": "ANA", "price_usd": 820, "stops": 0},
            {"airline": "Singapore Airlines", "price_usd": 760, "stops": 1},
        ],
        "London": [
            {"airline": "British Airways", "price_usd": 540, "stops": 0},
            {"airline": "Lufthansa", "price_usd": 500, "stops": 1},
        ],
        "New York": [
            {"airline": "Delta", "price_usd": 680, "stops": 0},
            {"airline": "Emirates", "price_usd": 620, "stops": 1},
        ],
    }

    prompt = f"""
    Generate a JSON array of 3 realistic flight options to {city} in {month}
    for a {days}-day trip.

    Each item must have:
    - airline
    - price_usd (number)
    - stops (0 or 1)

    Return ONLY valid JSON.
    """

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        return json.loads(response.choices[0].message.content)

    except Exception:
        return mock_data.get(city, [{"error": "Flight data not available"}])
from groq import Groq
import json

client = Groq()

def get_mock_hotels(city: str, nights: int = 3):
    mock_data = {
        "Tokyo": [
            {"name": "Hotel Sakura", "price_per_night_usd": 120, "rating": 4.5},
            {"name": "Tokyo Stay Inn", "price_per_night_usd": 90, "rating": 4.2},
        ],
        "London": [
            {"name": "The Westminster", "price_per_night_usd": 160, "rating": 4.5},
            {"name": "London Budget Stay", "price_per_night_usd": 110, "rating": 4.1},
        ],
        "New York": [
            {"name": "Manhattan Grand", "price_per_night_usd": 180, "rating": 4.6},
            {"name": "Central Park Lodge", "price_per_night_usd": 150, "rating": 4.3},
        ],
    }

    prompt = f"""
    Generate a JSON array of 3 hotels in {city} for a {nights}-night stay.

    Each hotel must include:
    - name
    - price_per_night_usd (number)
    - rating (between 3.5 and 5)

    Return ONLY valid JSON.
    """

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return json.loads(response.choices[0].message.content)

    except Exception:
        return mock_data.get(city, [{"error": "Hotel data not available"}])

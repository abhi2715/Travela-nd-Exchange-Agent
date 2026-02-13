def get_mock_hotels(city, nights=3):
    data = {
        "Tokyo": [
            {"name": "Hotel Sakura", "price_per_night_usd": 120, "rating": 4.5},
            {"name": "Tokyo Stay Inn", "price_per_night_usd": 90, "rating": 4.2},
        ],
        "New York": [
            {"name": "Manhattan Grand", "price_per_night_usd": 180, "rating": 4.6},
            {"name": "Central Park Lodge", "price_per_night_usd": 150, "rating": 4.3},
        ],
        "London": [
            {"name": "The Westminster", "price_per_night_usd": 160, "rating": 4.5},
            {"name": "London Budget Stay", "price_per_night_usd": 110, "rating": 4.1},
        ],
        "Paris": [
            {"name": "Hotel Lumière", "price_per_night_usd": 140, "rating": 4.4},
            {"name": "Paris Comfort Inn", "price_per_night_usd": 105, "rating": 4.2},
        ],
        "Singapore": [
            {"name": "Marina Bay Suites", "price_per_night_usd": 200, "rating": 4.7},
            {"name": "CityHub Singapore", "price_per_night_usd": 130, "rating": 4.3},
        ],
        "Dubai": [
            {"name": "Desert Pearl Hotel", "price_per_night_usd": 170, "rating": 4.6},
            {"name": "Dubai Budget Stay", "price_per_night_usd": 120, "rating": 4.2},
        ],
        "Sydney": [
            {"name": "Harbour View Hotel", "price_per_night_usd": 190, "rating": 4.6},
            {"name": "Sydney Backpacker Inn", "price_per_night_usd": 95, "rating": 4.0},
        ],
        "Delhi": [
            {"name": "Connaught Palace", "price_per_night_usd": 110, "rating": 4.4},
            {"name": "Delhi Budget Rooms", "price_per_night_usd": 70, "rating": 4.1},
        ],
    }

    return data.get(city, [{"error": "City not supported"}])

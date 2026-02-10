def get_mock_flights(city, month="May", days=3):
    return [
        {"airline": "ANA", "price_usd": 820, "stops": 0},
        {"airline": "Singapore Airlines", "price_usd": 760, "stops": 1},
    ]


def get_mock_hotels(city, nights=3):
    return [
        {"name": "Hotel Sakura", "price_per_night_usd": 120, "rating": 4.5},
        {"name": "Tokyo Stay Inn", "price_per_night_usd": 90, "rating": 4.2},
    ]
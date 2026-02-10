# Lab 12 – Agent Development (MCP + Streamlit)

## Folder structure

```
12A/
├── app.py              # Streamlit UI (two tabs: Trip Planner, Finance Agent)
├── agent.py            # LangChain + Gemini agents
├── requirements.txt
├── .env.sample         # Copy to .env and add API keys
├── README.md
└── tools/
    ├── __init__.py
    ├── weather.py      # OpenWeather API
    ├── exchange.py     # ExchangeRate API + country→currency
    ├── stocks.py       # yfinance index + Google Maps link
    └── trip.py         # Mock flights and hotels
```

## Run

1. Copy `.env.sample` to `.env` and set:
   - `GEMINI_API_KEY` (required)
   - `OPENWEATHER_API_KEY` (for Trip Planner weather)
   - `EXCHANGERATE_API_KEY` (for Finance Agent rates)

2. Install and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```
# Travel-and-currency-agent

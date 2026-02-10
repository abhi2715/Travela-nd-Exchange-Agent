import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain.agents import create_tool_calling_agent
from langchain.agents.agent import AgentExecutor

from tools.weather import get_weather
from tools.trip import get_mock_flights, get_mock_hotels
from tools.exchange import get_currency_and_rates
from tools.stocks import get_exchange_and_index

load_dotenv(override=False)
# ==================================================
# LLM
# ==================================================
def get_llm():
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY missing")

    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2,
    )

# ==================================================
# TOOLS (STRUCTURED — VERY IMPORTANT)
# ==================================================

@tool
def weather_tool(city: str) -> str:
    """Get weather for a city"""
    return str(get_weather(city))


@tool
def flights_tool(city: str, month: str = "May", days: int = 3) -> str:
    """Get flight options"""
    return str(get_mock_flights(city, month, days))


@tool
def hotels_tool(city: str, nights: int = 3) -> str:
    """Get hotel options"""
    return str(get_mock_hotels(city, nights))


@tool
def currency_tool(country: str) -> str:
    """Get currency and exchange rates"""
    return str(get_currency_and_rates(country))


@tool
def stocks_tool(country: str) -> str:
    """Get stock exchange and index"""
    return str(get_exchange_and_index(country))

# ==================================================
# TRIP AGENT
# ==================================================
def create_trip_agent():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a Trip Planner Agent.\n"
            "Use tools when required.\n"
            "Respond in sections:\n"
            "Culture & History\nWeather\nFlights\nHotels\nDay-wise Itinerary"
        ),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(
        llm=llm,
        tools=[weather_tool, flights_tool, hotels_tool],
        prompt=prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=[weather_tool, flights_tool, hotels_tool],
        verbose=False,
    )

# ==================================================
# FINANCE AGENT
# ==================================================
def create_finance_agent():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a Finance Agent.\n"
        "ONLY use the provided tools.\n"
        "DO NOT search the web.\n"
        "DO NOT use external tools.\n"
        "Return ONLY the following:\n"
        "- Currency\n"
        "- Exchange rate\n"
        "- Stock exchange\n"
        "- Market index\n"
        "If any data is unavailable, say 'Data not available'."
    ),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

    agent = create_tool_calling_agent(
        llm=llm,
        tools=[currency_tool, stocks_tool],
        prompt=prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=[currency_tool, stocks_tool],
        verbose=False,
        handle_parsing_errors=True,
    )
# ==================================================
# RUNNERS
# ==================================================
def run_trip_planner(query: str) -> str:
    return create_trip_agent().invoke({"input": query})["output"]


def run_finance_agent(country: str) -> str:
    return create_finance_agent().invoke({"input": country})["output"]

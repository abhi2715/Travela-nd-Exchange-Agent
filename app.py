import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from agent import run_trip_planner, run_finance_agent
from tools.location import get_country_location

# ==================================================
# SETUP
# ==================================================
load_dotenv(override=False)

st.set_page_config(page_title="Lab 12 – Agents", layout="wide")
st.title("Lab 12 – Agent Development")

if not os.getenv("GROQ_API_KEY"):
    st.error("GROQ_API_KEY missing in .env")
    st.stop()

tab1, tab2 = st.tabs(["Trip Planner", "Finance Agent"])

# ==================================================
# TRIP PLANNER TAB
# ==================================================
with tab1:
    st.header("Trip Planner Agent")
    query = st.text_input(
        "Trip request",
        placeholder="Plan a 3-day trip to Tokyo in May",
        key="trip_query"
    )

    if st.button("Plan Trip", key="trip_btn"):
        with st.spinner("Planning..."):
            st.markdown(run_trip_planner(query))

# ==================================================
# FINANCE TAB
# ==================================================
with tab2:
    st.header("Finance Agent")
    country = st.text_input(
        "Country name",
        placeholder="India",
        key="finance_country"
    )

    if st.button("Get Finance Info", key="finance_btn"):
        with st.spinner("Fetching..."):
            # Finance agent output
            st.markdown(run_finance_agent(country))

            # Country location + map
            loc = get_country_location(country)

            if "lat" in loc and "lon" in loc:
                df = pd.DataFrame({
                    "lat": [loc["lat"]],
                    "lon": [loc["lon"]],
                })
                st.subheader("Country Location")
                st.map(df)
            else:
                st.info("Map location not available")

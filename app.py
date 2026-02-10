import os
import streamlit as st
from dotenv import load_dotenv

from agent import run_trip_planner, run_finance_agent

load_dotenv()

st.set_page_config(page_title="Lab 12 – Agents", layout="wide")
st.title("Lab 12 – Agent Development")

if not os.getenv("GROQ_API_KEY"):
    st.error("GROQ_API_KEY missing in .env")
    st.stop()

tab1, tab2 = st.tabs(["Trip Planner", "Finance Agent"])

with tab1:
    st.header("Trip Planner Agent")
    query = st.text_input("Trip request", placeholder="Plan a 3-day trip to Tokyo in May")

    if st.button("Plan Trip"):
        with st.spinner("Planning..."):
            st.markdown(run_trip_planner(query))

with tab2:
    st.header("Finance Agent")
    country = st.text_input("Country name", placeholder="India")

    if st.button("Get Finance Info"):
        with st.spinner("Fetching..."):
            st.markdown(run_finance_agent(country))
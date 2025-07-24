import streamlit as st
from datetime import datetime
from data_fetcher import get_demand_data
from chart_utils import bookings_chart

st.set_page_config(page_title="Airline Demand Analyzer", layout="centered")
st.title("✈️ Airline Booking Market Demand Analyzer")

st.sidebar.header("🔎 Filter Bookings")

# Filters
origin = st.sidebar.selectbox("From (Origin)", ["", "SYD", "MEL", "DEL"])
destination = st.sidebar.selectbox("To (Destination)", ["", "MEL", "DEL", "SIN", "SYD"])
date_range = st.sidebar.date_input("Select Date Range", 
    value=(datetime(2025, 7, 20), datetime(2025, 7, 22)),
    min_value=datetime(2025, 7, 1),
    max_value=datetime(2025, 8, 31)
)

# Load Data
start_date, end_date = date_range
df = get_demand_data(origin, destination, start_date, end_date)

# Display Data
st.subheader("📋 Filtered Booking Data")
if df.empty:
    st.warning("No demand data found for the selected filters.")
else:
    st.dataframe(df, use_container_width=True)

    # Chart
    st.subheader("📊 Demand Trend Chart")
    st.altair_chart(bookings_chart(df), use_container_width=True)

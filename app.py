import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO | Grid Intelligence", layout="wide")

# 2. STEALTH CSS (Neon Cyan Theme)
st.markdown("""
    <style>
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.03);
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.15);
        border-radius: 10px;
    }
    h1, h2, h3, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    hr { border-color: #00ffff; opacity: 0.2; }
    </style>
    """, unsafe_allow_html=True)

# 3. DATA ENGINE (Weather + AQI)
def get_data(lat, lon):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=fahrenheit"
    aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=us_aqi"
    try:
        w_res = requests.get(weather_url).json()
        a_res = requests.get(aq_url).json()
        return {"t": w_res['current_weather']['temperature'], "a": a_res['hourly']['us_aqi'][0]}
    except:
        return {"t": "N/A", "a": "N/A"}

# 4. BRANDING (Optimized Header)
# width=600 provides a stronger presence on mobile without breaking the layout
st.image("reqxi.jpg", width=600)
st.caption("REQXI // CROSS-CONTINENT DATA FEED")

st.divider()

# 5. GRID PERFORMANCE
st.subheader("⚡ GLOBAL GRID STATUS")
e1, e2, e3 = st.columns(3)
with e1: st.metric("System Load", "420.5 GW", "STABLE")
with e2: st.metric("Market Price", "$37.46", "-0.25%")
with e3: st.metric("Active Hubs", "9", "SYNCED")

st.divider()

# 6. DIVERSE 9-CITY FEED (FL, NC, SC, North)
st.subheader("🌐 REGIONAL HUBS (Weather & Air Quality)")

# Updated City List: Removed Tarrant/excess Texas for geographic diversity
cities = {
    "Miami, FL": (25.76, -80.19),
    "Charlotte, NC": (35.22, -80.84),
    "Charleston, SC": (32.77, -79.93),
    "New York, NY": (40.71, -74.00),
    "Chicago, IL": (41.87, -87.62),
    "Fort Worth": (32.75, -97.33),
    "Toronto, ON": (43.65, -79.38),      # The "Cold North"
    "Minneapolis, MN": (44.97, -93.26),  # The "Cold State"
    "Los Angeles, CA": (34.05, -118.24)
}

names = list(cities.keys())
for i in range(0, 9, 3):
    cols = st.columns(3)
    for j in range(3):
        city = names[i+j]
        lat, lon = cities[city]
        data = get_data(lat, lon)
        with cols[j]:
            st.metric(city, f"{data['t']}°F", f"AQI: {data['a']}")

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

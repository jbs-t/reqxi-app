import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. STEALTH CSS (Matches the reqxi.jpg colors)
st.markdown("""
    <style>
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.03);
        border: 1px solid #00ffff;
        border-radius: 8px;
    }
    h1, h2, h3, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    hr { border-color: #00ffff; opacity: 0.2; }
    </style>
    """, unsafe_allow_html=True)

# 3. WEATHER & AQI DATA ENGINE
def get_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&air_quality=us_aqi&temperature_unit=fahrenheit"
    try:
        r = requests.get(url).json()
        return {
            "t": r['current_weather']['temperature'],
            "a": r.get('hourly', {}).get('us_aqi', ["N/A"])[0]
        }
    except:
        return {"t": "N/A", "a": "N/A"}

# 4. POINTING TO THE IMAGE (The Fix)
# We use width=350 to stop it from overpowering the site
st.image("reqxi.jpg", width=350)
st.caption("NORTH AMERICA DATA FEED")

st.divider()

# 5. ENERGY & CITY GRID (The Top 9 Cities)
st.subheader("⚡ LIVE GRID PERFORMANCE")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Avg Load", "420 GW", "+1.2%")
with col2: st.metric("Grid Price", "$37.46", "-0.5%")
with col3: st.metric("Active Nodes", "132", "STABLE")

st.divider()

# 9-CITY LIVE FEED
cities = {
    "New York": (40.71, -74.00), "Los Angeles": (34.05, -118.24), "Chicago": (41.87, -87.62),
    "Houston": (29.76, -95.36), "Phoenix": (33.44, -112.07), "Philadelphia": (39.95, -75.16),
    "San Antonio": (29.42, -98.49), "San Diego": (32.71, -117.16), "Fort Worth": (32.75, -97.33)
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

st.caption("REQXI PRO Terminal // Stealth Interface v4.0")

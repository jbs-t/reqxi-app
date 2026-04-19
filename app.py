import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(
    page_title="REQXI PRO | North America Data Feed",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. REQXI STEALTH CSS (Neon Cyan + Deep Black)
st.markdown("""
    <style>
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.03);
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.15);
        border-radius: 8px;
    }
    h1, h2, h3, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    hr { border-color: #00ffff; opacity: 0.3; }
    </style>
    """, unsafe_allow_html=True)

# 3. DATA ENGINES (Weather + Air Quality)
def get_city_data(lat, lon):
    # Fetching Weather (F) and Air Quality (US AQI)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&air_quality=us_aqi&temperature_unit=fahrenheit"
    try:
        data = requests.get(url).json()
        return {
            "temp": data['current_weather']['temperature'],
            "wind": data['current_weather']['windspeed'],
            "aqi": data.get('air_quality', {}).get('us_aqi', "N/A")
        }
    except:
        return {"temp": "N/A", "wind": "N/A", "aqi": "N/A"}

# 4. TOP HERO VISUAL
try:
    st.image("reqxi_stealth.jpg", use_container_width=True)
except:
    st.info("Point code to 'reqxi_stealth.jpg' and upload to GitHub.")

st.divider()

# 5. ENERGY GRID OVERVIEW (Simulated Enterprise Feed)
st.subheader("⚡ LIVE GRID PERFORMANCE")
e1, e2, e3 = st.columns(3)
with e1:
    st.metric("Total Load", "420 GW", "+1.2%")
with e2:
    st.metric("Grid Price", "$37.46", "-0.5%")
with e3:
    st.metric("Active Nodes", "132", "STABLE")

st.divider()

# 6. TOP 9 USA CITIES: WEATHER & AIR QUALITY
st.subheader("🌐 REGIONAL DATA FEED (Top 9 Hubs)")

# City Dictionary: Name -> (Lat, Lon)
cities = {
    "New York": (40.71, -74.00),
    "Los Angeles": (34.05, -118.24),
    "Chicago": (41.87, -87.62),
    "Houston": (29.76, -95.36),
    "Phoenix": (33.44, -112.07),
    "Philadelphia": (39.95, -75.16),
    "San Antonio": (29.42, -98.49),
    "San Diego": (32.71, -117.16),
    "Fort Worth": (32.75, -97.33)
}

# Creating 3 rows of 3 columns
rows = [list(cities.keys())[i:i+3] for i in range(0, 9, 3)]

for row in rows:
    cols = st.columns(3)
    for i, city_name in enumerate(row):
        lat, lon = cities[city_name]
        data = get_city_data(lat, lon)
        with cols[i]:
            st.write(f"### {city_name}")
            st.metric("Temp", f"{data['temp']}°F")
            st.write(f"💨 Wind: {data['wind']} km/h")
            # Logic for AQI color-coding could be added here later
            st.write(f"🌫️ AQI: {data['aqi']}")
    st.divider()

st.caption("REQXI PRO Terminal // Stealth Interface v2.0")

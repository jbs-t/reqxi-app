import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI Analytics | 2026 Data", layout="wide")

# 2. THEME (Deep Black + Neon Cyan)
st.markdown("""
    <style>
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.03);
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 10px rgba(0, 255, 255, 0.1);
        border-radius: 10px;
    }
    h1, h2, h3, p, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    .footer { text-align: center; color: #00ffff; padding: 30px; opacity: 0.6; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER
st.image("reqxi.jpg", width=600)
st.caption("REQXI INTELLIGENCE TERMINAL // 2026 ANALYTICS")

# 4. TOP CONSUMPTION HUBS (Data Centers & Industrial)
st.subheader("📊 2026 High-Consumption Hubs")
st.write("Cities with the highest projected load due to Data Center alley and AI infrastructure.")

c1, c2, c3 = st.columns(3)
with c1: st.metric("N. VIRGINIA (Loudoun)", "2.6 GW", "+18% Load")
with c2: st.metric("DALLAS-FT WORTH", "653 MW", "Low Price")
with c3: st.metric("NEW YORK METRO", "517 MW", "Critical")

st.divider()

# 5. CLEAN DATA HAVENS (Top Sustainable Cities)
st.subheader("🌿 2026 Clean Data Havens")
st.write("Recommended regions for green data infrastructure based on Air Quality (PM2.5) and Renewable Access.")

# Analytics Dataframe for Clean Cities
clean_cities_data = {
    "City": ["Honolulu, HI", "Anchorage, AK", "Portland, OR", "Seattle, WA", "Casper, WY"],
    "AQI (PM2.5)": ["4.1 µg/m³", "3.1 µg/m³", "4.2 µg/m³", "4.1 µg/m³", "4.0 µg/m³"],
    "Energy Source": ["Solar/Wind", "Hydro/Wind", "Hydroelectric", "Hydro/Wind", "Wind/Grid"],
    "Market Fit": ["Secondary", "Strategic", "Primary", "Primary", "Emerging"]
}
st.table(pd.DataFrame(clean_cities_data))

st.divider()

# 6. REGIONAL DATA FEED (Live)
st.subheader("🌐 LIVE CROSS-CONTINENT FEED")

def get_data(lat, lon):
    try:
        w = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=fahrenheit").json()
        a = requests.get(f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=us_aqi").json()
        return {"t": w['current_weather']['temperature'], "a": a['hourly']['us_aqi'][0]}
    except: return {"t": "N/A", "a": "N/A"}

# 9-City Diverse Split
cities = {
    "Miami, FL": (25.76, -80.19), "Charlotte, NC": (35.22, -80.84), "Charleston, SC": (32.77, -79.93),
    "Toronto, ON": (43.65, -79.38), "Minneapolis, MN": (44.97, -93.26), "Fort Worth": (32.75, -97.33),
    "New York": (40.71, -74.00), "Chicago": (41.87, -87.62), "Los Angeles": (34.05, -118.24)
}

names = list(cities.keys())
for i in range(0, 9, 3):
    cols = st.columns(3)
    for j in range(3):
        city = names[i+j]
        lat, lon = cities[city]
        d = get_data(lat, lon)
        with cols[j]: st.metric(city, f"{d['t']}°F", f"AQI: {d['a']}")

st.divider()
st.markdown('<div class="footer">PARTNERED COMPANY: JBS-T.COM</div>', unsafe_allow_html=True)
st.caption("Confidential // REQXI IT Consulting & Data Research")

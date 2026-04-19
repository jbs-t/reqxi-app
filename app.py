import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI Analytics | Resilience & Risk", layout="wide")

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
st.caption("REQXI INTELLIGENCE // DISASTER RISK & AIR ANALYTICS")

# 4. DISASTER RISK ANALYTICS (FEMA-Grade Insights)
st.subheader("🛡️ 2026 Resilience & Hazard Mitigation")
st.write("Top regions for infrastructure safety based on FEMA Community Rating System (CRS) and lower wildfire/flood risk.")

# Table for Resilience Data
resilience_data = {
    "Hub City": ["Seattle, WA", "Louisville, KY", "Baltimore, MD", "Charlotte, NC", "Columbus, OH"],
    "FEMA NFIP Discount": ["40%", "35%", "25%", "15%", "N/A"],
    "Primary Risk": ["Seismic", "Flood", "Coastal Flood", "Inland Flood", "Tornado"],
    "Mitigation Status": ["Verified", "Verified", "Active", "Active", "Active"]
}
st.table(pd.DataFrame(resilience_data))

st.divider()

# 5. HIGH-POLLUTION MONITOR (Current Trends)
st.subheader("⚠️ High-Pollution Impact Zones")
st.write("Regions seeing worsening air quality trends in 2026 due to topography, industry, or regulatory shifts.")

p1, p2, p3 = st.columns(3)
with p1: st.metric("Bakersfield, CA", "AQI Trend", "Worst US PM2.5")
with p2: st.metric("Houston, TX", "Ozone Alert", "Worsening")
with p3: st.metric("Maricopa, AZ", "PM10 Risk", "High Dust")

st.divider()

# 6. LIVE CROSS-CONTINENT FEED
st.subheader("🌐 LIVE REGIONAL DATA")

def get_data(lat, lon):
    try:
        w = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=fahrenheit").json()
        a = requests.get(f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=us_aqi").json()
        return {"t": w['current_weather']['temperature'], "a": a['hourly']['us_aqi'][0]}
    except: return {"t": "N/A", "a": "N/A"}

# 9-City Hubs
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

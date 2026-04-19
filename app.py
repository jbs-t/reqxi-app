import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO | FEMA+ Resilience", layout="wide")

# 2. STEALTH CSS
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
st.caption("REQXI INTELLIGENCE // BEYOND FEMA: ADVANCED RISK MODELING")

# 4. FEMA VS. PRIVATE RISK (The "Better" Data Section)
st.subheader("🛡️ Property-Level Resilience Metrics (First Street Model)")
st.write("Cross-referencing FEMA historical zones with 2026 Climate-Adjusted Risk Scores.")

# Analytics Data: Comparing FEMA to Modern High-Res Models
risk_comparison = {
    "Hub City": ["Miami, FL", "Charleston, SC", "Houston, TX", "New York, NY", "Chicago, IL"],
    "FEMA Zone": ["High", "High", "Moderate", "Moderate", "Low"],
    "First Street Factor": ["9/10 (Extreme)", "10/10 (Extreme)", "8/10 (Severe)", "6/10 (Moderate)", "4/10 (Minor)"],
    "Infrastructure Threat": ["Storm Surge", "Sea Level Rise", "Pluvial Flood", "Coastal Surge", "Heat Stress"]
}
st.table(pd.DataFrame(risk_comparison))

st.divider()

# 5. LIVE REGIONAL DATA (9-City Grid)
st.subheader("🌐 LIVE REGIONAL FEED")

def get_data(lat, lon):
    try:
        w = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=fahrenheit").json()
        a = requests.get(f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=us_aqi").json()
        return {"t": w['current_weather']['temperature'], "a": a['hourly']['us_aqi'][0]}
    except: return {"t": "N/A", "a": "N/A"}

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

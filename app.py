import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. CALIBRATED STEALTH CSS (Hides branding, keeps content)
st.markdown("""
    <style>
    /* HIDE TOP BAR AND BUTTONS WITHOUT BREAKING CONTENT */
    [data-testid="stHeader"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    .stDeployButton {display: none;}
    footer {visibility: hidden;}
    
    /* FIX TOP PADDING GAP */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* THEME: NEON CYAN + DEEP BLACK */
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.04);
        border: 1px solid #00ffff;
        border-radius: 10px;
        padding: 10px;
    }
    h1, h2, h3, p, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    .footer-text { text-align: center; color: #00ffff; padding: 20px; opacity: 0.6; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER (Size optimized for mobile)
st.image("reqxi.jpg", width=550)
st.caption("REQXI INTELLIGENCE // REAL-TIME OPTIMIZATION")

st.divider()

# 4. ENERGY COST ANALYTICS
st.subheader("💰 Energy Market Efficiency (LMP)")
cost_data = {
    "Market Node": ["Texas (ERCOT)", "PJM (East)", "California (CAISO)", "New York (ISO)", "Midwest (MISO)"],
    "Current $/MWh": ["$24.10", "$48.50", "$12.00", "$52.10", "$31.40"],
    "Savings Window": ["02:00-06:00", "01:00-05:00", "11:00-15:00", "03:00-05:00", "23:00-04:00"],
    "Load": ["Low", "High", "Surplus", "Peak", "Stable"]
}
st.table(pd.DataFrame(cost_data))

st.divider()

# 5. RISK MONITOR
st.subheader("🛡️ Infrastructure Resilience Monitor")
resilience_data = {
    "Region": ["Miami, FL", "Charlotte, NC", "Charleston, SC", "Minneapolis, MN", "Fort Worth"],
    "Flood Risk": ["Severe", "Moderate", "Extreme", "Low", "Low"],
    "Grid Stability": ["Watch", "Stable", "Coastal Risk", "Winter Load", "High Capacity"]
}
st.table(pd.DataFrame(resilience_data))

st.divider()

# 6. LIVE REGIONAL HUB FEED (9-City)
st.subheader("🌐 LIVE REGIONAL FEED")

def get_data(lat, lon):
    try:
        w = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=fahrenheit").json()
        a = requests.get(f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=us_aqi").json()
        return {"t": w['current_weather']['temperature'], "a": a['hourly']['us_aqi'][0]}
    except: return {"t": "--", "a": "--"}

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
st.markdown('<div class="footer-text">PARTNERED COMPANY: JBS-T.COM</div>', unsafe_allow_html=True)
st.caption("Confidential // REQXI IT Consulting & Data Research")

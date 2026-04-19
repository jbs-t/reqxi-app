import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. CLEAN STEALTH CSS
st.markdown("""
    <style>
    /* HIDE ALL STREAMLIT UI */
    [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton { display: none !important; }
    footer { visibility: hidden; }

    /* THEME: NEON CYAN + DEEP BLACK */
    .main { background-color: #010408 !important; }
    
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.04);
        border: 1px solid #00ffff;
        border-radius: 10px;
        padding: 10px;
    }
    
    /* TEXT COLORS */
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    
    /* PROGRESS BAR COLOR */
    .stProgress > div > div > div > div { background-color: #00ffff; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER
st.image("reqxi.jpg", width=550)

# 4. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Donations", "🛡️ Risk"])

with t1:
    st.subheader("🌐 Live Regional Feed")
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

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("**Compensation:** Based on Experience")
    st.markdown("""
    **Core Responsibilities:**
    * Scaling real-time ETL pipelines for grid-scale data.
    * Lead architect for automated hazard mitigation modeling.
    * Managing distributed environmental API integrations.

    **Apply:** Send resume to **justin@jbs-t.com**
    """)

with t3:
    st.subheader("🤝 Support Our Research")
    
    # RESEARCH GOAL TRACKER (Removed Dollar Amounts)
    st.write("**Current Phase: Dedicated Infrastructure Expansion**")
    st.progress(0.65) 
    st.caption("Strategic Research Goal Progress")
    
    # Display QR Code safely
    qr_path = "qr_code.svg"
    if os.path.exists(qr_path):
        st.image(qr_path, width=250)
    
    st.markdown("""
        <a href="https://cash.app/$jbstpay" target="_blank">
            <button style="background-color:#00ffff; color:black; border:none; padding:15px 30px; border-radius:8px; font-weight:bold; cursor:pointer;">
                💸 Click to Donate via Cash App
            </button>
        </a>
    """, unsafe_allow_html=True)
    st.success("Your support fuels open-access disaster intelligence.")

with t4:
    st.subheader("🛡️ Risk Analytics")
    risk_df = pd.DataFrame({
        "Region": ["Miami", "Charleston", "Fort Worth"],
        "Primary Threat": ["Hurricane/Flood", "Coastal Surge", "Severe Storms"]
    })
    st.table(risk_df)

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research Operations")

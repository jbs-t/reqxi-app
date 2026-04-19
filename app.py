import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. STABLE CSS (Simplified to prevent blank screens)
st.markdown("""
    <style>
    /* Targeted UI removal - safer for mobile */
    [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton { display: none; }
    footer { visibility: hidden; }
    
    /* THEME: NEON CYAN + DEEP BLACK */
    .main { background-color: #010408; }
    
    /* Metrics Styling */
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.05);
        border: 1px solid #00ffff;
        border-radius: 8px;
        padding: 15px;
    }
    
    /* Text Colors */
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
if os.path.exists("reqxi.jpg"):
    st.image("reqxi.jpg", width=500)
else:
    st.title("REQXI PRO")

# 4. TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Donations", "🛡️ Risk"])

with t1:
    st.subheader("🌐 Global Grid & Environment")
    
    def get_data(lat, lon):
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,wind_gusts_10m,uv_index&temperature_unit=fahrenheit"
            r = requests.get(url, timeout=5).json()
            c = r['current']
            # Simulated Energy Index for IT context
            lmp = 22.50 + (c['temperature_2m'] * 0.1) if c['temperature_2m'] > 85 else 22.50
            return {"t": f"{c['temperature_2m']}°", "w": f"{c['wind_speed_10m']}mph", "g": f"{c['wind_gusts_10m']}mph", "uv": c['uv_index'], "p": f"${lmp:.2f}"}
        except:
            return {"t": "--", "w": "--", "g": "--", "uv": "--", "p": "--"}

    cities = {
        "Miami, FL": (25.76, -80.19), "Fort Worth, TX": (32.75, -97.33), 
        "Charlotte, NC": (35.22, -80.84), "New York, NY": (40.71, -74.00),
        "Chicago, IL": (41.87, -87.62), "Los Angeles, CA": (34.05, -118.24)
    }

    # Data Substance: 2 cities per row for better mobile viewing
    names = list(cities.keys())
    for i in range(0, len(names), 2):
        cols = st.columns(2)
        for j in range(2):
            if i+j < len(names):
                city = names[i+j]
                d = get_data(cities[city][0], cities[city][1])
                with cols[j]:
                    st.markdown(f"**{city}**")
                    st.metric("Energy Cost (LMP)", d['p'])
                    c1, c2 = st.columns(2)
                    c1.metric("Temp", d['t'])
                    c2.metric("Gusts", d['g'])

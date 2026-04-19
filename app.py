import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. THE NEON THEME (Simple & Clean)
st.markdown("""
    <style>
    /* HIDE STREAMLIT UI */
    header, [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {display: none;}
    footer {visibility: hidden;}
    
    /* THEME: DEEP BLACK BACKGROUND */
    .main { background-color: #010408; }
    
    /* CYAN METRICS */
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.05);
        border: 1px solid #00ffff;
        border-radius: 10px;
    }
    
    /* TEXT COLORS */
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER
if os.path.exists("reqxi.jpg"):
    st.image("reqxi.jpg", width=500)

# 4. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Donations", "🛡️ Risk"])

with t1:
    st.subheader("🌐 Real-Time Intelligence")
    
    def get_data(lat, lon):
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&temperature_unit=fahrenheit"
            r = requests.get(url, timeout=5).json()
            return {"t": f"{r['current']['temperature_2m']}°F", "w": f"{r['current']['wind_speed_10m']} mph"}
        except: return {"t": "--", "w": "--"}

    cities = {
        "Miami, FL": (25.76, -80.19), "Fort Worth, TX": (32.75, -97.33), 
        "Charlotte, NC": (35.22, -80.84), "New York, NY": (40.71, -74.00)
    }

    for city, coords in cities.items():
        d = get_data(coords[0], coords[1])
        col1, col2 = st.columns(2)
        col1.metric(city, d['t'])
        col2.metric("Wind Speed", d['w'])
        st.divider()

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("**Pay:** Based on Experience")
    st.write("Specializing in real-time ETL and hazard modeling.")
    st.markdown("**Email Resume:** justin@jbs-t.com")

with t3:
    st.subheader("🤝 Support Research")
    st.write("**Status:** Infrastructure Expansion Phase")
    st.progress(0.65)
    
    # Safe Image Check
    if os.path.exists("qr_code.svg"):
        st.image("qr_code.svg", width=250)
    
    st.markdown("""
        <a href="https://cash.app/$jbstpay" target="_blank">
            <button style="background-color:#00ffff; color:black; border:none; padding:12px 24px; border-radius:5px; font-weight:bold; cursor:pointer;">
                💸 Donate via Cash App
            </button>
        </a>
    """, unsafe_allow_html=True)
    st.success("Your support fuels open-access disaster intelligence.")

with t4:
    st.subheader("🛡️ Risk Analytics")
    st.table(pd.DataFrame({
        "Region": ["Miami", "Fort Worth", "Charlotte", "New York"],
        "Primary Threat": ["Flood", "Storm", "Wind", "Grid Load"]
    }))

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

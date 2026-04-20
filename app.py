import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. THE SIGNATURE LOOK (Cyan & Black)
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
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&temperature_unit=fahrenheit"
            r = requests.get(url, timeout=5).json()
            c = r['current']
            return {"t": f"{c['temperature_2m']}°F", "h": f"{c['relative_humidity_2m']}%", "w": f"{c['wind_speed_10m']} mph"}
        except: return {"t": "--", "h": "--", "w": "--"}

    cities = {
        "Miami, FL": (25.76, -80.19), "Fort Worth, TX": (32.75, -97.33), 
        "Charlotte, NC": (35.22, -80.84), "New York, NY": (40.71, -74.00)
    }

    for city, coords in cities.items():
        d = get_data(coords[0], coords[1])
        st.markdown(f"### {city}")
        c1, c2, c3 = st.columns(3)
        c1.metric("Temp", d['t'])
        c2.metric("Humidity", d['h'])
        c3.metric("Wind Speed", d['w'])
        st.divider()

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("**Pay:** Based on Experience")
    st.write("Join the lead team for real-time ETL and hazard modeling.")
    st.markdown("**Email Resume:** justin@jbs-t.com")

with t3:
    st.subheader("🤝 Support Research")
    st.write("**Status:** Infrastructure Expansion Phase")
    st.progress(0.65)
    
    # Check for the file you uploaded
    if os.path.exists("$jbstpay.svg"):
        st.image("$jbstpay.svg", width=250)
    
    st.markdown("""
        <a href="https://cash.app/$jbstpay" target="_blank">
            <button style="background-color:#00ffff; color:black; border:none; padding:12px 24px; border-radius:5px; font-weight:bold; cursor:pointer;">
                💸 Donate via Cash App
            </button>
        </a>
    """, unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ Regional Resilience")
    risk_data = {
        "Region": ["Miami", "Fort Worth", "Houston", "Dallas", "Atlanta", "Seattle", "Charlotte", "New York"],
        "Risk Level": ["Extreme", "High", "Extreme", "High", "Moderate", "Moderate", "Moderate", "High"],
        "Threat": ["Flood", "Storm", "Hurricane", "Grid Load", "Inland Flood", "Heat", "Wind", "Grid Load"]
    }
    st.table(pd.DataFrame(risk_data))

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

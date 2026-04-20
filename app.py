import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. SIGNATURE CYAN & BLACK THEME
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {display: none;}
    footer {visibility: hidden;}
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.05);
        border: 1px solid #00ffff;
        border-radius: 10px;
    }
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING
if os.path.exists("reqxi.jpg"):
    st.image("reqxi.jpg", width=500)

# 4. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Donations", "🛡️ Risk Monitor"])

with t1:
    st.subheader("🌐 Global Environment & Air Quality")
    
    def get_full_data(lat, lon):
        try:
            w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&temperature_unit=fahrenheit"
            a_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi"
            w = requests.get(w_url, timeout=5).json()['current']
            a = requests.get(a_url, timeout=5).json()['current']
            return {"t": f"{w['temperature_2m']}°F", "h": f"{w['relative_humidity_2m']}%", "w": f"{w['wind_speed_10m']} mph", "aq": a['us_aqi']}
        except: return {"t": "--", "h": "--", "w": "--", "aq": "--"}

    # Expanded to 10 States / Hubs
    cities = {
        "Los Angeles, CA": (34.05, -118.24),
        "Fort Worth, TX": (32.75, -97.33), 
        "Las Vegas, NV": (36.17, -115.13),
        "New York, NY": (40.71, -74.00),
        "Chicago, IL": (41.87, -87.62),
        "Charlotte, NC": (35.22, -80.84),
        "Charleston, SC": (32.77, -79.93),
        "Atlanta, GA": (33.74, -84.38),
        "Miami, FL": (25.76, -80.19),
        "Seattle, WA": (47.60, -122.33)
    }

    for city, coords in cities.items():
        d = get_full_data(coords[0], coords[1])
        st.markdown(f"### {city}")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Air Quality (AQI)", d['aq'])
        c2.metric("Temp", d['t'])
        c3.metric("Humidity", d['h'])
        c4.metric("Wind Speed", d['w'])
        st.divider()

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("**Pay:** Based on Experience")
    st.markdown("**Email Resume:** justin@jbs-t.com")

with t3:
    st.subheader("🤝 Support Research")
    st.progress(0.65)
    if os.path.exists("$jbstpay.svg"):
        st.image("$jbstpay.svg", width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#00ffff; color:black; border:none; padding:12px 24px; border-radius:5px; font-weight:bold; cursor:pointer;">💸 Donate via Cash App</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ 10-State Risk & Grid Monitor")
    
    risk_data = {
        "State / Hub": ["California (LA)", "Texas (FTW)", "Nevada (LV)", "New York (NYC)", "Illinois (CHI)", "N. Carolina (CLT)", "S. Carolina (CHS)", "Georgia (ATL)", "Florida (MIA)", "Washington (SEA)"],
        "Grid Status": ["Watch", "High Load", "Extreme Heat", "High Load", "Stable", "Stable", "Coastal Risk", "Moderate", "Critical", "Stable"],
        "Primary Risk": ["Wildfire/Seismic", "Severe Storm", "Thermal Stress", "Infrastructure", "Grid Congestion", "Wind", "Flood/Surge", "Inland Flood", "Hurricane", "Seismic"],
        "Threat Level": ["High", "High", "High", "High", "Moderate", "Low", "Extreme", "Moderate", "Critical", "Moderate"]
    }
    st.table(pd.DataFrame(risk_data))

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

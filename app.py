import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. CLEAN STEALTH CSS
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton { display: none !important; }
    footer { visibility: hidden; }
    .main { background-color: #010408 !important; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.04);
        border: 1px solid #00ffff;
        border-radius: 10px;
        padding: 10px;
    }
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    .stProgress > div > div > div > div { background-color: #00ffff; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER
st.image("reqxi.jpg", width=550)

# 4. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Donations", "🛡️ Risk"])

with t1:
    st.subheader("🌐 Real-Time Grid & Environmental Intelligence")
    
    def get_advanced_data(lat, lon):
        try:
            # Combined API call for Weather, Wind, and UV
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,wind_speed_10m,wind_gusts_10m,uv_index&temperature_unit=fahrenheit&wind_speed_unit=mph"
            r = requests.get(url).json()
            c = r['current']
            
            # Simulated LMP (Locational Marginal Price) based on temp/load for business context
            base_price = 25.00
            lmp = base_price + (c['temperature_2m'] * 0.15) if c['temperature_2m'] > 80 else base_price
            
            return {
                "temp": f"{c['temperature_2m']}°F",
                "feels": f"{c['apparent_temperature']}°F",
                "wind": f"{c['wind_speed_10m']} mph",
                "gusts": f"{c['wind_gusts_10m']} mph",
                "uv": c['uv_index'],
                "lmp": f"${lmp:.2f}/MWh"
            }
        except:
            return {"temp": "--", "feels": "--", "wind": "--", "gusts": "--", "uv": "--", "lmp": "--"}

    cities = {
        "Miami, FL": (25.76, -80.19), "Charlotte, NC": (35.22, -80.84), "Charleston, SC": (32.77, -79.93),
        "Toronto, ON": (43.65, -79.38), "Minneapolis, MN": (44.97, -93.26), "Fort Worth, TX": (32.75, -97.33),
        "New York, NY": (40.71, -74.00), "Chicago, IL": (41.87, -87.62), "Los Angeles, CA": (34.05, -118.24)
    }

    # Displaying deep-dive data in 3 columns
    names = list(cities.keys())
    for i in range(0, 9, 3):
        cols = st.columns(3)
        for j in range(3):
            city = names[i+j]
            lat, lon = cities[city]
            d = get_advanced_data(lat, lon)
            with cols[j]:
                st.markdown(f"### {city}")
                st.metric("Grid Price (LMP)", d['lmp'])
                m_col1, m_col2 = st.columns(2)
                m_col1.metric("Temp / Feels", d['temp'], d['feels'])
                m_col2.metric("Wind / Gusts", d['wind'], d['gusts'])
                st.write(f"**UV Index:** {d['uv']}")
                st.divider()

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("**Compensation:** Based on Experience")
    st.markdown("""
    **Apply:** Send resume to **justin@jbs-t.com**
    """)

with t3:
    st.subheader("🤝 Support Our Research")
    st.write("**Current Phase: Infrastructure Expansion**")
    st.progress(0.65) 
    qr_path = "qr_code.svg"
    if os.path.exists(qr_path):
        st.image(qr_path, width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#00ffff; color:black; border:none; padding:15px 30px; border-radius:8px; font-weight:bold; cursor:pointer;">💸 Donate via Cash App</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ Risk Analytics")
    risk_df = pd.DataFrame({
        "Metric": ["Grid Stability", "Supply Chain Delay", "Thermal Stress"],
        "Status": ["Watch", "Elevated", "Low"],
        "Action": ["Load Balancing", "Route Optimization", "Nominal Ops"]
    })
    st.table(risk_df)

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research Operations")

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
    
    /* Metric Cards */
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.05);
        border: 1px solid #00ffff;
        border-radius: 10px;
    }
    
    /* Text Colors */
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. TOP NAVIGATION & BRANDING
col_a, col_b = st.columns([3, 1])
with col_a:
    if os.path.exists("reqxi.jpg"):
        st.image("reqxi.jpg", width=480)
with col_b:
    st.write("###") # Spacer
    st.markdown("""
        <a href="mailto:justin@jbs-t.com" style="text-decoration:none;">
            <button style="background-color:#00ffff; color:black; border:none; padding:15px; border-radius:5px; font-weight:bold; width:100%; cursor:pointer;">
                💼 CONSULTING INQUIRY
            </button>
        </a>
    """, unsafe_allow_html=True)

# 4. BUSINESS & MARKET DATA (Substance)
st.markdown("#### 📈 GLOBAL MARKET INTELLIGENCE")
m1, m2, m3, m4 = st.columns(4)
m1.metric("WTI CRUDE", "$79.12", "+1.4%")
m2.metric("NASDAQ 100", "18,240", "+0.8%")
m3.metric("BTC/USD", "$64,210", "+2.1%")
m4.metric("US 10Y YIELD", "4.22%", "-0.05%")
st.divider()

# 5. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Support", "🛡️ Risk Monitor"])

with t1:
    st.subheader("🌐 Global Environment & Air Quality")
    
    def get_data(lat, lon):
        try:
            w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m&current=us_aqi&temperature_unit=fahrenheit"
            aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi"
            w = requests.get(w_url, timeout=5).json()['current']
            a = requests.get(aq_url, timeout=5).json()['current']
            return {"t": f"{w['temperature_2m']}°", "h": f"{w['relative_humidity_2m']}%", "aq": a['us_aqi']}
        except: return {"t": "--", "h": "--", "aq": "--"}

    # 10 State Intelligence Feed
    cities = {
        "Los Angeles, CA": (34.05, -118.24), "Fort Worth, TX": (32.75, -97.33), 
        "Las Vegas, NV": (36.17, -115.13), "New York, NY": (40.71, -74.00),
        "Chicago, IL": (41.87, -87.62), "Charlotte, NC": (35.22, -80.84),
        "Charleston, SC": (32.77, -79.93), "Atlanta, GA": (33.74, -84.38),
        "Miami, FL": (25.76, -80.19), "Seattle, WA": (47.60, -122.33)
    }

    for city, coords in cities.items():
        d = get_data(coords[0], coords[1])
        c1, c2, c3, c4 = st.columns([2,1,1,1])
        c1.write(f"**{city}**")
        c2.metric("AQI", d['aq'])
        c3.metric("Temp", d['t'])
        c4.metric("Humidity", d['h'])
    st.divider()

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("Specialization: Geospatial Risk Modeling")
    st.markdown("**Justin@jbs-t.com**")

with t3:
    st.subheader("🤝 Support Research")
    if os.path.exists("$jbstpay.svg"):
        st.image("$jbstpay.svg", width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#00ffff; color:black; border:none; padding:15px 30px; border-radius:8px; font-weight:bold; cursor:pointer;">💸 Cash App</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ 10-State Risk & Grid Monitor")
    risk_df = pd.DataFrame({
        "State/Hub": ["CA (LA)", "TX (FTW)", "NV (LV)", "NY (NYC)", "IL (CHI)", "NC (CLT)", "SC (CHS)", "GA (ATL)", "FL (MIA)", "WA (SEA)"],
        "Grid Status": ["Watch", "High Load", "Heat Watch", "High Load", "Stable", "Stable", "Coastal Risk", "Moderate", "Critical", "Stable"],
        "Threat": ["Wildfire", "Storm", "Thermal", "Grid Load", "Congestion", "Wind", "Surge", "Flood", "Hurricane", "Seismic"]
    })
    st.table(risk_df)

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

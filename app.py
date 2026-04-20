import streamlit as st
import pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. THE NEON THEME (Cyan & Black)
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

# 3. BRANDING HEADER
if os.path.exists("reqxi.jpg"):
    st.image("reqxi.jpg", width=500)

# 4. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Donations", "🛡️ Risk"])

with t1:
    st.subheader("🌐 Operational Intelligence Feed")
    
    def get_deep_data(lat, lon):
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m&temperature_unit=fahrenheit"
            r = requests.get(url, timeout=5).json()
            c = r['current']
            return {
                "t": f"{c['temperature_2m']}°F", 
                "h": f"{c['relative_humidity_2m']}%",
                "p": f"{c['precipitation']}in",
                "w": f"{c['wind_speed_10m']}mph"
            }
        except: return {"t": "--", "h": "--", "p": "--", "w": "--"}

    cities = {
        "Miami, FL": (25.76, -80.19), "Fort Worth, TX": (32.75, -97.33), 
        "Charlotte, NC": (35.22, -80.84), "New York, NY": (40.71, -74.00)
    }

    for city, coords in cities.items():
        d = get_deep_data(coords[0], coords[1])
        st.markdown(f"### {city}")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Temp", d['t'])
        c2.metric("Humidity", d['h'])
        c3.metric("Precip", d['p'])
        c4.metric("Wind", d['w'])
        st.divider()

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("**Pay:** Based on Experience")
    st.markdown("**Email Resume:** justin@jbs-t.com")

with t3:
    st.subheader("🤝 Support Research")
    st.progress(0.65)
    if os.path.exists("qr_code.svg"):
        st.image("qr_code.svg", width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#00ffff; color:black; border:none; padding:12px 24px; border-radius:5px; font-weight:bold; cursor:pointer;">💸 Donate via Cash App</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ Regional Resilience Monitor")
    # Added Houston, Dallas, Atlanta, and Seattle
    risk_data = {
        "Region": ["Miami", "Fort Worth", "Houston", "Dallas", "Atlanta", "Seattle", "Charlotte", "New York"],
        "Threat Level": ["Extreme", "High", "Extreme", "High", "Moderate", "Moderate", "Moderate", "High"],
        "Primary Risk": ["Flood/Surge", "Severe Storm", "Hurricane", "Grid Load", "Inland Flood", "Seismic/Heat", "Wind", "Grid Load"]
    }
    st.table(pd.DataFrame(risk_data))

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

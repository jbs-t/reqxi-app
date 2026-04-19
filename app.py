import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. STABLE STEALTH CSS (Recalibrated for 2026 Streamlit)
st.markdown("""
    <style>
    /* HIDE TOP BARS WITHOUT BREAKING CONTENT */
    header, [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {
        display: none !important;
        visibility: hidden;
    }
    footer {visibility: hidden;}

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
    
    /* BUTTON STYLING */
    .stButton>button {
        background-color: #00ffff;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        border: none;
    }

    /* FOOTER LINK */
    .footer-link {
        color: #00ffff !important;
        text-decoration: none;
        font-weight: bold;
        border: 1px solid #00ffff;
        padding: 12px 24px;
        border-radius: 6px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER
st.image("reqxi.jpg", width=550)

# 4. NAVIGATION TABS
tab1, tab2, tab3, tab4 = st.tabs(["📊 Intelligence", "🛠️ Careers", "🤝 Donations", "🛡️ Risk Monitor"])

with tab1:
    st.subheader("🌐 Live Regional Feed")
    def get_data(lat, lon):
        try:
            # Weather and AQI data
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
            with cols[j]:
                st.metric(city, f"{d['t']}°F", f"AQI: {d['a']}")

with tab2:
    st.subheader("🚀 Join the REQXI Team")
    st.markdown("### **Hiring: Data Engineer (L3)**")
    st.write("Specializing in real-time ETL pipelines and hazard mitigation analytics.")
    st.markdown("""
    **Apply via the JBS-T Portal:**
    [Submit Application Here](https://www.jbs-t.com)
    """)

with tab3:
    st.subheader("🤝 Support Our Research")
    st.write("Scan the QR code or click the button below to donate via Cash App.")
    
    # Displays the QR code you provided
    st.image("$jbstpay.svg", width=300)
    
    st.markdown("""
        <a href="https://cash.app/$jbstpay" target="_blank">
            <button style="background-color:#00ffff; color:black; border:none; padding:15px 30px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:16px;">
                💸 Click to Donate via Cash App
            </button>
        </a>
    """, unsafe_allow_html=True)

with tab4:
    st.subheader("🛡️ Resilience Analytics")
    resilience_data = {
        "Region": ["Miami, FL", "Charleston, SC", "Fort Worth, TX", "Minneapolis, MN"],
        "Flood Risk": ["Severe", "Extreme", "Low", "Low"],
        "Grid Stability": ["Watch", "Coastal Risk", "High Capacity", "Winter Load"]
    }
    st.table(pd.DataFrame(resilience_data))

st.divider()

# 5. HYPERLINKED FOOTER
st.markdown('<div style="text-align:center;"><a href="https://www.jbs-t.com" target="_blank" class="footer-link">PARTNERED COMPANY: WWW.JBS-T.COM</a></div>', unsafe_allow_html=True)
st.caption("Confidential // REQXI IT Consulting & Data Research")

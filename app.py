import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. MELANIN-OPTIMIZED CSS (Warm High-Contrast)
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {display: none;}
    footer {visibility: hidden;}
    
    /* BASE: Deep Charcoal for better eye comfort */
    .main { background-color: #0A0A0A; }
    
    /* CARDS: Warm Mocha & Amber glow */
    [data-testid="stMetric"] {
        background: rgba(255, 191, 0, 0.03);
        border: 1px solid #FFBF00;
        border-radius: 12px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    /* TYPOGRAPHY: Gold, Amber, and High-Res White */
    h1, h2, h3 { color: #FFD700 !important; font-weight: 800; } /* Gold */
    p, span, label { color: #FFBF00 !important; } /* Amber */
    [data-testid="stMetricLabel"] > div { color: #FFBF00 !important; font-size: 1.1rem; }
    [data-testid="stMetricValue"] > div { color: #FFFFFF !important; font-weight: 700; text-shadow: 1px 1px 2px #000; }
    
    /* TAB STYLING */
    .stTabs [data-baseweb="tab"] { color: #FFBF00; font-weight: bold; }
    .stTabs [aria-selected="true"] { border-bottom-color: #FFD700 !important; color: #FFD700 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING
if os.path.exists("reqxi.jpg"):
    st.image("reqxi.jpg", width=520)

# 4. TABS
t1, t2, t3, t4 = st.tabs(["📊 Air & Grid", "🚀 Careers", "🤝 Support", "🛡️ Risk"])

with t1:
    st.subheader("🌐 Community Intelligence Feed")
    
    def get_community_data(lat, lon):
        try:
            # Weather + Air Quality (AQI)
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m&hourly=us_aqi,pm2_5&forecast_days=1"
            aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi,pm2_5"
            
            w = requests.get(url, timeout=5).json()
            aq = requests.get(aq_url, timeout=5).json()
            
            return {
                "t": f"{w['current']['temperature_2m']}°F",
                "h": f"{w['current']['relative_humidity_2m']}%",
                "aqi": aq['current']['us_aqi'],
                "pm": f"{aq['current']['pm2_5']} µg/m³"
            }
        except: return {"t": "--", "h": "--", "aqi": "--", "pm": "--"}

    cities = {
        "Fort Worth, TX": (32.75, -97.33), "Houston, TX": (29.76, -95.36),
        "Atlanta, GA": (33.74, -84.38), "Chicago, IL": (41.87, -87.62)
    }

    for city, coords in cities.items():
        d = get_community_data(coords[0], coords[1])
        st.markdown(f"### {city}")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Air Quality (US AQI)", d['aqi'])
        c2.metric("PM2.5 (Fine Soot)", d['pm'])
        c3.metric("Heat Index", d['t'])
        c4.metric("Humidity", d['h'])
        st.divider()

with t2:
    st.subheader("🚀 Join REQXI")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.info("Comp: Based on Experience. Focus: Community Resilience Data.")
    st.markdown("**Justin@jbs-t.com**")

with t3:
    st.subheader("🤝 Research Funding")
    st.progress(0.65)
    if os.path.exists("$jbstpay.svg"):
        st.image("$jbstpay.svg", width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#FFD700; color:black; border:none; padding:15px 30px; border-radius:8px; font-weight:bold; cursor:pointer;">💸 Cash App Donation</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ Resilience Monitor")
    risk_df = pd.DataFrame({
        "Market": ["Houston", "Fort Worth", "Atlanta", "Chicago"],
        "AQI Threat": ["Severe", "High", "Moderate", "High"],
        "Grid Risk": ["Critical", "High", "Low", "Moderate"]
    })
    st.table(risk_df)

st.divider()
st.caption("Confidential // REQXI IT & Community Intelligence Operations")

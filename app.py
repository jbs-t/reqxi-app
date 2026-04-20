import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. MELANIN-OPTIMIZED CSS (Warm, Deep, & Gold)
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {display: none;}
    footer {visibility: hidden;}
    
    /* BASE: Warm Charcoal for better eye comfort */
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
    
    /* 3. LOGO CONTAINER: Isolation & Focus */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 50px 0;
        background: linear-gradient(180deg, #0A0A0A 0%, #151515 100%);
        border-bottom: 1px solid #222;
        margin-bottom: 30px;
    }
    .eagle-ring {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background-color: #000;
        border: 4px solid #FFD700; /* Gold Ring */
        
        /* The Glow (Defining the center) */
        box-shadow: 0px 0px 60px rgba(0, 255, 255, 0.6); 
        margin-bottom: 20px;
    }
    .eagle-icon {
        color: #FFD700; /* Antique Gold */
        font-size: 80px;
        font-weight: 900;
        text-shadow: 0px 0px 10px rgba(0, 255, 255, 0.8);
    }
    .reqxi-text {
        color: #FFFFFF; /* High-Res White */
        font-size: 55px;
        font-weight: 800;
        letter-spacing: -2px;
        text-transform: uppercase;
        text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# 4. ENHANCED BRANDING HEADER (Defining the Eagle)
st.markdown("""
    <div class="logo-container">
        <div class="eagle-ring">
            <span class="eagle-icon">🦅</span>
        </div>
        <span class="reqxi-text">REQXI</span>
    </div>
    """, unsafe_allow_html=True)

# 5. BUSINESS & MARKET DATA (Simulated)
st.markdown("#### 📈 GLOBAL MARKET INTELLIGENCE")
m1, m2, m3, m4 = st.columns(4)
m1.metric("WTI CRUDE", "$79.12", "+1.4%")
m2.metric("NASDAQ 100", "18,240", "+0.8%")
m3.metric("BTC/USD", "$64,210", "+2.1%")
m4.metric("US 10Y YIELD", "4.22%", "-0.05%")
st.divider()

# 6. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Air & Grid", "🚀 Join Us", "🤝 Support", "🛡️ Resilience Monitor"])

with t1:
    st.subheader("🌐 Community Intelligence Feed")
    
    def get_community_data(lat, lon):
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m&current=us_aqi&temperature_unit=fahrenheit"
            aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi,pm2_5"
            w = requests.get(url, timeout=5).json()['current']
            aq = requests.get(aq_url, timeout=5).json()['current']
            return {"t": f"{w['temperature_2m']}°F", "h": f"{w['relative_humidity_2m']}%", "aqi": aq['us_aqi'], "pm": f"{aq['pm2_5']} µg/m³"}
        except: return {"t": "--", "h": "--", "aqi": "--", "pm": "--"}

    cities = {
        "Fort Worth, TX": (32.75, -97.33), "Houston, TX": (29.76, -95.36),
        "Atlanta, GA": (33.74, -84.38), "Chicago, IL": (41.87, -87.62)
    }

    for city, coords in cities.items():
        d = get_community_data(coords[0], coords[1])
        st.markdown(f"### {city}")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("AQI (US)", d['aqi'])
        c2.metric("PM2.5 (Soot)", d['pm'])
        c3.metric("Temp", d['t'])
        c4.metric("Humidity", d['h'])
        st.divider()

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("Join the lead team for real-time ETL and hazard modeling.")
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
        "Hub": ["Houston", "Fort Worth", "Atlanta", "Chicago"],
        "Threat Level": ["Extreme", "High", "Moderate", "High"],
        "Risk Factor": ["Flood/Hurricane", "Severe Storm", "Inland Flood", "Heat/Grid"]
    })
    st.table(risk_df)

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO | Intelligence Terminal", layout="wide")

# 2. STEALTH CSS (Hides branding + Corporate Styling)
st.markdown("""
    <style>
    /* HIDE STREAMLIT BRANDING */
    [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {display: none;}
    footer {visibility: hidden;}
    
    /* THEME: NEON CYAN + DEEP BLACK */
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.04);
        border: 1px solid #00ffff;
        border-radius: 10px;
    }
    
    /* TEXT COLORS */
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    
    /* TABS STYLING */
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    .stTabs [data-baseweb="tab"] { color: #00ffff; border-bottom: 2px solid transparent; }
    .stTabs [data-baseweb="tab"]:hover { color: #ffffff; }
    .stTabs [aria-selected="true"] { color: #ffffff !important; border-bottom: 2px solid #00ffff !important; }

    /* FOOTER */
    .footer-container { text-align: center; padding: 40px; }
    .footer-link { color: #00ffff !important; text-decoration: none; font-weight: bold; border: 1px solid #00ffff; padding: 10px 20px; border-radius: 5px; }
    .footer-link:hover { background: rgba(0, 255, 255, 0.1); }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER
st.image("reqxi.jpg", width=550)

# 4. NAVIGATION TABS
tab1, tab2, tab3, tab4 = st.tabs(["📊 Intelligence Feed", "🛠️ Careers", "🤝 Donations", "🛡️ Risk Monitor"])

with tab1:
    st.subheader("🌐 Live Regional Feed")
    
    def get_data(lat, lon):
        try:
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
            with cols[j]: st.metric(city, f"{d['t']}°F", f"AQI: {d['a']}")

with tab2:
    st.subheader("🚀 Careers at REQXI")
    st.markdown("### **Hiring: Data Engineer (L3)**")
    st.write("**Location:** Remote / Hybrid (Fort Worth Hub)")
    st.markdown("""
    **Core Responsibilities:**
    * Architecting real-time ETL pipelines for grid-scale energy data.
    * Maintaining distributed Air Quality and Weather API integrations.
    * Developing high-concurrency data models for disaster resilience analytics.
    
    **To Apply:** Send your CV and GitHub profile to the JBS-T portal.
    """)
    if st.button("Submit Inquiry"):
        st.success("Application link generated. Redirecting to JBS-T Secure Portal...")

with tab3:
    st.subheader("🤝 Support Our Research")
    st.write("Your donations power our open-access disaster resilience and air quality research for underserved communities.")
    
    amount = st.radio("Select Donation Amount", ["$25", "$50", "$100", "Custom"])
    if st.button("Proceed to Secure Payment"):
        st.info("Directing to Secure Stripe/PayPal Gateway...")

with tab4:
    st.subheader("🛡️ Resilience Monitor")
    resilience_data = {
        "Region": ["Miami", "Charlotte", "Charleston", "Minneapolis", "Fort Worth"],
        "Flood Risk": ["Severe", "Moderate", "Extreme", "Low", "Low"],
        "Grid Status": ["Watch", "Stable", "Coastal Risk", "Winter Load", "Secure"]
    }
    st.table(pd.DataFrame(resilience_data))

st.divider()

# 5. HYPERLINKED PARTNERSHIP FOOTER
st.markdown(
    '<div class="footer-container">'
    '<a href="https://www.jbs-t.com" target="_blank" class="footer-link">PARTNERED COMPANY: WWW.JBS-T.COM</a>'
    '</div>', 
    unsafe_allow_html=True
)
st.caption("Confidential // REQXI IT Consulting & Data Research")

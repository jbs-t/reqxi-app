import streamlit as st
import pandas as pd
import requests
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. SIGNATURE CYAN & BLACK THEME
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
    
    /* ENHANCED LOGO TEXT (Matches Cyan icon color) */
    .logo-container {
        display: flex;
        align-items: center;
        gap: 20px;
        padding-bottom: 25px;
    }
    .reqxi-text {
        font-family: 'Montserrat', sans-serif; /* Clean, modern font */
        color: #00ffff;
        font-size: 55px;
        font-weight: 800;
        letter-spacing: -2px;
        line-height: 1;
    }
    
    /* STANDARD TEXT COLORS */
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: 700; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. ENHANCED BRANDING HEADER
logo_path = "reqxi.jpg" # Make sure this matches your uploaded icon filename

if os.path.exists(logo_path):
    # This creates a cohesive container: [Icon] REQXI
    col_a, col_b = st.columns([1, 4])
    with col_a:
        st.image(logo_path, width=120) # Just the icon
    with col_b:
        # Integrated Text with font that matches the sleek icon
        st.markdown('<div class="logo-container"><span class="reqxi-text">REQXI</span></div>', unsafe_allow_html=True)
else:
    # Safe Fallback if image isn't found
    st.title("REQXI PRO")

# 4. MARKET TICKER
st.markdown("#### 📈 MARKET INTELLIGENCE")
m1, m2, m3, m4 = st.columns(4)
m1.metric("WTI CRUDE", "$79.12", "+1.4%")
m2.metric("NASDAQ 100", "18,240", "+0.8%")
m3.metric("ERCOT LOAD", "44.2 GW", "WATCH")
m4.metric("US 10Y YIELD", "4.22%", "-0.05%")
st.divider()

# 5. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Support", "🛡️ Risk Monitor"])

with t1:
    st.subheader("🌐 Global Environment & Air Quality")
    # ... (Keep your 10-city data engine here)
    st.info("Live data stream active. Monitoring 10 major US hubs.")

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("Pay: Based on Experience | Email: **justin@jbs-t.com**")

with t3:
    st.subheader("🤝 Support Research")
    if os.path.exists("$jbstpay.svg"):
        st.image("$jbstpay.svg", width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#00ffff; color:black; border:none; padding:12px; border-radius:5px; font-weight:bold; cursor:pointer;">💸 Donate via Cash App</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ Regional Resilience Monitor")
    # (Keep your expanded 10-state table here)
    risk_df = pd.DataFrame({
        "Hub": ["Houston", "Fort Worth", "LA", "NYC"],
        "Grid": ["Critical", "High", "Watch", "High"],
        "Threat": ["Hurricane", "Storm", "Seismic", "Age"]
    })
    st.table(risk_df)

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

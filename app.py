import streamlit as st
import pandas as pd
import requests
import pydeck as pdk
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
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: 700; }
    
    /* Clean Tab Navigation */
    .stTabs [data-baseweb="tab"] { color: #00ffff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. SINGLE LOGO HEADER (No duplication)
logo_path = "rex.jpg" # Using your specific filename

if os.path.exists(logo_path):
    st.image(logo_path, width=600) # This shows the full logo + text as one image
else:
    st.title("REQXI PRO")

# 4. MARKET INTELLIGENCE TICKER
st.markdown("#### 📈 MARKET DATA")
m1, m2, m3, m4 = st.columns(4)
m1.metric("WTI CRUDE", "$79.12", "+1.4%")
m2.metric("ERCOT LOAD", "44.2 GW", "WATCH")
m3.metric("FEDEX (FDX)", "$254.10", "STABLE")
m4.metric("NASDAQ 100", "18,240", "+0.8%")
st.divider()

# 5. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Support", "🛡️ Risk Monitor"])

with t1:
    st.subheader("🌐 Global Environment & Air Quality")
    
    def get_data(lat, lon):
        try:
            w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m&temperature_unit=fahrenheit"
            aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi"
            w = requests.get(w_url, timeout=5).json()['current']
            a = requests.get(aq_url, timeout=5).json()['current']
            return {"t": f"{w['temperature_2m']}°", "h": f"{w['relative_humidity_2m']}%", "aq": a['us_aqi']}
        except: return {"t": "--", "h": "--", "aq": 0}

    # 10 State Cities
    cities = {
        "Miami, FL": (25.76, -80.19), "Fort Worth, TX": (32.75, -97.33), 
        "Charlotte, NC": (35.22, -80.84), "New York, NY": (40.71, -74.00),
        "Chicago, IL": (41.87, -87.62), "Los Angeles, CA": (34.05, -118.24),
        "Las Vegas, NV": (36.17, -115.13), "Charleston, SC": (32.77, -79.93),
        "Atlanta, GA": (33.74, -84.38), "Seattle, WA": (47.60, -122.33)
    }

    map_list = []
    for city, coords in cities.items():
        d = get_data(coords[0], coords[1])
        c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
        c1.write(f"**{city}**")
        c2.metric("AQI", d['aq'])
        c3.metric("Temp", d['t'])
        c4.metric("Humid", d['h'])
        map_list.append({"name": city, "lat": coords[0], "lon": coords[1], "aqi": d['aq']})
    
    st.divider()
    st.markdown("### 🗺️ Geospatial Risk Map")
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v11',
        initial_view_state=pdk.ViewState(latitude=37.0902, longitude=-95.7129, zoom=3, pitch=45),
        layers=[
            pdk.Layer('ColumnLayer', data=pd.DataFrame(map_list), get_position=['lon', 'lat'], 
                      get_elevation='aqi', elevation_scale=1000, radius=30000, 
                      get_fill_color=[0, 255, 255, 180], pickable=True)
        ]
    ))

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("Specializing in Geospatial Intelligence.")
    st.markdown("**Justin@jbs-t.com**")

with t3:
    st.subheader("🤝 Support Research")
    if os.path.exists("$jbstpay.svg"):
        st.image("$jbstpay.svg", width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#00ffff; color:black; border:none; padding:15px; border-radius:5px; font-weight:bold; cursor:pointer;">💸 Cash App</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ 10-State Risk & Grid Monitor")
    risk_df = pd.DataFrame({
        "Hub": ["LA", "FTW", "LV", "NYC", "CHI", "CLT", "CHS", "ATL", "MIA", "SEA"],
        "Grid": ["Watch", "High", "Heat", "High", "Stable", "Stable", "Flood", "Mod", "Crit", "Stable"],
        "Risk": ["Wildfire", "Storm", "Thermal", "Load", "Congest", "Wind", "Surge", "Rain", "Hurricane", "Seismic"]
    })
    st.table(risk_df)

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

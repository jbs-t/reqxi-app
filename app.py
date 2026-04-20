import streamlit as st
import pandas as pd
import requests
import pydeck as pdk # We use pydeck to render the map
import os

# 1. PAGE SETUP
st.set_page_config(page_title="REQXI PRO", layout="wide")

# 2. THE CYAN-INTELLIGENCE THEME
st.markdown("""
    <style>
    /* HIDE STREAMLIT UI */
    header, [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {display: none;}
    footer {visibility: hidden;}
    
    /* THEME: DEEP BLACK BACKGROUND */
    .main { background-color: #010408; }
    
    /* Metrics Styling */
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.05);
        border: 1px solid #00ffff;
        border-radius: 10px;
    }
    
    /* Text Colors */
    h1, h2, h3, p, span, label, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

# 3. BRANDING HEADER
if os.path.exists("reqxi.jpg"):
    st.image("reqxi.jpg", width=500)
else:
    st.title("REQXI PRO")

# 4. NAVIGATION TABS
t1, t2, t3, t4 = st.tabs(["📊 Intelligence", "🚀 Careers", "🤝 Donations", "🛡️ Risk Monitor"])

with t1:
    st.subheader("🌐 Global Environment & Air Quality")
    
    def get_full_data(lat, lon):
        try:
            # Combined Weather API
            w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m&temperature_unit=fahrenheit"
            w = requests.get(w_url, timeout=5).json()['current']
            # Air Quality API
            a_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi"
            a = requests.get(a_url, timeout=5).json()['current']
            return {"t": f"{w['temperature_2m']}°F", "h": f"{w['relative_humidity_2m']}%", "aqi": a['us_aqi'], "aq_raw": a['us_aqi']}
        except: return {"t": "--", "h": "--", "aqi": "--", "aq_raw": 0}

    # Cities and Coords for the 10 States
    cities = {
        "Miami, FL": (25.76, -80.19), "Fort Worth, TX": (32.75, -97.33), 
        "Charlotte, NC": (35.22, -80.84), "New York, NY": (40.71, -74.00),
        "Chicago, IL": (41.87, -87.62), "Los Angeles, CA": (34.05, -118.24),
        "Las Vegas, NV": (36.17, -115.13), "Charleston, SC": (32.77, -79.93),
        "Atlanta, GA": (33.74, -84.38), "Seattle, WA": (47.60, -122.33)
    }

    # Process live data for the map and list
    map_data = []
    for city, coords in cities.items():
        d = get_full_data(coords[0], coords[1])
        # Data for the list view
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f"**{city}**")
        col2.metric("Temp", d['t'])
        col3.metric("Humidity", d['h'])
        col4.metric("Air Quality (AQI)", d['aqi'])
        st.divider()
        
        # Data for the dynamic map overlay
        map_data.append({"name": city, "lat": coords[0], "lon": coords[1], "aqi": d['aq_raw']})

    # 5. GEOSPATIAL MAP (The Request)
    st.markdown("### 🗺️ Dynamic US Risk Visualization")
    df_map = pd.DataFrame(map_data)
    
    # Render map using Pydeck for that "Cyan Bloomberg" style
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v11', # Deep dark base
        initial_view_state=pdk.ViewState(
            latitude=39.8283,
            longitude=-98.5795,
            zoom=3, # View North America
            pitch=50,
        ),
        layers=[
            # Cyan Bar Layer for AQI
            pdk.Layer(
               'ColumnLayer',
               data=df_map,
               get_position=['lon', 'lat'],
               get_elevation='aqi',
               elevation_scale=1000,
               radius=25000,
               get_fill_color=[0, 255, 255, 180], # Cyan: [R, G, B, Alpha]
               pickable=True,
               auto_highlight=True,
            ),
            # Cyan Text Labels
            pdk.Layer(
                'TextLayer',
                data=df_map,
                get_position=['lon', 'lat'],
                get_text='name',
                get_color=[0, 255, 255, 255],
                get_size=16,
                get_angle=0,
                # Align text above the columns
                get_pixel_offset=[0, -30],
            ),
        ],
        tooltip={"text": "{name}\nAQI: {aqi}"} # Show data on hover
    ))
    st.caption("Confidentail // Geospatial Air & Thermal Risk Data")

with t2:
    st.subheader("🚀 Careers")
    st.markdown("### **Senior Data Engineer (L3)**")
    st.write("**Pay:** Based on Experience")
    st.markdown("**Apply:** justin@jbs-t.com")

with t3:
    st.subheader("🤝 Support Research")
    st.progress(0.65)
    if os.path.exists("$jbstpay.svg"):
        st.image("$jbstpay.svg", width=250)
    st.markdown('<a href="https://cash.app/$jbstpay" target="_blank"><button style="background-color:#00ffff; color:black; border:none; padding:12px 24px; border-radius:5px; font-weight:bold; cursor:pointer;">💸 Donate via Cash App</button></a>', unsafe_allow_html=True)

with t4:
    st.subheader("🛡️ Regional Resilience Monitor")
    st.table(pd.DataFrame({
        "Hub": ["Houston", "Fort Worth", "LA", "NYC"],
        "Grid": ["Critical", "High", "Watch", "High"],
        "Threat": ["Hurricane", "Storm", "Seismic", "Age"]
    }))

st.divider()
st.caption("Confidential // REQXI IT Consulting & Data Research")

import streamlit as st
import pandas as pd
import requests
import pydeck as pdk
import numpy as np

# 1. PAGE CONFIG
st.set_page_config(page_title="REQXI PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. THE "CANVA GLOW" CSS
st.markdown("""
    <style>
    /* Dark Background matching your image */
    .main { background-color: #01080e; }
    
    /* Glowing Cyan Cards */
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.03);
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.15);
        border-radius: 10px;
        padding: 15px;
    }
    
    /* Text Colors */
    [data-testid="stMetricLabel"] > div { color: #00ffff !important; font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: 2px; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] { background-color: #01080e; border-right: 1px solid #00ffff; }
    </style>
    """, unsafe_allow_html=True)

# 3. LIVE WEATHER (Fahrenheit)
def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=fahrenheit"
    data = requests.get(url).json()
    return data['current_weather']

# 4. DISPLAY THE CANVA IMAGE (The Hero)
# This puts your design at the very top
st.image("dashboardrex.jpg", use_container_width=True)

st.divider()

# 5. LIVE DATA SECTION
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg Load", "420 GW", "+1.2%")
with col2:
    st.metric("Grid Price", "$73.20", "-4%")
with col3:
    # Live Weather integrated into a card
    w = get_weather(32.75, -97.33) # Tarrant County
    st.metric("Local Temp", f"{w['temperature']}°F", "LIVE")

# 6. LIVE GEOSPATIAL MAP (Matching the Canva Map style)
st.subheader("🌐 Network Propagation Feed")
map_data = pd.DataFrame(np.random.randn(100, 2) / [12, 18] + [38, -98], columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(latitude=38, longitude=-98, zoom=3, pitch=45),
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=map_data,
            get_position="[lon, lat]",
            color_range=[[0, 255, 255, 50], [0, 255, 255, 150], [0, 255, 255, 255]]
        ),
    ],
))

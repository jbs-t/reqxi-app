import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import requests

# 1. PAGE CONFIGURATION (Million-Dollar Look)
st.set_page_config(
    page_title="REQXI PRO | Grid Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CUSTOM CSS (Stealth Mode / North America Blue)
st.markdown("""
    <style>
    .main { background-color: #050505; }
    div[data-testid="stMetricValue"] { color: #00ffcc; font-family: 'Courier New', monospace; font-weight: bold; }
    .stMetric { background: #111; border-radius: 10px; border: 1px solid #222; padding: 15px; }
    h1, h2, h3 { color: #ffffff; font-family: 'Inter', sans-serif; }
    .stTable { background-color: #111; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. REQXI WEATHER ENGINE (Live Data - No Key Needed)
def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url).json()
        return response['current_weather']
    except:
        return {"temperature": "N/A", "windspeed": "N/A"}

# 4. SIDEBAR - CONTROL PANEL
st.sidebar.title("⚡ REQXI CONTROL")
st.sidebar.caption("NORTH AMERICA OPERATIONS")
hub = st.sidebar.selectbox("Select Regional Hub", ["Fort Worth", "New York", "Toronto", "Los Angeles"])

# Coordinate Mapping
coords = {"Fort Worth": (32.75, -97.33), "New York": (40.71, -74.00), "Toronto": (43.65, -79.38), "Los Angeles": (34.05, -118.24)}
lat, lon = coords[hub]
weather = get_weather(lat, lon)

st.sidebar.divider()
st.sidebar.subheader(f"Live Weather: {hub}")
st.sidebar.metric("TEMP", f"{weather['temperature']}°C")
st.sidebar.write(f"Wind Speed: {weather['windspeed']} km/h")
st.sidebar.button("Refresh API Feed")

# 5. HEADER & TOP METRICS
st.title("⚡ REQXI | GRID INTELLIGENCE")
st.caption("SECURE TERMINAL // NORTH AMERICA DATA CLUSTER")

col1, col2, col3 = st.columns(3)
col1.metric("AVG LOAD (GW)", "428.5", "+1.2%")
col2.metric("RENEWABLE MIX", "31.2%", "OPTIMIZED")
col3.metric("GRID STABILITY", "99.98%", "SECURE")

st.divider()

# 6. ESRI-STYLE 3D HEATMAP (Simulation while waiting for EIA Key)
st.subheader("🌐 Continental Demand Distribution (3D)")

# Generate 150 points across North America
map_data = pd.DataFrame(
    np.random.randn(150, 2) / [8, 12] + [39.82, -98.57],
    columns=['lat', 'lon']
)

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(latitude=38, longitude=-98, zoom=3, pitch=45),
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=map_data,
            get_position="[lon, lat]",
            radius_pixels=50,
            intensity=1,
            threshold=0.2,
            color_range=[[0, 255, 204, 50], [0, 255, 204, 150], [0, 255, 204, 255]]
        ),
    ],
))

# 7. SERVICE TIERS (For Word Doc Proposals)
st.divider()
st.subheader("🚀 REQXI GO PRO SERVICE TIERS")

tier_data = {
    "Plan": ["REQXI Lite", "REQXI Go Pro", "REQXI Enterprise"],
    "Price": ["$0 /mo", "$49.99 /mo", "$499.00 /mo"],
    "Deliverables": ["Regional Maps & Briefs", "Live EIA API + 3D Heatmaps", "AI Predictive Analytics & Routing"]
}
st.table(pd.DataFrame(tier_data))

st.caption("Confidential // REQXI IT Consulting & Data Research Services")

import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

# 1. High-End Page Setup
st.set_page_config(page_title="REQXI | North America", layout="wide", initial_sidebar_state="collapsed")

# 2. Custom CSS: Stealth Mode Styling
st.markdown("""
    <style>
    .main { background-color: #050505; }
    div[data-testid="stMetricValue"] { color: #00ffcc; font-family: 'Courier New', monospace; }
    .stMetric { background: #111; border-radius: 12px; border: 1px solid #222; padding: 15px; }
    h1, h2, h3 { color: #ffffff; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 3. Branding Header
st.title("⚡ REQXI PRO")
st.caption("GRID INTELLIGENCE // NORTH AMERICA DATA FEED")

# 4. Metrics Row
m1, m2, m3 = st.columns(3)
m1.metric("AVG LOAD", "420 GW", "+1.4%")
m2.metric("RENEWABLES", "28.5%", "-0.2%")
m3.metric("GRID STABILITY", "99.9%", "OPTIMIZED")

st.divider()

# 5. ESRI-STYLE HEATMAP (Synthetic Data for Demo)
st.subheader("🌐 Continental Demand Heatmap")

# Generating 100 points across the US/Canada for the "Wow" factor
df = pd.DataFrame(
    np.random.randn(100, 2) / [10, 15] + [37.09, -95.71],
    columns=['lat', 'lon']
)

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=37.09, longitude=-95.71, zoom=3, pitch=50
    ),
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=df,
            get_position="[lon, lat]",
            radius_pixels=60,
            intensity=1,
            threshold=0.3,
            color_range=[
                [0, 255, 204, 50],   # Reqxi Cyan
                [0, 255, 204, 150],
                [0, 255, 204, 255]
            ]
        ),
    ],
))

# 6. Pricing Section
st.divider()
st.subheader("🚀 REQXI GO PRO PLANS")
p1, p2, p3 = st.columns(3)
with p1:
    st.info("**LITE**\n\n$0/mo\n\nBasic Regional View")
with p2:
    st.success("**GO PRO**\n\n$49.99/mo\n\nLive EIA API + 3D Maps")
with p3:
    st.warning("**ENTERPRISE**\n\n$499/mo\n\nPredictive AI + Custom Nodes")

import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config
st.set_page_config(page_title="REQXI | North America", page_icon="⚡", layout="wide")

# 2. Custom "Pro" Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #374151; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    h1 { color: #58a6ff; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("⚡ REQXI | GRID INTELLIGENCE")
st.caption("NORTH AMERICA OPERATIONS // SECURE DATA FEED")
st.divider()

# 4. KPI Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="EST. SAVINGS (MTD)", value="$24,812", delta="+8.2%")
with col2:
    st.metric(label="NETWORK UPTIME", value="99.98%", delta="0.02%")
with col3:
    st.metric(label="ACTIVE COURIER NODES", value="142", delta="12")

st.divider()

# 5. Regional Analytics
st.subheader("📊 Continental Load Distribution")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Eastern Grid', 'Western Grid', 'Texas ERCOT'])
st.area_chart(chart_data)

st.sidebar.title("Control Panel")
st.sidebar.info("IT Consulting | Courier | Analytics")
st.sidebar.button("Refresh Feed")

import streamlit as st
import pandas as pd
import requests

# 1. PAGE SETUP (The Foundation)
st.set_page_config(
    page_title="REQXI Grid Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed" # Starts collapsed for full-screen feel
)

# 2. THE REQXI "STEALTH" THEME (Million-Dollar Styling)
# This CSS matches the deep background and neon text from your new image.
st.markdown("""
    <style>
    /* 1. The Deep Background */
    .main { background-color: #010408; }
    
    /* 2. Overriding standard text to be Neon Cyan */
    h1, h2, h3, p, label, .stMarkdown, .stText, [data-testid="stHeader"] { 
        color: #00ffff !important; 
        font-family: 'SF Pro Display', 'Inter', sans-serif;
    }
    
    /* 3. High-End Metric Card Styling (Neon Cyan Borders) */
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.03); /* Subtle background glow */
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.2);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
    }
    
    /* Metric label styling */
    [data-testid="stMetricLabel"] > div { color: #00ffff !important; font-size: 1rem; }
    /* Metric value styling */
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-size: 2rem; font-weight: bold;}
    
    /* 4. Selectbox / Dropdown Styling (making them stealthy) */
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #0d1117;
        border: 1px solid #00ffff;
        color: #00ffff;
    }
    
    /* 5. Custom Button Styling */
    .stButton>button {
        background-color: #010408;
        color: #00ffff;
        border: 1px solid #00ffff;
        border-radius: 5px;
        font-size: 1rem;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: rgba(0, 255, 255, 0.1);
        border: 1px solid #00ffff;
    }

    /* 6. Clean Divider */
    hr { border-color: #00ffff; opacity: 0.3; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { background-color: #010408; border-right: 1px solid #00ffff; }
    </style>
    """, unsafe_allow_html=True)

# 3. WEATHER ENGINE (Fahrenheit, Live Open-Meteo)
def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=fahrenheit"
    try:
        response = requests.get(url).json()
        return response['current_weather']
    except:
        return {"temperature": "N/A", "windspeed": "N/A"}

# 4. MAIN HEADER (The Hero)
# I am assuming your new image is uploaded as dashboardrex.jpg
st.markdown("<h1 style='text-align: center; color: #00ffff;'>REQXI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ffffff;'>NORTH AMERICA DATA FEED</p>", unsafe_allow_html=True)

try:
    st.image("dashboardrex.jpg", use_container_width=True)
except:
    st.info("⚠️ Action Required: Upload your new dashboard image to GitHub and name it 'dashboardrex.jpg'. Only then will it appear here.")

st.divider()

# 5. SELECT HUB & LIVE DATA (Fahrenheit Weather)
st.subheader("⚡ Control Hub")
hub_choice = st.selectbox(
    "Select Active Sector", 
    ["Fort Worth (Tarrant)", "New York (NYC)", "Los Angeles (LAX)"]
)

# Hub Coordinates (Lat, Lon)
coords = {
    "Fort Worth (Tarrant)": (32.75, -97.33), 
    "New York (NYC)": (40.71, -74.00), 
    "Los Angeles (LAX)": (34.05, -118.24)
}

lat, lon = coords[hub_choice]
weather = get_weather(lat, lon)

# 6. LIVE METRIC CARDS (Matching your Design)
st.subheader("📊 Live Grid Analytics (North America Cluster)")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Avg Load", "420 GW", "+1.2%")
with col2:
    # Live Fahrenheit Weather
    st.metric("Sector Temp", f"{weather['temperature']}°F", f"{hub_choice}")
with col3:
    st.metric("Grid Stability", "99.99%", "SECURE")

st.divider()

# 7. FOOTER VISUAL
st.markdown("<h1 style='text-align: center; color: #00ffff;'>REQXI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ffffff;'>IT CONSULTING & DATA RESEARCH</p>", unsafe_allow_html=True)

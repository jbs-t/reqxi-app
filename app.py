# 2. THEME & BRANDING REMOVAL (Deep Black + Neon Cyan)
st.markdown("""
    <style>
    /* HIDES TOP BAR, HAMBURGER MENU, AND DEPLOY BUTTON */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
    
    /* YOUR EXISTING THEME */
    .main { background-color: #010408; }
    [data-testid="stMetric"] {
        background: rgba(0, 255, 255, 0.03);
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 10px rgba(0, 255, 255, 0.1);
        border-radius: 10px;
    }
    h1, h2, h3, p, [data-testid="stMetricLabel"] > div { color: #00ffff !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    .footer { text-align: center; color: #00ffff; padding: 30px; opacity: 0.6; }
    
    /* REMOVES TOP MARGIN TO BRING CONTENT TO THE TOP */
    .block-container { padding-top: 0rem; }
    </style>
    """, unsafe_allow_html=True)

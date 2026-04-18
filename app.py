import streamlit as st

st.set_page_config(page_title="REQXI", page_icon="⚡")
st.title("REQXI | Grid Intelligence")

st.metric(label="EST. MONTHLY SAVINGS", value="$612.45", delta="12%")

st.write("### Tarrant County Energy Monitoring")
st.bar_chart([10, 15, 7, 22, 18, 12]) # Sample data for your demo

st.info("Private Beta: Digitizing the Grid, Owning the Flow.")

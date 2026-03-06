import streamlit as st
import pandas as pd
from io import BytesIO
import streamlit as st

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.set_page_config(page_title="STI Calculator", layout="wide")

st.title("💰 STI Calculator Dashboard")

# --- Sidebar Inputs ---
st.header("Manual Calculation")

group = st.selectbox("Bonus Group", ["1", "2", "3", "4"])
salary = st.number_input("Annual Salary", min_value = 0.0, step = 0.0001, format = "%.4f")
bonus = st.number_input("Bonus Percentage", min_value = 0.0, step = 0.0001, format = "%.4f")

multipliers = {
    "1": 0.1,
    "2": 0.12,
    "3": 0.14,
    "4": 0.18
}

# --- Manual Calculation ---
if st.button("Calculate STI"):
    sr_multiplier = multipliers[group]
    sti = (salary * bonus) * sr_multiplier
    st.success(f"STI = kr{sti:,.2f}", layout = "wide")

st.divider()











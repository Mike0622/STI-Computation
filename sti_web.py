import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="STI Calculator", layout="wide")

st.title("💰 STI Calculator Dashboard")

# --- Sidebar Inputs ---
st.center.header("Manual Calculation")

group = st.center.selectbox("Bonus Group", ["1", "2", "3", "4"])
salary = st.center.number_input("Annual Salary", min_value = 0.0, step = 0.0001, format = "%.4f")
bonus = st.center.number_input("Bonus Percentage", min_value = 0.0, step = 0.0001, format = "%.4f")

multipliers = {
    "1": 0.1,
    "2": 0.12,
    "3": 0.14,
    "4": 0.18
}

# --- Manual Calculation ---
if st.center.button("Calculate STI"):
    sr_multiplier = multipliers[group]
    sti = (salary * bonus) * sr_multiplier
    st.center.success(f"STI = ${sti:,.4f}")

st.divider()






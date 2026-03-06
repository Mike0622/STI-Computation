import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="STI Calculator", layout="wide")

st.title("💰 STI Calculator Dashboard")

# --- Sidebar Inputs ---
st.sidebar.header("Manual Calculation")

group = st.sidebar.selectbox("Bonus Group", ["1", "2", "3", "4"])
salary = st.sidebar.number_input("Annual Salary")
bonus = st.sidebar.number_input("Bonus Percentage")

multipliers = {
    "1": 0.1,
    "2": 0.12,
    "3": 0.14,
    "4": 0.18
}

# --- Manual Calculation ---
if st.sidebar.button("Calculate STI"):
    sr_multiplier = multipliers[group]
    sti = (salary * bonus) * sr_multiplier
    st.sidebar.success(f"STI = ${sti:,.2f}")

st.divider()

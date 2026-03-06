import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="STI Calculator", layout="wide")

st.title("💰 STI Calculator Dashboard")

# --- Sidebar Inputs ---
st.sidebar.header("Manual Calculation")

group = st.sidebar.selectbox("Bonus Group", ["1", "2", "3", "4"])
salary = st.sidebar.number_input("Annual Salary", min_value=0.000)
bonus = st.sidebar.number_input("Bonus Percentage", min_value=0.000)

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

# --- Excel Upload ---
st.header("📂 Upload Excel File for Batch Calculation")
uploaded_file = st.file_uploader("Drag and drop your Excel file here", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Automatically compute STI
    df["STI"] = (df["annualSalary"] * df["bonus"]) * df["srMultiplier"]

    st.subheader("✅ Computed Results")
    st.dataframe(df, use_container_width=True)

    # Allow down

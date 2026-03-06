import streamlit as st
import pandas as pd

st.title("STI Calculator")

# Inputs
group = st.selectbox("Bonus Group", ["1", "2", "3", "4"])
salary = st.number_input("Annual Salary", min_value=0.000)
bonus = st.number_input("Bonus Percentage", min_value=0.000)

multipliers = {
    "1": 0.1,
    "2": 0.12,
    "3": 0.14,
    "4": 0.18
}

if st.button("Calculate STI"):
    sr_multiplier = multipliers[group]
    sti = (salary * bonus) * sr_multiplier
    st.success(f"STI = {sti:,.2f}")

st.divider()

# Excel upload
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df["STI"] = (df["annualSalary"] * df["bonus"]) * df["srMultiplier"]

    st.write("Results")
    st.dataframe(df)

    st.download_button(
        "Download Results",
        df.to_excel("sti_results.xlsx", index=False),
        file_name="sti_results.xlsx"
    )


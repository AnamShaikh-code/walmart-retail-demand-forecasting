import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# Load the trained model
# -----------------------------
model = joblib.load("final_rf_model.pkl")

# -----------------------------
# App title
# -----------------------------
st.title("Walmart Retail Demand Forecasting")

st.write(
    "Enter the store information below to predict Walmart weekly sales."
)

# -----------------------------
# User inputs
# -----------------------------

store = st.number_input(
    "Store",
    min_value=1,
    max_value=45,
    value=1,
    step=1
)

dept = st.number_input(
    "Department",
    min_value=1,
    max_value=99,
    value=1,
    step=1
)

week = st.number_input(
    "Week",
    min_value=1,
    max_value=52,
    value=1,
    step=1
)

size = st.number_input(
    "Store Size",
    min_value=0.0,
    max_value=300000.0,
    value=150000.0,
    step=1000.0
)

store_type = st.selectbox(
    "Store Type",
    options=["A", "B", "C"]
)

is_holiday = st.selectbox(
    "Is Holiday?",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# -----------------------------
# Hidden model features
# -----------------------------
# These features are not shown to the user,
# but the trained model still requires them.

temperature = 60.0
fuel_price = 3.0

markdown1 = 0.0
markdown2 = 0.0
markdown3 = 0.0
markdown4 = 0.0
markdown5 = 0.0

cpi = 200.0
unemployment = 7.0

year = 2012
month = 1
quarter = 1

# Convert Store Type to one-hot encoding
type_b = 1 if store_type == "B" else 0
type_c = 1 if store_type == "C" else 0

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Weekly Sales"):

    input_data = pd.DataFrame([[
        store,
        dept,
        is_holiday,
        temperature,
        fuel_price,
        markdown1,
        markdown2,
        markdown3,
        markdown4,
        markdown5,
        cpi,
        unemployment,
        size,
        year,
        month,
        week,
        quarter,
        type_b,
        type_c
    ]], columns=[
        "Store",
        "Dept",
        "IsHoliday",
        "Temperature",
        "Fuel_Price",
        "MarkDown1",
        "MarkDown2",
        "MarkDown3",
        "MarkDown4",
        "MarkDown5",
        "CPI",
        "Unemployment",
        "Size",
        "Year",
        "Month",
        "Week",
        "Quarter",
        "Type_B",
        "Type_C"
    ])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Weekly Sales: ${prediction[0]:,.2f}"
    )
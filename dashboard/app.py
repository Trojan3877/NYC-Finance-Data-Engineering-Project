import streamlit as st
import requests

st.set_page_config(page_title="NYC Finance ML Dashboard", layout="centered")

st.title("📊 NYC Finance ML Prediction Dashboard")

st.markdown("Enter financial features to generate a real-time prediction.")

feature_1 = st.number_input("Feature 1", value=0.0)
feature_2 = st.number_input("Feature 2", value=0.0)
feature_3 = st.number_input("Feature 3", value=0.0)

if st.button("Run Prediction"):
    payload = {
        "features": [feature_1, feature_2, feature_3]
    }

    response = requests.post(
        "http://localhost:8000/predict",
        json=payload
    )

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicted Value: **{prediction:.2f}**")
    else:
        st.error("Prediction failed")

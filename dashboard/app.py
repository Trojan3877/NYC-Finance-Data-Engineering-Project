import os

import pandas as pd
import streamlit as st

st.title("NYC Finance Data Dashboard")

DATA_PATH = os.environ.get(
    "PROCESSED_DATA_PATH",
    os.path.join("data", "processed", "nyc_finance_processed.csv"),
)

if not os.path.exists(DATA_PATH):
    st.warning(
        f"Processed data file not found at `{DATA_PATH}`. "
        "Run the ETL pipeline first to generate the data."
    )
else:
    df = pd.read_csv(DATA_PATH)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if "stock_price" in df.columns and "volume" in df.columns:
        st.subheader("Stock Price & Volume")
        st.line_chart(df[["stock_price", "volume"]])
    elif len(numeric_cols) >= 2:
        st.subheader("Numeric Columns")
        st.line_chart(df[numeric_cols[:2]])
    elif len(numeric_cols) == 1:
        st.subheader(numeric_cols[0])
        st.line_chart(df[numeric_cols])
    else:
        st.info("No numeric columns available to chart.")

    st.subheader("Raw Data")
    st.dataframe(df.head(50))

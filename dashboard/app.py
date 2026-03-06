import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/nyc_finance_processed.csv")
st.title("NYC Finance Data Dashboard")
st.line_chart(df[["stock_price","volume"]])

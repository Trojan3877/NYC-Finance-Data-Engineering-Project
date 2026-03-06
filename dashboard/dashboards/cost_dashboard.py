import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "Service": ["EKS","S3","Kafka","Snowflake"],
    "Monthly Cost ($)": [420, 150, 310, 890]
})

st.title("Cloud Cost Monitoring")
st.bar_chart(data.set_index("Service"))

import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_URL = "http://api:8000"

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

st.title("Healthcare Data Dashboard")

#sidebar filters
limit = st.sidebar.slider("Number of Records", 10, 500, 100)

#Fetch data
response = requests.get(f"{API_URL}/health?limit={limit}")

if response.status_code !=200:
    st.error(f"API Error: {response.status_code}")
    st.stop()

data = response.json()

if not isinstance(data, list):
    st.error("Unexpected API response format")
    st.stop()

df = pd.DataFrame(data)

if df.empty:
    st.warning("No data available.")
    st.stop()

#Summary metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Records Loaded", len(df))
col2.metric("Average Diabetes_012", round(df["Diabetes_012"].mean(), 2))
col3.metric("HighChol", f"{round(df['HighChol'].mean()*100, 2)}%")

st.divider()

#Charts
st.subheader("HighChol Distribution")
fig1 = px.histogram(df, x="HighChol")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Diabetes_012 vs BMI")
fig2 = px.scatter(df, x="Diabetes_012", y="bmi", color="HighChol")
st.plotly_chart(fig2, use_container_width=True)




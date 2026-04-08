import streamlit as st
import pandas as pd

# Title
st.title("EDA Dashboard: Odonata Colour Change")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=";")

    # Show raw data
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Basic info
    st.subheader("Dataset Info")
    buffer = []
    df.info(buf=buffer)
    st.text(str(buffer))

    # Describe
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Missing values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Optional: column selection
    st.subheader("Select Column to Explore")
    column = st.selectbox("Choose a column", df.columns)

    if df[column].dtype != "object":
        st.line_chart(df[column])
    else:
        st.write(df[column].value_counts())

else:
    st.info("Please upload a CSV file to begin.")

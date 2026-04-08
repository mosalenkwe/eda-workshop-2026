import streamlit as st
import pandas as pd
import io

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="EDA Dashboard", layout="wide")

# -------------------------------
# Title
# -------------------------------
st.title("EDA Dashboard: Odonata Colour Change 🐉")
st.write("Upload your dataset and explore it interactively.")

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep=";")

        # -------------------------------
        # Data Preview
        # -------------------------------
        st.subheader("📊 Dataset Preview")
        st.dataframe(df.head())

        # -------------------------------
        # Dataset Info (FIXED)
        # -------------------------------
        st.subheader("📌 Dataset Info")
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        st.code(info_str)

        # -------------------------------
        # Summary Statistics
        # -------------------------------
        st.subheader("📈 Summary Statistics")
        st.write(df.describe())

        # -------------------------------
        # Missing Values
        # -------------------------------
        st.subheader("⚠️ Missing Values")
        missing = df.isnull().sum()
        st.write(missing)

        # -------------------------------
        # Column Exploration
        # -------------------------------
        st.subheader("🔍 Explore a Column")
        column = st.selectbox("Select a column", df.columns)

        if df[column].dtype != "object":
            st.write(f"### Distribution of {column}")
            st.line_chart(df[column])
        else:
            st.write(f"### Value Counts for {column}")
            st.write(df[column].value_counts())

    except Exception as e:
        st.error(f"Error loading file: {e}")

else:
    st.info("👆 Please upload a CSV file to begin.")

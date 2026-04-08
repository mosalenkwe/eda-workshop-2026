import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

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
        # Dataset Info
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
        st.write(df.isnull().sum())

        # -------------------------------
        # Correlation Heatmap
        # -------------------------------
        st.subheader("📊 Correlation Matrix")

        numeric_df = df.select_dtypes(include=['number'])

        if not numeric_df.empty:
            corr = numeric_df.corr()

            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

            st.pyplot(fig)
        else:
            st.warning("No numeric columns available for correlation analysis.")

        # -------------------------------
        # Column Exploration
        # -------------------------------
        st.subheader("🔍 Explore a Column")
        column = st.selectbox("Select a column", df.columns)

        fig, ax = plt.subplots()

        if df[column].dtype != "object":
            sns.histplot(df[column], kde=True, ax=ax)
            st.pyplot(fig)
        else:
            sns.countplot(x=df[column], ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error loading file: {e}")

else:
    st.info("👆 Please upload a CSV file to begin.")

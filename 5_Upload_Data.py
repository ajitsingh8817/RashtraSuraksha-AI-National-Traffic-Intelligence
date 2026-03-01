import streamlit as st
import pandas as pd

st.title("📤 Upload Traffic Data")

file=st.file_uploader("Upload CSV",type=["csv"])

if file:
    df=pd.read_csv(file)
    st.dataframe(df)
    st.success("Data Loaded Successfully")
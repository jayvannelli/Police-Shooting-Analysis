import streamlit as st

from src import data

df = data.get_dataframe()

st.write(df)
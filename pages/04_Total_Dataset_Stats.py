import streamlit as st

from src import data, helpers, displays

years = [2015,2016,2017,2018,2019,2020,2021,2022]

st.header("Total Dataset Statistics")

df = data.get_dataframe()

victims_by_race = helpers.get_victims_race_for_each_year(df, years)
displays.plot_victims_by_race_grouped(victims_by_race)



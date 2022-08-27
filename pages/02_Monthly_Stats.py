import streamlit as st

from src import data, displays, monthly, helpers

months = [1,2,3,4,5,6,7,8,9,10,11,12]

st.header("Monthly US Police Shooting Statistics")
select_year = st.selectbox("Select year to analyze", [2015,2016,2017,2018,2019,2020,2021,2022])

df = data.get_dataframe()

this_year = data.get_specific_year_dataframe(df=df, year=select_year)

col1, col2 = st.columns(2)
with col1:
    monthly_shootings = monthly.get_monthly_shooting_counts_for_specific_year(df=this_year, year=select_year)
    displays.display_monthly_shootings_in_year(monthly_shootings, year=str(select_year))
with col2:
    monthly_victim_by_race = helpers.get_victims_race_by_month_in_specific_year(df, months, select_year)
    displays.plot_victims_by_race_grouped_monthly(monthly_victim_by_race, select_year)
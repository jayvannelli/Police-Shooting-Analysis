import streamlit as st

from src import data, helpers

st.set_page_config(layout="wide")

st.header("Display the Location of US Police Shootings for a Given Year")
select_year = st.selectbox("Select year to analyze", [2015,2016,2017,2018,2019,2020,2021,2022])

df = data.get_dataframe()

given_year_df = data.get_specific_year_dataframe(df=df, year=select_year)
lat_lon = helpers.get_lat_lon_df(police_shootings_df=given_year_df)

st.subheader("Interactive Map of Police Shootings for a given year")
st.map(lat_lon)

st.write("---")

st.subheader(f"Cities With The Most Police Shootings in {select_year}")
top_x_vals = st.number_input("Display the top ___ cities", min_value=2, max_value=25, step=1)

shootings_by_city_dict = helpers.get_shootings_by_city(given_year_df)
shootings_by_city_descending = helpers.sort_descending(data=shootings_by_city_dict, top_x_values=top_x_vals)

counter = 1
for key, val in shootings_by_city_descending.items():
    st.subheader(f"{counter}: {key} = {val}")
    
    counter += 1

st.write("---")

st.subheader("Full Dataframe")
st.write(given_year_df)
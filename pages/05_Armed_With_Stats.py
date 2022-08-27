import streamlit as st

from src import data, displays, helpers

st.header("US Police Shootings - Suspect Was Armed With ____ During The Shooting")

df = data.get_dataframe()
col1, col2 = st.columns(2)
with col1:
    dashboard_selection = st.selectbox("Select how to display data", ["Standard Text", "Bar Chart"])
with col2:
    select_year = st.selectbox("Select year to analyze", [2015,2016,2017,2018,2019,2020,2021,2022])

specific_year_df = data.get_specific_year_dataframe(df=df, year=select_year)
armed_stats = helpers.get_armed_stats_dictionary(police_shootings=specific_year_df)

if dashboard_selection == "Standard Text":
    col1, col2 = st.columns(2)
    with col1:
        for i in armed_stats.keys():
            st.subheader(i)
    with col2:
        for i in armed_stats.values():
            st.subheader(i)
else:
    st.write("---")

    display_x_values = st.number_input("Display the top ____ values", 3, len(armed_stats), step=1)
    armed_stats_descending = helpers.sort_descending(data=armed_stats, top_x_values=display_x_values)

    displays.plot_armed_stats(armed_stats_descending, select_year)
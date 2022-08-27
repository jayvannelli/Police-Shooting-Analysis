import streamlit as st

from src import data, displays

st.header("Taking a look at US Police Shootings over the years from 2015 to 2022")
select_year = st.selectbox("Select year to analyze", [2015,2016,2017,2018,2019,2020,2021,2022])

df = data.get_dataframe()


this_year_df = data.get_specific_year_dataframe(df=df, year=select_year)

if select_year == 2015:
    st.error("You must choose 2016 or above to get previous year stats")
else:
    last_year_df = data.get_specific_year_dataframe(df=df, year=select_year-1)

displays.display_yoy_metrics(current_year_df=this_year_df, former_year_df=last_year_df)

st.write('---')

col1, col2 = st.columns(2)
with col1:
    st.subheader("This Year Full Dataframe")
    st.write(this_year_df)
with col2:
    st.subheader("Last Year Full Dataframe")
    st.write(last_year_df)
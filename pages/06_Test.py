import streamlit as st

from src import data

df = data.get_dataframe()

select_year = st.selectbox("Select year to analyze", [2015,2016,2017,2018,2019,2020,2021,2022])
select_month = st.selectbox("Select month within year to analyze", [1,2,3,4,5,6,7,8,9,10,11,12])

specific_year_df = data.get_specific_year_dataframe(df=df, year=select_year)

specific_month_df = data.get_specific_month_dataframe(df=df, current_month=select_month, next_month=select_month+1, year=select_year)

range_of_years_df = data.get_multiple_years_dataframe(df=df, start_year=select_year, end_year=select_year+3)

#st.write(range_of_years_df)
#st.write(specific_month_df)
#st.write(specific_year_df)

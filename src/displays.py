import matplotlib.pyplot as plt
import streamlit as st

import pandas as pd

def plot_armed_stats(armed_statistics, year):
    """
    This function plots US Police Shootings and what the suspect was
    armed with during the shooting for a given year. To plot this data,
    a bar chart is used for each item and is sorted in a descending order.
    """
    armed_with = list(armed_statistics.keys())
    values = list(armed_statistics.values())
    
    plt.bar(range(len(armed_statistics)), values, tick_label=armed_with)
    plt.xticks(rotation=45)
    plt.ylabel("Number of Shootings")
    plt.xlabel("Suspect Was Armed With ____ During Shooting")
    plt.title(f"{year} Armed Shooting Stats")
    st.pyplot(plt)

def display_yoy_metrics(current_year_df, former_year_df):
    """
    This function gets the year over year change for specific categories
    shown below and displays them through the streamlit metrics component.

    Parameters : current_year_df = the full police shootings dataframe for
                                   the current year.
                 former_year_df = the full police shootings dataframe for
                                   the previous year.
    
    This function does not have any return value, and instead displays the 
    metrics directly to the dashboard.
    """

    quantity_of_shooting_change = len(current_year_df.index) - len(former_year_df.index)

    # Get data for shootings that occured where the police were wearing body camera
    this_year_bodycam_df = current_year_df[current_year_df['body_camera']==True]
    last_year_bodycam_df = former_year_df[former_year_df['body_camera']==True]
    change_in_bodycam = len(this_year_bodycam_df) - len(last_year_bodycam_df)

    # Get data for shootings that involved a suspect with their race classified as "White"
    white_race_this_year_df = current_year_df[current_year_df['race']=="W"]
    white_race_last_year_df = former_year_df[former_year_df['race']=="W"]
    change_in_white_race_shootings = len(white_race_this_year_df.index) - len(white_race_last_year_df.index)

    # Get data for shootings that involved a suspect with their race classified as "Black"
    black_race_this_year_df = current_year_df[current_year_df['race']=="B"]
    black_race_last_year_df = former_year_df[former_year_df['race']=="B"]
    change_in_black_race_shootings = len(black_race_this_year_df.index) - len(black_race_last_year_df.index)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Quantity of Shootings", value=len(current_year_df), delta=quantity_of_shooting_change)
    with col2:
        st.metric(label="Shootings w Body-Camera", value=len(this_year_bodycam_df), delta=change_in_bodycam)
    with col3:
        st.metric(label="Shootings w white victim", value=len(white_race_this_year_df), delta=change_in_white_race_shootings)
    with col4:
        st.metric(label="Shootings w black victim", value=len(black_race_this_year_df), delta=change_in_black_race_shootings)

def plot_average_ages_of_victims(average_age_per_year_dictionary):
    """
    This function will generate a line chart of the average age of police shooting victims
    over time.

    Parameter: average_age_per_year_dictionary = a dictionary containing the average age of 
                                                 shooting victims per year.
    """
    years = list(average_age_per_year_dictionary.keys())
    values = list(average_age_per_year_dictionary.values())
    
    plt.plot(years, values)
    plt.xticks(rotation=45)
    plt.ylabel("Age (Years)")
    plt.xlabel("Year")
    plt.title("Average Age of Shooting Victims 2015-2022")
    st.pyplot(plt)

def plot_victims_by_race_grouped(victims_by_race_dictionary):
    df = pd.DataFrame(victims_by_race_dictionary)
    df = df.transpose()
    
    df.plot(kind='bar')
    plt.xlabel("Year")
    plt.xticks(rotation=45)
    plt.ylabel("Quantity of Shootings")
    plt.title("Police Shootings by Race From 2015-2022")

    st.pyplot(plt)

def plot_victims_by_race_grouped_monthly(victims_by_race_dictionary, year):
    df = pd.DataFrame(victims_by_race_dictionary)
    df = df.transpose()
    
    df.plot(kind='bar')
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.ylabel("Quantity of Shootings")
    plt.title(f"Police Shootings by Race and by Month in {year}")

    st.pyplot(plt)

def plot_shootings_per_year(annual_shootings_dictionary):
    labels = list(annual_shootings_dictionary.keys())
    values = list(annual_shootings_dictionary.values())

    plt.bar(range(len(annual_shootings_dictionary)), values, tick_label=labels)
    plt.xticks(rotation=45)
    plt.ylabel("Number of Shootings")
    plt.xlabel("Year")
    plt.title("Quantity of Police Shootings from 2015-2022")
    plt.legend().set_visible(False)
    st.pyplot(plt)

def display_total_shootings_by_race(df, compare_numbers=False):
    """
    This function will display the amount of shootings that occured for every race directly
    to the dashboard.
    """
    white_victims = df[df['race']=='W']
    black_victims = df[df['race']=='B']
    asian_victims = df[df['race']=='A']
    hispanic_victims = df[df['race']=='H']
    not_sure_victims = df[df['race']=='N']
    other_victims = df[df['race']=='O']

    st.subheader("Total Quantity of Shooting Victims by Race")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(f"White: {len(white_victims)}")
    with col2:
        st.write(f"Black: {len(black_victims)}")
    with col3:
        st.write(f"Latin: {len(hispanic_victims)}")
    with col4:
        st.write(f"Asian: {len(asian_victims)}")
    with col5:
        st.write(f"Other: {len(not_sure_victims) + len(other_victims)}")

    if compare_numbers == True:
        st.write('compare')
    
def display_monthly_shootings_in_year(monthly_shootings, year):
    """
    This function will generate a bar chart containing the amount of shootings that occured
    in each month of a year.

    Parameters: monthly_shootings = Dictionary containing the months of a given year and the 
                                    amount of shootings that occured in that month.
                year              = The current year that is being displayed (as a string)
    """
    months = list(monthly_shootings.keys())
    values = list(monthly_shootings.values())
    
    plt.bar(range(len(monthly_shootings)), values, tick_label=months)
    plt.xticks(rotation=45)
    plt.ylabel("Number of Shootings")
    plt.xlabel("Months")
    plt.title(f"Monthly Police Shootings in {year[:4]}")
    st.pyplot(plt)
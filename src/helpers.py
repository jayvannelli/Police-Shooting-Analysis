import itertools
import operator

from src import data

def sort_descending(data, top_x_values):
    """
    This function takes in data (as a dictionary) and will return a sorted dictionary
    containing the top ___ values (which is passed a paramter names top_x_values)

    Example:
    sort_descending(data=armed_stats_dictionary, top_x_values=10) would return a dictionary
    with the keys and values of the largest 10 datapoints
    """
    sorted_descending = dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True))
    prepared_date = dict(itertools.islice(sorted_descending.items(), top_x_values))

    return prepared_date

def get_date_from_year(year):
    """
    This function takes in a year as an integer and returns the year formatted
    as a string.

    Example: 
    get_date_from_year(year=2015) would return "2015-01-01"
    """
    num_as_string = str(year)
    cleaned_num_string = num_as_string[:4] + "-01-01"
    
    return cleaned_num_string

def get_armed_stats_dictionary(police_shootings):
    data = {}
    armed_with = police_shootings['armed'].unique()
    for i in armed_with:
        armed_with_dataframe = police_shootings[police_shootings['armed']==i]
        amount_of_people_armed = len(armed_with_dataframe.index)
        data[i] = amount_of_people_armed
    
    return data

def get_lat_lon_df(police_shootings_df):
    """
    This function takes a police_shootings_df and returns a dataframe containing
    only the latitude and longitude columns (with the nan values dropped)
    """
    lat_lon_df = police_shootings_df[['latitude', 'longitude']]
    return lat_lon_df.dropna()

def get_shootings_by_city(df):
    """
    This function takes a df containing police shooting data (could be for one year
    or the whole dataframe) and returns each unique city that had a shooting and the 
    amount of shootings for each city (as a dictionary)

    Example:
    get_shootings_by_city(df=police_shootings_2015_df) would return a dictionary
    containing each unique city that had a police shooting in 2015 and the amount
    of shootings in each of those cities.
    """
    data = {}
    for i in df['city'].unique():
        state = df.loc[df['city']==i, 'state'].iloc[0]
        data[f"{i}, {state}"] = len(df[df['city']==i])
    return data

def get_victims_race_for_each_year(df, years):
    """
    This function will return a dictionary of shooting victims by race per year,
    which is passed as a dictionary of years.
    """
    races = ["White", "Black", "Hispanic", "Asian", "Not-Sure", "Other"]

    annual_victims_by_race = {}
    for year in years:
        specific_df = data.get_specific_year_dataframe(df=df, year=year)
        victims_by_race_for_year = {}
        for race in races:
            victims_by_race_for_year[race] = len(specific_df[specific_df['race']==race[0]])

        annual_victims_by_race[year] = victims_by_race_for_year
    
    return annual_victims_by_race

def get_victims_race_by_month_in_specific_year(df, months, year):
    races = ["White", "Black", "Hispanic", "Asian", "Not-Sure", "Other"]

    monthly_victim_race = {}
    for month in months:
        monthly_df = data.get_specific_month_dataframe(df, month, month+1, year)
        monthly_victims = {}
        for race in races:
            monthly_victims[race] = len(monthly_df[monthly_df['race']==race[0]])

        monthly_victim_race[month] = monthly_victims
    
    return monthly_victim_race
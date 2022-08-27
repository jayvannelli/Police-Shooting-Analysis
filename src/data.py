import pandas as pd

def get_dataframe():
    df = pd.read_csv('data/US Police shootings in from 2015-22.csv')
    return df

def get_specific_year_dataframe(df, year):
    """
    This function specifies the entire dataframe to include data that is within the year specified.
    """
    current_year = str(year)
    next_year = str(year+1)

    mask = (df['date'] > current_year) & (df['date'] < next_year)
    df = df.loc[mask]
    return df

def get_multiple_years_dataframe(df, start_year, end_year):
    """
    This function specifies the entire dataframe to include data that is between the start_year
    and up until the end_year.
    """
    start_year = str(start_year)
    end_year = str(end_year)

    mask = (df['date'] > start_year) & (df['date'] < end_year)
    df = df.loc[mask]
    return df

def get_specific_month_dataframe(df, current_month, next_month, year):
    if current_month < 10:
        current_month = "0" + str(current_month)
    else:
        current_month = str(current_month)
    
    if next_month < 10:
        next_month = "0" + str(next_month)
    elif next_month == 13:
        next_month = "01"
    else:
        next_month = str(next_month)

    current_year = str(year)
    next_year = str(year+1)

    current_month_formatted = current_year + "-" + current_month + "-01"
    
    if current_month == "12":
        next_month_formatted = next_year + "-" + next_month + "-01"
    else:
        next_month_formatted = current_year + "-" + next_month + "-01"

    mask = (df['date'] > current_month_formatted) & (df['date'] < next_month_formatted)
    df = df.loc[mask]
    return df
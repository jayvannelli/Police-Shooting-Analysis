months = ["-01-01",
          "-02-01",
          "-03-01",
          "-04-01",
          "-05-01",
          "-06-01",
          "-07-01",
          "-08-01",
          "-09-01",
          "-10-01",
          "-11-01",
          "-12-01",
          ]

def get_monthly_shooting_counts(df, start_month, end_month):
    """
    This function will get the amount of shootings in an individual month, given the 
    start of the month and end of the month.
    """
    mask = (df['date'] > start_month) & (df['date'] < end_month)
    df = df.loc[mask]
    return df

def get_monthly_shooting_counts_for_specific_year(df, year):
    """
    This function will get the amount of shootings in every month for a given year.

    Parameters: df           = Total US Police Shootings Dataframe
                current_year = The current year (as a string) that you want to display the monthly
                               values for.
                next_year    = The following year (as a string) that will be used when finding the last
                               month of the monthly values.
    
    Returns: This function will return a dictionary that contains each month of the year and the amount
             of shootings that occured in that month.
    """
    current_year = str(year)
    next_year = str(year+1)

    monthly_dates = []
    for i in months:
        cur_date = current_year + i
        monthly_dates.append(cur_date)
    
    monthly_shootings = {}
    for i in range(len(monthly_dates)):
        if i < 11:
            monthly_shooting_df = get_monthly_shooting_counts(df, start_month=monthly_dates[i], end_month=monthly_dates[i+1])
        else:
            monthly_shooting_df = get_monthly_shooting_counts(df, start_month=monthly_dates[i], end_month=next_year+monthly_dates[0])
        monthly_shootings[monthly_dates[i]] = len(monthly_shooting_df)
    
    return monthly_shootings
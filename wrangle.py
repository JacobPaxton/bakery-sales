import pandas as pd

def prep_explore():
    """ Acquire dataset, drop nulls in datetime column """
    # initial acquisition
    sales = pd.read_csv('Bakery Sales.csv')
    prices = pd.read_csv('Bakery price.csv')
    # in sales, drop rows with nulls in datetime column (after index 2419)
    sales = sales[sales.datetime.index < 2420]

    return sales, prices

def drop_closed_tuesdays(resampled_day_df):
    """ 
        Business is closed on all Tuesdays except Christmas Eve,
        Drop all non-Christmas Eve Tuesdays,
        Return dataframe.
    """
    tuesdays = resampled_day_df.index.day_name() == 'Tuesday'
    resampled_day_df[tuesdays].index.strftime('%m-%d') != '12-24'

    days_to_drop = ((resampled_day_df.index.day_name() == 'Tuesday') & 
                    (resampled_day_df.index != '2019-12-24'))
    daily_no_tuesdays = resampled_day_df[days_to_drop == False]

    return daily_no_tuesdays
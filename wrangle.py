import pandas as pd

def prep_explore():
    """ 
        Acquire dataset,
        Drop nulls in datetime column,
        Remove outlier rows using IQR on transaction charge totals,
        Return dataframe.
    """
    # initial acquisition
    sales = pd.read_csv('Bakery Sales.csv')
    prices = pd.read_csv('Bakery price.csv')
    # in sales, drop rows with nulls in datetime column (after index 2419)
    sales = sales[sales.datetime.index < 2420]
    # set index to datetime
    sales.index = pd.to_datetime(sales.datetime)
    sales = sales.drop(columns='datetime')
    # remove outliers in charges
    sales = remove_outliers(sales)

    return sales, prices

def remove_outliers(sales):
    """ Use IQR to remove outliers in transaction charges column """
    # use IQR to remove outliers in 'total' column
    q1, q3 = sales['total'].quantile([.25, .75])  # Get quartiles
    iqr = q3 - q1   # Calculate interquartile range
    upper_bound = q3 + 1.5 * iqr   # Get upper bound
    lower_bound = q1 - 1.5 * iqr   # Get lower bound
    # create mask
    mask = (sales['total'] > lower_bound) & (sales['total'] < upper_bound)
    sales = sales[mask] # Apply mask

    return sales

def drop_zero_rev_days(sales):
    """ Aggregate transactions into daily totals, drop zero-revenue days """
    # create daily sales df
    daily_sales = sales.resample('D').sum()
    # drop zero-revenue days from daily sales df
    nonzero_rev_days = daily_sales[daily_sales.total > 0]

    return nonzero_rev_days

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
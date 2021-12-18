import pandas as pd

def prep_explore():
    """ Acquire dataset, drop nulls in datetime column """
    # initial acquisition
    sales = pd.read_csv('Bakery Sales.csv')
    prices = pd.read_csv('Bakery price.csv')
    # in sales, drop rows with nulls in datetime column (after index 2419)
    sales = sales[sales.datetime.index < 2420]

    return sales, prices
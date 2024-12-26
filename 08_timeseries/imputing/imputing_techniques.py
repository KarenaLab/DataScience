# Time Series Imputation techniques [P452]

# Versions
# 01 - Dec 23rd, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
# Interpolate (linear and spline)
# Foward fill
# Backward fill
# Average mean
# Average median


# Sources and relevant information
# Pandas Interpolate (pandas.interpolate)
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html

# https://www.geeksforgeeks.org/how-to-deal-with-missing-values-in-a-timeseries-in-python/

# 


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt



# ----------------------------------------------------------------------
def insert_nans(DataFrame, columns=None, percentage=0, seed=314):
    """
    Remove **percentage** of **DataFrame**, inserting NaN, the main
    usage is for educational purpose.
    
    """
    # Data preparation: Rows
    index = list(DataFrame.index)
    n_rows = len(index)

    # Data preparation: Columns
    if(columns == None):
        columns = list(DataFrame.columns)

    n_cols = len(columns)

    # Items to remove 
    n_remove = int(n_rows * n_cols * (percentage / 100))
    

    # Shuffling
    if(seed != None):
        np.random.seed(seed)

    np.random.shuffle(index)

    for row in index:
        col = np.random.randint(low=0, high=n_cols, size=1)[0]
        col = columns[col]

        DataFrame.loc[row, col] = np.nan
        
    
    return DataFrame


def fill_mean(DataFrame, columns):
    for col in columns:
        mean = np.mean(DataFrame[col].dropna())
        DataFrame[col] = fill_value(DataFrame[col], mean)

    return DataFrame


def fill_median(DataFrame, columns):
    for col in columns:
        median = np.median(DataFrame[col].dropna())
        DataFrame[col] = fill_value(DataFrame[col], median)

    return DataFrame


def fill_zeros(DataFrame, columns):
    for col in columns:
        DataFrame[col] = fill_value(DataFrame[col], 0)

    return DataFrame


def fill_interpolate(DataFrame, columns, method="linear", order=None):
    for col in columns:
        DataFrame[col] = DataFrame[col].interpolate(method=method, order=order)

    return DataFrame
    


def fill_value(Series, value):
    Series = Series.fillna(value)

    return Series





# backward fill
# forward fill
# fill max value
# fill min value



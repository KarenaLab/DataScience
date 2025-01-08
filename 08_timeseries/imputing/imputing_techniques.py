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


def fill_mean(DataFrame, columns="all"):
    """
    Time Series - Imputing techniques
    Fill NaNs with the mean of the column.

    """
    # Columns preparation
    if(columns == "all" or columns == None):
        columns = list(DataFrame.columns)

    # Data imputation    
    for col in columns:
        mean = np.mean(DataFrame[col].dropna())
        DataFrame[col] = fill_value(DataFrame[col], mean)

    return DataFrame


def fill_median(DataFrame, columns="all"):
    """
    Time Series - Imputing techniques.
    Fill NaNs with the median of the column.

    """
    # Columns preparation
    if(columns == "all" or columns == None):
        columns = list(DataFrame.columns)

    # Data imputation 
    for col in columns:
        median = np.median(DataFrame[col].dropna())
        DataFrame[col] = fill_value(DataFrame[col], median)

    return DataFrame


def fill_min(DataFrame, columns="all"):
    """
    Time Series - Imputing techniques.
    Fill NaNs with the minimum value of the column.

    """
    # Columns preparation
    if(columns == "all" or columns == None):
        columns = list(DataFrame.columns)

    # Data imputation 
    for col in columns:
        minimum = np.min(DataFrame[col].dropna())
        DataFrame[col] = fill_value(DataFrame[col], minimum)

    return DataFrame


def fill_max(DataFrame, columns="all"):
    """
    Time Series - Inputing techniques.
    Fill NaNs with the maximum value of the column.

    """
    # Columns preparation
    if(columns == "all" or columns == None):
        columns = list(DataFrame.columns)

    # Data imputation 
    for col in columns:
        maximum = np.max(DataFrame[col].dropna())
        DataFrame[col] = fill_value(DataFrame[col], maximum)

    return DataFrame


def fill_zeros(DataFrame, columns="all"):
    """
    Time Series - Imputing techniques.
    Fill NaNs with 0 (zero).

    """
    # Columns preparation
    if(columns == "all" or columns == None):
        columns = list(DataFrame.columns)

    # Data imputation 
    for col in columns:
        DataFrame[col] = fill_value(DataFrame[col], 0)

    return DataFrame


def fill_interpolate(DataFrame, columns="all", method="linear", order=None):
    """
    Time Series - Imputing techniques.
    Fill NaNs with interpolation with neighbours values.

    Interpolation techniques avaliable (from pd.interpolate):
    * linear (default), time and polynomial (need to give order).

    More info:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html

    """
    # Columns preparation
    if(columns == "all" or columns == None):
        columns = list(DataFrame.columns)

    # Data imputation 
    for col in columns:
        DataFrame[col] = DataFrame[col].interpolate(method=method, order=order)

    return DataFrame


def fill_forward(DataFrame, columns="all"):
    """
    Time Series - Imputing techniques
    Fill NaNs values by propagating the last valid observation to next
    valid.

    More info:
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html

    """
    # Columns preparation
    if(columns == "all" or columns == None):
        columns = list(DataFrame.columns)

    # Data imputation 
    for col in columns:
        DataFrame[col] = DataFrame[col].ffill()

    return DataFrame


def fill_backward(DataFrame, columns="all"):
    """
    Time series - Imputing techniques
    Fill NaNs values by using the next valid obervation to fill the gap.

    More info:
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.bfill.html

    """

    # Data imputation 
    for col in columns:
        DataFrame[col] = DataFrame[col].bfill()

    return DataFrame
    

def fill_value(Series, value):
    """
    Internal function to fill the with the given **value**.

    """
    Series = Series.fillna(value)

    return Series


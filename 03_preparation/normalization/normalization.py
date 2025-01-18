# [P345] Normalization (from scratch)

# Versions
# 01 - Jan 17th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------
def scaler_minmax(Series):
    """
    Performs a Min-Max normalization, rescaling data for a range
    of values from 0 to 1 [0, 1].

    Returns:
    values = Pandas series with min-max scaler applied.
    params = Python dictionary with value to invert the scaling.
             params[col_name] = [method, minimum, maximum]

    """    
    # Min-Max scaling
    x_min = Series.min()
    x_max = Series.max()

    params = dict()
    params[Series.name] = ["minmax", x_min, x_max]

    def minmax(x, minimum, maximum):
        x_scaled = (x - x_min) / (x_max - x_min)
        return x_scaled


    Series = Series.apply(lambda x: minmax(x, x_min, x_max))
   
    return Series, params


def scaler_standard(Series):
    """
    Performs a Standard normalization, rescaling data for values with
    mean in zero and standard deviatin of 1.

    Returns:
    values = Pandas series with standard scaler applied.
    params = Python dictionary with value to invert the scaling.
             params[col_name] = [method, mean, stddev] 

    """
    # Standard scaling
    x_mean = Series.mean()
    x_stddev = Series.std()

    params = dict()
    params[Series.name] = ["standard", x_mean, x_stddev]

    def standard(x, mean, stddev):
        x_scaled = (x - mean) / stddev
        return x_scaled


    Series = Series.apply(lambda x: standard(x, x_mean, x_stddev))

    return Series, params 
        

def inv_scaler_minmax(Series, params):
    """
    Performs the inverse of Min-Max normalization, rescaling the data
    for the previous (real) data.

    Returns:
    values = Pandas series with inverse min-max applied.

    """   
    _, x_min, x_max = list(params.values())[0]

    def inv_minmax(x_scaled, minimum, maximum):
        x = ((maximum - minimum) * x_scaled) + minimum
        return x


    Series = Series.apply(lambda xs: inv_minmax(xs, x_min, x_max))

    return Series


def inv_scaler_standard(Series, params):
    """
    Performs the inverse of Standard normalization, recaling the data
    for the previous (real) data.

    Return values = Pandas series with inverse standard applied.

    """
    _, x_mean, x_stddev = list(params.values())[0]

    def inv_standard(x_scaled, mean, stddev):
        x = (x_scaled * stddev) + mean
        return x


    Series = Series.apply(lambda xs: inv_standard(xs, x_mean, x_stddev))

    return Series


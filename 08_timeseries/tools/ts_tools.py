# [P473] Time Series Tools

# Versions
# 01 - Jan 15th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import os
import sys
import warnings

import numpy as np
import pandas as pd
import statsmodels.api as sm
import scipy.stats as stats

import matplotlib.pyplot as plt



# ----------------------------------------------------------------------
def ts_decomposition(DataFrame, model="additive", filt=None, period=None):
    """
    Performs the Time Series decomposition and returns a friendly
    output to be vizualized, maybe it is the first view of the Time
    Series data.

    Variables:
    * model: additive (default) or multiplicative.

    More info:
    https://www.statsmodels.org/dev/generated/statsmodels.tsa.seasonal.seasonal_decompose.html
    https://www.statsmodels.org/dev/generated/statsmodels.tsa.seasonal.DecomposeResult.html
    
    """
    # Model check
    model = model.lower()
    if(model != "additive" and model != "multiplicative"):
        model = "additive"
        warnings.warn('Model Error: Selected model "additive" as default.')

    # Time Series decomposition
    decomposition = sm.tsa.seasonal_decompose(DataFrame, model=model, filt=filt, period=period)

    observed = decomposition.observed
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    weights = decomposition.weights

    # Return decomposition as a dataframe
    data = pd.DataFrame(data=[])
    for info in [observed, trend, seasonal, residual]:
        data[info.name] = info

    # Append `weights` only if values are different from scalar (1).
    if(len(weights.unique()) > 1):
        data[weights.name] = weights
        

    return data


def create_lagged_features(DataFrame, variable, max_lag, freq):
    """
    Lagged features are create with the assumption that what happened
    in the past can influence or contain a sort of intrinsic information
    about the future.

    Function will create [1, **max_lag**] variables (columns) with
    **freq** based in the given **variable**.

    Variables
    * DataFrame: Pandas dataframe where data is,
    * variable: Single variable (as a string) to be shifted,
    * max_lag: integer or a list. If given an integer, function will create
               a list from [1, max_lag] and interate the shift with this.
               Also could inform directly the desired list. Inform a list
               with a single value if you wish a single new variable creation.
    * freq: Timestamp frequency to create lagged variables.

    More info:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html
    https://medium.com/@rahulholla1/advanced-feature-engineering-for-time-series-data-5f00e3a8ad29
    
    """
    # `max_lag` preparation:
    if(isinstance(max_lag, int) == True):
        lag_list = range(1, max_lag+1)

    elif(isinstance(max_lag, list) == True):
        lag_list = max_lag[:]

    # Lagged variables
    for t in lag_list:
        new_variable = f"{variable}_lag{t}"
        DataFrame[new_variable] = DataFrame[variable].shift(t, freq=freq)


    return DataFrame


def mape(y_true, y_pred):
    """
    Mean Absolute Percentage Error (MAPE) stands for the percentual
    absolute error of the prediction (or forecast).
    [MLTSF p.47]

    Important: Result is NOT multiplied by 100. Range: [0, 1]
    
    More info:
    https://en.wikipedia.org/wiki/Mean_absolute_percentage_error
    https://www.statology.org/how-to-interpret-mape/

    """
    # Data preparation
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Calculation
    result = np.mean((np.abs(y_true - y_pred) / y_true))
        
    return result  


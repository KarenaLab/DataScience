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


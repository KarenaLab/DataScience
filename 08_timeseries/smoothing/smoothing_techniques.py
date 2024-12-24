# [P449] Smoothing techniques

# Versions
# 01 - Dec 22nd, 2024 - Starter
#      Dec 23rd, 2024 - Add Exponential Moving Average (EWMA)
#      

# Insights, improvements and bugfix
# 01 - Add Holt-Winters Exponential technique
#


# Libraries
import numpy as np
import pandas as pd

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.nonparametric.smoothers_lowess import lowess
from pykalman import KalmanFilter
from scipy.signal import savgol_filter


# ----------------------------------------------------------------------
def moving_average(Series, window):
    """
    Performs the moving average with a given **window**.

    """
    data = Series.rolling(window=window).mean()
    
    return data


def exponential(x, y, alpha=0.5, halflife=None):
    """
    Performs Exponental Weighted Moving Average (EWMA) with a given
    **alpha**.

    Important: Based on pandas.ewm function. For more parameters, use
    that function directly.
    
    More info:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html

    """
    data = pd.DataFrame(index=x, data=y)
    data = data.ewm(alpha=alpha, halflife=halflife).mean()

    col = data.columns[0]
    y_ewma = data[col]
        
    return y_ewma
                


# lowess_smoothing
# kalman_filter
# savitzky_golay

# Source
# https://pieriantraining.com/python-smoothing-data-a-comprehensive-guide/


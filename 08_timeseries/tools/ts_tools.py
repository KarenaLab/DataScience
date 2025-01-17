# [P473] Time Series Tools

# Versions
# 01 - Jan 15th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt



# ----------------------------------------------------------------------
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


def gmrae(y_true, y_pred):
    """


    """
    pass

    return None


def smape(y_true, y_pred):
    """


    """
    pass

    return None

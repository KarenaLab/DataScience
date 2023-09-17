# Regression Metrics [P201] --------------------------------------------

# Libraries
import numpy as np
import pandas as pd

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score


# Versions
# 01 - May 15th, 2023 - Starter,
# 02 - Jun 27th, 2023 - Adjust for metrics="all" and sync with model params,
#      Aug 29th, 2023 - Add MAPE, SMAPE and Bias,
# 03 - Sep 01st, 2023 - Add size test and nan removing,
#                       Rename error functions (type_error),
#      Sep 02nd, 2023 - Add MSE option,
#                       Bugfix: y_pred and y_true with same source of data.
# 04 - Sep 17th, 2023 - Separate **Data Preparation**,
#                       Bias and SMAPE as user friendly function, could be
#                           called separately,
# 


# Insights, improvements and bugfix (remove, or move from here to Version ctrl)
# Add Hubber Loss [https://en.wikipedia.org/wiki/Huber_loss]
# Add Fbeta Score for two metrics (KarenaLab)
#


def _array_prep(array, dropna=True):
    """
    (( Internal function ))
    Standartize arrays as numpy array format and **dropna** values.

    """
    if(isinstance(array, np.array) == False):
        array = np.array(array)

    if(dropna == True):
        array = array[~np.isnan(array)]


    return array


def regr_metrics(y_true, y_pred, metrics="all", verbose=True):
    """
    Metrics for Regressor Models.
    
    Pearson R = Pearson R Coeficient,
    MAE = Mean Absolute Error,
    MAPE = Mean Absolute Percentage Error
    SMAPE = Symmetric mean absolute percentage error
            https://en.wikipedia.org/wiki/Symmetric_mean_absolute_percentage_error
    MSE = Mean Squared Error
    RMSE = Root Mean Squared Error
    Bias = Systematic tendency of the predicted against the ground truth
    
    R2 = R^2 or Coef. Determination
         https://en.wikipedia.org/wiki/Coefficient_of_determination

    """
    # Data preparation
    y_true = _array_prep(y_true, dropna=True)
    y_pred = _array_prep(y_pred, dropna=True)


    # Metrics
    if(len(y_true) == len(y_pred)):
        results = dict()
        
        if(metrics.count("pearson") == 1 or metrics == "all"):
            pearson = np.corrcoef(y_true, y_pred)[0][1]
            results["pearson"] = pearson
        
        if(metrics.count("mae") == 1 or metrics == "all"):
            mae = mean_absolute_error(y_true, y_pred)
            results["mae"] = mae

        if(metrics.count("mse") == 1 or metrics == "all"):
            mse = mean_squared_error(y_true, y_pred, squared=False)
            results["mse"] = mse 
            
        if(metrics.count("rmse") == 1 or metrics == "all"):
            rmse = mean_squared_error(y_true, y_pred, squared=True)
            results["rmse"] = rmse

        if(metrics.count("mape") == 1 or metrics == "all"):
            mape = mean_absolute_percentage_error(y_true, y_pred)
            results["mape"] = mape

        if(metrics.count("smape") == 1 or metrics == "all"):
            smape = smape_error(y_true, y_pred)
            results["smape"] = smape

        if(metrics.count("bias") == 1 or metrics == "all"):
            bias = bias_error(y_true, y_pred)
            results["bias"] = bias

        if(metrics.count("r2_score") == 1 or metrics == "all"):
            r2 = r2_score(y_true, y_pred)
            results["r2_score"] = r2

    else:
        results = np.nan

        if(verbose == True):
            print(f" > Warning: Arrays with different shape and/or having np.nan values ({len(y_true)}-{len(y_pred)}")
    

    return results


# def huberloss_error(y_true, y_pred):


def bias_error(y_true, y_pred):
    """
    Statistical **Bias**, in the mathematical field of statistics, is a systematic
    tendency in which the methods used to gather data and generate statistics
    present an inaccurate, skewed or biased depiction of reality.
    Statistical bias exists in numerous stages of the data collection and
    analysis process, including: the source of the data, the methods used to
    collect the data, the estimator chosen, and the methods used to analyze
    the data.

    """
    # Data preparation
    y_true = _array_prep(y_true, dropna=True)
    y_pred = _array_prep(y_pred, dropna=True)


    # Metrics
    if(len(y_true) == len(y_pred)):  
        bias = np.mean(y_pred - y_true)

    else:
        bias = np.nan

        if(verbose == True):
            print(f" > Warning: Arrays with different shape and/or having np.nan values ({len(y_true)}-{len(y_pred)}")



    return bias


def smape_error(y_true, y_pred):
    """
    Symmetric Mean Absolute Percentage Error (SMAPE) is an accuracy measure
    based on percentage (or relative) errors.
    Used to measure the predictive accuracy of models. It is called as:

    SMAPE = (1/n) * sum(|pred - true| / ((|true| + |pred|) / 2) * 100)

    """
    # Data preparation
    y_true = _array_prep(y_true, dropna=True)
    y_pred = _array_prep(y_pred, dropna=True)


    # Metrics
    if(len(y_true) == len(y_pred)):
        smape = (100 / len(y_true)) * np.sum((np.abs(y_pred - y_true) / ((np.abs(y_true) + np.abs(y_pred)) / 2)))

    else:
        smape = np.nan

        if(verbose == True):
            print(f" > Warning: Arrays with different shape and/or having np.nan values ({len(y_true)}-{len(y_pred)}")


    return smape
                                         

# end

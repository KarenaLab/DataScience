
# Libraries
import numpy as np

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score


# Versions
# 01 - unknown - Starter
# 02 - Jun 27th, 2023 - Adjusting for metrics="all" and sync with model
#      params

# Insights
# Add SMAPE
# Add MAPE
# Add Bias


def regr_metrics(y_true, y_pred, metrics="all", verbose=True):
    """
    Metrics for Regressor Models.
    
    Pearson R = Pearson R Coeficient,
    MAE = Mean Absolute Error,
    RMSE = Root Mean Squared Error
    R2 = R^2 or Coef. Determination
         https://en.wikipedia.org/wiki/Coefficient_of_determination

    """
    # Data preparation
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    results = {}
    
    # Metrics    
    if(metrics.count("pearson") == 1 or metrics == "all"):
        pearson = np.corrcoef(y_true, y_pred)[0][1]
        results["pearson"] = pearson
    
    if(metrics.count("mae") == 1 or metrics == "all"):
        mae = mean_absolute_error(y_true, y_pred)
        results["mae"] = mae
        
    if(metrics.count("rmse") == 1 or metrics == "all"):
        rmse = mean_squared_error(y_true, y_pred, squared=True)
        results["rmse"] = rmse

    if(metrics.count("mape") == 1 or metrics == "all"):
        mape = mean_absolute_percentage_error(y_true, y_pred)
        results["mape"] = mape

    if(metrics.count("smape") == 1 or metrics == "all"):
        smape = regr_smape(y_true, y_pred)
        results["smape"] = smape

    if(metrics.count("bias") == 1 or metrics == "all"):
        bias = regr_bias(y_true, y_pred)
        results["bias"] = bias

    if(metrics.count("r2_score") == 1 or metrics == "all"):
        r2 = r2_score(y_true, y_pred)
        results["r2_score"] = r2
    

    return results



def regr_bias(y_true, y_pred):
    """
    Statistical **Bias**, in the mathematical field of statistics, is a systematic
    tendency in which the methods used to gather data and generate statistics
    present an inaccurate, skewed or biased depiction of reality.
    Statistical bias exists in numerous stages of the data collection and
    analysis process, including: the source of the data, the methods used to
    collect the data, the estimator chosen, and the methods used to analyze
    the data.

    """
    # Data preparation: Not need because it will be called after the main
    # function. If be used in a single way, need to add np.array treatment

    bias = np.mean(y_pred - y_true)


    return bias


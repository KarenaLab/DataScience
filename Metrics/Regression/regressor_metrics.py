
# Libraries
import numpy as np

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# Versions
# 01 -


# Insights
#


def regressor_metrics(y_true, y_pred, metrics="all", decimals=4, verbose=True):
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

    # Prepare list
    
    if(pearson == True):
        pearson = np.corrcoef(y_true, y_pred)[0][1]
    
    if(MAE == True):
        MAE = mean_absolute_error(y_true, y_pred)
        MAE = np.round(MAE, decimals=decimals)
        

    if(RMSE == True):
        RMSE = mean_squared_error(y_true, y_pred, squared=True)
        RMSE = np.round(RMSE, decimals=decimals)
        

    if(R2 == True):
        R2 = r2_score(y_true, y_pred)
        R2 = np.round(R2, decimals=decimals)
    

    return None


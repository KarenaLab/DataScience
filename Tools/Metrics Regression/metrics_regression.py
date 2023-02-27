
import numpy as np

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


def regr_metrics(y_true, y_pred, metrics="all", verbose=True):
    """
    Calculates all regression metrics and returns a dictionary with all
    values selected.

    Variables:
    * y_true = Variable to be compared,
    * y_pred = Variable predicted and to be compared to,

    * MAE = Mean Absolute Error
    * MSE = Mean Squared Error
    * R2 = Coef. of Determination
    * Pearson = Pearson correaltion coef.
    
    """
    metrics_dict = {}
    
    if(metrics.count("mae") == 1 or metrics.count("all") == 1):
        mae = mean_absolute_error(y_true, y_pred)
        metrics_dict["mae"] = mae

        if(verbose == True):
            print(f" > MAE: {mae:.4f}")


    if(metrics.count("mse") == 1 or metrics.count("all") == 1):
        mse = mean_squared_error(y_true, y_pred)
        metrics_dict["mse"] = mse

        if(verbose == True):
            print(f" > MSE: {mse:.4f}")

            
    if(metrics.count("r2") == 1 or metrics.count("all") == 1):        
        r2 = r2_score(y_true, y_pred)
        metrics_dict["r2_score"] = r2

        if(verbose == True):
            print(f" >  R2: {r2:.5f}")


    if(metrics.count("pearson") == 1 or metrics.count("all") == 1):
        pearson = np.corrcoef(y_true, y_pred)[0][1]
        metrics_dict["pearson"] = pearson
        
        if(verbose == True):
            print(f" > Pearson: {pearson:.5f}")


    if(verbose == True):
        print("")

        
    return metrics_dict



def regressor_metrics(y_test, y_pred, decimals=4, verbose=True, MAE=True, MSE=True, R2=True):
    """
    Metrics for Regressor Models.

    MAE = Mean Absolute Error
    MSE = Mean Squared Error
    R2 = R^2 or Coef. Determination
         https://en.wikipedia.org/wiki/Coefficient_of_determination

    """
    import numpy as np
    
    from sklearn.metrics import mean_absolute_error
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score

    
    if(MAE == True):
        MAE = mean_absolute_error(y_test, y_pred)
        MAE = np.round(MAE, decimals=decimals)

    else:
        MAE = np.nan
        

    if(MSE == True):
        MSE = mean_squared_error(y_test, y_pred)
        MSE = np.round(MSE, decimals=decimals)

    else:
        MSE = np.nan
        

    if(R2 == True):
        R2 = r2_score(y_test, y_pred)
        R2 = np.round(R2, decimals=decimals)

    else:
        R2 = np.nan
    

    return MAE, MSE, R2


def correlation(y_test, y_pred, method="pearson", decimals=4):
    """
    Compute pairwise correlation of columns, excluding NA/null values.
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

    """

    import numpy as np
    import pandas as pd

    data = pd.DataFrame([])
    data["y_test"] = y_test
    data["y_pred"] = y_pred

    method = method.lower()
    if(method == "pearson" or method == "spearman" or method == "kendall"):
        corr = data.corr(method=method)
        corr = corr.loc["y_test", "y_pred"]
        corr = np.round(corr, decimals=decimals)

    else:
        corr = np.nan
        print(" ****  Error: Correlation not computed. WRONG method selected  ****")


    return corr

    

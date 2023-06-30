# PowerTransform [P347]
# Applies powertransform to the dataset using the scikit module and adding a
# dictionary with the lambdas used for analysis of data and inverse transform.


# Versions:
# 01 - Jun 30th, 2023 - Starter
# 02 -


# Insights and bugfix
# Add inverse operator
# Add explanation (help)
# Add verbose operator
#


# Libraries
import numpy as np
import pandas as pd

from sklearn.preprocessing import PowerTransformer



def apply_powertransformer(DataFrame, method="yeo-johnson", standardize=True):
    """
    (( add explanation ))
    
    More info:    
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html
    """
    # Data preparation
    data = DataFrame.copy()
    columns = data.columns

    if(method == "yeo-johnson" or method="box-cox"):
        # PowerTransform
        pt = PowerTransformer()

        # Hiperparameters
        pt.method = method
        pt.standardize = standardize

        # Fit and transform
        pt.fit(data)
        data = pt.transform(data)
        data = pd.DataFrame(data=data, columns=columns)

        # Collecting lambdas
        data_lambdas = {}
        for col, lambda_coef in zip(columns, pt.lambdas_):
            data_lambdas[col] = lambda_coef

        
    else:
        data = []
        data_lambdas = {}


    return data, data_lambdas


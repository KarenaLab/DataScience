
import numpy as np
import pandas as pd

def split_trainval_test(DataFrame, train_size=80, seed=None):
    """
    

    """
    # Versions ---------------------------------------------------------
    # 01 - Feb 18th, 2023 - Starter
    # 02 -

    # Insights
    # Add a Nested KFold function
    # Add a function that preserves distribution in both sets
    # Make sure extremes are in the trainval set
    #
    

    # Program ----------------------------------------------------------
    data = DataFrame.copy()
    data = data.dropna()

    if(seed != None):
        np.random.seed(seed)

    data = data.sample(frac=1)      # Shuffling entire dataset
    
    if(train_size >= 1):
        train_size = train_size / 100

    n_cut = (int(data.shape[0] * train_size) + 0.5)

    data_trainval = data.iloc[0:n_cut, :].reset_index(drop=True)
    data_test = data.iloc[n_cut: , :].reset_index(drop=True)
         

    return data_trainval, data_test


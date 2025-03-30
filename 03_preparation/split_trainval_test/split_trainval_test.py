# [P229] Train Validation and Test split (holdout)

# Libraries
import numpy as np
import pandas as pd


# Functions
def split_trainval_test(DataFrame, train_size=70, seed=None):
    """
    

    """
    # Train and Test preparation
    n_train = int((DataFrame.shape[0] * (train_size / 100)) + .5)
    n_test = DataFrame.shape[0] - n_train

    print(n_train, n_test)


    """
    # Seed preparation
    if(seed != None):
        np.random.seed(seed)

    data = data.sample(frac=1)      # Shuffling entire dataset
    
    if(train_size >= 1):
        train_size = train_size / 100

    n_cut = int((data.shape[0] * train_size) + 0.5)

    data_trainval = data.iloc[0:n_cut, :].reset_index(drop=True)
    data_test = data.iloc[n_cut: , :].reset_index(drop=True)
    """
    
    return data_trainval, data_test


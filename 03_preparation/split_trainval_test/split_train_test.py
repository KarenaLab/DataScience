# [P229] Train Validation and Test split (holdout)

# Libraries
import numpy as np
import pandas as pd


# Functions
def split_train_test(DataFrame, train_size=70, seed=None, reset_index=True):
    """
    

    """
    # Train and Test preparation
    cut = int((DataFrame.shape[0] * (train_size / 100)) + .5)

    # Seed preparation
    if(seed != None):
        np.random.seed(seed)

    # Train and Test split
    index = np.array(DataFrame.index)
    np.random.shuffle(index)

    print(index)

    train = DataFrame.iloc[0:cut, :].reset_index(drop=reset_index)
    test = DataFrame.iloc[cut: , :].reset_index(drop=reset_index)
    
    
    return train, test


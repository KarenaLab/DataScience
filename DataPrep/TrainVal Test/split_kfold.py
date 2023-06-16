# KFold split ----------------------------------------------------------

# Versions
# 01 - Jun 15th, 2023 - Starter
# 02 -


# Insights and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import KFold



def split_kfold(x, n_splits=5, shuffle=True, seed=None):
    """
    Splits a **dataset** in **n_splits** folds and
    returns a list with: [folder_index, train_index, test_index]

    Based in Scikit-learn function KFold. More info:
    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html

    """
    data = x.copy()


    # Data split parameters
    kf = KFold()

    kf.n_splits = n_splits
    kf.shuffle = shuffle

    if(seed != None):
        np.random.seed(seed)


    split_table = []
    for i, (train_index, test_index) in enumerate(kf.split(data)):
        line = [i, train_index, test_index]
        split_table.append(line)
    

    return split_table


def get_fold(split_table, fold, verbose=False):
    """
    Gets a table with train and test index splits and gets only one
    **fold**.

    Attention: Works together with *split_kfold* function.

    """
    if(fold < len(split_table)):
        train = split_table[fold][1]
        test = split_table[fold][2]

    else:
        train = []
        test = []

        if(verbose == True):
            print(f" >>> Error: *fold* exceeds the number of folds in the split_table. Returning an empty lists for both (train_index and test_index).") 


    return train, test




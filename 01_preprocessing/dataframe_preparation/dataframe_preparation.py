
# Data Preparation [P263] ---------------------------------------------

# Versions
# 01 - Feb 07th, 2023 - Starter
# 02 - May 25th, 2023 - Adjusting nan_counter
# 02 - May 25th, 2023 - Adding distinct_counter
# 03 - 


# Insights



# List of Functions



# Libraries
import os
from collections import namedtuple

import numpy as np
import pandas as pd
import scipy.stats as st


# Functions -------------------------------------------------------------

def col_preparation(DataFrame, method=None, verbose=False):
    """
    Standartize columns names.

    Variables:
    * DataFrame = DataFrame to be standartized,
    * method = lower, UPPER or Title. (default=lower),
    * verbose = True or False. (default=True).

    """
    data = DataFrame.copy()
    method = method.lower()

    cols_name = dict()
    for col in data.columns:
        new_col = col[:]

    # Dictionary with characters to be replaced or changed
        items_to_replace = {"-": "_",
                            " ": "_",
                            "(": "",
                            ")": "",
                            "?": "",
                            "[": "",
                            "]": ""}

        for old, new in list(zip(items_to_replace.keys(), items_to_replace.values())):
            new_col = new_col.replace(old, new)


        # Applying method name style
        if(method == "lower"):
            new_col = new_col.lower()

        elif(method == "upper"):
            new_col = new_col.upper()

        elif(method == "title"):
            new_col = new_col.title()

        if(verbose == True):
            print(f" > column {col} renamed for **{new_col}**")
            
        cols_name[col] = new_col 

    data = data.rename(columns=cols_name)

    if(verbose == True):
        print("")
        
    return data


def nan_preparation(DataFrame, columns=None):
    """
    Substitutes some values to np.nan.

    """
    pass

    return None


def remove_duplicates(DataFrame, verbose=True):
    """
    Remove duplicates from **DataFrame**

    """
    data = DataFrame.copy()

    no_rows = data.shape[0]
    duplicated = np.array(data.index[data.duplicated()])
    data = data.drop_duplicates(ignore_index=True)

    if(verbose == True):
        print(f" > Duplicated items removed: {len(duplicated)} ({(len(duplicated)/no_rows):.2%}) \n")


    return data


def count_nan(DataFrame, del_threshold=100, verbose=True):
    """
    Counts the number of NaN  (empty) at rows and delete row if the
    percentage of NaNs is higher than a given threshold.

    threshold: [0, 100], default=100; delete only if all columns of the
        row is empty.

    """
    data = DataFrame.copy()
    nan_count_list = []

    # Delete Threshold preparation.
    # value is always a percentage, if (x < 1), need to be transformed.
    if(del_threshold > 0 and del_threshold < 1):
        del_threshold = int(del_threshold * 100)

   
    nrows = DataFrame.shape[0]
    has_action = False

    for col in data.columns:
        nan_count = data[col].isna().sum()
        nan_count_list.append(nan_count)
        
        nan_pct = np.round((nan_count / nrows) * 100, decimals=3)

        if(nan_count > 0 and verbose == True):
            has_action = True
            print(f' > column "{col}" has {nan_count} NaNs ({(nan_count/nrows)*100:.2%})')

        if(nan_pct >= del_threshold):
            data = data.drop(columns=[col])

            if(verbose == True):
                has_action = True
                print(f' >>> Warning: Column deleted. Delete threshold={del_threshold}% \n')


    if(has_action == False and verbose == True):
        print(f" >>> No NaN detected at DataFrame. \n")


    return data


def count_unique(DataFrame, columns=None, verbose=True):
    """
    Counts the number of distinct values for all columns of DataFrame, or
    given columns.

    """
    data = DataFrame.copy()

    if(columns == None):
        columns = data.columns.tolist()

    distinct_list = list()
    
    for col in columns:
        distinct = len(data[col].unique())
        distinct_list.append(distinct)

        if(verbose == True):
            print(f' > col "{col}" has {distinct} distinct values')


    return distinct_list
        

def target_split(DataFrame, target):
    """
    Splits **Dataframe** into x (variables) and y (target).

    """
    data = DataFrame.copy()
    
    if(data.columns.tolist().count(target) == 1):
        x = data.drop(columns=[target])
        y = data[target]

    else:
        x = list()
        y = list()


    return x, y


def sample_test(array, size, seed=None, verbose=True):
    """
    Selects a sample from the given **array** with a selected number
    (**size**).

    Optionally, could use a **seed** for repeatability.

    """
    # If need, select a seed
    if(seed != None):
        np.random.seed(seed)

    if(size > 0 and size <= len(array)):
        # Array selection, without repetition
        np.random.shuffle(array)
        new_array = array[0: size]

    else:
        new_array = list()

        if(verbose == True):
            print(f" > Error: Size {size} is not compatible with given array")


    return new_array


# end
    

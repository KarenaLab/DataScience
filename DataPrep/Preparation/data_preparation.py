
# Data Preparation ----------------------------------------------------

# Versions
# 01 - Feb 07th, 2023 - Starter
# 02 -


# Insights


# Libraries
import numpy as np
import pandas as pd



def col_preparation(DataFrame, method="lower", verbose=True):
    """
    Standartize columns names.

    Variables:
    * DataFrame = DataFrame to be standartized,
    * method = lower, UPPER or Title. (default=lower),
    * verbose = True or False. (default=True).

    """
    data = DataFrame.copy()
    method = method.lower()

    for col in data.columns:
        new_col = col[:]

        items_to_replace = {"-": "_",
                            " ": "_",
                            "(": "",
                            ")": ""}
        # add new items here: item to be replaced and new item.

        for old, new in list(zip(items_to_replace.keys(), items_to_replace.values())):
            new_col = new_col.replace(old, new)

            if(method == "lower"):
                new_col = new_col.lower()

            elif(method == "upper"):
                new_col = new_col.upper()

            elif(method == "title"):
                new_col = new_col.title()        


        data = data.rename(columns={col: new_col})

        if(verbose == True):
            print(f" > column {col} renamed for **{new_col}**")


    if(verbose == True):
        print("")
        
    return data


def remove_duplicates(DataFrame, verbose=True):
    """
    Remove duplicates from **DataFrame**

    """
    data = DataFrame.copy()

    no_rows = data.shape[0]
    duplicated = np.array(data.index[data.duplicated()])
    data = data.drop_duplicates(ignore_index=True)

    if(verbose == True):
        print(f" > Duplicated items removed: {len(duplicated)} ({(len(duplicated)/no_rows)*100:.3f})%\n")

    return data


def nan_count(DataFrame, del_threshold=100, verbose=True):
    """


    """
    data = DataFrame.copy()
    nan_count_list = []

    # Delete Threshold preparation.
    # value is always a percentage, if x<1 be transformed.
    if(del_threshold > 0 and del_threshold < 1):
        del_threshold = int(del_threshold * 100)

   
    nrows = DataFrame.shape[0]

    for col in data.columns:
        nan_count = data[col].isna().sum()
        nan_count_list.append(nan_count)
        
        nan_pct = np.round((nan_count / nrows) * 100, decimals=3)

        if(nan_count > 0 and verbose == True):
            print(f' > column "{col}" has {nan_count} NaNs ({(nan_count/nrows)*100:.2f}%)')

        if(nan_pct >= del_threshold and verbose == True):
            data = data.drop(columns=[col])
            print(f' >>> Warning: Column deleted. Delete threshold={del_threshold}% \n')


    return data


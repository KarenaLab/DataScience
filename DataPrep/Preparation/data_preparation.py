
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



import numpy as np
import pandas as pd


def col_preparation(DataFrame, method="lower", verbose=True):
    """
    Standartize columns names.

    Variables:
    * DataFrame = DataFrame to be standartized,
    * method = lower, UPPER or Capitalize. (default=lower),
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

            elif(method == "capitalize"):
                new_col = new_col.capitalize()        


        data = data.rename(columns={col: new_col})

        if(verbose == True):
            print(f" > column {col} renamed for **{new_col}**")

    return data


# Duplicates

# Missing Data

# Data Format

# Consistency

# Standardization

# Histograms and related

# Transformation




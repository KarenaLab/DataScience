# Column checker and validation [P394]
# Tool for columns names checker and validation for graphs that uses
# DataFrames


# Libraries
import sys

import numpy as np
import pandas as pd


# Personal modules
sys.path.append(r"c:\python_modules")


# Functions
def col_select(DataFrame, columns="all"):
    """
    Validation for columns names for further analysis.
    Default for **columns** is all.

    """
    
    def column_checker(DataFrame, col_list):
        col_select = list()
        df_cols = DataFrame.columns.to_list()

        for i in col_list:
            if(df_cols.count(i) == 1):
                col_select.append(i)


        return col_select


    # Data preparation
    data = DataFrame.copy()

    # Columns preparation
    if(columns == "all"):
        # Default: Takes **all** columns from DataFrame
        col_select = data.columns.to_list()

    elif(isinstance(columns, str) == True):
        # Transforms a string into a list
        columns = columns.replace(" ", "")
        columns = columns.split(",")

        col_select = column_checker(data, columns)

    elif(isinstance(columns, list) == True):
        col_select = column_checker(data, columns)

    else:
        col_select = []


    return col_select


# end

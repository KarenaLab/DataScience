# One Hot Encoding [P200] ----------------------------------------------

# Libraries
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


# Versions:
# 01 - Feb 15th, 2023 - Starter
# 02 - Feb 20th, 2024 - Bugfix and adjusting


# Insights, improvements and bugfix
# 01 - Drop strategy (max, min, aleatory?)
# 



def one_hot_encoding(DataFrame, columns=[], sep="_",
                     verbose=True):
    """
    Performs One Hot Encoding with pd.get_dummies.

    Variables:
    * DataFrame = Pandas dataframe to be performed,
    * columns = list of variables to be performed one hot encoding,
    * col_drop = True* or False. If true, will remove the initial column,
    * sep = Separation sufix for the new column names. (default="_"),
    * verbose = True* or False (quiet mode). Prints important information
                about the operation.    

    """
    # Data preparation
    data = DataFrame.copy()

    for col in columns:
        if(data.columns.tolist().count(col) == 1):
            dummies = pd.get_dummies(data[col], prefix=col, prefix_sep=sep)

            # Control variables
            truth_table = {True: 1, False: 0}
            col_max_value = 0
            col_max_name = ""

            for dum_col in dummies.columns:
                if(is_numeric_dtype(dummies[dum_col]) == False):
                    dummies[dum_col] = dummies[dum_col].map(truth_table)

                col_count = dummies[dum_col].sum()

                if(col_count > col_max_value):
                    col_max_value = col_count
                    col_max_name = dum_col


            # Remove one of dummies column to avoid colinearity
            dummies = dummies.drop(columns=[col_max_name])
            data = data.join(dummies)

            # Remove the ´origin´ column
            data = data.drop(columns=[col])
                

        else:
            if(verbose == True):
                print(f' > Error: column "{col}" not found.') 


    return data


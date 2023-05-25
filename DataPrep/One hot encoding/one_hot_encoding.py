import numpy as np
import pandas as pd


def one_hot_encoding(DataFrame, columns=[], col_drop=True, sep="_",
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
    # Versions:
    # 01 - Feb 15th, 2023 - Starter
    # 02 -

    # Insigths:
    #
    
    # Program -----------------------------------------------------------
    data = DataFrame.copy()

    for col in columns:
        if(data.columns.tolist().count(col) == 1):
            dummies = pd.get_dummies(data[col], prefix=col, prefix_sep=sep)
            data = data.join(dummies)

            if(col_drop == True):
                data = data.drop(columns=[col])

        else:
            if(verbose == True):
                print(f' > Error: column "{col}" not found.') 


    return data


# Normatizations ------------------------------------------------------
# https://en.wikipedia.org/wiki/Normalization_(statistics)

# Versions
# 01 - Oct 21st, 2021 - Starter
# 02 - May 11th, 2022 - Adjusting for DataFrame
#


# Libraries
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


# Functions -----------------------------------------------------------

def norm_minmax(DF, columns, verbose=False):
    """
    Performs Min-Max normalization.
    More info: https://en.wikipedia.org/wiki/Normalization_(statistics)
    
    """

    data = DF.copy

    for col in columns:
        if(is_numeric_dtype(data[col]) == True):
            data_min = data[col].min()
            data_range = data[col].max() - data_min

            data[col] = data[col].apply(lambda x: (x-data_min)/(data_range))
            if(verbose == True):
                print(f" > Col {col}: Min-Max normalization applied")

        else:
            if(verbose == True):
                print(f" > Col {col}: *** Cannot perform Min-Max normalization (String) ***")

    return data



def Norm_StandScore(DF, columns, verbose=False):
    """
    Performs Standard Score normalization.
    More info: https://en.wikipedia.org/wiki/Normalization_(statistics)
    
    """

    data = DF.copy()

    for col in columns:
        if(is_numeric_dtype(data[col]) == True):
            data_mean = data[col].mean()
            data_stddev = data[col].std()

            data[col] = data[col].apply(lambda x: (x-data_mean)/data_stddev)
            if(verbose == True):
                print(f" > Col {col}: Standard Score ormalization applied")

        else:
            if(verbose == True):
                print(f" > Col {col}: *** Cannot perform Standard Score normalization (String) ***")

    return data            


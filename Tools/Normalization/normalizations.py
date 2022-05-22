# Normatizations
# https://en.wikipedia.org/wiki/Normalization_(statistics)

# Versions:
# 01 - Aug 11th, 2021 - Starter,
# 02 - May 21th, 2022 - Adjusting for Pandas options,
# 03 - May 21th, 2022 - Adding a dictionaty with parameters,
# 04 - 


# Libraries
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


# Min-Max normalization function
def normalize_minmax(DF, columns, verbose=False):
    """
    Returns the normalization by Min-Max strategy AND a dictionary
    with Minimum and Maximum for each normalization.
    
    """
    DF_temp = DF.copy()
    norm_params = {}


    if(isinstance(columns, str) == True):
       DF_temp = norm_minmax_(DF_temp, col, verbose)       

    if(isinstance(columns, pd.Index) == True or isinstance(columns, list) == True):
        for col in columns:
            DF_temp[col] = norm_minmax_(DF_temp[col], col, verbose)


    return DF_temp


def norm_minmax_(data, label, verbose):
    """
    Internal normalization Min-Max.
    Highly suggested to use normalize_minmax.

    """
    if(is_numeric_dtype(data) == True):
        data_min = data.min()
        data_max = data.max()

        data = (data - data_min)/(data_max - data_min)

        if(verbose == True):
            print(f" > col {label}: applied Min-Max normalization")     

    else:
        print(f" > col {label}: *** Error IS NOT numeric ***")


    return data


# Standard Score normalization function
def normalize_standscore(DF, columns, verbose=False):
    """
    Returns the normalization by Standard Score strategy AND a
    dictionary with Mean and Standard Deviation for each normalization.
    
    """
    DF_temp = DF.copy()
    norm_params = {}

    if(isinstance(columns, str) == True):
       DF_temp = norm_standscore_(DF_temp, col, verbose)       

    if((isinstance(columns, pd.Index) == True) or\
       (isinstance(columns, list) == True)):
        for col in columns:
            DF_temp[col] = norm_standscore_(DF_temp[col], col, verbose)


    return DF_temp   


def norm_standscore_(data, label, verbose):
    """
    Internal normalization Standard Score.
    Highly suggested to use normalize_standscore.

    """
    if(is_numeric_dtype(data) == True):
        data_mean = data.mean()
        data_stddev = data.std()

        data = (data - data_mean)/data_stddev

        if(verbose == True):
            print(f" > col {label}: applied Standard Score normalization")     

    else:
        print(f" > col {label}: *** Error IS NOT numeric ***")


    return data       


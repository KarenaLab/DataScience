
# EDA (Exploratory Data Analysis) for first look.

# Versions -------------------------------------------------------------
#01 - Jun 04th, 2022 - Starter

# Insights
#


# PROGRAM --------------------------------------------------------------

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype




def EDA_simple(DF, catnum=10, decimals=5, verbose=True):
    """
    Returns a simple EDA (Exploratory Data Analysis) for dataframe.
    
    """
    data = DF.copy()

    if(isinstance(data, pd.Series) == True):
        simple_(data, catnum, decimals, verbose)

    if(isinstance(data, pd.DataFrame) == True):
        for col in data.columns:
            simple_(data[col], catnum, decimals, verbose)


def simple_(data, catnum, decimals, verbose):
    """
    Internal function for EDA.
    
    """

    print("")
    data_name = data.name

    if(is_numeric_dtype(data) == True):
        data_nunique = data.nunique()
        
        if(data_nunique > catnum):
            data_count = data.count()
            data_nan = data.isna().sum()
            data_min = data.min()
            data_max = data.max()
            data_mean = data.mean()
            data_stddev = data.std()
            data_q25 = data.quantile(q=.25)
            data_median = data.quantile(q=.50)
            data_q75 = data.quantile(q=.75)

            # Printing EDA
            print(f" *** col: {data_name} ***")
            print(f" Uniques: {data_nunique}")
            print(f"   Count: {data_count}")
            print(f"    NaNs: {data_nan}")
            print(f"    Mean: {np.round(data_mean, decimals=decimals)}")
            print(f"  StdDev: {np.round(data_stddev, decimals=decimals)}")
            print(f"     Min: {np.round(data_min, decimals=decimals)}")
            print(f"    q25%: {np.round(data_q25, decimals=decimals)}")
            print(f"  Median: {np.round(data_median, decimals=decimals)}")
            print(f"    q75%: {np.round(data_q75, decimals=decimals)}")
            print(f"     Max: {np.round(data_max, decimals=decimals)}")

        else:
            if(verbose == True):
                print(f' **** col "{data_name}" IS categorical (unique={data_nunique}) ****') 

    else:
        if(verbose == True):
            print(f' **** col "{data_name}" IS NOT numeric ****')
          

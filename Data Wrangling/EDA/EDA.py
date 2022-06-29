
# EDA (Exploratory Data Analysis) for first look.

# Versions -------------------------------------------------------------
# 01 - Jun 04th, 2022 - Starter
# 02 - Jun 13th, 2022 - Adjusting and optmizing functions for Categoric
# 03 - Jun 27th, 2022 - Adding EDA Gaussian
# 04 -


# Insights
# Create a Date and/or Time EDA
#


# PROGRAM --------------------------------------------------------------

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype


def EDA_simple(DF, catnum=10, decimals=5, verbose=True):
    """
    Returns a simple EDA (Exploratory Data Analysis) for dataframe
    or Series.
    
    """

    data = DF.copy()

    if(isinstance(data, pd.Series) == True):
        simple_(data, catnum, decimals, verbose)

    if(isinstance(data, pd.DataFrame) == True):
        for col in data.columns:
            simple_(data[col], catnum, decimals, verbose)


def EDA_gaussian(DF, catnum=10, decimals=5, verbose=True):
    """
    Returns a Gaussian EDA (Exploratory Data Analysis) for dataframe
    or Series.
    
    """

    data = DF.copy()

    if(isinstance(data, pd.Series) == True):
        gaussian_(data, catnum, decimals, verbose)

    if(isinstance(data, pd.DataFrame) == True):
        for col in data.columns:
            gaussian_(data[col], catnum, decimals, verbose)
    


def simple_(data, catnum, decimals, verbose):
    """
    Internal function for EDA (Simple).
    
    """

    print("")
    data_name = data.name

    if(is_numeric_dtype(data) == True):
        # Stats common for Numeric and Categoric
        data_nunique = data.nunique()
        data_count = data.count()
        data_nan = data.isna().sum()

        if(data_nunique > catnum): data_type = "Numeric"
        if(data_nunique <= catnum): data_type = "Categoric"        

        # Type = Numerical
        if(data_type == "Numeric"):
            data_min = data.min()
            data_max = data.max()           
            data_mean = data.mean()
            data_stddev = data.std()
            data_q25 = data.quantile(q=.25)
            data_median = data.quantile(q=.50)
            data_q75 = data.quantile(q=.75)
            data_range = (data_max - data_min)

        # Type = Categoric
        if(data_type == "Categoric"):
            data_values = data.unique()
            data_values = np.sort(data_values)


        # Printing
        # Common for Numeric and Categoric
        print(f" *** col: {data_name} ***")
        print(f"    Type: {data_type}") 
        print(f" Uniques: {data_nunique}")
        print(f"   Count: {data_count}")
        print(f"    NaNs: {data_nan}")

        # Type = Numerical
        if(data_type == "Numeric"):
            print(f"    Mean: {np.round(data_mean, decimals=decimals)}")
            print(f"  StdDev: {np.round(data_stddev, decimals=decimals)}")
            print(f"     Min: {np.round(data_min, decimals=decimals)}")
            print(f"    q25%: {np.round(data_q25, decimals=decimals)}")
            print(f"  Median: {np.round(data_median, decimals=decimals)}")
            print(f"    q75%: {np.round(data_q75, decimals=decimals)}")
            print(f"     Max: {np.round(data_max, decimals=decimals)}")
            print(f"   Range: {np.round(data_range, decimals=decimals)}")

        # Type = Categoric
        if(data_type == "Categoric"):
            print(f"  Values: {data_values}")
             

    else:
        if(verbose == True):
            print(f' **** col "{data_name}" IS NOT Numeric ****')
            # Improve texts controls


def gaussian_(data, catnum, decimals, verbose):
    """
    Internal function for EDA (Gaussian).

    """

    print("")
    data_name = data.name
    data_nunique = data.nunique()

    if(is_numeric_dtype(data) == True):
        if(data_nunique > catnum):
            data_type = "Numeric"
            
            data_count = data.count()
            data_nan = data.isna().sum()

            data_min = data.min()
            data_max = data.max()           
            data_mean = data.mean()
            data_stddev = data.std()
            data_q25 = data.quantile(q=.25)
            data_median = data.quantile(q=.50)
            data_q75 = data.quantile(q=.75)

            data_iqr = data_q75 - data_q25
            data_range = data_max - data_min
            data_rangecoef = (data_max - data_min)/(data_max + data_min)
            data_quartiledeviation = (data_q75 - data_q25)/(data_q75 + data_q25)

            data_lowerlimit = data_mean - (3*data_stddev)
            data_upperlimit = data_mean + (3*data_stddev)
            data_outlierslow = (data < data_upperlimit).sum()
            data_outliersup = (data > data_upperlimit).sum()
            data_outliers = data_outlierslow + data_outliersup

            data_meandeviation = (data_mean - data_median)/data_stddev


            # Printing
            print(f" *** col: {data_name} ***")
            print(f"    Type: {data_type}") 
            print(f" Uniques: {data_nunique}")
            print(f"   Count: {data_count}")
            print(f"    NaNs: {data_nan}")
            print("")
            print(f"    Mean: {np.round(data_mean, decimals=decimals)}")
            print(f"  StdDev: {np.round(data_stddev, decimals=decimals)}")
            print(f"     Min: {np.round(data_min, decimals=decimals)}")
            print(f"    q25%: {np.round(data_q25, decimals=decimals)}")
            print(f"  Median: {np.round(data_median, decimals=decimals)}")
            print(f"    q75%: {np.round(data_q75, decimals=decimals)}")
            print(f"     Max: {np.round(data_max, decimals=decimals)}")
            print("")
            print(f"         IQR: {np.round(data_iqr, decimals=decimals)}")
            print(f"       Range: {np.round(data_range, decimals=decimals)}")
            print(f"  Range Coef: {np.round(data_rangecoef, decimals=decimals)}")
            print(f"Quartile Dev: {np.round(data_quartiledeviation, decimals=decimals)}")
            print(f"   Mean Dev*: {np.round(data_meandeviation, decimals=decimals)}")
            print("")
            print(f"    Outliers: {data_outliers}")
            print(f"Outliers Low: {data_outlierslow}")
            print(f" Outliers Up: {data_outliersup}")

            # print function to copy and paste
            # print(f": {np.round(data_, decimals=decimals)}")

            
        else:
            print(f' **** col "{data_name}" IS Categoric ****')


    else:
        if(verbose == True):
            print(f' **** col "{data_name}" IS NOT Numeric ****')
            
    
            

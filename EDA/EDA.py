# EDA

def EDA(data, decimals=5, **kwargs):
    """
    Performs EDA (Exploratory Data Analysis).
    Information returned:
    Numeric:   No. Items, No. NaNs, Mean, Standard Deviation, Minimum,
               Maximum, Range (or Amplitude) 25% Quantile, Median and
               75% Quantile.

    Categoric: No. Unique Items, Value Counting.
    
    """

    # Libraries
    import numpy as np
    import pandas as pd

    from pandas.api.types import is_numeric_dtype
    from pandas.api.types import is_string_dtype
    from pandas.api.types import is_bool_dtype


    # Versions ---------------------------------------------------------
    # 01 - Apr 22nd, 2022 - Launch
    # 02 -


    # Insights
    # Choose what type of information to return
    


    # Program ----------------------------------------------------------

    # Data = Pandas Series
    if(isinstance(data, list) == True):
        data = pd.Series(data)

    if(isinstance(data, np.ndarray) == True):
        data = pd.Series(data)

   
    # EDA
    data_label = data.name
    data_size = data.size


    # Testing Types
    is_numeric = is_numeric_dtype(data)
    is_text = is_string_dtype(data)
    is_bool = is_bool_dtype(data)
    

    # EDA for Numeric
    if(is_numeric == True):
        data_nan = np.isnan(data).sum()
        data_min = data.min()
        data_max = data.max()
        data_range = data_max - data_min

        data_mean = data.mean()
        data_stddev = data.std()

        data_q25 = np.quantile(data, q=0.25)
        data_median = np.quantile(data, q=0.50)
        data_q75 = np.quantile(data, q=0.75)

        # Showing information
        print(f" >>> Column: {data_label} \n")
        print(f"  No. Items: {data_size}")
        print(f"   No. NaNs: {data_nan}")
        print(f"       Mean: {np.round(data_mean, decimals=decimals)}")
        print(f"     StdDev: {np.round(data_stddev, decimals=decimals)}")
        print(f"      Range: {np.round(data_range, decimals=decimals)}")
        print(f"    Minimum: {np.round(data_min, decimals=decimals)}")
        print(f"       q_25: {np.round(data_q25, decimals=decimals)}")
        print(f"     Median: {np.round(data_median, decimals=decimals)}")
        print(f"       q_75: {np.round(data_q75, decimals=decimals)}")
        print(f"    Maximum: {np.round(data_max, decimals=decimals)}")
        print("")


    # EDA for Categoric
    if(is_text == True):

        # Showing information
        print(f" >>> Column: {data_label}")
        print(f" >>> data is CATEGORIC")
        print("")
    
        
    

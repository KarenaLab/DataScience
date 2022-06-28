# Database Classificator

def ColumnsClassifier(DF, cat_size=0.25, **kwargs):
    """
    Classifier for columns as Numeric, Categoric or Text.

    Variables:
    * cat_size = if: x >= 1     Number of items to be a threshold,
                     0 < x < 1  Percentage of items relative to the
                                size of DataFrame.
                                default = 0.25
    
    """

    import numpy as np
    import pandas as pd

    from pandas.api.types import is_numeric_dtype
    from pandas.api.types import is_string_dtype


    # Versions ---------------------------------------------------------

    # 01 - Oct 14th, 2021 - Starter
    # 02 - Apr 25th, 2022 - Adjusting variables and adding cat_size
    #                       variable.
    # 03 - 


    # Program ----------------------------------------------------------

    DF_columns = DF.columns

    numeric = []
    categoric = []
    text = []

    if(cat_size < 1):
        cat_size = DF.shape[0] * cat_size

    cat_size = int(cat_size + 0.5)

    for col in DF_columns:
        data = DF[col]
        data_unique = data.nunique()


        if(is_numeric_dtype(data) == True):
            if(data_unique > cat_size):
                numeric.append(col)

            else:
                categoric.append(col)


        if(is_string_dtype(data) == True):
            if(data_unique <= cat_size):
                categoric.append(col)

            else:
                text.append(col)


    return numeric, categoric, text


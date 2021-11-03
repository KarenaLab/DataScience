# Database Classificator

def ColumnsClassifier(DF):

    import numpy as np
    import pandas as pd

    from pandas.api.types import is_numeric_dtype
    from pandas.api.types import is_string_dtype


    # Versions ---------------------------------------------------------

    # 01 - Oct 14th, 2021 - Starter
    # 02 - 


    # List of Variables and kwargs -------------------------------------

    #
    #


    # Program ----------------------------------------------------------

    DF_Columns = DF.columns

    Numeric = []
    Categoric = []
    Text = []

    Cat_Size = 50


    for col in DF_Columns:

        Data = DF[col]
        Data_Unique = Data.nunique()


        if(is_numeric_dtype(Data) == True):

            if(Data_Unique > Cat_Size):
                Numeric.append(col)

            else:
                Categoric.append(col)


        if(is_string_dtype(Data) == True):

            if(Data_Unique <= Cat_Size):
                Categoric.append(col)

            else:
                Text.append(col)


    return Numeric, Categoric, Text


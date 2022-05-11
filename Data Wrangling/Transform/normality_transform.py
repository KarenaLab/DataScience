# Normality Transform --------------------------------------------------

# Versions
# 01 - May 02nd, 2022 - Starter
# 02 - May 05th, 2022 - Adding column control
# 03 - May 06th, 2022 - Adjusting mask
# 04 - May 10th, 2022 - Adding verbose control
#


# Libraries
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from scipy.stats import boxcox


# Functions ------------------------------------------------------------

def transform_log(DF, columns, verbose=True):
    """
    Performs Logaritmic transformation, EXCEPTS if there is negative
    numbers.
    
    """

    data = DF.copy()
    for col in columns:
        if(is_numeric_dtype(data[col]) == True):
            data_min = data[col].min()

            if(data_min > 0):
                data[col] = data[col].apply(lambda x: np.log(x))
                if(verbose == True):
                    print(f" > Col {col}: Log Transformation applied")

            else:
                if(verbose == True):
                    print(f" > Col {col} = *** Cannot perform Log transformation (Negative Number(s)) ***")

        else:
            if(verbose == True):
                print(f" > Col {col} = *** Cannot perform Log Tranformation (String) ***")
            
    return data


def transform_exp(DF, columns, c=3, verbose=True):
    """
    Perform Exponential transformation, raising the distribution by a
    power "c" (default=3) and could be a constant between 0 and 5.
    
    """
    
    data = DF.copy()

    for col in columns:
        if(is_numeric_dtype(data[col]) == True):
            data[col] = data[col].apply(lambda x: np.power(x, c))
            if(verbose == True):
                print(f" > Col {col}: Exp Transformation applied")

        else:
            if(verbose == True):
                print(f" > Col {col} = *** Cannot perform Exp Tranformation (String) ***")

    return data


def transform_boxcox(DF, columns, decimals=4, verbose=True):
    """
    Performs Box-Cox Transformation. The lmbda is the value used to fit
    the non-gaussian distribution to gaussian distribution. If you wish
    to perform the inverse box-cox, you need this value.

    Equation: y = (x ** (lmbda - 1))/lmbda  for  lmbda != 0,
                   log(x)                   for  lmbda = 0,

    Return: DataFrame transformed, list of lmbdas applied for each column
            If is not able to apply, will return NaN.

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boxcox.html
    https://www.ime.usp.br/~abe/lista/pdfQWaCMboK68.pdf (An Analysis of Tranformations)
    
    """

    data = DF.copy()
    lmbda_list = []

    for col in columns:
        if(is_numeric_dtype(data[col]) == True):
            data_min = data[col].min()

            if(data_min > 0):
                data[col], lmbda = boxcox(data[col])
                lmbda_list.append(lmbda)
                if(verbose == True):
                    print(f" > Col {col}: Box-Cox Transformation applied. (lmbda = {np.round(lmbda, decimals=decimals)})")                
            else:
                lmbda_list.append(np.nan)
                if(verbose == True):
                    print(f" > Col {col} = Cannot perform Box-Cox transformation (Negative Number(s))")

        else:
            lmbda_list.append(np.nan)
            if(verbose == True):
                print(f" > Col {col} = *** Cannot perform Box-Cox Tranformation (String) ***")
            
    return data, lmbda_list


def transform_reciprocal(DF, columns, verbose=True):
    """
    Performs a Reciprocal transformation using the INVERSE value.

    """
    
    data = DF.copy()

    for col in columns:
        if(is_numeric_dtype(data[col]) == True):
            data[col] = data[col].apply(lambda x: x ** (-1))
            if(verbose == True):
                print(f" > Col {col}: Reciprocal Transformation applied")

        else:
            if(verbose == True):
                print(f" > Col {col} = *** Cannot perform Reciprocal Tranformation (String) ***")

    return data


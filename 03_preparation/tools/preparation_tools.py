# Data Preparation Tools
# Short and small functions to help in data preparation

# Versions
# 01 - Jul 27th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------
def truncate(x, high, low=0):
    """
    Truncate the value **x** between **low** and **high**. 

    """
    if(x > high):
        x = high

    elif(x < low):
        x = low


    return x



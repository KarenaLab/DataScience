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


def linspacebystep(stop, step, start=0, cap=True):
    """
    Creates a linear space using the step as parameter for the number of values.

    """
    num = (stop - start) / step

    if(cap == True):
        num = int(num) + 1
    
    else:
        num = int(num + 0.5) + 1
    
    space = np.linspace(start=start, stop=stop, num=num)


    return space


def alpha_space():
    """
    Creates a numpy array with common alphas to be used for Ridge and Lasso regression
    hyperparameters.

    """
    alpha = np.append(np.array([]), linspacebystep(start=0.01, stop=0.05, step=0.01))
    alpha = np.append(alpha, linspacebystep(start=0.05, stop=0.5, step=0.05))
    alpha = np.append(alpha, linspacebystep(start=0.5, stop=1, step=0.1))
    alpha = np.append(alpha, linspacebystep(start=1, stop=10, step=1))
    alpha = np.append(alpha, linspacebystep(start=10, stop=20, step=2))

    alpha = np.round(alpha, decimals=3)
    alpha = np.sort(np.unique(alpha))


    return alpha


# end
    





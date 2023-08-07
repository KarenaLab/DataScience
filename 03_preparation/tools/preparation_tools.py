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
    space_list = [[0.01, 0.05, 0.01], [0.05, 0.5, 0.05], [0.5, 1, 0.1], [1, 10, 1], [10, 20, 2]]
    # parameters = [start, stop, step]

    alpha = np.array([])
    for (start, stop, step) in space_list:
        space = linspacebystep(start=start, stop=stop, step=step)
        alpha = np.append(alpha, space)

    # Removing duplicates and organizing (if necessary)
    alpha = np.round(alpha, decimals=4)
    alpha = np.sort(np.unique(alpha))


    return alpha


def clipped_relu(x, ceil):
    """
    Applies and returna the clipped ReLu to an input value.

    """
    if(x < 0): value = 0
    elif(x > ceil): value = ceil
    else: value = x

    return value


# end
    





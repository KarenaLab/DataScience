# Bins Strategy [P125] --------------------------------------------------

# Versions
# 01 - Jun 07th, 2023 - Starter
# 02 - Jan 04th, 2024 - Refactoring and adjusting as a module
# 03 - 


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

import warnings


# Setup/Config
warnings.filterwarnings("ignore")



# ----------------------------------------------------------------------
def bins_calculation(data, stat="median", verbose=False):
    """
    Calculates the various binning strategy and returns the selected
    stat (median*, min, max or mean).


    More info:
    https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges
    """
    # Data preparation
    data = np.array(data)
    data = data[~np.isnan(data)]        # Removing NaNs

    # Binning
    bins_list = list()
    bins_strategy = ["fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]

    for bs in bins_strategy:
        bins_count, bins_edges = np.histogram(data, bins=bs)
        bins_list.append(bins_count.size)


    # Select statistic
    if(stat == "median"):
        response = int(np.median(bins_list))

    elif(stat == "min" or stat == "minimum"):
        response = np.min(bins_list)

    elif(stat == "max" or stat == "maximum"):
        response = np.max(bins_list)

    elif(stat == "mean" or stat == "average"):
        response = int(np.mean(bins_list) + 0.5)

    else:
        response = int(np.median(bins_list))

        if(verbose == True):
            print("Warning: **stat** is not valid. Using the default value [median]")
        

    return response


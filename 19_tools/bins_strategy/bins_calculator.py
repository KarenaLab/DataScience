# Bins Calculator [P125] --------------------------------------------------

# Versions
# 01 - Jun 07th, 2023 - Starter
# 02 - Jan 04th, 2024 - Refactoring and adjusting as a module
# 03 - Mar 13th, 2024 - Code simplier, respect the unity.
#                       Rename for `bins_calculator`


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

import warnings


# Setup/Config
warnings.filterwarnings("ignore")


# ----------------------------------------------------------------------
def bins_calculator(data, stat="median", verbose=True):
    """
    Calculates the ideal number of **bins** for a given **data**

    More info:
    https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges
    """
    # Data preparation
    data = np.array(data)
    data = data[~np.isnan(data)]

    # Bins calculation
    bins_list = ["fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]
    bins = {x: np.histogram_bin_edges(data, bins=x).size for x in bins_list}

    # Strategy selection
    if(stat == "min"):
        no_bins = np.min(list(bins.values()))

    elif(stat == "max"):
        no_bins = np.max(list(bins.values()))

    elif(stat == "median"):
        no_bins = int(np.median(list(bins.values())))

    elif(bins_list.count(stat) == 1):
        no_bins = bins[stat]

    else:
        no_bins = np.nan

        if(verbose == True):
            print(f' > Warning: "stat={stat} is not valid')


    return no_bins


def bins_alloptions(data):
    """


    """
    # Data preparation
    data = np.array(data)
    data = data[~np.isnan(data)]

    bins_list = ["fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]
    bins = {x: np.histogram_bin_edges(data, bins=x).size for x in bins_list}

    return bins
    
    

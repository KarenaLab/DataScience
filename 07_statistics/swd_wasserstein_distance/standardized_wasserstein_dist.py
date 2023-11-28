# Wasserstein distance [P323] ------------------------------------------

# Libraries
import numpy as np
import pandas as pd

from scipy.stats import wasserstein_distance


# Version
# 01 - May 12th, 2023 - Starter

# Insights, bugfix and improvements
#


def standardized_wasserstein_dist(data_a, data_b):
    """
    Computes SWD (Standardized Wasserstein Distance) between sample A
    and sample B and standardized by its standard deviation.

    More information:
    * https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html
    * https://en.wikipedia.org/wiki/Wasserstein_metric

    """
    # Data preparation
    data_a = np.array(data_a)
    data_b = np.array(data_b)

    # Calc
    wasserstein_dist = wasserstein_distance(data_a, data_b)
    stddev_ab = np.std(np.concatenate([data_a, data_b]))

    if(stddev_ab != 0):
        swd = wasserstein_dist / stddev_ab

    else:
        swd = 0


    return swd


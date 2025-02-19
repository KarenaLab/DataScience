# [P481] Hellinger distance

# Versions
# 01 - Feb 19th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st


# ----------------------------------------------------------------------
def hellinger_distance(sample1, sample2):
    """
    Returns the Hellinger (H) distance between two probability
    distributions.
    
    Parameters:
    * sample1: True probability distribution.
    * sample2: Approximate probability distribution.
    
    """   
    # Data preparation  
    sample1 = np.array(sample1)
    sample2 = np.array(sample2)
    
    # Ensure the distributions sum to 1
    sample1 = sample1 / np.sum(sample1)
    sample2 = sample2 / np.sum(sample2)
    
    # Hellinger distance
    H = np.sqrt(np.sum((np.sqrt(sample2) - np.sqrt(sample1)) ** 2)) / np.sqrt(2)

    
    return H   


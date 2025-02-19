# [P480] Kullback-Leibler divergence

# Versions
# 01 - Fev 19th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from scipy.special import kl_div



# ----------------------------------------------------------------------
def kl_divergence(sample1, sample2):
    """
    Returns the Kullback-Leibler (KL) divergence between two
    probability distributions.
    
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
    
    # KL divergence
    KL = np.sum(np.where(sample1 != 0, sample1 * np.log(sample1 / sample2), 0))

    
    return KL  

   

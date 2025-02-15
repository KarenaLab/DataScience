# [P475] - Bootstrapping with the mean

# Versions
# 01 - Feb 01st, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st


# ----------------------------------------------------------------------
def bootstrap_with_mean(array, size=10, repeat=200, seed=None):
    """
    Algorithm to perform Bootstrap resampling of the mean.

    Steps:
    1. Draw a sample value with replacement with **size** pct,
    2. Calculate the mean of that sample,
    3. **Repeat** 1~2 steps,
    4. Calculate
       a. Calc the mean, standard deviation (and standard error),
       b. Generate histogram and/or boxplot,
       c. Find a confidence interval.

    Source: Practical statistics for Data Scientists (Peter and
            Andrew Bruce
            
    """
    # Data preparation
    array = array.flatten()
    sample_size = int(array.shape[0] * (size / 100))

    # Seed
    if(isinstance(seed, int) == True):
        np.random.seed(seed=seed)

    # Bootstrapping information
    bootstrap = np.array([])
    for i in range(0, repeat):
        sample = np.random.choice(array, size=sample_size, replace=True)

        sample_mean = np.mean(sample)
        bootstrap = np.append(bootstrap, sample_mean)


    # Information    
    bootstrap_mean = np.mean(bootstrap)
    bootstrap_stddev = np.std(bootstrap)
    ci_lower, ci_upper = confidence_interval(bootstrap)

    # Answer
    answer = dict()
    for var in ["bootstrap_mean", "bootstrap_stddev", "ci_lower", "ci_upper"]:
        answer[var] = locals()[var]

        
    return answer 


def confidence_interval(data, confidence=0.95):
    """
    A confidence interval is a range of values that estimates the true
    value of a population parameter (like a mean) with a certain level
    of confidence. It gives us an idea of how uncertain we are about our
    estimate.
    
    """
    # Data preparation
    data = np.array(data)

    # Confidence Interval calc
    mean = np.mean(data)
    se = st.sem(data)

    margin_error = se * st.t.ppf((1 + confidence) / 2, len(data)-1)

    lower = mean - margin_error
    upper = mean + margin_error


    return [lower, upper]


# end

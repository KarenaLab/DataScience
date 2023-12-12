# Data Preparation Tools [P355] ----------------------------------------
# Short and small functions to help in data preparation

# Versions
# 01 - Jul 27th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from time import time



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


def time_elapsed(time_in, decimals=3, verbose=True):
    """
    Calculate the time elapsed between **time_in** and the time that
    called this function.

    """
    time_out = time()
    elapsed = np.round(time_out - time_in, decimals=decimals)

    if(verbose == True):
        print(f"({elapsed} s)")


    return elapsed


def d_percentage(start, end, decimals=4):
    """
    Returns the differential percentage between **start** and **end**.

                end - start
    Equation = -------------
                  start
    
    """
    diff_pct = np.round(((end - start) / start), decimals=decimals)


    return diff_pct


def better_sample(loc, scale, size, error="dynamic", decimals=6, seed=None,
                  maximum=10000, verbose=True):
    """
    Creates a Gaussian distribution sample using ´np.random.normal´ but
    controls the error from **mean** and **standard deviation**, keeping
    it closer to the gap controled by the **error**.

    """
    # Seed (optional)
    if(seed != None and isinstance(seed, int) == True):
        np.random.seed(seed)


    # Error
    if(error == "dynamic"):
        error = 0.001


    # Rolling the dice ;)
    i = 0

    while(True):
        sample = np.random.normal(loc=loc, scale=scale, size=size)
        sample = np.round(sample, decimals=decimals)

        sample_mean = np.mean(sample)
        sample_stddev = np.std(sample)


        # Test conditions
        if(sample_mean >= (loc - error) and sample_mean <= (loc + error) and
           sample_stddev >= (scale - error) and sample_stddev <= (scale + error)):
            break


        i = i + 1

        # Upgrade the error, make it bigger because the conditions does not fit
        # the loc, scale and error.
        if(i == maximum):
            error_list = [0.001, 0.01, 0.1, 0.5, 1, 2, 5, 10, 20, 50, 100]

            try:
                pos = error_list.index(error)

            except ValueError:
                error = error_list[min(range(0, len(error_list)), key=lambda i: abs(error_list[i] - error))]
                pos = error_list.index(error)


            pos = pos + 1
            error = error_list[pos]
            i = 0

            if(verbose == True):
                print(f" > Message: Error range updated. {error=}")


    return sample


def gaussian_curve(loc, scale, size=1000, slide=4):
    """
    Returns x and y for a perfect gaussian curve fitted (Normal).
    Using the function: ´st.norm.pdf()`

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

    """
    x = np.linspace(start=(loc - (slide * scale)), stop=(loc + (slide * scale)), num=size)
    y = st.norm.pdf(x, loc=loc, scale=scale)

    return x, y


# end

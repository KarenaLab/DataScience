# Print Results [P365]

# Versions
# 01 - Aug 23rd, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
# 01 - Add data treatment in the inputation of data (line 31)
# 02 - Add maximum number of data fields permited
# 03 - 


# Libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------
def name(results, decimals, selection=["model", "alpha", "mse", "mae", "r2_score"],
                                       show_title=False):
    """
    Friendly visualization of model results (print at the Terminal).
    Works with results dictionary.

    """
    datafields_list = selection
    # Add maximum fields number
    
    outfit = dict()

    # Data collection and preparation
    for d in datafield_list:
        if(d in results):
            data = results[d]
            # Data type treatment

        else:
            data = ""

        output[d] = data


    # Print data
    if(show_title == True):
        print(f"{datafields_list[0]:>{20}} - {datafields_list[1]:>10}{datafields_list[2]:>10}{datafields_list[3]:>10}{datafields_list[4]:>10}")

    print(f'{output["model"]:>20} - {output["alpha"]:>10}{output["mse"]:>10.4f}{output["mae"]:>10.4f}{output["r2_score"]:>10.4f}')

    
    return None 

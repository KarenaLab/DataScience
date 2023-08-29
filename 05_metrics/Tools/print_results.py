# Print Results [P365] -------------------------------------------------

# Versions
# 01 - Aug 23rd, 2023 - Starter
# 02 - 


# Insights, improvements and bugfix
# 01 - Add data treatment in the inputation of data (line 42)
# 02 - Add maximum number of data fields permited (Aug 29th, 2023)
# 03 - 


# Libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------
def print_results(results, decimals=4,
                  selection=["model", "alpha", "mse", "mae", "r2_score"],
                  show_title=False):
    """
    Friendly visualization of model results (print at the Terminal).
    Works with results dictionary.

    """
    # Column preparation
    n = len(selection)

    if(n <= 6):
        col_size = 48 // (n - 1)
        name_size = 68 - (col_size * (n - 1))

        # Data collection and preparation        
        datafields = selection
        output = dict()
    
        for d in datafields:
            if(d in results):
                data = results[d]
                # Data type treatment

            else:
                data = ""

            output[d] = data


        # Print data
        if(show_title == True):
            print(f"{datafields[0]:>{name_size}} - ", end="")

            for x in range(1, len(selection)):
                print(f"{datafields[x]:>{col_size}}", end="")

            print("")


        print(f"{output[datafields[0]]:>{name_size}} - ", end="")

        for x in range(1, len(selection)):
            print(f"{output[datafields[x]]:>{col_size}}", end="")

        print("")


    else:
        print(f" > Warning: Number of columns exceeds 6")
        
    
    return None 


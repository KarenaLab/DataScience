# [P203] EDA Describe

# Versions
# 01 - Mar 22rd, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt

# Personal Libraries
import sys
sys.path.append(r"c:\python_modules")

from eda_taxonomy import eda_taxonomy
from plot_histbox import plot_histbox
from plot_barh import plot_barh



# ----------------------------------------------------------------------
def eda_describe(DataFrame, columns=None, n_unique=15):
    """


    """
    # Columns preparation
    if(columns == None):
        columns = DataFrame.columns


    # Columns taxonomy
    taxonomy = eda_taxonomy(DataFrame, n_unique=n_unique, verbose=False)

    for col, clf in zip(taxonomy.keys(), taxonomy.values()):
        data = DataFrame[col]

        if(clf == "Numerical" or clf == "Discrete"):
            plot_histbox(data)

        elif(clf == "Categorical" or clf == "Boolean"):
            plot_barh(data)

        else:
            pass
        

    return None
        

# Program
if(__name__ == "__main__"):
    df = pd.read_csv("auto_mpg.csv", sep=",", encoding="utf-8")
    tax = eda_describe(df)
    
    # end
    

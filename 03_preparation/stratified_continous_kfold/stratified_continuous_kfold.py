# Name [P305] Stratified Continuous KFold
# Applies the stratified KFold for targets wirh Continuous

# Versions
# 01 - Jan 03rd, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import warnings

import numpy as np
import pandas as pd

from sklearn.model_selection import StratifiedKFold


# Setup/Config
warnings.filterwarnings("ignore")



# ----------------------------------------------------------------------
def target_split(DataFrame, target):
    """
    Splits variable(s) and **target** from the **DataFrame**

    """
    columns = DataFrame.columns.to_list()
    
    if(columns.count(target) == 1):
        x = DataFrame.drop(columns=[target])
        y = DataFrame[target]

    else:
        x = np.nan
        y = np.nan


    return x, y


# end


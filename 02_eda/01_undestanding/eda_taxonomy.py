# [P505] EDA Taxonomy

# Versions
# 01 - Mar 15th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd



# ----------------------------------------------------------------------
def eda_taxonomy(DataFrame, n_unique=15):
    """


    """
    cols_classification = dict()

    for col in DataFrame.columns:
        col_type = DataFrame[col].dtype

        if(col_type == np.int64 or col_type == np.float64):
            unique_vals = DataFrame[col].nunique()
            if(unique_vals < n_unique):
                cols_classification[col] = "Ordinal"

            else:
                cols_classification[col] = "Numerical"

        elif(col_type == "object"):
            cols_classification[col] = "Categorical"

        elif(col_type == "bool"):
             cols_classification[col] = "Boolean"

        else:
            cols_classification[col] = "Unknown"
            
                   
    return cols_classification    


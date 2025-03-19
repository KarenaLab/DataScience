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
def eda_taxonomy(DataFrame, n_unique=15, verbose=True):
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


    if(verbose == True):
        print_results(cols_classification)
            
                   
    return cols_classification    


def print_results(dictionary):
    """


    """
    # Print header
    print(f"{'Columns':46s}  {'type':>12s}")       # 46 + 2 + 12 = 60
    print("-" * 60)

    for col_name, col_type in zip(dictionary.keys(), dictionary.values()):
        print(f"{col_name:46s}  {col_type:>12s}")

    print("-" * 60)
    
    return None

      

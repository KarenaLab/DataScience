
import numpy as np
import pandas as pd


def target_split(DF, target, verbose=False):
    """
    Split into two datasets with variables (DF_var) and target (DF_target).

    """

    variables = DF.columns.to_list()
    if(variables.count(target) == 1):
        variables.remove(target)

        df_var = DF[variables]
        df_target = DF[target]

        if(verbose == True):
            print(f" > Variables and Target dataframe splited")

    else:
        if(variables.count(target) == 0):
            print(f" > *** Target '{target}' not found ***")

        if(variables.count(target) > 1):
            print(f" > *** Target not unique, check Dataframe columns names ***")
            
        df_var = None
        df_target = None


    return df_var, df_target
    
    

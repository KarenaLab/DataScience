# Results analysis [P367] ----------------------------------------------

# Versions
# 01 - Sep 13th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------

def flatten_list(array):
    """
    Turns a list of lists into a flat list.
    
    """
    flatten = list()
    
    for sub_list in array:
        for i in sub_list:
            flatten.append(i)


    return flatten


def append_results(DataFrame, new_results):
    """
    Append a **new_results** as dictionary, pandas series or pandas
    dataframe into **DataFrame**.

    """
    if(isinstance(new_results, dict) == True):
        new_results = pd.Series(new_results).to_frame()


    if(isinstance(new_results, pd.Series) == True):
        DataFrame = pd.concat([DataFrame, new_results.T], ignore_index=True)


    elif(isinstance(new_results, pd.DataFrame) == True):
        DataFrame = pd.concat([DataFrame, new_results], ignore_index=True)

    else:
        DataFrame = list() 


    return DataFrame


def results_to_dataframe(results):
    """
    Converts a list of dictionaries with models results into a DataFrame.

    """
    results = flatten_list(results)
    data = pd.DataFrame(data=[])
    
    if(isinstance(results, list) == True):       
        for i in results:
            line = pd.Series(data=i)
            data = pd.concat([data, line.T], ignore_index=True)
            
            
    return data


# end

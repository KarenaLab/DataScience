
# Libraries
import numpy as np
import pandas as pd

from pca_analysis_v02 import *


# Functions
def split_target(DataFrame, target):
    """
    Splits **Dataframe** into x (variables) and y (target).

    """
    if(DataFrame.columns.tolist().count(target) == 1):
        x = df.drop(columns=[target])
        y = df[target]

    else:
        x = np.nan
        y = np.nan


    return x, y
        


# Program --------------------------------------------------------------
df = pd.read_csv("winequality_red.csv", sep=",", encoding="utf-8")

x, y = split_target(df, target="quality")

title = "PCA Analysis - Wine Quality Red dataset"
df_pca, pca_variance = pca_analysis(x, title, savefig=False)


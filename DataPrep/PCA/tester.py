
import numpy as np
import pandas as pd

from PCA_analysis_v01 import *


DF = pd.read_csv("winequality_red.csv", sep=",", encoding="utf-8")

target = "quality"
DF_var = DF.drop(columns=[target])
DF_target = DF[target]

title = "PCA Analysis"
PCA_analysis(DF_var, title)



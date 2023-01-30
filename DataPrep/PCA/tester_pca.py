
import numpy as np
import pandas as pd

from PCA_analysis_v01 import *


df = pd.read_csv("winequality_red.csv", sep=",", encoding="utf-8")

target = "quality"
df_var = df.drop(columns=[target])
df_target = df[target]

title = "PCA Analysis - Wine Quality Red dataset"
df_pca, pca_variance = pca_analysis(df_var, title, savefig=False)


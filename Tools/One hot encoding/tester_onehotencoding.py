
import numpy as np
import pandas as pd

from one_hot_encoding_v01 import *


filename = "insurance.csv"
df = pd.read_csv(filename, sep=",", encoding="utf-8")

cols_categoric = ["sex", "children", "smoker", "region", "test"]
df = one_hot_encoding(df, columns=cols_categoric)

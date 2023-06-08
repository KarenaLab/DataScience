
# Libraries
import numpy as np
import pandas as pd

from bins_strategy_v01 import *


# Setup/Config



# Program --------------------------------------------------------------
filename = "hmeq.csv"
df = pd.read_csv(filename, sep=",", encoding="utf-8")

col_values = ["LOAN", "MORTDUE", "VALUE", "YOJ", "DEROG", "DELINQ",
              "CLAGE", "NINQ", "CLNO", "DEBTINC"]

for col in col_values:
    bins_strategy(df[col])


bins_strategy(df["DEBTINC"], savefig=True)

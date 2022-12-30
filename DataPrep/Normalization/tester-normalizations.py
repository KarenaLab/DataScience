
# Libraries
import os

import numpy as np
import pandas as pd

from normalizations_v04 import *




# Program --------------------------------------------------------------

# Path Control
path_main = os.getcwd()
path_database = r"D:\01 - Projects Binder\03 - Databases"


# Data import
os.chdir(path_database)
filename = "housing.csv"
df = pd.read_csv(filename, sep=",", encoding="utf-8")

df = normalize_standscore(df, columns=["longitude", "latitude"])


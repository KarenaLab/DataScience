
import os

import numpy as np
import pandas as pd

from normalizations_v03 import *


# Program --------------------------------------------------------------

filename = "housing.csv"
DF = pd.read_csv(filename, sep=",", encoding="utf-8")

DF_copy = DF.copy()
DF = normalize_standscore(DF, columns=["longitude", "latitude"])


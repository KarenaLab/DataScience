# Time Series Exercise [P452]

# Libraries
import os


import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# Personal modules
from imputing_techniques import *


# Functions
def load_dataset():
    filename = "rainfall.csv"
    data = pd.read_csv(filename, sep=",", encoding="utf-8")

    return data


# Setup/Config



# Program --------------------------------------------------------------
df = load_dataset()
df_copy = df.copy()

# Columns
columns = list(df.columns)
columns.remove("datetime")

df = insert_nans(df, columns=columns, percentage=10)


# end
df_mean = df.copy()
df_mean = fill_mean(df_mean, columns=columns)

df_median = df.copy()
df_median = fill_median(df_median, columns=columns)

df_zeros = df.copy()
df_zeros = fill_zeros(df_zeros, columns=columns)

df_linear = df.copy()
df_linear = fill_interpolate(df_linear, columns=columns, method="linear")

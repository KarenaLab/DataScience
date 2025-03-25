# [P479] DBSCAN for outliers detection

# Versions
# 01 - Feb 12th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st

from sklearn.cluster import DBSCAN

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
def make_DBSCAN(DataFrame, var_1, var_2, eps=0.5, min_samples=5):
    
    # Selection of data
    data = DataFrame[[var_1, var_2]]
    data = data.dropna()

    # Prepare data scale
    data[var_1] = scaler_standard(data[var_1])
    data[var_2] = scaler_standard(data[var_2])    
    
    vector = pair_variables(data, var_1, var_2)

    # DBSCAN (Density-Based Spatial Clustering of Applications
    # with Noise)
    db = DBSCAN(eps=eps, min_samples=min_samples)
    db.fit(vector)

    labels = list(db.labels_)
    data["labels"] = labels
    
    # Cluster color
    colors = saintgobain_palette()
    colors = list(colors.values())
    colors.insert(0, "#000000")

    colors = dict(zip(np.unique(labels), colors[0:len(labels)]))
    data["colors"] = data["labels"].map(colors)
            
    return data  


def scaler_minmax(Series):
    # Data preparation
    x_min = np.min(Series)
    x_max = np.max(Series)

    scaled = list()
    for x in Series:
        x_scaled = (x - x_min) / (x_max - x_min)
        scaled.append(x_scaled)

    return scaled, x_min, x_max


def scaler_standard(Series):
    # Data preparation
    x_mean = np.mean(Series)
    x_stddev = np.std(Series)

    scaled = list()
    for x in Series:
        x_scaled = (x - x_mean) / x_stddev
        scaled.append(x_scaled)

    return scaled, x_min, x_max


def pair_variables(DataFrame, var_1, var_2):
    # Data selection
    x = np.array(DataFrame[var_1])
    y = np.array(DataFrame[var_2])

    vector = list()
    for xi, yi in zip(x, y):
        vector.append([xi, yi])

    return vector


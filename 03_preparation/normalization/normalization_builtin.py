
# Normalization [P345] -------------------------------------------------

# Versions
# 01 - Jun 27th, 2023 - Starter
# 02 -


# Insights and Bugfix
# Return parameters from normalization


# Libraries
import os

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def scaler_standardscore(x_train, x_test):
    """
    Applies Standard Score from scikit-learn library to x_train and
    replies it for x_test.

    More info:
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

    """
    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)


    return x_train, x_test


def scaler_minmax(x_train, x_test):
    """
    Applies Standard Score from scikit-learn library to x_train and
    replies it for x_test.

    More info:
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html

    """
    scaler = MinMaxScaler()
    scaler.fit(x_train)

    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)


    return x_train, x_test


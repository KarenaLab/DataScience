
# Linear Regression Module ---------------------------------------------

# Versions
# 01 - Jun 27th, 2023 - Starter
# 02 -

# Insights and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression


# Personal modules
import sys
sys.path.append(r"C:\python_modules")

from regr_metrics import *



def regr_linreg(x_train, y_train, x_test, y_test,
                fit_intercept=True, positive=False, metrics="all"):
    """
    Module to perform a **Linear Regression** using scikit-learn module
    and adding some features to help to have more control over modules and
    parameters.

    """
    model = LinearRegression()

    # Parameters
    model.fit_intercept = fit_intercept
    model.positive = positive
    hiperparams = {"fit_intercept": fit_intercept, "positive": positive}

    # Fit, predict and parameters
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    params = {"intercept": model.intercept_, "coef": model.coef_}

    # Metrics
    model_metrics = regr_metrics(y_test, y_pred, metrics=metrics)
    model_metrics["model"] = "Linear Regression"

    # Results
    results = {}
    results.update(hiperparams)
    results.update(params)
    results.update(metrics)

    return results


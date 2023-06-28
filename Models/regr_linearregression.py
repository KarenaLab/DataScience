
# Linear Regression Module ---------------------------------------------

# Versions
# 01 - Jun 27th, 2023 - Starter
# 02 - Jun 28th, 2023 - Added Ridge and Lasso
# 03 - 

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

    More info:
    https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

    """
    model = LinearRegression()

    # HiperParameters
    model.fit_intercept = fit_intercept
    model.positive = positive
    hiperparams = {"fit_intercept": fit_intercept, "positive": positive}

    # Fit, predict and parameters
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    params = {"intercept": model.intercept_, "coef": model.coef_}

    # Metrics
    metrics = regr_metrics(y_test, y_pred, metrics=metrics)
    metrics["model"] = "Linear Regression"

    # Results
    results = {}
    results.update(hiperparams)
    results.update(params)
    results.update(metrics)

    return results


def regr_ridge(x_train, y_train, x_test, y_test,
               alpha=1, fit_intercept=True, positive=False, metrics="all"):
    """
    Module to perform a **Ridge Regression (L2)** using scikit-learn module
    and adding some features to help to have more control over modules and
    parameters.

    More info:
    https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html

    """
    model = Ridge()

    # HiperParameters
    model.alpha = alpha
    model.fit_intercept = fit_intercept
    model.positive = positive
    hiperparams = {"alpha": alpha, "fit_intercept": fit_intercept, "positive": positive}

    # Fit, predict and parameters
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    params = {"intercept": model.intercept_, "coef": model.coef_}

    # Metrics
    metrics = regr_metrics(y_test, y_pred, metrics=metrics)
    metrics["model"] = "Ridge"

    # Results
    results = {}
    results.update(hiperparams)
    results.update(params)
    results.update(metrics)

    return results


def regr_lasso(x_train, y_train, x_test, y_test,
               alpha=1, fit_intercept=True, positive=False, metrics="all"):
    """
    Module to perform a **Lasso Regression (L1)** using scikit-learn module
    and adding some features to help to have more control over modules and
    parameters.

    More info:
    https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html

    """
    model = Lasso()

    # HiperParameters
    model.alpha = alpha
    model.fit_intercept = fit_intercept
    model.positive = positive
    hiperparams = {"alpha": alpha, "fit_intercept": fit_intercept, "positive": positive}

    # Fit, predict and parameters
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    params = {"intercept": model.intercept_, "coef": model.coef_}

    # Metrics
    metrics = regr_metrics(y_test, y_pred, metrics=metrics)
    metrics["model"] = "Ridge"

    # Results
    results = {}
    results.update(hiperparams)
    results.update(params)
    results.update(metrics)

    return results


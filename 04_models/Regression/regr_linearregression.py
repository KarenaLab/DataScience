
# Linear Regression Module [P346] --------------------------------------

# Versions
# 01 - Jun 27th, 2023 - Starter
#      Jun 28th, 2023 - Add Ridge and Lasso
# 02 - Sep 01st, 2023 - Return y_pred with results
# 03 - Sep 09th, 2023 - Adding Grid Search
# 

# Insights, improvements and bugfix
# Add ElasticNet model
#


# Libraries
import numpy as np
import pandas as pd
import itertools

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso


# Personal modules
import sys
sys.path.append(r"C:\python_modules")

from regr_metrics import *
# using functions **regr_metrics** and **append_results**


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
    hiperparams = {"model": "Linear Regression",
                   "fit_intercept": fit_intercept,
                   "positive": positive}

    # Fit, predict and parameters
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    
    params = {"intercept": model.intercept_, "coef": model.coef_}

    # Metrics
    metrics = regr_metrics(y_test, y_pred, metrics=metrics)

    # Results
    results = {}
    results.update(hiperparams)
    results.update(params)
    results.update(metrics)

    return results, y_pred


def gridsearch_linreg(x_train, y_train, x_test, y_test, metrics="all"):
    """
    Module to perform Grid Search with **Linear Regression** using
    scikit-learn module and adding some features to help to have more
    control over modules and parameters.

    More info:
    https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    
    """
    # Hiperparameters selection for Linear Regression
    fit_intercept = [True, False]
    positive = [False, True]


    # Grid Search
    gs_results = pd.DataFrame(data=[])
    parameters = itertools.product(fit_intercept, positive)
    
    for fi, p in parameters:
        results, _ = regr_linreg(x_train, y_train, x_test, y_test,
                                 fit_intercept=fi, positive=p, metrics=metrics)

        gs_results = append_results(gs_results, results)
        
        
    return gs_results


def regr_ridge(x_train, y_train, x_test, y_test,
               alpha, fit_intercept=True, positive=False, metrics="all"):
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
    hiperparams = {"model": "Ridge",
                   "alpha": alpha,
                   "fit_intercept": fit_intercept,
                   "positive": positive}

    # Fit, predict and parameters
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    params = {"intercept": model.intercept_, "coef": model.coef_}

    # Metrics
    metrics = regr_metrics(y_test, y_pred, metrics=metrics)

    # Results
    results = {}
    results.update(hiperparams)
    results.update(params)
    results.update(metrics)

    return results, y_pred


def regr_lasso(x_train, y_train, x_test, y_test,
               alpha, fit_intercept=True, positive=False, metrics="all"):
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
    hiperparams = {"model": "Lasso",
                   "alpha": alpha,
                   "fit_intercept": fit_intercept,
                   "positive": positive}

    # Fit, predict and parameters
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    params = {"intercept": model.intercept_, "coef": model.coef_}

    # Metrics
    metrics = regr_metrics(y_test, y_pred, metrics=metrics)

    # Results
    results = {}
    results.update(hiperparams)
    results.update(params)
    results.update(metrics)

    return results, y_pred


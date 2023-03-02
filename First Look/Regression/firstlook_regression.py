
# Libraries
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet


# Personal modules
import sys
sys.path.append(r"C:\python_modules")

from metrics_regression import *


# Functions ------------------------------------------------------------

def regr_linearregression(x_train, y_train, x_test, y_test,
                          fit_intercept=True, positive=False,
                          metrics="mae", verbose=True):
    """
    Performs a Linear Regression (OLS) using scikit-learn library.

    """
    # Model = Linear Regression (OLS)
    regr = LinearRegression()

    # Model parameters
    regr.set_params(fit_intercept=fit_intercept)
    regr.set_params(positive=positive)

    regr_params = regr.get_params()
    regr_params.pop("copy_X")
    regr_params.pop("n_jobs")
    
    regr_params = {"regr_name": "Lin Regression"} | regr_params

    # Fit, predict and coeficients
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    weights = {"intercept": regr.intercept_, "coefs": regr.coef_}
    results = regr_metrics(y_test, y_pred, metrics=metrics, verbose=verbose)

    
    return weights, regr_params, results 


def regr_lr_ridge(x_train, y_train, x_test, y_test,
                  alpha=1, fit_intercept=True, positive=False,
                  metrics="all", verbose=True):
    """
    Performs a Linear Regression with Ridge (L2) penalization using
    scikit-learn library.

    """
    # Model = Linear Regression with Ridge (L1) penalisation
    regr = Ridge()

    # Model parameters
    regr.set_params(alpha=alpha)
    
    regr_params = regr.get_params()
    regr_params.pop("copy_X")
    
    regr_params = {"regr_name": "LinRegr Ridge"} | regr_params

    # Fit, predict and coeficients
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    weights = {"intercept": regr.intercept_, "coefs": regr.coef_}
    results = regr_metrics(y_test, y_pred, metrics=metrics, verbose=verbose)

    return weights, regr_params, results


def regr_lr_lasso(x_train, y_train, x_test, y_test,
                  alpha=1, fit_intercept=True, positive=False,
                  metrics="all", verbose=True):
    """
    Performs a Linear Regression with Lasso (L1) penalization using
    scikit-learn library.

    """
    # Model = Linear Regression with Lasso (L2) penalisation
    regr = Lasso()

    # Model parameters
    regr.set_params(alpha=alpha)
    
    regr_params = regr.get_params()
    regr_params.pop("copy_X")
    regr_params = {"regr_name": "LinRegr Lasso"} | regr_params

    # Fit, predict and coeficients
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    weights = {"intercept": regr.intercept_, "coefs": regr.coef_}
    results = regr_metrics(y_test, y_pred, metrics=metrics, verbose=verbose)

    return weights, regr_params, results


def regr_elasticnet(x_train, y_train, x_test, y_test,
                    alpha=1, l1_ratio=0.5, fit_intercept=True, positive=False,
                    metrics="all", verbose=True):
    """
    Performs a Linear Regression combined L1 and L2 priors as regularizer.
    using scikit-learn library.

    """
    # Model = Linear Regression with ElasticNet (L1 and L2) penalisation
    regr = ElasticNet()

    # Model parameters
    regr.set_params(alpha=alpha)
    regr.set_params(l1_ratio=l1_ratio)

    regr_params = regr.get_params()
    regr_params.pop("copy_X")
    regr_params = {"regr_name": "LinRegr ElasticNet"} | regr_params

    # Fit, predict and coeficients
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    weights = {"intercept": regr.intercept_, "coefs": regr.coef_}
    results = regr_metrics(y_test, y_pred, metrics=metrics, verbose=verbose)

    return weights, regr_params, results


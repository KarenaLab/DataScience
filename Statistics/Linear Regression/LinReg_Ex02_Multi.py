# ***  Regression Linear  ***
#
#  Project: Regression Linear
# Filename: LinReg_Ex01
#  Creator: EKChikui (EKChikui@gmail.com)
#     Date: 24th May 2021
#  Version: 01
#
# -----------------------------------------------------------------------

# Libraries -------------------------------------------------------------

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics

import statsmodels.api as sm
 
from sklearn.datasets import load_diabetes



# Setup -----------------------------------------------------------------



# MAIN Program ----------------------------------------------------------

print(f"\n *****  Linear Regression | Diabetes Database  ****\n")

DF = load_diabetes()

features = pd.DataFrame(DF['data'], columns= DF['feature_names'])
target = pd.Series(DF['target'], name= 'target')

columns = ['age', 'bmi', 'bp', 's3', 's5']

X = features['bmi'].values.reshape(-1,1)
y = target.values.reshape(-1,1)

printing = False

if(printing == True):

    for i in columns:

        plt.scatter(features[i], y)
        plt.title(str(i))

        plt.grid(linestyle= "--")
        plt.show()



X = features[columns]

# 70% training data, 30% validation data
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size= 0.2, random_state= 6) 

multi = LinearRegression()
multi.fit(X_train, y_train) 

Coef = multi.coef_
Interc = multi.intercept_

pred = multi.predict(X_val)

MSE = metrics.mean_squared_error(y_val, pred)
MAE = metrics.mean_absolute_error(y_val, pred)


# add constant (intercept) manually
X_train = sm.add_constant(X_train)
model = sm.OLS(y_train, X_train).fit()
model.summary()


# Closing

print("")



# Sources ---------------------------------------------------------------

# 

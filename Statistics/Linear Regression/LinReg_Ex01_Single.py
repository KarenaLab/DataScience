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
import sklearn.metrics as metrics
 
from sklearn.datasets import load_diabetes



# Setup -----------------------------------------------------------------



# MAIN Program ----------------------------------------------------------

print(f"\n *****  Linear Regression | Diabetes Database  ****\n")

DF = load_diabetes()

features = pd.DataFrame(DF["data"], columns= DF["feature_names"])
target = pd.Series(DF["target"], name= "target")

X = features["bmi"].values.reshape(-1,1)
y = target.values.reshape(-1,1)

simple = LinearRegression()
simple.fit(X,y)

coef = simple.coef_[0][0]
inter = simple.intercept_[0]

print(f" >> coef = {coef:.4f}; intercept = {inter:.4f}")

calc_pred = simple.intercept_ + (X*simple.coef_)
pred = simple.predict(X)

(calc_pred == pred).all()

MSE = metrics.mean_squared_error(y, pred)
MAE = metrics.mean_absolute_error(y, pred)

print(f" >> MAE = {MAE}; MSE = {MSE}")


# Plotting

fig, ax = plt.subplots(figsize= (10, 5.62)) # Wide

# Plot Actual Values = SCATTER
ax.scatter(X, y, color= "royalblue", edgecolor= "white", label="Actual")

# plot Predicted Values = LINE
ax.plot(X, pred, color= "red", label= "Prediction")

# Graph Features
fig.suptitle("Simple Linear Regression", size= 14)

ax.set_xlabel("Feature X")
ax.set_ylabel("Target y")

ax.grid(axis= "both", color= "lightgrey")
ax.set_axisbelow(True)


#plt.tight_layout()
plt.legend(loc= "best")

plt.savefig("Simple_Reg", dpi= 240)
plt.show() 


# Closing

print("")



# Sources ---------------------------------------------------------------

# 

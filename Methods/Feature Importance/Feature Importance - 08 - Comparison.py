
import numpy as np
import pandas as pd

from sklearn.datasets import make_classification

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.inspection import permutation_importance


from sklearn.neighbors import KNeighborsRegressor
from sklearn.inspection import permutation_importance

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Program --------------------------------------------------------------

print("\n ****  Feature Importance  **** \n")

Data_X, Data_Y = make_classification(n_samples= 1000, n_features= 10,
                                     n_informative= 5, n_redundant= 5,
                                     random_state= 27)


DecTree = DecisionTreeRegressor()
DecTree.fit(Data_X, Data_Y)
DecTree_Importance = DecTree.feature_importances_


RandForest = RandomForestRegressor()
RandForest.fit(Data_X, Data_Y)
RandForest_Importance = RandForest.feature_importances_


XGBR = XGBRegressor()
XGBR.fit(Data_X, Data_Y)
XGBR_Importance = XGBR.feature_importances_


XGBC = XGBClassifier()
XGBC.fit(Data_X, Data_Y)
XGBC_Importance = XGBC.feature_importances_


KNN = KNeighborsRegressor()
KNN.fit(Data_X, Data_Y)

Permut_Importance = permutation_importance(KNN, Data_X, Data_Y,
                                           scoring= "neg_mean_squared_error")

Permut_Importance = Permut_Importance.importances_mean


# Plotting

plt.style.use("ekc")

fig = plt.figure()

Title = "Feature Importance - 08 - Comparing Models"
fig.suptitle(Title, fontsize= 14)

X_Ticks = np.arange(0, 10)

plt.bar((X_Ticks-.2), DecTree_Importance, width= .5, color= "navy", label= "Decision Tree")
plt.bar((X_Ticks-.1), RandForest_Importance, width= .5, color= "darkred", label= "Random Forest")
plt.bar((X_Ticks+.0), XGBR_Importance, width= .5, color= "orange", label= "XGBoost Reg")
plt.bar((X_Ticks+.1), XGBC_Importance, width= .5, color= "darkgreen", label= "XGBoost Class")

plt.grid(axis= "x")

plt.xticks(X_Ticks)
plt.xlabel("Data X Columns")
plt.ylim(bottom= 0, top= 0.30)

plt.legend(loc= "upper right")
plt.savefig(Title, dpi= 240)
plt.show()


# Closing

print("\n * \n")


import numpy as np
import pandas as pd

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeRegressor

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Program --------------------------------------------------------------

print("\n ****  Feature Importance  **** \n")

Data_X, Data_Y = make_classification(n_samples= 1000, n_features= 10,
                                     n_informative= 5, n_redundant= 5,
                                     random_state= 27)


# Decision Tree Model

DecTree = DecisionTreeRegressor()
DecTree.fit(Data_X, Data_Y)
DecTree_Importance = DecTree.feature_importances_

for i, coef in enumerate(DecTree_Importance):

    print(f" > Feature {i+1}: Score = {coef:.5f}")


print("")


plt.style.use("ekc")

Title = "Feature Importance - 03 - Decision Tree"

fig = plt.figure()
plt.suptitle(Title, fontsize= 14)

plt.bar(range(1, 11), DecTree_Importance, color= "royalblue", edgecolor= "black")

plt.axhline(y= 0, color= "black", linewidth= 0.8)

plt.grid(axis= "x")
plt.xticks(range(1, 11))
plt.xlabel("Data_X Columns")

plt.savefig(Title, dpi= 240)
plt.show()


# Closing

print(" * \n")

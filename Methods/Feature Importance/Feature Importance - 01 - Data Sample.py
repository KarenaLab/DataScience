
import numpy as np
import pandas as pd

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Program --------------------------------------------------------------

print("\n ****  Feature Importance  **** \n")

Data_X, Data_Y = make_classification(n_samples= 1000, n_features= 10,
                                     n_informative= 5, n_redundant= 5,
                                     random_state= 27)

# Data_X EDA

plt.style.use("ekc")

Title = "Feature Importance - 01 - Data Box Plot"

fig = plt.figure()
plt.suptitle(Title, fontsize= 14)

Red_Dict = dict(markerfacecolor= "red")
plt.boxplot(Data_X, widths= 0.75,
            showmeans= True, meanline= True, flierprops= Red_Dict)

plt.grid(axis= "x")
plt.xlabel("Data X Columns")

plt.savefig(Title, dpi= 240)
plt.show()





import numpy as np
import pandas as pd

from sklearn.datasets import make_blobs
from sklearn.covariance import EllipticEnvelope

import matplotlib.pyplot as plt


# Program ---------------------------------------------------------------

print("\n ****  Outlier Detection - Eliptic Envelope  **** \n")

Data_X, trash = make_blobs(n_samples= 200, n_features= 2, centers= 1,
                           cluster_std= 2, random_state= 27)

# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html
# https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html


Outlier_Detector = EllipticEnvelope(contamination= 0.05)
Outlier_Detector.fit(Data_X)

Outliers = Outlier_Detector.predict(Data_X)
Outliers = pd.Series(Outliers)

Color_Map = {  1: "royalblue",
              -1: "darkred" }

Out_Colors = Outliers.map(Color_Map)


# Plotting

plt.style.use("ekc")

fig = plt.figure()

Title = "Outlier Detection - Eliptic Envelope"
fig.suptitle(Title, fontsize= 14)

plt.scatter(Data_X[:, 0], Data_X[:, 1],
            c= Out_Colors, alpha= 0.7, edgecolor= "white")


#plt.savefig(Title, dpi= 240)
plt.show()


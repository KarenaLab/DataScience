
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Program

print("\n ****  K-Means - Optimal Number of Clusters (Elbow Method)  ****\n")


print("Attribute Information:")
print("")
print("1) FRESH: Annual spending (m.u.) on fresh products (Continuous);")
print("2) MILK: Annual spending (m.u.) on milk products (Continuous);")
print("3) GROCERY: Annual spending (m.u.)on grocery products (Continuous);")
print("4) FROZEN: Annual spending (m.u.)on frozen products (Continuous);")
print("5) DETERGENTS_PAPER: Annual spending (m.u.) on detergents and paper")
print("                     products (Continuous);")
print("6) DELICATESSEN: Annual spending (m.u.)on and delicatessen products")
print("                 (Continuous);")
print("7) CHANNEL: Customer Channel - Horeca (Hotel/Restaurant/Café) or")
print("            Retail channel (Nominal);")
print("8) REGION: Customer Region: Lisbon, Porto or Other (Nominal)")
print("")


DF = pd.read_csv("Wholesale_customers_data.csv", sep= ",")

Categorical_Features = ["Channel", "Region"]
Continuous_Features = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]


for col in Categorical_Features:
    
    Dummies = pd.get_dummies(DF[col], prefix= col)
    DF = pd.concat([DF, Dummies], axis= 1)
    DF.drop(col, axis= 1, inplace= True)



MMS = MinMaxScaler()
MMS.fit(DF)
DF_Transformed = MMS.transform(DF)


No_K = []
Sum_of_Squared_Distances = []

 
for k in range(1,15):
    
    KM = KMeans(n_clusters= k)
    KM = KM.fit(DF_Transformed)

    No_K.append(k)
    Sum_of_Squared_Distances.append(KM.inertia_)


# Plotting

plt.style.use("ekc")
fig = plt.figure()

Title = "K-Means Elbow Method - Wholesales Database"
plt.suptitle(Title, fontsize= 14)

plt.plot(No_K, Sum_of_Squared_Distances,
         color= "navy", linestyle= "-", marker= "o")

plt.xlabel("k")
plt.ylabel("Sum of Squared Distances")

#plt.savefig(Title, dpi= 240)
plt.show()


# Sources

# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

# https://archive.ics.uci.edu/ml/index.php
# https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html
# https://blog.cambridgespark.com/how-to-determine-the-optimal-number-of-clusters-for-k-means-clustering-14f27070048f
# https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers


import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.text import OffsetFrom


# Definitions/Config

Seed = 27
np.random.seed(Seed)



# Program

print("\n ****  K-Means Elbow Method - Iris Flowers  **** \n")


# Importing Information

DF = pd.read_csv("iris.csv", sep= ",")


# Setting Target Variable = Species

Target = "species"
DF_x = DF.drop(columns= [Target])
DF_y = DF[Target]


# Calculating the the Elbow Curve (Check Min and Max)

No_K = []
Sum_Dist2 = []

Min_K = 2
Max_K = 20

for k in range(Min_K, (Max_K+1)):

    KM = KMeans(n_clusters= k)
    KM = KM.fit(X= DF_x)

    No_K.append(k)
    Sum_Dist2.append(KM.inertia_)


# Calculating the best k point

x1, x2 = No_K[0], No_K[-1]
y1, y2 = Sum_Dist2[0], Sum_Dist2[-1]

Distance = []
Dist_Max = 0
Best_K = 0

for i in range(0, len(No_K)):

    x = No_K[i]
    y = Sum_Dist2[i]

    # https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line

    #                        |(x2-x1)*(y1-y) - (y2-y1)*(x1-x)|      Num
    #  D(P1, P2, (x, y)) = ------------------------------------- = ----- 
    #                           sqrt((x2-x1)^2 + (y2-y1)^2)         Den


    Numerator = np.absolute(((x2-x1)*(y1-y)) - ((y2-y1)*(x1-x)))
    Denominator = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    Dist = np.round(Numerator/Denominator, decimals= 6)
    
    Distance.append(Dist)

    if(Dist > Dist_Max):

        Dist_Max = Dist
        Best_K = x
        Best_Y = y


# Info

print(f" > Best K = {Best_K} \n")


# Setting Clusters

KM = KMeans(n_clusters= Best_K)
Clusters = KM.fit_predict(DF_x)

DF["clusters"] = Clusters


# Plotting

plt.style.use("ekc")
fig = plt.figure()

Title = f"K-Means Elbow Method [k= {Min_K}-{Max_K}] - Iris Petals"
plt.suptitle(Title, fontsize= 14)

plt.plot(No_K, Sum_Dist2, color= "navy", linestyle= "-", marker= "o", markersize= 4, zorder= 11)
plt.scatter(Best_K, Best_Y, color= "darkred", marker= "o", zorder= 12)
plt.axvline(x= Best_K, color= "black", linestyle= "--", linewidth= 0.5, zorder= 10)

plt.xlabel("k")
plt.xticks(No_K)
plt.ylabel("Sum of Squared Distance", loc= "center")

plt.savefig(Title, dpi= 240)
plt.show()


# Sources:

# https://jtemporal.com/kmeans-and-elbow-method/
# https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
#
#


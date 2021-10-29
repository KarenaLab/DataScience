# Curve Fitting

import numpy as np
import pandas as pd

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt


# Program ---------------------------------------------------------------

print("\n ****  Curve Fitting  ****\n")


DF = pd.read_csv("winequality_red.csv", sep= ",")

Data = DF["fixed_acidity"]


Size = Data.shape[0]
Mean = Data.mean()
Median = Data.median()
StdDev = Data.std()


No_Bins = int(np.sqrt(Size) + 0.5)
y_data, Bin_Edges = np.histogram(Data, bins= No_Bins)


x_data = []

i = 0
while(i < (No_Bins)):

    get = (Bin_Edges[i]+Bin_Edges[i+1])/2
    x_data.append(get)

    i = i+1

x_data = np.array(x_data)


def GaussCurve(x, Mean, StdDev):

    Gauss = (1/(StdDev*np.sqrt(2*np.pi))*np.exp((-0.5)*((x-Mean)/StdDev)**2))
    return Gauss


Gauss_Fit = GaussCurve(x_data, Mean, StdDev)
Gauss_Corr = np.corrcoef(y_data, Gauss_Fit)[0,1]




# Plotting

fig = plt.figure(figsize= (8, 4.5))

Title = "Curve Fitting - Gauss Curve"
plt.suptitle(Title, fontsize= 14)

plt.hist(x= Data, bins= No_Bins, color= "navy", edgecolor= "white",
         density= True, label= "Data", zorder= 10)

plt.axvline(x= Median, color= "orange", zorder= 11)
plt.axvline(x= Mean, color= "green", zorder= 12)

plt.plot(x_data, Gauss_Fit, color= "darkred", linestyle= "--",
         label= "Gauss Curve", zorder= 13)


plt.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
plt.legend(loc= "best", framealpha= 1)


# Closing

plt.savefig(Title, dpi= 240)
plt.show()

print(" * \n")

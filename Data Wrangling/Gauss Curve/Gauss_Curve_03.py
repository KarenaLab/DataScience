
import numpy as np
import pandas as pd

from scipy import stats
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Definitions & Variables

def GaussCurve(x, A, x0, sigma):

    Gauss = A * np.exp(-(x-x0)**2/(2*sigma**2))
    return Gauss


Seed = 27


# Program

print("\n ****  Gauss Curve - Example 03  **** \n")

np.random.seed(Seed)

x_data = np.linspace(0, 10, num= 100)
y_data = GaussCurve(x_data, 1, 5, 2)

y_noise = y_data + 0.2 * np.random.normal(size= len(x_data))

Func_Opt, covariance = curve_fit(GaussCurve, x_data, y_noise)

A_Opt = Func_Opt[0]
x0_Opt = Func_Opt[1]
sigma_Opt = Func_Opt[2]

y_best = GaussCurve(x_data, A_Opt, x0_Opt, sigma_Opt)


# Plotting

fig = plt.figure(figsize= (8, 4.5))

Title = "Gauss Curve - Fitting Data - Example 03"

plt.suptitle(Title, fontsize= 14)

plt.scatter(x_data, y_noise, color= "lightblue", label= "Data", zorder= 10)
plt.plot(x_data, y_data, color= "royalblue", label= "Gauss Curve", zorder= 11)
plt.plot(x_data, y_best, color= "darkred", label= "Best Fit", zorder= 12)

plt.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)

plt.legend(loc= "best", fontsize= 9, framealpha= 1)


# Closing

#plt.savefig(Title, dpi= 240)
plt.show()

print(" * \n")

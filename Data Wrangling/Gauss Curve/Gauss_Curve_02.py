
import numpy as np
import pandas as pd

from scipy import stats
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Definitions

def GaussCurve(x, A, B):

    y = A * np.exp((-1) * B * x**2)
    return y


# Program

print("\n ****  Gauss Curve - Example 02  **** \n")

x_data = np.arange(-10, 11, step= 1)

y_data = [1.2, 4.2, 6.7, 8.3, 10.6, 11.7, 13.5,
          14.5, 15.7, 16.1, 16.6, 16.0, 15.4, 14.4,
          14.2, 12.7, 10.3, 8.6, 6.1, 3.9, 2.1]


x_data = np.array(x_data)
y_data = np.array(y_data)

parameters, covariance = curve_fit(GaussCurve, x_data, y_data)

Fit_A = parameters[0]
Fit_B = parameters[1]

Fit_y = GaussCurve(x_data, Fit_A, Fit_B)


# Ploting

fig = plt.figure(figsize= (8, 4.5))

Title = "Gauss Curve - Fitting Data - Example 02"

plt.suptitle(Title, fontsize= 14)

plt.scatter(x_data, y_data, marker="o", color= "red", label= "Data", zorder= 9)
plt.plot(x_data, Fit_y, color= "navy", label= "Fit", zorder= 8)
plt.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)

plt.legend(loc= "best", framealpha= 1)


# Closing

#plt.savefig(Title, dpi= 240)
plt.show()

print(" * \n")

  





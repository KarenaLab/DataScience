
import numpy as np
import pandas as pd

from scipy import stats

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Program

print("\n ****  Gauss Curve - Example 01  **** \n")

# Data

Mean = 0
StdDev = 1

x_data = np.arange(-5, 5, step= 0.001)
y_data = stats.norm.pdf(x_data, loc= Mean, scale= StdDev)


# Plotting

fig= plt.figure(figsize= (8, 4.5))

Title = f"Gauss Curve [Mean= {Mean}, StdDev= {StdDev}]"

plt.suptitle(Title, fontsize= 14)

plt.plot(x_data, y_data, color= "navy", zorder= 9)
plt.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)

plt.ylabel("density")

plt.axvline(x= Mean, color= "grey", linewidth= 1)
plt.axhline(y= 0, color= "grey", linewidth= 1)


# Closing

#plt.savefig(Title, dpi= 240)
plt.show()

print(" * \n")


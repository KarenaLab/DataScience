
import numpy as np

import matplotlib.pyplot as plt

from binning_v02 import *

sqrt_list, rice_list, sturges_list = [], [], []
size = [10, 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]

for i in size:
    bins_sqrt = binning(i, method="sqrt")
    bins_rice = binning(i, method="rice")
    bins_sturges = binning(i, method="sturges")

    sqrt_list.append(bins_sqrt)
    rice_list.append(bins_rice)
    sturges_list.append(bins_sturges)

colors = ["navy", "darkred", "orange"]
names = ["Square root", "Rice rule", "Sturges"]
methods = [sqrt_list, rice_list, sturges_list]


# Plot
fig = plt.figure(figsize=[8, 4.5])
fig.suptitle("Binning methods comparison", fontsize=10, fontweight="bold")

for data, label, color in list(zip(methods, names, colors)):
    plt.plot(size, data, color=color, label=label, zorder=20)

plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)
plt.ylabel("Number of bins calculated", fontsize=10, loc="top")
plt.xlabel("Number of items", fontsize=10, loc="right")

plt.legend(loc="upper left", fontsize=8, framealpha=1)

plt.tight_layout()
plt.show()


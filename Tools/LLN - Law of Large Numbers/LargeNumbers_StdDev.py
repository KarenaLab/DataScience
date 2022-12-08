# *** Law of Large Numbers  ***
#
#  Project: LLN - Law of Large Number
# Filename: LargeNumbers_StdDev_v01
#  Version: 01
#
# ---------------------------------------------------------------------

# Versions ------------------------------------------------------------

# 01 - 19th Jan 2021 - Starter
# 02 - 05th Dec 2022 - Adjusting plots


# Libraries -----------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Setup ---------------------------------------------------------------
seed = 3

# MAIN Program ---------------------------------------------------------
print("\n *** LLN - Law of Large Numbers (Standard Deviation) *** \n")

# 1 - Calculating cumulative mean --------------------------------------
step_multi = [100, 500, 1000, 5000, 10000, 50000, 100000]

for i in step_multi:
    np.random.seed(seed)
    
    axis_x = np.linspace(start=1, stop=i, num=i)
    dice = np.random.randint(low=1, high=6+1, size=i)

    step = int(i/100)
    axis_x, move_mean, move_lower, move_upper = [], [], [], []    
    for j in range(1, i+step, step):
        mean = np.mean(dice[0:j])
        axis_x.append(j)
        move_mean.append(mean)

        stddev = np.std(move_mean)
        move_lower.append(mean - 3*stddev)
        move_upper.append(mean + 3*stddev)


    # 2 - Plotting ----------------------------------------------------
    title = f"Deviation of Law of Large Numbers [{i}]"
    
    fig = plt.figure(figsize=[8,4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    plt.plot(axis_x, move_mean, color="royalblue", linestyle="-", linewidth=1, zorder=30)
    plt.plot(axis_x, move_lower, color="lightsteelblue", linestyle="-", linewidth=0.5, zorder=20)
    plt.plot(axis_x, move_upper, color="lightsteelblue", linestyle="-", linewidth=0.5, zorder=21)    
    plt.fill_between(x= axis_x, y1=move_lower, y2=move_upper, color="lightsteelblue", alpha=0.5, zorder=22)

    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)
    plt.axhline(y=3.5, color="darkred", linestyle="-", linewidth=0.5, zorder=11)
    
    plt.tight_layout()
    plt.savefig(title, dpi=240)
    plt.show()

    
# Sources ---------------------------------------------------------------

# Random Functions = https://numpy.org/doc/1.16/reference/routines.random.html
# randint = https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint

# LLN Wikipedia (Law of Large Numbers) = https://en.wikipedia.org/wiki/Law_of_large_numbers
# LLN Wolfram (Law of Large Numbers) = https://mathworld.wolfram.com/WeakLawofLargeNumbers.html

# *** Law of Large Numbers  ***
#
#  Project: LLN - Law of Large Number
# Filename: LargeNumbers_v01
#     Date: 17th Jan 2021
#  Version: 01
#
# -----------------------------------------------------------------------

# Versions --------------------------------------------------------------

# 01 - 17th Jan 2021 - Starter
# 02 - 17th Jan 2021 - Lists with various Samples
# 03 - 04rd Dec 2022 - Adjusting plots
# 04 - 


# Libraries -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


# Setup -----------------------------------------------------------------
seed = 27


# MAIN Program ---------------------------------------------------------

# 0 - Header -----------------------------------------------------------
print("\n *** LLN - Law of Large Numbers *** \n")


# 1 - Calculating cumulative mean --------------------------------------
step_base = [1, 10, 25, 50, 100]
step_multi = [1, 5, 10, 50, 100]

for i in step_multi:
    np.random.seed(seed)
    step_list = [i * value for value in step_base]
    axis_x = np.linspace(start=1, stop=max(step_list), num=max(step_list))
    dice = np.random.randint(low=1, high=6+1, size=max(step_list))
    summation = np.cumsum(dice)
    mean = np.round(summation / axis_x, decimals=6)

    for j in step_list:
        error = np.round((np.abs(mean[j-1]-3.5)/3.5)*100, decimals=3)
        print(f"mean({j})= {mean[j-1]} >>> error: {error}%")

    print("")   


    # 2 - Plotting ------------------------------------------------------
    title = f"Testing Law of Large Numbers with one dice [{max(step_list)}]"

    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    plt.plot(axis_x, mean, color="blue", label="mean", zorder=20)

    plt.xlabel("# of samples", loc="right", fontsize=8)
    plt.ylabel("Dice mean", loc="center", fontsize=8)

    plt.ylim(bottom=0.5, top=6.5)

    plt.grid(color="lightgrey", linestyle="--", linewidth= 0.5, zorder=10)
    plt.axhline(y=3.5, color="red", linewidth=1, label="LLN Mean", zorder=11)

    # Plot Annotations
    offset = int(max(step_list)/100)
    for i in step_list:
        plt.axvline(x=i, color="black", linewidth=0.75)
        plt.text(x=(i+offset), y=1.2, s=str(i), rotation=90, alpha=1)
        plt.text(x=(i+offset), y=4.5, s=f"mean = {mean[i-1]}", rotation=90, alpha=1)

    
    plt.tight_layout()
    plt.savefig(title, dpi=240)
    plt.show()


# Sources ---------------------------------------------------------------

# Random Functions = https://numpy.org/doc/1.16/reference/routines.random.html
# randint = https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint

# LLN Wikipedia (Law of Large Numbers) = https://en.wikipedia.org/wiki/Law_of_large_numbers
# LLN Wolfram (Law of Large Numbers) = https://mathworld.wolfram.com/WeakLawofLargeNumbers.html


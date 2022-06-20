# Bland Altman Analysis

def bland_altman(y_true, y_pred, title, decimals=6, plot="both", **kwargs):
    """
    Performs Bland-Altman analysis to evaluate a bias between the mean
    differences, and to estimate an agreement interval, within which
    95% of the differences.

    """

    # Libraries
    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    

    # Versions ---------------------------------------------------------
    # 01 - May 23rd, 2022 - Starter
    # 02 -


    # Insights
    # Ideas to improve in the future


    # Program ----------------------------------------------------------

    BA = pd.DataFrame(data=[], columns=["y_true", "y_pred", "mean", "diff", "diff_pct"])

    BA["y_true"], BA["y_pred"] = y_true, y_pred

    BA["mean"] = (BA["y_true"] + BA["y_pred"]) / 2
    BA["diff"] = (BA["y_true"] - BA["y_pred"])
    BA["diff_pct"] = np.round((BA["diff"] / BA["mean"])*100, decimals=2)

    BA_mean = np.round(BA["diff"].mean(), decimals=decimals)
    BA_stddev = np.round(BA["diff"].std(), decimals=decimals)

    BA_upper = np.round(BA_mean + 1.96*BA_stddev, decimals=decimals)
    BA_lower = np.round(BA_mean - 1.96*BA_stddev, decimals=decimals)
    

    # Ploting
    fig = plt.figure(figsize=[8, 4.5])

    fig.suptitle(title, fontsize=10)

    plt.scatter(x=BA["mean"], y=BA["diff"], zorder=20)

    plt.ylabel("y_true - y_pred", fontsize=9, loc="center")
    plt.xlabel("mean of y_true and y_pred", fontsize=9, loc="center")

    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.8)
    plt.axhline(y=0, color="black", linestyle="-", linewidth=0.8)
    plt.axhline(y=BA_mean, color="darkgreen", linestyle="--", linewidth=0.8)
    plt.axhline(y=BA_upper, color="darkred", linestyle="-", linewidth=0.8)
    plt.axhline(y=BA_lower, color="darkred", linestyle="-", linewidth=0.8)

    plt.show()
      

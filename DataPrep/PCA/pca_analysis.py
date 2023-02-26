
def pca_analysis(DataFrame, title=None, decimals=4, color="darkblue",
                 plot=True, savefig=False, verbose=True):
    """
    Applies the PCA (Principal Component Analysis) into the **DataFrame**
    and returns the [0] Dataframe with PCA and [1] the explained variance
    ratio accumulated.

    Variables:
    * DataFrame = Dataframe to be analised,
    * title = Title for the plot and (if savefig=True), the name for the file,
    * decimals = Number of decimals to be plot (default=4)
    * color = Line color for the plot (default="darkblue")
    * plot = True* or False, plots the accumulated PCA explanation
    * savefig = True or False*, to save the plot as a figure
    * verbose = True* or False, to print important information

    """
    # Libraries
    import numpy as np
    import pandas as pd

    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec

    # Data preparation
    if(title == None):
        title = "PCA Analysis"


    # PCA
    n_comp = DataFrame.shape[1]  
    pca = PCA(n_components=n_comp)
    pca = pca.fit(DataFrame)

    # DataFrame with PCA
    pca_array = pca.fit_transform(DataFrame)
    pca_col = [("pca_" + str(i)) for i in range(1, n_comp+1)]
    df_pca = pd.DataFrame(data=pca_array, columns=pca_col)
    
    pct_variance = pca.explained_variance_ratio_
    pct_variance = np.cumsum(pct_variance)
    pct_var_plot = np.round(pct_variance * 100, decimals=decimals)


    # Plotting
    if(plot == True):
        fig = plt.figure(figsize=[8, 4.5])
        fig.suptitle(title, fontsize=10, fontweight="bold")

        plt.plot(range(1, len(pct_var_plot)+1), pct_var_plot, color=color, linewidth=1.5, zorder=20)
        plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)
        plt.ylabel("% Accumulated", loc="top")
        plt.xlabel("PCA Components", loc="right")

        plt.tight_layout()
        if(savefig == True):
            plt.savefig(title, dpi=240)
            if(verbose == True):
                print(f" > saving file {title}.png")

        else:
            plt.show()

        plt.close(fig)
    

    return df_pca, pct_variance


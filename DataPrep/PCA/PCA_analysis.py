
def pca_analysis(DataFrame, title, **kwargs):
    """
    Applies the PCA (Principal Component Analysis) into the **DataFrame**
    and returns the [0] Dataframe with PCA and [1] the explained variance
    ratio accumulated.

    """
    # Libraries
    import numpy as np
    import pandas as pd

    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


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
    pct_var_plot = np.round(pct_variance*100, decimals=4)


    # Plotting
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    plt.plot(range(1, len(pct_var_plot)+1), pct_var_plot, color="darkblue", linewidth=1.5, zorder=20)
    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)
    plt.ylabel("% Accumulated", loc="top")
    plt.xlabel("PCA Components", loc="right")
    
    plt.show()


    # Return information

    return df_pca, pct_variance

    

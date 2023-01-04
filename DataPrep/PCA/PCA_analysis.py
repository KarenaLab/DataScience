
def PCA_analysis(data, title, **kwargs):

    import numpy as np
    import pandas as pd

    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    
    
    
    scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)

    pca = PCA(n_components=data.shape[1])
    pca = pca.fit(data)
    pct_variance = pca.explained_variance_ratio_
    pct_variance = np.cumsum(pct_variance)
    pct_variance = np.round(pct_variance*100, decimals=3)
    
    
    # Plotting
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=11)

    plt.plot(range(1, len(pct_variance)+1), pct_variance, color="darkblue", linewidth=1.5, zorder=20)
    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)
    plt.ylabel("% Accumulated", loc="top")
    plt.xlabel("PCA Components", loc="right")
    
    plt.show()

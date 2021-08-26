# MAD (Median Absolute Deviation) Method for Outliers

def MADOutliers(DF, Variable, **kwargs):

    # (Libraries - delete this tag)

    import numpy as np
    import pandas as pd
    
    from scipy import stats 


    # Versions ---------------------------------------------------------

    # 01 - Aug 26th, 2021 - Starter
    # 02 -


    # List of Variables and kwargs -------------------------------------

    # Data = Dataframe (Pandas)
    # Variable = Column to be analyzed

    # threshold = 3* = Trigger to separate the Outliers
    #

    # References
    # MAD:
    # https://en.wikipedia.org/wiki/Median_absolute_deviation

    # Scipy MAD:
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_abs_deviation.html#scipy.stats.median_abs_deviation

   
    # Program ----------------------------------------------------------

    trigger = kwargs.get("threshold")

    if trigger:
        threshold = trigger

    else:
        threshold = 3


    Data = DF[Variable]

    Median = np.median(Data)
    MAD = stats.median_abs_deviation(Data)

    Outliers = []

    for index, x in enumerate(Data):

        t = (x-Median)/MAD
        t = np.absolute(t)

        if(t > threshold):
            Outliers.append(index)


    return Outliers



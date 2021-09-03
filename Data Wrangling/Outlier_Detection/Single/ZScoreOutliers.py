# Z Score Method for Outliers (Considering Gauss Distribution)

def ZScoreOutliers(DF, Variable, **kwargs):

    # (Libraries - delete this tag)

    import numpy as np
    import pandas as pd
    

    # Versions ---------------------------------------------------------

    # 01 - Aug 26th, 2021 - Starter
    # 02 -


    # List of Variables and kwargs -------------------------------------

    # Data = Dataframe (Pandas)
    # Variable = Column to be analyzed

    # threshold = 3* = Trigger to separate the Outliers
    #
    

    # Program ----------------------------------------------------------

    trigger = kwargs.get("threshold")

    if trigger:
        threshold = trigger
        
    else:
        threshold = 3

    
    Data = DF[Variable]

    Mean = np.mean(Data)
    StdDev = np.std(Data)

    Outliers = []

    for index, x in enumerate(Data):

        z = (x-Mean)/StdDev
        z = np.absolute(z)

        if(z > threshold):
            Outliers.append(index)


    return(Outliers)



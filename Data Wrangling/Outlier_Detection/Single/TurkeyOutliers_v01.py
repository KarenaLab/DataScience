# Turkey Method for Outliers (using metrics of BoxPlot)

def TurkeyOutliers(Data, Variable, **kwargs):

    import numpy as np
    import pandas as pd


    # Versions ---------------------------------------------------------

    # 01 - Aug 26th, 2021 - Starter
    # 02 -


    # List of Variables and kwargs -------------------------------------

    # Data = Dataframe (Pandas)
    # Variable = Column to be analyzed
    
    # probable = True* or False
    # possible = False* or True
    #

    # Text and Image References
    # https://www.researchgate.net/figure/Empirical-box-plot-together-with-the-empirical-inner-and-outer-fences_fig1_318223455


    # Program ----------------------------------------------------------

    # kwargs adjust

    Prob_get = kwargs.get("probable")

    if(Prob_get != False):
        Prob = True

    else:
        Prob = False
        

    Poss_get = kwargs.get("possible")

    if(Poss_get == True):
        Poss = True

    else:
        Poss = False


    # Calculating Limits of BoxPlot and Fences
    
    q1 = Data[Variable].quantile(0.25)
    q3 = Data[Variable].quantile(0.75)

    iqr = q3 - q1

    Inner_Distance = 1.5 * iqr
    Outer_Distance = 3.0 * iqr

    Outer_Left = q1 - Outer_Distance 
    Inner_Left = q1 - Inner_Distance

    Outer_Right = q3 + Outer_Distance
    Inner_Right = q3 + Inner_Distance


    # Separating Information

    Probable_Outliers = []

    if(Prob == True):

        for index, x in enumerate(Data[Variable]):

            if(x <= Outer_Left or x >= Outer_Right):
                Probable_Outliers.append(index)


    Possible_Outliers = []

    if(Poss == True):

        for index, x in enumerate(Data[Variable]):

            if(x <= Inner_Left or x >= Inner_Right):
                Possible_Outliers.append(index)


    # Return Info
    
    if(Prob == True and Poss == False):
        return Probable_Outliers

    if(Prob == False and Poss == True):
        return Possible_Outliers

    if(Prob == True and Poss == True):
        return Probable_Outliers, Possible_Outliers


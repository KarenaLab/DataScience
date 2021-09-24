
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype

from sklearn.impute import KNNImputer

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



# Definitions -----------------------------------------------------------

def Rounder(x):

    x = np.round(x, decimals= 0)
    return x


def Variation(Ref, New):

    if(Ref != 0):
        D_Pct = np.round(((New - Ref)/Ref)*100, decimals= 2)
        return D_Pct

    else:
        return 0



# Program ---------------------------------------------------------------

print("\n ****  KNN Imputation Testing Neighbor - HMEQ  **** \n")


# Getting Information from .csv

Filename = "hmeq.csv"

DF = pd.read_csv(Filename, sep= ",")
DF_SafeCopy = DF.copy()

DF_Rows = DF.shape[0]
DF_Cols = DF.shape[1]
DF_Columns = DF.columns


# NaNs Report

Total = 0

for col in DF_Columns:

    Data = DF[col]
    NaN_Count = Data.isnull().sum()
    Total = Total + NaN_Count

    print(f" > {col}: NaNs = {NaN_Count} ({(NaN_Count/DF_Rows)*100:.1f}%)")


print(f"\n >>> Total of NaNs = {Total}\n")


# Preparation for KNN: Changing Text columns into Numbers/Cetegoric

for col in DF_Columns:

    if(is_string_dtype(DF[col]) == True):

        Data = DF[col]
        
        Info_Unique = Data.unique()
        Info_Unique = Info_Unique[~pd.isnull(Info_Unique)]

        Unique_List = np.arange(0, Data.nunique())
        Unique_List = dict(zip(Info_Unique, Unique_List))
        Data = Data.map(Unique_List)

        DF[col] = Data
                  

# KNN Imputation

Target = "BAD"

Data_X = DF.drop(columns= [Target])
Data_Y = DF[Target]

Data_X_Columns = Data_X.columns

# Removing Categoric Columns for n-Neighbours Study
Data_X_Analysis = [ "MORTDUE", "VALUE", "YOJ", "DEROG", "DELINQ",
                    "CLAGE", "NINQ", "CLNO", "DEBTINC" ]


for col in Data_X_Analysis:
    
    No_Neighbors = []
    Measure_Mean = []
    Measure_Median = []
    Measure_StdDev = []

    Data = Data_X[col]

    Ref_Neighbors = 0
    Ref_Mean = Data.mean()
    Ref_Median = Data.median()
    Ref_StdDev = Data.std()


    for n in range(1, 9):

        print(f" > Calculating {col} with {n} KNN Neighbors")

        imputer = KNNImputer(n_neighbors= n,
                             weights= "uniform", metric= "nan_euclidean")

        DF_Transform = imputer.fit_transform(Data_X, Data_Y)
        DF_Transform = pd.DataFrame(data= DF_Transform, columns= Data_X_Columns)

        Data = DF_Transform[col]

        New_Mean = Data.mean()
        New_Median = Data.median()
        New_StdDev = Data.std()

        No_Neighbors.append(n)
        Measure_Mean.append((Variation(Ref_Mean, New_Mean)))
        Measure_Median.append(Variation(Ref_Median, New_Median))
        Measure_StdDev.append(Variation(Ref_StdDev, New_StdDev))       


    # Plotting

    plt.style.use("ekc")

    fig, ax = plt.subplots()
    
    Title = f"KNN Imputation Test_Ref - {col}"
    fig.suptitle(Title, fontsize= 14)

    x_ref = np.arange(0, len(No_Neighbors))

    bar_total = 0.9
    no_bars = 3
    bar_width = bar_total/no_bars

    ax.bar(x_ref-bar_width, Measure_Mean, width= bar_width,
           color= "navy", label= "Mean")

    ax.bar(x_ref, Measure_Median, width=bar_width,
           color= "darkred", label= "Median")

    ax.bar(x_ref+bar_width, Measure_StdDev, width= bar_width,
           color= "orange", label= "StdDev")


    ax.set_xlabel("No Neighbors")
    ax.set_xticks(x_ref)
    ax.set_xticklabels(No_Neighbors)
    ax.axhline(y= 0, color= "black", linewidth= 0.8)

    ax.set_ylabel("% to the Reference", loc= "center")
    ax.xaxis.grid(False)

    plt.legend()

    plt.savefig(Title, dpi= 240)
    plt.show()
    print("")


    
   
# Sources ---------------------------------------------------------------

# https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html



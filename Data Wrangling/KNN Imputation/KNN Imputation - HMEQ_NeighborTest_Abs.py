
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

Data_X_Analysis = [ "MORTDUE", "VALUE", "YOJ", "DEROG", "DELINQ",
                    "CLAGE", "NINQ", "CLNO", "DEBTINC" ]


for col in Data_X_Analysis:
    
    No_Neighbors = []
    Measure_Mean = []
    Measure_Median = []
    Measure_StdDev = []

    Data = Data_X[col]


    No_Neighbors.append(0)
    Measure_Mean.append(Data.mean())
    Measure_Median.append(Data.median())
    Measure_StdDev.append(Data.std())


    for n in range(1, 9):

        print(f" > Calculating {col} with {n} KNN Neighbors")

        imputer = KNNImputer(n_neighbors= n,
                             weights= "uniform", metric= "nan_euclidean")

        DF_Transform = imputer.fit_transform(Data_X, Data_Y)
        DF_Transform = pd.DataFrame(data= DF_Transform, columns= Data_X_Columns)


        # "Come Back": Tranforming KNN predictions Values of Text Columns

        DF = DF_SafeCopy.copy()

        if(is_numeric_dtype(DF[col]) == True):

            Data = DF_Transform[col]

            No_Neighbors.append(n)
            Measure_Mean.append(Data.mean())
            Measure_Median.append(Data.median())
            Measure_StdDev.append(Data.std())


    # Plotting

    plt.style.use("ekc")

    fig = plt.figure()

    Title = f"KNN Imputation Test Abs - {col}"
    fig.suptitle(Title, fontsize= 14)

    plt.plot(No_Neighbors, Measure_Mean, color= "navy", label= "Mean", zorder= 10)
    plt.plot(No_Neighbors, Measure_Median, color= "darkred", label= "Median", zorder= 11)
    plt.plot(No_Neighbors, Measure_StdDev, color= "orange", label= "StdDev", zorder= 12)

    plt.axvline(x= 5, color= "black", linestyle= "--", linewidth= 0.5)

    plt.xlabel("No Neighbors")
    plt.legend(loc= "center left")

    plt.savefig(Title)    
    plt.show()

    print("")
    
   
# Sources ---------------------------------------------------------------

# https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html



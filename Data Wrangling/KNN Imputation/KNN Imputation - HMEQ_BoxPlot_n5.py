
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

print("\n ****  KNN Imputation - HMEQ  **** \n")


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


print(f" >>> Total of NaNs = {Total}\n")


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

imputer = KNNImputer(n_neighbors= 5,
                     weights= "uniform", metric= "nan_euclidean")

DF_Transform = imputer.fit_transform(Data_X, Data_Y)
DF_Transform = pd.DataFrame(data= DF_Transform, columns= Data_X_Columns)


# "Come Back": Tranforming KNN predictions Values of Text Columns

DF = DF_SafeCopy.copy()

for col in Data_X_Columns:

    if(is_numeric_dtype(DF[col]) == True):

        DF[col] = DF_Transform[col]


    if(is_string_dtype(DF[col]) == True):

        Data_In = DF_Transform[col]
        Data_In = Data_In.apply(Rounder)
        
        Data_Out = DF[col]

        Info_Unique = Data_Out.unique()
        Info_Unique = Info_Unique[~pd.isnull(Info_Unique)]

        Unique_List = np.arange(0, Data.nunique())
        Unique_List = dict(zip(Unique_List, Info_Unique))

        Data_In = Data_In.map(Unique_List)

        DF[col] = Data_In



# Checking Information: NaN Report after KNN Imputation

Total = 0

for col in DF_Columns:

    Data = DF[col]
    NaN_Count = Data.isnull().sum()
    Total = Total + NaN_Count

    print(f" > {col}: NaNs = {NaN_Count} ({(NaN_Count/DF_Rows)*100:.1f}%)")


print(f" >>> Total of NaNs = {Total}\n")


# Plotting

for col in DF_Columns:

    if(is_numeric_dtype(DF[col]) == True):

        Data_Before = DF_SafeCopy[col]
        Data_Before = Data_Before.dropna()

        Data_Before_Count = Data_Before.shape[0]
        Data_Before_Mean = Data_Before.mean()
        Data_Before_Median = Data_Before.median()
        Data_Before_StdDev = Data_Before.std()


        Data_After = DF[col]

        Data_After_Count = Data_After.shape[0]
        Data_After_Mean = Data_After.mean()
        Data_After_Median = Data_After.median()
        Data_After_StdDev = Data_After.std()

        NaN_Count = Data_After_Count - Data_Before_Count
        Dif_Mean = ((Data_After_Mean - Data_Before_Mean) / Data_Before_Mean) * 100
        Dif_Median = ((Data_After_Median - Data_Before_Median) / Data_Before_Median) * 100
        Dif_StdDev = ((Data_After_StdDev - Data_Before_StdDev) / Data_Before_StdDev) * 100
        
    
        fig = plt.figure(figsize= (8, 4.5))
        grd = gridspec.GridSpec(nrows=2, ncols= 2, height_ratios= [7, 3])

        ax0 = plt.subplot(grd[0, 0])        # BoxPlot - Before
        ax1 = plt.subplot(grd[0, 1])        # BoxPlot - AFTER
        ax2 = plt.subplot(grd[1, 0])        # Report - Before
        ax3 = plt.subplot(grd[1, 1])        # Report - AFTER        


        Title = f"KNN Imputation Comparison HMEQ - {col}"
        fig.suptitle(Title, fontsize= 14)

        
        # Box Plot (Before)

        ax0.boxplot(x= Data_Before, widths= 0.5, showmeans= True, meanline= True)
        ax0.yaxis.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
        ax0.set_axisbelow(True)

        ax0.set_title("Info without Imputation")


        # Box Plot (AFTER)        

        ax1.boxplot(x= Data_After, widths= 0.5, showmeans= True, meanline= True)
        ax1.yaxis.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
        ax1.set_axisbelow(True)

        ax1.set_title("After KNN Imputation [n= 5]")


        # Information (Before)

        ax2.axis(False)
        
        Count_Text = f"Number of Items= {Data_Before_Count}"
        Mean_Text = f"Mean= {Data_Before_Mean:.6f}"
        Median_Text = f"Median= {Data_Before_Median:.6f}"
        StdDev_Text = f"StdDev= {Data_Before_StdDev:.6f}"
        
        ax2.text(x= 0.05, y= 1.00, s= Count_Text)
        ax2.text(x= 0.05, y= 0.80, s= Mean_Text)
        ax2.text(x= 0.05, y= 0.60, s= Median_Text)
        ax2.text(x= 0.05, y= 0.40, s= StdDev_Text)


        # Information (AFTER)       

        ax3.axis(False)

        Count_Text = f"Number of Items= {Data_After_Count}, NaN= {NaN_Count}"
        Mean_Text = f"Mean= {Data_After_Mean:.6f}, Dif= {Dif_Mean:.2f}%"
        Median_Text = f"Median= {Data_After_Median:.6f}, Dif= {Dif_Median:.2f}%"
        StdDev_Text = f"StdDev= {Data_After_StdDev:.6f}, Dif= {Dif_StdDev:.2f}%"
        
        ax3.text(x= 0.05, y= 1.00, s= Count_Text)
        ax3.text(x= 0.05, y= 0.80, s= Mean_Text)
        ax3.text(x= 0.05, y= 0.60, s= Median_Text)
        ax3.text(x= 0.05, y= 0.40, s= StdDev_Text)
        

        plt.tight_layout()
        plt.savefig(Title, dpi= 240)
        plt.show()



# Closing

print(" * \n")





# Sources ---------------------------------------------------------------

# https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html



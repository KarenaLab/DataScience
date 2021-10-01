
import numpy as np
import pandas as pd

from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Program ---------------------------------------------------------------

print("\n ****  PCA Analysis - Iris Dataset  **** \n")

Filename = "iris.csv"
DF = pd.read_csv(Filename, sep= ",")

DF_Rows = DF.shape[0]
DF_Cols = DF.shape[1]
DF_Columns = DF.columns


Target = "species"

Data_X = DF.drop(columns = [Target])
Data_Y = DF[Target]
Target_List = Data_Y.unique()
Target_Size = Data_Y.nunique()


# PCA Analysis

Components = 3
Comp_List = []

i = 1
while(i <= Components):

    Var_Name = "PC" + str(i)
    Comp_List.append(Var_Name)

    i = i+1
    

PCA = PCA(n_components= Components)

PCA.fit(Data_X)
PCA_X = PCA.transform(Data_X)

New_DF = pd.DataFrame(PCA_X, columns= Comp_List)
New_DF[Target] = Data_Y


# Plotting

plt.style.use("ekc")

Alpha = 0.7
Color_List = ["navy", "darkred", "orange", "drakgreen"]


fig = plt.figure()
grd = fig.add_gridspec(nrows= 3, ncols= 3)

ax0 = fig.add_subplot(grd[0, 0])
ax1 = fig.add_subplot(grd[0, 1])
ax2 = fig.add_subplot(grd[0, 2])

ax3 = fig.add_subplot(grd[1, 0])
ax4 = fig.add_subplot(grd[1, 1])
ax5 = fig.add_subplot(grd[1, 2])

ax6 = fig.add_subplot(grd[2, 0])
ax7 = fig.add_subplot(grd[2, 1])
ax8 = fig.add_subplot(grd[2, 2])


Title = f"PCA Analysis - Iris Petals [Components= {Components}]"
fig.suptitle(Title, fontsize= 14)


i = 0
No_Bins = int(np.sqrt(DF_Rows) + 0.5)

while(i < Target_Size):

    Group = Target_List[i]
    Color = Color_List[i]

    Data_PC1 = New_DF.groupby(Target).get_group(Group)["PC1"]
    Data_PC2 = New_DF.groupby(Target).get_group(Group)["PC2"]
    Data_PC3 = New_DF.groupby(Target).get_group(Group)["PC3"]

    ax0.hist(Data_PC1, bins= No_Bins, color= Color, alpha= Alpha, label= Group)
    ax4.hist(Data_PC2, bins= No_Bins, color= Color, alpha= Alpha, label= Group)
    ax8.hist(Data_PC3, bins= No_Bins, color= Color, alpha= Alpha, label= Group)

    ax1.scatter(Data_PC2, Data_PC1, color= Color, alpha= Alpha, edgecolor= "white", label= Group)
    ax2.scatter(Data_PC3, Data_PC1, color= Color, alpha= Alpha, edgecolor= "white", label= Group)
    ax3.scatter(Data_PC1, Data_PC2, color= Color, alpha= Alpha, edgecolor= "white", label= Group)
    ax5.scatter(Data_PC3, Data_PC2, color= Color, alpha= Alpha, edgecolor= "white", label= Group)
    ax6.scatter(Data_PC1, Data_PC3, color= Color, alpha= Alpha, edgecolor= "white", label= Group)
    ax7.scatter(Data_PC2, Data_PC3, color= Color, alpha= Alpha, edgecolor= "white", label= Group)

    i = i+1


ax0.set_ylabel("PC1", fontweight= "bold", loc= "center")
ax3.set_ylabel("PC2", fontweight= "bold", loc= "center")
ax6.set_ylabel("PC3", fontweight= "bold", loc= "center")

ax6.set_xlabel("PC1", fontweight= "bold", loc= "center")
ax7.set_xlabel("PC2", fontweight= "bold", loc= "center")
ax8.set_xlabel("PC3", fontweight= "bold", loc= "center")


plt.savefig(Title, dpi= 240)
plt.show()

# Closing

print(" \n * \n")






# ***  Normalize and Standardize Example  ***
#
#  Project: Normalize and Standardize
# Filename: NormStand_v01
#  Creator: EKChikui (EKChikui@gmail.com)
#     Date: 14th Apr 2021
#  Version: 01
#
# -----------------------------------------------------------------------

# Libraries -------------------------------------------------------------

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from HistBoxInfoNormal_v10 import *



# Setup -----------------------------------------------------------------

Seed = 123
np.random.seed(Seed)

Size = 2000
roundsize= 3



# Definitions -----------------------------------------------------------

def Norm_MinMax(x, Min, Max):

    z = (x - Min)/(Max - Min)

    return z


def Norm_StandScore(x, Mean, StdDev):

    z = (x - Mean)/StdDev

    return z





# MAIN Program ----------------------------------------------------------

print("\n ***  Standardize or Normalize Study  ***\n")

No_Bins = int(np.sqrt(Size) + 0.5)

if(No_Bins % 2 == 0):
    No_Bins = No_Bins-1


# Creating Data

Data01 = np.random.normal(loc= 10, scale= 30, size= Size)

Data01_mean = np.around(np.mean(Data01), decimals= roundsize)
Data01_stddev = np.around(np.std(Data01), decimals= roundsize)
Data01_min = np.amin(Data01)
Data01_max = np.amax(Data01)


Data02 = np.random.normal(loc= 200, scale= 20, size= Size)

Data02_mean = np.around(np.mean(Data02), decimals= roundsize)
Data02_stddev = np.around(np.std(Data02), decimals= roundsize)
Data02_min = np.amin(Data02)
Data02_max = np.amax(Data02)


# Normalization

Data01_Norm = []
Data02_Norm = []

i = 0
while(i < Size):

    z = Norm_StandScore(Data01[i], Data01_mean, Data01_stddev)
    Data01_Norm.append(z)

    z = Norm_StandScore(Data02[i], Data02_mean, Data02_stddev)
    Data02_Norm.append(z)

    i = i+1


# Creating Figure

fig = plt.figure(figsize= (8, 5.67))
gs = GridSpec(2, 2, figure= fig)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])


ax1.hist(Data01, bins= No_Bins, color= "royalblue")
ax1.set_xlim([-100, 300])
ax1.set_ylim([0, 200])

ax1.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax1.set_axisbelow(True)


ax2.hist(Data02, bins= No_Bins, color= "darkred")
ax2.set_xlim([-100, 300])
ax2.set_ylim([0, 200])

ax2.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax2.set_axisbelow(True)


ax3.hist(Data01_Norm, bins= No_Bins, color= "lightblue")
#ax3.set_xlim([0, 1])
ax3.set_ylim([0, 200])

ax3.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax3.set_axisbelow(True)


ax4.hist(Data02_Norm, bins= No_Bins, color= "lightcoral")
#ax4.set_xlim([0, 1])
ax4.set_ylim([0, 200])

ax4.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax4.set_axisbelow(True)


fig.suptitle("Normalization Standard Score")

fig.tight_layout()
fig.savefig("StandardScore Study.png", dpi= 240)
plt.show()



# Sources ---------------------------------------------------------------

# Standardize or Normalize?
# https://medium.com/@rrfd/standardize-or-normalize-examples-in-python-e3f174b65dfc


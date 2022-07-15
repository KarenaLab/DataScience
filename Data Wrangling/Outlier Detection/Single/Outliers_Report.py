
#   Project: Outliers_Report
#  Filename: OutliersReport
#   Creator: EKChikui, 
#      Date: Sep 01st, 2021
#   Version: 01
#     Descr: 
#

# Version Control -------------------------------------------------------

# 01 - 01/09/2021 - Launch Edition
# 02 - 


# Libraries -------------------------------------------------------------

import numpy as np
import pandas as pd

from pandas.api.types import is_numeric_dtype, is_string_dtype

from TurkeyOutliers_v02 import *
from ZScoreOutliers_v01 import *
from MADOutliers_v02 import *


# Definitions -----------------------------------------------------------



# Setup -----------------------------------------------------------------



# MAIN Program ----------------------------------------------------------

print("\n ****  Outliers Report  **** \n")


Filename = "hmeq.csv"
DF = pd.read_csv(Filename, sep= ",")

DF_Rows = DF.shape[0]
DF_Cols = DF.shape[1]
DF_Columns = DF.columns

DF_Numeric = []

for col in DF_Columns:

    if(is_numeric_dtype(DF[col]) == True):

        DF_Numeric.append(col)

    else:
        print(f" > Column [{col}] is NOT numeric")


print("\n")

print(" Column Name             -     Turkey      ZScore         MAD ")
print(" -------------------------------------------------------------")
#      123456789_123456789_123456789_123456789_123456789_123456789_12
#       col_with_maximum_length -    1000000     1000000     1000000


for col in DF_Numeric:

    Col_Name = col

    if(len(Col_Name) > 23):
       Col_Name = Col_Name[0:23]

    Col_Name_Space = (23-len(Col_Name)) * " "
    
    Turkey = str(len(TurkeyOutliers(DF, col)))
    Turkey_Space = (10-len(Turkey)) * " "

    ZScore = str(len(ZScoreOutliers(DF, col)))
    ZScore_Space = (12-len(ZScore)) * " "

    MAD = str(len(MADOutliers(DF, col)))
    MAD_Space = (12-len(MAD)) * " "

                    
    Text = f" {Col_Name}{Col_Name_Space} - {Turkey_Space}{Turkey}{ZScore_Space}{ZScore}{MAD_Space}{MAD}"
    print(Text)   


print("")


# Closing

print(" * \n")



import numpy as np
import pandas as pd

from Binning_v01 import *


Data_Size = [10, 50, 100, 102, 400, 500, 950, 1000, 1024, 1200, 1300,
             1400, 2000, 2222, 2345]

for i in Data_Size:

    bins = Binning(i, IQR= 50, method= "Freedman-Diaconis")
    print(f" > Size: {i} -> Bins: {bins}")


print("")

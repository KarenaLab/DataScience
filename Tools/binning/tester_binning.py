
import numpy as np

from binning_v02 import *


data_size = [10, 50, 100, 102, 400, 500, 950, 1000, 1024, 1200, 1300,
             1400, 2000, 2222, 2345]

for i in data_size:
    #method: sqrt*, rice, sturges and freedman methods. 
    #bins = binning(i, method="sqrt")
    bins = binning(i, IQR=50, method="Freedman-Diaconis")
    print(f" > Size: {i} -> Bins: {bins}")


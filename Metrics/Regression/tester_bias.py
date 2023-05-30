
# Libraries
import numpy as np
from metrics_bias_v01 import *


# Program
y_test = [3.0, 4.0, 3.0, 5.0, 4.0, 6.0, 7.0, 8.0, 9.0, 2.0]
y_pred = [2.4, 3.8, 3.2, 5.3, 4.5, 6.7, 7.2, 8.4, 9.5, 2.2]

bias = metrics_bias(y_test, y_pred)
print(bias)


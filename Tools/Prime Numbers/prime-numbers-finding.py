
# Libraries
import numpy as np
from prime_numbers_v01 import *


# Program ---------------------------------------------------------------

limit = [10, 100, 1000, 10000]

for i in limit:
    prime_number_list, _ = prime_numbers(i)
    print(f" > from 1 to {i} has {len(prime_number_list)} prime numbers.")
    

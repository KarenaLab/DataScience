
# Tester

# Libraries
import numpy as np
import pandas as pd

from datetime_mngt_v01 import *


start_date = "12-06-2023"

next_meeting = next_date(start_date, 45)
print_datetime(next_meeting)

today_plus10 = next_date(today(), 10)



# Name [P440]
# SQL Tools for Data Science

# Versions
# 01 - Oct 10th, 2024 - Starter
# 02 - Oct 14th, 2024 - Add Connection and Close functions


# Insights, improvements and bugfix
#


# Libraries
import sqlite3

import numpy as np
import pandas as pd


# ----------------------------------------------------------------------
def database_connection(filename):
    global conn, cursor

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    return None


def database_close():
    global conn, cursor

    cursor.close()
    conn.close()

    return None


# end


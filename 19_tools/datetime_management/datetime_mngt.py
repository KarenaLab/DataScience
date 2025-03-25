# Date and Time management (P338) ---------------------------------------
# Simple functions with datetime to support date and time calc.

# Versions
# 01 - Jun 13th, 2023 - Starter
#    - Jul 04th, 2023 - Adjust style and organization
# 02 - 


# Insights, improvements and bugs
#


# Libraries
import datetime

import numpy as np
import pandas as pd


# ----------------------------------------------------------------------

def today(date_format="%d-%m-%Y"):
    """
    Returns **today** from system.
    Attention: Standard **date_format** = dd-mm-yyyy.

    """
    return datetime.date.today()


def print_datetime(date, date_format="%d-%m-%Y"):
    """
    Prints the datetime in selected **date_format**.
    Attention: Standard **date_format** = dd-mm-yyyy.
    
    """
    print(date.strftime(date_format))

    return None


def next_date(start_date, days, date_format="%d-%m-%Y"):
    """
    Add a number of **days** for a initial **start_date**.
    Attention: Standard **date_format** = dd-mm-yyyy.

    """
    if(isinstance(start_date, str) == True):
        start_date = datetime.datetime.strptime(start_date, date_format)

    final_date = start_date + datetime.timedelta(days=days)

    return final_date


def time_between(start_date, final_date, date_format="%d-%m-%Y", verbose=True):
    """
    Returns the number of days between **start_date** and **final_date**.
    Attention: Standard **date_format** = dd-mm-yyyy.

    """
    # Format validation/transformation
    if(isinstance(start_date, str) == True):
        start_date = datetime.datetime.strptime(start_date, date_format)

    if(isinstance(final_date, str) == True):
        final_date = datetime.datetime.strptime(final_date, date_format)


    if(final_date >= start_date):
        time = final_date - start_date

    else:
        time = np.nan

        if(verbose == True):
            print(f" >>> Error: `final_date` is before `start_date`.")

    return time


def truncate_date(datestamp):
    """
    Removes hour from datestamp.

    """
    if(isinstance(datestamp, datetime) == True):
        trunc_date = datestamp.replace(hour=0, minute=0, second=0, microsecond=0)

    else:
        trunc_date = ""


    return trunc_date


# end

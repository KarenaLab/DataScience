# String to date (P228) ------------------------------------------------
# Convert a pandas column from string to python datetime.

# Versions
# 01 - Mai 30th, 2023 - Starter
# 02 - Jul 04th, 2023 - Adjust style and organization
# 03 -


# Insights, improvements and bugfix
#    Add control of old column (to keep it or delete it)
#    Add verbose controls and messages


# Libraries
import pandas as pd


# ----------------------------------------------------------------------

def string_to_date(DataFrame, source, destiny=""):
    """
    Tranforms the column source stored as string into a new column
    destiny as python datetime format.

    DataFrame = DataFrame to be transformed,
    source = column with the datetime stored as string
    destiny = (optional). if not informed, source will be replaced.

    """   
    data = DataFrame.copy()

    if(destiny == ""):
        destiny = source

    data[destiny] = pd.to_datetime(data[source])

    if(source != destiny):
        data = data.drop(columns=[source])

    data = data.sort_values(by=destiny).reset_index(drop=True)


    return data


# Checking Columns Names

def ColumnsChecker(DF):

    import numpy as np
    import pandas as pd



    # Versions ---------------------------------------------------------

    # 01 - Oct 14th, 2021 - Starter
    # 02 -


    # List of Variables and kwargs -------------------------------------

    #
    #



    # Program ----------------------------------------------------------

    DF_Columns = DF.columns
    New_Columns = []

    keyfinder = "ultrn"
    # U= Upper, L= lower, T= Title, R= Rename or N= Nothing

    i = 0
    while(i < len(DF_Columns)):

        col = DF_Columns[i].strip()

        print(f" >>> Column {i} = {col}")

        option = input("     (u) UPPER, (l) lower, (t) Title, (r) Rename or (n) Nothing: ")
        option = option.lower()

        if(keyfinder.find(option, 0) >= 0):

            if(option == "u"):
                col = col.upper()

            if(option == "l"):
                col = col.lower()

            if(option == "t"):
                col = col.lower().title()

            if(option == "r"):
                col = input("     >>> Type the new column Name: ")

        else:
            print("     **** Wrong choose. Nothing Done **** \n")
                    

        col = col.replace(" ", "_")
        col = col.replace("-", "_")

        New_Columns.append(col)
        print("")        

        i = i+1


    return New_Columns

    

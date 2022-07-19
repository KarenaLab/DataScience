# Checking Columns Names

def columns_checker(DF):
    """
    Check columns names and gives interactive options to change its
    names.

    """

    import numpy as np
    import pandas as pd


    # Versions ---------------------------------------------------------

    # 01 - Oct 14th, 2021 - Starter
    # 02 - Apr 26th, 2022 - Adjusting for PEP-008
    # 03 - 


    # Program ----------------------------------------------------------  
    DF_columns = DF.columns
    new_columns = []

    keyfinder = "ultrn"
    # U=UPPER, L=lower, T=Title, R=Rename or N=Nothing

    for col in DF_columns:
        print(f" > Column {i} = {col}")
        option = input("   (u) UPPER, (l) lower, (t) Title, (r) Rename or (n) Nothing: ")
        option = option.lower()

        col = col.strip()
        if(keyfinder.find(option, 0) >= 0):
            if(option == "u"):
                col = col.upper()

            if(option == "l"):
                col = col.lower()

            if(option == "t"):
                col = col.lower()\
                         .title()

            if(option == "r"):
                col = input("   > type the new column name: ")


            col = col.replace(" ", "_")\
                     .replace("-", "_")\
                     .replace("(", "")\
                     .replace(")", "")
            
            new_columns.append(col)
            print("")        
            
        else:
            print("   **** Wrong choose. Check the options and do it again **** \n")

                    
    print(" >>> Columns Name Check Done! \n")
    
    return new_columns


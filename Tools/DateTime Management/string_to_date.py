
def string_to_date(DF, source, destiny=""):
    """
    Convert from string to datetime.

    """
    import pandas as pd
    
    data = DF.copy()

    if(destiny == ""):
        destiny = source

    data[destiny] = pd.to_datetime(data[source])

    if(source != destiny):
        data = data.drop(columns=[source])

    data = data.sort_values(by=destiny).reset_index(drop=True)


    return data


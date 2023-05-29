
def metrics_bias(true, pred, verbose=True):
    """
    Calculates the difference 

    """
    import numpy as np
    
    true = np.array(true)
    true = true[~np.isnan(true)]    # Removes np.nan values
    
    pred = np.array(pred)
    pred = pred[~np.isnan(pred)]    # Removes np.nan values


    if(true.size == pred.size):
        bias = np.sum((true - pred))
        
    else:
        bias = np.nan

        if(verbose == True):
            print(f" > True and Pred **does not** have the same size")


    return bias


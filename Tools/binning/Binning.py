
def binning(size, method="square", **kwargs):
    """
    Calculates the optimal (or best) binning size for histogram.
    Methods available: sqrt*, rice, sturges and freedman-diaconis. 

    """
    import numpy as np

    # version
    # 01 - Sep 28th, 2021 - Starter,
    # 02 - Jan 10th, 2023 - adjusting PEP-008 and adding sturges method,
    # 03 - 

    # Program ----------------------------------------------------------
    method = method.lower()

    if(method == "square" or method == "sqrt"):
        # Equation = sqrt(size)
        bins = int(np.sqrt(size) + 0.5)       
        if(size >= 500):          
            # if size > 500, bins are always odd.
            if(bins % 2 == 0):
                bins = bins+1


    if(method == "rice" or method == "ricerule"):
        # Equation = 2* root(size, 3)
        bins = int((2 * np.cbrt(size)) + 0.5)

        
    if(method == "sturges" or method == "sturge"):
        # https://www.statology.org/sturges-rule/
        # Equation = log(n,2) + 1
        bins = int((np.log2(size)+1) + 0.5)


    if(method == "freedman" or method == "freedman-diaconis" or
       method == "freedmandiaconis" or method == "freedman_diaconis"):
        # https://en.wikipedia.org/wiki/Freedman-Diaconis_rule
        #
        #                     IQR(x)
        # Equation = 2 * --------------- 
        #                 root(size, 3)

        IQR = kwargs.get("IQR")
        if(IQR == None):
            print(" >> Warning: Missing IQR Value")
            bins = None

        else:
            bins = int((2*(IQR/np.cbrt(size) + 0.5)))          


    return bins


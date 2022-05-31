
def Binning(size, **kwargs):

    # Calculating the best number of bins for a Histogram.
    # Methods: square*, Rice Rule, Sturges and Freedman-Diaconis.

    import numpy as np


    # Versions ---------------------------------------------------------

    # 01 - Sep 28th, 2021 - Starter
    # 02 -


    # List of Variables and **kwargs -----------------------------------

    # Size = Number of items of Sample
    # Method = Square*, Sturges or Freedman-Diaconis,
    #

    # Program ----------------------------------------------------------
    get = kwargs.get("method")

    if(get == None):
        get = "square"

    get = get.lower()

    if(get == "square" or get == ""):
        if(size < 500):
            # Equation = sqrt(Size)
            bins = int(np.sqrt(size) + 0.5)

        else:
            bins = int(np.sqrt(size))
            # if Size >= 500, bins are always odd

            if(bins % 2 == 0):
                bins = bins+1


    if(get == "rice" or get == "ricerule"):
        # Equation = 2* root(Size, 3)
        bins = int((2 * np.cbrt(Size)) + 0.5)

    if(get == "sturges" or get == "sturge"):
        # https://www.statology.org/sturges-rule/
        # Equation = log(n,2) + 1
        bins = int((np.log2(Size)+1) + 0.5)

    if(get == "freedman" or get == "freedman-diaconis" or
       get == "freedmandiaconis" or get == "freedman_diaconis"):
        # https://en.wikipedia.org/wiki/Freedman-Diaconis_rule
        #                     IQR(x)
        # Equation = 2 * --------------- 
        #                 root(Size, 3)

        IQR = kwargs.get("IQR")

        if(IQR == None):
            print(" >> Warning: Missing IQR Value")
            bins = None

        else:
            bins = int((2*IQR)/(np.cbrt(size)) + 0.5)          


    return bins



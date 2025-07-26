# [P208] Elbow Distance for K-Means clustering --------------------------

# Libraries
import numpy as np


# -----------------------------------------------------------------------
def calc_elbowdistance(pk, pi, pn):
    """
    Calculates the distance from a line draw line between **pi** and **pn**
    to a point **pn**.

    where:
    * pi = [x1, y2] (initial)
    * pn = [x2, y2] (last)
    * pk = [x, y]   (k, or the variable point)


    Equation:
    
            |(x2 - x1)*(y1 - y0) - (x1 - x0)*(y2 - y1)|
    dist = ---------------------------------------------
                  sqrt((x2 - x1)^2 + (y2 - y1)^2)


    LaTex eq: dist = \frac{|(x_{2}-x_{1})(y_{1}-y_{0})-(x_{1}-x_{0})(y_{2}-y_{1})|}{\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}}

    """

    # Splitting points into coordinates (easy apply in equation)
    x1, y1 = pi[0], pi[1]
    x2, y2 = pn[0], pn[1]
    x, y = pk[0], pk[1]

    # Calc
    numerator = np.abs((x2 - x1) * (y1 - y)) - np.abs((y2 - y1) * (x1 - x))
    denominator = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist = numerator / denominator

    return dist


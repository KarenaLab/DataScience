
def elbowdistance(p1, p2, p3):
    """
    Calculates the distance from a line draw line between p1 and p2
    to a point (p3).

    p1 = [x1, y2]
    p2 = [x2, y2]
    p3 = [x, y]

    """

    # Versions
    # 01 - Jun 22nd, 2022 - Starter
    # 02 -


    # Insights:
    # Inform line as an equation
    #

    
    # Program ---------------------------------------------------------
    import numpy as np

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x, y = p3[0], p3[1]

    numerator = np.abs((x2-x1)*(y1-y)) - np.abs((y2-y1)*(x1-x))
    denominator = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    dist = numerator/denominator

    return dist


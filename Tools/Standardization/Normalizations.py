# Normatizations
# https://en.wikipedia.org/wiki/Normalization_(statistics)


def Norm_MinMax(x, Min, Max):

    z = (x - Min)/(Max - Min)

    return z



def Norm_StandScore(x, Mean, StdDev):

    z = (x - Mean)/StdDev

    return z



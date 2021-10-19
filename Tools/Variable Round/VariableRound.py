
def VariableRound(number):

    from numpy import around
    
    get = abs(number)

    if(get >= 10000):
        round_size = 0

    if(get >= 1000 and get < 10000):
        round_size = 1

    if(get >= 100 and get < 1000):
        round_size = 2

    if(get >= 10 and get < 100):
        round_size = 3

    if(get >=1 and get < 10):
        round_size = 4

    if(get < 1):
        round_size = 5


    return around(number, decimals= round_size)


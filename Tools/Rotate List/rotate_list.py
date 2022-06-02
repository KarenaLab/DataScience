
import numpy as np

def rotate_left(array, steps):
    """
    Rotates list left with n steps.
    """

    if(isinstance(array, np.ndarray) == True):
        array = array.tolist()

    new_array = array[steps: ] + array[ :steps]

    return new_array


def rotate_right(array, steps):
    """
    Rotates list right with n steps.
    """

    if(isinstance(array, np.ndarray) == True):
        array = array.tolist()

    new_array = array[-steps: ] + array[ :-steps]

    return new_array


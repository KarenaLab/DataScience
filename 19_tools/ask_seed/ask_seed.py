# Ask a seed [P375]

# Versions
# 01 - Oct 14th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import random



# ----------------------------------------------------------------------
def ask_seed():
    """
    Returns a single number to be used as seed.
    Use it just in case of doubt (or lazyness).

    """
    container = [302, 105, 275, 226, 207, 308, 42, 137, 255, 288,
                 307, 1016, 2010, 1016]

    random.shuffle(container)
    selection = container[0]
    

    return selection


# end


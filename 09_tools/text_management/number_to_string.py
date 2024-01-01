# Name [P390]
# Transforms numbers to string 

# Versions
# 01 - Jan 01st, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries


# ----------------------------------------------------------------------
def number_to_string(number, decimals=6, fill="zero", verbose=False):
    """
    Tranforms a float or integer number into a string with delimited
    space. Useful for alignment of numbers at screen (or print).

    """
    # Fill character selection
    if(fill == "space" or fill == "empty" or fill == " "):
        space = " "

    elif(fill == "zero" or fill == "zeros" or fill == "0"):
        space = "0"

    else:
        space = "0"

        if(verbose == True):
            print(f' > Warning: Fill option not at list. Using default value ["0"]')


    # Number treatment
    if(isinstance(number, (int, float)) == True):
        n_text = str(round(number, ndigits=decimals))

        if(n_text.count(".") > 0):
            # Float number
            integer, digits = n_text.split(".")
            digits = digits + ((decimals - len(digits)) * space)

        else:
            # Integer number
            integer = n_text
            digits = (decimals * space)

        n_text = integer + "." + digits

    else:
        # Not a number, return the same information
        n_text = number
     

    return n_text


# end

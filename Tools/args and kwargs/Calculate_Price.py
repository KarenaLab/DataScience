# Tester Arg and Kwargs

def calculate_price(value, **kwargs):

    tax_percentage = kwargs.get("tax_percentage")
    discount = kwargs.get("discount")

    if tax_percentage:
        print(f"Tax Percentage = {tax_percentage}")
        value = value + value * (tax_percentage/100)


    if discount:
        print(f"Discount = {discount}")
        value = value - discount


    return value


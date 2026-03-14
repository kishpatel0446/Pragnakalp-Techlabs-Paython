def calculate_power(base, exponent):

    #Handle edge Case when exponent is 0
    if exponent == 0:
        return 1

    result = 1
    count = 0

    if exponent > 0:
        while count < exponent:
            result = result * base
            count += 1
        return result

    #Handle Case when exponent is negative
    exponent = -exponent
    while count < exponent:
        result = result * base
        count += 1
    return 1/result

#Take Base & Exponent from the user
try:
    base = int(input("Enter Base: "))
    exponent = int(input("Enter Exponent: "))

    print(calculate_power(base, exponent))

#Handle for Invalid Input
except ValueError:
    print("Invalid Input")
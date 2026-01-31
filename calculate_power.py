def calculatePower(base,exponent):

    if exponent == 0:
        return 1

    result = 1
    count = 0

    if exponent > 0:
        while count < exponent:
            result = result * base
            count += 1
        return result

    exponent = -exponent
    while count < exponent:
        result = result * base
        count += 1
    return 1/result

try:
    base = int(input("Enter Base: "))
    exponent = int(input("Enter Exponent: "))

    print(calculatePower(base,exponent))
except ValueError:
    print("Invalid Input")
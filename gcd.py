def find_gcd(num1,num2):

    if num1 == 0 and num2 == 0:
        return "GDC IS UNDEFINED FOR 0"

    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    while num2 != 0:
        rem = num1 % num2
        num1 = num2
        num2 = rem
    return num1

#Handle Invalid Input
try:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    print(find_gcd(num1,num2))

except ValueError:
    print("Enter Valid Numbers")


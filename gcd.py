def gcd(num1,num2):

    while num2 != 0:
        rem = num1 % num2
        num1 = num2
        num2 = rem
    return num1

try:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    print(gcd(num1,num2))

except ValueError:
    print("Enter Valid Numbers")


def is_palindrome(number):

    num = number
    rev = 0

    while number > 0:
        d = number % 10
        rev = rev * 10 + d
        number = number // 10
    if rev == num:
        print("True")
    else:
        print("False")


try:
    n = int(input("Enter Number: "))
    is_palindrome(n)
except ValueError:
    print("Invalid Number")







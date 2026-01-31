def isPalindrome(n):

    num = n
    rev = 0

    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    if rev == num:
        print("True")
    else:
        print("False")


try:
    n = int(input("Enter Number: "))
    isPalindrome(n)
except ValueError:
    print("Invalid Number")







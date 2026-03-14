#Input from user with exception handling
try:
    n = int(input("Enter Number:"))
except ValueError:
    print("Invalid Input. There is no other datatype allowed except integer")
else:
    rev = 0
    is_neg = False

    # Handle Negative
    if n < 0:
        is_neg = True
        n = -n
    # Reverse Number using While loop
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    # Put negative symball if number is negative
    if is_neg:
        rev = -rev

    #Print Output
    print(rev)

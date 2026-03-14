#Input from user with exception handling
try:
    n = int(input("Enter Number:"))
except ValueError:
    print("Invalid Input. There is no other datatype allowed except integer")
else:
    if n < 0:
        print("Invalid input")
    else:
        f = 1
        i = 1

        while i <= n:
            f = f * i
            i += 1
        print(f)
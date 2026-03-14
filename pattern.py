#Input from user with exception handling
try:
    n = int(input("Enter Number:"))
except ValueError:
    print("Invalid Input. There is no other datatype allowed except integer")
else:
    #Handle edge Cases
    if n < 1:
        print("Invalid Input")
    else:
        for i in range(1,n + 1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
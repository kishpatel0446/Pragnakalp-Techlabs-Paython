#Input from user with exception handling
try:
    n = int(input("Enter Number:"))
except ValueError:
    print("Invalid Input. There is no other datatype allowed except integer")
else:
    #Handle edge Cases
    if n <= 1:
        print("Not Prime")
    else:
        is_prime = True

        #check if number is divisable with any number from range 2 to n
        for i in range(2,n):
            #if number is divisible set is_prime false & break the loop
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime Number")
        else:
            print("Not Prime")
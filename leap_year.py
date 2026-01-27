try:
    year = int(input("Enter Year: "))

    if year <= 0:
        print("Please Enter Valid Year!")
    elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
except ValueError:
    print("Enter Valid Year!")
def count_digit_frequency(number,digit):

    count = 0
    # For Digit range 0 to 9
    if digit < 0 or digit > 9:
        print("Invalid Digit. Digit must be in range from 0 to 9")
    else:
        # for negative number
        if number < 0:
            number = -number

        temp = number

        while temp > 0:
            d = temp % 10
            if d == digit:
                count += 1
            temp = temp // 10
        print(count)

# Handle Invalid Input
try:
    num = int(input("Enter Number: "))
except ValueError:
    print("Invalid Number!")
    exit()
try:
    dig = int(input("Enter Digit You Want to Count: "))
except ValueError:
    print("Invalid Digit!")
    exit()

count_digit_frequency(num,dig)

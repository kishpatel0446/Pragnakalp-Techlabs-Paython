#Take Units From The User
try:
    units = int(input("Enter Consumed Units: "))

    bill = 0

    #Handle Negative Units
    if units < 0:
        print("Invalid Units, It Can't less than 0.")

    #Handle 0 Units
    elif units == 0:
        print("Total Electricity Bill: 0")
    elif units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)

    print("Total Electricity Bill: ₹", bill)

except ValueError:
    print("Invalid Units.")


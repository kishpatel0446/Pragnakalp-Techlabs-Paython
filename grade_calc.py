try:
    marks = int(input("Enter Marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid Marks. Please Enter Marks Between 0 to 100.")
    elif marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")
    else:
        print("F")
except ValueError:
    print("Invalid Marks. Please Enter Marks Between 0 to 100.")
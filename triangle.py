try:
    a = int(input("Enter Side a: "))
    b = int(input("Enter Side b: "))
    c = int(input("Enter Side c: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid Sides")
    elif (a + b > c) and ( a + c > b) and (b + c > a):
        if a == b == c:
            print("Valid Triangle: Equilateral")
        elif a == b or a == c or b == c:
            print("Valid Triangle: Isosceles")
        else:
            print("Valid Triangle: Scalane")
    else:
        print("Not a Valid Triangle")
except ValueError:
    print("Please Enter Valid Sides!")
a = int(input("Enter Number a: "))
b = int(input("Enter Number b: "))
c = int(input("Enter Number c: "))

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
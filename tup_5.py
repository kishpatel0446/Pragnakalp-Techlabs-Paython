# Take tuples as input
t = eval(input("Enter first tuple: "))

i = len(t) - 1

print("(", end="")

while i >= 0:
    print(t[i], end="")
    if i !=0:
        print(",",end="")
    i -= 1
print(")")
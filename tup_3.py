# Take tuples as input
t1 = eval(input("Enter first tuple: "))
t2 = eval(input("Enter second tuple: "))

print("(", end="")

i = 0
while i < len(t1):
    print(t1[i], end="")
    if i < len(t1) - 1 or len(t2) != 0:
        print(", ", end="")
    i = i + 1

j = 0
while j < len(t2):
    print(t2[j], end="")
    if j < len(t2) - 1:
        print(", ", end="")
    j = j + 1

print(")")
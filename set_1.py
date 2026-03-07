s1_input = input("Enter first set: ")
s2_input = input("Enter second set: ")
if s1_input == "":
    s1 = set()
else:
    s1 = eval(s1_input)

if s2_input == "":
    s2 = set()
else:
    s2 = eval(s2_input)
print("{", end="")

first = True

for x in s1:
    if first == False:
        print(",", end="")
    print(x, end="")
    first = False

for y in s2:
    found = False

    for x in s1:
        if y == x:
            found = True
            break
    if found == False:
        if first == False:
            print(",", end="")
        print(y, end="")
        first = False
print("}")

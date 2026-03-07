# Take tuples as input
t = eval(input("Enter first tuple: "))
element = eval(input("Enter Element: "))

i = 0
index = -1

while i < len(t):
    if t[i] == element:
        index = i
        break
    i += 1
print(index)
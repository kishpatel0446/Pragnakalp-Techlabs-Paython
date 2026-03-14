tup = eval(input("Enter Tuple (End of each value add comma(,): "))

ele = eval(input("Enter element for count: "))

count = 0
i = 0

while i < len(tup):
    if tup[i] == ele:
        count += 1
    i += 1

print(count)


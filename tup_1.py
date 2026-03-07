tup = eval(input("Enter Tuple (End of each value add comma(,):"))

min_t = tup[0]
max_t = tup[0]

i = 0
while i < len(tup):
    if tup[i] < min_t:
        min_t = tup[i]

    if tup[i] > max_t:
        max_t = tup[i]

    i += 1

print("Maximum:",max_t, ", Minimum:",min_t)

d1_input = input("Dict1: ")
d2_input = input("Dict2: ")
if d1_input == "":
    d1 = {}
else:
    d1 = eval(d1_input)

if d2_input == "":
    d2 = {}
else:
    d2 = eval(d2_input)

res = {}

for k in d1:
    res[k] = d1[k]

for k in d2:
    found = False

    for r in res:
        if r == k:
            res[r] = res[r] + d2[k]
            found = True
            break
    if found == False:
        res[k] = d2[k]
print(res)
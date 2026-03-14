d_input = input("Dict: ")

if d_input == "":
    print({})
else:
    d = eval(d_input)

    inv = {}

    for k in d:
        v = d[k]
        inv[v] = k
    print(inv)
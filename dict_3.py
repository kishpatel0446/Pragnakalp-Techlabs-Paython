d_input = input("Dict: ")

if d_input == "":
    print("Dictionary is Empty")
else:
    d = eval(d_input)

    max_key = None
    max_value = None
    first = True

    for k in d:
        if first == True:
            max_key = k
            max_value = d[k]
            first = False
        else:
            if d[k] > max_value:
                max_value = d[k]
                max_key = k
    print(max_key)
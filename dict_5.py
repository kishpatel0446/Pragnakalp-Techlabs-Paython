l_input = input("Enter List: ")

if l_input == "":
    print({})
else:
    words = eval(l_input)

    res = {}

    for word in words:
        chars = []
        for ch in word:
            chars = chars + [ch]

        n = 0
        for c in chars:
            n = n + 1
        i = 0
        while i < n:
            j = 0
            while j < n - 1:
                if chars[j] > chars[j + 1]:
                    temp = chars[j]
                    chars[j] = chars[j + 1]
                    chars[j + 1] = temp
                j = j + 1
            i = i + 1
        key = ""
        for c in chars:
            key = key + c
        found = False

        for k in res:
            if k == key:
                res[k] = res[k] + [word]
                found = True
                break
        if found == False:
            res[key] = [word]
    # print(res)

    print("{")

    for k in res:
        print(" '"+k+"':",res[k],",")
    print("}")
text = input("Enter a string: ")

res = ""
i = 0

while i < len(text):
    ch = text[i]

    f = False
    j = 0

    while j < len(res):
        if res[j] == ch:
            f = True
            break
        j += 1

    if f == False:
        res += ch

    i += 1
print(res)
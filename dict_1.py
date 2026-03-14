s = input("Enter String: ")

freq = {}

for ch in s:
    found = False

    for key in freq:
        if key == ch:
            freq[key] = freq[key] + 1
            found = True
            break
    if found == False:
        freq[ch] = 1
print(freq)
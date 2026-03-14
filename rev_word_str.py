#Take Input From Usee
text = input("Enter a string: ")

res = ""
word = ""

i = 0
while i < len(text):
    if text[i] != " ":
        word += text[i]
    else:
        if word != "":
            #Reverse word
            rev_word = ""
            j = len(word) - 1
            while j >= 0:
                rev_word += word[j]
                j -= 1
            if res != " ":
                res += ""
            res += rev_word
            word = ""
    i += 1

#Handle Last Word
if word != "":
    rev_word = ""
    j = len(word) - 1
    while j >= 0:
        rev_word += word[j]
        j -= 1
    if res != "":
        res += " "
    res += rev_word
print(res)
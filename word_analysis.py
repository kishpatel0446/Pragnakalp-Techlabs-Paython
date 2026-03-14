def to_lower(text):
    result = ""
    i = 0
    while True:
        try:
            ch =text[i]
        except:
            break

        if ch >= 'A' and ch <= 'Z':
            result += chr(ord(ch)+32)
        else:
            result += ch
        i +=1
    return result

def get_words(text):
    words = []
    word = ""
    i = 0

    while True:
        try:
            ch =text[i]
        except:
            break

        if(ch >='a' and ch <= 'z'):
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""
        i +=1
    if word != "":
         words.append(word)
    return words

def count_freq(words):
    freq = {}

    i = 0
    while True:
        try:
            word =words[i]
        except:
            break

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
        i += 1
    return freq


def top_three(freq):
    top_words = ["","",""]
    top_count = [0,0,0]

    for word in freq:
        count = freq[word]

        if count > top_count[0]:
            top_count[2] = top_count[1]
            top_words[2] = top_words[1]

            top_count[1] = top_count[0]
            top_words[1] = top_words[0]

            top_count[0] = count
            top_words[0] = word

        elif count > top_count[1]:
            top_count[2] = top_count[1]
            top_words[2] = top_words[1]

            top_count[1] = count
            top_words[1] = word

        elif count > top_count[2]:
            top_count[2] = count
            top_words[2] = word

    return top_words,top_count

input_file = input("Enter file name: ")
output_file = input("Enter output file name: ")

try:
    f = open(input_file,"r")
    text = f.read()
    f.close()

    text = to_lower(text)

    words = get_words(text)

    total_words = 0
    for w in words:
        total_words += 1

    freq = count_freq(words)

    unique_words = 0
    for w in freq:
        unique_words += 1

    top_words,top_count = top_three(freq)

    out = open(output_file,"w")
    out.write("Total words:" + str(total_words)+"\n")
    out.write("Unique words:" + str(unique_words)+"\n")
    out.write("Word frequency: \n")
    for word in freq:
        out.write(word + ":" + str(freq[word])+"\n")
    out.write("Top 3 words:")

    i=0
    while i < 3:
        if top_words[i] != "":
            out.write(top_words[i]+"("+str(top_count[i])+")")

            if i < 2:
                out.write(",")
        i += 1
    out.close()
    print("Done")
except:
    print("Error: File not found")
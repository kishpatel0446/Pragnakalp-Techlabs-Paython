filename = input("Enter file name: ")

try:
    fh = open(filename, "r")

    lc = 0
    wc = 0
    cc = 0

    for line in fh:
        lc = lc + 1

        for ch in line:
            cc = cc + 1

        in_words = False
        for ch in line:
            if ch not in [" ","\n","\t"]:
                if not in_words:
                    wc = wc + 1
                    in_words = True
            else:
                in_words = False
    fh.close()

    print("Lines = " + str(lc), "Words = " + str(wc), "Characters = " + str(cc))

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occured: {e}")


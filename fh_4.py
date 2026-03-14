import string
source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    import os
    if os.path.exists(destination_file):
        print("Destination file already exists")
    else:
        src = open(source_file, 'r')
        txt = src.read()
        src.close()

        if not txt.strip():
            print(f"Source file {source_file} is empty")

        txt = txt.lower()

        for ch in string.punctuation:
            txt = txt.replace(ch, "")

        words = txt.split()

        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        dest = open(destination_file, 'w')
        for word, count in frequency.items():
            dest.write(f"{word} : {count}\n")
        dest.close()

        print(f"{destination_file} has been created")
except FileNotFoundError:
    print(f"{source_file} does not exist")

except Exception as e:
    print(f"An error occurred: {e}")
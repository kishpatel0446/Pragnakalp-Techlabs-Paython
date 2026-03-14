source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")
find_word = input("Enter the word to find: ")
replace_word = input("Enter the replace word: ")

try:
    import os
    if os.path.exists(destination_file):
        print("Destination file already exists")
    else:
        src = open(source_file, 'r')

        lines = src.readlines()
        src.close()

        if not lines:
            print("Source file is empty")

        dest = open(destination_file, 'w')

        for line in lines:
            words = line.split(" ")
            for i in range(len(words)):
                if words[i] == find_word:
                    words[i] = replace_word
            newline = " ".join(words)
            dest.write(newline + "\n")
        dest.close()

        print("Destination file has been created")
except FileNotFoundError:
    print(f"Error: Source file {source_file} does not exist")
except Exception as e:
    print(f"An Error occured: {e}")
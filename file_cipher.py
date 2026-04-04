#Function for shift char
def shift_char (ch,shift):
    if 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + shift)%26 + ord('A'))
    elif 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + shift)%26 + ord('a'))
    else:
        return ch

#Function to encrypt text
def encrypt_text (text,shift):
    result = ""
    for ch in text:
        result += shift_char(ch,shift)
    return result

#Function to decrypt text
def decrypt_text (text,shift):
    result = ""
    for ch in text:
        result += shift_char(ch,-shift)
    return result

#Function for encrypt file
def encrypt_file (input_file,output_file,shift):
    try:
        f = open(input_file,'r')
        content = f.read()
        f.close()

        if content == "":
            print("File is empty")
            return

        encrypted = encrypt_text(content,shift)

        f = open(output_file,'w')
        f.write(encrypted)
        f.close()

        print("File is encrypted successfully.")

    except:
        print("Error while encrypting file.")

#Function for decrypt file
def decrypt_file (input_file,output_file,shift):
    try:
        f = open(input_file,'r')
        content = f.read()
        f.close()

        if content == "":
            print("File is empty")
            return

        decrypted = decrypt_text(content,shift)

        f = open(output_file,'w')
        f.write(decrypted)
        f.close()

        print("File is decrypted successfully.")

    except:
        print("Error while decrypting file.")

#Function for brute force decrypt
def brute_force_decrypt (input_file):
    try:
        f = open(input_file,'r')
        content = f.read()
        f.close()

        if content == "":
            print("File is empty")
            return

        print("\nBrute Force Results:\n")

        for shift in range(1,26):
            decrypted = decrypt_text(content,shift)
            print("Shift", shift, ":", decrypted)

    except:
        print("Error while decrypting file.")

while True:
    print("\n1.Encrypt File")
    print("2.Decrypt File")
    print("3.Brute Force Decrypt")
    print("4.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        infile = input("Enter input file name: ")
        outfile = input("Enter output file name: ")
        shift = int(input("Enter shift value (1-25): "))

        if 1<=shift<=25:
            encrypt_file(infile,outfile,shift)
        else:
            print("Shift must be between 1-25")

    elif choice == "2":
        infile = input("Enter input file name: ")
        outfile = input("Enter output file name: ")
        shift = int(input("Enter shift value (1-25): "))

        if 1<=shift<=25:
            decrypt_file(infile,outfile,shift)
        else:
            print("Shift must be between 1-25")

    elif choice == "3":
        infile = input("Enter input file name: ")
        brute_force_decrypt(infile)

    elif choice == "4":
        print("Exit")
        break

    else:
        print("Invalid input")

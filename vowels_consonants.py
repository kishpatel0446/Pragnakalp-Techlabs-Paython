def countVowelsAndConsonants(str):

    vowels = 0
    consonants = 0

    if str == "":
        print("Vowels:",vowels,", Consonants:",consonants)
        return

    for char in str:
        if('A' <= char <= 'Z') or ('a' <= char <= 'z'):

            if (char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or
                    char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U'):
                vowels += 1
            else:
                consonants += 1
    print("Vowels:", vowels, end=",")
    print(" Consonants:", consonants)


str = str(input("Enter String: "))
countVowelsAndConsonants(str)
def char_freq_count(string,char):
    count = 0

    for ch in string:
        if ch == char:
            count += 1
    print(count)

string = str(input("Enter String: "))
char = str(input("Enter Character for Count:"))

char_freq_count(string,char)
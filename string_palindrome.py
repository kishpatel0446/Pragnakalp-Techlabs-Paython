text = input("Enter a string: ")

left = 0
right = len(text) - 1
flag = True

while left < right:

    # Skip space from left
    if text[left] == " ":
        left += 1
        continue

    # Skip space from right
    if text[right] == " ":
        right -= 1
        continue

    ch1 = text[left]
    ch2 = text[right]

    # Convert case
    if ch1 >= 'A' and ch1 <= 'Z':
        ch1 = chr(ord(ch1) + 32)

    if ch2 >= 'A' and ch2 <= 'Z':
        ch2 = chr(ord(ch2) + 32)

    if ch1 != ch2:
        flag = False
        break

    left += 1
    right -= 1

if flag:
    print("Palindrome")
else:
    print("Not Palindrome")
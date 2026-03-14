nums = input("Enter list: ")

# Convert string to list manually
arr = []
num = ""
i = 0

while i < len(nums):
    ch = nums[i]

    # If digit or negative sign, build number
    if (ch >= '0' and ch <= '9') or ch == '-':
        num += ch
    else:
        if num != "":
            arr += [int(num)]
            num = ""

    i += 1

# Add last number if exists
if num != "":
    arr += [int(num)]

#Take Target sum
t = int(input("Enter Target: "))

n = len(arr)

f = False
i = 0

while i < n:

    # Skip duplicate first elements
    k = 0
    skip_i = False
    while k < i:
        if arr[k] == arr[i]:
            skip_i = True
            break
        k += 1

    if skip_i:
        i += 1
        continue

    j = i + 1
    while j < n:

        # Skip duplicate second elements
        x = i + 1
        skip_j = False
        while x < j:
            if arr[x] == arr[j]:
                skip_j = True
                break
            x += 1

        if skip_j:
            j += 1
            continue

        if arr[i] + arr[j] == t:
            print("(", arr[i], ",", arr[j], ")", sep="")
            f = True

        j += 1
    i += 1

if f == False:
    print("No Pairs Found")
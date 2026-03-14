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

# Handle edge case for less than 2 elements
if len(arr) < 2:
    print("No second largest element")

else:
    largest = arr[0]
    second = None
    i = 1

    while i < len(arr):

        if arr[i] > largest:
            second = largest
            largest = arr[i]

        elif arr[i] < largest:
            if second is None or arr[i] > second:
                second = arr[i]

        i += 1

    if second is None:
        print("No second largest element")
    else:
        print(second)
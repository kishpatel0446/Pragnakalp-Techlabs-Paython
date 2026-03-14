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

res = []
i = 0

while i < len(arr):
    cur = arr[i]
    f = False
    j = 0

    while j < len(res):
        if res[j] == cur:
            f = True
            break
        j += 1

    if f == False:
        res += [cur]
    i += 1
print(res)

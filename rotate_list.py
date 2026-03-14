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

k = int(input("Enter K: "))

n = len(arr)

if n == 0:
    print(arr)
else:
    if k > n:
        k = k % n
    if k == 0:
        print(arr)
    else:
        res = []

        i = n - k
        while i < n:
            res += [arr[i]]
            i += 1

        i = 0
        while i < n - k:
            res += [arr[i]]
            i += 1

        print(res)
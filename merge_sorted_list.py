# Take First List
l1 = input("Enter 1st Sorted List: ")
arr1 = []
num = ""
i = 0

while i < len(l1):
    ch = l1[i]

    if (ch >= '0' and ch <='9') or ch == '-':
        num += ch
    else:
        if num != "":
            arr1 += [int(num)]
            num = ""
    i += 1
if num!="":
    arr1 += [int(num)]

#Take 2nd List
l2 = input("Enter 2nd Sorted List: ")
arr2 = []
num = ""
i = 0

while i < len(l2):
    ch = l2[i]

    if (ch >= '0' and ch <='9') or ch == '-':
        num += ch
    else:
        if num != "":
            arr2 += [int(num)]
            num = ""
    i += 1
if num!="":
    arr2 += [int(num)]

# Merge Here

res = []
i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        res += [arr1[i]]
        i += 1
    else:
        res += [arr2[j]]
        j += 1
while i < len(arr1):
    res += [arr1[i]]
    i += 1

while j < len(arr2):
    res += [arr2[j]]
    j += 1

print(res)
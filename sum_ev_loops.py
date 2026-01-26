n = int(input("Enter a Number: "))

#Handle of Edge case n<1

if n < 1:
    print(0)
else:
    total = 0
    i = 1

    while i <= n:
        if i % 2 == 0:
            total += i
        i += 1
    print(total)

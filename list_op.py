#Function for check prime number



def is_prime(num):
    if num <= 1:
        return 0

    i = 2
    while i < num:
        if num % i == 0:
            return 0
        i += 1
    return 1

#Function for check perfect number
def is_perfect(num):
    if num <= 0:
        return 0

    sum = 0
    i = 1

    while i < num:
        if num % i == 0:
            sum += i
        i = i + 1
    if sum == num:
        return 1
    else:
        return 0

#Function to check armstrong number
def is_armstrong(num):
    if num < 0:
        return 0

    temp = num
    count = 0

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10

        power = 1
        i = 0
        while i < count:
            power = power * digit
            i = i + 1

        total = total + power
        temp = temp // 10
    if total == num:
        return 1
    else:
        return 0

#Take Input From User
nums = input("Enter numbers: ")

arr = []
num = ""
i = 0

while i < 1000:
    try:
        ch = nums[i]
    except:
        break

    if (ch >= '0' and ch <= '9') or ch == '-':
        num = num + ch
    else:
        if num != "":
            arr = arr + [int(num)]
            num = ""

    i = i + 1

if num != "":
    arr = arr + [int(num)]

prime_list = []
perfect_list = []
armstrong_list = []

i = 0
while i < 1000:
    try:
        num = arr[i]
    except:
        break

    if is_prime(num) == 1:
        prime_list = prime_list + [num]

    if is_perfect(num) == 1:
        perfect_list = perfect_list + [num]

    if is_armstrong(num) == 1:
        armstrong_list = armstrong_list + [num]

    i = i + 1

print("Prime Numbers: ",prime_list)
print("Perfect Numbers: ",perfect_list)
print("Armstrong Numbers: ",armstrong_list)
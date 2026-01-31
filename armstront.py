def is_armstrong(number):

    num = number
    n = 0
    temp = number

    while temp > 0:
        temp = temp // 10
        n += 1

    sum = 0
    temp = number
    while temp > 0:
        d = temp % 10
        power = 1
        count = 0
        while count < n:
            power = power * d
            count +=1
        sum += power
        temp = temp // 10

    if sum == num:
        print("True")
    else:
        print("False")

try:
    number = int(input("Enter Number: "))
    is_armstrong(number)
except ValueError:
    print("Enter Valid Number!")

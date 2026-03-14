# Function to calculate length of list manually
def list_length(arr):
    count = 0
    for x in arr:
        count += 1
    return count

# Function to calculate mean
def calc_mean(arr):
    total = 0
    n = list_length(arr)
    if n == 0:
        return 0
    i = 0
    while i < n:
        total += arr[i]
        i += 1
    return total / n

# Function to sort list (bubble sort)
def sort_list(arr):
    n = list_length(arr)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr

# Function to calculate median
def calc_median(arr):
    n = list_length(arr)
    if n == 0:
        return 0
    arr = sort_list(arr)
    mid = n // 2
    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2

# Function to calculate mode
def calc_mode(arr):
    freq = {}
    n = list_length(arr)
    i = 0
    while i < n:
        num = arr[i]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        i += 1

    max_count = 0
    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]

    mode_list = []
    for key in freq:
        if freq[key] == max_count:
            mode_list.append(key)

    # If all numbers unique
    if max_count == 1:
        return "No mode"
    # Otherwise return mode_list
    return mode_list

# Function to calculate range
def calc_range(arr):
    n = list_length(arr)
    if n == 0:
        return 0
    arr = sort_list(arr)
    return arr[n-1] - arr[0]

# Function to calculate standard deviation
def calc_std(arr):
    n = list_length(arr)
    if n == 0:
        return 0
    mean = calc_mean(arr)
    total = 0
    i = 0
    while i < n:
        diff = arr[i] - mean
        total += diff * diff
        i += 1
    variance = total / n

    guess = variance
    i = 0
    while i < 20:
        if guess == 0:
            break
        guess = (guess + variance / guess) / 2
        i += 1
    return guess



input_file = input("Enter input file: ")
output_file = input("Enter output file: ")

try:
    f = open(input_file, "r")
    data = f.read()
    f.close()
except FileNotFoundError:
    print("Error: File not found")
    exit()

nums = []
for part in data.replace('\n',' ').split(','):
    part = part.strip()
    if part:  # non-empty

        val = 0
        sign = 1
        idx = 0
        if part[0] == '-':
            sign = -1
            idx = 1
        while idx < list_length(part):
            val = val * 10 + (ord(part[idx]) - 48)
            idx += 1
        val *= sign
        nums.append(val)

# Calculate statistics
results = {}
results["Mean"] = round(calc_mean(nums), 2)
results["Median"] = calc_median(nums)
mode_res = calc_mode(nums)
if type(mode_res) == list:

    mode_str = ""
    idx = 0
    while idx < list_length(mode_res):
        if idx > 0:
            mode_str += ", "
        n = mode_res[idx]
        temp = ""
        if n == 0:
            temp = "0"
        else:
            if n < 0:
                temp = "-"
                n = -n
            digits = []
            while n > 0:
                digits.append(chr((n % 10) + 48))
                n = n // 10
            d = list_length(digits) - 1
            while d >= 0:
                temp += digits[d]
                d -= 1
        mode_str += temp
        idx += 1
    results["Mode"] = mode_str
else:
    results["Mode"] = mode_res

results["Range"] = calc_range(nums)
results["Standard Deviation"] = round(calc_std(nums), 2)

try:
    out = open(output_file, "w")
    for key in results:
        out.write(key + ": " + str(results[key]) + "\n")
    out.close()
    print("Statistics written to file successfully")
except:
    print("Error writing to file")
#Function for calculate average

#from string import digits


def calculate_average(marks):
    total = 0
    count = 0
    i = 0

    while i < 3:
        total += marks[i]
        count += 1
        i += 1
    return total/count

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

source_file = input("Enter file name: ")
output_file = input("Enter output file name: ")

try:
    source = open(source_file, "r")
    lines = source.read()
    source.close()

    stud_lines = []
    current_line = ""
    i = 0
    while i < len(lines):
        if lines[i] == "\n":
            stud_lines.append(current_line)
            current_line = ""
        else:
            current_line += lines[i]
        i = i + 1
    if current_line != "":
        stud_lines.append(current_line)

    destination = open(output_file, "w")
    idx = 0
    while idx < len(stud_lines):
        line = stud_lines[idx]
        idx = idx + 1
        if line == "":
            continue

        parts = []
        temp = ""
        j = 0
        while j < len(line):
            if line[j] == ",":
                parts.append(temp)
                temp = ""
            else:
                temp += line[j]
            j = j + 1
        parts.append(temp)

        if len(parts) != 4:
            continue
        name = parts[0]
        marks = []
        k = 1
        while k <= 3:
            try:
                val = 0
                num_str = parts[k]
                m = 0
                while m < len(num_str):
                    ch = num_str[m]

                    val = val * 10 + (ord(ch) - 48)
                    m = m + 1
                marks.append(val)
            except:
                marks = []
                break
            k = k + 1
        if len(marks) != 3:
            continue

        avg = calculate_average(marks)
        grd = grade(avg)

        avg_str = ""
        avg_int = int(avg)
        avg_frac = int((avg - avg_int) * 100 + 0.5)

        temp_avg = []
        if avg_int == 0:
            temp_avg.append("0")
        else:
            n = avg_int
            digits = []
            while n > 0:
                digits.append(chr((n % 10) + 48))
                n = n // 10
            d = len(digits) - 1
            while d >= 0:
                temp_avg.append(digits[d])
                d = d - 1
        temp_avg.append(".")
        if avg_frac < 10:
            temp_avg.append("0")
        if avg_frac > 10:
            temp_avg.append(chr((avg_frac // 10) + 48))
        temp_avg.append(chr((avg_frac % 10) + 48))
        for ch in temp_avg:
            avg_str += ch
        destination.write(name +","+avg_str+","+grd+"\n")

    destination.close()
    print(f"Student grade written to {output_file}")
except:
    print("Error: File not found or Invalid Data")
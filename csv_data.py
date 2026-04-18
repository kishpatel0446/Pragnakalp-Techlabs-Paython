def read_csv(file_path):
    data = []
    try:
        file = open(file_path, 'r')
        lines = file.readlines()
        file.close()

        for line in lines:
            parts = line.strip().split(',')

            if len(parts) != 4:
                continue

            name, age, salary, dept = parts

            try:
                age = int(age)
                salary = int(salary)
            except:
                continue

            data.append((name, age, salary, dept))
    except:
        pass

    return data

def filter_records(data):
    filtered = []

    for record in data:
        if record[1] > 25:
            filtered.append(record)

    return filtered

def group_by_department(data):

    dept_map = {}

    for name, age, salary, dept in data:
        if dept not in dept_map:
            dept_map[dept] = []
        dept_map[dept].append((name, age, salary))

    return dept_map

def calculate_statistics(dept_map):

    stats = []

    for dept in dept_map:
        employees = dept_map[dept]
        count = len(employees)

        total_salary = 0
        for emp in employees:
            total_salary += emp[2]

        avg_salary = total_salary // count if count > 0 else 0

        stats.append((dept, count, avg_salary))

    stats.sort(key=lambda x: x[1], reverse=True)

    return stats

def write_output(file_path, filtered, stats):

    file = open(file_path, 'w')

    file.write("Filtered Records (age > 25):\n")

    if filtered:
        for name, age, salary, dept in filtered:
            file.write(f"{name},{age},{salary},{dept}\n")
    else:
        file.write("None\n")

    file.write("\nDepartment Statistics:\n")

    if stats:
        for dept, count, avg in stats:
            file.write(f"{dept}: {count} employees, Average Salary: {avg}\n")
    else:
        file.write("No departments found\n")

    file.close()

def main():
    input_file = "csv_in.txt"
    output_file = "csv_op.txt"

    data = read_csv(input_file)
    filtered = filter_records(data)
    dept_map = group_by_department(filtered)
    stats = calculate_statistics(dept_map)

    write_output(output_file, filtered, stats)

main()
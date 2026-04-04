# Function to read subject file
def read_subject_file(filename):
    data = {}
    try:
        with open(filename, "r") as f:
            content = f.read().strip()
        if content == "":
            return data
        entries = content.split("|")
        for entry in entries:
            name, marks = entry.strip().split(",")
            data[name.strip()] = int(marks.strip())
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return data


# Combine all student data
def combine_data(subject_files):
    all_students = set()
    subject_data = {}
    for subject in subject_files:
        data = read_subject_file(subject)
        subject_data[subject] = data
        for student in data:
            all_students.add(student)
    return subject_data, all_students


# Calculate totals and averages
def calculate_results(subject_data, all_students):
    results = {}
    for student in all_students:
        total = 0
        count = 0
        for subject in subject_data:
            if student in subject_data[subject]:
                total += subject_data[subject][student]
                count += 1
        average = total / count if count != 0 else 0
        results[student] = (total, average)
    return results


# Calculate ranks
def calculate_ranks(results):
    sorted_list = sorted(results.items(), key=lambda x: x[1][0], reverse=True)
    ranks = {}
    rank = 1
    for i in range(len(sorted_list)):
        student = sorted_list[i][0]
        if i > 0 and sorted_list[i][1][0] < sorted_list[i-1][1][0]:
            rank = i + 1
        ranks[student] = rank
    return ranks


# Subject toppers
def subject_toppers(subject_data):
    toppers = {}
    for subject in subject_data:
        max_marks = -1
        topper_name = ""
        for student in subject_data[subject]:
            marks = subject_data[subject][student]
            if marks > max_marks:
                max_marks = marks
                topper_name = student
        toppers[subject] = (topper_name, max_marks)
    return toppers


# Display report
def display_report(results, ranks, toppers):
    print("\nStudent Report:")
    for student in results:
        total, avg = results[student]
        print(f"{student} - Total: {total}, Average: {avg}, Rank: {ranks[student]}")

    print("\nSubject Toppers:")
    for subject in toppers:
        name, marks = toppers[subject]
        subject_name = subject.replace(".txt", "")  # remove .txt for display
        print(f"{subject_name}: {name}({marks})")

def main():
    files_input = input("Enter subject file names (comma separated, e.g., Math.txt,Science.txt): ")
    subject_files = [f.strip() for f in files_input.split(",")]

    subject_data, all_students = combine_data(subject_files)
    results = calculate_results(subject_data, all_students)
    ranks = calculate_ranks(results)
    toppers = subject_toppers(subject_data)

    display_report(results, ranks, toppers)


main()
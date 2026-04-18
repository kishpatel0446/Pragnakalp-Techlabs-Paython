def read_correct_answers(file_path):
    try:
        file = open(file_path)
        line = file.read().strip()
        file.close()

        answers = line.split(':')[1].strip().split(',')
        return answers
    except:
        return []


def read_student_data(file_path):
    students = []
    try:
        file = open(file_path, 'r')
        lines = file.readlines()
        file.close()

        for line in lines:
            if ':' not in line:
                continue

            name_part, answers_part = line.strip().split(':')
            name = name_part.strip()
            answers = answers_part.strip().split(',')

            students.append((name, answers))
    except:
        pass

    return students


def calculate_score(student_answers, correct_answers):
    score = 0
    total = len(correct_answers)

    for i in range(total):
        if i < len(student_answers) and student_answers[i] == correct_answers[i]:
            score += 1

    percentage = (score / total) * 100 if total > 0 else 0
    status = "Pass" if percentage >= 60 else "Fail"

    return score, total, percentage, status


def generate_statistics(results):
    if len(results) == 0:
        return 0, 0

    total_percentage = 0
    pass_count = 0

    for result in results:
        total_percentage += result["percentage"]
        if result["status"] == "Pass":
            pass_count += 1

    avg = total_percentage / len(results)
    pass_rate = (pass_count / len(results)) * 100

    return avg, pass_rate


def write_report(output_file, results, avg, pass_rate):
    file = open(output_file, 'w')

    for result in results:
        file.write(
            f"{result['name']}: {result['score']}/{result['total']} "
            f"({result['percentage']:.0f}%) - {result['status']}\n"
        )

    file.write(f"\nClass Average: {avg:.0f}%\n")
    file.write(f"Pass Rate: {pass_rate:.0f}%\n")

    file.close()


def main():
    correct_answers = read_correct_answers("quiz_ans.txt")
    students = read_student_data("quiz_st.txt")

    results = []

    for name, answers in students:
        score, total, percentage, status = calculate_score(answers, correct_answers)

        results.append({
            "name": name,
            "score": score,
            "total": total,
            "percentage": percentage,
            "status": status
        })

    avg, pass_rate = generate_statistics(results)

    write_report("quiz_report.txt", results, avg, pass_rate)


main()
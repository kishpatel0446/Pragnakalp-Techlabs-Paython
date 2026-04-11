# Remove extra spaces
def remove_extra_spaces(text):
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        words = line.strip().split()
        cleaned_lines.append(" ".join(words))

    return "\n".join(cleaned_lines)


# Capitalize first letter of sentences
def capitalize_sentences(text):
    result = ""
    capitalize_next = True

    for ch in text:
        if capitalize_next and ch.isalpha():
            result += ch.upper()
            capitalize_next = False
        else:
            result += ch

        if ch in ".!?":
            capitalize_next = True

    return result


# Fix spacing after punctuation
def fix_punctuation_spacing(text):
    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in ".!?":
            # Ensure single space after punctuation
            j = i + 1
            while j < len(text) and text[j] == " ":
                j += 1
            if j < len(text):
                result += " "
            i = j - 1

        i += 1

    return result


# Break long lines
def break_long_lines(text, max_length=80):
    lines = text.split("\n")
    new_lines = []

    for line in lines:
        while len(line) > max_length:
            break_pos = line.rfind(" ", 0, max_length)
            if break_pos == -1:
                break_pos = max_length

            new_lines.append(line[:break_pos])
            line = line[break_pos:].strip()

        new_lines.append(line)

    return "\n".join(new_lines)


# Process file
def format_text(input_file, output_file):
    file = open(input_file, "r")
    content = file.read()
    file.close()

    # Edge case: empty file
    if content.strip() == "":
        file = open(output_file, "w")
        file.write("")
        file.close()
        return

    # Apply formatting steps
    content = remove_extra_spaces(content)
    content = fix_punctuation_spacing(content)
    content = capitalize_sentences(content)
    content = break_long_lines(content)

    file = open(output_file, "w")
    file.write(content)
    file.close()


# Main
def main():
    input_file = "text_formatter_in.txt"
    output_file = "text_formatter_op.txt"

    format_text(input_file, output_file)
    print("Formatted text written to text_formatter_op.txt")


main()
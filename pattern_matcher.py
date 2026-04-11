#Find Phone Numbers
def find_phone_numbers(text):
    phone_numbers = []
    words = text.split()

    for word in words:
        if len(word) == 12:
            if (word[3] == '-' and word[7] == '-' and word[:3].isdigit() and word[4:7].isdigit() and word[8:].isdigit()):
                phone_numbers.append(word)
    return phone_numbers

#Find Emails
def find_emails(text):
    emails = []
    words = text.split()
    for word in words:
        word_lower = word.lower()

        if "@" in word_lower and "." in word_lower:
            if word_lower.index("@") < word_lower.index("."):
                emails.append(word.strip(",."))
    return emails

#Find URLS
def find_urls(text):
    urls = []
    words = text.split()
    for word in words:
        word_lower = word.lower()
        if word_lower.startswith("http://") or word_lower.startswith("https://") or word_lower.startswith("www."):
            urls.append(word.strip(",."))
    return urls

#Match Pattern
def pattern_matcher(input_file, output_file):
    try:
        file = open(input_file, "r")
        text = file.read()
        file.close()
    except FileNotFoundError:
        print("File not found")
        return

    results = {
        "Phone Numbers": find_phone_numbers(text),
        "Emails": find_emails(text),
        "URLs": find_urls(text)
    }

    out = open(output_file, "w")

    for key in results:
        line = f"{key}: {results[key]}"
        print(line)
        out.write(line + "\n")

    out.close()

def main():
    input_file = input("Enter file name: ")
    output_file = input("Enter output file name: ")
    pattern_matcher(input_file, output_file)

main()
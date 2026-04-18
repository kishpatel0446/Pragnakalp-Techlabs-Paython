def read_file_content(file_path):
    try:
        file = open(file_path,'r')
        content = file.read()
        file.close()
        return content
    except:
        return None
    
def group_files_by_content(file_paths):
    content_map = {}
    for file_path in file_paths:
        content = read_file_content(file_path)

        if content is None:
            continue

        if content in content_map:
            content_map[content].append(file_path)
        else:
            content_map[content] = [file_path]
    return content_map

def find_duplicates(content_map):
    duplicate_groups = []
    unique_files = []

    for content in content_map:
        files = content_map[content]
        if len(files) > 1:
            duplicate_groups.append(files)
        else:
            unique_files.extend(files)
    return duplicate_groups, unique_files

def write_report(output_file, duplicate_groups, unique_files):
    file = open(output_file,'w')

    if duplicate_groups:
        for i in range(len(duplicate_groups)):
            file.write(f"Duplicate Group {i+1}:\n")
            file.write(",".join(duplicate_groups[i]) + "\n\n")
    else:
        file.write("No duplicates found \n\n")

    if unique_files:
        file.write("Unique Files:\n")
        file.write(",".join(unique_files))

    file.close()

def main():
    file_paths = ["du_1.txt", "du_2.txt", "du_3.txt"]

    content_map = group_files_by_content(file_paths)
    duplicate_groups, unique_files = find_duplicates(content_map)
    write_report("du_op.txt", duplicate_groups,unique_files)

main()
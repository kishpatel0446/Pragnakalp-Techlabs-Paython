import os
import sys

file_num = int(input("How many files do you want to merge?: "))

source_files = []
for i in range(file_num):
    fname = input(f"Enter source file {i+1}: ")
    source_files.append(fname)

destination_files = input("Enter destination file name: ")
try:
    dest = open(destination_files, "w")

    for source_file in source_files:
        dest.write(f"---Content from {source_file}---\n\n")

        if not os.path.exists(source_file):
            dest.write(f"(Error: {source_file} not found)\n\n")
            continue
        source = open(source_file, "r")
        lines = source.readlines()
        source.close()

        if lines:
            for line in lines:
                dest.write(line)
            dest.write("\n")
    dest.close()
    print(f"Files merged successfully into {destination_files}")

except Exception as e:
    print(f"An error occured: {e}")
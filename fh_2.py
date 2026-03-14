source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    import os
    if os.path.exists(destination_file):
        print("Destination file already exists")
    else:
        src = open(source_file, 'r')

        dest = open(destination_file, 'w')

        for line in src:
            dest.write(line)

        src.close()
        dest.close()

        print(f"Content Copied Successfully from {source_file} to {destination_file}")

except Exception as e:
    print(f"An error occured: {e}")
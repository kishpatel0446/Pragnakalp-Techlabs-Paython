#Fuctiopn to read contact from a file
def read_contacts(filename):

    contacts = []

    try:
        f = open(filename,"r")
        data = f.read()
        f.close()
    except:
        return contacts

    line = ""
    i = 0

    while True:
        try:
            ch = data[i]
        except:
            break

        if ch == "\n":
            contacts = contacts + [line]
            line = ""
        else:
            line = line + ch
        i = i + 1

    if line != "":
        contacts = contacts + [line]
    return contacts

#Function to write contacts
def write_contacts(filename, contacts):

    f = open(filename,"w")

    i = 0

    while True:
        try:
            line = contacts[i]
        except:
            break

        f.write(line + "\n")
        i = i + 1
    f.close()


#Function to extract name from contact
def get_name(line):

    name = ""
    i = 0

    while True:
        try:
            ch = line[i]
        except:
            break
        if ch == ":":
            break

        name += ch
        i = i + 1
    return name

def add_contact(filename):

    contact = input("Enter contact (name:phone:email): ")

    contacts = read_contacts(filename)

    name = get_name(contact)

    i = 0
    while True:
        try:
            line = contacts[i]
        except:
            break

        if get_name(line) == name:
            print("Duplicate name not allowed")
            return

        i = i + 1

    contacts = contacts + [contact]

    write_contacts(filename, contacts)

    print("Contact added successfully")

#Function to Search contact
def search_contact(filename):

    search_name = input("Enter Name to search: ")

    contacts = read_contacts(filename)

    found = 0

    i = 0
    while True:
        try:
            line = contacts[i]
        except:
            break

        if get_name(line) == search_name:
            part = ""
            parts = []
            j = 0

            while True:
                try:
                    ch = line[j]
                except:
                    break

                if ch == ":":
                    parts = parts + [part]
                    part = ""
                else:
                    part = part + ch
                j = j + 1

            parts = parts + [part]

            print("Name:", parts[0])
            print("Phone:", parts[1])
            print("Email:", parts[2])

            found = 1
            break
        i = i + 1
    if found == 0:
        print("Contact not found")

#Function to delete contacts
def delete_contact(filename):

    del_name = input("Enter Name to delete: ")

    contacts = read_contacts(filename)

    new_list = []
    deleted = 0

    i = 0
    while True:
        try:
            line = contacts[i]
        except:
            break

        if get_name(line) == del_name:
            deleted = 1
        else:
            new_list = new_list + [line]
        i = i + 1

        if deleted == 1:
            write_contacts(filename, new_list)
            print("Contact deleted successfully")
        else:
            print("Contact not found")

#Function to display all contacts
def display_contacts(filename):

    contacts = read_contacts(filename)
    i = 0
    while True:
        try:
            line = contacts[i]
        except:
            break
        print(line)
        i = i + 1


file_name = input("Enter file name: ")

while True:
    print("\n 1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n")
        add_contact(file_name)
    elif choice == "2":
        print("\n")
        search_contact(file_name)
    elif choice == "3":
        print("\n")
        delete_contact(file_name)
    elif choice == "4":
        print("\n")
        display_contacts(file_name)
    elif choice == "5":
        break

    else:
        print("Invalid choice")
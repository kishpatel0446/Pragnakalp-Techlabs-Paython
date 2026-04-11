#Take inventory file for input
from os import name


def load_inventory(filename):
    inventory = {}
    try:
        file = open(filename, "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue

            pid, name, qty, price = parts

            try:
                inventory[pid] = {
                    "name": name,
                    "quantity": int(qty),
                    "price": float(price),
                }
            except:
                continue
        file.close()

    except FileNotFoundError:
        print("Inventory file not found")

    return inventory

#Save Inventory
def save_inventory(filename,inventory):
    file = open(filename, "w")

    for pid in inventory:
        item = inventory[pid]
        line = f"{pid}, {item['name']}, {item['quantity']}, {item['price']}\n"
        file.write(line)
    file.close()

#Add Product
def add_product(inventory):
    data = input("Enter product (id,name,quantity,price): ")

    parts = data.split(",")
    if len(parts) != 4:
        print("Invalid product format")
        return
    pid, name, qty, price = parts

    if pid in inventory:
        print("Product already exists")
        return

    try:
        qty = int(qty)
        price = float(price)

        if qty < 0 or price < 0:
            print("Invalid price and quantity")
            return

        inventory[pid] = {
            "name": name,
            "quantity": qty,
            "price": price,
        }

        print("Product added successfully")

    except:
        print("Invalid product format")

#Update quantity
def update_quantity(inventory):
    pid = input("Enter product id: ")

    if pid not in inventory:
        print("Product not found")
        return
    try:
        new_qty = int(input("Enter new quantity: "))

        if new_qty < 0:
            print("Invalid quantity")
            return

        inventory[pid]["quantity"] = new_qty
        print(f"Quantity Updated. New stock: {new_qty}")
    except:
        print("Invalid quantity")

#Search Product

def search_product(inventory):
    choice = input("Search by Id (1) or by Name (2): ")

    if choice == "1":
        pid = input("Enter product id: ")
        if pid in inventory:
            item = inventory[pid]
            print(f"{pid}, {item['name']}, {item['quantity']}, {item['price']}")
        else:
            print("Product not found")

    elif choice == "2":
        name = input("Enter product name: ").lower()
        found = False

        for pid in inventory:
            if inventory[pid]["name"].lower() == name:
                item = inventory[pid]
                print(f"{pid},{item['name']},{item['quantity']},{item['price']}")
                found = True
        if not found:
            print("Product not found")
    else:
        print("Invalid choice")


#Calculate Total Inventory value
def calculate_total_value(inventory):
    total = 0
    for pid in inventory:
        item = inventory[pid]
        total += item["quantity"] * item["price"]
    return total

#Generate Low Stock Report
def low_stock_report(inventory,output_file):
    file = open(output_file, "w")

    print("Low Stock Products:")
    file.write("Low Stock Products:\n")

    for pid in inventory:
        item = inventory[pid]

        if item["quantity"] < 10:
            line = f"{pid}, {item['name']}, {item['quantity']}, {item['price']}"
            print(line)
            file.write(line + "\n")
    total = calculate_total_value(inventory)
    print(f"Total Inventory Value: {total}")
    file.write(f"Total Inventory Value:{total}\n")

    file.close()

# Main menu
def main():
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")

    inventory = load_inventory(input_file)

    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. Search Product")
        print("4. Total Inventory Value")
        print("5. Low Stock Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product(inventory)
            save_inventory(input_file, inventory)

        elif choice == "2":
            update_quantity(inventory)
            save_inventory(input_file, inventory)

        elif choice == "3":
            search_product(inventory)

        elif choice == "4":
            total = calculate_total_value(inventory)
            print(f"Total Inventory Value: {total}")

        elif choice == "5":
            low_stock_report(inventory, output_file)

        elif choice == "6":
            save_inventory(input_file, inventory)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice!")


# Run program
main()
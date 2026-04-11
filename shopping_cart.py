# Parse Single Line
def parse_line(line):
    try:
        parts = line.strip().split(",")
        if len(parts) != 4:
            return None

        item = parts[0].strip()
        quantity = int(parts[1].strip())
        price = float(parts[2].strip())
        discount = float(parts[3].strip())

        if quantity <= 0 or price < 0 or discount < 0 or discount > 100:
            return None

        return {
            "item": item,
            "quantity": quantity,
            "price": price,
            "discount": discount
        }
    except:
        return None


# Calculate Item Total
def calculate_item(data):
    total_price = data["quantity"] * data["price"]
    discount_amount = (total_price * data["discount"]) / 100
    subtotal = total_price - discount_amount

    return total_price, discount_amount, subtotal


#Process Cart
def process_cart(input_file, output_file):
    items = []

    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        data = parse_line(line)
        if data:
            items.append(data)

    grand_subtotal = 0

    file = open(output_file, "w")

    for item in items:
        total_price, discount_amount, subtotal = calculate_item(item)
        grand_subtotal += subtotal

        file.write(f"Item: {item['item']}\n")
        file.write(f"Quantity: {item['quantity']}\n")
        file.write(f"Price: {total_price}\n")
        file.write(f"Discount ({item['discount']}%): -{discount_amount}\n")
        file.write(f"Subtotal: {subtotal}\n\n")

    tax = grand_subtotal * 0.18
    final_total = grand_subtotal + tax

    file.write(f"Grand Total: {grand_subtotal}\n")
    file.write(f"Tax (18%): {tax}\n")
    file.write(f"Final Total: {final_total}\n")

    file.close()


def main():
    input_file = "shopping_cart_in.txt"
    output_file = "shopping_cart_op.txt"

    process_cart(input_file, output_file)
    print("Bill generated successfully in shopping_cart_op.txt")


main()
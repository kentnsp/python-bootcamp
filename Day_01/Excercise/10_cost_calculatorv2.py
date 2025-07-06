item_count = int(input("Enter item count: "))
total = 0


for item in range(item_count):
    item_price = int(input("Enter item price: "))
    item_qty = int(input("Enter item qty: "))
    total = item_price * item_qty

    total += total

    print(total)
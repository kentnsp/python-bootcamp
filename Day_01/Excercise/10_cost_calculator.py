item_1_price = int(input("Please input your item 1 price: "))
item_2_price = int(input("Please input your item 2 price: "))
item_3_price = int(input("Please input your item 3 price: "))

item_1_qty = int(input("Please input qty of your item 1: "))
item_2_qty = int(input("Please input qty of your item 2: "))
item_3_qty = int(input("Please input qty of your item 3: "))

total = (
        (item_1_price * item_1_qty)
        + (item_2_price * item_2_qty)
        + (item_3_price * item_3_qty)
         )

print("Total QTY is: " + str(total))

items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"
item_to_skip = "spam"

for item in items:
    if item == item_to_find:
        print("Found",item)
        break

for item in items:
    if item == item_to_skip:
        continue
    else:
        print(item, end = " ")
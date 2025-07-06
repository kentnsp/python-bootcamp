example =[1,3,3,5,4]

example.append(999)

print(example)

other_example = [12,52,55]

example.extend(other_example)

print(example)

example.insert(0, 121212)

print(example)

print(example.index(5))

#example.remove(5)

item_to_remove = 5
if item_to_remove in example:
    example.remove(item_to_remove)
else:
    print('non existing')


print(example)

removed_item = example.pop(0)
print('POP index 0', example)
print('Removed item: ', removed_item)

print(example[2])
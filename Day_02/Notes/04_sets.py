example = {1,3,4,5,5}
orig_length = len(example)
print('initial', example)
print('orig length', orig_length)

example.add(99)
print('Add', example)

example.discard(5)
print('Discarded 5', example)
new_length = len(example)
print('new length', new_length)

#random delete for pop
return_value = example.pop()
print('random value POP: ', return_value)
print(example)
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print('Union 1', set1.union(set2))
print('Union 2', set1 | set2)

print('Intersection 1', set1.intersection(set2))
print('Intersection 2',set1 & set2)

print('Difference 1 - order sensitive', set1.difference(set2))
print('Difference 2 order sensitive', set2 - set1)

print('Symmetric diff 1', set1.symmetric_difference(set2))
print('Symmetric diff 2', set1 ^ set2)
set_1 = {1,2,3,4,5}
set_2 = {3,4,5,6,54,6,5,11,11}
f = set_1.isdisjoint(set_2)
print(f)

print(set_1 == set_2)

print(set_1.issubset(set_2))

print(set_1.issuperset(set_2))

print(set_1.union(set_2))

print(set_1.intersection(set_2))

print(set_1.difference(set_2))

print(set_1.symmetric_difference(set_2))

print(set_1.copy)
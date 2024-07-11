
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 60)

s2 = {1, 2, 3, 4, 5.6, 6.2, 7.1, 'eight', 'nine', 'ten', 11+0j, 12-2j, True, False}
print(f"s2 :{s2}")
print(type(s2))
print("-" * 60)

s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))
print("-" * 60)

# add new values into a set - add, update
s1 = {1, 2, 3}
print(f"s1 :{s1}")

s1.add(1)
s1.add(3)
s1.add(4)
s1.add(2)
s1.add(5)

print(f"s1 :{s1}")

print("-" * 60)
# update
s1.update([1, 2, 3])
s1.update([5, 6, 7])
s1.update([4, 5, 6])
s1.update([8, 9, 10])
s1.update([7, 8, 9])

print(f"s1 :{s1}")

print("-" * 60)
# delete values from a set - pop, remove, discard
print(f"s1 :{s1}")

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

print("-" * 60)
# remove

s1.remove(8)
s1.remove(4)

# s1.remove(1)
print(f"s1 :{s1}")
print("-" * 60)
# discard

s1.discard(6)
s1.discard(10)

s1.discard(1)           # no error though we do not have 1 in the set
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)
print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 60)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f"A symmetric_difference B :{A ^ B}")
print(f"B symmetric_difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# Frozenset - immutable
fs = frozenset([1, 2, 3, 4, 5])
print(f"frozenset :{fs}")
print(type(fs))

print("-" * 60)
l1 = [1, 2, 3, 3, 1, 1,2,3, 1,1,1, 2, 4,2, 3, 4, 5, 1, 2, 3,4, 4, 5, 5, 5, 1, 2, 3,4,5]
print(f"l1 :{l1}")

# get unique values from l1
res = set(l1)
# print(f"res :{res}")

res = list(res)
print(f"res :{res}")

print("-" * 60)
s1 = set(range(1, 11))
print(f"s1 :{s1}")
print(type(s1))

for i in s1:
    print(i, end=" ")
print()


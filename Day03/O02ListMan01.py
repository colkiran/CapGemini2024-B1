
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4.1, 5.2, 6.8, 'seven', 'eight', 'nine', 10+2j, 11-3j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD - Create, Read, Update, Delete
# create
l1 = list(range(1, 11))
print(f"l1 :{l1}")

print("-" * 60)
# read
print(f"l1[2]  :{l1[2]}")
print(f"l1[0]  :{l1[0]}")
print(f"l1[-1] :{l1[-1]}")

# iterate
for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

for j in l1:
    print(j, end=" ")
print()

print("-" * 60)
# update - modify, add new element
print(f"l1 :{l1}")

# modify
l1[3] = 400
l1[8] = 'Nine'

print(f"l1 :{l1}")

# insert
l1[4] = 4.5
l1[6] = 5.5
# l1[10] = 'eleven'

print(f"l1 :{l1}")

print("-" * 60)
# delete

del l1[3]
del l1[6]

print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))

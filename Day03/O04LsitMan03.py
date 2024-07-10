
print("count".center(60, "-"))
l1 = [1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

print(f"count of 1 :{l1.count(1)}")
print(f"count of 2 :{l1.count(2)}")
print(f"count of 3 :{l1.count(3)}")
print(f"count of 5 :{l1.count(5)}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")
# copy the elements of l1 into l2
l2 = l1             # shallow copy - copies the data with address

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")


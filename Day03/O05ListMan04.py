"""
copy - module
deepcopy - function

sort    - sort will sort the original list
sorted  - will take copy of the list and gets sorted
"""
print("sort".center(60, "-"))
l1 = [6, 9, 1, 7, 10, 4, 2, 5, 3, 8]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

# l1.sort()
# print(f"l1 :{l1}")

print("-" * 60)
l1 = [6, 'zebra', 'apple', 9, 'blue', 'yellow', 1, 'white', 'green', 7, 'violet', 'pink', 10, 'maroon', 'cat', 4, 'orange', 'xray', 2, 'egg', 'fish', 5, 'dog', 'hen', 3, 8, 190, 1832, 29, 275, 2189]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 60)
idx = 0
for i in range(0, len(res)):
    if type(res[i]) == int:
       idx = i
       break

# print(res[idx])
print(res[:idx-1] + sorted(res[idx:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'delhi', 'ooty', 'bangalore', 'mumbai', 'vishakapatnam', 'chennai', 'hyderabad', 'pune']

print(f"cities :{cities}")
# sort the cities based on the no of characters

print("-" * 60)
res = sorted(cities, key=len)
print(f"res :{res}")

print("reversed".center(60, "-"))
l1 = [6, 9, 1, 7, 10, 4, 2, 5, 3, 8]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")


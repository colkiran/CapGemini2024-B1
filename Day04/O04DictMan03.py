
print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")

# convert the list into a dictionary (list elements will become keys)
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print(f"setdefault".center(60, "-"))
emp = {'ename': 'Jack', 'age': 32, 'desig': 'MGR', 'dept': 'Finance', 'location': 'NYK'}
print(f"emp :{emp}")

# setdefault will allow us to add new key value into the dictionary
emp.setdefault('ename', 'Slater')
emp.setdefault('age',  40)

emp.setdefault('gender', 'Male')
emp.setdefault('sal', 4500)
emp.setdefault('country', 'USA')

print("-" * 60)
print(f"emp :{emp}")

print("pop".center(60, "-"))
emp2 = {'ename': 'Linda', 'age': 36, 'desig': 'MGR', 'dept': 'Finance', 'location': 'DAL'}
print(f"emp2 :{emp2}")

res = emp2.pop('age')
print(f"res :{res}")

res = emp2.pop('dept')
print(f"res :{res}")

print(f"emp2 :{emp2}")

print("popitem".center(60, "-"))
emp2 = {'ename': 'Linda', 'age': 36, 'desig': 'MGR', 'dept': 'Finance', 'location': 'DAL'}
print(f"emp2 :{emp2}")

res = emp2.popitem()
print(f"res :{res}")

res = emp2.popitem()
print(f"res :{res}")

print(f"emp2 :{emp2}")

print("clear".center(60, "-"))
emp2 = {'ename': 'Linda', 'age': 36, 'desig': 'MGR', 'dept': 'Finance', 'location': 'DAL'}

print(f"emp2 :{emp2}")
emp2.clear()

print(f"emp2 :{emp2}")

print(f"update".center(60, "-"))
emp2 = {'ename': 'Linda', 'age': 36, 'desig': 'MGR', 'location': 'DAL'}
emp3 = {'ename': 'Peter', 'age': 25, 'desig': 'SE', 'dept': 'IT'}

print(f"emp2 :{emp2}")
print("-" * 60)

print(f"emp3 :{emp3}")
print("-" * 60)

# update the values of emp2 with the values of emp3
emp2.update(emp3)
print(f"emp2 :{emp2}")

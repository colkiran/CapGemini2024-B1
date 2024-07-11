
print("keys".center(60, "-"))
emp = {'ename': 'Jack', 'age': 32, 'desig': 'MGR', 'dept': 'Finance', 'location': 'NYK'}
print(f"emp :{emp}")

print("-" * 60)
k = emp.keys()
print(f"keys :{k}")

print("-" * 60)
for k in emp.keys():
    print(k, "=>", emp[k])

print("values".center(60, "-"))
print(f"emp :{emp}")

print("-" * 60)
v = emp.values()
print(f"Values :{v}")

print("items".center(60, "-"))
# its a combination of keys and values functions

print(f"emp :{emp}")

print("-" * 60)
for k, v in emp.items():
    print(k, "=>", v)

print("-" * 60)

emp = {
    'emp1': {'ename': 'Keneth', 'age': 30, 'desig': 'TL', 'dept': 'MKT', 'location': 'LA'},
    'emp2': {'ename': 'Linda', 'age': 36, 'desig': 'MGR', 'dept': 'Finance', 'location': 'DAL'},
    'emp3': {'ename': 'Peter', 'age': 25, 'desig': 'SE', 'dept': 'IT', 'location': 'CHI'}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print("-" * 60)

print(f"emp2 :{emp['emp2']}")
print("-" * 60)

print(f"emp3 :{emp['emp3']}")
print("-" * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("get".center(60, "-"))
emp = {'ename': 'Keneth', 'age': 30, 'desig': 'TL', 'dept': 'MKT', 'location': 'LA'}
print(f"emp :{emp}")

print(f"Name  :{emp.get('ename', 'Invalid Key, Please enter a valid key')}")
print(f"Desig :{emp.get('desg', 'Invalid Key, Please enter a valid key')}")
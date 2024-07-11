
print("copy".center(60, "-"))
emp1 = {'ename': 'Linda', 'age': 36, 'desig': 'MGR', 'dept': 'Finance'}
print(f"emp1 before :{emp1}")

# copy emp1 to emp2
emp2 = emp1         # shallow copy - copy data with address
print(f"emp2 before :{emp2}")

emp2['salary'] = 5000
emp2['loc'] = 'DAL'
print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)
print("=" * 60)
emp3 = {'ename': 'Keneth', 'age': 30, 'desig': 'TL', 'dept': 'MKT'}
print(f"emp3 before :{emp3}")

# copy emp3 to emp4
emp4 = emp3.copy()      # deep copy
print(f"emp4 before :{emp4}")

emp4['gender'] = 'Male'
emp4['loc'] = 'LA'

print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("=" * 60)
print("=" * 60)

emp5 = {'ename': 'Keneth', 'age': 45, 'desig': {'hp': 'BDE', 'IBM': 'BDM', 'CTS': 'AGM'}, 'dept': 'MKT'}
print(f"emp5 before :{emp5}")

# copy emp5 to emp6
emp6 = emp5.copy()      # deep copy
print(f"emp6 before: {emp6}")

emp6['desig']['TCS'] = 'GM'
emp6['desig']['Dell'] = 'director'
print(f"emp6 after :{emp6}")
print(f"emp5 after :{emp5}")

print("=" * 60)
print("=" * 60)

emp7 = {'ename': 'Keneth', 'age': 45, 'desig': {'hp': 'BDE', 'IBM': 'BDM', 'CTS': 'AGM'}, 'dept': 'MKT'}
print(f"emp7 before :{emp7}")

from copy import deepcopy
# copy emp7 into emp8

emp8 = deepcopy(emp7)
print(f"emp8 before :{emp8}")

emp8['desig']['TCS'] = 'GM'
emp8['desig']['Dell'] = 'director'

print(f"emp8 after :{emp8}")
print(f"emp7 after :{emp7}")


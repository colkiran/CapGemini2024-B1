
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))
print("-" * 60)

d2 = {'name': 'sachin', 'age': 32, 'runs': 145, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))
print("-" * 60)

d3 = dict([('name', 'rahul'), ('age', 30), ('runs', 85), ('oppn', 'SA')])
print(f"d3 :{d3}")
print(type(d3))
print("-" * 60)

# print(f"ord('a') :{ord('a')}")
d4 = dict(sname = 'John', age=13, cls='8th', school='NPS')
print(f"d4 :{d4}")
print(type(d4))
print("-" * 60)

# CRUD  -  Create, Read, Update, Delete

# create
player = {'name': 'Sachin', 'age': 34, 'runs': 98, 'oppn': 'Nzl'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")
print(f"Team :{player['oppn']}")

print("-" * 60)
for i in player:
    print(i + " => " + str(player[i]))
print()

print("-" * 60)
# update
print(f"player :{player}")

# modify
player['name'] = "Tendulkar"
player['runs'] = 120

# add new key value
player['year'] = 2003
player['venue'] = 'Auckland'

print(f"player :{player}")

print("-" * 60)
# delete

del player['age']
del player['runs']

print(f"player :{player}")

print("-" * 60)
print(dir(player))


def add(x, y):
    return x + y

a = add

print(a(30, 40))

print("-"  * 60)

x = lambda a, b: a + b

print(x(100, 200))

print("-"  * 60)
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x: x ** 2, l1))
print(f"squares :{squares}")

print("-"  * 60)
months = ['dec', 'oct', 'aug', 'nov', 'sep', 'jan', 'apr', 'feb', 'may', 'jun', 'mar', 'jul']

print(f"months :{months}")

print("-"  * 60)
from calendar import month_abbr
print(list(month_abbr))
print("-"  * 60)

sortedMonths = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(sortedMonths)

print("-"  * 60)
# filters - expression should return a true or a false
l1 = list(range(1, 31))
print(f"l1 :{l1}")

res = list(filter(lambda x : x % 3 == 0, l1))
print(f"res :{res}")

sentence = "the quick  brown fox jumps over the lazy dog"

res = list(filter(lambda x: x != 'the', sentence.split()))
print(f"res :{res}")

res = list(filter(lambda x: len(x) > 3, sentence.split()))
print(f"res :{res}")

print("-"  * 60)
# reduce - list => single value
l1 = [3, 6, 2, 8, 9, 5, 10]
print(f"l1 :{l1}")

from functools import reduce

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

l1 = list(range(1, 11))
res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

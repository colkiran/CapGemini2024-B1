
l1 = [1, 2, 3]
print(F"l1 :{l1}")
print(type(l1))

l1.extend([4, 5, 6])
print("-" * 60)


def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# Variable length arguments

def prodAll(*numbers):
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extract_details(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extract_details(name='Steve', cls='8th', age=13, school='DPS')

print("-" * 60)

def fun():
    "this is a doc string"
    # this is a comment
    print("hello world")

fun()
print(fun.__doc__)      # __doc__ = double underscore = dunder_doc

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    1. if x and y are integers then the function will return the sum of numbers
    2. if x and y are strings then the function will concatenate the strings
    3. if the x and y are of two different data types then it will throw an error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello", "world"))
# print(fun1(10, 'Hello'))

print("-" * 60)
help(fun1)

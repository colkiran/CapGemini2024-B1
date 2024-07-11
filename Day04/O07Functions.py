
def greet():
    print("Greetings Mr.Jordan, Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event........")


# city default argument and gname is non default argument

"""
def greetGstCty(gname, city="Brooklyn", x):  
invalid function defnition because a non default argument follows a default argument

def greetGstCty(gname, x,  city="Brooklyn"):
valid function defnition as the non default argument is added before a default argument
"""

def greetGstCty(gname, city="Brooklyn"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")

greet()
print("-" * 60)

greetGst('Jordan')
greetGst('Shaquille')

print("-" * 60)
greetGstCty('Jordan')
greetGstCty('Shaquille')
greetGstCty("Johnson", "Lansing")

print("-" * 60)
# function can return a value

def multiplyMe(x, y):
    return x * y

print(f"The product of 5, 6 is :{multiplyMe(5, 6)}")

print("-" * 60)
# recursive calls

# def fun(x):
#     print(x)
#     fun(x-1)
#
# fun(10)

